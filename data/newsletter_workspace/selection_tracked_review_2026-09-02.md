# Independent Stage 4 tracked-updates selection review — 2026-09-02

Scope: GREEN and MAYBE tracked-project changes in `triage_2026-09-02.md`. Protocol-only proposals, the NIP-34 ecosystem signal, and untracked discovery candidates are outside this review.

## Gate and method

- Applied the NewsletterAgent Nostr Relay Test, 0–12 scoring rubric, minimum base score of 4, minimum final score of 5, and `-2` recent-coverage demotion.
- Read the three immediately preceding issues in full: #35 (2026-08-12), #36 (2026-08-19), and #37 (2026-08-26).
- Queried `data/coverage_history.json` (37 issues, generated 2026-08-26) for every candidate and scanned all 37 English issues for each proposed primary URL after canonicalizing trailing slashes.
- **PASS-SHORTLIST** means a slot may be allocated, but only to the explicitly allowed sources and distinct changes below. **PASS-RESERVE** clears the hard gate but loses on rank or section pressure. **FAIL** means no slot.
- Exact prior-source matches found among the GREEN set: nostream #729; NWC NIPs #2444; Amethyst #3991; Shopstr #436 and #437; nostrord v2.9.0; and Nostr Java v2.0.8. Reusing any of those URLs is prohibited.

## Ranked shortlist

### 1. PASS-SHORTLIST — Amethyst 1.14: NIP-84 highlights, author search, and NWC error handling — 7/12

- **Allowed sources:** [release 1.14](https://github.com/vitorpamplona/amethyst/releases/tag/v1.14.0), [NIP-84 highlight workflow #3983](https://github.com/vitorpamplona/amethyst/pull/3983), [NWC error handling #3987](https://github.com/vitorpamplona/amethyst/pull/3987).
- **Continuity evidence:** coverage history has 32 mentions and ends 2026-08-26; Amethyst also appeared in all three immediately preceding issues. Nevertheless, the allowed sources are absent from all prior issues and support distinct reader-facing behavior: creating highlights from selected article text, filtering search by author, and surfacing wallet-connect errors.
- **Exclusion:** [Blossom authorization #3991](https://github.com/vitorpamplona/amethyst/pull/3991) is an exact-source duplicate of issue #37 and **must not** appear.
- **Why it ranks:** strongest shipped client capability in the batch. The `-2` saturation demotion is already included; do not add generic release miscellany.

### 2. PASS-SHORTLIST — Conduit relay/mono: authenticated deletion and NIP-42 capability enforcement — 7/12

- **Allowed sources:** [authenticated deletion #36](https://github.com/Conduit-BTC/conduit-relay/pull/36), [profile capability verification #265](https://github.com/Conduit-BTC/conduit-mono/pull/265).
- **Continuity evidence:** no exact URL appears in any prior issue. `conduit-relay` has one prior mention (2026-06-24); `conduit-mono` has four, last 2026-08-12. Issue #35 discussed report context through mono #250, not deletion authorization or NIP-42 capability verification.
- **Why it ranks:** two complementary relay-boundary changes answer a clear operator question: which authenticated key may delete or act for a profile. Returning relay work earns +1 history novelty; neither source is a continuity marker.

### 3. PASS-SHORTLIST — Mostro 0.18.5: signed-order admission, audit retention, and Cashu escrow request — 6/12

- **Allowed sources:** [v0.18.5](https://github.com/MostroP2P/mostro/releases/tag/v0.18.5), [signature before spam gate #892](https://github.com/MostroP2P/mostro/pull/892), [kind-8383 retention #924](https://github.com/MostroP2P/mostro/pull/924), [escrow request #830](https://github.com/MostroP2P/mostro/pull/830).
- **Continuity evidence:** 20 historical mentions, last 2026-08-19. Issue #35 covered v0.18.1's escrow foundation; issue #36 covered mobile dispute-chat migration. All four allowed sources are new to history. This item is valid only if the paragraph explains the completed escrow request and the event-level guarantees (signature validation before admission and one-year audit-event retention), rather than saying the release merely follows v0.18.1.
- **Why it ranks:** three distinct protocol-facing guarantees survive the recent-coverage demotion and can support more than two substantive sentences.

### 4. PASS-SHORTLIST — nostream: DVM routing plus authenticated relay/admin sessions — 6/12

- **Allowed sources:** [NIP-89 handler kinds #737](https://github.com/cameri/nostream/pull/737), [worker dispatch #734](https://github.com/cameri/nostream/pull/734), [NIP-42 session tracking #716](https://github.com/cameri/nostream/pull/716), [NIP-98 admin auth #730](https://github.com/cameri/nostream/pull/730).
- **Continuity evidence:** six historical mentions, last 2026-08-19. Issue #36 covered relay monitoring and invite codes (#724/#689/#733/#729). The four allowed URLs are absent from all history and change DVM dispatch or authenticated-session behavior.
- **Exclusion:** [NIP-90 ingestion #729](https://github.com/cameri/nostream/pull/729) is an exact-source duplicate of issue #36. Do not use it to reconstruct the prior week's story.
- **Why it ranks:** a coherent relay-side story remains after removing the duplicate source; avoid turning four links into a PR laundry list.

### 5. PASS-SHORTLIST — CDK: NIP-17 wallet notifications with gift-wrapped receipts — 6/12

- **Allowed sources:** [NIP-17 notification delivery #1266](https://github.com/cashubtc/cdk/pull/1266), [gift-wrapped receipts #1278](https://github.com/cashubtc/cdk/pull/1278).
- **Continuity evidence:** two historical mentions, last 2026-07-15; neither source appears in any prior issue, and CDK is absent from the last three. The scope passes only for relay delivery and encrypted receipt semantics; the rest of the Cashu batch remains out of scope.
- **Why it ranks:** returning, source-clean infrastructure with ecosystem breadth. Keep the paragraph on NIP-17/Nostr delivery rather than ecash internals.

### 6. PASS-SHORTLIST — MDK 0.9.15: durable commits, recovery evidence, and message attribution — 6/12

- **Allowed sources:** [v0.9.15](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.15), [commit publication #1516](https://github.com/marmot-protocol/mdk/pull/1516), [recovery evidence #1550](https://github.com/marmot-protocol/mdk/pull/1550), [message attribution #1551](https://github.com/marmot-protocol/mdk/pull/1551), [pending-message export #1559](https://github.com/marmot-protocol/mdk/pull/1559).
- **Continuity evidence:** 18 historical mentions, last 2026-08-19; MDK was substantial in issues #35 and #36. None of these five sources appears in prior issues. The distinct new claim is a coherent durability/observability contract across commit publication, recovery evidence, attribution, and pending state, not another generic hardening release.
- **Why it ranks:** recent saturation reduces the score, but the new source set supports a protocol-facing change broad enough for a real paragraph. Pick at most three links and aggregate the rest.

### 7. PASS-SHORTLIST — NDK for Dart: negentropy encoding, request identity, and signature verification — 5/12

- **Allowed sources:** [negentropy v1 encoding #722](https://github.com/relaystr/ndk/pull/722), [request dedup key #705](https://github.com/relaystr/ndk/pull/705), [signature verification #726](https://github.com/relaystr/ndk/pull/726).
- **Continuity evidence:** the canonical `relaystr/ndk` row has four mentions, last 2026-08-19; `relaystr/dart_ndk` is an alias with two mentions, last 2026-07-01. Issue #36 covered post-quantum DMs (#713/#712), not synchronization, multi-relay request lifetime, or signature verification. All allowed URLs are absent from prior issues.
- **Why it ranks:** clears the floor after the `-2` recent-coverage demotion, but should be a compact notable change, not a lead.

## Reserves that clear continuity but lose the shortlist

### 8. PASS-RESERVE — Divine 1.0.22 direct-message correctness — 5/12

- **Allowed sources:** [1.0.22](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.22), [sender authorization #8174](https://github.com/divinevideo/divine-mobile/pull/8174), [inbox/reply handling #8154](https://github.com/divinevideo/divine-mobile/pull/8154), [kind-1059 routing #8133](https://github.com/divinevideo/divine-mobile/pull/8133).
- **Evidence:** 19 mentions, last 2026-08-19; substantial coverage in #35 and #36. No exact source duplicates. The DM fixes are distinct, but six consecutive recent appearances and a crowded client field make this a reserve.

### 9. PASS-RESERVE — Pakstr 0.16.0–0.16.3 Zapstore events and publish recovery — 5/12

- **Allowed sources:** [0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0), [NIP-94 assets #64](https://git.nostrdev.com/stuff/pakstr/pulls/64), [event ordering #62](https://git.nostrdev.com/stuff/pakstr/pulls/62), [release-event IDs #61](https://git.nostrdev.com/stuff/pakstr/pulls/61), [publish recovery #57](https://git.nostrdev.com/stuff/pakstr/pulls/57).
- **Evidence:** the non-GitHub project has no coverage-history row, but issue #37 devoted a top story to 0.13.0–0.15.0. None of the allowed URLs is an exact duplicate; 0.16.x adds distinct NIP-94/event-linkage and recovery behavior. The immediate same-surface repetition triggers `-2`, leaving it reserve-only.

### 10. PASS-RESERVE — NWC reference code: `total_count` support only — 5/12

- **Allowed sources:** [merged `total_count` #4](https://github.com/nostr-wallet-connect/nwc/pull/4) and its two pinned implementation commits from triage.
- **Evidence:** four mentions, last 2026-08-26. `total_count` is a distinct response-contract change and its sources are absent from history.
- **Exclusion:** [NIPs fee-ceiling #2444](https://github.com/nostr-protocol/nips/pull/2444) is an exact-source duplicate of issue #37, and the new NWC commit merely implements that already-explained `max_fee` proposal. Do not cover `max_fee` again. `total_count` alone is valid but too narrow for a primary slot unless another item drops.

## GREEN candidates that fail selection

### FAIL — Shopstr

- [Signer secret #437](https://github.com/shopstr-eng/shopstr/pull/437) and [NWC secret #436](https://github.com/shopstr-eng/shopstr/pull/436) are exact-source duplicates of issue #37.
- Product search #616 and profile badges #601 are new, but after `-2` for last-issue coverage the remaining pair scores 4/12 and does not justify another immediate Shopstr slot. History: 17 mentions, last 2026-08-26.

### FAIL — ZapCooking

- PRs #633/#625/#635 are source-clean, but the project has 11 mentions, last 2026-08-19, and issue #36 already devoted a section to its signed-admin and encrypted-wallet security batch. Session-expiry and key-import fixes score 4/12 after the recent-coverage demotion and are too small for two substantive sentences without filler.

### FAIL — nostrord

- [v2.9.0](https://github.com/nostrord/nostrord/releases/tag/v2.9.0) is an exact-source duplicate of issue #37. PRs #297/#295/#292/#293 are new, but nostrord has 14 mentions and appears in all three previous issues. The remaining DM repairs score 4/12 after saturation and do not warrant a fourth consecutive slot.

### FAIL — Nostr Java v2.0.8

- The release URL is an exact-source duplicate of issue #37, which already explained both subscription isolation and portable NIP-44. There is no distinct source or distinct change left. History: three mentions, last 2026-08-26.

## MAYBE tracked-project disposition

| Candidate | Verdict | Evidence-bearing reason |
|---|---|---|
| 0xchat reply-kind fixes | **PASS-RESERVE — 6/12** | PRs #397/#391 are absent from history; two mentions, last 2026-03-11, earn returning novelty. Still reserve because triage lacks a tagged release and the change is narrower than the seven shortlisted items. |
| Infans follow-up | **FAIL** | Issue #37 introduced Infans. Triage cannot verify an in-window timestamp and provides no pinned new primary change; continuity cannot substitute for evidence. |
| RSSNotes v0.1.6 | **FAIL** | No exact duplicate, but release notes were too weak to prove a substantive Nostr delta. Announcement alone does not pass the depth minimum. |
| Gateway PBF signer | **FAIL** | Proof-of-concept is not a working tracked-project release; trust boundaries remain unresolved. |
| NDVM tutorial | **FAIL** | Documentation-only with no shipped project delta. |
| NostrSync calendar | **FAIL** | Announced but untracked and without a pinned working release in the triage evidence. |
| Nostrbook | **FAIL** | Secondary summary only; no primary source. |
| Nostter NIP-48 links | **FAIL** | Small proxy-link handling after five mentions, last 2026-08-19; below 5 after recent demotion. |
| ehagaki | **FAIL** | Embed/UI/PWA batch does not establish a strong relay- or protocol-facing change. |
| StrZap | **FAIL** | Release-window timing is unresolved and the item is largely internal storage/error handling. |
| Diawu | **FAIL** | Validation timing is unresolved; no evidence-bearing in-window change. |
| musig2-nostr v0.1.1 | **FAIL** | Not present in the frozen non-GitHub inventory and therefore not independently reproducible for this issue. |

## Handoff

Allocate tracked-project slots first to ranks 1–7. If section pressure requires fewer items, cut from the bottom; do not replace them with reserves merely to increase project count. Every selected paragraph must cite only its allowed distinct primary sources and explain a change not already covered. Exact-source duplicates listed above are hard exclusions.

**GATE: PASS** — all GREEN/MAYBE tracked-project groups were dispositioned; every proposed source was checked against all 37 prior English issues; the last three issues were read in full; and the shortlist contains seven source-clean, distinct-change candidates with explicit exclusions.
