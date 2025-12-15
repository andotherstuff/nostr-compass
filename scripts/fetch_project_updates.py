#!/usr/bin/env python3
"""
Fetch recent releases and PRs from all projects in data/projects.yml.

Filters by date range using GitHub API.

Usage:
    pip install -r scripts/requirements.txt
    python3 scripts/fetch_project_updates.py --since-days N [--output-dir DIR] [--github-token TOKEN]

Environment variables:
    GITHUB_TOKEN: GitHub personal access token (optional, but recommended for rate limits)

Output files (in data/project_updates/):
    - releases.json: All fetched releases from the date range
    - pull_requests.json: All fetched PRs from the date range
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any, Optional

try:
    import requests
    import yaml
    from dotenv import load_dotenv
except ImportError:
    print("Missing dependencies. Install them with:")
    print("  pip install -r scripts/requirements.txt")
    sys.exit(1)

# Load environment variables from .env file if it exists
# Check both project root (standard) and scripts/ directory
project_root = Path(__file__).parent.parent
load_dotenv(project_root / ".env")  # Try project root first
load_dotenv(Path(__file__).parent / ".env")  # Fallback to scripts/.env

# Configuration
DEFAULT_OUTPUT_DIR = Path(__file__).parent.parent / "data" / "project_updates"
RELEASES_FILE = "releases.json"
PRS_FILE = "pull_requests.json"

# GitHub API
GITHUB_API_BASE = "https://api.github.com"
MAX_RELEASES_PER_REPO = 10
MAX_PRS_PER_REPO = 20


def parse_github_repo(repo_url: str) -> Optional[tuple[str, str]]:
    """
    Parse a GitHub repo URL and return (owner, repo) tuple.

    Handles various formats:
    - https://github.com/owner/repo
    - https://github.com/owner/repo.git
    - https://github.com/OrgName (org-level, returns None)
    - Non-GitHub URLs (returns None)
    """
    if not repo_url:
        return None

    # Handle GitHub URLs
    github_patterns = [
        r"https?://github\.com/([^/]+)/([^/\.]+?)(?:\.git)?/?$",
        r"https?://github\.com/([^/]+)/([^/]+?)/?$",
    ]

    for pattern in github_patterns:
        match = re.match(pattern, repo_url)
        if match:
            owner, repo = match.groups()
            # Filter out org-level URLs (no repo name)
            if repo and repo not in ["", "."]:
                return (owner, repo.rstrip("/"))

    return None


def get_github_headers(token: Optional[str]) -> dict[str, str]:
    """Get headers for GitHub API requests."""
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "nostr-compass-updater",
    }
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


def fetch_releases(owner: str, repo: str, headers: dict, since: Optional[str] = None) -> list[dict]:
    """Fetch recent releases for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        headers: HTTP headers for API request
        since: ISO 8601 timestamp to filter releases published after this time (client-side filter)
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/releases"
    params = {"per_page": MAX_RELEASES_PER_REPO}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        releases = response.json()

        result = [
            {
                "id": r["id"],
                "tag_name": r["tag_name"],
                "name": r["name"] or r["tag_name"],
                "published_at": r["published_at"],
                "html_url": r["html_url"],
                "prerelease": r["prerelease"],
                "draft": r["draft"],
            }
            for r in releases
            if not r["draft"]  # Skip drafts
        ]
        
        # Filter by date if since parameter provided
        if since:
            since_dt = datetime.fromisoformat(since.replace('Z', '+00:00'))
            result = [
                r for r in result
                if r["published_at"] and datetime.fromisoformat(r["published_at"].replace('Z', '+00:00')) >= since_dt
            ]
        
        return result
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return []  # Repo might not have releases
        print(f"  Warning: Failed to fetch releases for {owner}/{repo}: {e}", file=sys.stderr)
        return []
    except requests.exceptions.RequestException as e:
        print(f"  Warning: Failed to fetch releases for {owner}/{repo}: {e}", file=sys.stderr)
        return []


def fetch_pull_requests(owner: str, repo: str, headers: dict, since: Optional[str] = None) -> list[dict]:
    """Fetch recent merged PRs for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        headers: HTTP headers for API request
        since: ISO 8601 timestamp to filter PRs updated after this time (GitHub API since parameter)
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/pulls"
    params = {
        "state": "closed",
        "sort": "updated",
        "direction": "desc",
        "per_page": MAX_PRS_PER_REPO,
    }
    if since:
        params["since"] = since

    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        prs = response.json()

        result = [
            {
                "id": pr["id"],
                "number": pr["number"],
                "title": pr["title"],
                "body": (pr["body"] or "")[:500],  # Truncate long descriptions
                "merged_at": pr["merged_at"],
                "html_url": pr["html_url"],
                "user": pr["user"]["login"],
            }
            for pr in prs
            if pr["merged_at"]  # Only include merged PRs
        ]
        
        # Filter by merged_at date if since parameter provided
        # (GitHub API since filters by updated_at, but we want merged_at)
        if since:
            since_dt = datetime.fromisoformat(since.replace('Z', '+00:00'))
            result = [
                pr for pr in result
                if pr["merged_at"] and datetime.fromisoformat(pr["merged_at"].replace('Z', '+00:00')) >= since_dt
            ]
        
        return result
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return []
        print(f"  Warning: Failed to fetch PRs for {owner}/{repo}: {e}", file=sys.stderr)
        return []
    except requests.exceptions.RequestException as e:
        print(f"  Warning: Failed to fetch PRs for {owner}/{repo}: {e}", file=sys.stderr)
        return []


def load_projects(projects_file: Path) -> list[dict]:
    """Load and parse the projects.yml file, extracting all projects with GitHub repos."""
    with open(projects_file) as f:
        data = yaml.safe_load(f)

    projects = []

    for category, items in data.items():
        if not isinstance(items, list):
            continue

        for item in items:
            if not isinstance(item, dict):
                continue

            repo_url = item.get("repo")
            parsed = parse_github_repo(repo_url)

            if parsed:
                owner, repo = parsed
                projects.append({
                    "name": item.get("name", repo),
                    "category": category,
                    "owner": owner,
                    "repo": repo,
                    "repo_url": repo_url,
                    "description": item.get("description", ""),
                    "priority": item.get("priority", "low"),
                })

    return projects


def print_summary(releases: dict[str, list], prs: dict[str, list], since_days: int) -> None:
    """Print a human-readable summary."""
    total_releases = sum(len(r) for r in releases.values())
    total_prs = sum(len(p) for p in prs.values())
    repos_with_updates = set(list(releases.keys()) + list(prs.keys()))

    print("\n" + "=" * 60)
    print(f"UPDATES FROM LAST {since_days} DAYS")
    print("=" * 60)
    print()

    if total_releases == 0 and total_prs == 0:
        print("No updates found.")
        return

    print(f"Total releases: {total_releases}")
    print(f"Total merged PRs: {total_prs}")
    print(f"Repos with updates: {len(repos_with_updates)}")
    print()

    # Print releases
    if releases:
        print("-" * 40)
        print("RELEASES:")
        print("-" * 40)
        for repo_key, repo_releases in releases.items():
            for release in repo_releases:
                print(f"  [{repo_key}] {release['tag_name']}: {release['name']}")
                print(f"    {release['html_url']}")
        print()

    # Print PRs
    if prs:
        print("-" * 40)
        print("MERGED PRs:")
        print("-" * 40)
        for repo_key, repo_prs in prs.items():
            for pr in repo_prs:
                print(f"  [{repo_key}] #{pr['number']}: {pr['title']}")
                print(f"    by {pr['user']} | {pr['html_url']}")
        print()


def main():
    parser = argparse.ArgumentParser(
        description="Fetch releases and PRs from projects in data/projects.yml"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory to store output files (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--github-token",
        default=os.environ.get("GITHUB_TOKEN"),
        help="GitHub personal access token (or set GITHUB_TOKEN env var)",
    )
    parser.add_argument(
        "--projects-file",
        type=Path,
        default=Path(__file__).parent.parent / "data" / "projects.yml",
        help="Path to projects.yml file",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Don't fetch data, just show which repos would be queried",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output",
    )
    parser.add_argument(
        "--since-days",
        type=int,
        required=True,
        help="Filter to items from last N days (required)",
    )

    args = parser.parse_args()

    # Create output directory
    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Load projects
    print(f"Loading projects from {args.projects_file}...")
    projects = load_projects(args.projects_file)
    print(f"Found {len(projects)} projects with GitHub repos")

    if args.dry_run:
        print("\nProjects that would be fetched:")
        for p in projects:
            print(f"  - {p['name']} ({p['owner']}/{p['repo']})")
        return

    # Prepare headers
    headers = get_github_headers(args.github_token)
    if not args.github_token:
        print("\nWarning: No GitHub token provided. Rate limits may apply.")
        print("Set GITHUB_TOKEN environment variable or use --github-token\n")

    # Calculate since timestamp
    since_dt = datetime.now(timezone.utc) - timedelta(days=args.since_days)
    since_timestamp = since_dt.isoformat()
    print(f"\nFiltering to items from last {args.since_days} days (since {since_timestamp})\n")

    # Fetch data for each project
    all_releases: dict[str, list] = {}
    all_prs: dict[str, list] = {}

    for i, project in enumerate(projects, 1):
        repo_key = f"{project['owner']}/{project['repo']}"
        releases = fetch_releases(project["owner"], project["repo"], headers, since_timestamp)
        prs = fetch_pull_requests(project["owner"], project["repo"], headers, since_timestamp)

        all_releases[repo_key] = releases
        all_prs[repo_key] = prs

        # Only print if there are updates
        if releases or prs:
            print(f"[{i}/{len(projects)}] {repo_key}: {len(releases)} releases, {len(prs)} merged PRs")

        if args.verbose:
            for r in releases[:3]:
                print(f"    Release: {r['tag_name']} - {r['name']}")
            for pr in prs[:3]:
                print(f"    PR #{pr['number']}: {pr['title']}")

    # Print summary
    print_summary(all_releases, all_prs, args.since_days)

    # Save data files
    releases_file = args.output_dir / RELEASES_FILE
    with open(releases_file, "w") as f:
        json.dump(all_releases, f, indent=2)
    print(f"Releases saved to {releases_file}")

    prs_file = args.output_dir / PRS_FILE
    with open(prs_file, "w") as f:
        json.dump(all_prs, f, indent=2)
    print(f"PRs saved to {prs_file}")

    print("\nDone!")


if __name__ == "__main__":
    main()
