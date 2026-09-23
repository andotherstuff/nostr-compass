import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("selection_gate", ROOT / "scripts/check_selection_coverage.py")
assert SPEC and SPEC.loader
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class SelectionCoverageTests(unittest.TestCase):
    def fixture(self):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        manifest_path, ledger_path, draft_path = root / "manifest.json", root / "ledger.json", root / "draft.md"
        updates_path, activity_path = root / "updates.json", root / "activity.json"
        updates_path.write_text(json.dumps({"period": {"start": "2026-09-14", "end": "2026-09-22"}, "projects": {}}))
        activity_path.write_text(json.dumps({"schema_version": 1, "updates_sha256": digest(updates_path), "projects": []}))
        families = {
            family: {"status": "empty_verified", "candidate_ids": [], "dispositions": {}}
            for family in gate.SOURCE_FAMILIES
        }
        families["projects"] = {"status": "complete", "artifact_path": str(updates_path), "artifact_sha256": digest(updates_path), "candidate_ids": ["repo:a", "repo:noise"], "dispositions": {"repo:a": {"decision": "include", "reason": "active exact-window project"}, "repo:noise": {"decision": "skip", "reason": "outside source window"}}}
        families["nostr-recap"] = {"status": "complete", "candidate_ids": ["event:1"], "dispositions": {"event:1": {"decision": "include", "reason": "signed roundup event"}}}
        manifest = {
            "schema_version": 2,
            "pass_id": "pass-001",
            "finalized": True,
            "expected_families": list(gate.SOURCE_FAMILIES),
            "families": families,
        }
        manifest_path.write_text(json.dumps(manifest))
        draft_path.write_text("[Alpha](https://example.com/alpha) is useful.\n[Beta](https://example.com/beta) is useful.\n")
        candidate = lambda candidate_id, name, url: {
            "candidate_id": candidate_id,
            "name": name,
            "hard_gate": {field: True for field in gate.HARD_GATES},
            "scores": {axis: 2 for axis in gate.SCORE_AXES},
            "triage": "GREEN",
            "final_disposition": "include",
            "reason": "Material shipped Nostr behavior with direct primary evidence.",
            "primary_sources": [url],
            "draft_sources": [url],
        }
        ledger = {
            "schema_version": 1,
            "source_pass_id": "pass-001",
            "source_manifest_sha256": digest(manifest_path),
            "draft_sha256": digest(draft_path),
            "selection_policy": {"minimum_score": 8, "maximum_score": 10, "require_no_zero_axis": True, "fixed_item_cap": None, "qualified_items_must_publish": True},
            "hard_gate_fields": list(gate.HARD_GATES),
            "score_axes": list(gate.SCORE_AXES),

            "project_activity_decisions": {"path": str(activity_path), "sha256": digest(activity_path)},

            "editorial_sources": [
                {"source_id": "projects:repo:a", "collector_source_ids": ["projects:repo:a"]},
                {"source_id": "nostr-recap:event:1", "collector_source_ids": ["nostr-recap:event:1"]},
            ],

            "source_expansion": [
                {"source_id": "projects:repo:a", "candidate_ids": ["project:alpha"]},
                {"source_id": "nostr-recap:event:1", "candidate_ids": ["project:alpha", "project:beta"]},
            ],
            "candidates": [candidate("project:alpha", "Alpha", "https://example.com/alpha"), candidate("project:beta", "Beta", "https://example.com/beta")],
            "final": True,
        }
        ledger_path.write_text(json.dumps(ledger))
        return temp, manifest_path, ledger_path, draft_path, ledger

    def test_complete_aggregate_expansion_passes(self):
        temp, manifest, ledger, draft, _ = self.fixture()
        self.addCleanup(temp.cleanup)
        errors, receipt = gate.validate(manifest, ledger, draft)
        self.assertEqual(errors, [])
        self.assertEqual(receipt["qualified_candidate_count"], 2)

    def test_receipt_stdout_returns_the_complete_receipt_without_writing(self):
        temp, manifest, ledger, draft, _ = self.fixture()
        self.addCleanup(temp.cleanup)
        before = sorted(path.name for path in manifest.parent.iterdir())
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts/check_selection_coverage.py"),
                "--manifest", str(manifest),
                "--ledger", str(ledger),
                "--draft", str(draft),
                "--receipt-stdout",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["verdict"], "PASS")
        self.assertEqual(sorted(path.name for path in manifest.parent.iterdir()), before)

    def test_raw_collector_include_does_not_become_editorial_candidate(self):
        temp, manifest_path, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        manifest = json.loads(manifest_path.read_text())
        manifest["families"]["projects"]["candidate_ids"].append("repo:raw-evaluated")
        manifest["families"]["projects"]["dispositions"]["repo:raw-evaluated"] = {
            "decision": "include", "reason": "record evaluated by collector"
        }
        manifest_path.write_text(json.dumps(manifest))
        ledger["source_manifest_sha256"] = digest(manifest_path)
        ledger["editorial_sources"] = [
            {"source_id": "projects:repo:a", "collector_source_ids": ["projects:repo:a"]},
            {"source_id": "nostr-recap:event:1", "collector_source_ids": ["nostr-recap:event:1"]},
        ]
        ledger_path.write_text(json.dumps(ledger))
        errors, receipt = gate.validate(manifest_path, ledger_path, draft)
        self.assertEqual(errors, [])
        self.assertEqual(receipt["retained_source_candidate_count"], 2)

    def test_normalized_source_cannot_cite_unknown_collector_record(self):
        temp, manifest_path, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        ledger["editorial_sources"] = [
            {"source_id": "projects:repo:a", "collector_source_ids": ["projects:missing"]},
            {"source_id": "nostr-recap:event:1", "collector_source_ids": ["nostr-recap:event:1"]},
        ]
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest_path, ledger_path, draft)
        self.assertTrue(any("unknown collector record" in error for error in errors))

    def test_artifact_locator_is_bound_to_manifest_digest(self):
        temp, manifest_path, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        artifact = Path(temp.name) / "source.json"
        artifact.write_text(json.dumps({"period": {"start": "2026-09-14", "end": "2026-09-22"},
                                        "projects": {}, "repository": "https://example.com/alpha"}))
        activity_path = Path(ledger["project_activity_decisions"]["path"])
        activity_path.write_text(json.dumps({"schema_version": 1, "updates_sha256": digest(artifact), "projects": []}))
        ledger["project_activity_decisions"]["sha256"] = digest(activity_path)
        manifest = json.loads(manifest_path.read_text())
        manifest["families"]["projects"]["artifact_path"] = str(artifact)
        manifest["families"]["projects"]["artifact_sha256"] = digest(artifact)
        manifest_path.write_text(json.dumps(manifest))
        ledger["source_manifest_sha256"] = digest(manifest_path)
        ledger["editorial_sources"][0] = {
            "source_id": "projects:repo:a", "collector_source_ids": [],
            "artifact_provenance": {"family": "projects", "artifact_path": str(artifact),
                                    "artifact_sha256": digest(artifact),
                                    "locator": {"repository": "https://example.com/missing"}},
        }
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest_path, ledger_path, draft)
        self.assertTrue(any("artifact locator" in error for error in errors))
        ledger["editorial_sources"][0]["artifact_provenance"]["locator"]["repository"] = "https://example.com/alpha"
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest_path, ledger_path, draft)
        self.assertEqual(errors, [])

    def test_documented_editorial_override_has_exact_primary_url_and_hash(self):
        temp, manifest_path, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        doc = Path(temp.name) / "selection_review.md"
        doc.write_text("Source considered: https://example.com/alpha")
        ledger["editorial_sources"][0] = {
            "source_id": "projects:repo:a", "collector_source_ids": [],
            "editorial_provenance": {"path": str(doc), "sha256": digest(doc),
                                     "locator": "https://example.com/alpha"},
        }
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest_path, ledger_path, draft)
        self.assertEqual(errors, [])
        doc.write_text("Source considered: another URL")
        errors, _ = gate.validate(manifest_path, ledger_path, draft)
        self.assertTrue(any("editorial provenance" in error for error in errors))

    def test_empty_normalized_universe_cannot_silently_discard_collector_data(self):
        temp, manifest_path, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        ledger["editorial_sources"] = []
        ledger["source_expansion"] = []
        ledger["candidates"] = []
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest_path, ledger_path, draft)
        self.assertTrue(any("empty editorial" in error for error in errors))

    def test_rejected_at_hard_gate_does_not_need_fabricated_quality_scores(self):
        temp, manifest_path, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        rejected = next(c for c in ledger["candidates"] if c["candidate_id"] == "project:beta")
        rejected["hard_gate"]["in_window_progress"] = False
        rejected["triage"] = "SKIP"
        rejected["final_disposition"] = "skip"
        rejected["draft_sources"] = []
        rejected["scores"] = None
        ledger_path.write_text(json.dumps(ledger))
        errors, receipt = gate.validate(manifest_path, ledger_path, draft)
        self.assertEqual(errors, [])
        self.assertEqual(receipt["skipped_candidate_count"], 1)

    def test_hard_gate_skip_without_primary_url_keeps_artifact_provenance(self):
        temp, manifest_path, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        rejected = next(c for c in ledger["candidates"] if c["candidate_id"] == "project:beta")
        rejected["hard_gate"]["in_window_progress"] = False
        rejected["triage"] = "SKIP"
        rejected["final_disposition"] = "skip"
        rejected["scores"] = None
        rejected["draft_sources"] = []
        rejected["primary_sources"] = []
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest_path, ledger_path, draft)
        self.assertEqual(errors, [])

    def test_owner_queued_catch_up_requires_exact_explicit_exception(self):
        temp, manifest_path, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        included = ledger["candidates"][0]
        included["candidate_id"] = "top:fips-initramfs-0.1.0"
        ledger["source_expansion"][0]["candidate_ids"] = ["top:fips-initramfs-0.1.0"]
        ledger["source_expansion"][1]["candidate_ids"][0] = "top:fips-initramfs-0.1.0"
        override_doc = Path(temp.name) / "human_overrides.md"
        override_doc.write_text("User queued catch-up: " + included["primary_sources"][0])
        included["owner_override_evidence"] = {"path": str(override_doc), "sha256": digest(override_doc)}
        included["hard_gate"]["in_window_progress"] = False
        included["override"] = "owner_queued_catch_up"
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest_path, ledger_path, draft)
        self.assertEqual(errors, [])
        included["override"] = "made_up_override"
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest_path, ledger_path, draft)
        self.assertTrue(any("hard gate" in x or "sub-threshold" in x for x in errors))

    def test_skip_records_unassessed_hard_gates_as_null(self):
        temp, manifest_path, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        rejected = next(c for c in ledger["candidates"] if c["candidate_id"] == "project:beta")
        rejected["hard_gate"] = dict.fromkeys(gate.HARD_GATES)
        rejected["hard_gate"]["in_window_progress"] = False
        rejected["triage"] = "SKIP"
        rejected["final_disposition"] = "skip"
        rejected["scores"] = None
        rejected["draft_sources"] = []
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest_path, ledger_path, draft)
        self.assertEqual(errors, [])

    def test_missing_retained_source_fails(self):
        temp, manifest, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        ledger["source_expansion"].pop()
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest, ledger_path, draft)
        self.assertTrue(any("missing from triage" in error for error in errors))

    def test_missing_maintained_family_fails_even_when_manifest_redefines_expected(self):
        temp, manifest_path, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        manifest = json.loads(manifest_path.read_text())
        manifest["expected_families"].remove("specs")
        del manifest["families"]["specs"]
        manifest_path.write_text(json.dumps(manifest))
        ledger["source_manifest_sha256"] = digest(manifest_path)
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest_path, ledger_path, draft)
        self.assertTrue(any("exact ten maintained source families" in error for error in errors))

    def test_required_source_family_cannot_be_not_applicable(self):
        temp, manifest_path, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        manifest = json.loads(manifest_path.read_text())
        manifest["families"]["projects"] = {"status": "not_applicable", "candidate_ids": [], "dispositions": {}}
        manifest_path.write_text(json.dumps(manifest))
        ledger["source_manifest_sha256"] = digest(manifest_path)
        ledger["source_expansion"] = [
            row for row in ledger["source_expansion"] if row["source_id"] != "projects:repo:a"
        ]
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest_path, ledger_path, draft)
        self.assertTrue(any("required and cannot be marked not_applicable" in error for error in errors))

    def test_qualified_green_candidate_cannot_be_dropped(self):
        temp, manifest, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        ledger["candidates"][0]["final_disposition"] = "skip"
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest, ledger_path, draft)
        self.assertTrue(any("was dropped" in error for error in errors))

    def test_low_signal_candidate_cannot_be_published(self):
        temp, manifest, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        ledger["candidates"][0]["scores"]["novelty"] = 0
        ledger["candidates"][0]["triage"] = "MAYBE"
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest, ledger_path, draft)
        self.assertTrue(any("sub-threshold" in error for error in errors))

    def test_changed_draft_invalidates_ledger(self):
        temp, manifest, ledger, draft, _ = self.fixture()
        self.addCleanup(temp.cleanup)
        draft.write_text(draft.read_text() + "changed\n")
        errors, _ = gate.validate(manifest, ledger, draft)
        self.assertTrue(any("exact draft" in error for error in errors))

    def test_missing_project_activity_decisions_block_selection(self):
        temp, manifest, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        ledger.pop("project_activity_decisions")
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest, ledger_path, draft)
        self.assertTrue(any("project-activity decisions" in error for error in errors))

    def test_new_pr_only_project_cannot_disappear_from_selection(self):
        temp, manifest_path, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        manifest = json.loads(manifest_path.read_text())
        updates_path = Path(manifest["families"]["projects"]["artifact_path"])
        updates_path.write_text(json.dumps({"period": {}, "projects": {"cameri/nostream": {"name": "nostream", "releases": [], "merged_prs": [{"number": 741, "title": "feat: publish relay health events", "merged_at": "2026-09-20T05:05:09Z", "url": "https://github.com/cameri/nostream/pull/741"}]}}}))
        manifest["families"]["projects"]["artifact_sha256"] = digest(updates_path)
        manifest_path.write_text(json.dumps(manifest))
        ledger["source_manifest_sha256"] = digest(manifest_path)
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest_path, ledger_path, draft)
        self.assertTrue(any("not bound to the exact project updates" in error for error in errors))

    def test_selected_pr_requires_an_included_candidate_mapping(self):
        temp, manifest_path, ledger_path, draft_path, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        manifest = json.loads(manifest_path.read_text())
        updates_path = Path(manifest["families"]["projects"]["artifact_path"])
        decisions_path = Path(ledger["project_activity_decisions"]["path"])
        url = "https://github.com/example/alpha/pull/7"
        updates_path.write_text(json.dumps({"period": {}, "projects": {"example/alpha": {"releases": [], "merged_prs": [
            {"number": 7, "title": "feat: signed relay health events", "merged_at": "2026-09-20T05:05:09Z", "base_ref": "main", "url": url}
        ]}}}))
        activity = gate.activity_inventory(json.loads(updates_path.read_text()), digest(updates_path))
        decisions = {
            "schema_version": 1, "updates_sha256": digest(updates_path), "projects": [{
                "repo": "example/alpha", "reviewed_pr_urls": [url], "verdict": "include",
                "reason": "Signed relay health events are a useful new operator-facing capability.",
                "primary_sources": [url], "selected_pr_urls": [url],
                "hard_gate": {key: True for key in gate.HARD_GATES},
                "scores": {key: 2 for key in gate.SCORE_AXES},
                "branch_checks": [{"url": url, "source_url": url, "base_ref": "main", "default_branch": "main"}],
            }],
        }
        self.assertEqual(gate.validate_activity(activity, decisions, url), [])
        decisions_path.write_text(json.dumps(decisions))
        manifest["families"]["projects"]["artifact_sha256"] = digest(updates_path)
        manifest_path.write_text(json.dumps(manifest))
        draft_path.write_text(draft_path.read_text() + f"[Relay health]({url})\n")
        ledger["source_manifest_sha256"] = digest(manifest_path)
        ledger["draft_sha256"] = digest(draft_path)
        ledger["project_activity_decisions"]["sha256"] = digest(decisions_path)
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest_path, ledger_path, draft_path)
        self.assertTrue(any("lacks included candidate mapping" in error for error in errors))
        ledger["candidates"][0]["primary_sources"].append(url)
        ledger["candidates"][0]["draft_sources"].append(url)
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest_path, ledger_path, draft_path)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
