"""Tests for scripts/check_triage_coverage.py.

The gate answers one question: was this *release* considered? Newsletter #37
could not distinguish "we skipped Nail" from "we never saw Nail", because
nothing checked the triage artifact against the discovered release set.
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "check_triage_coverage.py"
spec = importlib.util.spec_from_file_location("check_triage_coverage", SCRIPT)
assert spec and spec.loader
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class TestMentionKeys(unittest.TestCase):
    def test_includes_name_repo_and_slug(self):
        keys = gate.mention_keys("Nail", "formstr-hq/nail")
        self.assertIn("Nail", keys)
        self.assertIn("formstr-hq/nail", keys)

    def test_strips_a_parenthetical_suffix(self):
        keys = gate.mention_keys("Marmot Protocol (mdk)", "marmot-protocol/mdk")
        self.assertIn("Marmot Protocol", keys)

    def test_drops_generic_tokens_that_would_match_anything(self):
        # A bare "nostr" hit proves nothing in a Nostr newsletter.
        self.assertNotIn("nostr", [k.lower() for k in gate.mention_keys("Nostr", "a/nostr")])

    def test_word_boundaries_prevent_substring_matches(self):
        # "ants" must not be satisfied by "constants".
        self.assertFalse(gate.is_mentioned("many constants here", "ants", "dergigi/ants"))
        self.assertTrue(gate.is_mentioned("ants v0.4.6 shipped", "ants", "dergigi/ants"))


class TestReleaseLevelConsideration(unittest.TestCase):
    """A project-family mention is not consideration of a specific release.

    #37 discussed Marmot's same-account-enrollment spec PR five times but never
    mentioned MDK v0.9.14/v0.9.15 shipping. Treating the family mention as
    coverage would let those releases vanish again, which is the original bug.
    """

    def test_family_mention_does_not_satisfy_a_library_release(self):
        prose = "An open Marmot experiment would replace the withdrawn draft."
        self.assertFalse(
            gate.is_mentioned(prose.lower(), "Marmot Protocol (mdk)", "marmot-protocol/mdk")
        )

    def test_naming_the_repo_does_satisfy_it(self):
        prose = "Skipping marmot-protocol/mdk v0.9.15: library-only, no user-facing surface."
        self.assertTrue(
            gate.is_mentioned(prose.lower(), "Marmot Protocol (mdk)", "marmot-protocol/mdk")
        )


def run_gate(digest: dict, triage_text: str, extra: list[str] | None = None, strict=False):
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        (d / "digest.json").write_text(json.dumps(digest), encoding="utf-8")
        (d / "triage.md").write_text(triage_text, encoding="utf-8")
        cmd = [
            sys.executable,
            str(SCRIPT),
            "--digest",
            str(d / "digest.json"),
            "--triage",
            str(d / "triage.md"),
        ]
        for i, text in enumerate(extra or []):
            p = d / f"extra{i}.md"
            p.write_text(text, encoding="utf-8")
            cmd += ["--also", str(p)]
        if strict:
            cmd.append("--strict")
        proc = subprocess.run(cmd, capture_output=True, text=True)
        return proc.returncode, proc.stdout + proc.stderr


def entry(project, repo, tag, **flags):
    base = {
        "project": project,
        "repo": repo,
        "releases": [{"tag": tag, "published_at": "2026-08-23", "url": "", "body_chars": 10}],
        "never_covered": False,
        "possible_first_release": False,
        "recent_followup": False,
        "last_covered": None,
        "zapstore_listing": [],
        "merged_prs": 0,
        "release_count": 1,
    }
    base.update(flags)
    return base


class TestGateExitCodes(unittest.TestCase):
    def test_fails_when_a_flagged_release_is_untriaged(self):
        digest = {"projects": [entry("Nail", "formstr-hq/nail", "v0.1.0", possible_first_release=True)]}
        code, out = run_gate(digest, "Considered Amethyst and Shopstr this week.")
        self.assertEqual(code, 1)
        self.assertIn("Nail", out)
        self.assertIn("FAIL", out)

    def test_passes_when_the_release_is_written_up(self):
        digest = {"projects": [entry("Nail", "formstr-hq/nail", "v0.1.0", possible_first_release=True)]}
        code, out = run_gate(digest, "Nail v0.1.0 ships the mail bridge; writing it up as a top story.")
        self.assertEqual(code, 0)
        self.assertIn("PASS", out)

    def test_passes_when_the_release_is_explicitly_skipped(self):
        # Skipping is a legitimate editorial choice. Skipping silently is not.
        digest = {"projects": [entry("Nail", "formstr-hq/nail", "v0.1.0", possible_first_release=True)]}
        code, _ = run_gate(digest, "SKIP formstr-hq/nail v0.1.0 — no Nostr surface change since #36.")
        self.assertEqual(code, 0)

    def test_unflagged_releases_are_informational_by_default(self):
        digest = {"projects": [entry("Astraea", "mouse484/astraea", "v5.35.62")]}
        code, out = run_gate(digest, "nothing relevant")
        self.assertEqual(code, 0)
        self.assertIn("informational", out)

    def test_strict_mode_blocks_on_unflagged_releases_too(self):
        digest = {"projects": [entry("Astraea", "mouse484/astraea", "v5.35.62")]}
        code, _ = run_gate(digest, "nothing relevant", strict=True)
        self.assertEqual(code, 1)

    def test_additional_artifacts_count_as_consideration(self):
        digest = {"projects": [entry("Nail", "formstr-hq/nail", "v0.1.0", recent_followup=True)]}
        code, _ = run_gate(digest, "triage says nothing", extra=["Selection: Nail deferred to #38."])
        self.assertEqual(code, 0)

    def test_missing_triage_artifact_is_an_error_not_a_pass(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            (d / "digest.json").write_text(json.dumps({"projects": []}), encoding="utf-8")
            proc = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--digest",
                    str(d / "digest.json"),
                    "--triage",
                    str(d / "absent.md"),
                ],
                capture_output=True,
                text=True,
            )
        self.assertEqual(proc.returncode, 2)

    def test_empty_digest_passes(self):
        code, out = run_gate({"projects": []}, "quiet week")
        self.assertEqual(code, 0)
        self.assertIn("PASS", out)


if __name__ == "__main__":
    unittest.main()
