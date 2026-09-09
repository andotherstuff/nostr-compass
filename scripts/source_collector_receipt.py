#!/usr/bin/env python3
"""Validate and persist collector-native evidence for one exact source pass.

This module never infers query completion from an artifact or exit status. Each
collector must supply its effective bounds, query timing, page/cursor evidence,
and one explicit disposition for every stable candidate identity.
"""
from __future__ import annotations

import argparse
import hashlib
from datetime import datetime, timezone
import json
import os
from pathlib import Path
from typing import Any

REQUIRED_ENV = ("COMPASS_SOURCE_PASS_ID", "COMPASS_WINDOW_SINCE", "COMPASS_WINDOW_UNTIL")


def observed_page(*, source: str, count: int, cap: int, exhausted: bool,
                  since: str, until: str, cursor: str | None = None) -> dict[str, Any]:
    """Build page evidence at the query site, never from a final artifact."""
    return {
        "source": source,
        "cursor": cursor,
        "count": count,
        "cap": cap,
        "exhausted": exhausted,
        "effective_since": since,
        "effective_until": until,
    }


def native_evidence(*, family: str, since: str, until: str, started: str,
                    pages: list[dict[str, Any]], candidate_ids: list[str],
                    dispositions: dict[str, dict[str, str]], failures: list[str] | None = None,
                    query: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "effective_since": since,
        "effective_until": until,
        "query_started_at": started,
        "query_finished_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "canonical_query": {"family": family, "since": since, "until": until, **(query or {})},
        "pages": pages,
        "candidate_ids": candidate_ids,
        "dispositions": dispositions,
        "failures": failures or [],
    }


def _utc(value: str, field: str) -> str:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (AttributeError, ValueError) as exc:
        raise ValueError(f"{field} must be an absolute timestamp") from exc
    if parsed.tzinfo is None:
        raise ValueError(f"{field} must include a timezone")
    return parsed.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_native_evidence(*, family: str, evidence: dict[str, Any], since: str, until: str) -> None:
    required = {
        "effective_since", "effective_until", "query_started_at", "query_finished_at",
        "canonical_query", "pages", "candidate_ids", "dispositions", "failures",
    }
    if set(evidence) != required:
        raise ValueError(f"collector evidence fields do not match schema: expected {sorted(required)}")
    if _utc(evidence["effective_since"], "effective_since") != _utc(since, "pass since"):
        raise ValueError("collector did not consume the exact pass since bound")
    if _utc(evidence["effective_until"], "effective_until") != _utc(until, "pass until"):
        raise ValueError("collector did not consume the exact exclusive pass until bound")
    started = _utc(evidence["query_started_at"], "query_started_at")
    finished = _utc(evidence["query_finished_at"], "query_finished_at")
    if started > finished:
        raise ValueError("query_finished_at precedes query_started_at")
    query = evidence["canonical_query"]
    if not isinstance(query, dict) or query.get("family") != family:
        raise ValueError("canonical query is missing the source family")
    if _utc(query.get("since"), "canonical query since") != _utc(since, "pass since") or _utc(query.get("until"), "canonical query until") != _utc(until, "pass until"):
        raise ValueError("canonical query is not bound to the exact pass window")

    failures = evidence["failures"]
    if not isinstance(failures, list):
        raise ValueError("collector failures must be an explicit list")
    if failures:
        raise ValueError("partial collector failures forbid an exact-pass receipt")

    pages = evidence["pages"]
    if not isinstance(pages, list) or not pages:
        raise ValueError("collector must supply native page evidence; page_count has no default")
    by_source: dict[str, list[dict[str, Any]]] = {}
    for page in pages:
        page_fields = {"source", "cursor", "count", "cap", "exhausted", "effective_since", "effective_until"}
        if not isinstance(page, dict) or set(page) != page_fields:
            raise ValueError("each page requires source/cursor/count/cap/exhausted and effective bound evidence")
        if not isinstance(page["source"], str) or not page["source"]:
            raise ValueError("page source identity is required")
        if not isinstance(page["count"], int) or not isinstance(page["cap"], int) or page["count"] < 0 or page["cap"] <= 0 or page["count"] > page["cap"]:
            raise ValueError("page count/cap evidence is invalid")
        if not isinstance(page["exhausted"], bool):
            raise ValueError("page exhaustion must be explicit")
        if _utc(page["effective_since"], "page effective_since") != _utc(since, "pass since"):
            raise ValueError(f"page query for {page['source']} ignored the exact since bound")
        if _utc(page["effective_until"], "page effective_until") != _utc(until, "pass until"):
            raise ValueError(f"page query for {page['source']} ignored the exact exclusive upper bound")
        by_source.setdefault(page["source"], []).append(page)
    for source, source_pages in by_source.items():
        if not source_pages[-1]["exhausted"]:
            raise ValueError(f"capped or incomplete pagination for {source}")
        if any(page["exhausted"] for page in source_pages[:-1]):
            raise ValueError(f"pagination continued after exhaustion for {source}")

    candidate_ids = evidence["candidate_ids"]
    dispositions = evidence["dispositions"]
    if not isinstance(candidate_ids, list) or not all(isinstance(value, str) and value for value in candidate_ids):
        raise ValueError("candidate_ids must be stable non-empty strings")
    if len(candidate_ids) != len(set(candidate_ids)):
        raise ValueError("candidate_ids must be unique")
    if not isinstance(dispositions, dict) or sorted(candidate_ids) != sorted(dispositions):
        raise ValueError("every candidate identity requires exactly one disposition")
    for candidate, disposition in dispositions.items():
        if not isinstance(disposition, dict) or set(disposition) != {"decision", "reason"}:
            raise ValueError(f"candidate {candidate} disposition fields do not match schema")
        if disposition["decision"] not in {"include", "skip"} or not isinstance(disposition["reason"], str) or not disposition["reason"].strip():
            raise ValueError(f"candidate {candidate} lacks explicit include/skip evidence")


def emit_receipt(*, family: str, artifact: Path, collector: Path, evidence: dict[str, Any],
                 environ: dict[str, str] | None = None, receipt_dir: Path | None = None) -> Path | None:
    env = os.environ if environ is None else environ
    present = [bool(env.get(key)) for key in REQUIRED_ENV]
    if not any(present):
        return None
    if not all(present):
        raise ValueError("Compass source pass environment is incomplete")
    if not artifact.is_file() or not collector.is_file():
        raise ValueError("collector and final artifact must be regular files")
    pass_id = env["COMPASS_SOURCE_PASS_ID"]
    validate_native_evidence(
        family=family,
        evidence=evidence,
        since=env["COMPASS_WINDOW_SINCE"],
        until=env["COMPASS_WINDOW_UNTIL"],
    )
    candidate_ids = evidence["candidate_ids"]
    dispositions = evidence["dispositions"]
    skip_evidence = [
        {"candidate_id": candidate, "reason": disposition["reason"]}
        for candidate, disposition in dispositions.items()
        if disposition["decision"] == "skip"
    ]
    include_count = sum(value["decision"] == "include" for value in dispositions.values())
    receipt = {
        "pass_id": pass_id,
        "family": family,
        "status": "complete" if candidate_ids else "empty_verified",
        "artifact_path": str(artifact.resolve()),
        "artifact_sha256": _sha256(artifact),
        "collector_path": str(collector.resolve()),
        "canonical_query": {**evidence["canonical_query"], "pass_id": pass_id},
        "pagination_complete": True,
        "item_count": len(candidate_ids),
        "page_count": len(evidence["pages"]),
        "include_count": include_count,
        "skip_count": len(skip_evidence),
        "skip_evidence": skip_evidence,
        "candidate_ids": candidate_ids,
        "dispositions": dispositions,
    }
    root = receipt_dir or artifact.parents[1] / "source_runs"
    target = root / f"collector_{pass_id}_{family}.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if json.loads(target.read_text()) != receipt:
            raise ValueError(f"conflicting exact-pass receipt already exists: {target}")
        return target
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    temp = target.with_name(f".{target.name}.tmp.{os.getpid()}")
    with temp.open("x") as handle:
        handle.write(rendered)
        handle.flush()
        os.fsync(handle.fileno())
    try:
        os.link(temp, target)
    except FileExistsError:
        if json.loads(target.read_text()) != receipt:
            raise ValueError(f"conflicting exact-pass receipt already exists: {target}")
    finally:
        temp.unlink(missing_ok=True)
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--family", required=True)
    parser.add_argument("--artifact", type=Path, required=True)
    parser.add_argument("--collector", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--receipt-dir", type=Path)
    args = parser.parse_args()
    evidence = json.loads(args.evidence.read_text())
    target = emit_receipt(
        family=args.family,
        artifact=args.artifact,
        collector=args.collector,
        evidence=evidence,
        receipt_dir=args.receipt_dir,
    )
    if target is not None:
        print(f"Wrote exact-pass receipt: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
