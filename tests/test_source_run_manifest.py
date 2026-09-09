import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

SCRIPT = Path(__file__).parents[1] / "scripts" / "source_run_manifest.py"
SPEC = importlib.util.spec_from_file_location("source_run_manifest", SCRIPT); assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MODULE)

class SourceRunManifestTests(unittest.TestCase):
    def test_immutable_pass_scoped_complete_receipt(self):
        with TemporaryDirectory() as directory:
            root = Path(directory); manifest = root / "source_run_date_pass-001.json"; artifact = root / "projects.json"; collector = root / "collector.py"; artifact.write_text("payload"); collector.write_text("# v1")
            value = MODULE.create_manifest(manifest, "pass-001", "2026-09-01T16:00:00Z", "2026-09-08T16:00:00Z", ["projects"])
            query = {"family": "projects", "pass_id": "pass-001", **value["window"]}
            MODULE.record_family(manifest, pass_id="pass-001", family="projects", status="complete", artifact=artifact, collector=collector, query=query, pagination_complete=True, item_count=1, page_count=1, include_count=1, skip_count=0, skip_evidence=[], candidate_ids=["repo:one"], dispositions={"repo:one": {"decision": "include", "reason": "retained"}})
            entry = MODULE.load_manifest(manifest)["families"]["projects"]
            self.assertEqual(entry["artifact_sha256"], "239f59ed55e737c77147cf55ad0c1b030b6d7ee748a7426952f9b852d5a935e5"); self.assertTrue(MODULE.finalize(manifest))
            self.assertTrue(MODULE.verify_finalized(manifest))
            artifact.write_text("changed")
            with self.assertRaisesRegex(ValueError, "artifact bytes changed"):
                MODULE.verify_finalized(manifest)
            with self.assertRaises(ValueError): MODULE.create_manifest(manifest, "pass-002", "2026-09-01T16:00:00Z", "2026-09-08T16:00:00Z", ["projects"])

    def test_fails_closed_on_window_pagination_and_skip_evidence(self):
        with TemporaryDirectory() as directory:
            root = Path(directory); manifest = root / "m.json"; artifact = root / "a.json"; collector = root / "c.py"; artifact.write_text("[]"); collector.write_text("v")
            value = MODULE.create_manifest(manifest, "pass-003", "2026-09-01T16:00:00Z", "2026-09-08T16:00:00Z", ["projects"])
            bad = {"family": "projects", "pass_id": "pass-003", "since": value["window"]["since"], "until": "2026-09-09T16:00:00Z"}
            with self.assertRaises(ValueError): MODULE.record_family(manifest, pass_id="pass-003", family="projects", status="empty_verified", artifact=artifact, collector=collector, query=bad, pagination_complete=True, item_count=0, page_count=1, include_count=0, skip_count=0, skip_evidence=[])
            query = {"family": "projects", "pass_id": "pass-003", **value["window"]}
            with self.assertRaises(ValueError): MODULE.record_family(manifest, pass_id="pass-003", family="projects", status="complete", artifact=artifact, collector=collector, query=query, pagination_complete=False, item_count=1, page_count=1, include_count=0, skip_count=1, skip_evidence=[], candidate_ids=["repo:one"], dispositions={"repo:one": {"decision": "skip", "reason": "fixture"}})
            self.assertFalse(MODULE.finalize(manifest))

    def test_not_applicable_is_explicit(self):
        with TemporaryDirectory() as directory:
            root=Path(directory); manifest=root/"m.json"; collector=root/"c.py"; collector.write_text("v"); value=MODULE.create_manifest(manifest,"pass-004","2026-09-01T00:00:00Z","2026-09-02T00:00:00Z",["monthly-history"]); query={"family":"monthly-history","pass_id":"pass-004",**value["window"]}
            MODULE.record_family(manifest,pass_id="pass-004",family="monthly-history",status="not_applicable",artifact=None,collector=collector,query=query,pagination_complete=False,item_count=0,page_count=0,include_count=0,skip_count=0,skip_evidence=[]); self.assertTrue(MODULE.finalize(manifest))

if __name__ == "__main__": unittest.main()
