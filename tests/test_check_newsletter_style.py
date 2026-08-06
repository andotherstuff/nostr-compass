import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_newsletter_style.py"


def load_module():
    spec = importlib.util.spec_from_file_location("check_newsletter_style", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class NewsletterStyleTests(unittest.TestCase):
    def test_flags_banned_join_section_phrase(self):
        checker = load_module()
        findings = checker.review("Mafrend and Hanami join Shipping This Week with Android releases.")
        self.assertEqual("join Shipping This Week with", findings[0].phrase)

    def test_flags_banned_developer_signed_release_phrase(self):
        checker = load_module()
        findings = checker.review("A developer-signed release expands the browser forge.")
        self.assertEqual("developer-signed release expands the browser", findings[0].phrase)

    def test_accepts_direct_specific_prose(self):
        checker = load_module()
        self.assertEqual([], checker.review("GitWorkshop adds maintainer coordination and repository sync."))

    def test_flags_internal_tracking_commentary(self):
        checker = load_module()
        findings = checker.review(
            "The repository has been added to Compass's signer tracker so later releases enter the weekly fetch."
        )
        self.assertEqual(
            ["has been added to Compass's", "so later releases"],
            [finding.phrase for finding in findings],
        )

    def test_flags_source_discovery_commentary(self):
        checker = load_module()
        findings = checker.review("The project was discovered through the weekly feed.")
        self.assertEqual("discovered through", findings[0].phrase)

    def test_flags_internal_selection_commentary(self):
        checker = load_module()
        findings = checker.review("Eleven versioned releases made the final scope cut.")
        self.assertEqual("made the final scope cut", findings[0].phrase)


if __name__ == "__main__":
    unittest.main()
