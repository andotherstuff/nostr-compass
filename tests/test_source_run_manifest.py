import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

SCRIPT = Path(__file__).parents[1] / "scripts" / "source_run_manifest.py"
SPEC = importlib.util.spec_from_file_location("source_run_manifest", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SourceRunManifestTests(unittest.TestCase):
    def test_records_hash_and_fails_closed_for_missing_required_family(self):
        with TemporaryDirectory() as directory:
            root = Path(directory); manifest = root / "manifest.json"; artifact = root / "projects.json"; artifact.write_text("payload")
            MODULE.create_manifest(manifest, "2026-09-01T16:00:00Z", "2026-09-08T16:00:00Z", ["projects", "specs"])
            MODULE.record_family(manifest, "projects", 0, artifact)
            value = MODULE.load_manifest(manifest)
            self.assertEqual(value["families"]["projects"]["artifact_sha256"], "239f59ed55e737c77147cf55ad0c1b030b6d7ee748a7426952f9b852d5a935e5")
            self.assertFalse(MODULE.finalize(manifest))
            MODULE.record_family(manifest, "specs", 0, root / "missing.json")
            self.assertFalse(MODULE.finalize(manifest))

    def test_rejects_malformed_and_non_absolute_windows(self):
        with TemporaryDirectory() as directory:
            manifest = Path(directory) / "manifest.json"
            with self.assertRaises(ValueError): MODULE.create_manifest(manifest, "2026-09-01T00:00:00", "2026-09-02T00:00:00Z", ["projects"])
            manifest.write_text("{}")
            with self.assertRaises(ValueError): MODULE.load_manifest(manifest)


if __name__ == "__main__": unittest.main()
