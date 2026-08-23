#!/usr/bin/env python3
"""Synchronize newsletter section artifacts from an assembled draft."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


CANONICAL = (
    ("## Top Stories", "lead-stories.md"),
    ("## Tagged Releases", "tagged-releases.md"),
    ("## In Development", "unreleased-changes.md"),
    ("## Protocol and Spec Work", "protocol-work.md"),
)

# Present in some issues and absent in others, so it cannot join CANONICAL
# without failing every draft that has no launches that week. It still has to
# round-trip: a resumed Assembly rebuilds the draft from sections/, and until
# now that path silently dropped every newly launched project in the issue.
OPTIONAL = (
    ("## Newly Discovered", "newly-discovered.md"),
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


def synchronize(markdown: str, output_dir: Path) -> list[Path]:
    sections = split_sections(markdown)
    output_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    for heading, filename in CANONICAL:
        if heading not in sections:
            raise ValueError(f"missing canonical section: {heading}")
        path = output_dir / filename
        path.write_text(sections[heading] + "\n\nGATE: PENDING REVIEW\n")
        written.append(path)

    for heading, filename in OPTIONAL:
        path = output_dir / filename
        if heading in sections:
            path.write_text(sections[heading] + "\n\nGATE: PENDING REVIEW\n")
            written.append(path)
        else:
            path.unlink(missing_ok=True)

    protocol = sections["## Protocol and Spec Work"]
    legacy_protocol = output_dir / "nip-updates.md"
    legacy_protocol.write_text(protocol + "\n\nGATE: PENDING REVIEW\n")
    written.append(legacy_protocol)

    history_heading = next((heading for heading in sections if heading.startswith("## Six Years of Nostr ")), None)
    if history_heading:
        history = sections[history_heading].split("\n---\n", 1)[0].rstrip()
        path = output_dir / "history.md"
        path.write_text(history + "\n\nGATE: PENDING REVIEW\n")
        written.append(path)
        (output_dir / "nip-deep-dive.md").unlink(missing_ok=True)
    else:
        deep_dive = next((heading for heading in sections if heading.startswith("## NIP Deep Dive")), None)
        if deep_dive:
            path = output_dir / "nip-deep-dive.md"
            path.write_text(sections[deep_dive] + "\n\nGATE: PENDING REVIEW\n")
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
