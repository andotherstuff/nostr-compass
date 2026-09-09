#!/usr/bin/env python3
"""Synchronize newsletter section artifacts from an assembled draft."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


CANONICAL = (
    (("## Top Stories",), "lead-stories.md"),
    (("## Tagged Releases", "## Releases"), "tagged-releases.md"),
    (("## In Development", "## Unreleased Changes"), "unreleased-changes.md"),
    (("## Protocol and Spec Work", "## NIP Updates and Protocol Spec Work"), "protocol-work.md"),
)


def split_sections(markdown: str) -> dict[str, str]:
    matches = list(re.finditer(r"(?m)^##\s+.+$", markdown))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        heading = match.group(0)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        body = markdown[match.start():end].rstrip()
        sections[heading] = body
    return sections


def write_section(path: Path, body: str) -> None:
    """Write a synchronized section without discarding its writer provenance."""
    provenance = ""
    if path.exists():
        match = re.search(r"(?m)^writer_model:.*$", path.read_text())
        if match:
            provenance = f"\n\n{match.group(0)}"
    path.write_text(f"{body}{provenance}\n\nGATE: PENDING REVIEW\n")


def synchronize(markdown: str, output_dir: Path) -> list[Path]:
    sections = split_sections(markdown)
    output_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    selected: dict[str, str] = {}
    for headings, filename in CANONICAL:
        heading = next((candidate for candidate in headings if candidate in sections), None)
        if heading is None:
            raise ValueError(f"missing canonical section: {headings[0]}")
        path = output_dir / filename
        write_section(path, sections[heading])
        written.append(path)
        selected[filename] = sections[heading]

    # Discovery is a selection source, not a separate published H2. A selected
    # new project belongs in Top Stories when architecturally significant.
    (output_dir / "newly-discovered.md").unlink(missing_ok=True)

    protocol = selected["protocol-work.md"]
    legacy_protocol = output_dir / "nip-updates.md"
    write_section(legacy_protocol, protocol)
    written.append(legacy_protocol)

    history_heading = next((heading for heading in sections if heading.startswith("## Six Years of Nostr ")), None)
    if history_heading:
        history = sections[history_heading].split("\n---\n", 1)[0].rstrip()
        path = output_dir / "history.md"
        write_section(path, history)
        written.append(path)
        (output_dir / "nip-deep-dive.md").unlink(missing_ok=True)
    else:
        deep_dive = next((heading for heading in sections if heading.startswith("## NIP Deep Dive")), None)
        if deep_dive:
            path = output_dir / "nip-deep-dive.md"
            write_section(path, sections[deep_dive])
            written.append(path)
            (output_dir / "history.md").unlink(missing_ok=True)

    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("newsletter", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("data/newsletter_workspace/sections"))
    args = parser.parse_args()
    written = synchronize(args.newsletter.read_text(), args.output_dir)
    for path in written:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
