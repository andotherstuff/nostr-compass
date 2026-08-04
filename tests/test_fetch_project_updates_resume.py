import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "fetch_project_updates.py"
SPEC = importlib.util.spec_from_file_location("fetch_project_updates", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ResumeCheckpointTests(unittest.TestCase):
    def test_completed_repo_keys_includes_no_activity_successes(self):
        existing = {
            "projects": {"active/repo": {"releases": []}},
            "fetched_repos": ["active/repo", "quiet/repo"],
        }
        self.assertEqual(
            MODULE._completed_repo_keys(existing),
            {"active/repo", "quiet/repo"},
        )

    def test_completed_repo_keys_supports_legacy_checkpoints(self):
        existing = {"projects": {"legacy/repo": {"releases": []}}}
        self.assertEqual(MODULE._completed_repo_keys(existing), {"legacy/repo"})

    def test_completed_repo_keys_does_not_infer_failed_repositories(self):
        existing = {
            "projects": {},
            "fetched_repos": ["successful/repo"],
            "errors": ["retry/me"],
        }
        self.assertEqual(
            MODULE._completed_repo_keys(existing), {"successful/repo"}
        )


if __name__ == "__main__":
    unittest.main()
