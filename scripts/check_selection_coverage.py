#!/usr/bin/env python3
"""Reconcile one finalized source pass through selection and the newsletter draft.

Collector-level skips remain in the immutable source manifest. Every retained
source candidate must then map to one or more stable editorial candidates in the
selection ledger. The ledger applies one hard eligibility gate and one fixed
quality threshold; every qualifying candidate must be included or folded into a
section, while every rejected candidate keeps a concrete reason.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from project_activity_coverage import inventory as activity_inventory, read_object as read_activity_object, validate as validate_activity

CHECKER_VERSION = "selection-coverage-v2"
SOURCE_FAMILIES = (
    "projects",
    "nip-discussions",
    "nostr-recap",
    "shakespeare-apps",
    "nip34",
    "zapstore",
    "app-discovery",
    "heartbeats",
    "monthly-history",
    "specs",
)
HARD_GATES = (
    "primary_evidence",
    "in_window_progress",
    "nostr_surface",
    "continuity_delta",
)
SCORE_AXES = (
    "nostr_significance",
    "user_operator_impact",
    "novelty",
    "evidence_maturity",
    "explanatory_value",
)


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read {label} {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be one JSON object")
    return value


def source_universe(manifest: dict[str, Any], errors: list[str]) -> set[str]:
    if manifest.get("schema_version") != 2 or manifest.get("finalized") is not True:
        errors.append("source manifest is not finalized schema version 2")
    families = manifest.get("families")
    expected = manifest.get("expected_families")
    if (
        not isinstance(families, dict)
        or not isinstance(expected, list)
        or tuple(expected) != SOURCE_FAMILIES
        or set(families) != set(SOURCE_FAMILIES)
    ):
        errors.append("source manifest must contain the exact ten maintained source families")
        return set()
    retained: set[str] = set()
    for family in expected:
        entry = families.get(family, {})
        status = entry.get("status")
        if status not in {"complete", "empty_verified", "not_applicable"}:
            errors.append(f"source family {family} is {status!r}, so selection cannot claim complete coverage")
        if family != "monthly-history" and status == "not_applicable":
            errors.append(f"source family {family} is required and cannot be marked not_applicable")
        ids = entry.get("candidate_ids")
        dispositions = entry.get("dispositions")
        if not isinstance(ids, list) or not isinstance(dispositions, dict) or set(ids) != set(dispositions):
            errors.append(f"source family {family} lacks exact candidate dispositions")
            continue
        for candidate_id in ids:
            disposition = dispositions.get(candidate_id)
            if not isinstance(candidate_id, str) or not candidate_id or not isinstance(disposition, dict):
                errors.append(f"source family {family} has a malformed candidate")
                continue
            decision, reason = disposition.get("decision"), disposition.get("reason")
            if decision not in {"include", "skip"} or not isinstance(reason, str) or not reason.strip():
                errors.append(f"source family {family} candidate {candidate_id!r} lacks a source disposition")
            if decision == "include":
                retained.add(f"{family}:{candidate_id}")
    return retained


def validate(manifest_path: Path, ledger_path: Path, draft_path: Path) -> tuple[list[str], dict[str, Any]]:
    manifest = load_json(manifest_path, "source manifest")
    ledger = load_json(ledger_path, "selection ledger")
    draft = draft_path.read_text()
    errors: list[str] = []

    manifest_hash = file_hash(manifest_path)
    draft_hash = file_hash(draft_path)
    if ledger.get("schema_version") != 1 or ledger.get("final") is not True:
        errors.append("selection ledger is not final schema version 1")
    if ledger.get("source_manifest_sha256") != manifest_hash:
        errors.append("selection ledger does not bind the exact source manifest")
    if ledger.get("source_pass_id") != manifest.get("pass_id"):
        errors.append("selection ledger source pass id does not match the manifest")
    if ledger.get("draft_sha256") != draft_hash:
        errors.append("selection ledger does not bind the exact draft")
    policy = ledger.get("selection_policy")
    expected_policy = {"minimum_score": 8, "maximum_score": 10, "require_no_zero_axis": True, "fixed_item_cap": None, "qualified_items_must_publish": True}
    if policy != expected_policy:
        errors.append("selection policy must use the 8/10 no-zero threshold with no fixed item cap")
    if tuple(ledger.get("hard_gate_fields", ())) != HARD_GATES:
        errors.append("selection ledger hard-gate fields do not match the maintained policy")
    if tuple(ledger.get("score_axes", ())) != SCORE_AXES:
        errors.append("selection ledger score axes do not match the maintained policy")

    # The source-manifest projects family contains low-level API record IDs,
    # while editorial selection works at project/change level. The separate
    # exact-input activity decision closes the release-only blind spot before a
    # final selection receipt can pass. It does not replace source expansion.
    activity_counts = {"activity_project_count": 0, "activity_pr_count": 0}
    activity_selected_urls: set[str] = set()
    manifest_families = manifest.get("families")
    project_entry = manifest_families.get("projects") if isinstance(manifest_families, dict) else None
    project_source = project_entry if isinstance(project_entry, dict) else {}
    source_path = project_source.get("artifact_path")
    decision_binding = ledger.get("project_activity_decisions")
    if not isinstance(source_path, str) or not source_path or not isinstance(decision_binding, dict):
        errors.append("final selection needs the project source artifact and bound project-activity decisions")
    else:
        decision_path = decision_binding.get("path")
        try:
            updates_path = Path(source_path)
            if file_hash(updates_path) != project_source.get("artifact_sha256"):
                errors.append("project-activity source does not match the finalized source manifest")
            if not isinstance(decision_path, str) or file_hash(Path(decision_path)) != decision_binding.get("sha256"):
                errors.append("project-activity decisions lack their exact-file binding")
            else:
                activity = activity_inventory(read_activity_object(updates_path), file_hash(updates_path))
                activity_counts = {"activity_project_count": activity["project_count"], "activity_pr_count": activity["pr_count"]}
                activity_decisions = read_activity_object(Path(decision_path))
                errors.extend(validate_activity(activity, activity_decisions, draft))
                decision_rows = activity_decisions.get("projects")
                if isinstance(decision_rows, list):
                    for row in decision_rows:
                        if isinstance(row, dict) and row.get("verdict") == "include" and isinstance(row.get("selected_pr_urls"), list):
                            activity_selected_urls.update(url for url in row["selected_pr_urls"] if isinstance(url, str))
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"project-activity evidence cannot be read: {exc}")

    retained_sources = source_universe(manifest, errors)
    candidates_value = ledger.get("candidates")
    expansions_value = ledger.get("source_expansion")
    if not isinstance(candidates_value, list) or not isinstance(expansions_value, list):
        errors.append("selection ledger needs candidate and source_expansion arrays")
        return errors, {}

    candidates: dict[str, dict[str, Any]] = {}
    for candidate in candidates_value:
        candidate_id = candidate.get("candidate_id") if isinstance(candidate, dict) else None
        if not isinstance(candidate_id, str) or not candidate_id:
            errors.append("editorial candidate lacks a stable candidate_id")
            continue
        if candidate_id in candidates:
            errors.append(f"duplicate editorial candidate id: {candidate_id}")
            continue
        candidates[candidate_id] = candidate

    expanded_sources: dict[str, list[str]] = {}
    for expansion in expansions_value:
        if not isinstance(expansion, dict):
            errors.append("source expansion rows must be objects")
            continue
        source_id, candidate_ids = expansion.get("source_id"), expansion.get("candidate_ids")
        if not isinstance(source_id, str) or not source_id or not isinstance(candidate_ids, list) or not candidate_ids:
            errors.append("every retained source needs a non-empty expansion row")
            continue
        if source_id in expanded_sources:
            errors.append(f"retained source appears in multiple expansion rows: {source_id}")
        expanded_sources[source_id] = candidate_ids
        for candidate_id in candidate_ids:
            if candidate_id not in candidates:
                errors.append(f"source {source_id} expands to missing candidate {candidate_id!r}")

    missing_sources = retained_sources - set(expanded_sources)
    extra_sources = set(expanded_sources) - retained_sources
    if missing_sources:
        errors.append("retained source candidates missing from triage: " + ", ".join(sorted(missing_sources)[:20]))
    if extra_sources:
        errors.append("selection ledger cites unknown retained sources: " + ", ".join(sorted(extra_sources)[:20]))

    selected = skipped = qualified_count = 0
    selected_candidate_sources: set[str] = set()
    for candidate_id, candidate in candidates.items():
        name = candidate.get("name")
        reason = candidate.get("reason")
        hard_gate = candidate.get("hard_gate")
        scores = candidate.get("scores")
        triage = candidate.get("triage")
        disposition = candidate.get("final_disposition")
        primary_sources = candidate.get("primary_sources")
        draft_sources = candidate.get("draft_sources")
        if not isinstance(name, str) or not name.strip() or not isinstance(reason, str) or len(reason.strip()) < 12:
            errors.append(f"candidate {candidate_id} lacks a useful name or decision reason")
        if not isinstance(hard_gate, dict) or set(hard_gate) != set(HARD_GATES) or not all(isinstance(hard_gate.get(field), bool) for field in HARD_GATES):
            errors.append(f"candidate {candidate_id} has malformed hard-gate evidence")
            continue
        if not isinstance(scores, dict) or set(scores) != set(SCORE_AXES) or not all(isinstance(scores.get(axis), int) and 0 <= scores[axis] <= 2 for axis in SCORE_AXES):
            errors.append(f"candidate {candidate_id} has malformed quality scores")
            continue
        if not isinstance(primary_sources, list) or not primary_sources or not all(isinstance(url, str) and url.startswith("https://") for url in primary_sources):
            errors.append(f"candidate {candidate_id} lacks HTTPS primary evidence")
        total = sum(scores.values())
        qualified = all(hard_gate.values()) and total >= 8 and all(value > 0 for value in scores.values())
        if qualified:
            qualified_count += 1
            if triage != "GREEN":
                errors.append(f"qualifying candidate {candidate_id} is not GREEN")
            if disposition not in {"include", "fold"}:
                errors.append(f"qualifying GREEN candidate {candidate_id} was dropped")
        else:
            if triage == "GREEN":
                errors.append(f"candidate {candidate_id} is GREEN without clearing the hard gate and score")
            if disposition != "skip":
                errors.append(f"sub-threshold candidate {candidate_id} was included")
        if disposition in {"include", "fold"}:
            selected += 1
            if isinstance(draft_sources, list):
                selected_candidate_sources.update(url for url in draft_sources if isinstance(url, str))
            if not isinstance(draft_sources, list) or not draft_sources:
                errors.append(f"selected candidate {candidate_id} lacks draft source evidence")
            elif any(url not in primary_sources or url not in draft for url in draft_sources):
                errors.append(f"selected candidate {candidate_id} is not linked to its primary source in the draft")
        elif disposition == "skip":
            skipped += 1
        else:
            errors.append(f"candidate {candidate_id} has invalid final disposition {disposition!r}")

    uncovered_activity = activity_selected_urls - selected_candidate_sources
    if uncovered_activity:
        errors.append("selected merged-PR activity lacks included candidate mapping: " + ", ".join(sorted(uncovered_activity)[:20]))

    referenced_candidates = {candidate_id for ids in expanded_sources.values() for candidate_id in ids}
    unreferenced = set(candidates) - referenced_candidates
    if unreferenced:
        errors.append("editorial candidates lack source provenance: " + ", ".join(sorted(unreferenced)[:20]))

    counts = {
        "retained_source_candidate_count": len(retained_sources),
        "editorial_candidate_count": len(candidates),
        "qualified_candidate_count": qualified_count,
        "selected_candidate_count": selected,
        "skipped_candidate_count": skipped,
        "unresolved_count": len(errors),
        **activity_counts,
    }
    receipt = {
        "schema_version": 1,
        "receipt_type": "selection-coverage",
        "verdict": "PASS" if not errors else "FAIL",
        "checker_version": CHECKER_VERSION,
        "source_pass_id": manifest.get("pass_id"),
        "source_manifest_path": str(manifest_path.resolve()),
        "source_manifest_sha256": manifest_hash,
        "ledger_path": str(ledger_path.resolve()),
        "ledger_sha256": file_hash(ledger_path),
        "draft_path": str(draft_path.resolve()),
        "draft_sha256": draft_hash,
        **counts,
        "final": not errors,
    }
    return errors, receipt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--draft", type=Path, required=True)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument(
        "--receipt-stdout",
        action="store_true",
        help="emit the complete PASS receipt as JSON without writing a receipt file",
    )
    args = parser.parse_args()
    if args.receipt and args.receipt_stdout:
        parser.error("--receipt and --receipt-stdout are mutually exclusive")
    try:
        errors, receipt = validate(args.manifest, args.ledger, args.draft)
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}")
        return 2
    if errors:
        print("FAIL: selection coverage is incomplete or admits low-signal work:")
        for error in errors:
            print(f"  - {error}")
        return 1
    if args.receipt_stdout:
        print(json.dumps(receipt, sort_keys=True))
        return 0
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(
        "PASS: "
        f"{receipt['retained_source_candidate_count']} retained source candidates -> "
        f"{receipt['editorial_candidate_count']} editorial candidates; "
        f"{receipt['selected_candidate_count']} selected, {receipt['skipped_candidate_count']} skipped"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
