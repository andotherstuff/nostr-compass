#!/usr/bin/env python3
"""Fetch weekly activity for every tracked Nostr-adjacent spec family."""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import subprocess
from typing import Any

ROOT = Path(__file__).parents[1]
DEFAULT_CONFIG = ROOT / "data" / "spec_sources.json"
OUTPUT_DIR = ROOT / "data" / "spec_updates"


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def in_window(value: str | None, since: str, until: str) -> bool:
    if not value:
        return False
    return parse_time(since) <= parse_time(value) < parse_time(until)


def family_result(
    family: dict[str, str],
    commits: list[dict[str, Any]],
    pulls: list[dict[str, Any]],
    since: str,
    until: str,
) -> dict[str, Any]:
    selected_pulls = []
    for pull in pulls:
        if not any(in_window(pull.get(field), since, until) for field in ("created_at", "updated_at", "merged_at")):
            continue
        selected_pulls.append(
            {
                "number": pull["number"],
                "title": pull["title"],
                "state": "merged" if pull.get("merged_at") else pull.get("state", "open"),
                "created_at": pull.get("created_at"),
                "updated_at": pull.get("updated_at"),
                "merged_at": pull.get("merged_at"),
                "url": pull["html_url"],
            }
        )
    selected_commits = [
        {
            "sha": commit["sha"],
            "date": commit["commit"]["author"]["date"],
            "title": commit["commit"]["message"].splitlines()[0],
            "url": commit["html_url"],
        }
        for commit in commits
        if in_window(commit["commit"]["author"]["date"], since, until)
    ]
    return {
        **family,
        "status": "active" if selected_commits or selected_pulls else "quiet",
        "window": {"since": since, "until": until},
        "commits": selected_commits,
        "pull_requests": selected_pulls,
    }


def gh_json(endpoint: str) -> Any:
    result = subprocess.run(
        ["gh", "api", endpoint],
        check=True,
        text=True,
        capture_output=True,
    )
    return json.loads(result.stdout)


def fetch_family(family: dict[str, str], since: str, until: str) -> dict[str, Any]:
    repo = family["repo"]
    commits = gh_json(f"repos/{repo}/commits?since={since}&until={until}&per_page=100")
    pulls = gh_json(f"repos/{repo}/pulls?state=all&sort=updated&direction=desc&per_page=100")
    return family_result(family, commits, pulls, since, until)


def iso_midnight(day: datetime) -> str:
    return day.astimezone(timezone.utc).strftime("%Y-%m-%dT00:00:00Z")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--since-days", type=int, default=8)
    parser.add_argument("--until", help="exclusive UTC date (YYYY-MM-DD)")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    args = parser.parse_args()

    until_day = (
        datetime.strptime(args.until, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        if args.until
        else datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    )
    since_day = until_day - timedelta(days=args.since_days)
    since = iso_midnight(since_day)
    until = iso_midnight(until_day)

    config = json.loads(args.config.read_text())
    families = [fetch_family(family, since, until) for family in config["spec_families"]]
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "window": {"since": since, "until": until},
        "families": families,
    }
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output = OUTPUT_DIR / f"spec_updates_{until_day.strftime('%Y-%m-%d')}.json"
    output.write_text(json.dumps(payload, indent=2) + "\n")
    for family in families:
        print(
            f"{family['name']}: {family['status']} "
            f"({len(family['pull_requests'])} PRs, {len(family['commits'])} commits)"
        )
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
