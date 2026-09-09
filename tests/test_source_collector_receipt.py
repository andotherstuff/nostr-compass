import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

ROOT = Path(__file__).parents[1]
RECEIPT_SCRIPT = ROOT / "scripts" / "source_collector_receipt.py"
MANIFEST_SCRIPT = ROOT / "scripts" / "source_run_manifest.py"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


RECEIPTS = load(RECEIPT_SCRIPT, "source_collector_receipt")
MANIFESTS = load(MANIFEST_SCRIPT, "source_run_manifest_integration")


class SourceCollectorReceiptTests(unittest.TestCase):
    since = "2026-09-01T16:00:00Z"
    until = "2026-09-08T16:00:00Z"

    def evidence(self, family: str, candidates: list[str] | None = None):
        candidates = [f"{family}:one"] if candidates is None else candidates
        return {
            "effective_since": self.since,
            "effective_until": self.until,
            "query_started_at": "2026-09-08T16:01:00Z",
            "query_finished_at": "2026-09-08T16:02:00Z",
            "canonical_query": {"family": family, "since": self.since, "until": self.until, "endpoint": "fixture"},
            "pages": [{"source": "fixture", "cursor": None, "count": len(candidates), "cap": 100, "exhausted": True, "effective_since": self.since, "effective_until": self.until}],
            "failures": [],
            "candidate_ids": candidates,
            "dispositions": {candidate: {"decision": "include", "reason": "fixture retained"} for candidate in candidates},
        }

    def test_all_ten_collector_receipts_finalize_one_exact_pass(self):
        collectors = {
            "projects": "fetch_project_updates.py", "nip-discussions": "fetch_nostr_nip_discussions.sh",
            "nostr-recap": "fetch_nostr_recap.sh", "shakespeare-apps": "fetch_shakespeare_apps.sh",
            "nip34": "fetch_nip34_repos.sh", "zapstore": "fetch_zapstore_releases.sh",
            "app-discovery": "fetch_app_discovery.py", "heartbeats": "fetch_heartbeats.sh",
            "monthly-history": "fetch_monthly_history.py", "specs": "fetch_spec_updates.py",
        }
        families = list(collectors)
        with TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = root / "source_run.json"
            MANIFESTS.create_manifest(manifest, "pass-all-ten", self.since, self.until, families)
            env = {"COMPASS_SOURCE_PASS_ID": "pass-all-ten", "COMPASS_WINDOW_SINCE": self.since, "COMPASS_WINDOW_UNTIL": self.until}
            for family in families:
                artifact = root / family / "artifact.json"
                artifact.parent.mkdir()
                artifact.write_text("{}\n")
                collector = ROOT / "scripts" / collectors[family]
                source = collector.read_text()
                self.assertTrue("emit_receipt" in source or "source_collector_receipt.py" in source)
                receipt = RECEIPTS.emit_receipt(family=family, artifact=artifact, collector=collector, evidence=self.evidence(family), environ=env, receipt_dir=root / "receipts")
                self.assertIsNotNone(receipt)
                MANIFESTS.ingest_receipt(manifest, receipt)
            self.assertTrue(MANIFESTS.finalize(manifest))
            value = MANIFESTS.load_manifest(manifest)
            self.assertEqual(set(value["families"]), set(families))
            for family in families:
                self.assertEqual(value["families"][family]["candidate_ids"], [f"{family}:one"])
                self.assertIn(f"{family}:one", value["families"][family]["dispositions"])

    def test_rejects_capped_page_without_exhaustion(self):
        evidence = self.evidence("projects")
        evidence["pages"] = [{"source": "github", "cursor": "page=1", "count": 100, "cap": 100, "exhausted": False, "effective_since": self.since, "effective_until": self.until}]
        with self.assertRaisesRegex(ValueError, "capped or incomplete"):
            RECEIPTS.validate_native_evidence(family="projects", evidence=evidence, since=self.since, until=self.until)

    def test_rejects_ignored_until_bound(self):
        evidence = self.evidence("projects")
        evidence["effective_until"] = "2026-09-09T16:00:00Z"
        with self.assertRaisesRegex(ValueError, "exact exclusive pass until"):
            RECEIPTS.validate_native_evidence(family="projects", evidence=evidence, since=self.since, until=self.until)

    def test_rejects_default_or_missing_page_evidence(self):
        evidence = self.evidence("projects")
        evidence["pages"] = []
        with self.assertRaisesRegex(ValueError, "no default"):
            RECEIPTS.validate_native_evidence(family="projects", evidence=evidence, since=self.since, until=self.until)

    def test_rejects_missing_candidate_disposition(self):
        evidence = self.evidence("projects", ["repo:a", "repo:b"])
        del evidence["dispositions"]["repo:b"]
        with self.assertRaisesRegex(ValueError, "every candidate"):
            RECEIPTS.validate_native_evidence(family="projects", evidence=evidence, since=self.since, until=self.until)

    def test_rejects_page_that_ignored_upper_bound_and_partial_failure(self):
        evidence = self.evidence("projects")
        evidence["pages"][0]["effective_until"] = "2026-09-09T16:00:00Z"
        with self.assertRaisesRegex(ValueError, "ignored the exact exclusive upper bound"):
            RECEIPTS.validate_native_evidence(family="projects", evidence=evidence, since=self.since, until=self.until)
        evidence = self.evidence("projects")
        evidence["failures"] = ["one relay failed"]
        with self.assertRaisesRegex(ValueError, "partial collector failures"):
            RECEIPTS.validate_native_evidence(family="projects", evidence=evidence, since=self.since, until=self.until)

    def test_conflicting_same_pass_receipt_fails_closed(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            artifact = root / "data" / "artifact.json"
            artifact.parent.mkdir()
            artifact.write_text("{}\n")
            collector = root / "collector.py"
            collector.write_text("# collector\n")
            env = {"COMPASS_SOURCE_PASS_ID": "pass-retry", "COMPASS_WINDOW_SINCE": self.since, "COMPASS_WINDOW_UNTIL": self.until}
            first = self.evidence("projects")
            RECEIPTS.emit_receipt(family="projects", artifact=artifact, collector=collector, evidence=first, environ=env, receipt_dir=root / "receipts")
            changed = self.evidence("projects", ["projects:changed"])
            with self.assertRaisesRegex(ValueError, "conflicting exact-pass"):
                RECEIPTS.emit_receipt(family="projects", artifact=artifact, collector=collector, evidence=changed, environ=env, receipt_dir=root / "receipts")


if __name__ == "__main__":
    unittest.main()
