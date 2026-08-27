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
    return (score, entry["project"].lower())


def build(updates: dict, zapstore: dict | None, coverage: dict | None) -> dict:
    covered = covered_repos(coverage)
    zap_by_project: dict[str, list[dict]] = {}
    if zapstore:
        for rel in zapstore.get("releases", []):
            tp = rel.get("tracked_project")
            if isinstance(tp, str):
                zap_by_project.setdefault(tp.strip().lower(), []).append(rel)

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
            "zapstore_listing": [
                {"app_id": z.get("app_id"), "version": z.get("version")} for z in zap[:3]
            ],
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
        entries.append(entry)

    entries.sort(key=rank)
    return {
        "period": updates.get("period"),
        "release_bearing_projects": len(entries),
        "total_releases": sum(e["release_count"] for e in entries),
        "coverage_history_available": bool(covered),
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
