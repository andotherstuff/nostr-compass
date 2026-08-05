#!/usr/bin/env python3
"""Block known Compass filler phrases before editorial review."""

from __future__ import annotations

import argparse
from collections import namedtuple
from pathlib import Path

Finding = namedtuple("Finding", "line phrase")
BANNED_PHRASES = (
    "join Shipping This Week with",
    "developer-signed release expands the browser",
    "has been added to Compass's",
    "has been added to the tracker",
    "so later releases",
    "found via",
    "discovered through",
    "surfaced on",
)


def review(markdown: str) -> list[Finding]:
    findings: list[Finding] = []
    for number, line in enumerate(markdown.splitlines(), 1):
        lower = line.lower()
        for phrase in BANNED_PHRASES:
            if phrase.lower() in lower:
                findings.append(Finding(number, phrase))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("newsletter", type=Path)
    args = parser.parse_args()
    findings = review(args.newsletter.read_text())
    if not findings:
        print("PASS: no banned Compass filler phrases")
        return 0
    for finding in findings:
        print(f"FAIL line {finding.line}: banned phrase: {finding.phrase}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
