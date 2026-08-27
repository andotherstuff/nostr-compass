#!/usr/bin/env python3
"""Block known Compass filler phrases and opaque link anchors before editorial review."""

from __future__ import annotations

import argparse
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
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("newsletter", type=Path)
    args = parser.parse_args()
    findings = review(args.newsletter.read_text())
    if not findings:
        print("PASS: no banned Compass filler phrases or opaque link anchors")
        return 0
    for finding in findings:
        if finding.kind == "phrase":
            print(f"FAIL line {finding.line}: banned phrase: {finding.detail}")
        elif finding.kind == "link_anchor":
            print(
                f"FAIL line {finding.line}: opaque link anchor {finding.detail}; "
                "use descriptive text (see CLAUDE.md Link anchor text)"
            )
        else:
            print(
                f"FAIL line {finding.line}: bare advisory id in prose: {finding.detail}; "
                "link with descriptive anchor text instead"
            )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
