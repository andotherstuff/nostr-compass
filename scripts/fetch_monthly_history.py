#!/usr/bin/env python3
"""Collect same-calendar-month GitHub commit candidates for Nostr history research."""

from __future__ import annotations

import argparse
import calendar
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def month_windows(month: int, start_year: int, through_year: int) -> list[tuple[int, str, str]]:
    windows = []
    for year in range(start_year, through_year + 1):
        start = f"{year:04d}-{month:02d}-01T00:00:00Z"
        next_year, next_month = (year + 1, 1) if month == 12 else (year, month + 1)
        end = f"{next_year:04d}-{next_month:02d}-01T00:00:00Z"
        windows.append((year, start, end))
    return windows


def normalize_pages(pages: list[list[dict[str, Any]]]) -> list[dict[str, str]]:
    rows = []
    for page in pages:
        for item in page:
            commit = item.get("commit") or {}
            author = commit.get("author") or {}
            rows.append(
                {
                    "sha": item.get("sha", ""),
                    "date": author.get("date", ""),
                    "author": author.get("name", ""),
                    "title": (commit.get("message") or "").splitlines()[0],
                    "url": item.get("html_url", ""),
                }
            )
    return rows


def gh_commits(repo: str, since: str, until: str) -> list[dict[str, str]]:
    command = [
        "gh",
        "api",
        "--method",
        "GET",
        "--paginate",
        f"repos/{repo}/commits",
        "-f",
        f"since={since}",
        "-f",
        f"until={until}",
        "-f",
        "per_page=100",
        "--jq",
        ".[] | @json",
    ]
    result = subprocess.run(command, capture_output=True, text=True, timeout=120)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or f"gh api failed for {repo}")
    items = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
    return normalize_pages([items])


def collect(config: dict[str, Any], month: int, start_year: int, through_year: int) -> dict[str, Any]:
    repositories = []
    for source in config["repositories"]:
        yearly = []
        for year, since, until in month_windows(month, start_year, through_year):
            try:
                commits = gh_commits(source["repo"], since, until)
                yearly.append({"year": year, "commits": commits})
            except (RuntimeError, subprocess.TimeoutExpired, json.JSONDecodeError) as exc:
                yearly.append({"year": year, "commits": [], "error": str(exc)})
        repositories.append({**source, "years": yearly})
    return {
        "month": month,
        "month_name": calendar.month_name[month],
        "start_year": start_year,
        "through_year": through_year,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repositories": repositories,
        "instructions": config.get("instructions", []),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--month", type=int, required=True, choices=range(1, 13))
    parser.add_argument("--start-year", type=int, default=2021)
    parser.add_argument("--through-year", type=int, required=True)
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).parents[1] / "data" / "monthly_history_sources.json",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.through_year < args.start_year:
        parser.error("--through-year must be >= --start-year")
    config = json.loads(args.config.read_text())
    report = collect(config, args.month, args.start_year, args.through_year)
    output = args.output or (
        Path(__file__).parents[1]
        / "data"
        / "history_research"
        / f"{args.through_year}-{args.month:02d}-candidates.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n")
    commits = sum(len(year["commits"]) for repo in report["repositories"] for year in repo["years"])
    errors = sum("error" in year for repo in report["repositories"] for year in repo["years"])
    print(f"{output}: {commits} commit candidates, {errors} source-window errors")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
