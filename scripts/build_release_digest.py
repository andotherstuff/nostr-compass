#!/usr/bin/env python3
"""Enumerate every release and Zapstore listing in the window, by name.

WHY THIS EXISTS
---------------
Stage 2's summary reported only aggregates. `fetch_2026-08-26.md` said
"100 releases, 905 merged PRs, 146 active repos of 713 fetched" and never named
a single release. Stage 3 reads that summary, so anything not named in it is
invisible unless a human opens the raw JSON.

Nail shipped v0.1.0 on 2026-08-23, inside Newsletter #37's window. It was in
`updates_*.json` with a full changelog, it was in the Zapstore feed as
`com.formstr.mail`, and it appeared in **no** downstream artifact: not
`fetch_2026-08-26.md`, not `triage_2026-08-26.md`, not
`selection_review_2026-08-26.md`, and not the published issue. Two independent
discovery sources caught it and the aggregate summary hid both.

This digest names every release so a drop becomes a visible editorial decision
instead of an accident. It also flags the two things the old pipeline could not
see at a glance:

  * FIRST-RELEASE: the project has no earlier release in `coverage_history` or
    in this fetch's own history. A project's first tagged release is inherently
    newsworthy; Nail v0.1.0 was exactly this and was ranked no differently from
    a patch bump.
  * NEVER-COVERED: the project has never appeared in any published newsletter,
    so there is no back-reference to lean on and no reason to assume it was
    covered already.

Output is deterministic and diffable: no timestamps, sorted by rank then name.

Usage:
  python3 scripts/build_release_digest.py --updates data/project_updates/updates_A_B.json \
      [--zapstore data/zapstore_releases/zapstore_D.json] \
      [--coverage data/coverage_history.json] [--out PATH]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_json(path: Path | None):
    if path is None or not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"error: {path} is not valid JSON: {exc}", file=sys.stderr)
        raise SystemExit(1)


def normalize_repo(value: str) -> str:
    """`formstr-hq/nail`, `github.com/formstr-hq/nail` and a full URL all collapse
    to the same key.

    coverage_history.json is keyed by normalized repo URL
    (`github.com/owner/repo`), while updates_*.json is keyed by `owner/repo`.
    Comparing project *names* across the two never matches, which flagged all 40
    projects NEVER-COVERED on the first run of this script and would have made
    the flag pure noise.
    """
    v = value.strip().lower()
    v = re.sub(r"^https?://", "", v)
    v = re.sub(r"^(www\.)?", "", v)
    v = re.sub(r"^(github|gitlab|codeberg)\.com/", "", v)
    v = re.sub(r"\.git$", "", v)
    return v.strip("/")


def covered_repos(coverage: dict | None) -> dict[str, str]:
    """Map normalized repo key -> last mention date for every covered project.

    The date matters as much as the fact. A project introduced one issue ago
    that now ships a release is a follow-up story, not a debut and not old news.
    Nail is exactly that shape: introduced in #36, shipped v0.1.0 during #37's
    window, and covered in neither.
    """
    if not coverage:
        return {}
    out: dict[str, str] = {}
    projects = coverage.get("projects")
    if isinstance(projects, dict):
        for k, v in projects.items():
            if not isinstance(k, str):
                continue
            last = ""
            if isinstance(v, dict):
                last = v.get("last_mention_date") or ""
            out[normalize_repo(k)] = last if isinstance(last, str) else ""
    elif isinstance(projects, list):
        for entry in projects:
            if isinstance(entry, dict):
                last = entry.get("last_mention_date") or ""
                for field in ("repo", "repository", "url", "name", "project"):
                    v = entry.get(field)
                    if isinstance(v, str):
                        out[normalize_repo(v)] = last if isinstance(last, str) else ""
            elif isinstance(entry, str):
                out[normalize_repo(entry)] = ""
    return {k: v for k, v in out.items() if k}


def days_between(earlier: str, later: str) -> int | None:
    """Whole days between two YYYY-MM-DD strings, or None if either is unusable."""
    from datetime import date

    try:
        a = date.fromisoformat(earlier[:10])
        b = date.fromisoformat(later[:10])
    except (ValueError, TypeError):
        return None
    return (b - a).days


SEMVER = re.compile(r"^v?0+\.(0+\.)?(\d+)")

# A project mentioned this recently is still fresh in the reader's mind, so a
# release from it is a follow-up rather than a re-introduction.
FOLLOWUP_WINDOW_DAYS = 21

# Recency alone must never suppress a project. Suppression requires BOTH that it
# was covered in the previous issue AND that nothing substantive shipped since.
# Newsletter #37 dropped Nail v0.1.0 — an Android app, a key-free notifier crate
# and a Zapstore listing — on recency alone, so "substantive" is computed from
# the release notes and PR titles rather than left to a judgement call.
SUBSTANCE_PATTERNS: list[tuple[str, str]] = [
    ("new-platform", r"\b(android|ios|iphone|ipad|desktop|linux|macos|windows|web ?app|mobile)\b"),
    ("app-store-listing", r"\b(zapstore|f-?droid|play store|app ?store|testflight|apk)\b"),
    ("protocol-surface", r"\b(nip-?[0-9a-f]{1,3}|kind ?[0-9]{1,5}|bud-?[0-9]+|nap-?[a-z0-9]+|relay|gift ?wrap|npub|nsec|naddr|nevent|signer|bunker)\b"),
    ("security", r"\b(cve-|ghsa-|advisor|vulnerab|exploit|confused deputy|bypass|leak|forge[ds]?)\b"),
    ("first-release", r"^v?0+\.(0+\.)?\d+$"),
    ("new-component", r"\b(crate|library|sdk|plugin|daemon|bridge|worker|service|module|rewrite|rebuild|redesign)\b"),
    ("data-integrity", r"\b(data ?loss|corrupt|migration|backup|recover|restore|dedupl)\b"),
    # Added after NYM v3.75.543 was wrongly marked suppressible: it shipped
    # "message threads in channels, PMs, and group chats" plus post-quantum
    # encrypted PMs, and none of the patterns above matched that language.
    ("messaging-feature", r"\b(thread(s|ed|ing)?|channel|group ?chat|direct ?message|\bpms?\b|feed|notification|mention|reaction|search)\b"),
    ("encryption", r"\b(encrypt|decrypt|cipher|post-?quantum|key ?rotation|forward ?secrec)\b"),
    ("explicit-new-marker", r"(^|\n)\s*[-*#]*\s*(new|feature|added|adds)\s*[:\-]"),
]

# A bare "Full Changelog: <compare url>" carries no information a reader can
# use, so it is not evidence of substance. Anything beyond that is.
_BOILERPLATE = re.compile(
    r"(\*\*full changelog\*\*.*|## what.s changed|## new contributors|"
    r"\*\*reproducible build\*\*.*|https?://\S+)",
    re.I,
)


def documented_change_chars(releases: list[dict]) -> int:
    """Characters of release notes left after stripping boilerplate and URLs."""
    total = 0
    for r in releases:
        body = (r.get("body") or "")
        total += len(_BOILERPLATE.sub("", body).strip())
    return total


def substance_signals(releases: list[dict], pr_titles: list[str], tag: str | None) -> list[str]:
    """Concrete markers that a release shipped something worth telling readers.

    Reads the release notes and merged-PR titles the fetch already captured. A
    hit is a reason to look, never a claim for prose: Triage still has to open
    the release and verify what changed.
    """
    haystack = " ".join(
        [r.get("body") or "" for r in releases] + list(pr_titles)
    ).lower()
    found: list[str] = []
    for label, pattern in SUBSTANCE_PATTERNS:
        if label == "first-release":
            if tag and re.match(pattern, tag.strip(), re.I):
                found.append(label)
            continue
        if re.search(pattern, haystack, re.I):
            found.append(label)
    if documented_change_chars(releases) >= 120:
        found.append("documented-changes")
    return found


def looks_like_first_release(tag: str | None, release_count_in_window: int) -> bool:
    """A 0.0.x / 0.1.0 / v1.0 tag with no prior coverage reads as a debut.

    Deliberately conservative: this only *raises* a release for review. It is a
    ranking hint, never a claim in prose, and Triage still has to verify the
    project's release history before calling anything a first release.
    """
    if not tag:
        return False
    return bool(SEMVER.match(tag.strip())) and release_count_in_window <= 2


def rank(entry: dict) -> tuple[int, str]:
    """Lower sorts first. Debuts and never-covered projects lead."""
    score = 50
    if entry["never_covered"]:
        score -= 20
    if entry["possible_first_release"]:
        score -= 15
    if entry["release_count"] >= 3:
        score -= 5
    if entry["zapstore_listing"]:
        score -= 5
    if entry["recent_followup"]:
        score -= 25
    if entry["substance_signals"]:
        score -= 10 * min(len(entry["substance_signals"]), 3)
    if entry["suppression_allowed"]:
        score += 40
    return (score, entry["project"].lower())


def zapstore_apps(zapstore: dict | None) -> list[dict]:
    """Per-app view of the Zapstore feed.

    Prefers the `apps` rollup the fetcher emits; falls back to computing it from
    `releases` so older artifacts still work. Per-release counts are unusable for
    review: #37 reported 622 Nostr-relevant releases, of which 476 were
    PosterChan CI builds and 60 were Boris. The real figure was 48 apps.
    """
    if not zapstore:
        return []
    apps = zapstore.get("apps")
    if isinstance(apps, list) and apps:
        return apps
    grouped: dict[str, list[dict]] = {}
    for rel in zapstore.get("releases", []):
        if rel.get("nostr_relevant") and rel.get("app_id"):
            grouped.setdefault(rel["app_id"], []).append(rel)
    out = []
    for app_id, rows in grouped.items():
        # release_created_at, not published_at: published_at is null on every
        # Zapstore row, so sorting on it yields arbitrary "latest" versions.
        rows.sort(key=lambda r: r.get("release_created_at") or 0)
        tracked = next((r.get("tracked_project") for r in rows if r.get("tracked_project")), None)
        out.append(
            {
                "app_id": app_id,
                "app_name": rows[0].get("app_name"),
                "tracked_project": tracked,
                "release_count": len(rows),
                "latest_version": rows[-1].get("version"),
                "latest_at": rows[-1].get("release_created_at_iso"),
                "new_app": any(r.get("new_app") for r in rows),
                "baseline_suppressed": all(r.get("first_run") for r in rows),
            }
        )
    out.sort(key=lambda a: (0 if a.get("tracked_project") else 1, -a.get("release_count", 0)))
    return out


def build(updates: dict, zapstore: dict | None, coverage: dict | None) -> dict:
    covered = covered_repos(coverage)
    apps = zapstore_apps(zapstore)
    zap_by_project: dict[str, list[dict]] = {}
    for app in apps:
        tp = app.get("tracked_project")
        if isinstance(tp, str):
            zap_by_project.setdefault(tp.strip().lower(), []).append(
                {"app_id": app.get("app_id"), "version": app.get("latest_version")}
            )

    entries: list[dict] = []
    for repo_key, proj in (updates.get("projects") or {}).items():
        if not isinstance(proj, dict):
            continue
        releases = proj.get("releases") or []
        if not releases:
            continue
        name = proj.get("name") or repo_key
        zap = zap_by_project.get(str(name).strip().lower(), [])
        rels = []
        for r in releases:
            rels.append(
                {
                    "tag": r.get("tag") or r.get("tag_name") or r.get("name") or "(untagged)",
                    "published_at": (r.get("published_at") or "")[:10],
                    "url": r.get("url") or "",
                    "body_chars": len(r.get("body") or ""),
                }
            )
        rels.sort(key=lambda x: x["published_at"])
        pr_titles = [
            p.get("title") or "" for p in (proj.get("merged_prs") or []) if isinstance(p, dict)
        ]
        signals = substance_signals(releases, pr_titles, rels[0]["tag"])
        entry = {
            "project": str(name),
            "repo": repo_key,
            "category": proj.get("category"),
            "priority": proj.get("priority"),
            "release_count": len(rels),
            "releases": rels,
            "merged_prs": len(proj.get("merged_prs") or []),
            "never_covered": normalize_repo(repo_key) not in covered if covered else False,
            "last_covered": covered.get(normalize_repo(repo_key)) or None,
            "recent_followup": False,  # filled in below, needs the window end date
            "possible_first_release": looks_like_first_release(rels[0]["tag"], len(rels)),
            "substance_signals": signals,
            # True only when the project is recently covered AND nothing
            # substantive shipped. Anything else must be written up.
            "suppression_allowed": False,
            "zapstore_listing": zap[:3],
        }
        # A project covered within FOLLOWUP_WINDOW_DAYS that now ships a release
        # is the highest-value miss: the reader already met it, and the release
        # is the payoff. Nail was introduced in #36 and its v0.1.0 went unwritten.
        last = entry["last_covered"]
        newest_release = entry["releases"][-1]["published_at"]
        if last and newest_release:
            gap = days_between(last, newest_release)
            if gap is not None and 0 <= gap <= FOLLOWUP_WINDOW_DAYS:
                entry["recent_followup"] = True
        entry["suppression_allowed"] = bool(entry["recent_followup"]) and not signals
        entries.append(entry)

    entries.sort(key=rank)
    # A tracked project can ship on Zapstore without cutting a GitHub release.
    # Six did inside #37's window (Imwald 0.4.0, Nostria 4.1.72, Flotilla 1.9.1,
    # Deepmarks 2.2.13, Surveil 0.1.8, Treasures 2.10.1) and a GitHub-only sweep
    # could not see any of them.
    named = {e["project"].strip().lower() for e in entries}
    zapstore_only = [
        a for a in apps if (a.get("tracked_project") or "").strip().lower() not in named
    ]
    zapstore_only.sort(key=lambda a: (0 if a.get("tracked_project") else 1, a.get("app_id") or ""))

    return {
        "period": updates.get("period"),
        "release_bearing_projects": len(entries),
        "total_releases": sum(e["release_count"] for e in entries),
        "coverage_history_available": bool(covered),
        "zapstore_apps": len(apps),
        "zapstore_only": zapstore_only,
        "projects": entries,
    }


def render_markdown(digest: dict) -> str:
    out: list[str] = []
    p = digest.get("period") or {}
    window = f"{p.get('start','?')} → {p.get('end','?')}" if isinstance(p, dict) else str(p)
    out.append("# Release digest — every tagged release in the window")
    out.append("")
    out.append(
        f"Window {window}. {digest['total_releases']} releases across "
        f"{digest['release_bearing_projects']} projects."
    )
    if not digest["coverage_history_available"]:
        out.append("")
        out.append(
            "**No coverage history available**, so never-covered flags are absent from this run. "
            "Rebuild it with `python3 scripts/build_coverage_history.py` and regenerate."
        )
    out.append("")
    out.append(
        "Triage MUST record a decision for every project below. A release that is "
        "neither written up nor given a skip reason is a pipeline defect, not an "
        "editorial choice: that is how Nail v0.1.0 was lost from Newsletter #37."
    )
    out.append("")
    for e in digest["projects"]:
        flags = []
        if e["never_covered"]:
            flags.append("**NEVER-COVERED**")
        if e["possible_first_release"]:
            flags.append("**POSSIBLE-FIRST-RELEASE**")
        if e["recent_followup"]:
            flags.append(f"**FOLLOW-UP** (last covered {e['last_covered']})")
        if e["substance_signals"]:
            flags.append("substance: " + ", ".join(e["substance_signals"]))
        if e["suppression_allowed"]:
            flags.append("_recently covered, no substance markers — a skip is defensible_")
        if e["zapstore_listing"]:
            ids = ", ".join(
                f"`{z['app_id']}`" + (f" v{z['version']}" if z.get("version") else "")
                for z in e["zapstore_listing"]
                if z.get("app_id")
            )
            if ids:
                flags.append(f"Zapstore: {ids}")
        head = f"- **{e['project']}** (`{e['repo']}`)"
        if flags:
            head += " — " + " · ".join(flags)
        out.append(head)
        for r in e["releases"]:
            line = f"  - `{r['tag']}` {r['published_at']}"
            if r["url"]:
                line += f" — {r['url']}"
            if r["body_chars"] == 0:
                line += " (empty release notes; audit the commit range instead)"
            out.append(line)
        if e["merged_prs"]:
            out.append(f"  - {e['merged_prs']} merged PRs in window")
        out.append("  - Triage decision: __________ (write up / skip + reason)")

    zo = digest.get("zapstore_only") or []
    shown = [a for a in zo if a.get("tracked_project") or a.get("new_app")]
    if shown:
        tracked_n = sum(1 for a in shown if a.get("tracked_project"))
        out.append("")
        out.append("## Zapstore releases with no GitHub release in window")
        out.append("")
        out.append(
            f"{len(shown)} of {digest.get('zapstore_apps', 0)} Zapstore apps shipped without a "
            f"matching GitHub release, {tracked_n} of them tracked projects. A GitHub-only sweep "
            "cannot see these."
        )
        out.append("")
        for a in shown:
            label = a.get("app_name") or a.get("app_id")
            line = f"- **{label}** `{a.get('app_id')}` {a.get('latest_version') or '?'}"
            if a.get("latest_at"):
                line += f" ({str(a['latest_at'])[:10]})"
            if a.get("tracked_project"):
                line += f" — tracked: {a['tracked_project']}"
            if a.get("new_app"):
                line += " — **NEW-APP**"
            if a.get("baseline_suppressed"):
                line += " — unclassified (baseline suppressed this run)"
            out.append(line)
            out.append("  - Triage decision: __________ (write up / skip + reason)")
    out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--updates", type=Path, required=True)
    ap.add_argument("--zapstore", type=Path)
    ap.add_argument("--coverage", type=Path, default=PROJECT_ROOT / "data/coverage_history.json")
    ap.add_argument("--out", type=Path)
    ap.add_argument("--json-out", type=Path)
    args = ap.parse_args()

    updates = load_json(args.updates)
    if updates is None:
        print(f"error: --updates {args.updates} not found", file=sys.stderr)
        return 1

    digest = build(updates, load_json(args.zapstore), load_json(args.coverage))
    md = render_markdown(digest)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(md, encoding="utf-8")
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        print(md)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(digest, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {args.json_out}", file=sys.stderr)

    print(
        f"release digest: {digest['total_releases']} releases / "
        f"{digest['release_bearing_projects']} projects",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
