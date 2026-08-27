"""Tests for scripts/build_release_digest.py.

The regression these guard is concrete: Nail shipped v0.1.0 inside Newsletter
#37's window, was present in both the GitHub and Zapstore fetches, and appeared
in no downstream artifact because the fetch summary reported only aggregates.
"""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "build_release_digest.py"
spec = importlib.util.spec_from_file_location("build_release_digest", SCRIPT)
assert spec and spec.loader
digest_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(digest_mod)


def updates(projects: dict) -> dict:
    return {"period": {"start": "2026-08-18", "end": "2026-08-26"}, "projects": projects}


def project(name, tag, published, releases=None, prs=0):
    return {
        "name": name,
        "releases": releases or [{"tag": tag, "published_at": published, "url": f"https://x/{tag}", "body": "notes"}],
        "merged_prs": [{"number": i} for i in range(prs)],
    }


class TestNormalizeRepo(unittest.TestCase):
    def test_collapses_url_forms_to_one_key(self):
        forms = [
            "formstr-hq/nail",
            "github.com/formstr-hq/nail",
            "https://github.com/formstr-hq/nail",
            "https://github.com/formstr-hq/nail.git",
            "GitHub.com/Formstr-HQ/Nail",
        ]
        keys = {digest_mod.normalize_repo(f) for f in forms}
        self.assertEqual(keys, {"formstr-hq/nail"})


class TestCoverageMatching(unittest.TestCase):
    def test_matches_coverage_history_keyed_by_repo_url(self):
        # coverage_history.json keys are `github.com/owner/repo`; updates keys are
        # `owner/repo`. Comparing project NAMES across the two matched nothing and
        # flagged all 40 projects NEVER-COVERED on this script's first run.
        coverage = {"projects": {"github.com/formstr-hq/nail": {"last_mention_date": "2026-08-19"}}}
        covered = digest_mod.covered_repos(coverage)
        self.assertIn("formstr-hq/nail", covered)
        self.assertEqual(covered["formstr-hq/nail"], "2026-08-19")

    def test_absent_coverage_means_no_flags_rather_than_all_flags(self):
        d = digest_mod.build(updates({"a/b": project("A", "v1.0.0", "2026-08-20")}), None, None)
        self.assertFalse(d["coverage_history_available"])
        self.assertFalse(d["projects"][0]["never_covered"])


class TestFirstReleaseDetection(unittest.TestCase):
    def test_debut_style_tags_are_flagged(self):
        for tag in ("v0.1.0", "0.1.0", "v0.0.1", "v0.2.0"):
            self.assertTrue(digest_mod.looks_like_first_release(tag, 1), tag)

    def test_mature_tags_are_not_flagged(self):
        for tag in ("v1.12.0", "v3.1.50", "2.21.1"):
            self.assertFalse(digest_mod.looks_like_first_release(tag, 1), tag)

    def test_many_releases_in_window_is_not_a_debut(self):
        self.assertFalse(digest_mod.looks_like_first_release("v0.1.0", 7))


class TestNailRegression(unittest.TestCase):
    """The exact shape that was lost from Newsletter #37."""

    def setUp(self):
        self.coverage = {
            "projects": {
                "github.com/formstr-hq/nail": {"last_mention_date": "2026-08-19"},
                "github.com/vitorpamplona/amethyst": {"last_mention_date": "2026-08-19"},
            }
        }
        # A real row matching a tracked project carries nostr_relevant via the
        # tracked-project-override reason; the rollup requires it.
        self.zapstore = {
            "releases": [
                {
                    "tracked_project": "Nail",
                    "app_id": "com.formstr.mail",
                    "version": "1.0",
                    "nostr_relevant": True,
                    "release_created_at": 1787700000,
                    "release_created_at_iso": "2026-08-24T00:00:00Z",
                }
            ]
        }
        self.updates = updates(
            {
                "formstr-hq/nail": project("Nail", "v0.1.0", "2026-08-23", prs=5),
                "vitorpamplona/amethyst": project("Amethyst", "v1.12.9", "2026-08-20", prs=40),
            }
        )

    def test_nail_ranks_first(self):
        d = digest_mod.build(self.updates, self.zapstore, self.coverage)
        self.assertEqual(d["projects"][0]["project"], "Nail")

    def test_nail_carries_every_signal(self):
        d = digest_mod.build(self.updates, self.zapstore, self.coverage)
        nail = d["projects"][0]
        self.assertTrue(nail["possible_first_release"])
        self.assertTrue(nail["recent_followup"], "introduced in #36, released during #37")
        self.assertEqual(nail["last_covered"], "2026-08-19")
        self.assertEqual(nail["zapstore_listing"][0]["app_id"], "com.formstr.mail")

    def test_release_is_named_in_the_markdown(self):
        d = digest_mod.build(self.updates, self.zapstore, self.coverage)
        md = digest_mod.render_markdown(d)
        # The whole point: the tag and URL appear as text, not as a count.
        self.assertIn("v0.1.0", md)
        self.assertIn("formstr-hq/nail", md)
        self.assertIn("FOLLOW-UP", md)

    def test_every_project_gets_a_decision_slot(self):
        d = digest_mod.build(self.updates, self.zapstore, self.coverage)
        md = digest_mod.render_markdown(d)
        self.assertEqual(md.count("Triage decision:"), len(d["projects"]))


class TestZapstoreRollup(unittest.TestCase):
    def test_prefers_the_fetcher_apps_rollup(self):
        z = {
            "apps": [{"app_id": "a.b", "app_name": "A", "tracked_project": "A", "latest_version": "9.9"}],
            "releases": [{"app_id": "ignored", "nostr_relevant": True}],
        }
        apps = digest_mod.zapstore_apps(z)
        self.assertEqual([a["app_id"] for a in apps], ["a.b"])

    def test_falls_back_to_grouping_releases(self):
        z = {
            "releases": [
                {"app_id": "a.b", "app_name": "A", "version": "1.0", "nostr_relevant": True, "release_created_at": 1},
                {"app_id": "a.b", "app_name": "A", "version": "1.1", "nostr_relevant": True, "release_created_at": 2},
            ]
        }
        apps = digest_mod.zapstore_apps(z)
        self.assertEqual(len(apps), 1)
        self.assertEqual(apps[0]["release_count"], 2)
        # Sorted on release_created_at, because published_at is null on every row.
        self.assertEqual(apps[0]["latest_version"], "1.1")

    def test_excludes_apps_that_are_not_nostr_relevant(self):
        z = {"releases": [{"app_id": "x.y", "nostr_relevant": False, "release_created_at": 1}]}
        self.assertEqual(digest_mod.zapstore_apps(z), [])

    def test_zapstore_only_tracked_project_is_surfaced(self):
        # Imwald shipped 0.4.0 on Zapstore inside #37's window with no GitHub
        # release. A GitHub-only digest could not see it.
        z = {
            "apps": [
                {
                    "app_id": "eu.imwald.android",
                    "app_name": "Imwald Android",
                    "tracked_project": "Imwald Android",
                    "latest_version": "0.4.0",
                    "latest_at": "2026-08-25T00:00:00Z",
                    "release_count": 4,
                }
            ]
        }
        d = digest_mod.build(updates({"a/b": project("Other", "v1.0.0", "2026-08-20")}), z, None)
        self.assertEqual(len(d["zapstore_only"]), 1)
        md = digest_mod.render_markdown(d)
        self.assertIn("Imwald Android", md)
        self.assertIn("no GitHub release in window", md)

    def test_zapstore_app_matching_a_github_release_is_not_listed_twice(self):
        z = {"apps": [{"app_id": "a.b", "app_name": "A", "tracked_project": "A", "latest_version": "1.0"}]}
        d = digest_mod.build(updates({"a/b": project("A", "v1.0.0", "2026-08-20")}), z, None)
        self.assertEqual(d["zapstore_only"], [])
        self.assertEqual(d["projects"][0]["zapstore_listing"][0]["app_id"], "a.b")


class TestFollowUpWindow(unittest.TestCase):
    def test_stale_coverage_is_not_a_followup(self):
        coverage = {"projects": {"github.com/a/b": {"last_mention_date": "2026-01-01"}}}
        d = digest_mod.build(updates({"a/b": project("A", "v0.1.0", "2026-08-20")}), None, coverage)
        self.assertFalse(d["projects"][0]["recent_followup"])

    def test_release_before_coverage_is_not_a_followup(self):
        # Negative gap: the release predates the mention, so the mention already
        # covered it. Flagging it would send triage after old news.
        coverage = {"projects": {"github.com/a/b": {"last_mention_date": "2026-08-26"}}}
        d = digest_mod.build(updates({"a/b": project("A", "v0.1.0", "2026-08-20")}), None, coverage)
        self.assertFalse(d["projects"][0]["recent_followup"])

    def test_unparseable_dates_do_not_crash(self):
        coverage = {"projects": {"github.com/a/b": {"last_mention_date": "not-a-date"}}}
        d = digest_mod.build(updates({"a/b": project("A", "v0.1.0", "2026-08-20")}), None, coverage)
        self.assertFalse(d["projects"][0]["recent_followup"])


class TestOutputHygiene(unittest.TestCase):
    def test_projects_without_releases_are_omitted(self):
        d = digest_mod.build(
            updates({"a/b": {"name": "Quiet", "releases": [], "merged_prs": []}}), None, None
        )
        self.assertEqual(d["release_bearing_projects"], 0)

    def test_empty_release_notes_are_called_out(self):
        u = updates(
            {"a/b": {"name": "A", "releases": [{"tag": "v0.1.0", "published_at": "2026-08-20", "url": "", "body": ""}], "merged_prs": []}}
        )
        md = digest_mod.render_markdown(digest_mod.build(u, None, None))
        self.assertIn("empty release notes", md)

    def test_deterministic_across_runs(self):
        u = updates(
            {
                "a/b": project("A", "v0.1.0", "2026-08-20"),
                "c/d": project("C", "v2.0.0", "2026-08-21"),
            }
        )
        first = digest_mod.render_markdown(digest_mod.build(u, None, None))
        second = digest_mod.render_markdown(digest_mod.build(u, None, None))
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()


class TestSuppressionRule(unittest.TestCase):
    """Recency alone must never suppress a project.

    The owner's rule: skip only when a project was covered in the previous issue
    AND shipped nothing exciting. #37 dropped Nail v0.1.0 on recency alone.
    """

    RECENT = {"projects": {"github.com/a/b": {"last_mention_date": "2026-08-19"}}}

    def entry_for(self, tag, body, prs=0, coverage=None):
        u = updates(
            {
                "a/b": {
                    "name": "A",
                    "releases": [
                        {"tag": tag, "published_at": "2026-08-23", "url": "u", "body": body}
                    ],
                    "merged_prs": [{"number": i, "title": "chore: bump"} for i in range(prs)],
                }
            }
        )
        d = digest_mod.build(u, None, coverage if coverage is not None else self.RECENT)
        return d["projects"][0]

    def test_recent_plus_substance_is_never_suppressible(self):
        e = self.entry_for("v0.1.0", "Add android app to mailstr; Zapstore publish config")
        self.assertTrue(e["recent_followup"])
        self.assertTrue(e["substance_signals"])
        self.assertFalse(e["suppression_allowed"])

    def test_recent_with_no_substance_is_suppressible(self):
        # A bare compare link carries nothing a reader can use.
        e = self.entry_for(
            "v0.3.46",
            "**Full Changelog**: https://github.com/x/y/compare/v0.3.44...v0.3.46",
        )
        self.assertTrue(e["recent_followup"])
        self.assertEqual(e["substance_signals"], [])
        self.assertTrue(e["suppression_allowed"])

    def test_never_covered_is_never_suppressible_even_without_substance(self):
        e = self.entry_for("v9.9.9", "", coverage={"projects": {}})
        self.assertFalse(e["recent_followup"])
        self.assertFalse(e["suppression_allowed"])

    def test_messaging_features_count_as_substance(self):
        # NYM v3.75.543 was wrongly suppressible before these patterns existed.
        e = self.entry_for(
            "v3.75.543",
            "New: message threads in channels, PMs, and group chats\nHotfix: post-quantum encrypted PMs",
        )
        self.assertIn("messaging-feature", e["substance_signals"])
        self.assertIn("encryption", e["substance_signals"])
        self.assertFalse(e["suppression_allowed"])

    def test_boilerplate_alone_is_not_documented_change(self):
        body = "## What's Changed\n**Full Changelog**: https://github.com/x/y/compare/a...b"
        self.assertLess(digest_mod.documented_change_chars([{"body": body}]), 120)

    def test_real_notes_count_as_documented_change(self):
        body = "### Features\n\n- accept LUD-25 bearer notes in an X-LNURLcash header, wiring the rails adapter through the new header parser and covering it with integration tests\n"
        self.assertGreaterEqual(digest_mod.documented_change_chars([{"body": body}]), 120)

    def test_suppressible_entries_sort_last(self):
        u = updates(
            {
                "a/b": {
                    "name": "Quiet",
                    "releases": [{"tag": "v1.2.3", "published_at": "2026-08-23", "url": "", "body": "**Full Changelog**: https://x/y"}],
                    "merged_prs": [],
                },
                "c/d": {
                    "name": "Loud",
                    "releases": [{"tag": "v0.1.0", "published_at": "2026-08-23", "url": "", "body": "Adds android app and relay support"}],
                    "merged_prs": [],
                },
            }
        )
        cov = {
            "projects": {
                "github.com/a/b": {"last_mention_date": "2026-08-19"},
                "github.com/c/d": {"last_mention_date": "2026-08-19"},
            }
        }
        d = digest_mod.build(u, None, cov)
        self.assertEqual(d["projects"][0]["project"], "Loud")
        self.assertEqual(d["projects"][-1]["project"], "Quiet")

    def test_markdown_states_when_a_skip_is_defensible(self):
        e = self.entry_for("v0.3.46", "**Full Changelog**: https://x/y/compare/a...b")
        d = {"projects": [e], "total_releases": 1, "release_bearing_projects": 1,
             "coverage_history_available": True, "zapstore_apps": 0, "zapstore_only": []}
        md = digest_mod.render_markdown(d)
        self.assertIn("a skip is defensible", md)
