#!/usr/bin/env python3
"""
Fetch historical project activity for a specific month across all years since Nostr started.

This script is designed for the newsletter's "This Month in Nostr History" section.
It uses the GitHub Search API for accurate historical data retrieval.

Features:
    - Fetches releases and merged PRs for a specific month (e.g., all Decembers)
    - Uses GitHub Search API for accurate historical PR data
    - Paginates through all releases to find old ones
    - Incremental saves after each year (resume-friendly)
    - Rate limit handling with configurable delay
    - Commits only fetched for high-priority projects (configurable)

Usage:
    # Fetch all December activity since Nostr started
    python3 scripts/fetch_month_history.py --month 12

    # Resume interrupted fetch (automatically loads existing data)
    python3 scripts/fetch_month_history.py --month 12

    # With slower delay for rate limiting
    python3 scripts/fetch_month_history.py --month 12 --delay 1.0

Environment variables:
    GITHUB_TOKEN: GitHub personal access token (strongly recommended)
"""

import argparse
import calendar
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    import requests
    import yaml
    from dotenv import load_dotenv
except ImportError:
    print("Missing dependencies. Install with: pip install requests pyyaml python-dotenv")
    sys.exit(1)


# =============================================================================
# Configuration
# =============================================================================

PROJECT_ROOT = Path(__file__).parent.parent
load_dotenv(PROJECT_ROOT / ".env")

GITHUB_API_BASE = "https://api.github.com"
OUTPUT_DIR = PROJECT_ROOT / "data" / "project_updates"

# Nostr started November 2020
NOSTR_START_YEAR = 2020
NOSTR_START_MONTH = 11

# Rate limiting
DEFAULT_DELAY = 0.5  # Seconds between requests
MAX_RETRIES = 3

# Bot patterns to filter out
BOT_PATTERNS = [
    r".*\[bot\]$",
    r"^dependabot$",
    r"^weblate$",
    r"^allcontributors$",
]


# =============================================================================
# Utilities
# =============================================================================

def is_bot_user(username: str) -> bool:
    """Check if username belongs to a bot."""
    if not username:
        return False
    username_lower = username.lower()
    return any(re.match(p, username_lower) for p in BOT_PATTERNS)


def parse_github_repo(repo_url: str) -> Optional[tuple[str, str]]:
    """Extract owner and repo from GitHub URL."""
    if not repo_url:
        return None
    match = re.match(r"https?://github\.com/([^/]+)/([^/\.]+)", repo_url)
    if match:
        return match.groups()
    return None


def get_month_ranges(month: int) -> list[tuple[datetime, datetime]]:
    """Generate date ranges for a month across all years since Nostr started."""
    ranges = []
    now = datetime.now(timezone.utc)

    for year in range(NOSTR_START_YEAR, now.year + 1):
        # Skip months before Nostr started
        if year == NOSTR_START_YEAR and month < NOSTR_START_MONTH:
            continue
        # Skip future months
        if year == now.year and month > now.month:
            continue

        _, last_day = calendar.monthrange(year, month)
        start = datetime(year, month, 1, 0, 0, 0, tzinfo=timezone.utc)
        end = datetime(year, month, last_day, 23, 59, 59, tzinfo=timezone.utc)
        ranges.append((start, end))

    return ranges


# =============================================================================
# GitHub API
# =============================================================================

class GitHubAPI:
    """GitHub API client with rate limit handling."""

    def __init__(self, token: Optional[str], delay: float = DEFAULT_DELAY):
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "nostr-compass-history",
        }
        if token:
            self.headers["Authorization"] = f"token {token}"
        self.delay = delay
        self.request_count = 0

    def _request(self, url: str, params: Optional[dict] = None) -> Optional[dict]:
        """Make API request with rate limit handling."""
        for attempt in range(MAX_RETRIES):
            try:
                time.sleep(self.delay)
                self.request_count += 1

                response = requests.get(url, headers=self.headers, params=params, timeout=30)

                # Handle rate limiting
                remaining = response.headers.get("X-RateLimit-Remaining")
                reset_time = response.headers.get("X-RateLimit-Reset")

                if response.status_code == 403 and remaining == "0":
                    wait = int(reset_time) - int(time.time()) + 1 if reset_time else 60
                    print(f"  Rate limited. Waiting {wait}s...", file=sys.stderr)
                    time.sleep(max(wait, 1))
                    continue

                if response.status_code == 429:
                    wait = int(response.headers.get("Retry-After", 60))
                    print(f"  Too many requests. Waiting {wait}s...", file=sys.stderr)
                    time.sleep(wait)
                    continue

                if response.status_code == 404:
                    return None

                # Warn on low rate limit
                if remaining and int(remaining) < 50:
                    print(f"  Warning: {remaining} API requests remaining", file=sys.stderr)

                response.raise_for_status()
                return response.json()

            except requests.exceptions.RequestException as e:
                if attempt < MAX_RETRIES - 1:
                    print(f"  Request failed: {e}. Retrying...", file=sys.stderr)
                    time.sleep(2 ** attempt)
                else:
                    print(f"  Request failed after {MAX_RETRIES} attempts: {e}", file=sys.stderr)
                    return None

        return None

    def search_merged_prs(self, owner: str, repo: str, start: datetime, end: datetime) -> list[dict]:
        """Search for merged PRs in a date range using Search API."""
        start_str = start.strftime("%Y-%m-%d")
        end_str = end.strftime("%Y-%m-%d")

        query = f"repo:{owner}/{repo} is:pr is:merged merged:{start_str}..{end_str}"
        url = f"{GITHUB_API_BASE}/search/issues"

        results = []
        page = 1

        while True:
            params = {"q": query, "sort": "created", "order": "asc", "per_page": 100, "page": page}
            data = self._request(url, params)

            if not data or "items" not in data:
                break

            items = data["items"]
            for pr in items:
                author = pr.get("user", {}).get("login", "")
                if is_bot_user(author):
                    continue

                labels = [l["name"] for l in pr.get("labels", [])]
                pr_data = pr.get("pull_request", {})

                results.append({
                    "number": pr["number"],
                    "title": pr["title"],
                    "author": author,
                    "merged_at": pr_data.get("merged_at") or pr.get("closed_at"),
                    "url": pr["html_url"],
                    "labels": labels,
                })

            if len(items) < 100:
                break
            page += 1

        return results

    def fetch_releases(self, owner: str, repo: str, start: datetime, end: datetime) -> list[dict]:
        """Fetch releases within a date range, paginating through all."""
        url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/releases"
        results = []
        page = 1

        while page <= 10:  # Max 1000 releases
            params = {"per_page": 100, "page": page}
            data = self._request(url, params)

            if not data:
                break

            for r in data:
                if r.get("draft"):
                    continue

                pub_date = r.get("published_at")
                if not pub_date:
                    continue

                pub_dt = datetime.fromisoformat(pub_date.replace("Z", "+00:00"))
                if pub_dt < start:
                    # Releases are sorted newest first, so we can stop
                    return results
                if pub_dt > end:
                    continue

                results.append({
                    "tag": r["tag_name"],
                    "name": r.get("name") or r["tag_name"],
                    "published_at": pub_date,
                    "url": r["html_url"],
                    "author": r.get("author", {}).get("login", "unknown"),
                    "prerelease": r.get("prerelease", False),
                })

            if len(data) < 100:
                break
            page += 1

        return results

    def fetch_commits(self, owner: str, repo: str, start: datetime, end: datetime) -> list[dict]:
        """Fetch commits within a date range."""
        url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/commits"
        params = {
            "since": start.isoformat(),
            "until": end.isoformat(),
            "per_page": 100,
        }

        data = self._request(url, params)
        if not data:
            return []

        results = []
        for c in data:
            commit = c.get("commit", {})
            author = commit.get("author", {})

            results.append({
                "sha": c.get("sha", "")[:12],
                "message": commit.get("message", "").split("\n")[0],  # First line only
                "author": author.get("name", "unknown"),
                "date": author.get("date"),
                "url": c.get("html_url", ""),
            })

        return results


# =============================================================================
# Project Loading
# =============================================================================

def load_projects(projects_file: Path) -> list[dict]:
    """Load all projects with GitHub repos from projects.yml."""
    with open(projects_file) as f:
        data = yaml.safe_load(f)

    projects = []
    seen_urls = set()

    for category, items in data.items():
        if not isinstance(items, list):
            continue

        for item in items:
            if not isinstance(item, dict):
                continue

            # Process main repo
            repo_url = item.get("repo")
            parsed = parse_github_repo(repo_url)
            if parsed and repo_url not in seen_urls:
                owner, repo = parsed
                projects.append({
                    "owner": owner,
                    "repo": repo,
                    "name": item.get("name", repo),
                    "category": category,
                    "priority": item.get("priority", "low"),
                })
                seen_urls.add(repo_url)

            # Process additional repos
            for key, sub_url in item.get("repos", {}).items():
                sub_parsed = parse_github_repo(sub_url)
                if sub_parsed and sub_url not in seen_urls:
                    sub_owner, sub_repo = sub_parsed
                    projects.append({
                        "owner": sub_owner,
                        "repo": sub_repo,
                        "name": f"{item.get('name', '')} ({key})",
                        "category": category,
                        "priority": item.get("priority", "low"),
                    })
                    seen_urls.add(sub_url)

    return projects


# =============================================================================
# Data Persistence
# =============================================================================

def get_output_path(month: int, output_dir: Path = OUTPUT_DIR) -> Path:
    """Get output file path for a month."""
    return output_dir / f"history_month_{month:02d}.json"


def load_existing_data(path: Path) -> dict:
    """Load existing history data."""
    if not path.exists():
        return {"by_year": {}}

    try:
        with open(path) as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"by_year": {}}


def save_data(path: Path, month: int, by_year: dict) -> None:
    """Save history data with summary."""
    month_name = calendar.month_name[month]

    # Calculate summary
    summary = {"by_year": {}, "total_releases": 0, "total_prs": 0, "total_commits": 0}

    for year, projects in by_year.items():
        year_stats = {"releases": 0, "prs": 0, "commits": 0, "active_repos": 0}
        for proj in projects.values():
            r = len(proj.get("releases", []))
            p = len(proj.get("merged_prs", []))
            c = len(proj.get("commits", []))
            year_stats["releases"] += r
            year_stats["prs"] += p
            year_stats["commits"] += c
            if r or p or c:
                year_stats["active_repos"] += 1
        summary["by_year"][year] = year_stats
        summary["total_releases"] += year_stats["releases"]
        summary["total_prs"] += year_stats["prs"]
        summary["total_commits"] += year_stats["commits"]

    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "month": month,
        "month_name": month_name,
        "years_covered": sorted(by_year.keys()),
        "summary": summary,
        "by_year": by_year,
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(output, f, indent=2)


# =============================================================================
# Main
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Fetch historical project activity for a specific month",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python3 scripts/fetch_month_history.py --month 12
    python3 scripts/fetch_month_history.py --month 12 --delay 1.0
    python3 scripts/fetch_month_history.py --month 12 --skip-commits
        """,
    )
    parser.add_argument("--month", type=int, required=True, choices=range(1, 13),
                        metavar="N", help="Month to fetch (1-12)")
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY,
                        help=f"Delay between API requests (default: {DEFAULT_DELAY}s)")
    parser.add_argument("--github-token", default=os.environ.get("GITHUB_TOKEN"),
                        help="GitHub token (or set GITHUB_TOKEN env var)")
    parser.add_argument("--skip-commits", action="store_true",
                        help="Skip fetching commits entirely")
    parser.add_argument("--commits-all", action="store_true",
                        help="Fetch commits for all projects (default: high priority only)")
    parser.add_argument("--projects-file", type=Path,
                        default=PROJECT_ROOT / "data" / "projects.yml",
                        help="Path to projects.yml")
    parser.add_argument("--output-dir", type=Path,
                        default=OUTPUT_DIR,
                        help=f"Output directory (default: {OUTPUT_DIR})")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be fetched without fetching")

    args = parser.parse_args()
    month_name = calendar.month_name[args.month]

    # Load projects
    print(f"Loading projects from {args.projects_file}...")
    projects = load_projects(args.projects_file)
    print(f"Found {len(projects)} projects")

    # Get date ranges
    ranges = get_month_ranges(args.month)
    print(f"\n{month_name} history: {len(ranges)} years ({ranges[0][0].year}-{ranges[-1][0].year})")

    if args.dry_run:
        print("\nDry run - would fetch:")
        for start, end in ranges:
            print(f"  {start.year}: {start.strftime('%Y-%m-%d')} to {end.strftime('%Y-%m-%d')}")
        return

    # Check token
    if not args.github_token:
        print("\nWarning: No GitHub token. Rate limits will be strict (60/hour).")
        print("Set GITHUB_TOKEN env var for 5000/hour limit.\n")

    # Load existing data
    output_path = get_output_path(args.month, args.output_dir)
    existing = load_existing_data(output_path)
    by_year = {int(k): v for k, v in existing.get("by_year", {}).items()}

    completed_years = set(by_year.keys())
    if completed_years:
        print(f"Resuming: {sorted(completed_years)} already fetched")

    # Filter to remaining years
    remaining = [(s, e) for s, e in ranges if s.year not in completed_years]
    if not remaining:
        print("All years already fetched!")
        return

    print(f"Fetching {len(remaining)} years: {[r[0].year for r in remaining]}\n")

    # Initialize API client
    api = GitHubAPI(args.github_token, args.delay)

    # Fetch each year
    for start, end in remaining:
        year = start.year
        print(f"--- {month_name} {year} ---")

        year_data = {}

        for i, proj in enumerate(projects, 1):
            owner, repo = proj["owner"], proj["repo"]
            name = proj["name"]

            # Fetch releases
            releases = api.fetch_releases(owner, repo, start, end)

            # Fetch merged PRs
            prs = api.search_merged_prs(owner, repo, start, end)

            # Fetch commits (only high priority unless --commits-all)
            commits = []
            if not args.skip_commits:
                if args.commits_all or proj["priority"] == "high":
                    commits = api.fetch_commits(owner, repo, start, end)

            # Store if any activity
            if releases or prs or commits:
                year_data[f"{owner}/{repo}"] = {
                    "name": name,
                    "category": proj["category"],
                    "releases": releases,
                    "merged_prs": prs,
                    "commits": commits,
                }
                print(f"  [{i}/{len(projects)}] {name}: {len(releases)} releases, {len(prs)} PRs, {len(commits)} commits")

        # Save incrementally
        by_year[year] = year_data
        save_data(output_path, args.month, by_year)
        print(f"  Saved {month_name} {year}\n")

    # Print summary
    print("=" * 50)
    print(f"HISTORY OF {month_name.upper()} IN NOSTR")
    print("=" * 50)

    total_prs = total_releases = 0
    for year in sorted(by_year.keys()):
        data = by_year[year]
        prs = sum(len(p.get("merged_prs", [])) for p in data.values())
        rels = sum(len(p.get("releases", [])) for p in data.values())
        total_prs += prs
        total_releases += rels
        print(f"  {year}: {rels} releases, {prs} PRs")

    print(f"\nTotal: {total_releases} releases, {total_prs} PRs")
    print(f"Output: {output_path}")
    print(f"API requests made: {api.request_count}")


if __name__ == "__main__":
    main()
