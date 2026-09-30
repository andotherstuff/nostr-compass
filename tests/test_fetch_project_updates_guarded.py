import asyncio
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from argparse import Namespace
from datetime import datetime, timezone

SCRIPT = Path(__file__).parents[1] / "scripts" / "fetch_project_updates.py"
spec = importlib.util.spec_from_file_location("guarded_updates", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class GuardedTransportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.cli = self.root / "gh"
        self.calls = self.root / "calls"
        self.cli.write_text("""#!/usr/bin/env python3
import json,os,sys
from pathlib import Path
with Path(os.environ["CALLS"]).open("a") as out:
    out.write(json.dumps({"args":sys.argv[1:],"bulk":os.environ.get("HERMES_GH_BULK")})+chr(10))
if os.environ.get("DEFER") == "1":
    print("GitHub API rate limit reserve (core)", file=sys.stderr)
    sys.exit(75)
print("HTTP/2 200 OK")
print("X-RateLimit-Remaining: 3500")
if "page=2" not in sys.argv[2]:
    print('Link: <https://api.github.com/repos/a/b/releases?per_page=1&page=2>; rel="next"')
print()
print('[{"id":2}]' if "page=2" in sys.argv[2] else '[{"id":1}]')
""")
        self.cli.chmod(0o755)
        env = patch.dict(os.environ, {"COMPASS_GITHUB_GH": str(self.cli), "CALLS": str(self.calls)})
        env.start()
        self.addCleanup(env.stop)
        mod.ACTIVE_WINDOW = None

    def test_guarded_transport_uses_bulk_admission_and_preserves_pagination(self):
        async def run():
            async with mod.GitHubClient("") as client:
                self.assertIsNone(client.client)
                rows = await client.get_paginated("repos/a/b/releases?per_page=1")
                self.assertEqual([{"id":1},{"id":2}], rows)
        asyncio.run(run())
        calls = [json.loads(line) for line in self.calls.read_text().splitlines()]
        self.assertEqual(2, len(calls))
        self.assertTrue(all(item["bulk"] == "1" for item in calls))
        self.assertTrue(all(item["args"][-1] == "--include" for item in calls))

    def test_quota_deferral_is_latched_without_raw_fallback_or_retries(self):
        async def run():
            async with mod.GitHubClient("") as client:
                for _ in range(2):
                    with self.assertRaises(mod.GitHubQuotaDeferred):
                        await client.get("repos/a/b")
        with patch.dict(os.environ, {"DEFER":"1"}):
            asyncio.run(run())
        self.assertEqual(1, len(self.calls.read_text().splitlines()))

    def test_concurrent_batch_stops_network_after_first_quota_deferral(self):
        async def run():
            async with mod.GitHubClient("") as client:
                rows=await asyncio.gather(*(client.get(f"repos/a/r{i}") for i in range(50)),return_exceptions=True)
                self.assertTrue(all(isinstance(row,mod.GitHubQuotaDeferred) for row in rows))
        with patch.dict(os.environ, {"DEFER":"1"}):
            asyncio.run(run())
        self.assertEqual(1,len(self.calls.read_text().splitlines()))

    def test_foreign_page_origin_rejected_before_credentials_or_network(self):
        async def run():
            async with mod.GitHubClient("") as client:
                with self.assertRaisesRegex(RuntimeError, "authenticated API origin"):
                    await client.get("https://foreign.example/repos/a/b")
        asyncio.run(run())
        self.assertFalse(self.calls.exists())

    def test_configured_missing_wrapper_does_not_fall_back(self):
        with patch.dict(os.environ, {"COMPASS_GITHUB_GH": str(self.root / "missing")}):
            with self.assertRaises(RuntimeError):
                mod.GitHubClient("")

    def test_portable_transport_network_failures_are_not_quiet_successes(self):
        mod.ACTIVE_WINDOW=None
        with self.assertRaisesRegex(RuntimeError,"network failed"):
            mod._request_failure("network failed")

    def test_exact_windows_have_distinct_checkpoint_files(self):
        since = datetime(2026,9,21,13,tzinfo=timezone.utc)
        first = datetime(2026,9,30,13,tzinfo=timezone.utc)
        later = datetime(2026,9,30,15,30,tzinfo=timezone.utc)
        self.assertNotEqual(mod.get_output_filename(since,first),mod.get_output_filename(since,later))
        self.assertEqual(mod.get_output_filename(since,first),mod.get_output_filename(since,first))

    def test_quota_stop_checkpoints_but_never_emits_receipt(self):
        args=Namespace(since=datetime(2026,9,21,tzinfo=timezone.utc),
            until=datetime(2026,9,30,13,tzinfo=timezone.utc),since_days=None,
            output_dir=self.root,fresh=False,compact=False,verbose=False,concurrency=2)
        project={"host":"github.com","owner":"a","repo":"b","name":"b","category":"clients"}
        with patch.dict(os.environ, {"DEFER":"1","COMPASS_SOURCE_PASS_ID":"fixture"}), \
                patch.object(mod,"emit_receipt") as receipt:
            with self.assertRaises(SystemExit) as error:
                asyncio.run(mod.run(args,[project]))
        self.assertEqual(75,error.exception.code)
        receipt.assert_not_called()
        output=self.root/mod.get_output_filename(args.since,args.until,scope=mod.collection_scope([project]))
        saved=json.loads(output.read_text())
        self.assertEqual([],saved["fetched_repos"])
        self.assertEqual("2026-09-30T13:00:00Z",saved["collector_window"]["until"])

    def test_partial_repository_failure_cannot_be_certified_as_quiet(self):
        args=Namespace(since=datetime(2026,9,21,tzinfo=timezone.utc),
            until=datetime(2026,9,30,13,tzinfo=timezone.utc),since_days=None,
            output_dir=self.root,fresh=False,compact=False,verbose=False,concurrency=2)
        project={"host":"github.com","owner":"a","repo":"b","name":"b","category":"clients"}
        with patch.dict(os.environ, {"COMPASS_SOURCE_PASS_ID":"fixture"}), \
                patch.object(mod,"fetch_releases",side_effect=RuntimeError("HTTP 500")), \
                patch.object(mod,"emit_receipt") as receipt:
            with self.assertRaisesRegex(RuntimeError,"partial project collection"):
                asyncio.run(mod.run(args,[project]))
        receipt.assert_not_called()
        saved=json.loads((self.root/mod.get_output_filename(args.since,args.until,scope=mod.collection_scope([project]))).read_text())
        self.assertEqual([],saved["fetched_repos"])

    def test_manual_guarded_failure_is_not_certified_as_quiet(self):
        project={"owner":"a","repo":"b"}
        async def run():
            async with mod.GitHubClient("") as client:
                with self.assertRaises(RuntimeError):
                    await mod.fetch_repo(client,project,"2026-09-21T00:00:00Z",False)
        with patch.dict(os.environ,{"COMPASS_SOURCE_PASS_ID":""}), \
                patch.object(mod,"fetch_releases",side_effect=RuntimeError("HTTP 500")):
            mod.ACTIVE_WINDOW=None
            asyncio.run(run())

    def test_verification_resume_persists_repaired_evidence_without_changing_timestamp(self):
        args=Namespace(since=datetime(2026,9,21,tzinfo=timezone.utc),
            until=datetime(2026,9,30,13,tzinfo=timezone.utc),since_days=None,
            output_dir=self.root/"data/project_updates",fresh=False,compact=False,verbose=False,concurrency=2)
        args.output_dir.mkdir(parents=True)
        project={"host":"github.com","owner":"a","repo":"b","name":"b","category":"clients"}
        path=args.output_dir/mod.get_output_filename(args.since,args.until,scope=mod.collection_scope([project]))
        checkpoint={"generated_at":"2026-09-30T13:01:00Z",
            "collector_window":{"since":"2026-09-21T00:00:00Z","until":"2026-09-30T13:00:00Z","compact":False},
            "projects":{},"fetched_repos":["a/b"],
            "_collector_evidence":{"pages":[{"source":"repos/a/b/pulls?per_page=100#walk-0","cursor":"repos/a/b/pulls?per_page=100","cap":100,"count":0,"exhausted":False,"effective_since":"2026-09-21T00:00:00Z","effective_until":"2026-09-30T13:00:00Z"}],"dispositions":{}}}
        path.write_text(json.dumps(checkpoint))
        with patch.dict(os.environ,{"COMPASS_SOURCE_PASS_ID":"fixture-run"}), \
                patch.object(mod,"emit_receipt") as receipt, patch.object(mod,"fetch_repo") as network:
            asyncio.run(mod.run(args,[project]))
        network.assert_not_called()
        receipt.assert_called_once()
        saved=json.loads(path.read_text())
        self.assertEqual(checkpoint["generated_at"],saved["generated_at"])
        self.assertTrue(saved["_collector_evidence"]["pages"][0]["exhausted"])
        sealed=self.root/"data/source_runs/collector_fixture-run_projects.json"
        sealed.parent.mkdir(parents=True);sealed.write_text("sealed")
        path.write_text(json.dumps(checkpoint));before=path.read_bytes()
        with patch.dict(os.environ,{"COMPASS_SOURCE_PASS_ID":"fixture-run"}),patch.object(mod,"emit_receipt") as receipt:
            with self.assertRaisesRegex(RuntimeError,"refusing overwrite"):
                asyncio.run(mod.run(args,[project]))
        self.assertEqual(before,path.read_bytes())
        receipt.assert_not_called()

    def test_mismatched_window_journal_is_not_used_for_resume(self):
        args=Namespace(since=datetime(2026,9,21,tzinfo=timezone.utc),
            until=datetime(2026,9,30,13,tzinfo=timezone.utc),since_days=None,
            output_dir=self.root,fresh=False,compact=False,verbose=False,concurrency=2)
        project={"host":"github.com","owner":"a","repo":"b","name":"b","category":"clients"}
        path=self.root/mod.get_output_filename(args.since,args.until,scope=mod.collection_scope([project]))
        path.write_text(json.dumps({"collector_window":{"since":"2026-09-21T00:00:00Z","until":"2026-09-30T12:00:00Z","compact":False},"fetched_repos":["a/b"],"projects":{}}))
        async def fetch(*_):
            return None
        with patch.object(mod,"fetch_repo",side_effect=fetch) as reader, patch.dict(os.environ,{"COMPASS_SOURCE_PASS_ID":""}):
            asyncio.run(mod.run(args,[project]))
        reader.assert_called_once()



if __name__ == "__main__":
    unittest.main()
