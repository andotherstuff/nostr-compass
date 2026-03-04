#!/usr/bin/env python3
"""
Fetch recent updates (releases, PRs, commits) from projects in data/projects.yml.

Uses `gh` CLI for all GitHub API calls (auth, rate limits handled automatically).

Requirements:
    - gh CLI authenticated (`gh auth status`)
    - pip install pyyaml

Usage:
    python3 scripts/fetch_project_updates.py --since-days 7
    python3 scripts/fetch_project_updates.py --projects "Damus,Amethyst"
"""

import argparse
import json
import re
import signal
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print("Missing pyyaml. Install with: pip install pyyaml")
    sys.exit(1)

DEFAULT_BODY_MAX_LENGTH = 0
PROJECT_ROOT = Path(__file__).parent.parent
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "data" / "project_updates"

BOT_PATTERNS = [
    r".*\[bot\]$",
    r"^dependabot$",
    r"^weblate$",
    r"^allcontributors$",
]


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
    return text[:max_length].rsplit(' ', 1)[0] + "..."


# =============================================================================
# gh CLI API Helper - single page fetch (no --paginate)
# =============================================================================

def gh_api_page(endpoint: str, verbose: bool = False) -> Optional[tuple[list | dict, Optional[str]]]:
    """
    Fetch a single page from GitHub API via gh CLI.

    Returns (data, next_page_url) or None on failure.
    next_page_url is parsed from the Link header if present.
    """
    cmd = ["gh", "api", "-i", endpoint]  # -i includes response headers

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        if verbose:
            print(f"  Warning: Timeout fetching {endpoint}", file=sys.stderr)
        return None

    if result.returncode != 0:
        stderr = result.stderr.strip()
        if "404" in stderr or "Not Found" in stderr:
            return ([], None)
        if verbose:
            print(f"  Warning: gh api failed for {endpoint}: {stderr}", file=sys.stderr)
        return None

    output = result.stdout

    # Split headers from body (separated by blank line)
    parts = output.split("\r\n\r\n", 1)
    if len(parts) < 2:
        parts = output.split("\n\n", 1)

    if len(parts) < 2:
        return None

    headers_text, body = parts[0], parts[1]

    # Parse Link header for next page
    next_url = None
    for line in headers_text.split("\n"):
        if line.lower().startswith("link:"):
            link_value = line.split(":", 1)[1].strip()
            # Parse <url>; rel="next"
            for part in link_value.split(","):
                if 'rel="next"' in part:
                    match = re.search(r'<([^>]+)>', part)
                    if match:
                        next_url = match.group(1)
                        # gh api expects relative paths, strip the base URL
                        if next_url.startswith("https://api.github.com/"):
                            next_url = next_url[len("https://api.github.com/"):]
            break

    body = body.strip()
    if not body:
        return ([], next_url)

    try:
        data = json.loads(body)
        return (data, next_url)
    except json.JSONDecodeError:
        if verbose:
            print(f"  Warning: Could not parse JSON from {endpoint}", file=sys.stderr)
        return None


def gh_api_simple(endpoint: str, verbose: bool = False) -> Optional[list | dict]:
    """Fetch a single (non-paginated) endpoint."""
    cmd = ["gh", "api", endpoint]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return None
    if result.returncode != 0:
        return None
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return None


# =============================================================================
# Data Fetching Functions (manual pagination with early termination)
# =============================================================================

def fetch_releases(owner: str, repo: str, since: Optional[str] = None, verbose: bool = False) -> list[dict]:
    since_dt = datetime.fromisoformat(since.replace("Z", "+00:00")) if since else None
    endpoint = f"repos/{owner}/{repo}/releases?per_page=100"
    result = []

    while endpoint:
        page = gh_api_page(endpoint, verbose)
        if page is None:
            break
        data, next_url = page
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
            result.append({
                "id": r["id"],
                "tag": r["tag_name"],
                "name": r.get("name") or r["tag_name"],
                "published_at": published_at,
                "url": r["html_url"],
                "body": truncate_body(r.get("body") or ""),
                "prerelease": r.get("prerelease", False),
                "author": r.get("author", {}).get("login", "unknown"),
            })

        if stop:
            break
        endpoint = next_url

    return result


def fetch_merged_prs(owner: str, repo: str, since: Optional[str] = None, verbose: bool = False) -> list[dict]:
    since_dt = datetime.fromisoformat(since.replace("Z", "+00:00")) if since else None
    endpoint = f"repos/{owner}/{repo}/pulls?state=closed&sort=updated&direction=desc&per_page=100"
    result = []

    while endpoint:
        page = gh_api_page(endpoint, verbose)
        if page is None:
            break
        data, next_url = page
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
                    updated_dt = datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
                    if updated_dt < since_dt:
                        past_range = True
                        break
                    continue
            labels = [label["name"] for label in pr.get("labels", [])]
            result.append({
                "id": pr["id"],
                "number": pr["number"],
                "title": pr["title"],
                "body": truncate_body(pr.get("body") or ""),
                "author": author,
                "merged_at": merged_at,
                "url": pr["html_url"],
                "labels": labels,
            })

        if past_range:
            break
        endpoint = next_url

    return result


def fetch_open_prs(owner: str, repo: str, since: Optional[str] = None, verbose: bool = False) -> list[dict]:
    since_dt = datetime.fromisoformat(since.replace("Z", "+00:00")) if since else None
    endpoint = f"repos/{owner}/{repo}/pulls?state=open&sort=created&direction=desc&per_page=100"
    result = []

    while endpoint:
        page = gh_api_page(endpoint, verbose)
        if page is None:
            break
        data, next_url = page
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
            result.append({
                "id": pr["id"],
                "number": pr["number"],
                "title": pr["title"],
                "body": truncate_body(pr.get("body") or ""),
                "author": author,
                "opened_at": created_at,
                "url": pr["html_url"],
                "labels": labels,
                "draft": pr.get("draft", False),
            })

        if past_range:
            break
        endpoint = next_url

    return result


def fetch_commits(owner: str, repo: str, since: Optional[str] = None, branch: Optional[str] = None, verbose: bool = False) -> list[dict]:
    if not branch:
        repo_data = gh_api_simple(f"repos/{owner}/{repo}", verbose)
        branch = (repo_data or {}).get("default_branch", "main")

    params = f"sha={branch}&per_page=100"
    if since:
        params += f"&since={since}"
    endpoint = f"repos/{owner}/{repo}/commits?{params}"
    result = []

    while endpoint:
        page = gh_api_page(endpoint, verbose)
        if page is None:
            break
        data, next_url = page
        if not data or not isinstance(data, list):
            break

        for c in data:
            commit_data = c.get("commit", {})
            author_data = commit_data.get("author", {})
            message = commit_data.get("message", "")
            message_summary = message.split("\n")[0] if message else ""
            result.append({
                "sha": c.get("sha", "")[:12],
                "message": message_summary,
                "author": author_data.get("name", "unknown"),
                "date": author_data.get("date"),
                "url": c.get("html_url", ""),
            })

        endpoint = next_url

    return result


# =============================================================================
# Project Loading
# =============================================================================

def load_projects(projects_file: Path, filter_projects=None, filter_categories=None) -> list[dict]:
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
                projects.append({
                    "owner": owner, "repo": repo, "repo_url": repo_url,
                    "name": project_name or repo,
                    "description": item.get("description", ""),
                    "category": category,
                    "priority": item.get("priority", "low"),
                    "website": item.get("website", ""),
                    "maintainer": item.get("maintainer", ""),
                    "status": item.get("status", ""),
                })
                added_urls.add(repo_url)

            repos_dict = item.get("repos", {})
            if isinstance(repos_dict, dict):
                for repo_key, sub_repo_url in repos_dict.items():
                    if sub_repo_url in added_urls:
                        continue
                    sub_parsed = parse_github_repo(sub_repo_url)
                    if sub_parsed:
                        sub_owner, sub_repo = sub_parsed
                        projects.append({
                            "owner": sub_owner, "repo": sub_repo, "repo_url": sub_repo_url,
                            "name": f"{project_name} ({repo_key})" if project_name else sub_repo,
                            "description": item.get("description", ""),
                            "category": category,
                            "priority": item.get("priority", "low"),
                            "website": item.get("website", ""),
                            "maintainer": item.get("maintainer", ""),
                            "status": item.get("status", ""),
                        })
                        added_urls.add(sub_repo_url)

    return projects


# =============================================================================
# Output helpers
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
                d = datetime.strptime(m.group(1), "%Y-%m-%d").replace(tzinfo=timezone.utc)
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
    s = {"total_releases": 0, "total_merged_prs": 0, "total_open_prs": 0, "total_commits": 0, "active_repos": 0}
    for p in projects.values():
        r, m, o, c = len(p.get("releases", [])), len(p.get("merged_prs", [])), len(p.get("open_prs", [])), len(p.get("commits", []))
        s["total_releases"] += r; s["total_merged_prs"] += m; s["total_open_prs"] += o; s["total_commits"] += c
        if r or m or o or c:
            s["active_repos"] += 1
    return s


def print_summary(data, since_days):
    summary = data.get("summary", {})
    print("\n" + "=" * 60)
    print(f"UPDATES FROM LAST {since_days} DAYS")
    print("=" * 60 + "\n")
    if summary.get("active_repos", 0) == 0:
        print("No updates found."); return
    print(f"Active repositories: {summary['active_repos']}")
    print(f"Releases: {summary['total_releases']}")
    print(f"Merged PRs: {summary['total_merged_prs']}")
    print(f"Open PRs: {summary['total_open_prs']}")
    print(f"Commits: {summary['total_commits']}\n")
    print("-" * 40 + "\nREPOSITORIES WITH ACTIVITY:\n" + "-" * 40)
    for rk, p in data.get("projects", {}).items():
        r, m, o, c = len(p.get("releases", [])), len(p.get("merged_prs", [])), len(p.get("open_prs", [])), len(p.get("commits", []))
        if r or m or o or c:
            parts = []
            if r: parts.append(f"{r} releases")
            if m: parts.append(f"{m} merged PRs")
            if o: parts.append(f"{o} open PRs")
            if c: parts.append(f"{c} commits")
            print(f"  {p.get('name', rk)}: {', '.join(parts)}")
    print()


# =============================================================================
# Main
# =============================================================================

def main():
    # Verify gh CLI
    try:
        r = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True, timeout=10)
        if r.returncode != 0:
            print("Error: gh CLI not authenticated. Run `gh auth login`.", file=sys.stderr); sys.exit(1)
    except FileNotFoundError:
        print("Error: gh CLI not found. Install from https://cli.github.com/", file=sys.stderr); sys.exit(1)

    parser = argparse.ArgumentParser(description="Fetch project updates from GitHub via gh CLI")
    parser.add_argument("--since-days", type=int, default=None)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--projects-file", type=Path, default=PROJECT_ROOT / "data" / "projects.yml")
    parser.add_argument("--projects", type=str)
    parser.add_argument("--categories", type=str)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--fresh", action="store_true")
    parser.add_argument("--compact", action="store_true", help="Skip commits and open PRs")
    args = parser.parse_args()

    filter_projects = [p.strip() for p in args.projects.split(",")] if args.projects else None
    filter_categories = [c.strip() for c in args.categories.split(",")] if args.categories else None
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
                print(f"Resuming: {len(already_fetched)} repos already fetched (use --fresh to restart)")

    print(f"\nFetching updates since {since_dt.strftime('%Y-%m-%d')}...\n")
    sys.stdout.flush()

    def save_progress():
        with open(output_path, "w") as f:
            json.dump({
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "period": {"start": since_dt.strftime("%Y-%m-%d"), "end": now.strftime("%Y-%m-%d"), "days": args.since_days},
                "summary": calculate_summary(all_projects),
                "projects": all_projects,
            }, f, indent=2)

    def handle_interrupt(signum, frame):
        print("\n\nInterrupted! Saving progress...", file=sys.stderr)
        save_progress()
        print(f"Saved to {output_path}. Run again to resume.", file=sys.stderr)
        sys.exit(130)

    signal.signal(signal.SIGINT, handle_interrupt)

    total = len(projects)
    for i, project in enumerate(projects, 1):
        repo_key = f"{project['owner']}/{project['repo']}"
        if repo_key in already_fetched:
            continue

        print(f"[{i}/{total}] {project['name']} ({repo_key})...", end=" ", flush=True)

        releases = fetch_releases(project["owner"], project["repo"], since_ts, args.verbose)
        merged_prs = fetch_merged_prs(project["owner"], project["repo"], since_ts, args.verbose)

        if args.compact:
            open_prs, commits = [], []
        else:
            open_prs = fetch_open_prs(project["owner"], project["repo"], since_ts, args.verbose)
            commits = fetch_commits(project["owner"], project["repo"], since_ts, verbose=args.verbose)

        if releases or merged_prs or open_prs or commits:
            all_projects[repo_key] = {
                "name": project["name"], "description": project["description"],
                "category": project["category"], "priority": project["priority"],
                "website": project["website"], "maintainer": project["maintainer"],
                "releases": releases, "merged_prs": merged_prs,
                "open_prs": open_prs, "commits": commits,
            }
            print(f"{len(releases)}r {len(merged_prs)}m {len(open_prs)}o {len(commits)}c")
        else:
            print("no activity")

        if i % 20 == 0:
            save_progress()

    save_progress()
    print(f"\nOutput saved to {output_path}")
    print_summary({"projects": all_projects, "summary": calculate_summary(all_projects)}, args.since_days)
    print("Done!")


if __name__ == "__main__":
    main()
