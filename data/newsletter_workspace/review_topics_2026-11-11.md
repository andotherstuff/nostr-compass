# TopicAudit review: Nostr Compass #48 (2026-11-11)


## Results
- check_topic_backlinks.py (with rendered HTML): PASS, 17 topic pages with Primary sources blocks, 17 rendered backlinks.
- All 12 new backlink anchors (route96, keep-android, marmot-projects-at-bitcoin-seoul, nip-01-relays-can-tell-clients-how-long-to-back-off, nip-d9-proposes-events-that-resist-deletion, a-poll-and-a-vote, noornote, amber, streets, nostr-social-graph, splitnut, nip-deep-dive-nip-88-polls) exist as ids in the built HTML.
- All /en/topics/ links in the draft resolve to files.
- NIP link mismatch audit from the repository guidelines: the literal command prints 13 "MISMATCH ... ->" lines, but this is a false positive. The awk field index ($9) is empty for this URL shape. Re-run with a corrected extraction (compare the NIP number to the slug): zero real mismatches.
- Topic page edits (17 files, 18 insertions) are one-line Mentioned-in additions pointing to real anchors. The Cashu, NIP-88 and other claims match the draft text (SplitNut runs a stock Cashu mint; Newsletter 48 compares Amethyst, noStrudel, Coracle and Wisp for iOS). No unsourced factual claims were added.
- NIP-88 reported MISSING_SOURCES: false positive. The page uses a `## Primary sources` heading rather than `**Primary sources:**`, and that section has a source link.

## Findings
1. NIP-47 has a topic page (content/en/topics/nip-47.md), but the draft's "NIP-47 logout method proposed" section (line 95-97) never links it, and the page has no Mentioned-in entry for this issue. The first body mention links only to the GitHub PR. Medium.
2. NIP-69 is mentioned (line 297) as an aside ("today NIP-69 is peer-to-peer trading"). A topic page exists but is not linked and has no mention entry. Low. Acceptable as a disambiguating aside, but linking it is cheap.
3. NIP-88 first mention is in the intro (line 9) as an anchor link to the deep dive, not the topic page. The first topic-page link is in the Nostur section (line 23). The intro link to the issue's own deep dive is reasonable. Low, optional.
4. Concepts with topic pages that are mentioned but never linked: MLS (line 117, topics/mls.md, "built on MLS and Nostr") and Negentropy (line 63, topics/negentropy.md, linked via NIP-77 only). Low. Optional.
5. NIP-D9 has no topic page. It is an open proposal and is linked to its PR, so this is acceptable. NIP-09 and NIP-62 backlinks cover the area.
6. Cashu (first mention line 17 plain text "Cashu ecash", linked at line 83) and Web of Trust (first mention line 23 unlinked, linked at line 63) are not linked at first mention. Low.
7. NIP-01 first body mention is the section heading (line 91). The link is in the paragraph directly below, which is fine.

## Fix list
NIP-47: topic page not linked in draft and has no Mentioned-in entry for 2026-11-11-newsletter
SUGGESTED: link the first mention in the "NIP-47 logout method proposed" paragraph as [NIP-47](/en/topics/nip-47/) (keep the PR link on "logout method"), then add "- [Newsletter #48: NIP-47 logout method proposed](/en/newsletters/2026-11-11-newsletter/#nip-47-logout-method-proposed)" to content/en/topics/nip-47.md Mentioned in.
NIP-69: aside at line 297 unlinked
SUGGESTED (optional): link it as [NIP-69](/en/topics/nip-69/) and add a Mentioned-in entry pointing to the #how-four-clients-tally anchor.
Web of Trust / Cashu / MLS: unlinked at first mention
SUGGESTED (optional): link the first occurrence at lines 23, 17 and 117.

No blocking issues. The fixes above are polish.

GATE: PASS
