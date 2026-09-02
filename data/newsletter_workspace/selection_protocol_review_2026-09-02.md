# Independent Stage 4 protocol/deep-dive review — Newsletter #38

**Target:** 2026-09-02  
**Source window:** 2026-08-19T00:00:00Z–2026-08-27T00:00:00Z  
**Live verification:** 2026-08-26T18:00:18Z  
**Mode:** selection only; no newsletter prose

## Overall verdict

- **PASS — Protocol/spec selection:** NWC-05 optional `total_count` in `list_transactions`, narrowly scoped to the newly merged change.
- **PASS — Deep-dive pair:** **NIP-18 (Reposts) + NIP-25 (Reactions)**.
- **FAIL — Mainline NIPs reply-convergence item for this issue:** technically strong and merged, but already covered in the immediately preceding newsletter.
- **FAIL — NIP-25 + NIP-30 as the deep-dive pair:** tighter cross-reference, but NIP-30 was materially covered in Newsletter #37; NIP-18 + NIP-25 is the continuity-safe pair.

## 1. Protocol/spec selection

### PASS — NWC-05 transaction totals

**Select:** [nostr-wallet-connect/nwc PR #4](https://github.com/nostr-wallet-connect/nwc/pull/4), “NWC 05: add optional total_count to list_transactions response.”

Evidence:

- The source artifact records the merge commit [6b408ad](https://github.com/nostr-wallet-connect/nwc/commit/6b408adedbd38da584035f949c48a368a792bd8b) at `2026-08-26T08:00:13Z`, inside the declared window.
- Live GitHub verification returned `merged: true`, `merged_at: 2026-08-26T08:00:14Z`, merge SHA `6b408adedbd38da584035f949c48a368a792bd8b`.
- The substantive commits are [ff3e49a](https://github.com/nostr-wallet-connect/nwc/commit/ff3e49a47d040075edc46ee42fc0e33f10f1ef67) (adds optional `total_count`) and [06315e7](https://github.com/nostr-wallet-connect/nwc/commit/06315e735f744b1afd3df0b57436fdce8a7bfc2e) (clarifies that the count excludes pagination).
- Continuity scan: Newsletter #37 discussed the NWC `max_fee` proposal, but contains no `total_count`, `list_transactions`, or NWC-05 transaction-count coverage. This is a distinct merged source/change.

Selection boundary:

- Advance only the transaction-count change.
- Do **not** bundle it as a generic “transaction counts and fee controls” item: the fee-control half was already covered in Newsletter #37 and its corresponding NIPs PR remains open.

### FAIL — NIP-22/NIP-30 kind-1111 convergence

Candidates:

- [NIPs PR #2358](https://github.com/nostr-protocol/nips/pull/2358), live-verified merged at `2026-08-24T16:54:49Z`, merge SHA [13664fb](https://github.com/nostr-protocol/nips/commit/13664fb18a3ce5fa48a849de012ab789d82eb254).
- [NIPs PR #2448](https://github.com/nostr-protocol/nips/pull/2448), live-verified merged at `2026-08-25T10:58:35Z`, merge SHA [735a25e](https://github.com/nostr-protocol/nips/commit/735a25e44b8e7a01539864f2a2dcf3e728977fd3).

Why FAIL for Newsletter #38:

- Newsletter #37’s protocol section already states that Snort and Ditto use NIP-22 kind `1111` for ordinary replies and explicitly links PR #2448’s addition of kind `1111` to NIP-30.
- Its August history section repeats the same NIP-22 amendment and NIP-30 merge.
- This is exact-source/exact-change continuity duplication, not a new implementation or follow-up.
- NIP-22 is also rotation-excluded: it was deep-dived in `content/en/newsletters/2026-08-19-newsletter.md` under “Comments (NIP-22).”

### FAIL — NWC `max_fee` as a second protocol item

Evidence/status:

- NWC commit [ea75ea8](https://github.com/nostr-wallet-connect/nwc/commit/ea75ea82677cb5e0e742bda4a5c12fb601481a4c) is in-window.
- Corresponding [NIPs PR #2444](https://github.com/nostr-protocol/nips/pull/2444) was live-verified **OPEN**, not merged.
- Newsletter #37 already explained the proposed `max_fee` semantics and the dependency on NWC-side agreement.

Why FAIL: immediate continuity duplicate, plus no newly merged NIP-side standard.

### FAIL — Open NIPs proposals

Live-verified statuses:

- [PR #2451](https://github.com/nostr-protocol/nips/pull/2451), BCP-47 language labels — **OPEN**.
- [PR #2449](https://github.com/nostr-protocol/nips/pull/2449), NIP-51 static-site curation sets — **OPEN**.
- [PR #2447](https://github.com/nostr-protocol/nips/pull/2447), NIP-10 preference for kind `1111` replies — **OPEN**.
- [PR #2445](https://github.com/nostr-protocol/nips/pull/2445), NIP-100 agent identity proposal — **OPEN**.

Why FAIL: no merged behavior. PR #2451 and the kind-1111 family also overlap Newsletter #37 coverage.

### FAIL — NAP-DISPLAY and Marmot same-account enrollment

Live-verified statuses:

- [NAP registry PR #98](https://github.com/napplet/naps/pull/98) — **MERGED** at `2026-08-20T16:15:49Z`; it registers a draft interface.
- [NAP behavior PR #97](https://github.com/napplet/naps/pull/97) — **OPEN**; runtime-controlled pixel displays remain draft.
- [Marmot PR #417](https://github.com/marmot-protocol/marmot/pull/417) — **OPEN**.

Why FAIL: Newsletter #37 already covered both proposals and correctly distinguished registry landing from unmerged behavior. No new merge or implementation boundary exists for #38.

## 2. Deep-dive selection

### PASS — NIP-18 (Reposts) + NIP-25 (Reactions)

#### Eligibility

- [NIP-18](https://github.com/nostr-protocol/nips/blob/master/18.md) and [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md) both resolve live (`HTTP 200`) as merged files on `nostr-protocol/nips` master. Both currently carry `draft` / `optional` labels; “merged” here means present in the canonical repository, not “final.”
- Archive scan of every `## NIP Deep Dive` section, including generic August headings and their `###` subsections, found **no prior NIP-18 or NIP-25 deep dive**.
- The pair is coherent: both define signed social-distribution actions over existing events. NIP-18 uses kind `6` for note reposts, kind `16` for generic reposts, and `q` tags for quotes; NIP-25 uses kind `7` reactions, with `e`/`p` references and optional `a`/`k` context. The comparison exposes how reposting redistributes an event while reacting attaches a compact signed response.
- Neither selected NIP is one of the protocol items repeated from Newsletter #37.

#### Current implementation evidence — three independent clients

All links below were live-checked and returned `HTTP 200`; repository heads were current as of the verification timestamp.

1. **Amethyst**
   - NIP-18: [`RepostEvent.kt`](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip18Reposts/RepostEvent.kt) defines the repost event type in the active Quartz protocol layer.
   - NIP-25: [`ReactionEvent.kt`](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt) defines the reaction event type in the same active protocol layer.

2. **Snort**
   - NIP-18: [`packages/system/src/impl/nip18.ts`](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip18.ts) explicitly implements NIP-18 helpers, including quote-link tag handling; `NoteCreator.tsx` consumes the implementation in the app.
   - NIP-25: [`packages/system/src/impl/nip25.ts`](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip25.ts) explicitly implements NIP-25 and creates event-reaction tags.

3. **Ditto**
   - NIP-18: [`RepostMenu.tsx`](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/components/RepostMenu.tsx) publishes generic repost kind `16`, adds the `k` tag, and adds an `a` coordinate for addressable events “per NIP-18.”
   - NIP-25: [`nostrEvents.ts`](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/lib/nostrEvents.ts) applies NIP-25 reaction semantics to kind `7`, treating the last `e` tag as the target event.

Optional tool-level corroboration (not needed to satisfy the three-client floor): `nostr-tools` exposes current [NIP-18](https://github.com/nbd-wtf/nostr-tools/blob/70eabad612205faa00604965168d0235303da135/nip18.ts) and [NIP-25](https://github.com/nbd-wtf/nostr-tools/blob/70eabad612205faa00604965168d0235303da135/nip25.ts) modules and tests.

#### Required writer constraints

- Keep the deep dive spec-first; do not frame reposts/reactions as new this week.
- Distinguish kind `6` note reposts, kind `16` generic reposts, `q`-tag quote reposts, and kind `7` reactions.
- Do not imply relay-side deletion, ranking, or universal reaction aggregation semantics that the two specs do not define.
- End with a non-exhaustive implementation paragraph using at least Amethyst, Snort, and Ditto.

### FAIL — NIP-25 + NIP-30 alternative

- The specs are directly connected: NIP-25 permits NIP-30 custom-emoji reactions, and [NIP-30](https://github.com/nostr-protocol/nips/blob/master/30.md) explicitly includes kind `7`.
- Current code exists in Amethyst, Ditto, and `nostr-tools` for both.
- Nevertheless, Newsletter #37 materially covered NIP-30’s newly merged kind-1111 change twice. Selecting NIP-30 again one issue later would violate the continuity preference when an equally implementable untouched pair exists.

**Verdict:** reject this alternative for #38; reserve it only for a later issue with a genuinely new implementation hook.

## 3. Continuity exclusions carried forward

Hard exclusions for this issue:

- **NIP-22 deep dive:** already deep-dived on 2026-08-19.
- **NIP-30 protocol update:** already covered in Newsletter #37 via PR #2448 and the August history section.
- **NIP-47 deep dive:** already deep-dived on 2026-02-04; current `max_fee` proposal is also already covered in Newsletter #37.
- **NIP-32 language-label proposal, NAP-DISPLAY, and Marmot PR #417:** already introduced in Newsletter #37 and still open/draft.

## Final handoff

- **Protocol/spec item to advance:** NWC-05 `list_transactions.total_count` only.
- **Deep-dive pair to advance:** NIP-18 + NIP-25.
- **Do not advance:** NIP-22/NIP-30 reply convergence, NWC `max_fee`, open NIPs proposals, NAP-DISPLAY, or Marmot same-account enrollment.
