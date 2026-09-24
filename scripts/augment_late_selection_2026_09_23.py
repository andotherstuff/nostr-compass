#!/usr/bin/env python3
"""Fold the separately verified late cutoff into Compass #41's selection ledger."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "data/newsletter_workspace"
LEDGER = WORK / "selection_coverage_wednesday_2026-09-23.json"
INVENTORY = WORK / "late_delta_inventory_2026-09-23.json"
REVIEW = WORK / "late_delta_review_2026-09-23.md"
DRAFT = ROOT / "content/en/newsletters/2026-09-23-newsletter.md"

GROUPS = {
    "Amethyst": {
        "id": "activity:amethyst-mls-late",
        "name": "Amethyst MLS interoperability and group rendering",
        "pr_numbers": {4182, 4183, 4184, 4185, 4187, 4188, 4189},
        "draft_numbers": {4182, 4184, 4187, 4188, 4189},
        "score": 9,
        "summary": "Merged Quartz options improve cross-stack MLS group creation, extensions, authenticated data, and key-package lifetime; desktop group rendering also stops blank messages. No tagged release is claimed.",
    },
    "Nostter": {
        "id": "activity:nostter-capabilities-late",
        "name": "nostter signer-capability migration",
        "pr_numbers": set(range(2570, 2585)),
        "draft_numbers": {2570, 2574, 2576, 2577},
        "score": 9,
        "summary": "Merged app changes gate writes, private reads, and remote signer settings on actual signer or decrypter capabilities; later projection removals support the same migration.",
    },
    "Pensieve": {
        "id": "activity:pensieve-archive-late",
        "name": "Pensieve archive reconciliation",
        "pr_numbers": {48, 49, 50},
        "draft_numbers": {48, 49, 50},
        "score": 8,
        "summary": "Three merged library steps make archive receipt completion durable, independent of optional Parquet sealing, and bounded in a replayable inventory; no deployed worker is claimed.",
    },
}
SKIP_REASONS = {
    ("Buzz", 7844): "Provider-model label grammar is not a Nostr-facing change.",
    ("diVine", 9413): "Supporter badges require an unverified companion deployment and add no demonstrated Nostr event behavior.",
    ("Mostro", 976): "PR quality documentation does not change shipped Nostr behavior.",
    ("Angor", 974): "Bitcoin indexer retries and test throttling have no demonstrated Nostr-facing effect.",
    ("Angor", 973): "Bitcoin indexer error parsing has no demonstrated Nostr-facing effect.",
    ("Marmot Protocol (mdk)", 2008): "Audit OTLP attempt remains inactive with no production sender, native binding, or user-facing release.",
    ("Heterodyne", 33): "Optional read-only FIDO custody checker leaves the live Nostr protocol unchanged.",
}
FIPS_PRS = {49, 50, 51, 52}
FIPS_ID = "top:fips2go-0.6.0"
FIPS_SUMMARY = ("Version 0.6.0 adds local mesh names; 0.6.1 repairs DNS64 bootstrap address selection "
                "without field validation; 0.7.0 adds three default bootstrap links and opt-in, capped Nostr discovery.")
SNO_ID = "activity:amethyst-deck0003-late"
SNO_SUMMARY = ("Merged DECK-0003 work parses and renders Nostr 3D objects, handles avatar/shard/bag event kinds, "
               "and opens hinted encrypted region bags with reference conformance; the bag UI is not phone-verified.")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def main() -> None:
    ledger = json.loads(LEDGER.read_text())
    inventory = json.loads(INVENTORY.read_text())
    review = REVIEW.read_text()
    draft = DRAFT.read_text()
    if "GATE: PASS" not in review:
        raise ValueError("late delta review is not final")
    if inventory.get("source_artifact_sha256") not in review:
        raise ValueError("late review does not bind the project collector artifact")
    if inventory.get("source_manifest_sha256") not in review:
        raise ValueError("late review does not bind the finalized cutoff pass")
    if len(inventory["merged_prs"]) != 37 or len(inventory["releases"]) != 2:
        raise ValueError("late inventory count changed")
    if len(ledger["candidates"]) != 211 or len(ledger["selected"]) != 66:
        raise ValueError("Wednesday base ledger changed or late delta already applied")
    review_ref = {"path": str(REVIEW), "sha256": digest(REVIEW)}
    selected_by_id = {row["id"]: row for row in ledger["selected"]}
    candidate_by_id = {row["candidate_id"]: row for row in ledger["candidates"]}
    fips = candidate_by_id[FIPS_ID]
    fips_selected = selected_by_id[FIPS_ID]
    release_urls = [row["url"] for row in inventory["releases"]]
    if sorted(row["tag"] for row in inventory["releases"]) != ["v0.6.1", "v0.7.0"]:
        raise ValueError("late fips2go tag set changed")
    if any(url not in draft or url not in review for url in release_urls):
        raise ValueError("late fips2go release missing from draft or review")
    fips["name"] = fips_selected["name"] = "fips2go 0.6.0–0.7.0"
    fips["reason"] = fips_selected["summary"] = FIPS_SUMMARY
    fips["primary_sources"] += release_urls
    fips["draft_sources"] += release_urls
    fips_selected["primary_sources"] += release_urls
    for release in inventory["releases"]:
        url = release["url"]
        source_id = "editorial:late-release:fips2go-" + release["tag"]
        ledger["editorial_sources"].append({
            "source_id": source_id, "collector_source_ids": [],
            "editorial_provenance": {**review_ref, "locator": url},
        })
        ledger["source_expansion"].append({"source_id": source_id, "candidate_ids": [FIPS_ID]})

    zzub_rows = inventory.get("zapstore_releases", [])
    if len(zzub_rows) != 1 or zzub_rows[0].get("app_id") != "social.cloudfodder.zzub" or zzub_rows[0].get("version") != "0.0.16":
        raise ValueError("late signed Zzub release identity changed")
    if inventory.get("zapstore_artifact_sha256") not in review:
        raise ValueError("late Zapstore artifact is not bound by review")
    zzub_url = zzub_rows[0]["url"]
    if zzub_url not in draft or zzub_url not in review:
        raise ValueError("late Zzub signed source missing from draft or review")
    zzub_id = "zapstore:social.cloudfodder.zzub"
    zzub = candidate_by_id[zzub_id]
    zzub_selected = selected_by_id[zzub_id]
    zzub_name = "Zzub 0.0.15–0.0.16"
    zzub_summary = ("Developer-signed 0.0.15 brings mobile status boards, comments, review decisions, Git browsing and diffs; "
                    "signed 0.0.16 restores announced projects and adds project-wide Tasks/Reviews tabs, mentions and filters.")
    zzub["name"] = zzub_selected["name"] = zzub_name
    zzub["reason"] = zzub_selected["summary"] = zzub_summary
    zzub["primary_sources"].append(zzub_url)
    zzub["draft_sources"].append(zzub_url)
    zzub_selected["primary_sources"].append(zzub_url)
    zzub_source_id = "editorial:late-zapstore:zzub-0.0.16"
    ledger["editorial_sources"].append({
        "source_id": zzub_source_id, "collector_source_ids": [],
        "editorial_provenance": {**review_ref, "locator": zzub_url},
    })
    ledger["source_expansion"].append({"source_id": zzub_source_id, "candidate_ids": [zzub_id]})

    prs = inventory["merged_prs"]
    if len({(row["project"], row["number"]) for row in prs}) != 37:
        raise ValueError("duplicate late PR identity")
    by_identity = {(row["project"], row["number"]): row for row in prs}
    expected = (set(SKIP_REASONS)
                | {("fips2go", n) for n in FIPS_PRS}
                | {("Amethyst", 4186)}
                | {(project, n) for project, group in GROUPS.items()
                   for n in group["pr_numbers"]})
    if set(by_identity) != expected:
        raise ValueError("late PR decisions do not exactly cover the collector inventory")
    for project, group in GROUPS.items():
        urls = [by_identity[(project, n)]["url"] for n in sorted(group["draft_numbers"])]
        if any(url not in draft or url not in review for url in urls):
            raise ValueError(f"grouped {project} source absent from draft or review")
        axes = dict(zip(ledger["score_axes"], [2, 2, 1, 2, 2] if group["score"] == 9
                        else [2, 2, 1, 2, 1]))
        gates = dict.fromkeys(ledger["hard_gate_fields"], True)
        candidate = {
            "candidate_id": group["id"], "name": group["name"], "hard_gate": gates,
            "scores": axes, "score_total": sum(axes.values()), "triage": "GREEN",
            "final_disposition": "include", "reason": group["summary"],
            "primary_sources": urls, "draft_sources": urls, "section": "in_development",
            "triage_decision_ref": str(REVIEW) + "#merged-pr-dispositions",
        }
        ledger["candidates"].append(candidate)
        ledger["selected"].append({
            "id": group["id"], "name": group["name"], "section": "in_development",
            "primary_sources": urls,
            "hard_gates": {
                "direct_primary_evidence": True, "material_window_progress": True,
                "nostr_surface": True, "distinct_from_recent_coverage": True,
            },
            "score_axes": axes, "score_total": sum(axes.values()),
            "summary": group["summary"], "continuity": "",
        })
    sno_url = by_identity[("Amethyst", 4186)]["url"]
    if sno_url not in draft or sno_url not in review:
        raise ValueError("DECK-0003 primary source absent from draft or review")
    sno_axes = dict(zip(ledger["score_axes"], [2, 2, 2, 2, 1]))
    ledger["candidates"].append({
        "candidate_id": SNO_ID, "name": "Amethyst DECK-0003 objects and encrypted bag search",
        "hard_gate": dict.fromkeys(ledger["hard_gate_fields"], True),
        "scores": sno_axes, "score_total": 9, "triage": "GREEN",
        "final_disposition": "include", "reason": SNO_SUMMARY,
        "primary_sources": [sno_url], "draft_sources": [sno_url],
        "section": "in_development",
        "triage_decision_ref": str(REVIEW) + "#merged-pr-dispositions",
    })
    ledger["selected"].append({
        "id": SNO_ID, "name": "Amethyst DECK-0003 objects and encrypted bag search",
        "section": "in_development", "primary_sources": [sno_url],
        "hard_gates": {
            "direct_primary_evidence": True, "material_window_progress": True,
            "nostr_surface": True, "distinct_from_recent_coverage": True,
        },
        "score_axes": sno_axes, "score_total": 9,
        "summary": SNO_SUMMARY, "continuity": "",
    })

    for row in prs:
        project, number, url = row["project"], row["number"], row["url"]
        if url not in review:
            raise ValueError(f"late PR missing from review: {url}")
        if project == "fips2go":
            candidate_id = FIPS_ID
        elif project in GROUPS and number in GROUPS[project]["pr_numbers"]:
            candidate_id = GROUPS[project]["id"]
        elif project == "Amethyst" and number == 4186:
            candidate_id = SNO_ID
        else:
            candidate_id = f"skip:late-pr:{slug(project)}:{number}"
            reason = SKIP_REASONS[(project, number)]
            ledger["candidates"].append({
                "candidate_id": candidate_id, "name": row["title"],
                "hard_gate": {
                    "primary_evidence": True, "in_window_progress": True,
                    "nostr_surface": False, "continuity_delta": False,
                },
                "scores": None, "score_total": None, "triage": "SKIP",
                "final_disposition": "skip", "reason": reason,
                "primary_sources": [url], "draft_sources": [],
                "triage_decision_ref": str(REVIEW) + "#merged-pr-dispositions",
            })
        source_id = f"editorial:late-pr:{slug(project)}:{number}"
        ledger["editorial_sources"].append({
            "source_id": source_id, "collector_source_ids": [],
            "editorial_provenance": {**review_ref, "locator": url},
        })
        ledger["source_expansion"].append({"source_id": source_id, "candidate_ids": [candidate_id]})
    ledger["selected_count"] = len(ledger["selected"])
    ledger["draft_sha256"] = digest(DRAFT)
    ledger["source_reconciliation"]["late_delta"] = {
        "review_path": str(REVIEW), "review_sha256": digest(REVIEW),
        "inventory_path": str(INVENTORY), "inventory_sha256": digest(INVENTORY),
        "source_manifest_sha256": inventory["source_manifest_sha256"],
        "merged_pr_count": 37, "release_count": 2,
    }
    ledger["finalization_note"] += " Separate finalized late cutoff: 37 merged PRs and two fips2go releases, with all dispositions bound to the late review."
    LEDGER.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"candidates": len(ledger["candidates"]), "selected": ledger["selected_count"],
                      "skipped": len(ledger["candidates"]) - ledger["selected_count"]}))


if __name__ == "__main__":
    main()
