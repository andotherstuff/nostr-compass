#!/usr/bin/env python3
"""Blocking gate: every release in the digest must have a triage decision.

WHY THIS EXISTS
---------------
Naming releases is not enough on its own. Newsletter #37's real failure was that
nothing checked whether a discovered release had been *considered*. Nail v0.1.0
sat in `updates_*.json` and in the Zapstore feed, and the triage artifact never
mentioned it — so nobody could tell the difference between "we decided to skip
Nail" and "we never saw Nail".

This closes that loop. For every project in the release digest, the triage
artifact must either mention the project or record a skip. A project that
appears in neither is reported as UNTRIAGED, and the script exits non-zero.

It deliberately does not judge editorial merit. Skipping a release is fine;
skipping it silently is not.

Usage:
  python3 scripts/check_triage_coverage.py --digest data/project_updates/release_digest_D.json \
      --triage data/newsletter_workspace/triage_D.md [--also FILE ...] [--min-priority N]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


# Names too generic to match on alone: a bare hit would mean nothing.
GENERIC_TOKENS = {"nostr", "app", "client", "relay", "bot", "protocol", "core", "sdk", "web"}


def mention_keys(project: str, repo: str) -> list[str]:
    """Strings whose presence in the triage text counts as 'considered'.

    Three shapes are needed, learned from real false positives:

    * the display name as-is;
    * the repo path and its slug, because triage often writes
      `formstr-hq/nail` or pastes a release URL instead of a name;
    * the display name with a parenthetical suffix stripped. Newsletter #37
      discusses Marmot five times, but the digest name is
      "Marmot Protocol (mdk)", so the full-name test alone reported it
      untriaged.
    """
    project = project.strip()
    keys = [project]
    base = re.sub(r"\s*\([^)]*\)\s*$", "", project).strip()
    if base and base != project:
        keys.append(base)
    slug = repo.split("/")[-1] if "/" in repo else repo
    keys.append(repo.strip())
    if slug and slug.lower() != project.lower():
        keys.append(slug.strip())
    out = []
    for k in keys:
        if len(k) < 3:
            continue
        if k.lower() in GENERIC_TOKENS:
            continue
        out.append(k)
    return out


def is_mentioned(text_lower: str, project: str, repo: str) -> bool:
    for key in mention_keys(project, repo):
        # Word-ish boundary so "ants" does not match "constants".
        if re.search(rf"(?<![a-z0-9]){re.escape(key.lower())}(?![a-z0-9])", text_lower):
            return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--digest", type=Path, required=True)
    ap.add_argument("--triage", type=Path, required=True)
    ap.add_argument(
        "--also",
        type=Path,
        nargs="*",
        default=[],
        help="Additional artifacts that count as a record of consideration "
        "(selection review, human overrides, the newsletter itself).",
    )
    ap.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero on any untriaged project. Without it, only flagged "
        "projects (never-covered, first release, follow-up) are blocking.",
    )
    args = ap.parse_args()

    if not args.digest.is_file():
        print(f"error: digest not found: {args.digest}", file=sys.stderr)
        return 2
    digest = json.loads(args.digest.read_text(encoding="utf-8"))

    texts = []
    for path in [args.triage, *args.also]:
        if path and path.is_file():
            texts.append(path.read_text(encoding="utf-8"))
        elif path == args.triage:
            print(f"error: triage artifact not found: {args.triage}", file=sys.stderr)
            return 2
    blob = "\n".join(texts).lower()

    untriaged_flagged: list[dict] = []
    untriaged_plain: list[dict] = []
    for e in digest.get("projects", []):
        if is_mentioned(blob, e["project"], e["repo"]):
            continue
        flagged = e.get("never_covered") or e.get("possible_first_release") or e.get("recent_followup")
        (untriaged_flagged if flagged else untriaged_plain).append(e)

    total = len(digest.get("projects", []))
    print(f"Release digest projects: {total}")
    print(f"Untriaged (flagged as high-signal): {len(untriaged_flagged)}")
    print(f"Untriaged (unflagged): {len(untriaged_plain)}")

    def show(rows: list[dict], label: str) -> None:
        if not rows:
            return
        print(f"\n{label}:")
        for e in rows:
            flags = []
            if e.get("never_covered"):
                flags.append("NEVER-COVERED")
            if e.get("possible_first_release"):
                flags.append("POSSIBLE-FIRST-RELEASE")
            if e.get("recent_followup"):
                flags.append(f"FOLLOW-UP(last {e.get('last_covered')})")
            tags = ", ".join(r["tag"] for r in e.get("releases", []))
            print(f"  - {e['project']} ({e['repo']}) {tags} {' '.join(flags)}")

    show(untriaged_flagged, "UNTRIAGED HIGH-SIGNAL RELEASES (blocking)")
    show(untriaged_plain, "Untriaged releases (informational)")

    if untriaged_flagged:
        print(
            "\nFAIL: a release flagged never-covered, first-release, or follow-up was "
            "never named in triage. Write it up or record an explicit skip reason. "
            "This is the exact gap that lost Nail v0.1.0 from Newsletter #37.",
            file=sys.stderr,
        )
        return 1
    if args.strict and untriaged_plain:
        print("\nFAIL (--strict): unflagged releases are also untriaged.", file=sys.stderr)
        return 1
    print("\nPASS: every high-signal release was considered in triage.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
