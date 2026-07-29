import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_newsletter_continuity.py"


def load_module():
    spec = importlib.util.spec_from_file_location("check_newsletter_continuity", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ContinuityCheckTests(unittest.TestCase):
    def test_flags_repeated_project_header_without_new_primary_source(self):
        checker = load_module()
        previous = """### [Nostrord](https://github.com/nostrord/nostrord) v2.2.0\n\n[Release](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) adds direct-message controls.\n"""
        current = """### Nostrord v2.2.0 follow-up\n\nWith [v2.3.0](#nostrord-v230) leading this week's section, this slot only notes that it follows v2.2.0.\n"""

        findings = checker.review(current, previous)

        self.assertEqual(1, len(findings))
        self.assertEqual("Nostrord", findings[0].project)
        self.assertEqual("no new primary source", findings[0].reason)

    def test_allows_repeated_project_with_a_new_primary_source(self):
        checker = load_module()
        previous = """### [Wisp](https://github.com/barrydeen/wisp) v1.1.0\n\n[Release](https://github.com/barrydeen/wisp/releases/tag/v1.1.0) adds relay controls.\n"""
        current = """### Wisp v1.2.0 adds a multi-account switcher\n\n[Wisp](https://github.com/barrydeen/wisp) shipped [v1.2.0](https://github.com/barrydeen/wisp/releases/tag/v1.2.0) with account switching and reply threads.\n"""

        self.assertEqual([], checker.review(current, previous))

    def test_flags_versioned_project_name_in_previous_heading(self):
        checker = load_module()
        previous = """### [Nostrord v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) adds DM controls\n\nThe [release](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) adds controls.\n"""
        current = """### Nostrord v2.2.0 follow-up\n\nWith [v2.3.0](#nostrord-v230) leading this week's section, this slot only notes that it follows v2.2.0.\n"""

        findings = checker.review(current, previous)

        self.assertEqual([checker.Finding("Nostrord", "no new primary source")], findings)

    def test_flags_versioned_project_name_in_unlinked_previous_heading(self):
        checker = load_module()
        previous = """### Nostrord v2.2.0 adds DM controls\n\n[Release](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) adds controls.\n"""
        current = """### Nostrord v2.2.0 follow-up\n\nWith [v2.3.0](#nostrord-v230) leading this week's section, this slot only notes that it follows v2.2.0.\n"""

        self.assertEqual(
            [checker.Finding("Nostrord", "no new primary source")],
            checker.review(current, previous),
        )

    def test_ignores_projects_absent_from_previous_issue(self):
        checker = load_module()
        previous = "### [Wisp](https://github.com/barrydeen/wisp) v1.1.0\n\nText.\n"
        current = "### ClipRelay ships clipboard sync\n\n[ClipRelay](https://github.com/tajava2006/cliprelay) ships [v0.1.2](https://github.com/tajava2006/cliprelay/releases).\n"

        self.assertEqual([], checker.review(current, previous))

    def test_review_history_catches_repeat_from_older_issue(self):
        checker = load_module()
        older = """### Citrine adds relay management\n\n[Citrine](https://github.com/greenart7c3/Citrine) adds controls.\n"""
        previous = """### A different project\n\n[Release](https://github.com/example/other/releases/tag/v1).\n"""
        current = """### Citrine follow-up\n\nCitrine gets another mention without a release, PR, or commit.\n"""

        findings = checker.review_history(current, [previous, older])

        self.assertIn(checker.Finding("Citrine", "no new primary source"), findings)

    def test_review_history_flags_reused_primary_source_outside_monthly_history(self):
        checker = load_module()
        release = "https://github.com/example/app/releases/tag/v1.2.0"
        older = f"""### Example App 1.2.0\n\n[Release]({release}) shipped.\n"""
        current = f"""### Example App 1.2.0 again\n\n[Release]({release}) shipped.\n"""

        findings = checker.review_history(current, [older])

        self.assertIn(checker.Finding("Example App", "primary source already covered"), findings)


if __name__ == "__main__":
    unittest.main()
