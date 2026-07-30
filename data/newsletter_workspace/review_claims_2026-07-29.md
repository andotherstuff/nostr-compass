# Newsletter #33 claims review

Generated: 2026-07-29T16:15:40Z
Target: `content/en/newsletters/2026-07-29-newsletter.md`

## Live verification

- A three-agent factual/editorial review checked the full newsletter against live primary sources. The factual reviewers covered every release and feature claim in the first half, all cited pull-request states in the second half, protocol proposals, specification commits, and the six-year historical section.
- Extracted 37 distinct `NIP-XX` citations and resolved every corresponding canonical file through the GitHub GraphQL API: 37/37 present.
- Rechecked 52 distinct GitHub pull requests: 43 merged and 9 open, with no closed-unmerged PR represented as shipped.
- Resolved all 27 distinct GitHub release-tag links and 29 cited GitHub commit objects.
- Corrected Amethyst attribution: Nostr apps and the broader feature set belong to 1.13.0; NIP-29 host-relay authentication and authenticated Blossom retry behavior belong to 1.13.1.
- Updated Code Call from 0.2.66 to the latest in-window release, 0.2.68, and linked the individual releases supporting multi-session routing, sender verification, relay inbox behavior, and attachment handling.
- Corrected FIPS status: OpenWrt PR #126 is merged; FreeBSD PR #129 remains open. The digest, heading, and body now preserve that distinction.
- Anchored Nostrology figures to the July 29 publication review and corrected the live relay-table count from 34,427 to 34,430; the profile-distribution and top-relay counts matched the live payload.
- Corrected open-proposal tense for BUD-02 PR #110 and the active NIP/NAP drafts.
- Corrected the Cashu specification commit date and the NIP-29 subgroup commit date from July 17/15 to July 16, based on GitHub author timestamps.

## Final regression

The post-edit factual reviewer returned PASS at 16:17:44 UTC after rechecking all 131 external links, 52 pull requests, the release attributions, specification states, historical commits, and the Nostrology snapshot. The post-edit prose reviewer found two heading/body attribution mismatches, both corrected. Its final re-review returned PASS at 16:20:40 UTC with no remaining material factual, grammatical, technical-clarity, source-status, or headline/body issue.

GATE: PASS (post-edit factual and prose regressions passed at 2026-07-29T16:20:40Z)
