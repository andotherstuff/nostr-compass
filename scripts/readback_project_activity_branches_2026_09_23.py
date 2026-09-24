#!/usr/bin/env python3
"""Live authenticated branch readback for selected Compass #41 merged PRs."""
from __future__ import annotations

import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from finalize_project_activity_2026_09_23 import DRAFT, INCLUDE, ROOT, WORK

GH = "/opt/data/.local/bin/gh"
INVENTORY = WORK / "project_activity_inventory_2026-09-23.json"
OUTPUT = WORK / "project_activity_branch_checks_2026-09-23.json"


def api(path: str) -> dict:
    env = {**os.environ, "HERMES_GH_NO_CACHE": "1"}
    result = subprocess.run([GH, "api", path], text=True, capture_output=True, env=env, check=False)
    if result.returncode:
        raise RuntimeError(f"authenticated GitHub read failed for {path}: {result.stderr.strip()[:300]}")
    obj = json.loads(result.stdout)
    if not isinstance(obj, dict):
        raise ValueError(f"GitHub returned a non-object for {path}")
    return obj


def main() -> None:
    inventory = json.loads(INVENTORY.read_text())
    draft = DRAFT.read_text()
    rows = {row["repo"]: row for row in inventory["projects"]}
    if not set(INCLUDE).issubset(rows):
        raise ValueError("included project is absent from the exact inventory")
    result: dict[str, dict] = {}
    for repo in sorted(INCLUDE):
        urls = [pr["url"] for pr in rows[repo]["prs"] if pr["url"] in draft]
        if not urls:
            raise ValueError(f"{repo}: no selected PR in the assembled draft")
        url_repos = {"/".join(urlparse(url).path.strip("/").split("/")[:2]) for url in urls}
        if len(url_repos) != 1:
            raise ValueError(f"{repo}: selected URLs span multiple actual repositories")
        remote_repo = next(iter(url_repos))
        repo_api = api(f"/repos/{remote_repo}")
        default_branch = repo_api.get("default_branch")
        if not isinstance(default_branch, str) or not default_branch:
            raise ValueError(f"{repo}: no live default branch")
        for url in urls:
            path = urlparse(url).path.strip("/").split("/")
            if len(path) != 4 or path[2] != "pull" or f"{path[0]}/{path[1]}".casefold() != remote_repo.casefold():
                raise ValueError(f"invalid selected PR URL: {url}")
            live = api(f"/repos/{remote_repo}/pulls/{path[3]}")
            if live.get("html_url") != url or live.get("state") != "closed" or not live.get("merged_at"):
                raise ValueError(f"{url}: PR is not authoritatively merged at the selected URL")
            base = live.get("base") or {}
            base_ref = base.get("ref")
            base_repo = (base.get("repo") or {}).get("full_name")
            if not base_ref or str(base_repo).casefold() != remote_repo.casefold():
                raise ValueError(f"{url}: PR base repository/ref mismatch")
            item = {
                "url": url, "source_url": url,
                "default_branch": default_branch, "base_ref": base_ref,
                "merged_at": live["merged_at"], "merge_commit_sha": live.get("merge_commit_sha"),
                "checked_at": datetime.now(timezone.utc).isoformat(),
            }
            if base_ref != default_branch:
                raise ValueError(f"{url}: feature branch requires separate live integration proof")
            result[url] = item
        print(f"verified {repo}: {len(urls)} merged PRs on {default_branch}", flush=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {len(result)} exact live PR branch checks written to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
