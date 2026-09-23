"""Exact-window canonical ledger builder regression checks."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/build_selection_coverage_2026_09_23.py"


class LedgerBuildTests(unittest.TestCase):
    def build(self, *extra):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "canonical.json"
            run = subprocess.run([sys.executable, str(SCRIPT), "--output", str(output), *extra], cwd=ROOT, text=True, capture_output=True)
            return run, json.loads(output.read_text()) if output.exists() else None

    def test_exact_window_inventory_and_preserved_selection(self):
        run, ledger = self.build()
        self.assertEqual(run.returncode, 0, run.stderr)
        provisional = json.loads((ROOT / "data/newsletter_workspace/selection_coverage_2026-09-23.json").read_text())
        self.assertEqual(ledger["selected"], provisional["selected"])
        self.assertEqual(len(provisional["selected"]), 35)
        self.assertEqual(len(ledger["candidates"]), 144)
        self.assertEqual(sum(c["final_disposition"] == "skip" for c in ledger["candidates"]), 109)
        self.assertEqual(len(ledger["editorial_sources"]), len(ledger["source_expansion"]))
        self.assertEqual({c["candidate_id"] for c in ledger["candidates"]}, {x for row in ledger["source_expansion"] for x in row["candidate_ids"]})
        self.assertEqual(ledger["selection_policy"], {"minimum_score": 8, "maximum_score": 10, "require_no_zero_axis": True, "fixed_item_cap": None, "qualified_items_must_publish": True})
        self.assertEqual(ledger["source_pass_id"], provisional["pass_id"])
        catch_up = next(c for c in ledger["candidates"] if c["candidate_id"] == "top:fips-initramfs-0.1.0")
        self.assertEqual(catch_up["override"], "owner_queued_catch_up")
        self.assertFalse(catch_up["hard_gate"]["in_window_progress"])
        self.assertEqual(catch_up["scores"], next(x["score_axes"] for x in provisional["selected"] if x["id"] == catch_up["candidate_id"]))
        for candidate in ledger["candidates"]:
            self.assertTrue(candidate["triage_decision_ref"])
            if candidate["final_disposition"] == "skip" and not all(candidate["hard_gate"].values()):
                self.assertIsNone(candidate["scores"])
        self.assertEqual(len([c for c in ledger["candidates"] if c["candidate_id"].startswith("discovery:")]), 37)
        self.assertEqual(len(ledger["editorial_sources"]), 144)
        self.assertTrue(ledger["final"])
        self.assertTrue(all(s["collector_source_ids"] or s.get("artifact_provenance", {}).get("artifact_sha256") or s.get("editorial_provenance", {}).get("sha256") for s in ledger["editorial_sources"]))
        manifest = json.loads((ROOT / "data/source_runs/source_run_2026-09-23_tuesday-2026-09-23-codex-1.json").read_text())
        known = {f"{family}:{raw}" for family, meta in manifest["families"].items() for raw in meta["candidate_ids"]}
        self.assertTrue(all(raw in known for source in ledger["editorial_sources"] for raw in source["collector_source_ids"]))
        for source in ledger["editorial_sources"]:
            if source["source_id"] in {"editorial:top:fips-initramfs-0.1.0", "editorial:deep-dive:nip-30"}:
                self.assertIn("editorial_provenance", source)
                self.assertNotIn("artifact_provenance", source)
        override = next(c for c in ledger["candidates"] if c["candidate_id"] == "top:fips-initramfs-0.1.0")
        self.assertEqual(len(override["owner_override_evidence"]["sha256"]), 64)
        run_again, again = self.build()
        self.assertEqual(run_again.returncode, 0, run_again.stderr)
        self.assertEqual(again, ledger)

    def test_current_ledger_passes_publication_checker(self):
        with tempfile.NamedTemporaryFile(dir=ROOT / "data/newsletter_workspace",
                                         suffix=".json", delete=False) as handle:
            output = Path(handle.name)
        self.addCleanup(output.unlink)
        built = subprocess.run(
            [sys.executable, str(SCRIPT), "--output", str(output)],
            cwd=ROOT, text=True, capture_output=True,
        )
        self.assertEqual(built.returncode, 0, built.stderr)
        checked = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check_selection_coverage.py"),
             "--manifest", str(ROOT / "data/source_runs/source_run_2026-09-23_tuesday-2026-09-23-codex-1.json"),
             "--ledger", str(output),
             "--draft", str(ROOT / "content/en/newsletters/2026-09-23-newsletter.md"),
             "--receipt-stdout"],
            cwd=ROOT, text=True, capture_output=True,
        )
        self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
        receipt = json.loads(checked.stdout)
        self.assertEqual(receipt["selected_candidate_count"], 35)
        self.assertEqual(receipt["retained_source_candidate_count"], 144)


if __name__ == "__main__":
    unittest.main()
