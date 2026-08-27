#!/usr/bin/env python3
"""Consolidate per-worktree discovery baselines into the shared state directory.

WHY THIS EXISTS
---------------
`data/zapstore_releases/` and `data/app_discovery/` are gitignored, and every
newsletter runs in a fresh worktree created from origin/main. The persistent
baselines therefore never existed at run time:

  * Zapstore's fresh-install guard fired on every run, flagging every release
    `first_run: true` / `new_app: false`. Newsletter #37 discarded 622
    Nostr-relevant releases this way, including Nail's own `com.formstr.mail`
    listing and Mostro Mobile v1.4.0.
  * App discovery's `first_run` fired on every run, so nothing was deduped
    against a baseline and triage received 603 candidates (561 owner-siblings) —
    a volume nobody reviews, which buries real launches.

Whatever state each worktree did accumulate is partial and mutually divergent
(five worktrees held five different baselines, from 6 to 778 repositories).
Picking one would throw away the others' knowledge and re-flag old apps as new,
so this takes the UNION: an app or repository seen by any worktree counts as
seen. The union is the conservative direction — it can only suppress a stale
"new" flag, never invent one.

Idempotent. Safe to re-run. Never deletes a source file.

Usage:
  python3 scripts/migrate_discovery_state.py [--dry-run] [--state-dir DIR]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

WORKTREE_ROOTS = [
    Path("/opt/data/compass"),
    *sorted(Path("/opt/data/compass-worktrees").glob("*")),
]

SEEN_HEADER = [
    "# Persistent state for zapstore newness detection.",
    "# Format: { <pubkey>: [<app_id>, ...] }",
    "# DO NOT delete this file. Fresh install suppresses new_app flags on next run.",
]


def load_zapstore_seen(path: Path) -> dict[str, list[str]]:
    """Parse the seen file, which is JSON below a block of `#` comments."""
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError:
        return {}
    body = "\n".join(
        line for line in raw.splitlines() if not re.match(r"^\s*#", line) and line.strip()
    )
    if not body:
        return {}
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        print(f"  warning: {path} is malformed; skipping", file=sys.stderr)
        return {}
    if not isinstance(data, dict):
        return {}
    return {
        k: [a for a in v if isinstance(a, str)]
        for k, v in data.items()
        if isinstance(k, str) and isinstance(v, list)
    }


def merge_zapstore(sources: list[Path]) -> tuple[dict[str, list[str]], list[str]]:
    merged: dict[str, set[str]] = {}
    notes: list[str] = []
    for path in sources:
        seen = load_zapstore_seen(path)
        if not seen:
            continue
        pairs = sum(len(v) for v in seen.values())
        notes.append(f"{path}: {len(seen)} publishers / {pairs} app ids")
        for pubkey, apps in seen.items():
            merged.setdefault(pubkey, set()).update(apps)
    return {k: sorted(v) for k, v in sorted(merged.items())}, notes


def merge_app_discovery(sources: list[Path]) -> tuple[dict, list[str]]:
    repositories: set[str] = set()
    owner_siblings: set[str] = set()
    protocol_events: dict[str, str] = {}
    notes: list[str] = []
    for path in sources:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(data, dict):
            continue
        repos = [r for r in data.get("repositories", []) if isinstance(r, str)]
        sibs = [r for r in data.get("owner_sibling_repositories", []) if isinstance(r, str)]
        events = {
            k: v
            for k, v in (data.get("protocol_events") or {}).items()
            if isinstance(k, str) and isinstance(v, str)
        }
        notes.append(
            f"{path}: {len(repos)} repositories / {len(sibs)} owner siblings / {len(events)} protocol events"
        )
        repositories.update(repos)
        owner_siblings.update(sibs)
        # Later worktrees win for a given address; any recorded id is enough to
        # stop the event being re-reported as brand new.
        protocol_events.update(events)
    return (
        {
            "repositories": sorted(repositories),
            "owner_sibling_repositories": sorted(owner_siblings),
            "protocol_events": dict(sorted(protocol_events.items())),
        },
        notes,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument(
        "--state-dir",
        type=Path,
        default=Path(os.environ.get("COMPASS_STATE_DIR", "/opt/data/compass-state")),
    )
    args = ap.parse_args()

    zap_sources = [
        r / "data/zapstore_releases/publishers_seen.yml"
        for r in WORKTREE_ROOTS
        if (r / "data/zapstore_releases/publishers_seen.yml").is_file()
    ]
    app_sources = [
        r / "data/app_discovery/seen_repos.json"
        for r in WORKTREE_ROOTS
        if (r / "data/app_discovery/seen_repos.json").is_file()
    ]

    zap_target = args.state_dir / "zapstore_releases/publishers_seen.yml"
    app_target = args.state_dir / "app_discovery/seen_repos.json"
    # An already-migrated target is itself a source, so re-running never regresses.
    if zap_target.is_file():
        zap_sources.append(zap_target)
    if app_target.is_file():
        app_sources.append(app_target)

    print(f"Zapstore seen files found: {len(zap_sources)}")
    zap_merged, zap_notes = merge_zapstore(zap_sources)
    for n in zap_notes:
        print(f"  {n}")
    zap_pairs = sum(len(v) for v in zap_merged.values())
    print(f"  => union: {len(zap_merged)} publishers / {zap_pairs} app ids")

    print(f"App discovery state files found: {len(app_sources)}")
    app_merged, app_notes = merge_app_discovery(app_sources)
    for n in app_notes:
        print(f"  {n}")
    print(
        f"  => union: {len(app_merged['repositories'])} repositories / "
        f"{len(app_merged['owner_sibling_repositories'])} owner siblings / "
        f"{len(app_merged['protocol_events'])} protocol events"
    )

    if args.dry_run:
        print("\n--dry-run: nothing written")
        return 0

    zap_target.parent.mkdir(parents=True, exist_ok=True)
    app_target.parent.mkdir(parents=True, exist_ok=True)

    tmp = zap_target.with_suffix(".tmp")
    tmp.write_text(
        "\n".join(SEEN_HEADER) + "\n" + json.dumps(zap_merged, indent=2) + "\n",
        encoding="utf-8",
    )
    tmp.replace(zap_target)

    tmp = app_target.with_suffix(".tmp")
    tmp.write_text(json.dumps(app_merged, indent=2) + "\n", encoding="utf-8")
    tmp.replace(app_target)

    print(f"\nwrote {zap_target}")
    print(f"wrote {app_target}")
    if zap_pairs == 0:
        print(
            "WARNING: the merged Zapstore baseline is empty. The next run will "
            "legitimately baseline as a fresh install.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
