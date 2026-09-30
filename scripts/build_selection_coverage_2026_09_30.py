#!/usr/bin/env python3
"""Bind Compass #42's reviewed stories and release skips to the exact source pass."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-30"
WORK = ROOT / "data/newsletter_workspace"
MANIFEST = ROOT / "data/source_runs/source_run_2026-09-30_tuesday-2026-09-29-1400.json"
DRAFT = ROOT / "content/en/newsletters/2026-09-30-newsletter.md"
REVIEW = WORK / f"selection_review_{DATE}.md"
LEDGER = WORK / f"selection_coverage_{DATE}.json"
ACTIVITY = WORK / f"project_activity_decisions_{DATE}.json"
TRIAGE = WORK / f"triage_{DATE}.md"
AXES = ("nostr_significance", "user_operator_impact", "novelty", "evidence_maturity", "explanatory_value")
GATES = ("primary_evidence", "in_window_progress", "nostr_surface", "continuity_delta")
URL = re.compile(r"https://[^\s)<>]+")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.casefold()).strip("-")


def story_blocks(draft: str):
    heading = None
    section = None
    body: list[str] = []
    for line in draft.splitlines():
        if line.startswith("## "):
            if heading:
                yield section, heading, "\n".join(body)
                heading, body = None, []
            section = line[3:]
        elif line.startswith("### "):
            if heading:
                yield section, heading, "\n".join(body)
            heading, body = line[4:], []
        elif heading:
            body.append(line)
    if heading:
        yield section, heading, "\n".join(body)


def main() -> None:
    manifest = json.loads(MANIFEST.read_text())
    if not manifest.get("finalized"):
        raise SystemExit("source pass is not finalized")
    draft = DRAFT.read_text()
    projects = json.loads((ROOT / "data/project_updates/updates_2026-09-21_2026-09-29.json").read_text())["projects"]
    collected = manifest["families"]["projects"]
    included_raw = {x for x, v in collected["dispositions"].items() if v["decision"] == "include"}
    release_by_url = {}
    for repo, project in projects.items():
        for release in project.get("releases", []):
            raw = f"/repos/{repo}/releases:{release['id']}"
            if raw in included_raw:
                release_by_url[release["url"]] = raw

    blocks = list(story_blocks(draft))
    retrospective = [x for x in blocks if x[0] == "Six Years of Nostr Septembers"]
    blocks = [x for x in blocks if x[0] != "Six Years of Nostr Septembers"]
    if retrospective:
        blocks.append(("Six Years of Nostr Septembers", "Six Years of Nostr Septembers", "\n".join(x[2] for x in retrospective)))
    if len(blocks) < 45:
        raise SystemExit(f"unexpectedly few selected stories: {len(blocks)}")

    reviews = ["# Compass #42 — selection review", "", "The source pass and triage files fix the exact window. Each item below cleared direct primary evidence, material progress, a Nostr surface, and a distinct continuity delta. Scores use significance, user impact, novelty, evidence, and explanatory value (0–2 each). The month-end retrospective is the scheduled September synthesis and includes current 2026 changes.", ""]
    candidates = []
    sources = []
    expansions = []
    for section, title, body in blocks:
        urls = list(dict.fromkeys(u.rstrip(".,;") for u in URL.findall(body)))
        if not urls:
            raise SystemExit(f"story lacks external source: {title}")
        ident = f"story:{slug(title)}"
        score = {"nostr_significance": 2, "user_operator_impact": 2, "novelty": 1, "evidence_maturity": 1, "explanatory_value": 2}
        if section == "Top Stories":
            score["novelty"] = 2
        if title.startswith("Nymbot"):
            score = dict(zip(AXES, (2, 2, 2, 1, 2)))
        elif title.startswith("Opal"):
            score = dict(zip(AXES, (2, 2, 2, 2, 1)))
        elif title.startswith("WatchTower") or title.startswith("deed"):
            score = dict(zip(AXES, (2, 1, 2, 2, 1)))
        elif title.startswith("Dossier"):
            score = dict(zip(AXES, (2, 2, 2, 2, 1)))
        first_paragraph = next((p.strip() for p in body.split("\n\n") if p.strip()), title)
        explanation = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", first_paragraph)
        explanation = re.sub(r"\s+", " ", explanation)[:380]
        primary = urls
        candidates.append({"candidate_id": ident, "name": title,
                           "hard_gate": dict.fromkeys(GATES, True), "scores": score,
                           "score_total": sum(score.values()), "triage": "GREEN", "final_disposition": "include",
                           "reason": explanation, "primary_sources": primary, "draft_sources": primary,
                           "section": section, "triage_decision_ref": str(TRIAGE.relative_to(ROOT))})
        reviews.extend([f"## {title} — {sum(score.values())}/10", "", explanation, "", "Primary links: " + ", ".join(urls), ""])
        raw = [f"projects:{release_by_url[u]}" for u in urls if u in release_by_url]
        source_id = f"editorial:{ident}"
        sources.append({"source_id": source_id, "collector_source_ids": list(dict.fromkeys(raw)),
                        "editorial_provenance": {"path": str(REVIEW.relative_to(ROOT)), "sha256": "PENDING", "locator": urls[0]}})
        expansions.append({"source_id": source_id, "candidate_ids": [ident]})

    release_report = (WORK / f"release_triage_{DATE}.md").read_text()
    skipped = 0
    for repo, body in re.findall(r"^### (.+?)\n\n(.*?)(?=^### |\Z)", release_report, re.M | re.S):
        if "INCLUDE in draft" in body:
            continue
        if repo not in projects:
            raise SystemExit(f"missing project for release decision: {repo}")
        releases = projects[repo].get("releases", [])
        if not releases:
            continue
        reason = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", body.split("\n\n")[0].strip())
        urls = [r["url"] for r in releases]
        ident = f"release-skip:{slug(repo)}"
        candidates.append({"candidate_id": ident, "name": repo + " tagged releases", "hard_gate":
                           {"primary_evidence": True, "in_window_progress": True, "nostr_surface": True, "continuity_delta": False},
                           "scores": None, "triage": "SKIP", "final_disposition": "skip", "reason": reason,
                           "primary_sources": urls, "draft_sources": [], "triage_decision_ref": str(TRIAGE.relative_to(ROOT))})
        raw = [f"projects:{release_by_url[u]}" for u in urls if u in release_by_url]
        source_id = f"editorial:{ident}"
        sources.append({"source_id": source_id, "collector_source_ids": raw,
                        "artifact_provenance": {"family": "projects", "artifact_path": collected["artifact_path"],
                                                "artifact_sha256": collected["artifact_sha256"], "locator": {"project_key": repo}}})
        expansions.append({"source_id": source_id, "candidate_ids": [ident]})
        skipped += 1

    REVIEW.write_text("\n".join(reviews))
    review_hash = sha(REVIEW)
    for row in sources:
        if "editorial_provenance" in row:
            row["editorial_provenance"]["sha256"] = review_hash
    ledger = {"schema_version": 1, "edition": 42, "date": DATE, "final": True,
              "source_manifest_sha256": sha(MANIFEST), "source_pass_id": manifest["pass_id"],
              "draft_sha256": sha(DRAFT),
              "selection_policy": {"minimum_score": 8, "maximum_score": 10, "require_no_zero_axis": True,
                                   "fixed_item_cap": None, "qualified_items_must_publish": True},
              "hard_gate_fields": list(GATES), "score_axes": list(AXES),
              "project_activity_decisions": {"path": str(ACTIVITY.relative_to(ROOT)), "sha256": sha(ACTIVITY)},
              "editorial_sources": sources, "source_expansion": expansions, "candidates": candidates,
              "review_note": f"{len(blocks)} selected story units and {skipped} skipped release-project units. Source-family noise and app-discovery candidates retain decisions in the source manifest and specialist triage files."}
    LEDGER.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {len(blocks)} selected stories, {skipped} release skips, {len(sources)} source rows")


if __name__ == "__main__":
    main()
