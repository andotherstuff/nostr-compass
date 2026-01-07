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
import json
import os
import re
import signal
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

# Default max length for body text (PR descriptions, release notes)
# Set to 0 for unlimited (default - preserves full context for agent analysis)
DEFAULT_BODY_MAX_LENGTH = 0

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


def truncate_body(text: str, max_length: int = DEFAULT_BODY_MAX_LENGTH) -> str:
    """
    Truncate body text to reduce output size for agent consumption.

    Args:
        text: The text to truncate
        max_length: Maximum length (0 = unlimited)

    Returns:
        Truncated text with "..." if it was cut off
    """
    if not text or max_length == 0:
        return text or ""

    if len(text) <= max_length:
        return text

    # Try to cut at a word boundary
    truncated = text[:max_length].rsplit(' ', 1)[0]
    return truncated + "..."


# =============================================================================
# GitHub API Helpers
# =============================================================================

# Rate limit configuration
RATE_LIMIT_BUFFER = 50  # Start slowing down when this many requests remain
RATE_LIMIT_SLEEP = 60   # Seconds to sleep when rate limited

# Request configuration
REQUEST_TIMEOUT = 60    # Seconds to wait for API response
MAX_RETRIES = 3         # Number of retries for transient failures
RETRY_DELAY = 5         # Seconds to wait between retries


def get_github_headers(token: Optional[str]) -> dict[str, str]:
    """Build headers for GitHub API requests."""
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "nostr-compass-updater",
    }
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


def request_with_retry(
    url: str,
    headers: dict,
    params: Optional[dict] = None,
    verbose: bool = False
) -> Optional[requests.Response]:
    """
    Make a GET request with retry logic for transient failures.

    Retries on timeouts and connection errors.
    Returns None if all retries fail.
    """
    last_error = None

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url, headers=headers, params=params, timeout=REQUEST_TIMEOUT)
            return response
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            last_error = e
            if attempt < MAX_RETRIES - 1:
                if verbose:
                    print(f"  Retry {attempt + 1}/{MAX_RETRIES} after error: {e}", file=sys.stderr)
                time.sleep(RETRY_DELAY * (attempt + 1))  # Exponential backoff
            continue

    if last_error:
        print(f"  Failed after {MAX_RETRIES} retries: {last_error}", file=sys.stderr)
    return None


def check_rate_limit(response: requests.Response, verbose: bool = False) -> None:
    """
    Check rate limit headers and sleep if necessary.

    GitHub returns these headers:
        X-RateLimit-Limit: Total requests allowed per hour
        X-RateLimit-Remaining: Requests remaining in current window
        X-RateLimit-Reset: Unix timestamp when the limit resets
    """
    remaining = response.headers.get("X-RateLimit-Remaining")
    reset_time = response.headers.get("X-RateLimit-Reset")

    if remaining is None:
        return

    remaining = int(remaining)

    if remaining <= 0 and reset_time:
        # We're rate limited - wait until reset
        reset_ts = int(reset_time)
        wait_seconds = max(0, reset_ts - int(time.time())) + 5  # Add 5s buffer
        print(f"  Rate limited! Waiting {wait_seconds}s until reset...", file=sys.stderr)
        time.sleep(wait_seconds)
    elif remaining < RATE_LIMIT_BUFFER:
        # Getting low - add a small delay
        if verbose:
            print(f"  Rate limit low ({remaining} remaining), adding delay...", file=sys.stderr)
        time.sleep(1)


def parse_link_header(link_header: str) -> dict[str, str]:
    """
    Parse the GitHub Link header for pagination.

    The Link header looks like:
        <https://api.github.com/repos/owner/repo/pulls?page=2>; rel="next",
        <https://api.github.com/repos/owner/repo/pulls?page=5>; rel="last"

    Returns:
        Dict mapping rel values to URLs, e.g., {"next": "...", "last": "..."}
    """
    links = {}
    if not link_header:
        return links

    for part in link_header.split(","):
        part = part.strip()
        if not part:
            continue

        # Split into URL and rel parts
        try:
            url_part, rel_part = part.split(";")
            url = url_part.strip().strip("<>")
            rel = rel_part.strip().split("=")[1].strip('"')
            links[rel] = url
        except (ValueError, IndexError):
            continue

    return links


def get_default_branch(owner: str, repo: str, headers: dict) -> Optional[str]:
    """
    Fetch the default branch name for a repository.

    Most repos use 'main' or 'master', but this fetches the actual
    default to ensure we get commits from the right branch.
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    response = request_with_retry(url, headers)
    if response is None:
        return "main"  # Fallback to common default
    try:
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
    since: Optional[str] = None,
    verbose: bool = False
) -> list[dict]:
    """
    Fetch releases for a repository with pagination support.

    Includes full release notes (body) for newsletter content.
    Filters to releases published after the 'since' timestamp.

    Args:
        owner: Repository owner
        repo: Repository name
        headers: HTTP headers for API request
        since: ISO 8601 timestamp - only include releases after this time
        verbose: Whether to print detailed progress
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/releases"
    params = {"per_page": 100}  # Max allowed by GitHub API
    result = []
    since_dt = None
    if since:
        since_dt = datetime.fromisoformat(since.replace("Z", "+00:00"))

    while url:
        response = request_with_retry(url, headers, params, verbose)
        if response is None:
            print(f"  Warning: Failed to fetch releases for {owner}/{repo}", file=sys.stderr)
            break

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                break  # Repo might not use releases
            print(f"  Warning: Failed to fetch releases for {owner}/{repo}: {e}", file=sys.stderr)
            break

        check_rate_limit(response, verbose)

        releases = response.json()
        if not releases:
            break

        for r in releases:
            # Skip draft releases
            if r.get("draft"):
                continue

            published_at = r.get("published_at")

            # Early termination: if we've gone past our time range, stop paginating
            if since_dt and published_at:
                pub_dt = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
                if pub_dt < since_dt:
                    # Releases are sorted by date desc, so we can stop
                    url = None
                    break

            result.append({
                "id": r["id"],
                "tag": r["tag_name"],
                "name": r["name"] if r["name"] else r["tag_name"],
                "published_at": published_at,
                "url": r["html_url"],
                "body": truncate_body(r.get("body") or ""),
                "prerelease": r["prerelease"],
                "author": r.get("author", {}).get("login", "unknown"),
            })

        # Check for next page
        if url:
            links = parse_link_header(response.headers.get("Link", ""))
            url = links.get("next")
            params = {}  # URL already contains params

    # Final filter by publication date (in case of any edge cases)
    if since_dt:
        result = [
            r for r in result
            if r["published_at"] and
            datetime.fromisoformat(r["published_at"].replace("Z", "+00:00")) >= since_dt
        ]

    return result


def fetch_merged_prs(
    owner: str,
    repo: str,
    headers: dict,
    since: Optional[str] = None,
    verbose: bool = False
) -> list[dict]:
    """
    Fetch merged pull requests for a repository with pagination support.

    Includes full PR descriptions and labels. Filters out bot-authored PRs.

    Args:
        owner: Repository owner
        repo: Repository name
        headers: HTTP headers for API request
        since: ISO 8601 timestamp - only include PRs merged after this time
        verbose: Whether to print detailed progress
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/pulls"
    params = {
        "state": "closed",
        "sort": "updated",
        "direction": "desc",
        "per_page": 100,  # Max allowed by GitHub API
    }
    result = []
    since_dt = None
    if since:
        since_dt = datetime.fromisoformat(since.replace("Z", "+00:00"))

    while url:
        response = request_with_retry(url, headers, params, verbose)
        if response is None:
            print(f"  Warning: Failed to fetch PRs for {owner}/{repo}", file=sys.stderr)
            break

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                break
            print(f"  Warning: Failed to fetch PRs for {owner}/{repo}: {e}", file=sys.stderr)
            break

        check_rate_limit(response, verbose)

        prs = response.json()
        if not prs:
            break

        # Track if we've gone past our time range
        past_time_range = False

        for pr in prs:
            # Only include merged PRs
            if not pr.get("merged_at"):
                continue

            # Filter out bot-authored PRs
            author = pr.get("user", {}).get("login", "")
            if is_bot_user(author):
                continue

            # Check if merged within time range
            merged_at = pr["merged_at"]
            if since_dt:
                merged_dt = datetime.fromisoformat(merged_at.replace("Z", "+00:00"))
                if merged_dt < since_dt:
                    # Since we're sorting by updated desc, we might still find
                    # PRs merged in our range that were updated earlier.
                    # But if the updated_at is also before our range, we can stop.
                    updated_at = pr.get("updated_at", merged_at)
                    updated_dt = datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
                    if updated_dt < since_dt:
                        past_time_range = True
                        break
                    continue

            # Extract labels
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

        # Stop if we've gone past our time range
        if past_time_range:
            break

        # Check for next page
        links = parse_link_header(response.headers.get("Link", ""))
        url = links.get("next")
        params = {}  # URL already contains params

    return result


def fetch_open_prs(
    owner: str,
    repo: str,
    headers: dict,
    since: Optional[str] = None,
    verbose: bool = False
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
        verbose: Whether to print detailed progress
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/pulls"
    params = {
        "state": "open",
        "sort": "created",
        "direction": "desc",
        "per_page": 100,  # Max allowed by GitHub API
    }
    result = []
    since_dt = None
    if since:
        since_dt = datetime.fromisoformat(since.replace("Z", "+00:00"))

    while url:
        response = request_with_retry(url, headers, params, verbose)
        if response is None:
            print(f"  Warning: Failed to fetch open PRs for {owner}/{repo}", file=sys.stderr)
            break

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                break
            print(f"  Warning: Failed to fetch open PRs for {owner}/{repo}: {e}", file=sys.stderr)
            break

        check_rate_limit(response, verbose)

        prs = response.json()
        if not prs:
            break

        # Track if we've gone past our time range
        past_time_range = False

        for pr in prs:
            # Filter out bot-authored PRs
            author = pr.get("user", {}).get("login", "")
            if is_bot_user(author):
                continue

            # Check if opened within time range
            created_at = pr.get("created_at")
            if since_dt and created_at:
                created_dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
                if created_dt < since_dt:
                    # Sorted by created desc, so we can stop
                    past_time_range = True
                    break

            # Extract labels
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

        # Stop if we've gone past our time range
        if past_time_range:
            break

        # Check for next page
        links = parse_link_header(response.headers.get("Link", ""))
        url = links.get("next")
        params = {}  # URL already contains params

    return result


def fetch_commits(
    owner: str,
    repo: str,
    headers: dict,
    since: Optional[str] = None,
    branch: Optional[str] = None,
    verbose: bool = False
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
        verbose: Whether to print detailed progress
    """
    # Get default branch if not specified
    if not branch:
        branch = get_default_branch(owner, repo, headers)

    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/commits"
    params = {
        "sha": branch,
        "per_page": 100,  # Max allowed by GitHub API
    }
    if since:
        params["since"] = since

    result = []

    while url:
        response = request_with_retry(url, headers, params, verbose)
        if response is None:
            print(f"  Warning: Failed to fetch commits for {owner}/{repo}", file=sys.stderr)
            break

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                break
            print(f"  Warning: Failed to fetch commits for {owner}/{repo}: {e}", file=sys.stderr)
            break

        check_rate_limit(response, verbose)

        commits = response.json()
        if not commits:
            break

        for c in commits:
            commit_data = c.get("commit", {})
            author_data = commit_data.get("author", {})

            # Get just the first line of commit message (summary)
            message = commit_data.get("message", "")
            message_summary = message.split("\n")[0] if message else ""

            result.append({
                "sha": c.get("sha", "")[:12],  # Short SHA for readability
                "message": message_summary,
                "author": author_data.get("name", "unknown"),
                "date": author_data.get("date"),
                "url": c.get("html_url", ""),
            })

        # Check for next page
        links = parse_link_header(response.headers.get("Link", ""))
        url = links.get("next")
        params = {}  # URL already contains params

    return result


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

            # Track which repo URLs we've added to avoid duplicates
            added_urls = set()

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
                added_urls.add(repo_url)

            # Also process the 'repos' dictionary if present
            repos_dict = item.get("repos", {})
            if isinstance(repos_dict, dict):
                for repo_key, sub_repo_url in repos_dict.items():
                    # Skip if we already added this repo URL
                    if sub_repo_url in added_urls:
                        continue

                    sub_parsed = parse_github_repo(sub_repo_url)
                    if sub_parsed:
                        sub_owner, sub_repo = sub_parsed
                        projects.append({
                            # GitHub identifiers
                            "owner": sub_owner,
                            "repo": sub_repo,
                            "repo_url": sub_repo_url,
                            # Project metadata for newsletter context
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
# Output File Management
# =============================================================================

def get_output_filename(
    since_date: datetime,
    until_date: datetime,
    filter_projects: Optional[list[str]] = None,
    filter_categories: Optional[list[str]] = None
) -> str:
    """
    Generate filename based on the time period.

    Format: updates_YYYY-MM-DD_YYYY-MM-DD.json

    All runs for the same date range go to the same file, regardless of
    filters. This allows incremental fetching with different filters
    that all contribute to one output file.
    """
    start_str = since_date.strftime("%Y-%m-%d")
    end_str = until_date.strftime("%Y-%m-%d")
    return f"updates_{start_str}_{end_str}.json"


def get_last_run_date(
    output_dir: Path,
    filter_projects: Optional[list[str]] = None,
    filter_categories: Optional[list[str]] = None
) -> Optional[datetime]:
    """
    Find the most recent update file.

    We use the START date (not end date) to ensure overlap and avoid gaps.
    This means some entries may appear in multiple files, but that's
    preferable to missing data between runs.

    Returns None if no previous files exist.
    """
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
    """Load existing update file for resume support."""
    if not filepath.exists():
        return None

    try:
        with open(filepath) as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: Could not load existing file {filepath}: {e}", file=sys.stderr)
        return None


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
    parser.add_argument(
        "--fresh",
        action="store_true",
        help="Start fresh, ignoring any previous partial runs",
    )
    parser.add_argument(
        "--compact",
        action="store_true",
        help="Compact output: skip commits and open PRs (reduces size for agent consumption)",
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

    # Determine output file path upfront (for incremental saves)
    output_filename = get_output_filename(since_dt, now, filter_projects, filter_categories)
    output_path = args.output_dir / output_filename

    # Load existing data for resume support (unless --fresh)
    existing_data = None
    already_fetched = set()
    if not args.fresh:
        existing_data = load_existing_data(output_path)
        if existing_data:
            already_fetched = set(existing_data.get("projects", {}).keys())
            if already_fetched:
                print(f"Resuming: {len(already_fetched)} repos already fetched, skipping them")
                print(f"  (use --fresh to start over)")

    print(f"\nFetching updates since {since_dt.strftime('%Y-%m-%d')}...\n")

    # Initialize output structure (will be updated incrementally)
    all_projects: dict[str, dict] = {}
    if existing_data:
        all_projects = existing_data.get("projects", {})

    # Track if we were interrupted
    interrupted = False

    def save_progress():
        """Save current progress to file."""
        output_data = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "period": {
                "start": since_dt.strftime("%Y-%m-%d"),
                "end": now.strftime("%Y-%m-%d"),
                "days": args.since_days,
            },
            "summary": calculate_summary(all_projects),
            "projects": all_projects,
        }
        with open(output_path, "w") as f:
            json.dump(output_data, f, indent=2)

    def handle_interrupt(signum, frame):
        """Handle Ctrl+C gracefully."""
        nonlocal interrupted
        interrupted = True
        print("\n\nInterrupted! Saving progress...", file=sys.stderr)
        save_progress()
        print(f"Progress saved to {output_path}", file=sys.stderr)
        print(f"Run the same command again to resume.", file=sys.stderr)
        sys.exit(130)  # Standard exit code for Ctrl+C

    # Register signal handler for graceful interruption
    signal.signal(signal.SIGINT, handle_interrupt)

    # Fetch data for each project
    for i, project in enumerate(projects, 1):
        repo_key = f"{project['owner']}/{project['repo']}"

        # Skip already fetched repos (resume support)
        if repo_key in already_fetched:
            if args.verbose:
                print(f"[{i}/{len(projects)}] Skipping {repo_key} (already fetched)")
            continue

        if args.verbose:
            print(f"[{i}/{len(projects)}] Fetching {repo_key}...")

        # Fetch all data types (skip some in compact mode)
        releases = fetch_releases(project["owner"], project["repo"], headers, since_timestamp, args.verbose)
        merged_prs = fetch_merged_prs(project["owner"], project["repo"], headers, since_timestamp, args.verbose)

        # In compact mode, skip open PRs and commits to reduce output size
        if args.compact:
            open_prs = []
            commits = []
        else:
            open_prs = fetch_open_prs(project["owner"], project["repo"], headers, since_timestamp, args.verbose)
            commits = fetch_commits(project["owner"], project["repo"], headers, since_timestamp, verbose=args.verbose)

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

    # Final save
    save_progress()

    print(f"\nOutput saved to {output_path}")

    # Print summary
    print_summary({"projects": all_projects, "summary": calculate_summary(all_projects)}, args.since_days)

    print("Done!")


if __name__ == "__main__":
    main()
