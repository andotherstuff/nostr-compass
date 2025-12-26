#!/usr/bin/env python3
"""
Fetch recent updates (releases, PRs, commits) from projects in data/projects.yml.

This script collects project activity from GitHub repositories and outputs
structured data suitable for generating newsletters or activity reports.

Features:
    - Fetches releases with full release notes
    - Fetches merged PRs with full descriptions and labels
    - Fetches newly opened PRs within the time range
    - Fetches commits from the default branch
    - Filters out automated bot activity
    - Supports filtering by project name or category
    - Outputs to time-period-based files with deduplication

Usage:
    pip install -r scripts/requirements.txt

    # Auto-detect time range from last run (recommended for regular use)
    python3 scripts/fetch_project_updates.py

    # Or specify explicit time range
    python3 scripts/fetch_project_updates.py --since-days 7

    # Filter by specific projects
    python3 scripts/fetch_project_updates.py --since-days 7 --projects "Damus,Amethyst"

    # Filter by categories
    python3 scripts/fetch_project_updates.py --since-days 7 --categories "social_clients,wallets"

Environment variables:
    GITHUB_TOKEN: GitHub personal access token (recommended for rate limits)
"""

import argparse
import copy
import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

try:
    import requests
    import yaml
    from dotenv import load_dotenv
except ImportError:
    print("Missing dependencies. Install them with:")
    print("  pip install -r scripts/requirements.txt")
    sys.exit(1)


# =============================================================================
# Configuration
# =============================================================================

# Load environment variables from .env file if present
PROJECT_ROOT = Path(__file__).parent.parent
load_dotenv(PROJECT_ROOT / ".env")
load_dotenv(Path(__file__).parent / ".env")

# Output directory for update files
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "data" / "project_updates"

# GitHub API configuration
GITHUB_API_BASE = "https://api.github.com"
MAX_RELEASES_PER_REPO = 20
MAX_PRS_PER_REPO = 50
MAX_COMMITS_PER_REPO = 100

# Bot accounts to filter out from PR results
# These patterns are matched against the username (case-insensitive)
BOT_PATTERNS = [
    r".*\[bot\]$",           # GitHub Apps: dependabot[bot], renovate[bot], github-actions[bot], etc.
    r"^dependabot$",         # Dependabot (legacy, without [bot] suffix)
    r"^weblate$",            # Weblate translation bot
    r"^allcontributors$",    # All Contributors bot
]


# =============================================================================
# GitHub URL Parsing
# =============================================================================

def parse_github_repo(repo_url: str) -> Optional[tuple[str, str]]:
    """
    Extract owner and repo name from a GitHub URL.

    Handles various URL formats:
        - https://github.com/owner/repo
        - https://github.com/owner/repo.git
        - https://github.com/owner/repo/

    Returns:
        Tuple of (owner, repo) if valid GitHub repo URL, None otherwise.
        Returns None for org-level URLs or non-GitHub URLs.
    """
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
            # Filter out org-level URLs (no actual repo name)
            if repo and repo not in ["", "."]:
                return (owner, repo.rstrip("/"))

    return None


# =============================================================================
# Bot Filtering
# =============================================================================

def is_bot_user(username: str) -> bool:
    """
    Check if a username belongs to a known bot account.

    Used to filter out automated PRs from translation services,
    dependency updaters, and other automated tools.
    """
    if not username:
        return False

    username_lower = username.lower()
    for pattern in BOT_PATTERNS:
        if re.match(pattern, username_lower):
            return True
    return False


# =============================================================================
# GitHub API Helpers
# =============================================================================

def get_github_headers(token: Optional[str]) -> dict[str, str]:
    """Build headers for GitHub API requests."""
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "nostr-compass-updater",
    }
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


def get_default_branch(owner: str, repo: str, headers: dict) -> Optional[str]:
    """
    Fetch the default branch name for a repository.

    Most repos use 'main' or 'master', but this fetches the actual
    default to ensure we get commits from the right branch.
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json().get("default_branch", "main")
    except requests.exceptions.RequestException:
        return "main"  # Fallback to common default


# =============================================================================
# Data Fetching Functions
# =============================================================================

def fetch_releases(
    owner: str,
    repo: str,
    headers: dict,
    since: Optional[str] = None
) -> list[dict]:
    """
    Fetch releases for a repository.

    Includes full release notes (body) for newsletter content.
    Filters to releases published after the 'since' timestamp.

    Args:
        owner: Repository owner
        repo: Repository name
        headers: HTTP headers for API request
        since: ISO 8601 timestamp - only include releases after this time
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/releases"
    params = {"per_page": MAX_RELEASES_PER_REPO}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        releases = response.json()

        result = []
        for r in releases:
            # Skip draft releases
            if r.get("draft"):
                continue

            result.append({
                "id": r["id"],
                "tag": r["tag_name"],
                "name": r["name"] if r["name"] else r["tag_name"],
                "published_at": r["published_at"],
                "url": r["html_url"],
                "body": r.get("body") or "",  # Full release notes
                "prerelease": r["prerelease"],
                "author": r.get("author", {}).get("login", "unknown"),
            })

        # Filter by publication date
        if since:
            since_dt = datetime.fromisoformat(since.replace("Z", "+00:00"))
            result = [
                r for r in result
                if r["published_at"] and
                datetime.fromisoformat(r["published_at"].replace("Z", "+00:00")) >= since_dt
            ]

        return result

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return []  # Repo might not use releases
        print(f"  Warning: Failed to fetch releases for {owner}/{repo}: {e}", file=sys.stderr)
        return []
    except requests.exceptions.RequestException as e:
        print(f"  Warning: Failed to fetch releases for {owner}/{repo}: {e}", file=sys.stderr)
        return []


def fetch_merged_prs(
    owner: str,
    repo: str,
    headers: dict,
    since: Optional[str] = None
) -> list[dict]:
    """
    Fetch merged pull requests for a repository.

    Includes full PR descriptions and labels. Filters out bot-authored PRs.

    Args:
        owner: Repository owner
        repo: Repository name
        headers: HTTP headers for API request
        since: ISO 8601 timestamp - only include PRs merged after this time
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/pulls"
    params = {
        "state": "closed",
        "sort": "updated",
        "direction": "desc",
        "per_page": MAX_PRS_PER_REPO,
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        prs = response.json()

        result = []
        for pr in prs:
            # Only include merged PRs
            if not pr.get("merged_at"):
                continue

            # Filter out bot-authored PRs
            author = pr.get("user", {}).get("login", "")
            if is_bot_user(author):
                continue

            # Check if merged within time range
            if since:
                since_dt = datetime.fromisoformat(since.replace("Z", "+00:00"))
                merged_dt = datetime.fromisoformat(pr["merged_at"].replace("Z", "+00:00"))
                if merged_dt < since_dt:
                    continue

            # Extract labels
            labels = [label["name"] for label in pr.get("labels", [])]

            result.append({
                "id": pr["id"],
                "number": pr["number"],
                "title": pr["title"],
                "body": pr.get("body") or "",  # Full description, no truncation
                "author": author,
                "merged_at": pr["merged_at"],
                "url": pr["html_url"],
                "labels": labels,
            })

        return result

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return []
        print(f"  Warning: Failed to fetch PRs for {owner}/{repo}: {e}", file=sys.stderr)
        return []
    except requests.exceptions.RequestException as e:
        print(f"  Warning: Failed to fetch PRs for {owner}/{repo}: {e}", file=sys.stderr)
        return []


def fetch_open_prs(
    owner: str,
    repo: str,
    headers: dict,
    since: Optional[str] = None
) -> list[dict]:
    """
    Fetch open pull requests that were opened within the time range.

    Useful for tracking work-in-progress features. Filters out
    bot-authored PRs and PRs opened before the time range.

    Args:
        owner: Repository owner
        repo: Repository name
        headers: HTTP headers for API request
        since: ISO 8601 timestamp - only include PRs opened after this time
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/pulls"
    params = {
        "state": "open",
        "sort": "created",
        "direction": "desc",
        "per_page": MAX_PRS_PER_REPO,
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        prs = response.json()

        result = []
        for pr in prs:
            # Filter out bot-authored PRs
            author = pr.get("user", {}).get("login", "")
            if is_bot_user(author):
                continue

            # Check if opened within time range
            created_at = pr.get("created_at")
            if since and created_at:
                since_dt = datetime.fromisoformat(since.replace("Z", "+00:00"))
                created_dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
                if created_dt < since_dt:
                    continue

            # Extract labels
            labels = [label["name"] for label in pr.get("labels", [])]

            result.append({
                "id": pr["id"],
                "number": pr["number"],
                "title": pr["title"],
                "body": pr.get("body") or "",
                "author": author,
                "opened_at": created_at,
                "url": pr["html_url"],
                "labels": labels,
                "draft": pr.get("draft", False),
            })

        return result

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return []
        print(f"  Warning: Failed to fetch open PRs for {owner}/{repo}: {e}", file=sys.stderr)
        return []
    except requests.exceptions.RequestException as e:
        print(f"  Warning: Failed to fetch open PRs for {owner}/{repo}: {e}", file=sys.stderr)
        return []


def fetch_commits(
    owner: str,
    repo: str,
    headers: dict,
    since: Optional[str] = None,
    branch: Optional[str] = None
) -> list[dict]:
    """
    Fetch commits from the default branch within the time range.

    Includes full commit messages (not just the first line) and
    basic statistics. Useful for projects that push directly
    without using pull requests.

    Args:
        owner: Repository owner
        repo: Repository name
        headers: HTTP headers for API request
        since: ISO 8601 timestamp - only include commits after this time
        branch: Branch to fetch from (defaults to repo's default branch)
    """
    # Get default branch if not specified
    if not branch:
        branch = get_default_branch(owner, repo, headers)

    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/commits"
    params = {
        "sha": branch,
        "per_page": MAX_COMMITS_PER_REPO,
    }
    if since:
        params["since"] = since

    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        commits = response.json()

        result = []
        for c in commits:
            commit_data = c.get("commit", {})
            author_data = commit_data.get("author", {})

            # Get the full commit message (includes body after first line)
            message = commit_data.get("message", "")

            result.append({
                "sha": c.get("sha", "")[:12],  # Short SHA for readability
                "message": message,
                "author": author_data.get("name", "unknown"),
                "date": author_data.get("date"),
                "url": c.get("html_url", ""),
            })

        return result

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return []
        print(f"  Warning: Failed to fetch commits for {owner}/{repo}: {e}", file=sys.stderr)
        return []
    except requests.exceptions.RequestException as e:
        print(f"  Warning: Failed to fetch commits for {owner}/{repo}: {e}", file=sys.stderr)
        return []


# =============================================================================
# Project Loading and Filtering
# =============================================================================

def load_projects(
    projects_file: Path,
    filter_projects: Optional[list[str]] = None,
    filter_categories: Optional[list[str]] = None
) -> list[dict]:
    """
    Load projects from the YAML file with optional filtering.

    Extracts project metadata needed for newsletter context:
    name, description, category, priority, website, maintainer.

    Args:
        projects_file: Path to projects.yml
        filter_projects: Optional list of project names to include
        filter_categories: Optional list of categories to include
    """
    with open(projects_file) as f:
        data = yaml.safe_load(f)

    projects = []

    for category, items in data.items():
        if not isinstance(items, list):
            continue

        # Apply category filter if specified
        if filter_categories and category not in filter_categories:
            continue

        for item in items:
            if not isinstance(item, dict):
                continue

            # Apply project name filter if specified
            project_name = item.get("name", "")
            if filter_projects and project_name not in filter_projects:
                continue

            repo_url = item.get("repo")
            parsed = parse_github_repo(repo_url)

            if parsed:
                owner, repo = parsed
                projects.append({
                    # GitHub identifiers
                    "owner": owner,
                    "repo": repo,
                    "repo_url": repo_url,
                    # Project metadata for newsletter context
                    "name": project_name or repo,
                    "description": item.get("description", ""),
                    "category": category,
                    "priority": item.get("priority", "low"),
                    "website": item.get("website", ""),
                    "maintainer": item.get("maintainer", ""),
                    "status": item.get("status", ""),
                })

    return projects


# =============================================================================
# Output File Management
# =============================================================================

def get_filter_suffix(
    filter_projects: Optional[list[str]] = None,
    filter_categories: Optional[list[str]] = None
) -> str:
    """
    Generate a filename suffix based on active filters.

    This keeps filtered runs separate from full runs to avoid confusion.

    Examples:
        No filters: "" (empty)
        --projects "Damus,Amethyst": "_Damus_Amethyst"
        --categories "wallets": "_wallets"
        Both: "_wallets_Damus_Amethyst"
    """
    parts = []

    if filter_categories:
        parts.extend(sorted(filter_categories))

    if filter_projects:
        parts.extend(sorted(filter_projects))

    if parts:
        # Sanitize names: replace spaces/special chars with dashes
        sanitized = [re.sub(r'[^a-zA-Z0-9-]', '-', p) for p in parts]
        return "_" + "_".join(sanitized)

    return ""


def get_output_filename(
    since_date: datetime,
    until_date: datetime,
    filter_projects: Optional[list[str]] = None,
    filter_categories: Optional[list[str]] = None
) -> str:
    """
    Generate filename based on the time period and filters.

    Format: updates_YYYY-MM-DD_YYYY-MM-DD[_filter_suffix].json

    Examples:
        Full run: updates_2024-12-18_2024-12-25.json
        Filtered: updates_2024-12-18_2024-12-25_Damus_Amethyst.json
    """
    start_str = since_date.strftime("%Y-%m-%d")
    end_str = until_date.strftime("%Y-%m-%d")
    suffix = get_filter_suffix(filter_projects, filter_categories)
    return f"updates_{start_str}_{end_str}{suffix}.json"


def get_last_run_date(
    output_dir: Path,
    filter_projects: Optional[list[str]] = None,
    filter_categories: Optional[list[str]] = None
) -> Optional[datetime]:
    """
    Find the most recent update file matching the same filter pattern.

    Only considers files with the same filter suffix to avoid confusion
    between full runs and filtered runs.

    We use the START date (not end date) to ensure overlap and avoid gaps.
    This means some entries may appear in multiple files, but that's
    preferable to missing data between runs.

    Returns None if no previous matching files exist.
    """
    suffix = get_filter_suffix(filter_projects, filter_categories)

    # Build pattern to match files with this specific suffix
    if suffix:
        # Escape the suffix for regex (in case of special chars)
        escaped_suffix = re.escape(suffix)
        pattern = re.compile(rf"updates_(\d{{4}}-\d{{2}}-\d{{2}})_(\d{{4}}-\d{{2}}-\d{{2}}){escaped_suffix}\.json")
    else:
        # Full run: match files WITHOUT any suffix after the date
        pattern = re.compile(r"updates_(\d{4}-\d{2}-\d{2})_(\d{4}-\d{2}-\d{2})\.json$")

    latest_start = None

    for filepath in output_dir.glob("updates_*.json"):
        match = pattern.match(filepath.name)
        if match:
            start_str, end_str = match.groups()
            try:
                # Use the START date to ensure overlap
                start_date = datetime.strptime(start_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
                if latest_start is None or start_date > latest_start:
                    latest_start = start_date
            except ValueError:
                continue

    return latest_start


def load_existing_data(filepath: Path) -> Optional[dict]:
    """Load existing update file for deduplication."""
    if not filepath.exists():
        return None

    try:
        with open(filepath) as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: Could not load existing file {filepath}: {e}", file=sys.stderr)
        return None


def merge_and_deduplicate(existing: dict, new: dict) -> dict:
    """
    Merge new data into existing data, removing duplicates.

    Deduplication is based on item IDs within each category
    (releases, merged_prs, open_prs, commits).
    """
    if not existing:
        return new

    # Deep copy to avoid modifying the original data
    merged = copy.deepcopy(existing)

    # Update metadata
    merged["generated_at"] = new["generated_at"]

    # Merge project data
    for repo_key, new_project in new.get("projects", {}).items():
        if repo_key not in merged.get("projects", {}):
            merged.setdefault("projects", {})[repo_key] = new_project
            continue

        existing_project = merged["projects"][repo_key]

        # Update project metadata from new data (in case it changed)
        for key in ["name", "description", "category", "priority", "website", "maintainer"]:
            if key in new_project:
                existing_project[key] = new_project[key]

        # Merge each data type, deduplicating by ID
        for data_type in ["releases", "merged_prs", "open_prs", "commits"]:
            existing_items = existing_project.get(data_type, [])
            new_items = new_project.get(data_type, [])

            # Build set of existing IDs for fast lookup
            # Use 'id' for PRs/releases, 'sha' for commits
            id_key = "sha" if data_type == "commits" else "id"
            existing_ids = {item.get(id_key) for item in existing_items}

            # Add new items that don't already exist
            for item in new_items:
                if item.get(id_key) not in existing_ids:
                    existing_items.append(item)

            existing_project[data_type] = existing_items

    # Recalculate summary
    merged["summary"] = calculate_summary(merged.get("projects", {}))

    return merged


def calculate_summary(projects: dict) -> dict:
    """Calculate aggregate statistics across all projects."""
    total_releases = 0
    total_merged_prs = 0
    total_open_prs = 0
    total_commits = 0
    active_repos = 0

    for project in projects.values():
        releases = len(project.get("releases", []))
        merged = len(project.get("merged_prs", []))
        opened = len(project.get("open_prs", []))
        commits = len(project.get("commits", []))

        total_releases += releases
        total_merged_prs += merged
        total_open_prs += opened
        total_commits += commits

        if releases or merged or opened or commits:
            active_repos += 1

    return {
        "total_releases": total_releases,
        "total_merged_prs": total_merged_prs,
        "total_open_prs": total_open_prs,
        "total_commits": total_commits,
        "active_repos": active_repos,
    }


# =============================================================================
# Main Execution
# =============================================================================

def print_summary(data: dict, since_days: int) -> None:
    """Print a human-readable summary to the console."""
    summary = data.get("summary", {})

    print("\n" + "=" * 60)
    print(f"UPDATES FROM LAST {since_days} DAYS")
    print("=" * 60)
    print()

    if summary.get("active_repos", 0) == 0:
        print("No updates found.")
        return

    print(f"Active repositories: {summary.get('active_repos', 0)}")
    print(f"Releases: {summary.get('total_releases', 0)}")
    print(f"Merged PRs: {summary.get('total_merged_prs', 0)}")
    print(f"Open PRs: {summary.get('total_open_prs', 0)}")
    print(f"Commits: {summary.get('total_commits', 0)}")
    print()

    # List repos with activity
    print("-" * 40)
    print("REPOSITORIES WITH ACTIVITY:")
    print("-" * 40)

    for repo_key, project in data.get("projects", {}).items():
        releases = len(project.get("releases", []))
        merged = len(project.get("merged_prs", []))
        opened = len(project.get("open_prs", []))
        commits = len(project.get("commits", []))

        if releases or merged or opened or commits:
            parts = []
            if releases:
                parts.append(f"{releases} releases")
            if merged:
                parts.append(f"{merged} merged PRs")
            if opened:
                parts.append(f"{opened} open PRs")
            if commits:
                parts.append(f"{commits} commits")

            print(f"  {project.get('name', repo_key)}: {', '.join(parts)}")

    print()


def main():
    parser = argparse.ArgumentParser(
        description="Fetch project updates from GitHub for newsletter generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Fetch last 7 days of updates
  python3 fetch_project_updates.py --since-days 7

  # Fetch updates for specific projects only
  python3 fetch_project_updates.py --since-days 7 --projects "Damus,Amethyst,Primal"

  # Fetch updates for specific categories
  python3 fetch_project_updates.py --since-days 7 --categories "social_clients,wallets"

  # Combine filters
  python3 fetch_project_updates.py --since-days 14 --categories "libraries" --projects "NDK"
        """
    )

    parser.add_argument(
        "--since-days",
        type=int,
        default=None,
        help="Fetch updates from the last N days. If not specified, auto-detects from last run.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Output directory (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--projects-file",
        type=Path,
        default=PROJECT_ROOT / "data" / "projects.yml",
        help="Path to projects.yml file",
    )
    parser.add_argument(
        "--projects",
        type=str,
        help="Comma-separated list of project names to include",
    )
    parser.add_argument(
        "--categories",
        type=str,
        help="Comma-separated list of categories to include",
    )
    parser.add_argument(
        "--github-token",
        default=os.environ.get("GITHUB_TOKEN"),
        help="GitHub personal access token (or set GITHUB_TOKEN env var)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show which repos would be queried without fetching",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed progress",
    )

    args = parser.parse_args()

    # Parse filter arguments
    filter_projects = None
    if args.projects:
        filter_projects = [p.strip() for p in args.projects.split(",")]

    filter_categories = None
    if args.categories:
        filter_categories = [c.strip() for c in args.categories.split(",")]

    # Create output directory
    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Auto-detect since_days from last run if not specified
    if args.since_days is None:
        last_run = get_last_run_date(args.output_dir, filter_projects, filter_categories)
        if last_run:
            # Calculate days since last run's start date (for overlap)
            now = datetime.now(timezone.utc)
            days_diff = (now - last_run).days
            # Minimum 1 day, add 1 day buffer for safety
            args.since_days = max(1, days_diff + 1)
            print(f"Auto-detected: last run started {last_run.strftime('%Y-%m-%d')}, fetching {args.since_days} days")
        else:
            # No previous runs with this filter, default to 7 days
            args.since_days = 7
            print(f"No previous runs found for this filter, defaulting to {args.since_days} days")

    # Load and filter projects
    print(f"Loading projects from {args.projects_file}...")
    projects = load_projects(args.projects_file, filter_projects, filter_categories)
    print(f"Found {len(projects)} projects with GitHub repos")

    if filter_projects:
        print(f"  Filtered to projects: {', '.join(filter_projects)}")
    if filter_categories:
        print(f"  Filtered to categories: {', '.join(filter_categories)}")

    if not projects:
        print("No matching projects found.")
        return

    if args.dry_run:
        print("\nProjects that would be fetched:")
        for p in projects:
            print(f"  - {p['name']} ({p['owner']}/{p['repo']}) [{p['category']}]")
        return

    # Prepare API headers
    headers = get_github_headers(args.github_token)
    if not args.github_token:
        print("\nWarning: No GitHub token provided. Rate limits may apply.")
        print("Set GITHUB_TOKEN environment variable or use --github-token\n")

    # Calculate time range
    now = datetime.now(timezone.utc)
    since_dt = now - timedelta(days=args.since_days)
    since_timestamp = since_dt.isoformat()

    print(f"\nFetching updates since {since_dt.strftime('%Y-%m-%d')}...\n")

    # Fetch data for each project
    all_projects: dict[str, dict] = {}

    for i, project in enumerate(projects, 1):
        repo_key = f"{project['owner']}/{project['repo']}"

        if args.verbose:
            print(f"[{i}/{len(projects)}] Fetching {repo_key}...")

        # Fetch all data types
        releases = fetch_releases(project["owner"], project["repo"], headers, since_timestamp)
        merged_prs = fetch_merged_prs(project["owner"], project["repo"], headers, since_timestamp)
        open_prs = fetch_open_prs(project["owner"], project["repo"], headers, since_timestamp)
        commits = fetch_commits(project["owner"], project["repo"], headers, since_timestamp)

        # Only include projects with some activity
        if releases or merged_prs or open_prs or commits:
            all_projects[repo_key] = {
                # Project metadata for context
                "name": project["name"],
                "description": project["description"],
                "category": project["category"],
                "priority": project["priority"],
                "website": project["website"],
                "maintainer": project["maintainer"],
                # Activity data
                "releases": releases,
                "merged_prs": merged_prs,
                "open_prs": open_prs,
                "commits": commits,
            }

            if not args.verbose:
                print(f"[{i}/{len(projects)}] {project['name']}: "
                      f"{len(releases)} releases, {len(merged_prs)} merged PRs, "
                      f"{len(open_prs)} open PRs, {len(commits)} commits")

    # Build output data structure
    output_data = {
        "generated_at": now.isoformat(),
        "period": {
            "start": since_dt.strftime("%Y-%m-%d"),
            "end": now.strftime("%Y-%m-%d"),
            "days": args.since_days,
        },
        "summary": calculate_summary(all_projects),
        "projects": all_projects,
    }

    # Determine output file and handle deduplication
    output_filename = get_output_filename(since_dt, now, filter_projects, filter_categories)
    output_path = args.output_dir / output_filename

    existing_data = load_existing_data(output_path)
    if existing_data:
        print(f"\nMerging with existing data in {output_filename}...")
        output_data = merge_and_deduplicate(existing_data, output_data)

    # Write output file
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)

    print(f"\nOutput saved to {output_path}")

    # Print summary
    print_summary(output_data, args.since_days)

    print("Done!")


if __name__ == "__main__":
    main()
