#!/usr/bin/env python3
"""
Build coverage_history.json from past newsletters.

For each project linked in content/en/newsletters/*.md, record:
  - first_mention_date  : ISO date of earliest newsletter mentioning it
  - last_mention_date   : ISO date of most recent newsletter mentioning it
  - mention_count       : total number of newsletters that mention it
  - newsletters         : list of (date, newsletter_filename) pairs

Project identity comes from repository URLs found in newsletter markdown.
GitHub, Codeberg, Sourcehut, and GitLab are all captured. All forms collapse
to host/owner/repo.

Used by Change B (novelty bonus) in the AnalystAgent scoring rubric.

Usage:
  python3 scripts/build_coverage_history.py
  python3 scripts/build_coverage_history.py --validate

Output:
  data/coverage_history.json
"""

import argparse
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

PROJECT_ROOT = Path(__file__).resolve().parent.parent
NEWSLETTERS_DIR = PROJECT_ROOT / "content" / "en" / "newsletters"
OUTPUT_FILE = PROJECT_ROOT / "data" / "coverage_history.json"

# Match repo URLs on GitHub, Codeberg, Sourcehut, GitLab.
# Sourcehut uses ~user/repo format.
REPO_URL_RE = re.compile(
    r"https?://"
    r"(?P<host>github\.com|codeberg\.org|gitlab\.com|sr\.ht)"
    r"/"
    r"(?P<path>~?[\w.\-]+/[\w.\-]+)"
    r"(?:/[^\s)\"'#]*)?",
    re.IGNORECASE,
)

NEWSLETTER_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-newsletter\.md$")


def normalize_project_id(host: str, path: str) -> str:
    """Canonical id like 'github.com/damus-io/damus' (lowercased)."""
    path = path.strip("/").lower()
    if path.endswith(".git"):
        path = path[: -len(".git")]
    return f"{host.lower()}/{path}"


def extract_projects_from_newsletter(md_path: Path) -> set[str]:
    text = md_path.read_text(encoding="utf-8")
    projects: set[str] = set()
    for m in REPO_URL_RE.finditer(text):
        pid = normalize_project_id(m.group("host"), m.group("path"))
        # nostr-protocol/nips conflates as a project; NIP rotation is tracked
        # separately in MEMORY.md
        if pid == "github.com/nostr-protocol/nips":
            continue
        projects.add(pid)
    return projects


def build_history() -> dict:
    if not NEWSLETTERS_DIR.is_dir():
        raise SystemExit(f"Newsletters directory missing: {NEWSLETTERS_DIR}")

    by_project: dict[str, list[tuple[str, str]]] = defaultdict(list)
    newsletter_count = 0

    for md_path in sorted(NEWSLETTERS_DIR.glob("*.md")):
        name = md_path.name
        date_match = NEWSLETTER_DATE_RE.match(name)
        if not date_match:
            continue
        date = date_match.group(1)
        newsletter_count += 1
        for pid in extract_projects_from_newsletter(md_path):
            by_project[pid].append((date, name))

    history: dict[str, dict] = {}
    for pid, entries in by_project.items():
        entries.sort(key=lambda e: e[0])
        dates = [d for d, _ in entries]
        history[pid] = {
            "first_mention_date": dates[0],
            "last_mention_date": dates[-1],
            "mention_count": len(entries),
            "newsletters": [{"date": d, "file": f} for d, f in entries],
        }

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "newsletter_count": newsletter_count,
        "project_count": len(history),
        "projects": history,
    }


def self_test(history: dict) -> int:
    """Self-test required by plan: must find >= 100 distinct projects.
    Below that, parsing is likely broken (format change, regex drift)."""
    pcount = history["project_count"]
    ncount = history["newsletter_count"]
    print(f"Self-test: {pcount} projects across {ncount} newsletters", file=sys.stderr)
    if pcount < 100:
        print(
            f"FAIL: expected >= 100 distinct projects, got {pcount}. "
            "Parser likely broken (newsletter format change?)",
            file=sys.stderr,
        )
        return 1
    if ncount < 10:
        print(f"FAIL: expected >= 10 newsletters, got {ncount}", file=sys.stderr)
        return 1
    print("Self-test: PASS", file=sys.stderr)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Build history and run self-test only; do not write output",
    )
    args = parser.parse_args()

    history = build_history()

    if args.validate:
        return self_test(history)

    rc = self_test(history)
    if rc != 0:
        print(
            "Refusing to write coverage_history.json with failed self-test",
            file=sys.stderr,
        )
        return rc

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        json.dumps(history, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {OUTPUT_FILE}", file=sys.stderr)
    print(
        f"  {history['project_count']} projects across {history['newsletter_count']} newsletters",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
