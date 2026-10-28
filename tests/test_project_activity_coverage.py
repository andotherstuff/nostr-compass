import copy
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

    def alias_fixture(self):
        activity, decisions = self.fixture()
        canonical = next(row for row in activity["projects"] if row["repo"] == "cameri/nostream")
        alias = copy.deepcopy(canonical)
        alias["repo"] = "old/alias"
        activity["projects"].append(alias)
        alias_decision = copy.deepcopy(next(row for row in decisions["projects"] if row["repo"] == "example/boring"))
        alias_decision.update(repo="old/alias", reviewed_pr_urls=[pr["url"] for pr in alias["prs"]],
                              primary_sources=[alias["prs"][0]["url"]], fold_into="cameri/nostream")
        decisions["projects"].append(alias_decision)
        return activity, decisions, pr(741, "", "")["url"]

    def test_exact_alias_fold_preserves_inventory_and_hash_binding(self):
        activity, decisions, draft = self.alias_fixture()
        before = copy.deepcopy(activity)
        self.assertEqual(coverage.validate(activity, decisions, draft), [])
        self.assertEqual(activity, before)
        decisions["updates_sha256"] = "changed"
        self.assertTrue(any("not bound to the exact" in e for e in coverage.validate(activity, decisions, draft)))

    def test_alias_fold_is_explicit_and_does_not_exempt_unselected_citation(self):
        activity, decisions, draft = self.alias_fixture()
        alias = decisions["projects"][-1]
        del alias["fold_into"]
        self.assertTrue(any("skipped PR activity is cited" in e for e in coverage.validate(activity, decisions, draft)))
        alias["fold_into"] = "cameri/nostream"
        draft += " " + pr(783, "", "")["url"]
        self.assertTrue(any("skipped PR activity is cited" in e for e in coverage.validate(activity, decisions, draft)))

    def test_alias_rejects_changed_source_missing_target_and_chains(self):
        for mutation in ["changed_record", "missing_digest", "missing_target", "chain", "noncanonical", "target_skip", "incomplete", "self_cycle"]:
            with self.subTest(mutation=mutation):
                activity, decisions, draft = self.alias_fixture()
                alias = decisions["projects"][-1]
                target = decisions["projects"][0]
                if mutation == "changed_record": activity["projects"][-1]["prs"][0]["source_record_sha256"] = "a" * 64
                if mutation == "missing_digest": del activity["projects"][-1]["prs"][0]["source_record_sha256"]
                if mutation == "incomplete": activity["projects"][-1]["prs"][0]["url"] += "-not-in-canonical"
                if mutation == "self_cycle": alias["fold_into"] = "old/alias"
                if mutation == "missing_target": alias["fold_into"] = "absent/repo"
                if mutation == "chain": target["fold_into"] = "old/alias"
                if mutation == "target_skip": target["verdict"] = "skip"
                if mutation == "noncanonical":
                    target["repo"] = "other/name"
                    activity["projects"][0]["repo"] = "other/name"
                    alias["fold_into"] = "other/name"
                self.assertTrue(any("alias fold needs exact" in e for e in coverage.validate(activity, decisions, draft)))

    def test_alias_does_not_bypass_canonical_source_and_branch_gates(self):
        for mutation in ["gate", "branch"]:
            with self.subTest(mutation=mutation):
                activity, decisions, draft = self.alias_fixture()
                canonical = decisions["projects"][0]
                if mutation == "gate": canonical["hard_gate"]["in_window_progress"] = False
                else: canonical["branch_checks"] = []
                expected = ("cameri/nostream: included progress must pass all gates" if mutation == "gate"
                            else "lacks live branch verification")
                self.assertTrue(any(expected in error for error in coverage.validate(activity, decisions, draft)))

    def test_source_digest_covers_full_record_not_only_inventory_fields(self):
        one = {"projects": {"cameri/nostream": {"merged_prs": [pr(1, "same", "2026-10-01")]}}}
        two = copy.deepcopy(one)
        two["projects"]["cameri/nostream"]["merged_prs"][0]["body"] = "different material source"
        first = coverage.inventory(one, "a")["projects"][0]["prs"][0]["source_record_sha256"]
        second = coverage.inventory(two, "b")["projects"][0]["prs"][0]["source_record_sha256"]
        self.assertNotEqual(first, second)

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
