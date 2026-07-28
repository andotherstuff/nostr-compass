#!/usr/bin/env python3
"""Flag repeated project coverage that lacks a new primary source.

This is an editorial gate, not a prose scorer. A project repeated from the
prior issue must cite a new release, pull request, commit, or other primary
source in its own section. Reusing the same primary-source URL is also a
blocking duplicate. The reviewer decides whether a distinct source carries
enough substance to keep the item.
"""

from __future__ import annotations

import argparse
import re
from collections import namedtuple
from pathlib import Path

Finding = namedtuple("Finding", "project reason")

HEADING_RE = re.compile(r"^###\s+(.+)$", re.MULTILINE)
LINK_LABEL_RE = re.compile(r"\[([^\]]+)\]\([^\)]+\)")
PRIMARY_URL_RE = re.compile(
    r"(?:https?://[^\s)]+/(?:releases(?:/tag)?|pull|commit|merge_requests|-/commit)(?:/[^\s)]*)?"
    r"|https?://primal\.net/e/[0-9a-f]+)"
)


def sections(markdown: str) -> list[tuple[str, str]]:
    """Return each H3 heading and its body, stopping at the next H3 or H2."""
    headings = list(HEADING_RE.finditer(markdown))
    result = []
    for index, match in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(markdown)
        body = markdown[match.end() : end]
        body = body.split("\n## ", 1)[0]
        result.append((match.group(1), body))
    return result


def canonical_project_name(label: str) -> str:
    """Remove a trailing version or editorial action phrase from a heading label."""
    boundary = re.match(
        r"^(.*?)(?:(?:\s+v?\d+\.\d+(?:\.\d+)?(?:[-.][A-Za-z0-9]+)?)\b|"
        r"\s+(?:adds|brings|builds|cuts|fixes|gets|keeps|lands|launches|moves|opens|"
        r"pairs|recovers|rewrites|ships|tightens|turns|updates|widens)\b)",
        label,
        re.IGNORECASE,
    )
    return (boundary.group(1) if boundary else label).strip()


def heading_project(heading: str, known_projects: set[str] | None = None) -> str | None:
    """Extract a project label from a linked heading or a known-project prefix."""
    linked = LINK_LABEL_RE.search(heading)
    if linked:
        return canonical_project_name(linked.group(1).strip())
    if known_projects:
        heading_folded = heading.casefold()
        matches = [project for project in known_projects if heading_folded.startswith(project.casefold())]
        if matches:
            return max(matches, key=len)
    return canonical_project_name(heading)


def has_new_primary_source(body: str) -> bool:
    """A repeated item needs a directly linked release, PR, or commit."""
    return bool(PRIMARY_URL_RE.search(body))


def review(current: str, previous: str) -> list[Finding]:
    previous_projects = {
        project
        for heading, _ in sections(previous)
        if (project := heading_project(heading)) is not None
    }
    findings = []
    for heading, body in sections(current):
        project = heading_project(heading, previous_projects)
        if project and project in previous_projects and not has_new_primary_source(body):
            findings.append(Finding(project, "no new primary source"))
    return findings


def primary_urls(markdown: str) -> set[str]:
    return {url.rstrip(".,") for url in PRIMARY_URL_RE.findall(markdown)}


def review_history(current: str, previous_issues: list[str]) -> list[Finding]:
    """Review against all earlier issues, not only the immediately prior one."""
    previous_projects: set[str] = set()
    previous_sources: set[str] = set()
    for previous in previous_issues:
        previous_projects.update(
            project
            for heading, _ in sections(previous)
            if (project := heading_project(heading)) is not None
        )
        previous_sources.update(primary_urls(previous))

    findings: list[Finding] = []
    for heading, body in sections(current):
        project = heading_project(heading, previous_projects)
        if not project or project not in previous_projects:
            continue
        current_sources = primary_urls(f"{heading}\n{body}")
        if not current_sources:
            findings.append(Finding(project, "no new primary source"))
            continue
        if current_sources & previous_sources:
            findings.append(Finding(project, "primary source already covered"))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("current", type=Path)
    parser.add_argument("previous", type=Path, nargs="*")
    parser.add_argument(
        "--history-dir",
        type=Path,
        help="compare with every earlier *-newsletter.md in this directory",
    )
    args = parser.parse_args()

    previous_paths = list(args.previous)
    if args.history_dir:
        previous_paths.extend(
            path
            for path in sorted(args.history_dir.glob("*-newsletter.md"))
            if path.resolve() != args.current.resolve() and path.name < args.current.name
        )
    if not previous_paths:
        parser.error("provide a previous issue or --history-dir")
    previous_text = [path.read_text() for path in dict.fromkeys(previous_paths)]
    findings = (
        review(args.current.read_text(), previous_text[0])
        if len(previous_text) == 1
        else review_history(args.current.read_text(), previous_text)
    )
    if not findings:
        print("PASS: repeated projects each cite a distinct primary source")
        return 0

    for finding in findings:
        print(f"FAIL: {finding.project}: {finding.reason}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
