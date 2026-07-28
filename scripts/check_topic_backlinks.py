#!/usr/bin/env python3
"""Validate topic sources and rendered backlinks for one newsletter."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

TOPIC_RE = re.compile(r"\]\(/en/topics/([^/)]+)/?\)")
ID_RE = re.compile(r"\bid=[\"']([^\"']+)[\"']")
PRIMARY_RE = re.compile(r"(?mi)^(?:##\s+Primary sources\s*$|\*\*Primary sources:\*\*\s*$)")


def review(newsletter: Path, topic_dir: Path, rendered_html: Path) -> tuple[list[str], dict[str, int]]:
    text = newsletter.read_text()
    slugs = sorted(set(TOPIC_RE.findall(text)))
    issue_slug = newsletter.stem
    ids = set(ID_RE.findall(rendered_html.read_text()))
    findings: list[str] = []
    backlink_count = 0

    for slug in slugs:
        topic = topic_dir / f"{slug}.md"
        if not topic.exists():
            findings.append(f"missing topic page: {topic}")
            continue
        topic_text = topic.read_text()
        if not PRIMARY_RE.search(topic_text):
            findings.append(f"{slug}: missing Primary sources block")
        backlink_re = re.compile(
            rf"/en/newsletters/{re.escape(issue_slug)}/#([A-Za-z0-9_-]+)"
        )
        fragments = backlink_re.findall(topic_text)
        if not fragments:
            findings.append(f"{slug}: missing backlink to {issue_slug}")
            continue
        backlink_count += len(fragments)
        for fragment in fragments:
            if fragment not in ids:
                findings.append(f"{slug}: stale backlink fragment #{fragment}")

    return findings, {"topics": len(slugs), "backlinks": backlink_count}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("newsletter", type=Path)
    parser.add_argument("--topic-dir", type=Path, default=Path("content/en/topics"))
    parser.add_argument("--rendered-html", type=Path, required=True)
    args = parser.parse_args()
    findings, stats = review(args.newsletter, args.topic_dir, args.rendered_html)
    if findings:
        for finding in findings:
            print(f"FAIL: {finding}")
        return 1
    print(
        "PASS: "
        f"{stats['topics']} topic pages have Primary sources blocks and "
        f"{stats['backlinks']} rendered newsletter backlinks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
