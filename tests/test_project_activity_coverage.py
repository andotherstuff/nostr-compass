import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/project_activity_coverage.py"
SPEC = importlib.util.spec_from_file_location("project_activity_coverage", SCRIPT)
assert SPEC and SPEC.loader
coverage = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(coverage)


def pr(number, title, merged_at, repo="cameri/nostream", base_ref="main"):
    return {"number": number, "title": title, "merged_at": merged_at,
            "url": f"https://github.com/{repo}/pull/{number}", "base_ref": base_ref}


class ProjectActivityCoverageTests(unittest.TestCase):
    def fixture(self):
        updates = {
            "period": {"start": "2026-09-14", "end": "2026-09-22"},
            "projects": {
                "cameri/nostream": {"name": "nostream", "releases": [], "merged_prs": [
                    pr(741, "feat(nip66): publish relay health events", "2026-09-20T05:05:09Z"),
                    pr(783, "docs: add a badge", "2026-09-20T17:25:57Z"),
                ]},
                "example/boring": {"name": "Boring", "releases": [], "merged_prs": [
                    pr(5, "chore: bump a dependency", "2026-09-20T10:00:00Z", "example/boring"),
                ]},
                "example/released": {"name": "Released", "releases": [{"published_at": "2026-09-19T10:00:00Z"}], "merged_prs": [
                    pr(1, "feat: already in the tag", "2026-09-18T10:00:00Z", "example/released"),
                    pr(2, "fix: new after the tag", "2026-09-20T10:00:00Z", "example/released"),
                ]},
            },
        }
        activity = coverage.inventory(updates, "abc123")
        decisions = coverage.decision_template(activity)
        nostream = next(row for row in decisions["projects"] if row["repo"] == "cameri/nostream")
        nostream.update({
            "verdict": "include",
            "reason": "Signed relay health observations are a new Nostr-facing operator capability.",
            "primary_sources": [pr(741, "", "")["url"]],
            "selected_pr_urls": [pr(741, "", "")["url"]],
            "hard_gate": {name: True for name in coverage.HARD_GATES},
            "scores": {name: 2 for name in coverage.SCORE_AXES},
            "branch_checks": [{"url": pr(741, "", "")["url"], "source_url": pr(741, "", "")["url"], "base_ref": "main", "default_branch": "main"}],
        })
        for row in decisions["projects"]:
            if row["repo"] == "cameri/nostream":
                continue
            row.update({
                "verdict": "skip",
                "reason": "No separate material Nostr behavior beyond routine maintenance or an earlier tagged release.",
                "primary_sources": row["reviewed_pr_urls"][:1],
                "scores": {name: 1 for name in coverage.SCORE_AXES},
            })
        return activity, decisions

    def test_inventory_includes_pr_only_and_post_release_progress(self):
        activity, _ = self.fixture()
        self.assertEqual(activity["project_count"], 3)
        self.assertEqual(activity["pr_count"], 5)
        released = next(row for row in activity["projects"] if row["repo"] == "example/released")
        self.assertEqual([pr["number"] for pr in released["prs"]], [1, 2])
        self.assertEqual([pr["before_latest_release"] for pr in released["prs"]], [True, False])
        self.assertEqual(coverage.validate(activity, coverage.decision_template(activity)), [
            "cameri/nostream: pending or invalid editorial verdict",
            "example/boring: pending or invalid editorial verdict",
            "example/released: pending or invalid editorial verdict",
        ])

    def test_complete_decisions_include_substance_and_exclude_maintenance(self):
        activity, decisions = self.fixture()
        draft = f"nostream merged [relay health]({pr(741, '', '')['url']})."
        self.assertEqual(coverage.validate(activity, decisions, draft), [])

    def test_missing_project_blocks_even_if_other_projects_are_scored(self):
        activity, decisions = self.fixture()
        decisions["projects"] = [row for row in decisions["projects"] if row["repo"] != "cameri/nostream"]
        self.assertTrue(any("untriaged merged-PR project: cameri/nostream" in error for error in coverage.validate(activity, decisions)))

    def test_qualifying_pr_cannot_be_skipped_as_boring(self):
        activity, decisions = self.fixture()
        row = next(row for row in decisions["projects"] if row["repo"] == "cameri/nostream")
        row["verdict"] = "skip"
        row["selected_pr_urls"] = []
        self.assertTrue(any("qualifying or selected PR activity was skipped" in error for error in coverage.validate(activity, decisions)))

    def test_included_pr_must_reach_draft_and_have_default_branch_evidence(self):
        activity, decisions = self.fixture()
        self.assertTrue(any("missing from the draft" in error for error in coverage.validate(activity, decisions, "draft without source")))
        row = next(row for row in decisions["projects"] if row["repo"] == "cameri/nostream")
        row["branch_checks"][0]["base_ref"] = "feature"
        project = next(row for row in activity["projects"] if row["repo"] == "cameri/nostream")
        project["prs"][0]["base_ref"] = "feature"
        draft = pr(741, "", "")["url"]
        self.assertTrue(any("lacks default-branch integration" in error for error in coverage.validate(activity, decisions, draft)))

    def test_collector_base_branch_must_match_live_branch_check(self):
        activity, decisions = self.fixture()
        row = next(row for row in decisions["projects"] if row["repo"] == "cameri/nostream")
        row["branch_checks"][0]["base_ref"] = "feature"
        row["branch_checks"][0]["integration_url"] = "https://github.com/cameri/nostream/pull/900"
        self.assertTrue(any("branch mismatch" in error for error in coverage.validate(activity, decisions)))

    def test_skipped_maintenance_source_cannot_be_cited_as_news(self):
        activity, decisions = self.fixture()
        draft = pr(741, "", "")["url"] + " " + pr(5, "", "", "example/boring")["url"]
        self.assertTrue(any("skipped PR activity is cited" in error for error in coverage.validate(activity, decisions, draft)))

    def test_cli_template_refuses_overwrite_and_exact_source_change_fails(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            updates = root / "updates.json"
            template = root / "decisions.json"
            updates.write_text(json.dumps({"period": {}, "projects": {"example/one": {"merged_prs": [pr(1, "feat: publish", "2026-09-20", "example/one")], "releases": []}}}))
            first = subprocess.run([sys.executable, str(SCRIPT), "--updates", str(updates), "--template", str(template)], capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
            second = subprocess.run([sys.executable, str(SCRIPT), "--updates", str(updates), "--template", str(template)], capture_output=True, text=True)
            self.assertEqual(second.returncode, 2)
            decisions = json.loads(template.read_text())
            updates.write_text(updates.read_text() + "\n")
            activity = coverage.inventory(json.loads(updates.read_text()), hashlib.sha256(updates.read_bytes()).hexdigest())
            self.assertTrue(any("not bound to the exact" in error for error in coverage.validate(activity, decisions)))


if __name__ == "__main__":
    unittest.main()
