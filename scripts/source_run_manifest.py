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
    if path.exists():
        existing = load_manifest(path)
        if existing["pass_id"] != pass_id or existing["window"] != {"since": start, "until": end} or existing["expected_families"] != expected:
            raise ValueError(f"refusing to reuse source pass with conflicting identity/window/families: {path}")
        return existing
    manifest = {"schema_version": SCHEMA_VERSION, "pass_id": pass_id, "window": {"since": start, "until": end}, "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"), "expected_families": expected, "observed_families": [], "families": {}, "finalized": False}
    _atomic_new(path, manifest); return manifest

def _validate_candidate_evidence(entry: dict, *, family: str) -> None:
    candidate_ids = entry.get("candidate_ids")
    dispositions = entry.get("dispositions")
    if not isinstance(candidate_ids, list) or not all(isinstance(value, str) and value for value in candidate_ids):
        raise ValueError(f"source family {family} has malformed candidate identities")
    if len(candidate_ids) != len(set(candidate_ids)) or not isinstance(dispositions, dict) or sorted(candidate_ids) != sorted(dispositions):
        raise ValueError(f"source family {family} candidate/disposition identities conflict")
    for candidate, disposition in dispositions.items():
        if not isinstance(disposition, dict) or disposition.get("decision") not in {"include", "skip"} or not disposition.get("reason"):
            raise ValueError(f"source family {family} candidate {candidate} lacks explicit include/skip evidence")
    include_count = sum(value["decision"] == "include" for value in dispositions.values())
    skip_count = sum(value["decision"] == "skip" for value in dispositions.values())
    if include_count != entry.get("include_count") or skip_count != entry.get("skip_count") or len(candidate_ids) != entry.get("item_count"):
        raise ValueError(f"source family {family} candidate evidence counts conflict")
    skip_evidence = entry.get("skip_evidence")
    expected_skips = {candidate for candidate, value in dispositions.items() if value["decision"] == "skip"}
    if not isinstance(skip_evidence, list) or {value.get("candidate_id") for value in skip_evidence if isinstance(value, dict)} != expected_skips:
        raise ValueError(f"source family {family} skip evidence conflicts with dispositions")


def load_manifest(path: Path) -> dict:
    try: value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc: raise ValueError(f"invalid source-run manifest {path}: {exc}") from exc
    if value.get("schema_version") != SCHEMA_VERSION or not isinstance(value.get("families"), dict) or not PASS_ID_RE.fullmatch(str(value.get("pass_id", ""))): raise ValueError(f"invalid source-run manifest {path}: unsupported or malformed schema")
    for family, entry in value["families"].items():
        if not isinstance(entry, dict): raise ValueError(f"invalid source family entry: {family}")
        _validate_candidate_evidence(entry, family=family)
    return value

def digest_json(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def record_family(path: Path, *, pass_id: str, family: str, status: str, artifact: Path | None, collector: Path, query: dict, pagination_complete: bool, item_count: int, page_count: int, include_count: int, skip_count: int, skip_evidence: list[dict], candidate_ids: list[str] | None = None, dispositions: dict[str, dict] | None = None) -> dict:
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
    candidate_ids = [] if candidate_ids is None else candidate_ids
    dispositions = {} if dispositions is None else dispositions
    artifact_exists = artifact is not None and artifact.is_file()
    if status in {"complete", "empty_verified"} and (not pagination_complete or not artifact_exists): raise ValueError("complete receipts require pagination completion and a pass artifact")
    if status == "empty_verified" and item_count != 0: raise ValueError("empty_verified requires zero items")
    if status == "complete" and item_count == 0: raise ValueError("complete requires at least one item")
    if status == "not_applicable" and (artifact_exists or item_count or page_count): raise ValueError("not_applicable cannot claim fetched artifacts or counts")
    artifact_hash = hashlib.sha256(artifact.read_bytes()).hexdigest() if artifact_exists and artifact is not None else None
    entry = {"status": status, "pass_id": pass_id, "window": manifest["window"], "collector": str(collector.resolve()), "collector_sha256": hashlib.sha256(collector.read_bytes()).hexdigest(), "canonical_query": query, "canonical_query_sha256": digest_json(query), "pagination_complete": pagination_complete, "item_count": item_count, "page_count": page_count, "include_count": include_count, "skip_count": skip_count, "skip_evidence": skip_evidence, "candidate_ids": candidate_ids, "dispositions": dispositions, "artifact_path": str(artifact.resolve()) if artifact_exists and artifact is not None else None, "artifact_sha256": artifact_hash}
    _validate_candidate_evidence(entry, family=family)
    existing = manifest["families"].get(family)
    if existing is not None:
        if existing != entry:
            raise ValueError(f"conflicting receipt for source family {family}")
        return manifest
    manifest["families"][family] = entry; manifest["observed_families"] = [name for name in manifest["expected_families"] if name in manifest["families"]]
    _atomic_replace(path, manifest); return manifest

def ingest_receipt(path: Path, receipt_path: Path) -> dict:
    try: receipt = json.loads(receipt_path.read_text())
    except (OSError, json.JSONDecodeError) as exc: raise ValueError(f"invalid collector receipt {receipt_path}: {exc}") from exc
    required = {"pass_id", "family", "status", "artifact_path", "artifact_sha256", "collector_path", "canonical_query", "pagination_complete", "item_count", "page_count", "include_count", "skip_count", "skip_evidence", "candidate_ids", "dispositions"}
    if set(receipt) != required: raise ValueError("collector receipt fields do not match schema")
    if sorted(receipt["candidate_ids"]) != sorted(receipt["dispositions"]): raise ValueError("every candidate identity requires exactly one include/skip disposition")
    for candidate, disposition in receipt["dispositions"].items():
        if disposition.get("decision") not in {"include", "skip"} or not disposition.get("reason"): raise ValueError(f"candidate {candidate} lacks explicit include/skip evidence")
    include_count = sum(1 for value in receipt["dispositions"].values() if value["decision"] == "include")
    skip_count = sum(1 for value in receipt["dispositions"].values() if value["decision"] == "skip")
    if include_count != receipt["include_count"] or skip_count != receipt["skip_count"] or len(receipt["candidate_ids"]) != receipt["item_count"]: raise ValueError("collector receipt candidate/disposition counts conflict")
    artifact = Path(receipt["artifact_path"]) if receipt["artifact_path"] else None
    if artifact is not None and hashlib.sha256(artifact.read_bytes()).hexdigest() != receipt["artifact_sha256"]:
        raise ValueError("collector receipt artifact hash does not match artifact bytes")
    return record_family(path, pass_id=receipt["pass_id"], family=receipt["family"], status=receipt["status"], artifact=artifact, collector=Path(receipt["collector_path"]), query=receipt["canonical_query"], pagination_complete=receipt["pagination_complete"], item_count=receipt["item_count"], page_count=receipt["page_count"], include_count=receipt["include_count"], skip_count=receipt["skip_count"], skip_evidence=receipt["skip_evidence"], candidate_ids=receipt["candidate_ids"], dispositions=receipt["dispositions"])


def finalize(path: Path) -> bool:
    manifest = load_manifest(path)
    for family in manifest["expected_families"]:
        entry = manifest["families"].get(family)
        if entry is None or entry.get("pass_id") != manifest["pass_id"] or entry.get("window") != manifest["window"] or entry.get("status") not in {"complete", "empty_verified", "not_applicable"}: return False
        _validate_candidate_evidence(entry, family=family)
        if digest_json(entry.get("canonical_query")) != entry.get("canonical_query_sha256"):
            raise ValueError(f"source family {family} canonical query changed after collection")
        collector = Path(entry["collector"])
        if not collector.is_file() or hashlib.sha256(collector.read_bytes()).hexdigest() != entry.get("collector_sha256"):
            raise ValueError(f"source family {family} collector bytes changed after collection")
        if entry["status"] != "not_applicable":
            artifact = Path(entry["artifact_path"])
            if not artifact.is_file() or hashlib.sha256(artifact.read_bytes()).hexdigest() != entry.get("artifact_sha256"):
                raise ValueError(f"source family {family} artifact bytes changed after collection")
    if manifest.get("finalized"): return True
    manifest["finalized"] = True; manifest["finalized_at"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"); _atomic_replace(path, manifest); return True


def verify_finalized(path: Path) -> bool:
    return bool(load_manifest(path).get("finalized")) and finalize(path)

def main() -> int:
    parser = argparse.ArgumentParser(); sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("create"); create.add_argument("--manifest", type=Path, required=True); create.add_argument("--pass-id", required=True); create.add_argument("--since", required=True); create.add_argument("--until", required=True); create.add_argument("--expected", action="append", required=True)
    record = sub.add_parser("record"); record.add_argument("--manifest", type=Path, required=True); record.add_argument("--pass-id", required=True); record.add_argument("--family", required=True); record.add_argument("--status", choices=sorted(STATUS_VALUES), required=True); record.add_argument("--artifact", type=Path); record.add_argument("--collector", type=Path, required=True); record.add_argument("--query-json", required=True); record.add_argument("--pagination-complete", action="store_true"); record.add_argument("--item-count", type=int, required=True); record.add_argument("--page-count", type=int, required=True); record.add_argument("--include-count", type=int, required=True); record.add_argument("--skip-count", type=int, required=True); record.add_argument("--skip-evidence-json", default="[]"); record.add_argument("--candidate-ids-json", default="[]"); record.add_argument("--dispositions-json", default="{}")
    ingest = sub.add_parser("ingest"); ingest.add_argument("--manifest", type=Path, required=True); ingest.add_argument("--receipt", type=Path, required=True)
    finish = sub.add_parser("finalize"); finish.add_argument("--manifest", type=Path, required=True)
    verify = sub.add_parser("verify-finalized"); verify.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "create": create_manifest(args.manifest, args.pass_id, args.since, args.until, args.expected); return 0
    if args.command == "ingest": ingest_receipt(args.manifest, args.receipt); return 0
    if args.command == "record": record_family(args.manifest, pass_id=args.pass_id, family=args.family, status=args.status, artifact=args.artifact, collector=args.collector, query=json.loads(args.query_json), pagination_complete=args.pagination_complete, item_count=args.item_count, page_count=args.page_count, include_count=args.include_count, skip_count=args.skip_count, skip_evidence=json.loads(args.skip_evidence_json), candidate_ids=json.loads(args.candidate_ids_json), dispositions=json.loads(args.dispositions_json)); return 0
    if args.command == "verify-finalized": return 0 if verify_finalized(args.manifest) else 1
    return 0 if finalize(args.manifest) else 1

if __name__ == "__main__": raise SystemExit(main())
