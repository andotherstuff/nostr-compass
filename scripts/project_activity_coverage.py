#!/usr/bin/env python3
"""Inventory all merged-PR progress and require explicit editorial decisions.

The release digest cannot see projects that merge useful work without tagging a
release. This gate inventories every tracked project with merged PRs, including
PRs that may be folded into a release story. A project is never
discarded because its PR count is small. The generated template is deliberately
pending: title heuristics may order review but must not make editorial decisions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

HARD_GATES = ("primary_evidence", "in_window_progress", "nostr_surface", "continuity_delta")
SCORE_AXES = ("nostr_significance", "user_operator_impact", "novelty", "evidence_maturity", "explanatory_value")
MATERIAL_HINT = re.compile(
    r"\b(feat|feature|fix|security|privacy|relay|signer|nip[- ]?[0-9a-z]+|"
    r"blossom|gift.?wrap|auth|stream|publish|identity|moderation|message|"
    r"upload|download|search|sync|backup|restore|payment|wallet)\b", re.I
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def inventory(updates: dict[str, Any], updates_sha256: str) -> dict[str, Any]:
    projects = updates.get("projects")
    if not isinstance(projects, dict):
        raise ValueError("project updates lack a projects object")
    rows = []
    for repo, project in sorted(projects.items(), key=lambda item: item[0].lower()):
        if not isinstance(project, dict):
            continue
        releases = [item for item in project.get("releases", []) if isinstance(item, dict)]
        newest_release = max((str(item.get("published_at") or "") for item in releases), default="")
        prs = []
        seen = set()
        for pr in project.get("merged_prs", []):
            if not isinstance(pr, dict):
                continue
            url = pr.get("url")
            merged_at = pr.get("merged_at")
            number = pr.get("number")
            if not isinstance(url, str) or not url.startswith("https://") or not isinstance(merged_at, str) or not isinstance(number, int):
                raise ValueError(f"{repo} has a merged PR without a stable URL, number, or merge time")
            if url in seen:
                raise ValueError(f"{repo} repeats merged PR {url}")
            seen.add(url)
            title = str(pr.get("title") or "")
            prs.append({
                "number": number,
                "title": title,
                "url": url,
                "merged_at": merged_at,
                "base_ref": pr.get("base_ref"),
                "before_latest_release": bool(newest_release and merged_at <= newest_release),
                "material_hint": bool(MATERIAL_HINT.search(title)),
            })
        if not prs:
            continue
        prs.sort(key=lambda item: (item["merged_at"], item["number"], item["url"]))
        rows.append({
            "repo": repo,
            "name": project.get("name") or repo,
            "newest_release_at": newest_release or None,
            "pr_count": len(prs),
            "material_hint_count": sum(pr["material_hint"] for pr in prs),
            "prs": prs,
        })
    return {
        "schema_version": 1,
        "updates_sha256": updates_sha256,
        "period": updates.get("period"),
        "project_count": len(rows),
        "pr_count": sum(row["pr_count"] for row in rows),
        "projects": rows,
    }


def decision_template(activity: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "updates_sha256": activity["updates_sha256"],
        "projects": [
            {
                "repo": row["repo"],
                "reviewed_pr_urls": [pr["url"] for pr in row["prs"]],
                "verdict": "pending",
                "reason": "",
                "primary_sources": [],
                "selected_pr_urls": [],
                "hard_gate": {name: False for name in HARD_GATES},
                "scores": {name: 0 for name in SCORE_AXES},
                "branch_checks": [],
            }
            for row in activity["projects"]
        ],
    }


def validate(
    activity: dict[str, Any], decisions: dict[str, Any], draft: str | None = None
) -> list[str]:
    errors: list[str] = []
    if activity.get("schema_version") != 1 or decisions.get("schema_version") != 1:
        errors.append("activity inventory and decisions must use schema version 1")
    if decisions.get("updates_sha256") != activity.get("updates_sha256"):
        errors.append("activity decisions are not bound to the exact project updates")
    rows = activity.get("projects")
    decision_rows = decisions.get("projects")
    if not isinstance(rows, list) or not isinstance(decision_rows, list):
        return errors + ["activity inventory and decisions need projects arrays"]
    expected = {row["repo"]: row for row in rows if isinstance(row, dict) and isinstance(row.get("repo"), str)}
    actual: dict[str, dict[str, Any]] = {}
    for row in decision_rows:
        if not isinstance(row, dict) or not isinstance(row.get("repo"), str):
            errors.append("activity decision lacks a repository key")
            continue
        repo = row["repo"]
        if repo in actual:
            errors.append(f"duplicate activity decision for {repo}")
        actual[repo] = row
    for repo in sorted(set(expected) - set(actual)):
        errors.append(f"untriaged merged-PR project: {repo}")
    for repo in sorted(set(actual) - set(expected)):
        errors.append(f"activity decision has no source project: {repo}")
    for repo in sorted(set(actual) & set(expected)):
        row, decision = expected[repo], actual[repo]
        urls = {pr["url"] for pr in row["prs"]}
        reviewed = decision.get("reviewed_pr_urls")
        if not isinstance(reviewed, list) or any(not isinstance(url, str) for url in reviewed) or len(reviewed) != len(set(reviewed)) or set(reviewed) != urls:
            errors.append(f"{repo}: reviewed PR URLs do not cover the complete merged-PR activity")
        verdict = decision.get("verdict")
        if verdict not in {"include", "skip"}:
            errors.append(f"{repo}: pending or invalid editorial verdict")
            continue
        reason = decision.get("reason")
        if not isinstance(reason, str) or len(reason.strip()) < 25:
            errors.append(f"{repo}: verdict needs a concrete reason of at least 25 characters")
        primary = decision.get("primary_sources")
        if not isinstance(primary, list) or not primary or any(not isinstance(url, str) for url in primary) or not set(primary).issubset(urls):
            errors.append(f"{repo}: verdict needs direct PR evidence from this activity")
        gates = decision.get("hard_gate")
        scores = decision.get("scores")
        if not isinstance(gates, dict) or set(gates) != set(HARD_GATES) or any(type(gates[key]) is not bool for key in HARD_GATES):
            errors.append(f"{repo}: malformed hard-gate verdict")
            continue
        if not isinstance(scores, dict) or set(scores) != set(SCORE_AXES) or any(type(scores[key]) is not int or not 0 <= scores[key] <= 2 for key in SCORE_AXES):
            errors.append(f"{repo}: malformed quality scores")
            continue
        qualified = all(gates.values()) and sum(scores.values()) >= 8 and all(scores.values())
        selected = decision.get("selected_pr_urls")
        if not isinstance(selected, list) or any(not isinstance(url, str) for url in selected) or len(selected) != len(set(selected)) or not set(selected).issubset(urls):
            errors.append(f"{repo}: selected PR URLs are malformed or absent from this activity")
            continue
        if verdict == "include":
            if not qualified or not selected or not set(selected).issubset(set(primary)):
                errors.append(f"{repo}: included progress must pass all gates and 8/10 with selected primary sources")
            checks = decision.get("branch_checks")
            checked = {item.get("url"): item for item in checks if isinstance(item, dict)} if isinstance(checks, list) else {}
            for url in selected:
                branch = checked.get(url, {})
                if not branch.get("default_branch") or not branch.get("base_ref") or branch.get("source_url") != url:
                    errors.append(f"{repo}: selected PR {url} lacks live branch verification")
                elif next((pr.get("base_ref") for pr in row["prs"] if pr["url"] == url), None) not in (None, branch["base_ref"]):
                    errors.append(f"{repo}: selected PR {url} has a branch mismatch with the project collector")
                elif branch["base_ref"] != branch["default_branch"] and not str(branch.get("integration_url") or "").startswith("https://"):
                    errors.append(f"{repo}: feature-branch PR {url} lacks default-branch integration evidence")
                if draft is not None and url not in draft:
                    errors.append(f"{repo}: selected PR {url} is missing from the draft")
        else:
            if qualified or selected:
                errors.append(f"{repo}: qualifying or selected PR activity was skipped")
            if draft is not None and any(url in draft for url in urls):
                errors.append(f"{repo}: skipped PR activity is cited in the draft")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--updates", type=Path, required=True)
    parser.add_argument("--digest", type=Path)
    parser.add_argument("--template", type=Path)
    parser.add_argument("--decisions", type=Path)
    parser.add_argument("--draft", type=Path)
    args = parser.parse_args()
    try:
        activity = inventory(read_object(args.updates), sha256(args.updates))
        if args.digest:
            args.digest.parent.mkdir(parents=True, exist_ok=True)
            args.digest.write_text(json.dumps(activity, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        if args.template:
            if args.template.exists():
                raise ValueError(f"refusing to overwrite existing decisions: {args.template}")
            args.template.parent.mkdir(parents=True, exist_ok=True)
            args.template.write_text(json.dumps(decision_template(activity), indent=2, sort_keys=True) + "\n", encoding="utf-8")
        if args.decisions:
            errors = validate(activity, read_object(args.decisions), args.draft.read_text(encoding="utf-8") if args.draft else None)
            if errors:
                for error in errors:
                    print(f"FAIL: {error}")
                return 1
            print(f"PASS: {activity['project_count']} merged-PR projects and {activity['pr_count']} PRs have exact editorial decisions")
        else:
            print(f"Activity inventory: {activity['project_count']} projects, {activity['pr_count']} merged PRs requiring review")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
