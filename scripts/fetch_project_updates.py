#!/usr/bin/env python3
"""
Fetch recent updates (releases, PRs, commits) from projects in data/projects.yml.

Uses httpx with asyncio for concurrent GitHub API requests (20-50x faster than
sequential gh CLI subprocess spawning).

Requirements:
    - GitHub token: either GITHUB_TOKEN env var or `gh auth token`
    - pip install pyyaml httpx

Usage:
    python3 scripts/fetch_project_updates.py --since-days 7
    python3 scripts/fetch_project_updates.py --since-days 1 --fresh
    python3 scripts/fetch_project_updates.py --projects "Damus,Amethyst"
    python3 scripts/fetch_project_updates.py --concurrency 40
"""

import argparse
import asyncio
import json
import os
import re
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print("Missing pyyaml. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

try:
    import httpx
except ImportError:
    print("Missing httpx. Install with: pip install httpx", file=sys.stderr)
    sys.exit(1)

DEFAULT_BODY_MAX_LENGTH = 0
PROJECT_ROOT = Path(__file__).parent.parent
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "data" / "project_updates"
GITHUB_API_BASE = "https://api.github.com"
DEFAULT_CONCURRENCY = 25
RATE_LIMIT_BUFFER = 100  # slow down when fewer than this many requests remain

BOT_PATTERNS = [
    r".*\[bot\]$",
    r"^dependabot$",
    r"^weblate$",
    r"^allcontributors$",
]


# =============================================================================
# Shared helpers (unchanged logic)
# =============================================================================


def parse_github_repo(repo_url: str) -> Optional[tuple[str, str]]:
    if not repo_url:
        return None
    patterns = [
        r"https?://github\.com/([^/]+)/([^/\.]+?)(?:\.git)?/?$",
        r"https?://github\.com/([^/]+)/([^/]+?)/?$",
    ]
    for pattern in patterns:
        match = re.match(pattern, repo_url)
        if match:
            owner, repo = match.groups()
            if repo and repo not in ["", "."]:
                return (owner, repo.rstrip("/"))
    return None


def is_bot_user(username: str) -> bool:
    if not username:
        return False
    username_lower = username.lower()
    return any(re.match(p, username_lower) for p in BOT_PATTERNS)


def truncate_body(text: str, max_length: int = DEFAULT_BODY_MAX_LENGTH) -> str:
    if not text or max_length == 0:
        return text or ""
    if len(text) <= max_length:
        return text
    return text[:max_length].rsplit(" ", 1)[0] + "..."


# =============================================================================
# GitHub token acquisition
# =============================================================================


def get_github_token() -> str:
    """Get GitHub token from env var or gh CLI (single subprocess call)."""
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token

    try:
        result = subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    print(
        "Error: No GitHub token found. Set GITHUB_TOKEN env var or install gh CLI.",
        file=sys.stderr,
    )
    sys.exit(1)


# =============================================================================
# Rate-limit-aware async HTTP client
# =============================================================================


class GitHubClient:
    """Async GitHub API client with rate limit awareness and concurrency control."""

    def __init__(
        self, token: str, concurrency: int = DEFAULT_CONCURRENCY, verbose: bool = False
    ):
        self.token = token
        self.verbose = verbose
        self.semaphore = asyncio.Semaphore(concurrency)
        self.rate_limit_remaining: Optional[int] = None
        self.rate_limit_reset: Optional[float] = None
        self._rate_lock = asyncio.Lock()
        self.request_count = 0
        self.client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        self.client = httpx.AsyncClient(
            base_url=GITHUB_API_BASE,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            timeout=httpx.Timeout(30.0, connect=10.0),
            follow_redirects=True,
            limits=httpx.Limits(
                max_connections=100,
                max_keepalive_connections=50,
            ),
        )
        return self

    async def __aexit__(self, *args):
        if self.client:
            await self.client.aclose()

    async def _check_rate_limit(self, headers: httpx.Headers):
        """Update rate limit state from response headers."""
        remaining = headers.get("x-ratelimit-remaining")
        reset = headers.get("x-ratelimit-reset")

        if remaining is not None:
            async with self._rate_lock:
                self.rate_limit_remaining = int(remaining)
                if reset is not None:
                    self.rate_limit_reset = float(reset)

    async def _maybe_throttle(self):
        """If rate limit is getting low, slow down."""
        async with self._rate_lock:
            remaining = self.rate_limit_remaining
            reset_time = self.rate_limit_reset

        if remaining is not None and remaining < RATE_LIMIT_BUFFER:
            if reset_time:
                wait = max(0, reset_time - time.time()) + 1
                if self.verbose:
                    print(
                        f"  Rate limit low ({remaining} remaining), "
                        f"sleeping {wait:.0f}s until reset...",
                        file=sys.stderr,
                    )
                await asyncio.sleep(wait)

    async def get(self, endpoint: str) -> Optional[httpx.Response]:
        """Make a GET request with concurrency control and rate limit handling."""
        await self._maybe_throttle()

        async with self.semaphore:
            self.request_count += 1
            try:
                resp = await self.client.get(endpoint)
            except (
                httpx.TimeoutException,
                httpx.ConnectError,
                httpx.RemoteProtocolError,
            ) as e:
                if self.verbose:
                    print(
                        f"  Warning: Request failed for {endpoint}: {e}",
                        file=sys.stderr,
                    )
                return None

            await self._check_rate_limit(resp.headers)

            if resp.status_code == 404:
                return resp  # caller handles 404 as empty
            if resp.status_code == 403:
                # Rate limited - wait and retry once
                reset = resp.headers.get("x-ratelimit-reset")
                if reset:
                    wait = max(0, float(reset) - time.time()) + 1
                    if self.verbose:
                        print(
                            f"  Rate limited! Sleeping {wait:.0f}s...",
                            file=sys.stderr,
                        )
                    await asyncio.sleep(wait)
                    try:
                        resp = await self.client.get(endpoint)
                    except (
                        httpx.TimeoutException,
                        httpx.ConnectError,
                        httpx.RemoteProtocolError,
                    ):
                        return None
                    await self._check_rate_limit(resp.headers)
                else:
                    if self.verbose:
                        print(
                            f"  Warning: 403 for {endpoint} (no reset header)",
                            file=sys.stderr,
                        )
                    return None

            if resp.status_code >= 400:
                if self.verbose:
                    print(
                        f"  Warning: HTTP {resp.status_code} for {endpoint}",
                        file=sys.stderr,
                    )
                return None

            return resp

    async def get_json(self, endpoint: str) -> Optional[list | dict]:
        """GET and parse JSON, returning None on failure."""
        resp = await self.get(endpoint)
        if resp is None:
            return None
        if resp.status_code == 404:
            return []
        try:
            return resp.json()
        except (json.JSONDecodeError, ValueError):
            return None

    async def get_paginated(
        self, endpoint: str, since_dt: Optional[datetime] = None, stop_check=None
    ) -> list:
        """
        Fetch all pages from a paginated endpoint with early termination.

        stop_check: callable(item) -> bool. If it returns True for an item,
                    stop processing that item AND stop paginating.
        """
        results = []
        url = endpoint

        while url:
            resp = await self.get(url)
            if resp is None:
                break
            if resp.status_code == 404:
                break

            try:
                data = resp.json()
            except (json.JSONDecodeError, ValueError):
                break

            if not data or not isinstance(data, list):
                break

            should_stop = False
            for item in data:
                if stop_check and stop_check(item):
                    should_stop = True
                    break
                results.append(item)

            if should_stop:
                break

            # Parse Link header for next page
            url = self._parse_next_link(resp.headers.get("link", ""))

        return results

    @staticmethod
    def _parse_next_link(link_header: str) -> Optional[str]:
        """Parse 'next' URL from GitHub Link header."""
        if not link_header:
            return None
        for part in link_header.split(","):
            if 'rel="next"' in part:
                match = re.search(r"<([^>]+)>", part)
                if match:
                    url = match.group(1)
                    # Strip base URL to use relative paths with httpx base_url
                    if url.startswith(GITHUB_API_BASE + "/"):
                        return url[len(GITHUB_API_BASE) + 1 :]
                    elif url.startswith(GITHUB_API_BASE):
                        return url[len(GITHUB_API_BASE) :]
                    return url
        return None


# =============================================================================
# Data Fetching Functions (async, same output format as original)
# =============================================================================


async def fetch_releases(
    client: GitHubClient, owner: str, repo: str, since: Optional[str] = None
) -> list[dict]:
    since_dt = datetime.fromisoformat(since.replace("Z", "+00:00")) if since else None

    def stop_check(r):
        if r.get("draft"):
            return False  # skip drafts but don't stop
        published_at = r.get("published_at")
        if since_dt and published_at:
            pub_dt = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
            if pub_dt < since_dt:
                return True  # stop paginating
        return False

    endpoint = f"/repos/{owner}/{repo}/releases?per_page=100"
    results = []
    url = endpoint

    while url:
        resp = await client.get(url)
        if resp is None:
            break
        if resp.status_code == 404:
            break

        try:
            data = resp.json()
        except (json.JSONDecodeError, ValueError):
            break

        if not data or not isinstance(data, list):
            break

        stop = False
        for r in data:
            if r.get("draft"):
                continue
            published_at = r.get("published_at")
            if since_dt and published_at:
                pub_dt = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
                if pub_dt < since_dt:
                    stop = True
                    break
            results.append(
                {
                    "id": r["id"],
                    "tag": r["tag_name"],
                    "name": r.get("name") or r["tag_name"],
                    "published_at": published_at,
                    "url": r["html_url"],
                    "body": truncate_body(r.get("body") or ""),
                    "prerelease": r.get("prerelease", False),
                    "author": r.get("author", {}).get("login", "unknown"),
                }
            )

        if stop:
            break
        url = client._parse_next_link(resp.headers.get("link", ""))

    return results


async def fetch_merged_prs(
    client: GitHubClient, owner: str, repo: str, since: Optional[str] = None
) -> list[dict]:
    since_dt = datetime.fromisoformat(since.replace("Z", "+00:00")) if since else None
    endpoint = f"/repos/{owner}/{repo}/pulls?state=closed&sort=updated&direction=desc&per_page=100"
    results = []
    url = endpoint

    while url:
        resp = await client.get(url)
        if resp is None:
            break
        if resp.status_code == 404:
            break

        try:
            data = resp.json()
        except (json.JSONDecodeError, ValueError):
            break

        if not data or not isinstance(data, list):
            break

        past_range = False
        for pr in data:
            if not pr.get("merged_at"):
                continue
            author = pr.get("user", {}).get("login", "")
            if is_bot_user(author):
                continue
            merged_at = pr["merged_at"]
            if since_dt:
                merged_dt = datetime.fromisoformat(merged_at.replace("Z", "+00:00"))
                if merged_dt < since_dt:
                    updated_at = pr.get("updated_at", merged_at)
                    updated_dt = datetime.fromisoformat(
                        updated_at.replace("Z", "+00:00")
                    )
                    if updated_dt < since_dt:
                        past_range = True
                        break
                    continue
            labels = [label["name"] for label in pr.get("labels", [])]
            results.append(
                {
                    "id": pr["id"],
                    "number": pr["number"],
                    "title": pr["title"],
                    "body": truncate_body(pr.get("body") or ""),
                    "author": author,
                    "merged_at": merged_at,
                    "url": pr["html_url"],
                    "labels": labels,
                }
            )

        if past_range:
            break
        url = client._parse_next_link(resp.headers.get("link", ""))

    return results


async def fetch_open_prs(
    client: GitHubClient, owner: str, repo: str, since: Optional[str] = None
) -> list[dict]:
    since_dt = datetime.fromisoformat(since.replace("Z", "+00:00")) if since else None
    endpoint = f"/repos/{owner}/{repo}/pulls?state=open&sort=created&direction=desc&per_page=100"
    results = []
    url = endpoint

    while url:
        resp = await client.get(url)
        if resp is None:
            break
        if resp.status_code == 404:
            break

        try:
            data = resp.json()
        except (json.JSONDecodeError, ValueError):
            break

        if not data or not isinstance(data, list):
            break

        past_range = False
        for pr in data:
            author = pr.get("user", {}).get("login", "")
            if is_bot_user(author):
                continue
            created_at = pr.get("created_at")
            if since_dt and created_at:
                created_dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
                if created_dt < since_dt:
                    past_range = True
                    break
            labels = [label["name"] for label in pr.get("labels", [])]
            results.append(
                {
                    "id": pr["id"],
                    "number": pr["number"],
                    "title": pr["title"],
                    "body": truncate_body(pr.get("body") or ""),
                    "author": author,
                    "opened_at": created_at,
                    "url": pr["html_url"],
                    "labels": labels,
                    "draft": pr.get("draft", False),
                }
            )

        if past_range:
            break
        url = client._parse_next_link(resp.headers.get("link", ""))

    return results


async def fetch_commits(
    client: GitHubClient,
    owner: str,
    repo: str,
    since: Optional[str] = None,
    branch: Optional[str] = None,
) -> list[dict]:
    if not branch:
        repo_data = await client.get_json(f"/repos/{owner}/{repo}")
        branch = (
            (repo_data or {}).get("default_branch", "main")
            if isinstance(repo_data, dict)
            else "main"
        )

    params = f"sha={branch}&per_page=100"
    if since:
        params += f"&since={since}"
    endpoint = f"/repos/{owner}/{repo}/commits?{params}"
    results = []
    url = endpoint

    while url:
        resp = await client.get(url)
        if resp is None:
            break
        if resp.status_code == 404:
            break

        try:
            data = resp.json()
        except (json.JSONDecodeError, ValueError):
            break

        if not data or not isinstance(data, list):
            break

        for c in data:
            commit_data = c.get("commit", {})
            author_data = commit_data.get("author", {})
            message = commit_data.get("message", "")
            message_summary = message.split("\n")[0] if message else ""
            results.append(
                {
                    "sha": c.get("sha", "")[:12],
                    "message": message_summary,
                    "author": author_data.get("name", "unknown"),
                    "date": author_data.get("date"),
                    "url": c.get("html_url", ""),
                }
            )

        url = client._parse_next_link(resp.headers.get("link", ""))

    return results


# =============================================================================
# Per-repo fetch orchestrator
# =============================================================================


async def fetch_repo(
    client: GitHubClient, project: dict, since_ts: str, compact: bool
) -> Optional[dict]:
    """Fetch all data for a single repo concurrently."""
    owner, repo = project["owner"], project["repo"]

    # Launch releases and merged_prs always; open_prs and commits only if not compact
    tasks = {
        "releases": fetch_releases(client, owner, repo, since_ts),
        "merged_prs": fetch_merged_prs(client, owner, repo, since_ts),
    }
    if not compact:
        tasks["open_prs"] = fetch_open_prs(client, owner, repo, since_ts)
        tasks["commits"] = fetch_commits(client, owner, repo, since_ts)

    results = {}
    task_items = list(tasks.items())
    gathered = await asyncio.gather(*[t for _, t in task_items], return_exceptions=True)

    for (key, _), result in zip(task_items, gathered):
        if isinstance(result, Exception):
            if client.verbose:
                print(
                    f"  Warning: {key} failed for {owner}/{repo}: {result}",
                    file=sys.stderr,
                )
            results[key] = []
        else:
            results[key] = result

    releases = results.get("releases", [])
    merged_prs = results.get("merged_prs", [])
    open_prs = results.get("open_prs", [])
    commits = results.get("commits", [])

    if releases or merged_prs or open_prs or commits:
        return {
            "name": project["name"],
            "description": project["description"],
            "category": project["category"],
            "priority": project["priority"],
            "website": project["website"],
            "maintainer": project["maintainer"],
            "releases": releases,
            "merged_prs": merged_prs,
            "open_prs": open_prs,
            "commits": commits,
        }
    return None


# =============================================================================
# Project Loading (unchanged logic)
# =============================================================================


def load_projects(
    projects_file: Path, filter_projects=None, filter_categories=None
) -> list[dict]:
    with open(projects_file) as f:
        data = yaml.safe_load(f)

    projects = []
    for category, items in data.items():
        if not isinstance(items, list):
            continue
        if filter_categories and category not in filter_categories:
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            project_name = item.get("name", "")
            if filter_projects and project_name not in filter_projects:
                continue

            repo_url = item.get("repo")
            parsed = parse_github_repo(repo_url)
            added_urls = set()

            if parsed:
                owner, repo = parsed
                projects.append(
                    {
                        "owner": owner,
                        "repo": repo,
                        "repo_url": repo_url,
                        "name": project_name or repo,
                        "description": item.get("description", ""),
                        "category": category,
                        "priority": item.get("priority", "low"),
                        "website": item.get("website", ""),
                        "maintainer": item.get("maintainer", ""),
                        "status": item.get("status", ""),
                    }
                )
                added_urls.add(repo_url)

            repos_dict = item.get("repos", {})
            if isinstance(repos_dict, dict):
                for repo_key, sub_repo_url in repos_dict.items():
                    if sub_repo_url in added_urls:
                        continue
                    sub_parsed = parse_github_repo(sub_repo_url)
                    if sub_parsed:
                        sub_owner, sub_repo = sub_parsed
                        projects.append(
                            {
                                "owner": sub_owner,
                                "repo": sub_repo,
                                "repo_url": sub_repo_url,
                                "name": f"{project_name} ({repo_key})"
                                if project_name
                                else sub_repo,
                                "description": item.get("description", ""),
                                "category": category,
                                "priority": item.get("priority", "low"),
                                "website": item.get("website", ""),
                                "maintainer": item.get("maintainer", ""),
                                "status": item.get("status", ""),
                            }
                        )
                        added_urls.add(sub_repo_url)

    return projects


# =============================================================================
# Output helpers (unchanged logic)
# =============================================================================


def get_output_filename(since_date, until_date):
    return f"updates_{since_date.strftime('%Y-%m-%d')}_{until_date.strftime('%Y-%m-%d')}.json"


def get_last_run_date(output_dir):
    pattern = re.compile(r"updates_(\d{4}-\d{2}-\d{2})_(\d{4}-\d{2}-\d{2})\.json$")
    latest = None
    for fp in output_dir.glob("updates_*.json"):
        m = pattern.match(fp.name)
        if m:
            try:
                d = datetime.strptime(m.group(1), "%Y-%m-%d").replace(
                    tzinfo=timezone.utc
                )
                if latest is None or d > latest:
                    latest = d
            except ValueError:
                continue
    return latest


def load_existing_data(filepath):
    if not filepath.exists():
        return None
    try:
        with open(filepath) as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None


def calculate_summary(projects):
    s = {
        "total_releases": 0,
        "total_merged_prs": 0,
        "total_open_prs": 0,
        "total_commits": 0,
        "active_repos": 0,
    }
    for p in projects.values():
        r, m, o, c = (
            len(p.get("releases", [])),
            len(p.get("merged_prs", [])),
            len(p.get("open_prs", [])),
            len(p.get("commits", [])),
        )
        s["total_releases"] += r
        s["total_merged_prs"] += m
        s["total_open_prs"] += o
        s["total_commits"] += c
        if r or m or o or c:
            s["active_repos"] += 1
    return s


def print_summary(data, since_days):
    summary = data.get("summary", {})
    print("\n" + "=" * 60)
    print(f"UPDATES FROM LAST {since_days} DAYS")
    print("=" * 60 + "\n")
    if summary.get("active_repos", 0) == 0:
        print("No updates found.")
        return
    print(f"Active repositories: {summary['active_repos']}")
    print(f"Releases: {summary['total_releases']}")
    print(f"Merged PRs: {summary['total_merged_prs']}")
    print(f"Open PRs: {summary['total_open_prs']}")
    print(f"Commits: {summary['total_commits']}\n")
    print("-" * 40 + "\nREPOSITORIES WITH ACTIVITY:\n" + "-" * 40)
    for rk, p in data.get("projects", {}).items():
        r, m, o, c = (
            len(p.get("releases", [])),
            len(p.get("merged_prs", [])),
            len(p.get("open_prs", [])),
            len(p.get("commits", [])),
        )
        if r or m or o or c:
            parts = []
            if r:
                parts.append(f"{r} releases")
            if m:
                parts.append(f"{m} merged PRs")
            if o:
                parts.append(f"{o} open PRs")
            if c:
                parts.append(f"{c} commits")
            print(f"  {p.get('name', rk)}: {', '.join(parts)}")
    print()


# =============================================================================
# Main async orchestrator
# =============================================================================


async def run(args, projects: list[dict]):
    token = get_github_token()

    now = datetime.now(timezone.utc)
    since_dt = now - timedelta(days=args.since_days)
    since_ts = since_dt.isoformat()

    output_path = args.output_dir / get_output_filename(since_dt, now)

    already_fetched = set()
    all_projects = {}
    if not args.fresh:
        existing = load_existing_data(output_path)
        if existing:
            all_projects = existing.get("projects", {})
            already_fetched = set(all_projects.keys())
            if already_fetched:
                print(
                    f"Resuming: {len(already_fetched)} repos already fetched (use --fresh to restart)"
                )

    # Filter out already-fetched repos
    remaining = [
        p for p in projects if f"{p['owner']}/{p['repo']}" not in already_fetched
    ]

    print(
        f"\nFetching updates since {since_dt.strftime('%Y-%m-%d')} "
        f"({len(remaining)} repos, concurrency={args.concurrency})...\n"
    )
    sys.stdout.flush()

    def save_progress():
        with open(output_path, "w") as f:
            json.dump(
                {
                    "generated_at": datetime.now(timezone.utc).isoformat(),
                    "period": {
                        "start": since_dt.strftime("%Y-%m-%d"),
                        "end": now.strftime("%Y-%m-%d"),
                        "days": args.since_days,
                    },
                    "summary": calculate_summary(all_projects),
                    "projects": all_projects,
                },
                f,
                indent=2,
            )

    # SIGINT handler
    interrupted = False

    def handle_interrupt(signum, frame):
        nonlocal interrupted
        if interrupted:
            # Second interrupt - force exit
            sys.exit(130)
        interrupted = True
        print(
            "\n\nInterrupted! Will save progress after current batch...",
            file=sys.stderr,
        )

    signal.signal(signal.SIGINT, handle_interrupt)

    start_time = time.monotonic()
    completed = 0
    total = len(remaining)

    async with GitHubClient(
        token, concurrency=args.concurrency, verbose=args.verbose
    ) as client:
        # Process in batches for progress reporting and periodic saves
        batch_size = (
            args.concurrency * 2
        )  # 2x concurrency for good pipeline utilization
        for batch_start in range(0, total, batch_size):
            if interrupted:
                break

            batch = remaining[batch_start : batch_start + batch_size]
            tasks = [fetch_repo(client, p, since_ts, args.compact) for p in batch]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            for project, result in zip(batch, results):
                repo_key = f"{project['owner']}/{project['repo']}"
                completed += 1

                if isinstance(result, Exception):
                    if args.verbose:
                        print(
                            f"  [{completed}/{total}] {project['name']} ({repo_key}): ERROR - {result}",
                            file=sys.stderr,
                        )
                    else:
                        print(f"  [{completed}/{total}] {project['name']}: error")
                elif result is not None:
                    all_projects[repo_key] = result
                    r = len(result["releases"])
                    m = len(result["merged_prs"])
                    o = len(result["open_prs"])
                    c = len(result["commits"])
                    print(
                        f"  [{completed}/{total}] {project['name']}: {r}r {m}m {o}o {c}c"
                    )
                else:
                    if args.verbose:
                        print(f"  [{completed}/{total}] {project['name']}: no activity")

            # Save progress after each batch
            save_progress()

    elapsed = time.monotonic() - start_time

    # Final save
    save_progress()

    print(f"\nOutput saved to {output_path}")
    print(
        f"Completed in {elapsed:.1f}s ({client.request_count} API requests, "
        f"{client.request_count / max(elapsed, 0.1):.1f} req/s)"
    )

    if interrupted:
        print(
            f"Interrupted after {completed}/{total} repos. Run again to resume.",
            file=sys.stderr,
        )
        sys.exit(130)

    print_summary(
        {"projects": all_projects, "summary": calculate_summary(all_projects)},
        args.since_days,
    )
    print("Done!")


# =============================================================================
# Entry point
# =============================================================================


def main():
    parser = argparse.ArgumentParser(
        description="Fetch project updates from GitHub (async)"
    )
    parser.add_argument("--since-days", type=int, default=None)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--projects-file", type=Path, default=PROJECT_ROOT / "data" / "projects.yml"
    )
    parser.add_argument("--projects", type=str)
    parser.add_argument("--categories", type=str)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--fresh", action="store_true")
    parser.add_argument(
        "--compact", action="store_true", help="Skip commits and open PRs"
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help=f"Max concurrent requests (default: {DEFAULT_CONCURRENCY})",
    )
    args = parser.parse_args()

    filter_projects = (
        [p.strip() for p in args.projects.split(",")] if args.projects else None
    )
    filter_categories = (
        [c.strip() for c in args.categories.split(",")] if args.categories else None
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)

    if args.since_days is None:
        last_run = get_last_run_date(args.output_dir)
        if last_run:
            args.since_days = max(1, (datetime.now(timezone.utc) - last_run).days + 1)
            print(f"Auto-detected: fetching {args.since_days} days")
        else:
            args.since_days = 7
            print(f"No previous runs, defaulting to {args.since_days} days")

    print(f"Loading projects from {args.projects_file}...")
    projects = load_projects(args.projects_file, filter_projects, filter_categories)
    print(f"Found {len(projects)} projects with GitHub repos")

    if args.dry_run:
        for p in projects:
            print(f"  - {p['name']} ({p['owner']}/{p['repo']}) [{p['category']}]")
        return

    asyncio.run(run(args, projects))


if __name__ == "__main__":
    main()
