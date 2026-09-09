import importlib.util
from pathlib import Path
import unittest
from argparse import Namespace
from datetime import datetime, timezone


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


class AbsoluteWindowTests(unittest.TestCase):
    def test_resolves_explicit_absolute_window(self):
        since = MODULE.parse_absolute_time("2026-09-01T16:00:00Z")
        until = MODULE.parse_absolute_time("2026-09-08T16:00:00+00:00")
        self.assertEqual(MODULE.resolve_window(Namespace(since=since, until=until, since_days=None)), (since, until))

    def test_until_filter_is_inclusive_and_preserves_resume_shape(self):
        until = datetime(2026, 9, 8, 16, tzinfo=timezone.utc)
        result = {"releases": [{"published_at": "2026-09-08T16:00:00Z"}, {"published_at": "2026-09-08T16:00:01Z"}], "merged_prs": [], "open_prs": [], "commits": []}
        bounded = MODULE.bound_result_until(result, until)
        self.assertEqual(len(bounded["releases"]), 1)


if __name__ == "__main__":
    unittest.main()
