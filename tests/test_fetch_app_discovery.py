import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

SCRIPT = Path(__file__).parents[1] / "scripts" / "fetch_app_discovery.py"


def load_module():
    spec = importlib.util.spec_from_file_location("app_discovery", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class AppDiscoveryTests(unittest.TestCase):
    def test_cli_writes_candidate_report_and_seen_state_from_fixtures(self):
        github_item = {
            "full_name": "trbouma/safebox-acorn",
            "html_url": "https://github.com/trbouma/safebox-acorn",
            "description": "Acorn component from a Nostr application",
            "created_at": "2026-07-27T20:28:08Z",
            "pushed_at": "2026-08-01T18:28:48Z",
            "homepage": "",
            "stargazers_count": 0,
            "topics": [],
            "_discovery_sources": ["github_text_new"],
        }
        zapstore_event = {
            "id": "e" * 64,
            "pubkey": "a" * 64,
            "created_at": 1785600000,
            "kind": 32267,
            "tags": [
                ["d", "com.example.reader"],
                ["name", "Example Reader"],
                ["summary", "Nostr relay client"],
                ["repository", "https://github.com/example/reader"],
            ],
            "content": "Nostr app listing",
            "_relay": "wss://relay.zapstore.dev",
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            projects = root / "projects.yml"
            github_fixture = root / "github.json"
            nip89_fixture = root / "nip89.json"
            zapstore_fixture = root / "zapstore.json"
            output_dir = root / "out"
            state = root / "seen.json"
            projects.write_text("clients: []\n")
            github_fixture.write_text(json.dumps([github_item]))
            nip89_fixture.write_text("[]\n")
            zapstore_fixture.write_text(json.dumps([zapstore_event]))

            proc = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--since-days",
                    "8",
                    "--today",
                    "2026-08-02",
                    "--projects-file",
                    str(projects),
                    "--output-dir",
                    str(output_dir),
                    "--state-file",
                    str(state),
                    "--github-fixture",
                    str(github_fixture),
                    "--nip89-fixture",
                    str(nip89_fixture),
                    "--zapstore-fixture",
                    str(zapstore_fixture),
                ],
                text=True,
                capture_output=True,
            )

            self.assertEqual(proc.returncode, 0, proc.stderr)
            report = json.loads((output_dir / "discovery_2026-08-02.json").read_text())
            self.assertEqual(report["summary"]["candidate_count"], 2)
            self.assertEqual(report["summary"]["zapstore_listing_candidates"], 1)
            self.assertIn(
                "zapstore_listing",
                {source for item in report["candidates"] for source in item["source_types"]},
            )
            self.assertNotIn("_updated_seen_repositories", report)
            seen = json.loads(state.read_text())
            self.assertEqual(seen["repositories"], ["https://github.com/trbouma/safebox-acorn"])

    def test_normalize_url_rejects_unsafe_or_relative_values(self):
        mod = load_module()
        for value in (
            "javascript:alert(1)",
            "/relative/path",
            "docs/readme",
            "https://user:pass@example.com/app",
            "https://example.com/bad path",
            "https://example.com/\nheader",
        ):
            self.assertEqual(mod.normalize_url(value), "", value)
        self.assertEqual(mod.normalize_url("example.com/app"), "https://example.com/app")

    def test_projects_index_normalizes_repository_and_website_urls(self):
        mod = load_module()
        text = """
clients:
  - name: StableKraft
    repo: https://github.com/ChadFarrow/stablekraft-app/
    website: https://stablekraft.app/
  - name: SafeBox
    repo: https://github.com/trbouma/safebox.git
"""

        index = mod.parse_projects_index(text)

        self.assertEqual(index["repos"]["https://github.com/chadfarrow/stablekraft-app"], "StableKraft")
        self.assertEqual(index["websites"]["https://stablekraft.app"], "StableKraft")
        self.assertEqual(index["repos"]["https://github.com/trbouma/safebox"], "SafeBox")

    def test_github_text_discovery_is_bounded_to_name_and_description(self):
        mod = load_module()
        queries = mod.github_search_queries("2026-07-25")
        text_query = next(query for query, source in queries if source == "github_text_new")

        self.assertIn("in:name,description", text_query)
        self.assertNotIn("readme", text_query)

    def test_github_search_paginates_bounded_results(self):
        mod = load_module()
        first = {
            "total_count": 101,
            "incomplete_results": True,
            "items": [
                {"full_name": f"example/repo-{index}", "html_url": f"https://github.com/example/repo-{index}"}
                for index in range(100)
            ],
        }
        second = {
            "total_count": 101,
            "items": [{"full_name": "example/repo-100", "html_url": "https://github.com/example/repo-100"}],
        }
        responses = [
            subprocess.CompletedProcess([], 0, stdout=json.dumps(first), stderr=""),
            subprocess.CompletedProcess([], 0, stdout=json.dumps(second), stderr=""),
        ]

        warnings = []
        with mock.patch.object(mod.subprocess, "run", side_effect=responses) as run:
            items = mod.run_github_search("topic:nostr", "github_topic_active", warnings=warnings)

        self.assertEqual(len(items), 101)
        self.assertEqual(run.call_count, 2)
        self.assertIn("page=1", run.call_args_list[0].args[0])
        self.assertIn("page=2", run.call_args_list[1].args[0])
        self.assertTrue(any("incomplete_results" in warning for warning in warnings))

    def test_relay_query_drops_malformed_created_at_before_pagination(self):
        mod = load_module()
        malformed = {"id": "a" * 64, "kind": 31990, "created_at": "not-a-timestamp"}
        response = subprocess.CompletedProcess([], 0, stdout=json.dumps(malformed) + "\n", stderr="")

        with mock.patch.object(mod.subprocess, "run", return_value=response):
            events = mod.query_relay_kind("wss://relay.example", 31990, 0, page_size=1, max_pages=1)

        self.assertEqual(events, [])

    def test_github_candidates_require_explicit_nostr_application_signal(self):
        mod = load_module()
        base = {
            "html_url": "https://github.com/example/noise",
            "full_name": "example/noise",
            "homepage": "",
            "created_at": "2026-07-31T00:00:00Z",
            "pushed_at": "2026-08-01T00:00:00Z",
            "stargazers_count": 0,
            "topics": [],
            "_discovery_sources": ["github_text_new"],
        }
        useful = {
            **base,
            "html_url": "https://github.com/example/signer",
            "full_name": "example/signer",
            "description": "A Nostr remote signer app",
        }
        noise = {**base, "description": "Generic coding exercise"}
        topic_noise = {
            **base,
            "html_url": "https://github.com/example/topic-miner",
            "full_name": "example/topic-miner",
            "description": "Bitcoin mining experiment",
            "topics": ["nostr"],
            "_discovery_sources": ["github_topic_active"],
        }
        topic_useful = {
            **base,
            "html_url": "https://github.com/example/topic-signer",
            "full_name": "example/topic-signer",
            "description": "Remote signer",
            "topics": ["nostr"],
            "_discovery_sources": ["github_topic_active"],
        }
        topic_library = {
            **base,
            "html_url": "https://github.com/example/nostr-sdk",
            "full_name": "example/nostr-sdk",
            "description": "Protocol library",
            "topics": ["nostr"],
            "_discovery_sources": ["github_topic_active"],
        }

        candidates, _ = mod.github_candidates(
            [useful, noise, topic_noise, topic_useful, topic_library],
            tracked={"repos": {}, "websites": {}, "names": {}},
            seen_repos=set(),
            since=datetime(2026, 7, 25, tzinfo=timezone.utc),
            first_run=True,
        )

        self.assertEqual(
            {candidate["repository"] for candidate in candidates},
            {useful["html_url"], topic_useful["html_url"]},
        )

    def test_github_discovery_keeps_new_untracked_repos_and_baselines_old_ones(self):
        mod = load_module()
        since = datetime(2026, 7, 25, tzinfo=timezone.utc)
        items = [
            {
                "full_name": "trbouma/safebox-acorn",
                "html_url": "https://github.com/trbouma/safebox-acorn",
                "description": "Acorn component from a Nostr application",
                "created_at": "2026-07-27T20:28:08Z",
                "pushed_at": "2026-08-01T18:28:48Z",
                "homepage": "",
                "stargazers_count": 0,
                "topics": ["nostr"],
            },
            {
                "full_name": "old/example",
                "html_url": "https://github.com/old/example",
                "description": "Older Nostr app",
                "created_at": "2024-01-01T00:00:00Z",
                "pushed_at": "2026-08-01T00:00:00Z",
                "homepage": "https://old.example",
                "stargazers_count": 3,
                "topics": ["nostr"],
            },
            {
                "full_name": "ChadFarrow/stablekraft-app",
                "html_url": "https://github.com/ChadFarrow/stablekraft-app",
                "description": "Tracked",
                "created_at": "2025-01-01T00:00:00Z",
                "pushed_at": "2026-08-01T00:00:00Z",
                "homepage": "https://stablekraft.app",
                "stargazers_count": 1,
                "topics": ["nostr"],
            },
        ]
        tracked = {"repos": {"https://github.com/chadfarrow/stablekraft-app": "StableKraft"}, "websites": {}, "names": {}}

        candidates, seen = mod.github_candidates(items, tracked, set(), since, first_run=True)

        self.assertEqual([candidate["repository"] for candidate in candidates], ["https://github.com/trbouma/safebox-acorn"])
        self.assertEqual(candidates[0]["source_types"], ["github_topic_new"])
        self.assertEqual(candidates[0]["evidence_status"], "unconfirmed")
        self.assertIn("https://github.com/old/example", seen)
        self.assertIn("https://github.com/trbouma/safebox-acorn", seen)

    def test_github_discovery_surfaces_old_repo_when_first_seen_after_baseline(self):
        mod = load_module()
        since = datetime(2026, 7, 25, tzinfo=timezone.utc)
        item = {
            "full_name": "old/example",
            "html_url": "https://github.com/old/example",
            "description": "Older Nostr app newly tagged for discovery",
            "created_at": "2024-01-01T00:00:00Z",
            "pushed_at": "2026-08-01T00:00:00Z",
            "homepage": "https://old.example",
            "stargazers_count": 3,
            "topics": ["nostr"],
        }

        candidates, _ = mod.github_candidates([item], {"repos": {}, "websites": {}, "names": {}}, set(), since, first_run=False)

        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["source_types"], ["github_topic_first_seen"])

    def test_nip89_discovery_requires_identity_location_and_non_dvm_kind(self):
        mod = load_module()
        useful = {
            "id": "useful",
            "pubkey": "a" * 64,
            "kind": 31990,
            "created_at": 100,
            "content": '{"name":"New Reader","website":"https://reader.example","repository":"https://github.com/example/reader"}',
            "tags": [
                ["d", "reader"],
                ["k", "30023"],
                ["web", "https://reader.example/<bech32>"],
                ["latest", f"35128:{'a' * 64}:reader-site", "wss://nos.lol"],
                ["next", "javascript:bad"],
            ],
            "_relay": "wss://nos.lol",
        }
        dvm_only = {
            "id": "dvm",
            "pubkey": "b" * 64,
            "kind": 31990,
            "created_at": 101,
            "content": '{"name":"Summarizer","website":"https://dvm.example"}',
            "tags": [["d", "summarizer"], ["k", "5300"]],
            "_relay": "wss://nos.lol",
        }
        no_location = {
            "id": "missing",
            "pubkey": "c" * 64,
            "kind": 31990,
            "created_at": 102,
            "content": '{"name":"Mystery"}',
            "tags": [["d", "mystery"], ["k", "1"]],
            "_relay": "wss://nos.lol",
        }

        candidates = mod.nip89_candidates([useful, dvm_only, no_location], {"repos": {}, "websites": {}, "names": {}})

        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["name"], "New Reader")
        self.assertEqual(candidates[0]["repository"], "https://github.com/example/reader")
        self.assertEqual(candidates[0]["pubkeys"], ["a" * 64])
        self.assertEqual(candidates[0]["supported_kinds"], [30023])
        self.assertEqual(candidates[0]["source_types"], ["nip89_handler"])
        self.assertEqual(candidates[0]["evidence_status"], "unconfirmed")
        self.assertEqual(candidates[0]["relay_status"], "single-relay")
        self.assertEqual(
            candidates[0]["nsite_references"],
            [{"relation": "latest", "address": f"35128:{'a' * 64}:reader-site", "relay": "wss://nos.lol"}],
        )

    def test_nip89_discovery_ignores_malformed_metadata_and_unsafe_handlers(self):
        mod = load_module()
        malformed = {
            "id": "malformed",
            "pubkey": "a" * 64,
            "kind": 31990,
            "created_at": 100,
            "content": '{"name":{"nested":true},"website":["https://bad.example"]}',
            "tags": [["d", "bad"], ["k", "1"]],
            "_relay": "wss://nos.lol",
        }
        non_string_content = {
            "id": "non-string-content",
            "pubkey": "c" * 64,
            "kind": 31990,
            "created_at": 100,
            "content": {"name": "Not valid NIP-01 content"},
            "tags": [["d", "bad-content"], ["k", "1"]],
            "_relay": "wss://nos.lol",
        }
        safe = {
            "id": "safe",
            "pubkey": "b" * 64,
            "kind": 31990,
            "created_at": 101,
            "content": '{"name":"Reader","website":"https://reader.example"}',
            "tags": [
                ["d", "reader"],
                ["k", "1"],
                ["web", "javascript:alert(1)"],
                ["web", "https://reader.example/<bech32>"],
                ["ios", "reader://event/<bech32>"],
                ["ios", {"not": "a string"}],
            ],
            "_relay": "wss://nos.lol",
        }

        candidates = mod.nip89_candidates(
            [malformed, non_string_content, safe],
            {"repos": {}, "websites": {}, "names": {}},
        )

        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["name"], "Reader")
        self.assertEqual(
            candidates[0]["platform_handlers"],
            [
                {"platform": "web", "template": "https://reader.example/<bech32>"},
                {"platform": "ios", "template": "reader://event/<bech32>"},
            ],
        )

    def test_build_report_marks_partial_sources_without_promoting_candidates(self):
        mod = load_module()
        report = mod.build_report(
            since="2026-07-25T00:00:00+00:00",
            github_items=[],
            nip89_events=[],
            tracked={"repos": {}, "websites": {}, "names": {}},
            seen_repos=set(),
            first_run=True,
            source_errors={"nip89": ["relay timeout"]},
        )

        self.assertEqual(report["summary"]["candidate_count"], 0)
        self.assertEqual(report["summary"]["source_records"], {"github": 0, "nip89": 0, "zapstore": 0})
        self.assertEqual(report["source_status"]["github"], "ok")
        self.assertEqual(report["source_status"]["nip89"], "partial")
        self.assertEqual(report["review_policy"], "candidate-only; never auto-add to projects.yml")

    def test_protocol_candidates_emit_once_and_reemit_on_replacement(self):
        mod = load_module()
        base = {
            "pubkey": "a" * 64,
            "kind": 31990,
            "created_at": 100,
            "content": '{"name":"Reader","website":"https://reader.example"}',
            "tags": [["d", "reader"], ["k", "1"]],
            "_relay": "wss://nos.lol",
        }

        first = mod.build_report(
            since="2026-07-25T00:00:00+00:00",
            github_items=[],
            nip89_events=[{**base, "id": "1" * 64}],
            tracked={"repos": {}, "websites": {}, "names": {}},
            seen_repos=set(),
            first_run=True,
            source_errors={},
            seen_protocol_events={},
        )
        unchanged = mod.build_report(
            since="2026-07-25T00:00:00+00:00",
            github_items=[],
            nip89_events=[{**base, "id": "1" * 64}],
            tracked={"repos": {}, "websites": {}, "names": {}},
            seen_repos=set(),
            first_run=False,
            source_errors={},
            seen_protocol_events=first["_updated_seen_protocol_events"],
        )
        replacement = mod.build_report(
            since="2026-07-25T00:00:00+00:00",
            github_items=[],
            nip89_events=[{**base, "id": "2" * 64, "created_at": 101}],
            tracked={"repos": {}, "websites": {}, "names": {}},
            seen_repos=set(),
            first_run=False,
            source_errors={},
            seen_protocol_events=first["_updated_seen_protocol_events"],
        )

        self.assertEqual(first["summary"]["candidate_count"], 1)
        self.assertEqual(unchanged["summary"]["candidate_count"], 0)
        self.assertEqual(replacement["summary"]["candidate_count"], 1)

    def test_merge_candidates_combines_protocol_and_github_evidence(self):
        mod = load_module()
        github = {
            "name": "reader",
            "repository": "https://github.com/example/reader",
            "website": "https://reader.example",
            "source_types": ["github_topic_new"],
            "review_flags": ["github flag"],
            "topics": ["nostr"],
            "evidence_status": "unconfirmed",
        }
        nip89 = {
            "name": "New Reader",
            "repository": "https://github.com/example/reader",
            "website": "https://reader.example",
            "source_types": ["nip89_handler"],
            "review_flags": ["nip89 flag"],
            "pubkeys": ["a" * 64],
            "supported_kinds": [30023],
            "evidence_status": "unconfirmed",
            "relay_status": "multi-relay",
        }

        merged = mod.merge_candidates([github, nip89])

        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]["source_types"], ["github_topic_new", "nip89_handler"])
        self.assertEqual(merged[0]["pubkeys"], ["a" * 64])
        self.assertEqual(merged[0]["review_flags"], ["github flag", "nip89 flag"])
        self.assertEqual(merged[0]["evidence_status"], "unconfirmed")
        self.assertEqual(merged[0]["relay_status"], "multi-relay")

    def test_merge_candidates_uses_website_alias_when_only_github_has_repository(self):
        mod = load_module()
        github = {
            "name": "reader",
            "repository": "https://github.com/example/reader",
            "website": "https://reader.example",
            "source_types": ["github_topic_new"],
            "review_flags": [],
        }
        nip89 = {
            "name": "New Reader",
            "repository": "",
            "website": "https://reader.example/",
            "source_types": ["nip89_handler"],
            "review_flags": [],
            "pubkeys": ["a" * 64],
        }

        merged = mod.merge_candidates([github, nip89])

        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]["repository"], "https://github.com/example/reader")
        self.assertEqual(merged[0]["source_types"], ["github_topic_new", "nip89_handler"])

    def test_zapstore_listing_discovers_unreleased_untracked_app(self):
        mod = load_module()
        event = {
            "id": "e" * 64,
            "pubkey": "a" * 64,
            "created_at": 1785600000,
            "kind": 32267,
            "tags": [
                ["d", "com.example.reader"],
                ["name", "Example Reader"],
                ["summary", "A Nostr relay client"],
                ["repository", "https://github.com/example/reader.git"],
                ["url", "https://reader.example/"],
            ],
            "content": {"unexpected": "object"},
            "_relay": "wss://relay.zapstore.dev",
        }

        candidates = mod.zapstore_candidates(
            [event],
            tracked={"repos": {}, "websites": {}, "names": {}},
        )

        self.assertEqual(len(candidates), 1)
        candidate = candidates[0]
        self.assertEqual(candidate["repository"], "https://github.com/example/reader")
        self.assertEqual(candidate["website"], "https://reader.example")
        self.assertEqual(candidate["source_types"], ["zapstore_listing"])
        self.assertEqual(candidate["address"], f"32267:{'a' * 64}:com.example.reader")
        self.assertFalse(candidate["has_release_in_window"])
        self.assertEqual(candidate["evidence_status"], "unconfirmed")
        self.assertEqual(candidate["relay_status"], "single-relay")

    def test_zapstore_listing_rejects_weak_or_tracked_metadata(self):
        mod = load_module()
        base = {
            "id": "e" * 64,
            "pubkey": "a" * 64,
            "created_at": 1785600000,
            "kind": 32267,
            "tags": [
                ["d", "com.example.wallet"],
                ["name", "Example Wallet"],
                ["summary", "Bitcoin wallet"],
                ["repository", "https://github.com/example/wallet"],
            ],
            "content": "Bitcoin wallet with no relay functionality.",
            "_relay": "wss://relay.zapstore.dev",
        }
        tracked = {
            **base,
            "id": "f" * 64,
            "tags": [
                ["d", "com.example.reader"],
                ["name", "Example Reader"],
                ["summary", "Nostr relay client"],
                ["repository", "https://github.com/example/reader"],
            ],
        }

        candidates = mod.zapstore_candidates(
            [base, tracked],
            tracked={
                "repos": {"https://github.com/example/reader": "Reader"},
                "websites": {},
                "names": {},
            },
        )

        self.assertEqual(candidates, [])

    def test_relay_fetch_fails_closed_on_invalid_signatures(self):
        mod = load_module()
        valid = {"id": "a" * 64, "kind": 31990, "_relay": "wss://one"}
        invalid = {"id": "b" * 64, "kind": 31990, "_relay": "wss://one"}
        with (
            mock.patch.object(mod, "query_relay_kind", return_value=[valid, invalid]),
            mock.patch.object(mod, "verify_nostr_event", side_effect=lambda event: event["id"] == valid["id"]),
        ):
            events, errors, rejected = mod.fetch_relay_kind_discovery(31990, 0, ["wss://one"])

        self.assertEqual(events, [valid])
        self.assertEqual(errors, [])
        self.assertEqual(rejected, [invalid["id"]])

    def test_verified_events_deduplicates_validation_by_event_id(self):
        mod = load_module()
        events = [
            {"id": "a" * 64, "_relay": "wss://one"},
            {"id": "a" * 64, "_relay": "wss://two"},
            {"id": "b" * 64, "_relay": "wss://one"},
        ]
        checked = []

        kept, rejected = mod.filter_verified_events(events, lambda event: checked.append(event["id"]) or event["id"].startswith("a"))

        self.assertEqual(len(kept), 2)
        self.assertEqual(rejected, ["b" * 64])
        self.assertEqual(checked, ["a" * 64, "b" * 64])

    def test_nip89_discovery_deduplicates_address_and_records_relays(self):
        mod = load_module()
        base = {
            "pubkey": "d" * 64,
            "kind": 31990,
            "content": '{"name":"Handler","website":"https://handler.example"}',
            "tags": [["d", "handler"], ["k", "1"], ["web", "https://handler.example/<bech32>"]],
        }
        older = {**base, "id": "old", "created_at": 100, "_relay": "wss://nos.lol"}
        newer_a = {**base, "id": "new", "created_at": 200, "_relay": "wss://nos.lol"}
        newer_b = {**base, "id": "new", "created_at": 200, "_relay": "wss://relay.primal.net"}

        candidates = mod.nip89_candidates([older, newer_a, newer_b], {"repos": {}, "websites": {}, "names": {}})

        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["event_id"], "new")
        self.assertEqual(candidates[0]["source_relays"], ["wss://nos.lol", "wss://relay.primal.net"])
        self.assertEqual(candidates[0]["evidence_status"], "unconfirmed")
        self.assertEqual(candidates[0]["relay_status"], "multi-relay")


if __name__ == "__main__":
    unittest.main()
