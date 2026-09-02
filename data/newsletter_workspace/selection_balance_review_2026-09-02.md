# Independent Stage 4 editorial-balance review — Newsletter #38

Target: 2026-09-02  
Mode: selection only; no newsletter prose

## Verdict

**PASS, conditional on using the allocation and omissions below.** The proposed slate is deliberately shorter than the nominal capacity because the Stage 3 window overlaps material already published in Newsletter #37. Relevance score alone does not override the hard continuity gate.

Evidence reviewed:

- `skills/_COMPASS/agents/OrchestratorAgent.md`, Stage 4, especially lines 122-130.
- `skills/_COMPASS/agents/NewsletterAgent.md`, relevance rubric and section budgets, especially lines 277-300 and 423-475.
- `data/newsletter_workspace/triage_2026-09-02.md` in full.
- `data/coverage_history.json` for every selected and omitted GREEN project.
- Newsletters #35, #36, and #37 in full: `2026-08-12-newsletter.md`, `2026-08-19-newsletter.md`, and `2026-08-26-newsletter.md`.
- Mechanical all-history exact-URL comparison for promoted primary sources.
- Deep-dive existence check: `gh api repos/nostr-protocol/nips/contents/17.md` and `59.md` both returned their paths with exit 0.

## Scoring method

Scores use the requested 0-10 editorial scale: Nostr relevance, user impact, ecosystem breadth, and novelty/continuity value, capped at 10. A score of 8-10 makes an item eligible for News, 5-7 makes it eligible for a shorter section, and below 5 is omitted. The hard prior-newsletter gate is applied after scoring: an otherwise strong item is omitted if its source or substantive behavior was already covered.

## Complete GREEN disposition

| Candidate | Score | Decision | Evidence and balance rationale |
|---|---:|---|---|
| nostream relay-side DVM/auth expansion | 9 | **News** | Distinct PRs #737, #729, #734, #716, and #730; none of these exact URLs appears in prior newsletters. Relay-side DVM ingestion/dispatch and authenticated session/admin behavior form one coherent relay story. Last project mention was 2026-08-19, so this must be framed as a distinct implementation advance, not generic activity. |
| NIP-22 kind 1111 reply path plus NIP-30 alignment | 10 | **OMIT** | Hard duplicate. PR #2358 already appeared in Newsletter #31 (2026-06-24), and PR #2448 plus the kind-1111 rollout were explained at length in Newsletter #37, including its August history section. High relevance does not justify repetition. |
| NWC transaction counts and fee controls | 9 | **Protocol and Spec Work, narrowed** | Include only merged `total_count` support from NWC PR #4 / commit `ff3e49a`, whose exact URLs were not previously used. Omit max-fee PR #2444 / commit `ea75ea8`: Newsletter #37 already explained the fee-ceiling proposal via PR #2444. Do not include lookup-payment PR #5. |
| Amethyst v1.14.0 highlights and reliability | 8 | **OMIT** | Amethyst appeared in all three latest newsletters and has 32 mentions in coverage history. PR #3991 was reproduced exactly in Newsletter #37, while NIP-84 received a full deep dive in Newsletter #34. The remaining release material does not outweigh four-issue saturation. |
| Mostro daemon v0.18.5 | 8 | **Tagged Releases** | New release and PRs #892, #924, and #830 are distinct from prior sources. Keep to one release entry focused on validation-before-spam admission and durable relay-carried order/audit state; do not let Cashu mechanics dominate the Nostr rationale. |
| Divine Mobile 1.0.22 DM correctness | 8 | **Tagged Releases** | Distinct release and PRs #8174, #8173, #8164, and #8163; no exact-URL reuse found. Despite recent Divine coverage, wrapped deletion, preserved signatures, and same-second DM correctness are a new user-facing message-integrity category. Aggregate under one header. |
| Conduit Relay protected inbox | 7 | **Notable Changes** | PR #8 is a distinct primary source and the project last appeared on 2026-06-24. Protected-inbox authentication is concrete relay behavior, but one PR is too narrow for News. |
| NDK for Dart negentropy/request correctness | 8 | **News** | PRs #722, #705, and #726 are distinct sources. Negentropy encoding, request deduplication, and signature verification directly affect multi-relay synchronization and event acceptance. One coherent SDK reliability story; do not mention build/package churn. |
| Shopstr product search and badges | 8 | **Notable Changes, narrowed** | Include only NIP-50 product search #616 and NIP-58 badges #601 as distinct user-facing changes. Omit #437 and #436 because Newsletter #37 already used those exact URLs and fully explained signer/NWC secret containment. This is continuity by new capability, not a reprise of security work. |
| ZapCooking signer relay scoping and NIP-98 | 8 | **Notable Changes** | PRs #633 and #630 are distinct URLs and substantive auth/routing behavior. Keep as one compact item. Avoid expanding generic hardening work or repeating the same authentication explanation used for nostream/Conduit. |
| nostrord DM and multi-device fixes | 8 | **Notable Changes, narrowed** | Include PRs #297, #295, #292, and #293 as distinct DM/event-reference behavior. Omit v2.9.0 because that exact release URL and its relay-scoped group behavior appeared in Newsletter #37. The new angle must be messaging and multi-device interoperability only. |
| MDK v0.9.15 group durability | 8 | **Tagged Releases** | v0.9.15 and PRs #1516, #1550, #1551, and #1559 are distinct sources supporting final-send deduplication, valid KeyPackage choice, membership activity, and epoch-divergence handling. MDK is heavily covered, so limit this to one release entry and omit internal projection/release-prep details. |
| Nostr Java v2.0.8 | 8 | **OMIT** | Exact release URL was already used in Newsletter #37, where subscription isolation and NIP-44 behavior received a full release entry. This is duplicate coverage, not continuity. |
| Pakstr / NostrAppShell v0.16.0 | 7 | **OMIT** | Newsletter #37 already explained publisher validation, publication ordering, Content-Digest, and kind-32267 listing metadata through releases 0.13.0-0.15.0. The newly cited PR URLs and v0.16.0 tag do not establish a distinct reader-facing category; they repackage the same publication-pipeline behavior. |
| NIP-34 native repository issue activity | 5 | **OMIT** | The evidence is 42 issue events and zero patch events. Triage itself warns not to describe these as shipped changes. It is an ecosystem activity signal, but not enough for 2-3 substantive newsletter sentences or a shipping claim. |

## Approved balanced section allocation

### News — 2 items

1. **nostream relay-side DVM and authentication expansion** — 9/10.
2. **NDK for Dart negentropy and request correctness** — 8/10.

The section is intentionally below the usual 5-7 range. Filling it would require promoting repeated projects, narrow single-PR work, or issue-only signals. The selection rules explicitly allow a shorter quiet-week section.

### Tagged Releases — 3 items

1. **Mostro daemon v0.18.5** — 8/10.
2. **Divine Mobile 1.0.22** — 8/10.
3. **MDK v0.9.15** — 8/10.

All three have distinct release/PR evidence and enough behavior for substantive treatment. None should receive a second header elsewhere.

### Notable Changes — 4 items

1. **Conduit Relay protected inbox** — 7/10.
2. **Shopstr NIP-50 product search and NIP-58 badges only** — 8/10.
3. **ZapCooking NIP-46 relay scoping and NIP-98 protection** — 8/10.
4. **nostrord DM and multi-device interoperability fixes only** — 8/10.

This stays inside the 3-5 capacity. It also prevents the authentication cluster from taking over News: Conduit and ZapCooking receive compact treatment, while Shopstr and nostrord supply marketplace/discovery and messaging variety.

### Protocol and Spec Work — 1 item

1. **NWC `total_count` only** — 9/10, using PR #4 and commit `ff3e49a`.

Explicitly exclude the already-covered max-fee source, lookup-payment PR #5, the repeated kind-1111 material, and quiet BUD/Gamma/Concord families. A one-item section is preferable to repeating Newsletter #37's protocol section.

### NIP Deep Dive — 2 NIPs

- **NIP-17: Private Direct Messages**
- **NIP-59: Gift Wrap**

Connection: NIP-17 defines the private-message conversation shape and uses NIP-59 gift wrapping to hide sender/recipient metadata from relays. Neither appeared in the repository's running deep-dive list (NIP-50/84, NIP-09/56, NIP-58/22), and both spec files were independently verified to exist. This pairing gives readers an application-level bridge to the week's Divine and nostrord messaging work without repeating their release details.

Edition type: **Regular**. September 2 is not the final weekly issue of a month, so no month-end history substitution applies.

## Explicit MAYBE omissions

All Stage 3 MAYBEs remain omitted from this selection:

- **NIP language labels #2451** — already covered as open in Newsletter #37; no new merged state.
- **NIP-51 static-site curation #2449** — open proposal, no shipped behavior.
- **NIP-10 preference for kind 1111 #2447** — open and would deepen an already repetitive reply-kind story.
- **Marmot same-account enrollment #417** — already explained as an open experiment in Newsletter #37.
- **NAP-DISPLAY #97/#98** — behavior remains open and Newsletter #37 already covered the draft.
- **0xchat NIP-55 reconnection #76** — narrow single fix amid packaging/CI churn.
- **Infans v2.3.x** — timestamp/batch-release anomaly remains unresolved; Infans was also a Newsletter #37 lead.
- **RSSNotes v0.1.6** — latest-tag substance remains unverified and Recap describes an older version.
- **Iris Drive** — no pinned in-window release or patch event.
- **Napstr** — “new” claim lacks an in-window release artifact.
- **NIP-89 app-handler candidates** — self-published handlers lack verified repository ownership and a material in-window change.
- **NIP-34 Vidstr/flotilla-budabit activity** — issue/test activity is not shipping evidence.

The triage SKIP set also remains omitted wholesale: quiet spec families, open/closed non-merged proposals, secondary-only Recap items, zero-delta Shakespeare/Zapstore data, owner-sibling discoveries without in-window changes, and release/PR churn that fails the Nostr Relay or So What tests.

## Balance and gate checks

- **PASS — section capacity:** 2 News, 3 Tagged Releases, 4 Notable Changes, 1 Protocol item, and 2 deep dives. The only under-cap sections are underfilled to enforce the quality and continuity rules rather than padded.
- **PASS — all-history redundancy:** exact repeats PR #2358, PR #2448, PR #2444, Amethyst PR #3991, Shopstr PRs #437/#436, nostrord v2.9.0, and Nostr Java v2.0.8 are explicitly removed. Pakstr is removed for behavioral repetition even though the wrapper URLs differ.
- **PASS — latest-three continuity:** Amethyst is omitted for saturation; recurring Mostro, Divine, MDK, Shopstr, ZapCooking, and nostrord entries are retained only with distinct sources and distinct behavior, each named above.
- **PASS — narrative balance:** the slate spans relay/DVM infrastructure, SDK synchronization, marketplace/discovery, private messaging, encrypted groups, protected inboxes, signer/HTTP authentication, and wallet-connect protocol behavior. Authentication appears in several candidates but only nostream leads; narrower auth changes stay compact.
- **PASS — source diversity:** the selection uses independent primary sources from nostream, relaystr, Mostro, Divine, Conduit, Shopstr, ZapCooking, nostrord, MDK, NWC, and the NIPs repository. Host diversity is limited because the trustworthy week-specific evidence is mostly GitHub; the non-GitHub Pakstr source is omitted on continuity grounds rather than retained cosmetically.
- **PASS — user relevance:** every selected item changes relay behavior, event correctness, synchronization, signer/auth behavior, marketplace discovery, encrypted-group reliability, or wallet-client responses. Issue counts and inventory baselines are excluded.
- **PASS — weak-source control:** all Recap-only, baseline-only, handler-only, issue-only, and timestamp-ambiguous MAYBEs are omitted.
- **PASS — one-header rule:** each project is allocated to exactly one section; narrowed recurring projects explicitly exclude their previously covered source subset.

GATE: PASS (independent balance review completed; 15/15 GREEN candidates disposed, 12/12 MAYBE groups explicitly omitted or bounded, 7 exact prior-source duplicates plus 1 behavioral duplicate removed, latest three newsletters read in full, NIP-17 and NIP-59 existence checks exit 0)
