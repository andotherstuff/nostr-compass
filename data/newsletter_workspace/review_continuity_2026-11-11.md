# Review 5: ContinuityValueCheck, Nostr Compass #48 (2026-11-11)
Compared against: #47 (2026-11-04) and #46 (2026-10-28), plus Oct 14/21 for repeated project headers.

## Checker
`python3 scripts/check_newsletter_continuity.py content/en/newsletters/2026-11-11-newsletter.md --history-dir content/en/newsletters`
Result: "PASS: repeated topics use new sources or state a material status change", exit 0, 0 findings.
Month-end history rule: does not apply. The next issue (2026-11-18) is still in November.

## NIP deep-dive repeat check
Prior deep dives (grep of "^## NIP Deep Dive"): NIP-05/24, NIP-23/92, NIP-07, NIP-39, reposts/reactions, NIP-31/73 (#47), NIP-86, NIP-89, NIP-29, NIP-90, custom emoji/video, NIP-36/38, NIP-99. NIP-88 has never been a deep dive. Earlier mentions are passing only: Oct 21 Feather and Staircase polls, Sep 23 Marmot application events, Apr 1 NIP-B9 reference. No repeat. Weak overlap: the #47 NIP-31/73 deep dive used a kind 1068 poll as its alt-tag example.

## Repeated project headers (read against prior paragraphs)
All 15 repeated or related headers cite a distinct primary source and a distinct change, so none must be removed.
- Nostur: Oct 7 was kind 16 reposts. Now polls in 1.35.0 and an in-app browser. New.
- Monostr: Oct 28 was 0.26.0 video and Fediverse. Now Tor in 0.34.0. New.
- Chama: Oct 14/21/28 covered seed backup, wallet bridge and replay vectors. Now 6.4.34 escrow share withholding for trades from 1 Dec. New, security-relevant.
- Zapstore: Oct 21/28 covered 1.1.3 and TV. Now 2.0.2 to 2.0.4 claim labels and trust fallback. New.
- Manent: Oct 21/28 covered 3.0.0 voice notes and Dart NDK. Now 3.1.0 media sizing and ffmpeg-free voice. New.
- Streets: Oct 28 covered reaction emoji sync. Now relay budgets. New.
- NoorNote: Oct 14/21/28 covered 1.9.x. Now 1.9.10 zap invoice checks. New, concrete.
- Keep Android: Oct 21 covered 1.3.0/1.3.2. Now 1.4.0 leak fixes. New.
- nostr-social-graph: Oct 21 covered 3.0.0. Now 4.0.0 breaking snapshot format. New.
- Route96: Oct 21 covered path PUT. Now unreleased security fixes with PR links. New.
- Concord: two merges that explicitly back-reference #45 and #36. Good.
- Amber, MDK, Vector, Marmot spec items: new versions or merges with their own sources.
- Nothing is a version-only note. No entry points back to a lead story as its only content.

## Findings (non-blocking)
1. Missing back-references (reader orientation only; the deltas are real):
   - MDK 0.15.0 (multi-device group creation/invite) and the five Marmot device-group spec items (#498 to #502) build directly on #47's Marmot Protocol (mdk) story: the default-off dev-device-groups linking commands (mdk #2922) and the heartbeat rule (marmot #497). Neither says so. Add one clause, for example "the device linking that #47 reported as default-off", linking /en/newsletters/2026-11-04-newsletter/.
   - nostr-social-graph 4.0.0: add "after 3.0.0 in #45" and link /en/newsletters/2026-10-21-newsletter/.
   - Route96: add a clause linking to #45's path PUT/hash upload coverage, so readers see these are follow-on hardening.
   - Keep Android 1.4.0: optionally name 1.3.x (#45) as the prior release.
   - Chama: optionally say it is the last item of the audit work covered in #44 to #46. The text says "last item of its security audit", but the earlier items are never linked.
2. Value and length: five consecutive Marmot spec items (#498 to #502) are each one or two sentences and read as a changelog. Consider merging #499 to #502 into the existing device-group entry or one combined item. Also, "Logout mirrored in the NWC specs repository" is a thin entry that duplicates the NIP-47 logout item. Merge it into the NIP-47 entry.
3. Marmot at bitcoin++ Seoul (lead): new event and distinct from #47's top story (mdk nightlies). Strong value. The Marmot hackathon item and the SplitNut/Moranduba new projects share a Marmot theme, but their sources are distinct. Keep.
4. Deep dive: add a one-line pointer that NIP-88 polls also appeared as the alt-tag example in #47's NIP-31/73 dive, and that Nostur 1.35.0 (this issue) and Feather (#45) ship them. Optional.

## Fix list
1. (Should) Add #47 back-reference to the MDK 0.15.0 entry and to the first Marmot device-group item.
2. (Should) Add #45 back-references to nostr-social-graph and Route96 (and optionally Keep Android and Chama).
3. (Could) Collapse the Marmot #499 to #502 items and the NWC logout mirror into their parent entries.
None of these is a blocking continuity failure.

GATE: PASS (compared with #47 and #46; continuity checker 0 findings; NIP-88 not previously deep-dived; month-end rule not applicable)
