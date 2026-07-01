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

# Known Gitea/Forgejo hosts. Each entry maps a hostname to its API base URL.
# Extend this when adding new self-hosted forges to projects.yml.
GITEA_HOSTS = {
    "git.vanderwarker.family": "https://git.vanderwarker.family/api/v1",
    "git.reya.su": "https://git.reya.su/api/v1",
    "git.nostrdev.com": "https://git.nostrdev.com/api/v1",
}
GITEA_CONCURRENCY = 8  # per-host cap to avoid hammering small self-hosted instances

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


def parse_gitea_repo(repo_url: str) -> Optional[tuple[str, str, str]]:
    """Parse a Gitea/Forgejo repo URL into (host, owner, repo).

    Only matches hosts in GITEA_HOSTS. Returns None for unknown hosts.
    """
    if not repo_url:
        return None
    match = re.match(r"https?://([^/]+)/([^/]+)/([^/]+?)(?:\.git)?/?$", repo_url)
    if not match:
        return None
    host, owner, repo = match.groups()
    if host not in GITEA_HOSTS:
        return None
    if not repo or repo in ("", "."):
        return None
    return (host, owner, repo.rstrip("/"))


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
# Gitea/Forgejo client (mirrors GitHubClient public interface)
# =============================================================================


class GiteaClient:
    """Async Gitea/Forgejo API client.

    Same public surface as GitHubClient (get, get_json, get_paginated,
    _parse_next_link, request_count, verbose) so the fetch_* functions can
    treat it interchangeably. No auth, no rate-limit tracking; small
    self-hosted instances are throttled via a lower per-host concurrency cap.

    Pagination: Gitea sends ?page=N&limit=N parameters and does NOT emit
    Link headers, so _parse_next_link inspects the result count vs requested
    limit and increments a per-URL page counter.
    """

    def __init__(
        self, host: str, concurrency: int = GITEA_CONCURRENCY, verbose: bool = False
    ):
        if host not in GITEA_HOSTS:
            raise ValueError(f"Unknown Gitea host: {host}")
        self.host = host
        self.base_url = GITEA_HOSTS[host]
        self.verbose = verbose
        self.semaphore = asyncio.Semaphore(concurrency)
        self.request_count = 0
        self.client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        self.client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={
                "Accept": "application/json",
                "User-Agent": "nostr-compass-fetcher",
            },
            timeout=httpx.Timeout(30.0, connect=10.0),
            follow_redirects=True,
            limits=httpx.Limits(
                max_connections=concurrency_cap_for_host(),
                max_keepalive_connections=GITEA_CONCURRENCY,
            ),
        )
        return self

    async def __aexit__(self, *args):
        if self.client:
            await self.client.aclose()

    async def get(self, endpoint: str) -> Optional[httpx.Response]:
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
                        f"  Warning: Gitea request failed for {self.host}{endpoint}: {e}",
                        file=sys.stderr,
                    )
                return None

            if resp.status_code == 404:
                return resp
            if resp.status_code >= 400:
                if self.verbose:
                    print(
                        f"  Warning: Gitea HTTP {resp.status_code} for {self.host}{endpoint}",
                        file=sys.stderr,
                    )
                return None
            return resp

    async def get_json(self, endpoint: str) -> Optional[list | dict]:
        resp = await self.get(endpoint)
        if resp is None:
            return None
        if resp.status_code == 404:
            return []
        try:
            return resp.json()
        except (json.JSONDecodeError, ValueError):
            return None

    @staticmethod
    def _parse_next_link(_link_header: str) -> Optional[str]:
        """Gitea does not emit Link headers; pagination is handled inline
        in the fetch functions via _next_page_url. This always returns None
        so the fetch_* loops fall through to their own next-page logic when
        the client is a GiteaClient."""
        return None

    @staticmethod
    def next_page_url(current_url: str, page_size: int) -> str:
        """Bump the &page=N counter on a Gitea endpoint URL."""
        match = re.search(r"[?&]page=(\d+)", current_url)
        if match:
            current_page = int(match.group(1))
            return re.sub(r"([?&])page=\d+", lambda m: f"{m.group(1)}page={current_page + 1}", current_url)
        sep = "&" if "?" in current_url else "?"
        return f"{current_url}{sep}page=2"


def concurrency_cap_for_host() -> int:
    """httpx connection pool cap for a single Gitea host."""
    return max(GITEA_CONCURRENCY * 2, 16)


def is_gitea_client(client) -> bool:
    return isinstance(client, GiteaClient)


# =============================================================================
# Data Fetching Functions (async, same output format as original)
# =============================================================================


async def fetch_releases(
    client, owner: str, repo: str, since: Optional[str] = None
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

    page_size = 50 if is_gitea_client(client) else 100
    endpoint = f"/repos/{owner}/{repo}/releases?limit={page_size}&page=1" if is_gitea_client(client) else f"/repos/{owner}/{repo}/releases?per_page={page_size}"
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

        page_count = len(data)
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
                    "author": (r.get("author") or {}).get("login", "unknown"),
                }
            )

        if stop:
            break
        if is_gitea_client(client):
            if page_count < page_size:
                break
            url = GiteaClient.next_page_url(url, page_size)
        else:
            url = client._parse_next_link(resp.headers.get("link", ""))

    return results


async def fetch_merged_prs(
    client, owner: str, repo: str, since: Optional[str] = None
) -> list[dict]:
    since_dt = datetime.fromisoformat(since.replace("Z", "+00:00")) if since else None
    page_size = 50 if is_gitea_client(client) else 100
    if is_gitea_client(client):
        endpoint = f"/repos/{owner}/{repo}/pulls?state=closed&sort=newest&limit={page_size}&page=1"
    else:
        endpoint = f"/repos/{owner}/{repo}/pulls?state=closed&sort=updated&direction=desc&per_page={page_size}"
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

        page_count = len(data)
        past_range = False
        for pr in data:
            if not pr.get("merged_at"):
                continue
            author = (pr.get("user") or {}).get("login", "")
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
        if is_gitea_client(client):
            if page_count < page_size:
                break
            url = GiteaClient.next_page_url(url, page_size)
        else:
            url = client._parse_next_link(resp.headers.get("link", ""))

    return results


async def fetch_open_prs(
    client, owner: str, repo: str, since: Optional[str] = None
) -> list[dict]:
    since_dt = datetime.fromisoformat(since.replace("Z", "+00:00")) if since else None
    page_size = 50 if is_gitea_client(client) else 100
    if is_gitea_client(client):
        endpoint = f"/repos/{owner}/{repo}/pulls?state=open&sort=newest&limit={page_size}&page=1"
    else:
        endpoint = f"/repos/{owner}/{repo}/pulls?state=open&sort=created&direction=desc&per_page={page_size}"
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

        page_count = len(data)
        past_range = False
        for pr in data:
            author = (pr.get("user") or {}).get("login", "")
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
        if is_gitea_client(client):
            if page_count < page_size:
                break
            url = GiteaClient.next_page_url(url, page_size)
        else:
            url = client._parse_next_link(resp.headers.get("link", ""))

    return results


async def fetch_commits(
    client,
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

    page_size = 50 if is_gitea_client(client) else 100
    if is_gitea_client(client):
        # Gitea/Forgejo rejects ISO8601 offset notation (+00:00); normalize to Z
        gitea_since = (
            re.sub(r"\+00:00$", "Z", since) if since else None
        )
        params = f"sha={branch}&limit={page_size}&page=1"
        if gitea_since:
            params += f"&since={gitea_since}"
    else:
        params = f"sha={branch}&per_page={page_size}"
        if since:
            params += f"&since={since}"
    endpoint = f"/repos/{owner}/{repo}/commits?{params}"
    results = []
    url = endpoint
    gitea_since_dt = (
        datetime.fromisoformat(since.replace("Z", "+00:00")) if since and is_gitea_client(client) else None
    )

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

        page_count = len(data)
        past_range = False
        for c in data:
            commit_data = c.get("commit", {})
            author_data = commit_data.get("author", {}) or {}
            date_str = author_data.get("date")
            # Gitea ignores ?since= on /commits, so we filter client-side
            if gitea_since_dt and date_str:
                try:
                    commit_dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                    if commit_dt < gitea_since_dt:
                        past_range = True
                        break
                except ValueError:
                    pass
            message = commit_data.get("message", "")
            message_summary = message.split("\n")[0] if message else ""
            results.append(
                {
                    "sha": c.get("sha", "")[:12],
                    "message": message_summary,
                    "author": author_data.get("name", "unknown"),
                    "date": date_str,
                    "url": c.get("html_url", ""),
                }
            )

        if past_range:
            break
        if is_gitea_client(client):
            if page_count < page_size:
                break
            url = GiteaClient.next_page_url(url, page_size)
        else:
            url = client._parse_next_link(resp.headers.get("link", ""))

    return results


# =============================================================================
# Per-repo fetch orchestrator
# =============================================================================


async def fetch_repo(
    client, project: dict, since_ts: str, compact: bool
) -> Optional[dict]:
    """Fetch all data for a single repo concurrently. Accepts GitHubClient or GiteaClient."""
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
            "host": project.get("host", "github.com"),
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
            added_urls = set()

            entry = _project_entry_from_url(
                repo_url, project_name, item, category
            )
            if entry:
                projects.append(entry)
                added_urls.add(repo_url)

            repos_dict = item.get("repos", {})
            if isinstance(repos_dict, dict):
                for repo_key, sub_repo_url in repos_dict.items():
                    if sub_repo_url in added_urls:
                        continue
                    sub_name = (
                        f"{project_name} ({repo_key})" if project_name else None
                    )
                    sub_entry = _project_entry_from_url(
                        sub_repo_url, sub_name, item, category
                    )
                    if sub_entry:
                        projects.append(sub_entry)
                        added_urls.add(sub_repo_url)

    return projects


def _project_entry_from_url(
    repo_url: str, project_name: Optional[str], item: dict, category: str
) -> Optional[dict]:
    """Build a project entry from a repo URL, routing to GitHub or Gitea parser."""
    if not repo_url:
        return None

    base = {
        "description": item.get("description", ""),
        "category": category,
        "priority": item.get("priority", "low"),
        "website": item.get("website", ""),
        "maintainer": item.get("maintainer", ""),
        "status": item.get("status", ""),
        "repo_url": repo_url,
    }

    gh = parse_github_repo(repo_url)
    if gh:
        owner, repo = gh
        return {
            **base,
            "host": "github.com",
            "owner": owner,
            "repo": repo,
            "name": project_name or repo,
        }

    gt = parse_gitea_repo(repo_url)
    if gt:
        host, owner, repo = gt
        return {
            **base,
            "host": host,
            "owner": owner,
            "repo": repo,
            "name": project_name or repo,
        }

    return None


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


def _repo_key(project: dict) -> str:
    """Stable identifier including host so github vs gitea owner/repo don't collide."""
    host = project.get("host", "github.com")
    if host == "github.com":
        return f"{project['owner']}/{project['repo']}"
    return f"{host}/{project['owner']}/{project['repo']}"


async def run(args, projects: list[dict]):
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
    remaining = [p for p in projects if _repo_key(p) not in already_fetched]

    # Split by host so each gets the right client
    github_projects = [p for p in remaining if p.get("host", "github.com") == "github.com"]
    gitea_by_host: dict[str, list[dict]] = {}
    for p in remaining:
        h = p.get("host", "github.com")
        if h != "github.com":
            gitea_by_host.setdefault(h, []).append(p)

    total = len(remaining)
    print(
        f"\nFetching updates since {since_dt.strftime('%Y-%m-%d')} "
        f"({total} repos: {len(github_projects)} GitHub, "
        f"{sum(len(v) for v in gitea_by_host.values())} Gitea across {len(gitea_by_host)} host(s))...\n"
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
            sys.exit(130)
        interrupted = True
        print(
            "\n\nInterrupted! Will save progress after current batch...",
            file=sys.stderr,
        )

    signal.signal(signal.SIGINT, handle_interrupt)

    start_time = time.monotonic()
    completed = [0]  # mutable for nested closure
    total_requests = [0]

    async def run_batch(client, batch: list[dict]):
        nonlocal interrupted
        if interrupted:
            return
        tasks = [fetch_repo(client, p, since_ts, args.compact) for p in batch]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for project, result in zip(batch, results):
            repo_key = _repo_key(project)
            completed[0] += 1
            if isinstance(result, Exception):
                if args.verbose:
                    print(
                        f"  [{completed[0]}/{total}] {project['name']} ({repo_key}): ERROR - {result}",
                        file=sys.stderr,
                    )
                else:
                    print(f"  [{completed[0]}/{total}] {project['name']}: error")
            elif result is not None:
                all_projects[repo_key] = result
                r = len(result["releases"])
                m = len(result["merged_prs"])
                o = len(result["open_prs"])
                c = len(result["commits"])
                print(
                    f"  [{completed[0]}/{total}] {project['name']}: {r}r {m}m {o}o {c}c"
                )
            else:
                if args.verbose:
                    print(f"  [{completed[0]}/{total}] {project['name']}: no activity")
        save_progress()

    # GitHub batch
    if github_projects:
        token = get_github_token()
        async with GitHubClient(
            token, concurrency=args.concurrency, verbose=args.verbose
        ) as client:
            batch_size = args.concurrency * 2
            for batch_start in range(0, len(github_projects), batch_size):
                if interrupted:
                    break
                await run_batch(
                    client, github_projects[batch_start : batch_start + batch_size]
                )
            total_requests[0] += client.request_count

    # Gitea batches, one host at a time
    for host, host_projects in gitea_by_host.items():
        if interrupted:
            break
        async with GiteaClient(host, verbose=args.verbose) as client:
            batch_size = GITEA_CONCURRENCY * 2
            for batch_start in range(0, len(host_projects), batch_size):
                if interrupted:
                    break
                await run_batch(
                    client, host_projects[batch_start : batch_start + batch_size]
                )
            total_requests[0] += client.request_count

    elapsed = time.monotonic() - start_time

    save_progress()

    print(f"\nOutput saved to {output_path}")
    print(
        f"Completed in {elapsed:.1f}s ({total_requests[0]} API requests, "
        f"{total_requests[0] / max(elapsed, 0.1):.1f} req/s)"
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
    gh_count = sum(1 for p in projects if p.get("host", "github.com") == "github.com")
    gt_count = len(projects) - gh_count
    print(f"Found {len(projects)} repos ({gh_count} GitHub, {gt_count} Gitea)")

    if args.dry_run:
        for p in projects:
            host = p.get("host", "github.com")
            print(f"  - {p['name']} ({host}/{p['owner']}/{p['repo']}) [{p['category']}]")
        return

    asyncio.run(run(args, projects))


if __name__ == "__main__":
    main()
