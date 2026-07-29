#!/usr/bin/env python3
"""Validate the expanded history section required in month-end newsletters."""

from __future__ import annotations

import argparse
import calendar
import re
from datetime import date, timedelta
from pathlib import Path

DATE_RE = re.compile(r"(?m)^date:\s*[\"']?(\d{4}-\d{2}-\d{2})")
HEADING_RE = re.compile(r"(?m)^(#{2,3})\s+(.+?)\s*$")
EXTERNAL_LINK_RE = re.compile(r"\[[^\]]+\]\(https?://[^)]+\)")


def is_month_end_issue(value: date) -> bool:
    """A weekly issue is month-end when its next weekly slot crosses a month."""
    return (value + timedelta(days=7)).month != value.month


def paragraph_blocks(text: str) -> list[str]:
    return [
        block.strip()
        for block in re.split(r"\n\s*\n", text)
        if block.strip() and not block.lstrip().startswith("#")
    ]


def review(markdown: str) -> list[str]:
    match = DATE_RE.search(markdown)
    if not match:
        return ["missing frontmatter date"]
    issue_date = date.fromisoformat(match.group(1))
    if not is_month_end_issue(issue_date):
        return []

    findings: list[str] = []
    if re.search(r"(?mi)^##\s+NIP Deep Dive", markdown):
        findings.append("month-end history must not be labeled NIP Deep Dive")

    expected_title = f"Six Years of Nostr {calendar.month_name[issue_date.month]}s"
    title_match = re.search(rf"(?m)^##\s+{re.escape(expected_title)}\s*$", markdown)
    if not title_match:
        findings.append(f"missing exact history heading: ## {expected_title}")
        return findings

    section_start = title_match.end()
    next_h2 = re.search(r"(?m)^##\s+", markdown[section_start:])
    section_end = section_start + next_h2.start() if next_h2 else len(markdown)
    section = markdown[section_start:section_end]
    headings = list(re.finditer(r"(?m)^###\s+(.+?)\s*$", section))
    expected_years = list(range(2021, issue_date.year + 1))

    for year in expected_years:
        label = f"{calendar.month_name[issue_date.month]} {year}"
        index = next((i for i, item in enumerate(headings) if item.group(1) == label), None)
        if index is None:
            findings.append(f"missing history year heading: ### {label}")
            continue
        body_start = headings[index].end()
        body_end = headings[index + 1].start() if index + 1 < len(headings) else len(section)
        paragraphs = paragraph_blocks(section[body_start:body_end])
        linked = [paragraph for paragraph in paragraphs if EXTERNAL_LINK_RE.search(paragraph)]
        if len(paragraphs) < 2:
            findings.append(f"{label} needs at least two substantive paragraphs")
        if len(linked) < 2:
            findings.append(f"{label} needs at least two primary-source-linked paragraphs")

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("newsletter", type=Path)
    args = parser.parse_args()
    findings = review(args.newsletter.read_text())
    if findings:
        for finding in findings:
            print(f"FAIL: {finding}")
        return 1
    print("PASS: month-end history title, years, depth, and source links are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
