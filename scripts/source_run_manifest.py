#!/usr/bin/env python3
"""Atomic, versioned evidence manifest for one bounded Compass source run."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = 1


def _absolute(value: str) -> str:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("source window timestamps must include a timezone")
    return parsed.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def _atomic(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.tmp.{os.getpid()}")
    with temp.open("w") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temp, path)


def create_manifest(path: Path, since: str, until: str, expected: list[str]) -> dict:
    start, end = _absolute(since), _absolute(until)
    if start >= end:
        raise ValueError("source window start must precede end")
    if not expected or len(expected) != len(set(expected)):
        raise ValueError("expected source families must be non-empty and unique")
    manifest = {"schema_version": SCHEMA_VERSION, "window": {"since": start, "until": end}, "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"), "expected_families": expected, "observed_families": [], "families": {}}
    _atomic(path, manifest)
    return manifest


def load_manifest(path: Path) -> dict:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"invalid source-run manifest {path}: {exc}") from exc
    if value.get("schema_version") != SCHEMA_VERSION or not isinstance(value.get("families"), dict):
        raise ValueError(f"invalid source-run manifest {path}: unsupported or malformed schema")
    return value


def record_family(path: Path, family: str, exit_code: int, artifact: Path | None, required: bool = True) -> dict:
    manifest = load_manifest(path)
    if family not in manifest["expected_families"]:
        raise ValueError(f"unexpected source family: {family}")
    artifact_exists = artifact is not None and artifact.is_file()
    status = "ok" if exit_code == 0 and artifact_exists else "failed" if exit_code else "missing"
    artifact_hash = hashlib.sha256(artifact.read_bytes()).hexdigest() if artifact is not None and artifact_exists else None
    entry = {"required": required, "exit_code": exit_code, "status": status, "artifact_path": str(artifact.resolve()) if artifact is not None else None, "artifact_sha256": artifact_hash}
    manifest["families"][family] = entry
    manifest["observed_families"] = [name for name in manifest["expected_families"] if name in manifest["families"]]
    _atomic(path, manifest)
    return manifest


def finalize(path: Path) -> bool:
    manifest = load_manifest(path)
    for family in manifest["expected_families"]:
        entry = manifest["families"].get(family)
        if entry is None or (entry.get("required", True) and entry.get("status") != "ok"):
            return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("create")
    create.add_argument("--manifest", type=Path, required=True); create.add_argument("--since", required=True); create.add_argument("--until", required=True); create.add_argument("--expected", action="append", required=True)
    record = sub.add_parser("record")
    record.add_argument("--manifest", type=Path, required=True); record.add_argument("--family", required=True); record.add_argument("--exit-code", type=int, required=True); record.add_argument("--artifact", type=Path); record.add_argument("--optional", action="store_true")
    finish = sub.add_parser("finalize"); finish.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "create": create_manifest(args.manifest, args.since, args.until, args.expected); return 0
    if args.command == "record": record_family(args.manifest, args.family, args.exit_code, args.artifact, not args.optional); return 0
    return 0 if finalize(args.manifest) else 1


if __name__ == "__main__":
    raise SystemExit(main())
