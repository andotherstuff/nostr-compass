#!/usr/bin/env python3
"""Rebase the reviewed Compass #41 ledger onto the complete Wednesday source pass.

This is a deterministic editorial reconciliation, not a collector or network
client. New release decisions are explicit; discovery-only leads remain SKIP.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/newsletter_workspace/selection_coverage_2026-09-23.json"
MANIFEST = ROOT / "data/source_runs/source_run_2026-09-23_wednesday-2026-09-23-codex-recovery-1.json"
DRAFT = ROOT / "content/en/newsletters/2026-09-23-newsletter.md"
TRIAGE = ROOT / "data/newsletter_workspace/triage_2026-09-23.md"
REVIEW = ROOT / "data/newsletter_workspace/selection_review_2026-09-23.md"
ACTIVITY_REVIEW = ROOT / "data/newsletter_workspace/project_activity_coverage_2026-09-23.md"
PROJECT_DECISIONS = ROOT / "data/newsletter_workspace/project_activity_decisions_2026-09-23.json"
RELEASES = [
    ("release:scramble-0.7.2", "Scramble 0.7.2", "DavidGershony/openChat",
     "https://github.com/DavidGershony/Scramble/releases/tag/v0.7.2",
     "Switches to Dark Matter MLS without migrating 0.6.x groups, and offers two interchangeable Android view layers under one app identity.", 9),
    ("release:morganite-0.0.5", "Morganite 0.0.5", "greenart7c3/Morganite",
     "https://github.com/greenart7c3/Morganite/releases/tag/v0.0.5",
     "Adds Tor-aware .onion Blossom fetching and cache-miss Range handling for seekable uncached video.", 9),
    ("release:bitcredit-0.5.16", "Bitcredit E-Bills 0.5.16", "BitcreditProtocol/Bitcredit-Core",
     "https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.16",
     "Repairs Nostr 0.45 signature serialization compatibility and failed bill-event resend and resynchronization paths.", 9),
    ("release:fips-ts-0.0.43", "fips-ts runtime 0.0.43", "mmalmi/fips-ts",
     "https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.43",
     "Preserves authenticated identity across concurrent FIPS WebRTC handover and rejects late negotiation callbacks.", 8),
]
SKIPPED_RELEASE = (
    "release:toll-booth-6.2.6", "toll-booth 6.2.6", "forgesworn/toll-booth",
    "https://github.com/forgesworn/toll-booth/releases/tag/v6.2.6",
    "General payment-middleware session and reconciliation fixes lack a concrete Nostr-facing release change.",
)
ADDITIONAL_TAGGED_RELEASES = [
    ("release:noornote-1.6.0", "NoorNote 1.6.0", "77elements/noornote",
     "https://github.com/77elements/noornote/releases/tag/v1.6.0",
     "Adds public and encrypted Nostr calendar events, reminders, and interactive shared-event cards.", 9),
    ("release:noornote-1.7.0", "NoorNote 1.7.0", "77elements/noornote",
     "https://github.com/77elements/noornote/releases/tag/v1.7.0",
     "Adds appointment booking and cancellation by Nostr direct message, plus calendar import/export and NWC recovery fixes.", 9),
]
ADDITIONAL_TOP_RELEASE = (
    "release:napplet-soyli-0.20.0", "napplet.soy CLI 0.20.0", "zeSchlausKwab/napplet-soy",
    "https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.20.0",
    "Adds scoped NIP-78 helpers for reusable public napplet data, with consent and revision checks; website deployment is separate.", 8,
)
ZAPSTORE_RELEASES = [
    ("eu.decentnewsroom.bookshelf", "0.1.25", "Bookshelf 0.1.25",
     "https://github.com/decent-newsroom/bookshelf-app/releases/tag/v0.1.25",
     "Signed book-rating and review revisions persist through an outbox and newest-event cache, with code and tests in the tagged diff.", 9),
    ("org.cordn.app", "0.5.0", "Cordn 0.5.0",
     "https://github.com/Cordn-msg/cordn-web/releases/tag/v0.5.0",
     "Encrypted group text sends gain durable offline queueing and explicit NIP-44 signer-capability checks.", 9),
    ("space.einundzwanzig.meetup", "1.6.6", "21Meetup 1.6.6",
     "https://github.com/louisthecat86/Einundzwanzig-Meetup-App/releases/tag/v1.6.6",
     "Bounded multi-hop attendance trust, retryable badge publication, and relay-acknowledged success repair a Nostr-facing workflow.", 9),
    ("space.einundzwanzig.mobile", "1.13.0", "TWENTY ONE Companion 1.13.0",
     "https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.13.0",
     "Relay-backed pins, explicit public Nostr RSVP disclosure, and contact-list preview guards ship together.", 9),
    ("buzz.armada.app", "0.61.0", "Armada 0.61.0",
     "https://primal.net/e/122a06dbab02d207b3aa793b0fedd06fd59d36178a7b9ae5971cfc3b7f3eb6ce",
     "Developer-signed update adds opt-in media proxying, profile moderation, and automatic private-channel role keys in an encrypted Nostr client.", 9),
    ("pub.ditto.app", "2.40.0", "Ditto 2.40.0",
     "https://gitlab.com/soapbox-pub/ditto/-/releases/v2.40.0",
     "Profile Top 8 rankings gain an explicit publish step and a follower-feed card, distinct from earlier Ditto media coverage.", 8),
    ("com.xmarcade.app", "1.1.3", "XM Arcade 1.1.3",
     "https://primal.net/e/dec0edda9ff464b4b7598032318cb48e17cf496e29d05031d1f1629409039a4c",
     "Mini-app post consent is bound to one run, request, app, account, group, and channel with expiry and replay protection; group-key epoch trust persists across restart.", 8),
    ("social.cloudfodder.zzub", "0.0.15", "Zzub 0.0.15",
     "https://primal.net/e/70c5efeea2e9314329b8951346d83ad0688b74607a108e8bc820caae545196c2",
     "Developer-signed release adds mobile status boards with sorting, filters, threaded comments, named assignees, review decisions, source browsing, and pull-request diffs.", 9),
]
ACTIVITY = [
    ("activity:divine-mobile", "Divine Mobile relay reconnection", "divinevideo/divine-mobile", "https://github.com/divinevideo/divine-mobile/pull/9246", "Idle or remote-closed relay connections now self-heal so passive video and moderation subscriptions recover without an outgoing send.", 9),
    ("activity:nostter", "nostter remote signing", "SnowCait/nostter", "https://github.com/SnowCait/nostter/pull/2518", "Remote signer lifecycle is tied to the active session so stale signers cannot outlive the user's session.", 9),
    ("activity:conduit-mono", "Conduit Blossom images", "Conduit-BTC/conduit-mono", "https://github.com/Conduit-BTC/conduit-mono/pull/503", "Marketplace product images are uploaded through Blossom with signed Nostr authorization.", 9),
    ("activity:block-buzz", "Buzz relay moderation", "block/buzz", "https://github.com/block/buzz/pull/7302", "Relay moderation routes require signed authorization and record an audit trail.", 9),
    ("activity:zapcooking", "Zap Cooking image descriptions", "zapcooking/frontend", "https://github.com/zapcooking/frontend/pull/746", "Image descriptions use NIP-92 tags for interoperable Nostr media display.", 8),
    ("activity:contextvm-ts-sdk", "ContextVM SDK relay acknowledgements", "contextvm/ts-sdk", "https://github.com/ContextVM/sdk/pull/100", "Publishing waits for the first positive relay acknowledgement by default, without blocking on the slowest relay.", 9),
    ("activity:nostream", "nostream NIP-66 relay health", "Cameri/nostream", "https://github.com/cameri/nostream/pull/741", "The relay emits signed NIP-66 health events for external monitoring.", 8),
    ("activity:mostro-nip69", "Mostro stable order time", "MostroP2P/mostro", "https://github.com/MostroP2P/mostro/pull/971", "Nostr trading orders retain their original creation time across status revisions.", 9),
    ("activity:nostream-pow", "nostream adaptive proof of work", "Cameri/nostream", "https://github.com/cameri/nostream/pull/779", "An opt-in web-of-trust distance rule lowers adaptive proof-of-work difficulty for nearby keys while unknown keys retain the full requirement.", 9),
    ("activity:nostter-share", "nostter image sharing", "SnowCait/nostter", "https://github.com/SnowCait/nostter/pull/2510", "The web share target accepts images and passes them into the normal Nostr composer and upload flow.", 8),
    ("activity:zapcooking-search", "Zap Cooking safe Nostr search", "zapcooking/frontend", "https://github.com/zapcooking/frontend/pull/744", "Pasted Nostr identifiers open directly and secret keys are rejected before relay search.", 9),
    ("activity:divine-profile", "Divine Mobile profile verification", "divinevideo/divine-mobile", "https://github.com/divinevideo/divine-mobile/pull/9293", "Profile verification waits for every queried relay before declaring linked accounts absent.", 9),
    ("activity:contextvm-stream", "ContextVM SDK stream sequencing", "contextvm/ts-sdk", "https://github.com/ContextVM/sdk/pull/95", "Client-started streams use one per-sender sequence for accept and control frames, avoiding duplicate sequence numbers.", 9),
    ("activity:0xchat-security", "0xchat audit security fixes", "0xchat-app/0xchat-app-main", "https://github.com/0xchat-app/0xchat-app-main/pull/92", "Merged fixes restrict Cashu P2PK witness signing, validate gift-wrap seals and trusted configuration, and require WebView signing consent; no app release is claimed.", 9),
    ("activity:nos2x-pin", "nos2x-fox PIN bridge protection", "diegogurpegui/nos2x-fox", "https://github.com/diegogurpegui/nos2x-fox/pull/69", "Merged page-bridge and background checks stop websites from reading the PIN that derives the Nostr private-key encryption key.", 9),
    ("activity:nos2x-identifier", "nos2x-fox deterministic provider", "diegogurpegui/nos2x-fox", "https://github.com/diegogurpegui/nos2x-fox/pull/67", "Merged document-start injection removes a web-accessible script URL that disclosed a stable extension identifier.", 9),
]

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def require(value: bool, message: str) -> None:
    if not value:
        raise ValueError(message)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--delta-output", type=Path, required=True)
    args = parser.parse_args()
    base, manifest = copy.deepcopy(load(BASE)), load(MANIFEST)
    require(base["schema_version"] == 1 and base["final"] is True and len(base["candidates"]) == 144,
            "reviewed Tuesday ledger changed")
    require(manifest["schema_version"] == 2 and manifest["finalized"] is True
            and manifest["pass_id"] == "wednesday-2026-09-23-codex-recovery-1",
            "Wednesday source manifest is not final")
    families = manifest["families"]
    require(all(meta["status"] in {"complete", "empty_verified", "not_applicable"}
                for meta in families.values()), "incomplete source family")
    draft = DRAFT.read_text(encoding="utf-8")
    review_text = REVIEW.read_text(encoding="utf-8")
    artifacts = {family: Path(meta["artifact_path"]).read_text(encoding="utf-8")
                 for family, meta in families.items() if meta.get("artifact_path")}
    included = {f"{family}:{raw}" for family, meta in families.items()
                for raw, decision in meta["dispositions"].items() if decision["decision"] == "include"}
    selected_ids = {"editorial:" + row["candidate_id"] for row in base["candidates"]
                    if row["final_disposition"] in {"include", "fold"}}
    superseded_raw = []
    superseded_sources = []
    def retire_skipped(row: dict) -> None:
        candidate_ids = next(item["candidate_ids"] for item in base["source_expansion"]
                             if item["source_id"] == row["source_id"])
        require(row["source_id"] not in selected_ids
                and all(cid not in {s["id"] for s in base["selected"]} for cid in candidate_ids),
                f"cannot retire selected candidate: {row['source_id']}")
        base["editorial_sources"].remove(row)
        base["source_expansion"] = [item for item in base["source_expansion"]
                                    if item["source_id"] != row["source_id"]]
        base["candidates"] = [item for item in base["candidates"]
                              if item["candidate_id"] not in candidate_ids]
        superseded_sources.append(row["source_id"])
        for bucket in ("zapstore_only", "tagged_release_projects"):
            entries = base["source_reconciliation"].get(bucket)
            if isinstance(entries, list):
                base["source_reconciliation"][bucket] = [item for item in entries
                                                          if item.get("source_id") not in candidate_ids]
    for row in list(base["editorial_sources"]):
        raw = row["collector_source_ids"]
        missing = [value for value in raw if value not in included]
        require(not missing or row["source_id"] not in selected_ids,
                f"selected collector record vanished: {row['source_id']}: {missing[:3]}")
        if missing:
            superseded_raw.extend(missing)
            retire_skipped(row)
            continue
        if "artifact_provenance" in row:
            provenance = row["artifact_provenance"]
            family = provenance["family"]
            meta = families[family]
            if not any(isinstance(value, str) and value in artifacts[family]
                       for value in provenance["locator"].values()):
                retire_skipped(row)
                continue
            provenance["artifact_path"] = meta["artifact_path"]
            provenance["artifact_sha256"] = meta["artifact_sha256"]
        if "editorial_provenance" in row:
            editorial = row["editorial_provenance"]
            require(editorial["locator"] in review_text,
                    f"selection review locator missing: {row['source_id']}")
            editorial["path"] = str(REVIEW)
            editorial["sha256"] = sha(REVIEW)
    project_data = load(Path(families["projects"]["artifact_path"]))["projects"]
    def record(item: tuple, *, include: bool, section: str = "tagged_releases",
               reconcile_project: bool = True, triage_ref: str = "wednesday-exact-window-release-delta") -> None:
        cid, name, repo, url, reason, *score = item
        require(url in draft if include else True, f"draft omits selected source: {cid}")
        release = next((release for release in project_data[repo]["releases"]
                        if release["url"] == url), None)
        require(release is not None, f"project release absent: {cid}")
        raw = f"projects:/repos/{repo}/releases:{release['id']}"
        require(raw in included, f"release not retained by collector: {cid}")
        source_id = "editorial:" + cid
        require(all(row["source_id"] != source_id for row in base["editorial_sources"]),
                f"duplicate editorial source: {source_id}")
        base["editorial_sources"].append({
            "source_id": source_id, "collector_source_ids": [raw],
            "artifact_provenance": {
                "family": "projects", "artifact_path": families["projects"]["artifact_path"],
                "artifact_sha256": families["projects"]["artifact_sha256"],
                "locator": {"primary_url": url, "repository": repo},
            },
        })
        base["source_expansion"].append({"source_id": source_id, "candidate_ids": [cid]})
        scores = dict(zip(base["score_axes"], [2, 2, 2, 2, 1] if score and score[0] == 9
                          else [2, 2, 1, 2, 1])) if include else None
        gates = dict.fromkeys(base["hard_gate_fields"], True) if include else {
            "primary_evidence": True, "in_window_progress": True,
            "nostr_surface": False, "continuity_delta": True,
        }
        base["candidates"].append({
            "candidate_id": cid, "name": name, "hard_gate": gates,
            "scores": scores, "score_total": sum(scores.values()) if scores else None,
            "triage": "GREEN" if include else "SKIP",
            "final_disposition": "include" if include else "skip", "reason": reason,
            "primary_sources": [url], "draft_sources": [url] if include else [],
            "section": section if include else None,
            "triage_decision_ref": str(TRIAGE) + "#" + triage_ref,
        })
        if include:
            base["selected"].append({
                "id": cid, "name": name, "section": section,
                "primary_sources": [url],
                "hard_gates": {
                    "direct_primary_evidence": True, "material_window_progress": True,
                    "nostr_surface": True, "distinct_from_recent_coverage": True,
                },
                "score_axes": scores, "score_total": sum(scores.values()),
                "summary": reason, "continuity": "",
            })
        if reconcile_project:
            base["source_reconciliation"]["tagged_release_projects"].append({
                "source_id": cid, "name": name, "verdict": "selected" if include else "skip",
                "decision_source": str(TRIAGE) + "#" + triage_ref,
            })
    for release in RELEASES:
        record(release, include=True)
    for release in ADDITIONAL_TAGGED_RELEASES:
        record(release, include=True, reconcile_project=False, triage_ref="scope-review-release-reconciliation")
    record(ADDITIONAL_TOP_RELEASE, include=True, section="top_stories",
           reconcile_project=False, triage_ref="scope-review-release-reconciliation")
    record(SKIPPED_RELEASE, include=False)
    # The draft already has eight In Development stories. Bind each to its
    # exact merged-PR collector record; a prose-only activity audit is not a
    # selection ledger disposition.
    for cid, name, repo, url, reason, score in ACTIVITY:
        require(url in draft and url in ACTIVITY_REVIEW.read_text(encoding="utf-8"),
                f"activity source absent from draft or audit: {cid}")
        pr = next((item for item in project_data[repo]["merged_prs"] if item["url"] == url), None)
        require(pr is not None, f"merged PR absent from Wednesday project artifact: {cid}")
        raw_matches = [raw for raw in included if raw.startswith("projects:")
                       and raw.endswith(f"/pulls:{pr['id']}")]
        require(len(raw_matches) == 1, f"merged PR is not one retained collector record: {cid}")
        source_id = "editorial:" + cid
        require(all(row["source_id"] != source_id for row in base["editorial_sources"]),
                f"duplicate activity source: {cid}")
        base["editorial_sources"].append({
            "source_id": source_id, "collector_source_ids": raw_matches,
            "artifact_provenance": {
                "family": "projects", "artifact_path": families["projects"]["artifact_path"],
                "artifact_sha256": families["projects"]["artifact_sha256"],
                "locator": {"primary_url": url, "repository": repo},
            },
        })
        base["source_expansion"].append({"source_id": source_id, "candidate_ids": [cid]})
        scores = dict(zip(base["score_axes"], [2, 2, 2, 2, 1] if score == 9
                          else [2, 2, 1, 2, 1]))
        base["candidates"].append({
            "candidate_id": cid, "name": name,
            "hard_gate": dict.fromkeys(base["hard_gate_fields"], True),
            "scores": scores, "score_total": sum(scores.values()),
            "triage": "GREEN", "final_disposition": "include", "reason": reason,
            "primary_sources": [url], "draft_sources": [url], "section": "in_development",
            "triage_decision_ref": str(ACTIVITY_REVIEW) + "#green--eight-selected-projects-thirteen-pr-milestones",
        })
        base["selected"].append({
            "id": cid, "name": name, "section": "in_development", "primary_sources": [url],
            "hard_gates": {
                "direct_primary_evidence": True, "material_window_progress": True,
                "nostr_surface": True, "distinct_from_recent_coverage": True,
            },
            "score_axes": scores, "score_total": sum(scores.values()),
            "summary": reason, "continuity": "",
        })
    # Both source series were already described in the draft; the Tuesday
    # ledger cited only their first/last tag and therefore understated evidence.
    for cid, repo, older_url, latest_url in (
        ("release:scramble-0.7.2", "DavidGershony/openChat",
         "https://github.com/DavidGershony/Scramble/releases/tag/v0.7.0",
         "https://github.com/DavidGershony/Scramble/releases/tag/v0.7.2"),
        ("release:wot-extension-0.8.0", "nostr-wot/nostr-wot-extension",
         "https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.0",
         "https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.3"),
    ):
        require(older_url in draft and latest_url in draft, f"series not linked in draft: {cid}")
        releases = {item["url"]: item for item in project_data[repo]["releases"]}
        require(older_url in releases and latest_url in releases, f"series missing source release: {cid}")
        source = next(row for row in base["editorial_sources"] if row["source_id"] == "editorial:" + cid)
        raw = [f"projects:/repos/{repo}/releases:{releases[url]['id']}"
               for url in (older_url, latest_url)]
        require(all(item in included for item in raw), f"series not retained by collector: {cid}")
        source["collector_source_ids"] = list(dict.fromkeys(raw))
        urls = list(dict.fromkeys((older_url, latest_url)))
        candidate = next(row for row in base["candidates"] if row["candidate_id"] == cid)
        selected = next(row for row in base["selected"] if row["id"] == cid)
        candidate["primary_sources"] = candidate["draft_sources"] = urls
        selected["primary_sources"] = urls
        if cid.startswith("release:wot-"):
            candidate["name"] = selected["name"] = "nostr-wot-extension 0.8.0–0.8.3"
            candidate["reason"] = selected["summary"] = (
                "The 0.8.0 release restores opt-in graph queries and protects follow-list replacement; "
                "0.8.3 adds scoped NWC connections with daily budgets, expiry and revocation.")
    amethyst_id = "release:amethyst-1.16.0"
    amethyst_summary = (
        "The tagged release fixes single-flight fast Blossom signer authorization and token caching, "
        "and adds BOLT12 offers with BOLT11 fallback for profile payments and zaps.")
    next(row for row in base["candidates"] if row["candidate_id"] == amethyst_id)["reason"] = amethyst_summary
    next(row for row in base["selected"] if row["id"] == amethyst_id)["summary"] = amethyst_summary
    protocol_id = "protocol:nip86-pr2477"
    protocol_summary = "Merged September 23, PR #2477 adds clear and list methods to NIP-86 relay management, with observable administrative effects."
    next(row for row in base["candidates"] if row["candidate_id"] == protocol_id)["reason"] = protocol_summary
    next(row for row in base["selected"] if row["id"] == protocol_id)["summary"] = protocol_summary
    merge_url = "https://github.com/nostr-protocol/nips/commit/5b9920982ae1f4061328c1b09a90360da28d13c8"
    for rows, key in ((base["candidates"], "candidate_id"), (base["selected"], "id")):
        row = next(item for item in rows if item[key] == protocol_id)
        row["primary_sources"] = list(dict.fromkeys(row["primary_sources"] + [merge_url]))
    pakstr_id = "release:pakstr-0.21.0-0.24.0"
    pakstr_candidate = next(row for row in base["candidates"] if row["candidate_id"] == pakstr_id)
    pakstr_current_sources = [url for url in pakstr_candidate["primary_sources"] if not url.endswith("/v0.21.0")]
    require(all(url in draft for url in pakstr_current_sources), "pakstr current series missing exact tag links")
    pakstr_candidate["draft_sources"] = pakstr_current_sources
    pakstr_summary = "Last week's issue covered 0.21.x packaging. New 0.22.0 adds NIP-55 signing through the bunker, 0.23.0 persists the runtime address, and 0.24.0 only adds an icon."
    pakstr_candidate["name"] = "pakstr 0.22.0–0.24.0"
    pakstr_candidate["reason"] = pakstr_summary
    pakstr_selected = next(row for row in base["selected"] if row["id"] == pakstr_id)
    pakstr_selected["name"] = pakstr_candidate["name"]
    pakstr_selected["summary"] = pakstr_summary
    for topic in ("deep-dive:nip-30", "deep-dive:nip-71"):
        selected = next(row for row in base["selected"] if row["id"] == topic)
        selected["event_example_status"] = "embedded and verified in exact assembled draft by check_newsletter_event_examples.py"
    base["source_reconciliation"]["tagged_release_projects"].append({
        "source_id": "release:white-noise-android-2026.9.21",
        "name": "White Noise Android", "verdict": "selected",
        "decision_source": str(TRIAGE) + "#white-noise-release-correction",
    })
    zapstore = load(Path(families["zapstore"]["artifact_path"]))["releases"]
    for app_id, version, name, url, reason, score in ZAPSTORE_RELEASES:
        require(url in draft, f"draft omits selected Zapstore source: {app_id}")
        release = next((item for item in zapstore
                        if item["app_id"] == app_id and item["version"] == version), None)
        require(release is not None and release["nostr_relevant"],
                f"signed Zapstore release absent: {app_id} {version}")
        if app_id == "com.xmarcade.app":
            require("epochTrusted" in release.get("release_notes", ""),
                    "XM Arcade signed notes do not support group-key epoch claim")
        if app_id == "social.cloudfodder.zzub":
            require(all(term in release.get("release_notes", "") for term in ("status columns", "assignees", "comments thread")),
                    "Zzub signed notes do not support board-detail claims")
        raw = "zapstore:" + release["release_id"]
        require(raw in included, f"release not retained by collector: {app_id}")
        cid, source_id = "zapstore:" + app_id, "editorial:zapstore:" + app_id
        source = next((item for item in base["editorial_sources"]
                       if item["source_id"] == source_id), None)
        provenance = {
            "family": "zapstore",
            "artifact_path": families["zapstore"]["artifact_path"],
            "artifact_sha256": families["zapstore"]["artifact_sha256"],
            "locator": {"app_id": app_id, "release_id": release["release_id"]},
        }
        if source is None:
            base["editorial_sources"].append({
                "source_id": source_id, "collector_source_ids": [raw],
                "artifact_provenance": provenance,
            })
            base["source_expansion"].append({"source_id": source_id, "candidate_ids": [cid]})
        else:
            source["collector_source_ids"] = [raw]
            source["artifact_provenance"] = provenance
        scores = dict(zip(base["score_axes"], [2, 2, 2, 2, 1] if score == 9
                          else [2, 2, 1, 2, 1]))
        candidate = {
            "candidate_id": cid, "name": name,
            "hard_gate": dict.fromkeys(base["hard_gate_fields"], True),
            "scores": scores, "score_total": sum(scores.values()),
            "triage": "GREEN", "final_disposition": "include", "reason": reason,
            "primary_sources": [url], "draft_sources": [url], "section": "tagged_releases",
            "triage_decision_ref": str(TRIAGE) + "#wednesday-verified-zapstore-release-delta",
        }
        old_candidate = next((item for item in base["candidates"]
                              if item["candidate_id"] == cid), None)
        if old_candidate is None:
            base["candidates"].append(candidate)
        else:
            old_candidate.clear()
            old_candidate.update(candidate)
        require(not any(item["id"] == cid for item in base["selected"]),
                f"duplicate selected candidate: {cid}")
        base["selected"].append({
            "id": cid, "name": name, "section": "tagged_releases",
            "primary_sources": [url],
            "hard_gates": {
                "direct_primary_evidence": True, "material_window_progress": True,
                "nostr_surface": True, "distinct_from_recent_coverage": True,
            },
            "score_axes": scores, "score_total": sum(scores.values()),
            "summary": reason, "continuity": "",
        })
        reconciliation = base["source_reconciliation"]["zapstore_only"]
        entry = next((item for item in reconciliation if item["source_id"] == cid), None)
        if entry is None:
            reconciliation.append({"source_id": cid, "name": name,
                                   "verdict": "selected",
                                   "decision_source": str(TRIAGE) + "#wednesday-verified-zapstore-release-delta"})
        else:
            entry.update({"name": name, "verdict": "selected",
                          "decision_source": str(TRIAGE) + "#wednesday-verified-zapstore-release-delta"})
    existing_discovery = {
        row["artifact_provenance"]["locator"].get("repository")
        for row in base["editorial_sources"]
        if row.get("artifact_provenance", {}).get("family") == "app-discovery"
    }
    discovery = load(Path(families["app-discovery"]["artifact_path"]))["candidates"]
    new_discovery = []
    selected_discovery = {name.rsplit(" ", 1)[0]: url
                          for _, _, name, url, _, _ in ZAPSTORE_RELEASES}
    for app in discovery:
        repo = app.get("repository") or ""
        if repo and repo in existing_discovery:
            continue
        if not repo and any(row.get("artifact_provenance", {}).get("locator", {}).get("name") == app["name"]
                            for row in base["editorial_sources"]):
            continue
        url = repo or app.get("website") or ""
        require(url.startswith("https://"), f"discovery lacks HTTPS evidence: {app['name']}")
        cid = "discovery:" + (repo.removeprefix("https://") if repo else app["name"].casefold().replace(" ", "-"))
        reason = (app.get("review_flags") or ["Unconfirmed discovery metadata"])[0]
        if app["name"] in selected_discovery:
            reason = (f"Discovery metadata is folded into the separately verified release "
                      f"{selected_discovery[app['name']]}; it is not a second story.")
        else:
            reason = f"{reason}; no independently verified release or material product launch in this source pass."
        source_id = "editorial:" + cid
        require(all(row["source_id"] != source_id for row in base["editorial_sources"]),
                f"duplicate discovery candidate: {cid}")
        locator = {"repository": repo, "name": app["name"]} if repo else {"name": app["name"]}
        base["editorial_sources"].append({
            "source_id": source_id, "collector_source_ids": [],
            "artifact_provenance": {
                "family": "app-discovery", "artifact_path": families["app-discovery"]["artifact_path"],
                "artifact_sha256": families["app-discovery"]["artifact_sha256"],
                "locator": locator,
            },
        })
        base["source_expansion"].append({"source_id": source_id, "candidate_ids": [cid]})
        base["candidates"].append({
            "candidate_id": cid, "name": app["name"],
            "hard_gate": {"primary_evidence": True, "in_window_progress": False,
                          "nostr_surface": bool("nostr" in (app.get("description") or "").casefold()),
                          "continuity_delta": False},
            "scores": None, "triage": "SKIP", "final_disposition": "skip",
            "reason": reason, "primary_sources": [url], "draft_sources": [],
            "triage_decision_ref": str(TRIAGE) + "#wednesday-app-discovery-delta",
        })
        new_discovery.append({"name": app["name"], "url": url, "reason": reason})
    require(len(discovery) == 83,
            f"unexpected discovery delta: {len(discovery)} total, {len(new_discovery)} new")
    require(PROJECT_DECISIONS.is_file(), "exact project-activity decisions are not final")
    base["project_activity_decisions"] = {
        "path": str(PROJECT_DECISIONS),
        "sha256": sha(PROJECT_DECISIONS),
    }
    base["schema_version"] = 1
    base["pass_id"] = manifest["pass_id"]
    base["source_pass_id"] = manifest["pass_id"]
    base["source_manifest"] = MANIFEST.name
    base["source_manifest_sha256"] = sha(MANIFEST)
    base["reporting_window"] = {
        "start": manifest["window"]["since"], "end": manifest["window"]["until"]
    }
    base["draft_sha256"] = sha(DRAFT)
    base["selected_count"] = len(base["selected"])
    base["source_reconciliation"]["app_discovery"]["count"] = len(discovery)
    base["source_reconciliation"]["app_discovery"]["decision_source"] = str(TRIAGE) + "#wednesday-app-discovery-delta"
    base["finalization_note"] = "Complete Wednesday pass with explicit release and discovery delta decisions; independent editorial review remains separate."
    require(len(base["candidates"]) == len(base["editorial_sources"]) == len(base["source_expansion"]),
            "candidate/source expansion mismatch")
    args.output.write_text(json.dumps(base, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.delta_output.write_text(json.dumps({
        "schema_version": 1, "source_pass_id": manifest["pass_id"],
        "source_manifest_sha256": sha(MANIFEST),
        "app_discovery_artifact_sha256": families["app-discovery"]["artifact_sha256"],
        "new_discovery_decisions": [{"verdict": "SKIP", **row} for row in new_discovery],
        "superseded_editorial_sources": superseded_sources,
        "superseded_raw_collector_ids": superseded_raw,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"candidates": len(base["candidates"]), "selected": base["selected_count"],
                      "new_discovery": len(new_discovery), "superseded_skip_raw": superseded_raw,
                      "superseded_sources": superseded_sources,
                      "new_discovery_decisions": new_discovery}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
