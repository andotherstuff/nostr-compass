#!/usr/bin/env python3
"""Immutable, pass-scoped evidence manifest for one bounded Compass source run."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = 2
STATUS_VALUES = {"complete", "empty_verified", "partial", "unavailable", "not_applicable"}
PASS_ID_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9._-]{5,79}$")

def _absolute(value: str) -> str:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None: raise ValueError("source window timestamps must include a timezone")
    return parsed.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")

def _atomic_new(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.tmp.{os.getpid()}")
    with temp.open("x") as handle:
        json.dump(value, handle, indent=2, sort_keys=True); handle.write("\n"); handle.flush(); os.fsync(handle.fileno())
    try: os.link(temp, path)
    except FileExistsError as exc: raise ValueError(f"refusing to overwrite immutable source pass {path}") from exc
    finally: temp.unlink(missing_ok=True)

def _atomic_replace(path: Path, value: dict) -> None:
    temp = path.with_name(f".{path.name}.tmp.{os.getpid()}")
    with temp.open("w") as handle:
        json.dump(value, handle, indent=2, sort_keys=True); handle.write("\n"); handle.flush(); os.fsync(handle.fileno())
    os.replace(temp, path)

def create_manifest(path: Path, pass_id: str, since: str, until: str, expected: list[str]) -> dict:
    if not PASS_ID_RE.fullmatch(pass_id): raise ValueError("pass_id must be an explicit 6-80 character portable identifier")
    start, end = _absolute(since), _absolute(until)
    if start >= end: raise ValueError("source window start must precede end")
    if not expected or len(expected) != len(set(expected)): raise ValueError("expected source families must be non-empty and unique")
    manifest = {"schema_version": SCHEMA_VERSION, "pass_id": pass_id, "window": {"since": start, "until": end}, "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"), "expected_families": expected, "observed_families": [], "families": {}, "finalized": False}
    _atomic_new(path, manifest); return manifest

def load_manifest(path: Path) -> dict:
    try: value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc: raise ValueError(f"invalid source-run manifest {path}: {exc}") from exc
    if value.get("schema_version") != SCHEMA_VERSION or not isinstance(value.get("families"), dict) or not PASS_ID_RE.fullmatch(str(value.get("pass_id", ""))): raise ValueError(f"invalid source-run manifest {path}: unsupported or malformed schema")
    return value

def digest_json(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def record_family(path: Path, *, pass_id: str, family: str, status: str, artifact: Path | None, collector: Path, query: dict, pagination_complete: bool, item_count: int, page_count: int, include_count: int, skip_count: int, skip_evidence: list[dict]) -> dict:
    manifest = load_manifest(path)
    if manifest.get("finalized"): raise ValueError("source pass is already finalized")
    if pass_id != manifest["pass_id"]: raise ValueError("receipt pass_id does not match manifest")
    if family not in manifest["expected_families"]: raise ValueError(f"unexpected source family: {family}")
    if status not in STATUS_VALUES: raise ValueError(f"invalid source status: {status}")
    if not collector.is_file(): raise ValueError("collector must be a readable versioned file")
    if query.get("since") != manifest["window"]["since"] or query.get("until") != manifest["window"]["until"]: raise ValueError("canonical query is not bound to the exact pass window")
    if query.get("family") != family or query.get("pass_id") != pass_id: raise ValueError("canonical query family/pass identity mismatch")
    if min(item_count, page_count, include_count, skip_count) < 0 or include_count + skip_count < item_count: raise ValueError("invalid item/page/include/skip counts")
    if len(skip_evidence) != skip_count: raise ValueError("skip count must have explicit skip evidence")
    artifact_exists = artifact is not None and artifact.is_file()
    if status in {"complete", "empty_verified"} and (not pagination_complete or not artifact_exists): raise ValueError("complete receipts require pagination completion and a pass artifact")
    if status == "empty_verified" and item_count != 0: raise ValueError("empty_verified requires zero items")
    if status == "complete" and item_count == 0: raise ValueError("complete requires at least one item")
    if status == "not_applicable" and (artifact_exists or item_count or page_count): raise ValueError("not_applicable cannot claim fetched artifacts or counts")
    artifact_hash = hashlib.sha256(artifact.read_bytes()).hexdigest() if artifact_exists and artifact is not None else None
    entry = {"status": status, "pass_id": pass_id, "window": manifest["window"], "collector": str(collector.resolve()), "collector_sha256": hashlib.sha256(collector.read_bytes()).hexdigest(), "canonical_query": query, "canonical_query_sha256": digest_json(query), "pagination_complete": pagination_complete, "item_count": item_count, "page_count": page_count, "include_count": include_count, "skip_count": skip_count, "skip_evidence": skip_evidence, "artifact_path": str(artifact.resolve()) if artifact_exists and artifact is not None else None, "artifact_sha256": artifact_hash}
    manifest["families"][family] = entry; manifest["observed_families"] = [name for name in manifest["expected_families"] if name in manifest["families"]]
    _atomic_replace(path, manifest); return manifest

def ingest_receipt(path: Path, receipt_path: Path) -> dict:
    try: receipt = json.loads(receipt_path.read_text())
    except (OSError, json.JSONDecodeError) as exc: raise ValueError(f"invalid collector receipt {receipt_path}: {exc}") from exc
    required = {"pass_id", "family", "status", "artifact_path", "collector_path", "canonical_query", "pagination_complete", "item_count", "page_count", "include_count", "skip_count", "skip_evidence", "candidate_ids", "dispositions"}
    if set(receipt) != required: raise ValueError("collector receipt fields do not match schema")
    if sorted(receipt["candidate_ids"]) != sorted(receipt["dispositions"]): raise ValueError("every candidate identity requires exactly one include/skip disposition")
    for candidate, disposition in receipt["dispositions"].items():
        if disposition.get("decision") not in {"include", "skip"} or not disposition.get("reason"): raise ValueError(f"candidate {candidate} lacks explicit include/skip evidence")
    include_count = sum(1 for value in receipt["dispositions"].values() if value["decision"] == "include")
    skip_count = sum(1 for value in receipt["dispositions"].values() if value["decision"] == "skip")
    if include_count != receipt["include_count"] or skip_count != receipt["skip_count"] or len(receipt["candidate_ids"]) != receipt["item_count"]: raise ValueError("collector receipt candidate/disposition counts conflict")
    return record_family(path, pass_id=receipt["pass_id"], family=receipt["family"], status=receipt["status"], artifact=Path(receipt["artifact_path"]) if receipt["artifact_path"] else None, collector=Path(receipt["collector_path"]), query=receipt["canonical_query"], pagination_complete=receipt["pagination_complete"], item_count=receipt["item_count"], page_count=receipt["page_count"], include_count=receipt["include_count"], skip_count=receipt["skip_count"], skip_evidence=receipt["skip_evidence"])


def finalize(path: Path) -> bool:
    manifest = load_manifest(path)
    if manifest.get("finalized"): return True
    for family in manifest["expected_families"]:
        entry = manifest["families"].get(family)
        if entry is None or entry.get("pass_id") != manifest["pass_id"] or entry.get("window") != manifest["window"] or entry.get("status") not in {"complete", "empty_verified", "not_applicable"}: return False
    manifest["finalized"] = True; manifest["finalized_at"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"); _atomic_replace(path, manifest); return True

def main() -> int:
    parser = argparse.ArgumentParser(); sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("create"); create.add_argument("--manifest", type=Path, required=True); create.add_argument("--pass-id", required=True); create.add_argument("--since", required=True); create.add_argument("--until", required=True); create.add_argument("--expected", action="append", required=True)
    record = sub.add_parser("record"); record.add_argument("--manifest", type=Path, required=True); record.add_argument("--pass-id", required=True); record.add_argument("--family", required=True); record.add_argument("--status", choices=sorted(STATUS_VALUES), required=True); record.add_argument("--artifact", type=Path); record.add_argument("--collector", type=Path, required=True); record.add_argument("--query-json", required=True); record.add_argument("--pagination-complete", action="store_true"); record.add_argument("--item-count", type=int, required=True); record.add_argument("--page-count", type=int, required=True); record.add_argument("--include-count", type=int, required=True); record.add_argument("--skip-count", type=int, required=True); record.add_argument("--skip-evidence-json", default="[]")
    ingest = sub.add_parser("ingest"); ingest.add_argument("--manifest", type=Path, required=True); ingest.add_argument("--receipt", type=Path, required=True)
    finish = sub.add_parser("finalize"); finish.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "create": create_manifest(args.manifest, args.pass_id, args.since, args.until, args.expected); return 0
    if args.command == "ingest": ingest_receipt(args.manifest, args.receipt); return 0
    if args.command == "record": record_family(args.manifest, pass_id=args.pass_id, family=args.family, status=args.status, artifact=args.artifact, collector=args.collector, query=json.loads(args.query_json), pagination_complete=args.pagination_complete, item_count=args.item_count, page_count=args.page_count, include_count=args.include_count, skip_count=args.skip_count, skip_evidence=json.loads(args.skip_evidence_json)); return 0
    return 0 if finalize(args.manifest) else 1

if __name__ == "__main__": raise SystemExit(main())
