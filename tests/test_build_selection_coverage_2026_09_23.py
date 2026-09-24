"""Retired Tuesday Compass #41 builder must fail closed after the issue advances."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.check_selection_coverage import validate

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/build_selection_coverage_2026_09_23.py"
MANIFEST = ROOT / "data/source_runs/source_run_2026-09-23_tuesday-2026-09-23-codex-1.json"
LEDGER = ROOT / "data/newsletter_workspace/selection_coverage_2026-09-23.json"
DRAFT = ROOT / "content/en/newsletters/2026-09-23-newsletter.md"


class RetiredTuesdayLedgerTests(unittest.TestCase):
    def test_legacy_builder_refuses_advanced_triage(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "retired.json"
            run = subprocess.run(
                [sys.executable, str(SCRIPT), "--output", str(output)],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertNotEqual(run.returncode, 0)
            self.assertIn("missing triage decision section", run.stderr)
            self.assertFalse(output.exists())

    def test_tuesday_ledger_cannot_bless_current_draft(self):
        errors, receipt = validate(MANIFEST, LEDGER, DRAFT)
        self.assertIn("selection ledger does not bind the exact draft", errors)
        self.assertEqual(receipt["verdict"], "FAIL")


if __name__ == "__main__":
    unittest.main()
