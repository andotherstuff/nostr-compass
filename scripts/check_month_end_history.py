#!/usr/bin/env python3
"""Validate Compass month-end history depth, sourcing, and narrative shape."""

from __future__ import annotations

import argparse
import calendar
import re
from datetime import date, timedelta
from pathlib import Path

DATE_RE = re.compile(r"(?m)^date:\s*(\d{4}-\d{2}-\d{2})\s*$")
HISTORY_RE = re.compile(r"(?m)^##\s+([A-Za-z]+|\d+) Years of Nostr ([A-Za-z]+)\s*$")
YEAR_RE = re.compile(r"(?m)^###\s+([A-Za-z]+)\s+(20\d{2})(?::[^\n]+)?\s*$")
URL_RE = re.compile(r"https?://[^)\]\s>]+")
PROGRESSION_RE = re.compile(
    r"\b(?:by|from|through|shift(?:ed)?|mov(?:e|ed)|turn(?:ed)?|became|laid|built|"
    r"expand(?:ed)?|matur(?:e|ed)|transition(?:ed)?|stage|cycle|foundation|enabled)\b",
    re.IGNORECASE,
)
NUMBER_WORDS = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
}


def parse_issue_date(markdown: str) -> date:
    match = DATE_RE.search(markdown)
    if not match:
        raise ValueError("newsletter frontmatter has no ISO date")
    return date.fromisoformat(match.group(1))


def is_final_weekly_issue(value: date) -> bool:
    return (value + timedelta(days=7)).month != value.month


def plural_month(month: int) -> str:
    name = calendar.month_name[month]
    if name == "January":
        return "Januaries"
    if name == "February":
        return "Februaries"
    if name == "March":
        return "Marches"
    return f"{name}s"


def prose_paragraphs(markdown: str) -> list[str]:
    paragraphs = []
    for block in re.split(r"\n\s*\n", markdown):
        value = block.strip()
        if not value or value.startswith("#") or value.startswith("---"):
            continue
        paragraphs.append(value)
    return paragraphs


def extract_history(markdown: str) -> tuple[re.Match[str] | None, str]:
    match = HISTORY_RE.search(markdown)
    if not match:
        return None, ""
    remainder = markdown[match.end():]
    next_h2 = re.search(r"(?m)^##\s+", remainder)
    separator = re.search(r"(?m)^---\s*$", remainder)
    ends = [m.start() for m in (next_h2, separator) if m]
    return match, remainder[: min(ends) if ends else len(remainder)]


def review(markdown: str) -> list[str]:
    findings: list[str] = []
    try:
        issue_date = parse_issue_date(markdown)
    except ValueError as exc:
        return [str(exc)]

    history_match, history = extract_history(markdown)
    required = is_final_weekly_issue(issue_date)
    has_deep_dive = bool(re.search(r"(?mi)^##\s+.*NIP Deep Dive", markdown))

    if required and has_deep_dive:
        findings.append("final weekly issue must use history, not NIP Deep Dive")
    if not history_match:
        if required:
            findings.append("missing exact month-end history title")
        return findings

    title_month = history_match.group(2)
    month_lookup = {plural_month(i).lower(): i for i in range(1, 13)}
    history_month = month_lookup.get(title_month.lower())
    if history_month is None:
        findings.append(f"history title has unsupported month plural: {title_month}")
        return findings

    expected_years = list(range(2021, issue_date.year + 1))
    count_label = NUMBER_WORDS.get(len(expected_years), str(len(expected_years)))
    expected_title = f"{count_label} Years of Nostr {plural_month(history_month)}"
    actual_title = f"{history_match.group(1)} Years of Nostr {title_month}"
    if actual_title != expected_title:
        findings.append(f"history title must be '{expected_title}'")

    year_matches = list(YEAR_RE.finditer(history))
    found_years = [int(match.group(2)) for match in year_matches]
    if found_years != expected_years:
        findings.append(f"history years must be {expected_years}; found {found_years}")
    for match in year_matches:
        expected_month = calendar.month_name[history_month]
        if match.group(1) != expected_month:
            findings.append(f"year heading must use {expected_month}, not {match.group(1)}")

    intro = history[: year_matches[0].start()] if year_matches else history
    intro_paragraphs = prose_paragraphs(intro)
    if not intro_paragraphs or sum(len(p.split()) for p in intro_paragraphs) < 70:
        findings.append("history needs a sourced narrative introduction of at least 70 words")
    for paragraph in intro_paragraphs:
        if not URL_RE.search(paragraph):
            findings.append("history introduction paragraph lacks a primary-source link")
    if intro_paragraphs and not PROGRESSION_RE.search(" ".join(intro_paragraphs)):
        findings.append("history introduction does not state a progressive arc")

    all_h3 = list(re.finditer(r"(?m)^###\s+[^\n]+$", history))
    for index, match in enumerate(year_matches):
        year = int(match.group(2))
        next_heading = next((heading.start() for heading in all_h3 if heading.start() > match.start()), len(history))
        body = history[match.end():next_heading]
        paragraphs = prose_paragraphs(body)
        label = f"{calendar.month_name[history_month]} {year}"
        if len(paragraphs) < 2:
            findings.append(f"{label} needs at least two sourced prose paragraphs, not a laundry list")
        for paragraph_index, paragraph in enumerate(paragraphs, 1):
            if len(paragraph.split()) < 30:
                findings.append(f"{label} paragraph {paragraph_index} is too thin for researched history")
            if not URL_RE.search(paragraph):
                findings.append(f"{label} paragraph {paragraph_index} lacks a primary-source link")
        if paragraphs and not PROGRESSION_RE.search(" ".join(paragraphs)):
            findings.append(f"{label} does not explain progression or transition")
        if re.search(r"(?m)^\s*[-*]\s+", body):
            findings.append(f"{label} uses bullets; history must be narrative prose")

    if year_matches:
        last = year_matches[-1]
        conclusion_start = next(
            (heading.end() for heading in all_h3 if heading.start() > last.start()),
            len(history),
        )
        conclusion_paragraphs = prose_paragraphs(history[conclusion_start:])
        for paragraph in conclusion_paragraphs:
            if not URL_RE.search(paragraph):
                findings.append("history conclusion paragraph lacks a primary-source link")

    if len(history.split()) < 900:
        findings.append("history section is too short; require at least 900 words")
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
    print("PASS: month-end history title, yearly depth, sourcing, and progressive narrative are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
