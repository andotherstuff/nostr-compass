#!/usr/bin/env python3
"""
Fetch recent releases and PRs from all projects in _data/projects.yml.

Tracks changes between runs and generates a diff showing "what's new since last run".

Usage:
    pip install -r scripts/requirements.txt
    python scripts/fetch_project_updates.py [--output-dir DIR] [--github-token TOKEN]

Environment variables:
    GITHUB_TOKEN: GitHub personal access token (optional, but recommended for rate limits)

Output files (in _data/project_updates/):
    - state.json: Full state from last run (used to compute diffs)
    - diff.json: Changes since last run
    - releases.json: All fetched releases
    - pull_requests.json: All fetched PRs
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import requests
    import yaml
except ImportError:
    print("Missing dependencies. Install them with:")
    print("  pip install -r scripts/requirements.txt")
    sys.exit(1)

# Configuration
DEFAULT_OUTPUT_DIR = Path(__file__).parent.parent / "_data" / "project_updates"
STATE_FILE = "state.json"
DIFF_FILE = "diff.json"
RELEASES_FILE = "releases.json"
PRS_FILE = "pull_requests.json"

# GitHub API
GITHUB_API_BASE = "https://api.github.com"
MAX_RELEASES_PER_REPO = 10
MAX_PRS_PER_REPO = 20


def parse_github_repo(repo_url: str) -> tuple[str, str] | None:
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


def get_github_headers(token: str | None) -> dict[str, str]:
    """Get headers for GitHub API requests."""
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "nostr-compass-updater",
    }
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


def fetch_releases(owner: str, repo: str, headers: dict) -> list[dict]:
    """Fetch recent releases for a repository."""
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/releases"
    params = {"per_page": MAX_RELEASES_PER_REPO}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        releases = response.json()

        return [
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
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return []  # Repo might not have releases
        print(f"  Warning: Failed to fetch releases for {owner}/{repo}: {e}", file=sys.stderr)
        return []
    except requests.exceptions.RequestException as e:
        print(f"  Warning: Failed to fetch releases for {owner}/{repo}: {e}", file=sys.stderr)
        return []


def fetch_pull_requests(owner: str, repo: str, headers: dict) -> list[dict]:
    """Fetch recent merged PRs for a repository."""
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

        return [
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


def load_state(output_dir: Path) -> dict:
    """Load the previous state from disk."""
    state_file = output_dir / STATE_FILE
    if state_file.exists():
        with open(state_file) as f:
            return json.load(f)
    return {"last_run": None, "releases": {}, "pull_requests": {}}


def save_state(output_dir: Path, state: dict) -> None:
    """Save the current state to disk."""
    state_file = output_dir / STATE_FILE
    with open(state_file, "w") as f:
        json.dump(state, f, indent=2)


def compute_diff(old_data: dict, new_data: dict, key_field: str) -> dict:
    """
    Compute the diff between old and new data.

    Returns:
        {
            "added": [...],      # New items
            "removed": [...],    # Items no longer present
        }
    """
    old_keys = {item[key_field] for item in old_data} if old_data else set()
    new_keys = {item[key_field] for item in new_data} if new_data else set()

    new_items_map = {item[key_field]: item for item in new_data} if new_data else {}
    old_items_map = {item[key_field]: item for item in old_data} if old_data else {}

    added_keys = new_keys - old_keys
    removed_keys = old_keys - new_keys

    return {
        "added": [new_items_map[k] for k in added_keys],
        "removed": [old_items_map[k] for k in removed_keys],
    }


def generate_diff_report(
    old_state: dict,
    new_releases: dict[str, list],
    new_prs: dict[str, list],
) -> dict:
    """Generate a comprehensive diff report."""
    diff = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "previous_run": old_state.get("last_run"),
        "releases": {},
        "pull_requests": {},
        "summary": {
            "new_releases": 0,
            "new_prs": 0,
            "repos_with_updates": set(),
        },
    }

    # Compare releases
    old_releases = old_state.get("releases", {})
    for repo_key, releases in new_releases.items():
        old_repo_releases = old_releases.get(repo_key, [])
        repo_diff = compute_diff(old_repo_releases, releases, "id")

        if repo_diff["added"] or repo_diff["removed"]:
            diff["releases"][repo_key] = repo_diff
            diff["summary"]["new_releases"] += len(repo_diff["added"])
            if repo_diff["added"]:
                diff["summary"]["repos_with_updates"].add(repo_key)

    # Compare PRs
    old_prs = old_state.get("pull_requests", {})
    for repo_key, prs in new_prs.items():
        old_repo_prs = old_prs.get(repo_key, [])
        repo_diff = compute_diff(old_repo_prs, prs, "id")

        if repo_diff["added"] or repo_diff["removed"]:
            diff["pull_requests"][repo_key] = repo_diff
            diff["summary"]["new_prs"] += len(repo_diff["added"])
            if repo_diff["added"]:
                diff["summary"]["repos_with_updates"].add(repo_key)

    # Convert set to list for JSON serialization
    diff["summary"]["repos_with_updates"] = list(diff["summary"]["repos_with_updates"])

    return diff


def print_diff_summary(diff: dict) -> None:
    """Print a human-readable summary of the diff."""
    summary = diff["summary"]

    print("\n" + "=" * 60)
    print("WHAT'S NEW SINCE LAST RUN")
    print("=" * 60)

    if diff["previous_run"]:
        print(f"Previous run: {diff['previous_run']}")
    else:
        print("Previous run: (first run)")
    print(f"Current run:  {diff['generated_at']}")
    print()

    if summary["new_releases"] == 0 and summary["new_prs"] == 0:
        print("No new updates found.")
        return

    print(f"Total new releases: {summary['new_releases']}")
    print(f"Total new merged PRs: {summary['new_prs']}")
    print(f"Repos with updates: {len(summary['repos_with_updates'])}")
    print()

    # Print new releases
    if diff["releases"]:
        print("-" * 40)
        print("NEW RELEASES:")
        print("-" * 40)
        for repo_key, repo_diff in diff["releases"].items():
            for release in repo_diff["added"]:
                print(f"  [{repo_key}] {release['tag_name']}: {release['name']}")
                print(f"    {release['html_url']}")
        print()

    # Print new PRs
    if diff["pull_requests"]:
        print("-" * 40)
        print("NEW MERGED PRs:")
        print("-" * 40)
        for repo_key, repo_diff in diff["pull_requests"].items():
            for pr in repo_diff["added"]:
                print(f"  [{repo_key}] #{pr['number']}: {pr['title']}")
                print(f"    by {pr['user']} | {pr['html_url']}")
        print()


def main():
    parser = argparse.ArgumentParser(
        description="Fetch releases and PRs from projects in _data/projects.yml"
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
        default=Path(__file__).parent.parent / "_data" / "projects.yml",
        help="Path to projects.yml file",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Don't save state, just show what would be fetched",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output",
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

    # Load previous state
    old_state = load_state(args.output_dir)

    # Prepare headers
    headers = get_github_headers(args.github_token)
    if not args.github_token:
        print("\nWarning: No GitHub token provided. Rate limits may apply.")
        print("Set GITHUB_TOKEN environment variable or use --github-token\n")

    # Fetch data for each project
    all_releases: dict[str, list] = {}
    all_prs: dict[str, list] = {}

    for i, project in enumerate(projects, 1):
        repo_key = f"{project['owner']}/{project['repo']}"
        print(f"[{i}/{len(projects)}] Fetching {repo_key}...", end=" ", flush=True)

        releases = fetch_releases(project["owner"], project["repo"], headers)
        prs = fetch_pull_requests(project["owner"], project["repo"], headers)

        all_releases[repo_key] = releases
        all_prs[repo_key] = prs

        print(f"{len(releases)} releases, {len(prs)} merged PRs")

        if args.verbose:
            for r in releases[:3]:
                print(f"    Release: {r['tag_name']} - {r['name']}")
            for pr in prs[:3]:
                print(f"    PR #{pr['number']}: {pr['title']}")

    # Generate diff
    diff = generate_diff_report(old_state, all_releases, all_prs)

    # Print summary
    print_diff_summary(diff)

    # Save new state
    new_state = {
        "last_run": datetime.now(timezone.utc).isoformat(),
        "releases": all_releases,
        "pull_requests": all_prs,
    }

    save_state(args.output_dir, new_state)
    print(f"\nState saved to {args.output_dir / STATE_FILE}")

    # Save diff
    diff_file = args.output_dir / DIFF_FILE
    with open(diff_file, "w") as f:
        json.dump(diff, f, indent=2)
    print(f"Diff saved to {diff_file}")

    # Save full data files for reference
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
