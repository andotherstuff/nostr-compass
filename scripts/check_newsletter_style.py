#!/usr/bin/env python3
"""Block known Compass filler phrases and opaque link anchors before editorial review."""

from __future__ import annotations

import argparse
import json
import re
from collections import namedtuple
from pathlib import Path

Finding = namedtuple("Finding", "line kind detail")
BANNED_PHRASES = (
    "join Shipping This Week with",
    "developer-signed release expands the browser",
    "has been added to Compass's",
    "has been added to the tracker",
    "so later releases",
    "found via",
    "discovered through",
    "surfaced on",
    "made the final scope cut",
    "nothing from it appears",
    "in compass at all",
    "no nostr surface, so nothing",
    "did not qualify",
    "was not included",
    "outside the reporting window",
)
LINK_ANCHOR_ID_RE = re.compile(
    r"\[(?:GHSA-[a-z0-9-]+|CVE-\d{4}-\d+)\]\(",
    re.IGNORECASE,
)
BARE_GHSA_PROSE_RE = re.compile(
    r"(?<![\[/\w-])(GHSA-[a-z0-9-]{4,})(?![\]/\w-])",
    re.IGNORECASE,
)
ORDINAL_GHSA_RE = re.compile(
    r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten|first|second|third|"
    r"highest|lowest|most serious|several)\s*,\s*GHSA-",
    re.IGNORECASE,
)
ROOT = Path(__file__).parents[1]
SPEC_SECTION_HEADING = "## Protocol and Spec Work"
GITHUB_CHANGE_URL_RE = re.compile(
    r"https://github\.com/([^/\s)]+/[^/\s)]+)/(pull/\d+|commit/[0-9a-f]{7,40})"
    r"(?:[?#][^\s)]*)?",
    re.IGNORECASE,
)


def _spec_repositories() -> frozenset[str]:
    config = json.loads((ROOT / "data" / "spec_sources.json").read_text())
    return frozenset(
        family["repo"].casefold() for family in config["spec_families"]
    )


SPEC_REPOSITORIES = _spec_repositories()
GENERIC_SPEC_HEADINGS = frozenset(
    {
        "nips",
        "nips repository",
        "nostr implementation possibilities (nips)",
        "buds",
        "blossom upgrade documents",
        "blossom upgrade documents (buds)",
        "naps",
        "napplet application proposals",
        "napplet application proposals (naps)",
        "marmot",
        "mips",
        "marmot improvement proposals",
        "marmot improvement proposals (mips)",
        "gamma markets",
        "cord",
        "cord specs",
        "concord",
        "concord (cord specs)",
        "nwc",
        "nostr wallet connect",
        "nostr wallet connect (nwc)",
    }
)


def _review_spec_headings(markdown: str) -> list[Finding]:
    """Require one descriptive H3 for each tracked specification change."""
    findings: list[Finding] = []
    in_section = False
    heading: str | None = None
    heading_line = 0
    pull_changes: set[str] = set()
    commit_changes: set[str] = set()

    def finish_heading() -> None:
        if heading is None or not (pull_changes or commit_changes):
            return
        if heading.casefold() in GENERIC_SPEC_HEADINGS:
            findings.append(
                Finding(
                    heading_line,
                    "generic_spec_heading",
                    heading,
                )
            )
        primary_changes = pull_changes | commit_changes
        if len(primary_changes) > 1:
            findings.append(
                Finding(
                    heading_line,
                    "grouped_spec_changes",
                    f"{heading}: {len(primary_changes)} changes",
                )
            )

    for number, line in enumerate(markdown.splitlines(), 1):
        if line.strip() == SPEC_SECTION_HEADING:
            in_section = True
            continue
        if not in_section:
            continue
        if line.startswith("## "):
            finish_heading()
            break
        if line.startswith("### "):
            finish_heading()
            heading = line[4:].strip()
            heading_line = number
            pull_changes = set()
            commit_changes = set()
            continue
        for match in GITHUB_CHANGE_URL_RE.finditer(line):
            repo = match.group(1).casefold()
            if repo not in SPEC_REPOSITORIES:
                continue
            change = f"{repo}/{match.group(2).casefold()}"
            if heading is None:
                findings.append(
                    Finding(
                        number,
                        "missing_spec_heading",
                        change,
                    )
                )
            elif "/pull/" in change:
                pull_changes.add(change)
            else:
                commit_changes.add(change)
    else:
        if in_section:
            finish_heading()
    return findings


def review(markdown: str) -> list[Finding]:
    findings: list[Finding] = []
    for number, line in enumerate(markdown.splitlines(), 1):
        lower = line.lower()
        for phrase in BANNED_PHRASES:
            if phrase.lower() in lower:
                findings.append(Finding(number, "phrase", phrase))
        for match in LINK_ANCHOR_ID_RE.finditer(line):
            findings.append(
                Finding(number, "link_anchor", match.group(0).strip("["))
            )
        for match in ORDINAL_GHSA_RE.finditer(line):
            findings.append(Finding(number, "bare_ghsa", match.group(0)))
        for match in BARE_GHSA_PROSE_RE.finditer(line):
            if LINK_ANCHOR_ID_RE.search(line):
                continue
            findings.append(Finding(number, "bare_ghsa", match.group(1)))
    findings.extend(_review_spec_headings(markdown))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("newsletter", type=Path)
    args = parser.parse_args()
    findings = review(args.newsletter.read_text())
    if not findings:
        print(
            "PASS: no banned Compass filler phrases, opaque link anchors, "
            "or grouped specification changes"
        )
        return 0
    for finding in findings:
        if finding.kind == "phrase":
            print(f"FAIL line {finding.line}: banned phrase: {finding.detail}")
        elif finding.kind == "link_anchor":
            print(
                f"FAIL line {finding.line}: opaque link anchor {finding.detail}; "
                "use descriptive text (see CLAUDE.md Link anchor text)"
            )
        elif finding.kind == "generic_spec_heading":
            print(
                f"FAIL line {finding.line}: generic specification-family heading "
                f"{finding.detail!r}; name the individual change"
            )
        elif finding.kind == "grouped_spec_changes":
            print(
                f"FAIL line {finding.line}: grouped specification changes "
                f"({finding.detail}); give each change its own descriptive H3"
            )
        elif finding.kind == "missing_spec_heading":
            print(
                f"FAIL line {finding.line}: specification change {finding.detail} "
                "appears before an H3; give it its own descriptive H3"
            )
        else:
            print(
                f"FAIL line {finding.line}: bare advisory id in prose: {finding.detail}; "
                "link with descriptive anchor text instead"
            )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
