#!/usr/bin/env python3
"""Bind the distinct finalized Compass #41 cutoff to the reviewed selection ledger."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data/newsletter_workspace/selection_coverage_wednesday_2026-09-23.json"
REVIEW = ROOT / "data/newsletter_workspace/final_cutoff_review_2026-09-23.md"
DRAFT = ROOT / "content/en/newsletters/2026-09-23-newsletter.md"
MANIFEST = Path("/opt/data/compass-worktrees/2026-09-23-final-cutoff/data/source_runs/source_run_2026-09-23_final-20260924T0041Z.json")
SELECTED_URL = "https://github.com/marmot-protocol/mdk/pull/2007"
SELECTED_SUMMARY = (
    "Merged MDK library work removes repeated lineage scans and state rewinds for parked encrypted "
    "messages after publish/join; regression tests cover one versus eight rows, but no tagged release "
    "or measured end-user latency result is claimed."
)
SKIP = {
    "https://github.com/SnowCait/nostter/pull/2585": "Notification-classification extraction supports the already covered account migration without a new client behavior.",
    "https://github.com/SnowCait/nostter/pull/2586": "Unused global Author store removal explicitly preserves existing account-state runtime behavior.",
    "https://github.com/SnowCait/nostter/pull/2587": "Account event loading is separated from application state while preserving current behavior; the migration issue remains open.",
    "https://github.com/Mesh-LLM/mesh-llm/pull/2026": "System One canary evidence handling has no demonstrated Nostr event, relay, or client change.",
    "https://github.com/marmot-protocol/mdk/pull/2005": "Public directory relay separation is preparation; bounded acquisition and recovery activation remain future work.",
}
TABLE_MESH_ID = "c5c5ad0eba413e18c10e3cd2be607e550ac818a8abaf97ccbf8fa242fbaff15f"
TABLE_MESH_URL = f"https://primal.net/e/{TABLE_MESH_ID}"
POSTERCHAN_ID = "35e74e8a6546c85a8ce540a845dc859010138ef03aec9572478bb4c5a111cfa2"
TABLE_MESH_SUMMARY = ("Developer-signed first Android release plays board games over a local Bluetooth/Wi-Fi mesh "
                      "and discovers optional sandboxed game modules on Nostr with Blossom downloads; real multi-phone testing is still requested.")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def main() -> None:
    ledger, manifest = load(LEDGER), load(MANIFEST)
    review, draft = REVIEW.read_text(), DRAFT.read_text()
    if "GATE: PASS" not in review:
        raise ValueError("final cutoff review is not accepted")
    if manifest.get("schema_version") != 2 or manifest.get("pass_id") != "final-20260924T0041Z" or manifest.get("finalized") is not True:
        raise ValueError("final cutoff manifest is not the expected finalized pass")
    if manifest.get("window") != {"since": "2026-09-23T23:44:00Z", "until": "2026-09-24T00:41:00Z"}:
        raise ValueError("final cutoff window changed")
    if sha(MANIFEST) not in review:
        raise ValueError("review does not bind the exact final cutoff manifest")
    families = manifest["families"]
    if set(families) != {"projects", "nip-discussions", "nostr-recap", "shakespeare-apps", "nip34", "zapstore", "app-discovery", "heartbeats", "monthly-history", "specs"}:
        raise ValueError("final cutoff is missing a maintained source family")
    if any(row["status"] not in {"complete", "empty_verified", "not_applicable"} for row in families.values()):
        raise ValueError("final cutoff contains an unfinished family")
    project_path = Path(families["projects"]["artifact_path"])
    if sha(project_path) != families["projects"]["artifact_sha256"] or sha(project_path) not in review:
        raise ValueError("final project source is not exactly bound")
    projects = load(project_path)["projects"]
    prs = [(repo, pr) for repo, project in projects.items() for pr in project.get("merged_prs", [])]
    by_url = {pr["url"]: (repo, pr) for repo, pr in prs}
    if len(prs) != 6 or len(by_url) != 6 or set(by_url) != set(SKIP) | {SELECTED_URL}:
        raise ValueError("final project PR identity set changed")
    if any(url not in review for url in by_url):
        raise ValueError("final review omits a merged PR")
    if SELECTED_URL not in draft or any(url in draft for url in SKIP):
        raise ValueError("draft does not match final cutoff decisions")
    zap_path = Path(families["zapstore"]["artifact_path"])
    if sha(zap_path) != families["zapstore"]["artifact_sha256"] or sha(zap_path) not in review:
        raise ValueError("final signed-store source is not exactly bound")
    releases = load(zap_path)["releases"]
    by_release = {row["release_id"]: row for row in releases}
    if (len(releases) != 2 or set(by_release) != {TABLE_MESH_ID, POSTERCHAN_ID}
            or (by_release[TABLE_MESH_ID]["app_id"], by_release[TABLE_MESH_ID]["version"]) != ("org.tablemesh.app", "0.1.0")
            or (by_release[POSTERCHAN_ID]["app_id"], by_release[POSTERCHAN_ID]["version"]) != ("place.poster.app", "1.0.2356")
            or by_release[TABLE_MESH_ID]["new_app"] is not True):
        raise ValueError("final signed-store release identity set changed")
    if TABLE_MESH_URL not in review or TABLE_MESH_URL not in draft or "https://zapstore.dev/apps/org.tablemesh.app" not in draft:
        raise ValueError("Table Mesh decision is not bound to the draft and primary event")
    if ledger.get("selected_count") != 70 or len(ledger["candidates"]) != 222:
        raise ValueError("pre-cutoff selection changed or cutoff already applied")
    review_ref = {"path": str(REVIEW), "sha256": sha(REVIEW)}
    selected_id = "activity:mdk-parked-replay-final"
    axes = dict(zip(ledger["score_axes"], [2, 2, 1, 2, 2]))
    gates = dict.fromkeys(ledger["hard_gate_fields"], True)
    ledger["candidates"].append({
        "candidate_id": selected_id, "name": "MDK parked-message replay",
        "hard_gate": gates, "scores": axes, "score_total": 9,
        "triage": "GREEN", "final_disposition": "include",
        "reason": SELECTED_SUMMARY, "primary_sources": [SELECTED_URL],
        "draft_sources": [SELECTED_URL], "section": "in_development",
        "triage_decision_ref": str(REVIEW) + "#merged-pr-dispositions",
    })
    ledger["selected"].append({
        "id": selected_id, "name": "MDK parked-message replay", "section": "in_development",
        "primary_sources": [SELECTED_URL],
        "hard_gates": {
            "direct_primary_evidence": True, "material_window_progress": True,
            "nostr_surface": True, "distinct_from_recent_coverage": True,
        },
        "score_axes": axes, "score_total": 9, "summary": SELECTED_SUMMARY,
        "continuity": "Merged after the 0.10.4 release; no tag or measured client latency is claimed.",
    })
    for url, (repo, pr) in by_url.items():
        if url == SELECTED_URL:
            cid = selected_id
        else:
            cid = f"skip:final-pr:{slug(repo)}:{pr['number']}"
            ledger["candidates"].append({
                "candidate_id": cid, "name": pr["title"],
                "hard_gate": {
                    "primary_evidence": True, "in_window_progress": True,
                    "nostr_surface": repo != "michaelneale/mesh-llm",
                    "continuity_delta": False,
                },
                "scores": None, "score_total": None,
                "triage": "SKIP", "final_disposition": "skip",
                "reason": SKIP[url], "primary_sources": [url], "draft_sources": [],
                "triage_decision_ref": str(REVIEW) + "#merged-pr-dispositions",
            })
        source_id = f"editorial:final-pr:{slug(repo)}:{pr['number']}"
        ledger["editorial_sources"].append({
            "source_id": source_id, "collector_source_ids": [],
            "editorial_provenance": {**review_ref, "locator": url},
        })
        ledger["source_expansion"].append({"source_id": source_id, "candidate_ids": [cid]})
    table_id = "zapstore:org.tablemesh.app:0.1.0"
    table_axes = dict(zip(ledger["score_axes"], [1, 2, 2, 1, 2]))
    table_url = "https://zapstore.dev/apps/org.tablemesh.app"
    ledger["candidates"].append({
        "candidate_id": table_id, "name": "Table Mesh 0.1.0",
        "hard_gate": gates, "scores": table_axes, "score_total": 8,
        "triage": "GREEN", "final_disposition": "include",
        "reason": TABLE_MESH_SUMMARY,
        "primary_sources": [TABLE_MESH_URL, table_url], "draft_sources": [TABLE_MESH_URL, table_url],
        "section": "tagged_releases", "triage_decision_ref": str(REVIEW) + "#signed-store-dispositions",
    })
    ledger["selected"].append({
        "id": table_id, "name": "Table Mesh 0.1.0", "section": "tagged_releases",
        "primary_sources": [TABLE_MESH_URL, table_url],
        "hard_gates": {
            "direct_primary_evidence": True, "material_window_progress": True,
            "nostr_surface": True, "distinct_from_recent_coverage": True,
        },
        "score_axes": table_axes, "score_total": 8, "summary": TABLE_MESH_SUMMARY,
        "continuity": "First signed 0.1.0 release; Nostr delivers optional games, while table play is offline and real multi-phone validation is pending.",
    })
    ledger["candidates"].append({
        "candidate_id": "skip:final-zapstore:place.poster.app:1.0.2356", "name": "PosterChan 1.0.2356",
        "hard_gate": {"primary_evidence": True, "in_window_progress": True,
                      "nostr_surface": False, "continuity_delta": False},
        "scores": None, "score_total": None, "triage": "SKIP", "final_disposition": "skip",
        "reason": "Signed update concerns linked Pleroma follow import and bridge puppets; no distinct Nostr milestone beyond the previously skipped app-store release.",
        "primary_sources": [f"https://primal.net/e/{POSTERCHAN_ID}"], "draft_sources": [],
        "triage_decision_ref": str(REVIEW) + "#signed-store-dispositions",
    })
    for app_id, cid, release_id in (("org.tablemesh.app", table_id, TABLE_MESH_ID),
                                    ("place.poster.app", "skip:final-zapstore:place.poster.app:1.0.2356", POSTERCHAN_ID)):
        source_id = f"editorial:final-zapstore:{slug(app_id)}"
        ledger["editorial_sources"].append({
            "source_id": source_id, "collector_source_ids": [],
            "editorial_provenance": {**review_ref, "locator": f"https://primal.net/e/{release_id}"},
        })
        ledger["source_expansion"].append({"source_id": source_id, "candidate_ids": [cid]})
    ledger["selected_count"] = len(ledger["selected"])
    ledger["draft_sha256"] = sha(DRAFT)
    ledger["source_reconciliation"]["final_cutoff"] = {
        "manifest_path": str(MANIFEST), "manifest_sha256": sha(MANIFEST),
        "review_path": str(REVIEW), "review_sha256": sha(REVIEW),
        "project_artifact_path": str(project_path), "project_artifact_sha256": sha(project_path),
        "zapstore_artifact_path": str(zap_path), "zapstore_artifact_sha256": sha(zap_path),
        "merged_pr_count": 6, "release_count": 0, "signed_store_release_count": 2,
    }
    ledger["finalization_note"] += " Separate finalized final cutoff: six merged PRs and two signed store releases, with selected MDK library and Table Mesh milestones."
    LEDGER.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"candidates": len(ledger["candidates"]), "selected": ledger["selected_count"]}))


if __name__ == "__main__":
    main()
