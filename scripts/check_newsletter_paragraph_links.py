#!/usr/bin/env python3
"""Require a repository or primary-source link in every prose paragraph."""

from __future__ import annotations

import argparse
import re
from collections import namedtuple
from pathlib import Path

Finding = namedtuple("Finding", "line text")

REPOSITORY_URL_RE = re.compile(
    r"https?://(?:www\.)?(?:"
    r"github\.com/[^/\s)]+/[^/\s)]+|"
    r"gitlab\.com/[^/\s)]+/[^/\s)]+|"
    r"codeberg\.org/[^/\s)]+/[^/\s)]+|"
    r"git\.nostrdev\.com/[^/\s)]+/[^/\s)]+|"
    r"gitworkshop\.dev/[^\s)]+|"
    r"[^/\s)]+/[^\s)]+/(?:commit|pull|merge_requests|releases|issues)/[^\s)]+|"
    # A first-party homepage can be the only primary source for a newly
    # launched hosted application whose source repository is private.
    r"[^/\s)]+\.[a-z]{2,}/?(?:[?#][^\s)]*)?"
    r")",
    re.IGNORECASE,
)


def prose_blocks(markdown: str) -> list[tuple[int, str]]:
    """Return non-list prose blocks outside frontmatter and fenced code."""
    lines = markdown.splitlines()
    blocks: list[tuple[int, str]] = []
    current: list[str] = []
    start = 0
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    in_fence = False

    def flush() -> None:
        nonlocal current, start
        text = " ".join(line.strip() for line in current).strip()
        if text:
            blocks.append((start, text))
        current = []
        start = 0

    for number, line in enumerate(lines, 1):
        stripped = line.strip()
        if in_frontmatter:
            if number > 1 and stripped == "---":
                in_frontmatter = False
            continue
        if stripped.startswith("```"):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not stripped:
            flush()
            continue
        if stripped.startswith(("#", "- ", "* ", ">", "---")):
            flush()
            continue
        if not current:
            start = number
        current.append(line)
    flush()
    return blocks


def review(markdown: str) -> list[Finding]:
    return [
        Finding(line, text)
        for line, text in prose_blocks(markdown)
        if not REPOSITORY_URL_RE.search(text)
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("newsletter", type=Path)
    args = parser.parse_args()
    findings = review(args.newsletter.read_text())
    if not findings:
        print("PASS: every prose paragraph links to a repository or primary source")
        return 0
    for finding in findings:
        print(f"FAIL line {finding.line}: no repository link: {finding.text[:180]}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
