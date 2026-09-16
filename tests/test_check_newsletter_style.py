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
    def test_flags_banned_join_section_detail(self):
        checker = load_module()
        findings = checker.review("Mafrend and Hanami join Shipping This Week with Android releases.")
        self.assertEqual("join Shipping This Week with", findings[0].detail)

    def test_flags_banned_developer_signed_release_detail(self):
        checker = load_module()
        findings = checker.review("A developer-signed release expands the browser forge.")
        self.assertEqual("developer-signed release expands the browser", findings[0].detail)

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
            [finding.detail for finding in findings],
        )

    def test_flags_source_discovery_commentary(self):
        checker = load_module()
        findings = checker.review("The project was discovered through the weekly feed.")
        self.assertEqual("discovered through", findings[0].detail)

    def test_flags_internal_selection_commentary(self):
        checker = load_module()
        findings = checker.review("Eleven versioned releases made the final scope cut.")
        self.assertEqual("made the final scope cut", findings[0].detail)

    def test_flags_opaque_advisory_link_anchor(self):
        checker = load_module()
        findings = checker.review("The fix is documented in [GHSA-abcd-1234-efgh](https://example.com).")
        self.assertEqual("link_anchor", findings[0].kind)

    def test_accepts_descriptive_advisory_link_anchor(self):
        checker = load_module()
        self.assertEqual(
            [],
            checker.review("The [relay parser advisory](https://example.com/GHSA-abcd-1234-efgh) is fixed."),
        )

    def test_flags_generic_heading_that_groups_spec_changes(self):
        checker = load_module()
        findings = checker.review(
            """## Protocol and Spec Work

### NIPs repository

[First change](https://github.com/nostr-protocol/nips/pull/2462) adds commands.

[Second change](https://github.com/nostr-protocol/nips/pull/2463) clarifies payments.

## NIP Deep Dive
"""
        )
        self.assertEqual(
            ["generic_spec_heading", "grouped_spec_changes"],
            [finding.kind for finding in findings],
        )

    def test_flags_generic_family_heading_for_one_spec_change(self):
        checker = load_module()
        findings = checker.review(
            """## Protocol and Spec Work

### Marmot Improvement Proposals

[Relay discovery](https://github.com/marmot-protocol/marmot/pull/422) is clarified.
"""
        )
        self.assertEqual(["generic_spec_heading"], [finding.kind for finding in findings])

    def test_flags_shorthand_family_heading_for_one_spec_change(self):
        checker = load_module()
        findings = checker.review(
            """## Protocol and Spec Work

### NWC

[Payment lookup](https://github.com/nostr-wallet-connect/nwc/pull/5) is specified.
"""
        )
        self.assertEqual(["generic_spec_heading"], [finding.kind for finding in findings])

    def test_flags_pr_and_commit_grouped_under_one_heading(self):
        checker = load_module()
        findings = checker.review(
            """## Protocol and Spec Work

### NWC changes wallet connections

[Payment lookup](https://github.com/nostr-wallet-connect/nwc/pull/5) is specified.
[Connection flow](https://github.com/nostr-wallet-connect/nwc/commit/abcdef1234567) is merged.
"""
        )
        self.assertEqual(["grouped_spec_changes"], [finding.kind for finding in findings])

    def test_flags_spec_change_without_h3(self):
        checker = load_module()
        findings = checker.review(
            """## Protocol and Spec Work

[Payment lookup](https://github.com/nostr-wallet-connect/nwc/pull/5) is specified.
"""
        )
        self.assertEqual(["missing_spec_heading"], [finding.kind for finding in findings])

    def test_accepts_one_descriptive_heading_per_spec_change(self):
        checker = load_module()
        findings = checker.review(
            """## Protocol and Spec Work

### NIP-CD proposes app slash commands

[Slash commands](https://github.com/nostr-protocol/nips/pull/2462) are proposed.

### NIP-A3 clarifies payment target handling

[Payment targets](https://github.com/nostr-protocol/nips/pull/2463) are clarified.

### NWC adds payment lookup and BOLT12

[Payment lookup](https://github.com/nostr-wallet-connect/nwc/pull/5) is specified.
"""
        )
        self.assertEqual([], findings)

    def test_ignores_supporting_implementation_pr_in_spec_item(self):
        checker = load_module()
        findings = checker.review(
            """## Protocol and Spec Work

### NIP-90 proposes expiring DVM heartbeats

[The spec change](https://github.com/nostr-protocol/nips/pull/2465) defines heartbeats.
[A client implementation](https://github.com/example/dvm-client/pull/42) demonstrates it.
"""
        )
        self.assertEqual([], findings)


if __name__ == "__main__":
    unittest.main()
