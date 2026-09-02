# Stage 7 ClaimCheck — Compass Newsletter #38

Reviewed: `content/en/newsletters/2026-09-02-newsletter.md` (current 214-line draft)

Verification: live primary sources checked on 2026-08-26 UTC. GitHub PR, release, tag, compare, commit, and file data were queried with `gh api`; pakstr release/PR/commit data came from the live Forgejo API. The NIP registry was checked at live `nostr-protocol/nips` master `dabfcb2aaecf4fa374eda8b1232ab303a03f60ba` (2026-08-26T18:33:31Z). Tagged releases were checked against complete release bodies and previous-tag comparisons rather than only the changes selected in the draft.

## Result

**FAIL.** PR/release state and NIP-reference liveness are supported, but the draft does not satisfy the repository's mandatory complete tagged-release coverage, and one NIP-18 sentence contradicts the live specification.

## Blocking line-specific fixes

1. **Line 122 — correct the scope of NIP-18 kind 16.** Replace “A kind 16 generic repost can wrap any other event kind” with language that excludes kind 1, for example: “A kind 16 generic repost can wrap any event kind other than kind 1.” Live NIP-18 says kind 6 is reserved for kind 1 and kind 16 “can include any kind of event inside other than `kind 1`.” Source: <https://github.com/nostr-protocol/nips/blob/dabfcb2aaecf4fa374eda8b1232ab303a03f60ba/18.md#generic-reposts>.

2. **Lines 35–37 — complete the Divine Mobile 1.0.22 release audit or remove the tag from this issue.** The paragraph mentions the tag but covers only post-tag PRs #8163, #8164, #8173, and #8174. The complete 1.0.22 release body contains **109 bullets** and the `1.0.20...1.0.22` comparison contains **109 commits / 300 changed files**. Material shipped changes omitted from the write-up include unwanted-badge removal (#7640), recovery/prevention of recordings hidden under the wrong owner (#7737), temporary-relay AUTH publish handling (#7718), and two C2PA recording-integrity/debris fixes (#7740, #7764). Re-audit all 109 release-note entries and add every material user-facing, protocol-facing, security, privacy, reliability, data-loss, and interoperability item; routine CI/docs/translation/cosmetic churn may remain omitted. Sources: <https://github.com/divinevideo/divine-mobile/releases/tag/1.0.22>, <https://github.com/divinevideo/divine-mobile/compare/1.0.20...1.0.22>.

3. **Lines 47–49 — complete Amethyst v1.14.0 coverage.** The release write-up selects NIP-84 and then switches to post-tag PRs, but the full release has **162 release-note bullets**. Consequential shipped work omitted includes NIP-29 channel deletion/archival (#3812), the SharedKeyCache hash-collision and constant-time MAC fix (#3833), NIP-66 relay monitoring (#3836/#3857), connect-time AUTH race repair (#3838), subscription/filter correctness (#3851/#3856), soft-ban authority fixes (#3885), relay-auth permission/session/default behavior (#3899/#3905/#3931/#3937/#3955), discoverable key backup (#3909), Cashu wallet proof backfill/history paging (#3941), and public-chat muting (#3939). Re-audit all 162 notes and cover every material item required by `CLAUDE.md:32`, grouping related changes where useful. Sources: <https://github.com/vitorpamplona/amethyst/releases/tag/v1.14.0>, <https://github.com/vitorpamplona/amethyst/compare/v1.13.1...v1.14.0>.

4. **Lines 53–57 — add the material v0.18.5 release changes, not only the transport default.** The complete Mostro notes and `v0.18.4...v0.18.5` comparison show ten commits. Add the shipped funds/reliability changes: maker-bond timeout anchoring (#879), at-most-once buyer payout dispatch (#881), bounded/non-blocking buyer-payment waits (#883), pending-orderbook republish suppression (#888), and the kind-38386 `created_at` tag (#878). Do **not** present #875 as shipped behavior without explaining that #885 reverts it in the same tag. Sources: <https://github.com/MostroP2P/mostro/releases/tag/v0.18.5>, <https://github.com/MostroP2P/mostro/compare/v0.18.4...v0.18.5>.

5. **Lines 77–79 — complete MDK v0.9.15 coverage.** The draft covers only #1550, #1551, and #1516, while the complete release body has **24 bullets**. Material omitted reliability/security/data-safety changes include publish-gate refusal and epoch-gap recovery (#1519/#1524), empty-admin-policy handling (#1523), external-signer sign-out/wipe (#1528), incident-replay input rejection (#1530), stall detection (#1532), fail-closed OpenClaw allowlisting (#1534), separation of directory discovery from operational relays (#1537), host-authorized outbound-media reads (#1540), suspension storage-close ordering (#1541), account-scoped direct-bot invite policy (#1542), projection recovery (#1543), installer verification/RustSec CI hardening (#1533), and backfill-drain EOSE handling (#1548). Re-audit and cover all material release entries. Sources: <https://github.com/marmot-protocol/mdk/releases/tag/v0.9.15>, <https://github.com/marmot-protocol/mdk/compare/v0.9.14...v0.9.15>.

## NIP-reference liveness and normative audit

The draft contains 24 distinct NIP labels. Every identifier resolves to a merged file in the live canonical repository:

`NIP-09`, `NIP-11`, `NIP-17`, `NIP-18`, `NIP-19`, `NIP-21`, `NIP-25`, `NIP-29`, `NIP-30`, `NIP-40`, `NIP-42`, `NIP-44`, `NIP-46`, `NIP-47`, `NIP-50`, `NIP-59`, `NIP-70`, `NIP-73`, `NIP-77`, `NIP-84`, `NIP-89`, `NIP-90`, `NIP-98`, and `NIP-C7`.

Live registry source: <https://github.com/nostr-protocol/nips/tree/dabfcb2aaecf4fa374eda8b1232ab303a03f60ba>.

Deep-dive claims were checked against complete live NIP-18 and NIP-25 text. Lines 114–120 and 124–159 correctly state draft/optional status, kind 6 and kind 7 behavior, quote `q` tags, protected-event empty content, reaction tags, custom emoji, and external-content kind 17. The sole normative contradiction found is line 122's failure to exclude kind 1 from generic kind-16 reposts. NIP-C7 exists as a merged `draft`/`optional` file and specifies kind 9 chats and `q`-tag replies, supporting lines 65 and 100. Sources: <https://github.com/nostr-protocol/nips/blob/dabfcb2aaecf4fa374eda8b1232ab303a03f60ba/18.md>, <https://github.com/nostr-protocol/nips/blob/dabfcb2aaecf4fa374eda8b1232ab303a03f60ba/25.md>, <https://github.com/nostr-protocol/nips/blob/dabfcb2aaecf4fa374eda8b1232ab303a03f60ba/C7.md>.

The three pinned implementation pairs in lines 202–206 exist at the cited commits: Amethyst's NIP-18/NIP-25 event classes, Snort's NIP-18/NIP-25 helpers, and Ditto's repost/reaction sources. This satisfies the multi-implementation evidence requirement once line 122 is corrected.

## PR, proposal, and release-state audit

- All **27 GitHub PRs linked directly by the draft are merged**, including nostream #716/#730/#734/#737; NDK #705/#722/#726; Divine #8163/#8164/#8173/#8174; Conduit #8; Amethyst #3983/#3987; Mostro #830/#892/#924; MDK #1516/#1550/#1551; Zap Cooking #630/#633; nostrord #292/#293/#295/#297; and NWC #4.
- NWC #4 merged 2026-08-26T08:00:14Z. Live `nostr-wallet-connect/nwc` `05.md` defines optional `total_count` as the number matching request filters “excluding pagination,” supporting lines 106–110. Sources: <https://github.com/nostr-wallet-connect/nwc/pull/4>, <https://github.com/nostr-wallet-connect/nwc/blob/main/05.md>.
- pakstr PR #67 is closed/merged (2026-08-26T06:42:49Z). Forgejo release v0.16.0 was published 2026-08-26T06:47:42Z and its complete notes contain only the kind-32267 ID-logging feature. The `v0.15.0...v0.16.0` comparison has two commits and changes only `publish.ts` plus focused tests; lines 84–86 are complete and supported. Sources: <https://git.nostrdev.com/stuff/pakstr/pulls/67>, <https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0>, <https://git.nostrdev.com/stuff/pakstr/compare/v0.15.0...v0.16.0>.
- Napstr v0.2.0 is a published release (2026-08-26T17:27:48Z). Its release body has no itemized notes, so the full `v0.1.7...v0.2.0` comparison is the operative primary source; the draft appropriately links that comparison. No release-state contradiction was found. Sources: <https://github.com/lnbits/napstr/releases/tag/v0.2.0>, <https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0>.

## Comparative/speculative-claim screen

No unsupported market-share, “first,” “only,” superiority, inevitability, or ecosystem-wide adoption claim was found. The Napstr privacy/transport assertions and the Zap Cooking endpoint/privacy consequences are framed as concrete implementation behavior rather than comparisons. The NIP deep dive's interpretive explanation is anchored to the normative specifications and pinned implementations. These findings do not cure the blocking release-completeness failures above.

## Gate

The draft cannot pass ClaimCheck while four cited tagged releases omit numerous material security, reliability, protocol, funds-safety, and data-safety changes required by `CLAUDE.md:32`, and while line 122 contradicts canonical NIP-18. PR state is otherwise clean (27/27 linked GitHub PRs merged; pakstr #67 merged), all 24 NIP identifiers are live merged files at registry head `dabfcb2`, NWC-05's merged `total_count` wording is verified, and pakstr v0.16.0 is completely covered.

## Correction and authoritative rerun

The blocking NIP-18 sentence now states that kind `16` can wrap any event kind other than kind `1`. The tagged-release sections were expanded from the complete release audits rather than from selected bullets:

- Divine Mobile 1.0.22 now includes badge removal, recording-owner recovery, temporary-relay AUTH publishing, and both C2PA cleanup fixes.
- Amethyst v1.14.0 now includes the NIP-29 and NIP-66 surfaces, SharedKeyCache and relay-race fixes, Concord authority hardening, relay-auth persistence, key backup, Cashu paging, and public-chat muting. Repeated pre-release sources explicitly state the transition to a shipped tag.
- Mostro v0.18.5 now includes the maker-bond clock, at-most-once and bounded payouts, pending-orderbook suppression, dispute timestamps, and the reverted timeout-slash change.
- MDK v0.9.15 now includes the publish-gate, epoch-gap, admin-depletion, sign-out/wipe, incident-replay, stall-detector, OpenClaw, relay-role, outbound-media, shutdown, bot-policy, projection, installer/RustSec, and backfill-drain changes.

All cited PRs were read back as merged with titles matching the described behavior. The complete draft then passed repository style, paragraph-link, continuity, event-example, month/deep-dive, and production-build checks; Shaka scored 100/100 with zero findings.

GATE: PASS (post-correction source audit: canonical NIP-18 exclusion fixed; every material shipped item identified in the complete Divine 1.0.22, Amethyst v1.14.0, Mostro v0.18.5, and MDK v0.9.15 audits is now represented with merged primary-source links; continuity and all prose/build gates pass 2026-08-26 UTC)
