# Selection Review — Nostr Compass #33

Target: 2026-07-29
Edition type: Monthly retrospective
Estimated reading time: 28–30 minutes
Triage input: 44 GREEN, 50 MAYBE, 163 SKIP; Stage 3 `GATE: PASS`

## Mechanical editorial checks

- Month-end: PASS. `2026-07-29 + 7 days = 2026-08-05`, so this is July's final Wednesday issue.
- Deep-dive override: PASS. The regular two-NIP rotation is replaced by `Six Nostr Julys`; no NIP Deep Dive candidates are selected.
- Previous issues read in full: #32 (2026-07-22), #31 (2026-07-15), and #30 (2026-07-08).
- Scoring: `R/U/B/N` means Nostr relevance (0–3), user impact (0–3), ecosystem breadth (0–2), and novelty (0–3), followed by the coverage-history bonus and documented demotions. Minimum selected score is 5/12. Lead stories score at least 8/12.
- Section isolation: each project is allocated to one content section only. Spec proposals appear only in Protocol work and NIP updates. Unreleased changes contain app/client code only.
- Immediate-prior exclusion: Amethyst is the only selected project that appeared in #32. Its distinct primary source and substantive change are recorded below. Every other #32 repeat is on SKIP.
- Discovery budget: one candidate, Hanami. No other untracked Zapstore or NIP-34-native discovery is selected.

## Section allocations

### Lead stories — 7 items

1. **Mafrend v1.0**
   - Score: **11/12** (`R2/U3/B1/N3 +2 first mention`).
   - Primary sources: [v1.0](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.0), [developer-signed release event](https://primal.net/e/02dbd9484ac8b06eb8417668fdcb89ce0671e43b19b856acd3c1a3e9f31634f4).
   - Angle: A public Android alpha turns map destinations into Nostr chat contexts. Explain what users publish to relays, how place-based discovery differs from a conventional global feed, and the limits of an early alpha.
   - Continuity: First newsletter appearance. Intake already added Mafrend to `data/projects.yml`; Stage 5 must not add it again.

2. **Hanami 0.1.0**
   - Score: **11/12** (`R2/U3/B1/N3 +2 first mention`).
   - Primary sources: [Android repository](https://github.com/Letdown2491/hanami-android), [developer-signed release event](https://primal.net/e/55c3b6223da55e98e7172d989c3a60c6763fbd584d1ee398b88e399e464cd26f).
   - Angle: The first Android companion for a Blossom server uses NIP-55 signing and a native NIP-98 session handshake, giving authenticated uploads and downloads a signer-mediated mobile path.
   - Continuity: First newsletter appearance and this issue's sole Discovery selection.

3. **Cordn Android launch**
   - Score: **9/12** (`R2/U3/B1/N3`; existing Cordn coverage, new platform category).
   - Primary sources: [Cordn repository](https://github.com/Cordn-msg/cordn-web), [0.2.1 developer-signed release event](https://primal.net/e/75ee7a79b11655c6dafd11ac71c0368933b8d3847a33cb91c74d4afc4d3243ec), [0.2.4 developer-signed release event](https://primal.net/e/81dd085540976c4d082d4797a8a1cce5adf14f0f2a4b90fda3a093fc55e54293).
   - Angle: Cordn moves from its prior web/coordinator context to a native Android client with Nostr identity onboarding, NIP-05 profile links, verified app links, and coordinator-assisted MLS group messaging. Collapse the five Zapstore rows into one launch; treat 0.2.2–0.2.4 as build fixes, not separate news.
   - Continuity: Cordn last appeared on 2026-07-01. `data/projects.yml` already contains Cordn; no addition is needed.

4. **Nostur 1.30.1**
   - Score: **8/12** (`R2/U3/B1/N2`).
   - Primary source: [Nostur 1.30.1](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.30.1).
   - Angle: Center disappearing DMs, share-sheet publishing into Nostr, nested replies, and duplicate-post protection. Separate the new messaging and publishing behavior from routine 1.30.x fixes.
   - Continuity: Returning after 2026-06-24, not an immediate-prior repeat.

5. **Formstr Drive 0.0.2**
   - Score: **10/12** (`R2/U3/B1/N3 +1 first release category`).
   - Primary source: [formstr-drive 0.0.2](https://github.com/formstr-hq/formstr-drive/releases/tag/v0.0.2).
   - Angle: A Nostr-native drive now has chunked Blossom storage, previews, authenticated deletion, and a local relay. Explain the division between relay metadata and blob storage, and distinguish the shipped app from the still-open storage proposal covered in #31.
   - Continuity: The repository has no `coverage_history.json` entry; #31 discussed the related spec proposal, not this release.

6. **Code Call 0.2.66**
   - Score: **9/12** (`R2/U3/B1/N2 +1 new routing category`).
   - Primary source: [Code Call 0.2.66](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.66).
   - Angle: Collapse 47 tags into one story about multi-worker routing over Nostr, background delivery across relays, sender-verified session isolation, attachment decryption, and catch-up requests. Do not narrate tag count or model-version churn.
   - Continuity: Last covered in #31 as Nostr Codex Phone; #32 did not cover it. This release changes routing and delivery, not the helper-command surface from #31.

7. **GitWorkshop's developer-signed release**
   - Score: **9/12** (`R2/U3/B2/N2`).
   - Primary source: [developer-signed release event](https://primal.net/e/869e01f9a74d98f468a66f3b83865d198a82cc718c1db36324398b1b88a17c60).
   - Angle: Lead with Android NIP-55 login, then explain recursive lead-maintainer coordination, independent GRASP synchronization, relay-hint preservation, and cross-repository work-item references as one NIP-34 collaboration update.
   - Continuity: Last covered in #31 for the first Android build and repo-explorer ref handling; #32 did not cover it. The selected source supports separate collaboration and synchronization behavior.

### Tagged releases — 8 items

1. **NoorNote 1.3.0**
   - Score: **8/12** (`R2/U3/B1/N2`).
   - Primary source: [NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0).
   - Angle: Live-event cards, NIP-68 image tagging, encrypted soft-mute synchronization, and relay-seen diagnostics form one client-capability release.

2. **algia 0.0.133**
   - Score: **8/12** (`R2/U3/B1/N2`).
   - Primary source: [algia 0.0.133](https://github.com/mattn/algia/releases/tag/v0.0.133).
   - Angle: Explain NIP-29 group posting, join/leave flows, image attachments, and NIP-42 relay pre-authentication. Last covered on 2026-07-08.

3. **swift-nostr 0.7.0**
   - Score: **9/12** (`R2/U3/B2/N2`).
   - Primary source: [swift-nostr 0.7.0](https://github.com/yysskk/swift-nostr/releases/tag/0.7.0).
   - Angle: Frame the breaking API around full remote-signer coverage, NIP-29 groups, NIP-98 HTTP authentication, and strict NIP-44 vectors for Swift clients.

4. **lawallet-nwc 2.0.0**
   - Score: **9/12** (`R2/U3/B2/N2`).
   - Primary source: [lawallet-nwc 2.0.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.0.0).
   - Angle: Passkeys derive Nostr keys client-side, multiple pubkeys can link to one account, and a standalone NWC relay bridge adds delivery guarantees. Keep non-Nostr wallet details out.

5. **MDK 0.9.9**
   - Score: **9/12** (`R2/U3/B2/N2`).
   - Primary source: [MDK 0.9.9](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.9).
   - Angle: Manual pin order persists, terminal group disbanding closes a Marmot lifecycle gap, and rich inbound context gives Marmot agents a stable interface. Last covered in #31, not #32.

6. **pakstr 0.3.1**
   - Score: **11/12** (`R2/U3/B1/N3 +2 first mention`).
   - Primary source: [pakstr 0.3.1](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.3.1).
   - Angle: Use the canonical `stuff/pakstr` source, not the stale fetch key. Cover Amber signing, NIP-44 encryption, Android permission injection, and runtime-configurable API proxying as an app-shell release.

7. **Ditto 2.34.1**
   - Score: **9/12** (`R2/U3/B1/N2 +1 returning after more than six issues`).
   - Primary source: [Ditto 2.34.1](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.34.1).
   - Angle: NIP-5A root-site links extend the client surface by opening an author's published website from their profile.
   - Stage 5 source correction: The NIP-38 rendering commit landed after the v2.34.1 tag, and the legacy-commerce removal landed before it. Neither belongs to this tagged-release item.

8. **Earthly 0.0.9**
   - Score: **8/12** (`R2/U3/B1/N2`).
   - Primary source: [Earthly 0.0.9](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.0.9).
   - Angle: Treat this as the first tracked release of a collaborative spatial-research client backed by Nostr. Include repaired zaps, remote wallet connections, and Nostr entity actions only where the release source supports them.

### Unreleased app/client changes — 5 items

1. **Amethyst: relay-refusal recovery and per-account state**
   - Score: **6/12** (`R2/U1/B2/N2 +1 new category -2 recent substantial coverage`).
   - Primary sources: [PR #3747](https://github.com/vitorpamplona/amethyst/pull/3747), [PR #3757](https://github.com/vitorpamplona/amethyst/pull/3757), [PR #3755](https://github.com/vitorpamplona/amethyst/pull/3755).
   - Angle: Lead with NIP-77 negentropy no longer stalling when a relay refuses via NOTICE; add NIP-84 quote rendering and per-account synced bottom-bar state as a compact second thread.
   - Immediate-prior continuity source: **https://github.com/vitorpamplona/amethyst/pull/3747**.
   - Immediate-prior substantive change: **A relay refusal now terminates the affected NIP-77 negentropy path instead of leaving synchronization stalled. #32 covered pre-release napplet QA, Desktop polls, search ranking, and relay-store performance, not this refusal recovery.**

2. **Imwald Android: offline/outbox publishing**
   - Score: **9/12** (`R2/U1/B1/N3 +2 first mention`).
   - Primary source: [commit f4de9f6](https://git.imwald.eu/silberengel/imwald-android/commit/f4de9f61df35110c77d2e5f99d764c0df176962b).
   - Angle: Explain how the client repairs offline/outbox publication and loads referenced feed and thread events in the background. This is user-submitted intake, not the Discovery slot.

3. **Zap Cooking: encrypted scheduled publishing and scanner authentication**
   - Score: **7/12** (`R2/U1/B1/N2 +1 new publishing category`).
   - Primary sources: [PR #566](https://github.com/zapcooking/frontend/pull/566), [PR #569](https://github.com/zapcooking/frontend/pull/569), [PR #599](https://github.com/zapcooking/frontend/pull/599).
   - Angle: Cluster the week into two threads: encrypted-at-rest scheduled Nostr posts broadcast by a minutely sweep, and a fridge scanner that now binds NIP-98 authentication to the exact request body instead of trusting a supplied pubkey.

4. **Citrine: managing and rebroadcasting from an Android relay**
   - Score: **7/12** (`R2/U1/B1/N2 +1 returning project/new capability`).
   - Primary sources: [PR #179](https://github.com/greenart7c3/Citrine/pull/179), [PR #150](https://github.com/greenart7c3/Citrine/pull/150), [PR #178](https://github.com/greenart7c3/Citrine/pull/178), [PR #174](https://github.com/greenart7c3/Citrine/pull/174).
   - Angle: A local Android relay can rebroadcast stored events externally, expose NIP-86 management, administer NIP-29 groups through Amber, and keep Tor lifecycle state coherent.

5. **Wired: complete browser traversal with relay hints**
   - Score: **6/12** (`R2/U1/B1/N2`).
   - Primary sources: [PR #148](https://github.com/smolgrrr/Wired/pull/148), [PR #147](https://github.com/smolgrrr/Wired/pull/147), [PR #146](https://github.com/smolgrrr/Wired/pull/146), [PR #145](https://github.com/smolgrrr/Wired/pull/145), [PR #144](https://github.com/smolgrrr/Wired/pull/144).
   - Angle: Complete snapshot, feed, and thread traversal plus restored relay hints changes what users can recover and follow through the browser. Cover Wired only; the stale TAO alias must not create a second header.

### Protocol work and NIP updates — 6 items

**Merged**

1. **NIP-34 removes GRASP hosting instructions from pull-request semantics**
   - Score: **5/12** (`R3/U1/B2/N1 -2 documentation-only demotion`).
   - Primary source: [PR #2423](https://github.com/nostr-protocol/nips/pull/2423), verified merged 2026-07-26.
   - Angle: Explain the boundary change: NIP-34 retains the event semantics for pull requests while removing instructions tied to one hosting implementation. Keep it concise because no wire shape changes.

**Open proposals**

2. **Mutual key-set declarations**
   - Score: **9/12** (`R3/U1/B2/N3`).
   - Primary source: [PR #2424](https://github.com/nostr-protocol/nips/pull/2424), verified open as “Add NIP-A1: Key Set Declaration (kind 10045).”
   - Angle: Kind 10045 proposes reciprocal links between keys so clients merge identities only after both sides declare the relationship. Describe without presenting the provisional NIP label as canonical.

3. **BOLT12 zaps**
   - Score: **9/12** (`R3/U1/B2/N3`).
   - Primary source: [PR #2421](https://github.com/nostr-protocol/nips/pull/2421), verified open.
   - Angle: Signed Nostr zap intents bind BOLT12 payment proofs and let clients verify settlement without depending on a recipient-operated receipt publisher. Explain the proposed intent/proof flow from the diff.

4. **NIP-59 standalone seal rejection**
   - Score: **8/12** (`R3/U1/B2/N2`).
   - Primary source: [PR #2399](https://github.com/nostr-protocol/nips/pull/2399), verified open.
   - Angle: Relays would reject standalone kind 13 seals because valid seals exist only inside kind 1059 gift wraps, reducing protocol-invalid storage and metadata leakage.

5. **One-time device pairing**
   - Score: **8/12** (`R3/U1/B2/N3 -1 no merged spec or cited implementation`).
   - Primary source: [PR #2328](https://github.com/nostr-protocol/nips/pull/2328), verified open as “NIP-AB: Device Pairing.”
   - Angle: Walk the QR bootstrap, ephemeral ECDH, comparison code, NIP-44 channel, and encrypted secret payload. Describe without treating the provisional label as canonical.

6. **Transient private location sharing**
   - Score: **8/12** (`R3/U1/B2/N3 -1 early proposal`).
   - Primary source: [PR #2309](https://github.com/nostr-protocol/nips/pull/2309), verified open as “NIP-TPLD: Transient Private Location Data.”
   - Angle: Explain ephemeral encrypted geohashes for selected recipients, expiration and relay-observer limits, and the privacy tradeoffs. Describe without treating the provisional label as canonical.

## Month-end section — Six Nostr Julys

- Score: **10/12 editorial value** (`R3/U2/B2/N3`).
- Required title: **Six Nostr Julys**.
- Coverage span: July 2021 through July 2026. Do not add two NIP Deep Dives.
- Structure: one chronological subsection per year. Each subsection must establish the prior state, the verified July change, and the capability or coordination problem it introduced or resolved. Use direct primary sources, not later summaries, and avoid repeating projects selected elsewhere in this issue.

### July-history research brief

1. **July 2021: NIP-05 reaches the early JavaScript toolchain.**
   - Primary source: [nostr-tools commit 1ce00bd](https://github.com/nbd-wtf/nostr-tools/commit/1ce00bd3b6909f78f212a7a172cf845b55280599).
   - Research angle: The dedicated NIPs repository had no July 2021 commits. Read the commit and surrounding `nostr-tools` history to explain how domain-to-pubkey verification entered an early client library before Nostr had a broad application market. Do not infer behavior from the one-word commit subject alone.

2. **July 2022: reactions become a protocol event.**
   - Primary source: [NIP-25 introduction commit](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88), with [downvote follow-up](https://github.com/nostr-protocol/nips/commit/89bb08ba8683).
   - Research angle: Explain the move from notes/follows toward interoperable social actions, the kind 7 reaction shape, and how the immediate follow-up generalized positive and negative reactions.

3. **July 2023: live activities and classified listings widen the application model.**
   - Primary sources: [NIP-53 commit](https://github.com/nostr-protocol/nips/commit/141197c564d97073f0293e3b2f367f0b6b3619c2), [initial classified-listing draft](https://github.com/nostr-protocol/nips/commit/451c06a3c572a13afe45c1d80616f8e6dd9bb1de).
   - Research angle: Contrast live events and chat coordination with addressable marketplace listings. Verify the final NIP-99 numbering and later tag edits before describing the classified draft's lasting shape.

4. **July 2024: protected events and deterministic tie ordering tighten relay/client behavior.**
   - Primary sources: [NIP-70 protected-event commit](https://github.com/nostr-protocol/nips/commit/ae1906ec7943a6bd756f05d2cd2fb2a041398921), [NIP-01 event-ordering commit](https://github.com/nostr-protocol/nips/commit/9c54549f1842245b842d8a66f3bade744da24189).
   - Research angle: Explain the `-` tag's author-only relay acceptance contract, then show why sorting equal-`created_at` events by id removes cross-client ambiguity.

5. **July 2025: voice messages and NWC negotiation/state.**
   - Primary sources: [NIP-A0 Voice Messages commit](https://github.com/nostr-protocol/nips/commit/e50f37a527ace39cc3057827d52295c6b6de1112), [NWC NIP-44 negotiation commit](https://github.com/nostr-protocol/nips/commit/f30a43bd37e08516923b96dd0d860122c9ffe04e), [NIP-47 transaction-state commit](https://github.com/nostr-protocol/nips/commit/0595d438aaa163dd33ed00748026698a411a0861).
   - Research angle: Pair a media-specific message format with NWC's move toward explicit encryption negotiation and transaction state. Verify current numbering because the voice-message label is alphanumeric.

6. **July 2026: relay-group coordination matures and corrects itself.**
   - Primary sources: [NIP-29 subgroups PR #2319](https://github.com/nostr-protocol/nips/pull/2319), [message-pinning PR #2379](https://github.com/nostr-protocol/nips/pull/2379), [addressable-pin follow-up #2416](https://github.com/nostr-protocol/nips/pull/2416), [favorite-follow-sets PR #2413](https://github.com/nostr-protocol/nips/pull/2413), [renumbering PR #2417](https://github.com/nostr-protocol/nips/pull/2417).
   - Research angle: Use the month to show two forms of protocol maturation: NIP-29 gaining hierarchy and ordered pin state, and NIP-51 correcting a kind collision before broad deployment. Keep this historical synthesis separate from the current-week Protocol section.

## Discovery slot

- Selected candidate: **[Hanami](https://github.com/Letdown2491/hanami-android)** (`source: Zapstore`).
- Score: **11/12**.
- Why it qualifies: A working first release adds an Android NIP-55/NIP-98 client for authenticated Blossom server sessions, with developer-signed release metadata and install artifacts.
- Newsletter placement: Lead stories.
- `data/projects.yml` addition needed: **YES**, under the existing storage/client-compatible category chosen by Stage 5 after checking neighboring entries. Stage 4 does not edit it.
- Other discovery candidates: not selected. Mafrend came through Intake and is already tracked; Cordn is already tracked despite the Zapstore URL mismatch; all NIP-34-native launch candidates remain on SKIP.

## Topic pages needed or updated

### Create in Stage 5

- `content/en/topics/nip-25.md` — needed for the July 2022 reaction milestone; primary source is the [introduction commit](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88).
- `content/en/topics/nip-68.md` — needed for NoorNote's image tagging; primary specification: [68.md](https://github.com/nostr-protocol/nips/blob/master/68.md).

### Update Mentioned-in and current implementation/source notes in Stage 5

- `blossom.md`, `nip-55.md`, and `nip-98.md` for Hanami and Formstr Drive.
- `nip-05.md` for Cordn and the July 2021 history subsection.
- `nip-17.md`, `nip-44.md`, `nip-46.md`, and `nip-59.md` for selected messaging, signing, NWC, and gift-wrap work.
- `nip-29.md`, `nip-42.md`, and `nip-86.md` for algia, Citrine, and the July 2026 history subsection.
- `nip-50.md`, `nip-77.md`, and `nip-84.md` for Ditto, Amethyst, and library/client changes.
- `nip-53.md`, `nip-70.md`, `nip-01.md`, `nip-47.md`, `nip-51.md`, and `nip-99.md` for the July-history section.
- Do not create topic pages under provisional labels from PRs #2424, #2328, or #2309. Cite the PRs and describe the proposals without canonicalizing their draft labels.

## SKIP list — all remaining GREEN/MAYBE candidates

### Immediate-prior issue repeats rejected

- **[Wisp 1.2.1](https://github.com/barrydeen/wisp/releases/tag/v1.2.1)** — **4/12**. Distinct source and crash-safe malformed-image handling exist, but one narrow patch cannot support two substantive sentences after #32's 1.2.0 coverage.
- **[Buzz Desktop 0.4.26](https://github.com/block/buzz/releases/tag/v0.4.26)** — **5/12**. Community administration and relay recovery are distinct from #32's Armada/Buzz workspace story, but seven rapid patches lack one bounded, release-level user story.
- **[Sonar alpha.12](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.12)** — **5/12**. Durable Marmot backup and retryable sending are new, but this is the third consecutive issue in the alpha line and the incremental follow-up demotion applies.
- **[Divine Mobile PR #6368](https://github.com/divinevideo/divine-mobile/pull/6368)** — **5/12**. Rejecting forged rumor fields and unsigned seals is distinct security work, but #32 gave Divine a full release paragraph and this single unreleased fix loses the slot to Amethyst's broader repeat exception.
- **[nostr-pubsub TypeScript 0.5.5](https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.5)** — **4/12**. Exact-object verification reuse is a distinct source-level change, but it is a narrow internal boundary directly after #32's launch treatment.
- **[Nostrord 2.4.0](https://github.com/nostrord/nostrord/releases/tag/v2.4.0)** — **6/12**. Subgroup channels and socket recovery are substantive, but Nostrord led #32 and has appeared in three consecutive issues; hold until the next broader release.
- **[Shopstr PR #574](https://github.com/shopstr-eng/shopstr/pull/574)** — **5/12**. Merchant follows now publish kind 3 contact lists, but the surrounding week is Cashu/tests and #32 already covered Shopstr's payment-integrity work.
- **[nostream PR #706](https://github.com/Cameri/nostream/pull/706)** — **5/12**. Authenticated live settings editing and rejection errors are new, but #32 covered nostream and its relay access stack in both unreleased and Deep Dive sections.
- **[Armada developer-signed release](https://primal.net/e/aead1dc1f55793a91a332cb006e2461c210e01067d212e3bb969a0f6514929a8)** — **6/12**. Authenticated DM-relay fetches and non-forking Concord key rotation are distinct, but Armada had a full #32 release section and another consecutive slot would crowd stronger launches.
- **[IndieSats developer-signed release](https://primal.net/e/57a9d4e732e32524d5c2ac04d5d0791f9acac645fff485e579d80943a2d602d6)** — **5/12**. Native music-event formatting and corrected relay delivery are distinct, but #32's lead already covered the relaunch and its July 21 publication-format update.
- **[Wisp iOS PR #423](https://github.com/barrydeen/wisp-ios/pull/423)** — **4/12**. The tapped-note replacement fix is narrow and belongs to the same project family covered in #32.
- **[Dark Wisp 1.2.1](https://github.com/barrydeen/dark-wisp-android/releases/tag/v1.2.1)** — **5/12**. Collapsible threads and crash-safe images are credible, but the project/flavor relationship to Wisp is unresolved; selecting it risks duplicating #32 under another package name.
- **[Zapstore webapp commit c5d4e5e](https://github.com/zapstore/webapp/commit/c5d4e5e479e48dd3899ae58ebea41c87d5aa3e8f)** — **4/12**. Direct downloads improve access, but the chain includes reverted approaches and #32 already led with Zapstore 1.1.0.
- **[NIP-47 core simplification PR #2419](https://github.com/nostr-protocol/nips/pull/2419)** — **4/12**. Same PR and same proposal already explained in #32; no distinct source or substantive delta.
- **[Sandboxed web applets PR #2303](https://github.com/nostr-protocol/nips/pull/2303)** — **4/12**. Same PR and sandbox model already explained in #32; no distinct source or substantive delta.
- **[AND filters PR #2252](https://github.com/nostr-protocol/nips/pull/2252)** — **4/12**. Same PR and server-side tag-intersection proposal already explained in #32; no distinct source or substantive delta.

### Other unselected GREEN/MAYBE items

- **[Chama 5.6.0](https://github.com/jesuspirate/chama/releases/tag/v5.6.0)** — **7/12**. Relay-redelivery bounds and Nostr work offers pass scope, but release slots favor broader client and interoperability changes.
- **[Elisym SDK 0.30.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/sdk%400.30.0)** — **6/12**. Verified identities and agent messaging are relevant, but ten package tags do not yet establish a clear user-facing launch.
- **[CodeDeck 2026.07.25](https://github.com/JeroenOnNostr/codedeck/releases/tag/v2026.07.25)** — **5/12**. Startup and buffered-first-message improvements are useful, but model-version support dominates the release.
- **[Horcrux 0.9.3+2](https://github.com/mplorentz/horcrux/releases/tag/v0.9.3-2)** — **5/12**. Fail-closed SQLCipher checks protect signer shares, but this is a pre-release APK with no release narrative.
- **[Bark 1.3.5](https://github.com/forgesworn/bark/releases/tag/v1.3.5)** — **5/12**. Approval UX is clearer, but provisional event kinds and limited depth keep it below selected releases.
- **[Angor 0.2.34](https://github.com/block-core/angor/releases/tag/v0.2.34)** — **7/12**. Nostr investment-state sync passes scope, but the Bitcoin-heavy release loses a slot to Nostr-native apps.
- **[Auditable Voting 0.1.157](https://github.com/tidley/auditable-voting/releases/tag/v0.1.157)** — **7/12**. Race-safe approval and ballot delivery are meaningful, but the same project appeared in #31 and stronger releases fit the depth budget.
- **[Napplet Vite plugin 0.12.0](https://github.com/napplet/web/releases/tag/%40napplet/vite-plugin%400.12.0)** — **6/12**. Convention identities and attested intent delivery are relevant, but draft-protocol maturity and monorepo churn lower confidence.
- **[Bitchat merged work](https://github.com/permissionlesstech/bitchat/pull/1486)** — **5/12**. Nostr-envelope and relay-signature checks are real, but mesh work dominates and the Nostr thread lacks section depth.
- **[Conduit PR #217](https://github.com/Conduit-BTC/conduit-mono/pull/217)** — **5/12**. NIP-46 signing and [encrypted marketplace DMs](https://github.com/Conduit-BTC/conduit-mono/pull/181) pass scope, but Conduit had a full #31 section and recent-coverage demotion applies.
- **[Paygress PR #80](https://github.com/DhananjayPurohit/Paygress/pull/80)** — **7/12**. Paid sandbox execution for ngit CI is novel, but evidence is concentrated in one merged PR and loses the infrastructure slot to GitWorkshop.
- **[Pensieve PR #37](https://github.com/andotherstuff/pensieve/pull/37)** — **7/12**. Archive recovery and evidence preservation are valuable, but analytical infrastructure loses the slot to user-facing apps.
- **[Kehto PR #204](https://github.com/kehto/web/pull/204)** — **5/12**. CSP and napplet conformance improve safety, but documentation/conformance work dominates the sampled set.
- **[rust-nostr PR #1393](https://github.com/nostrdevkit/nostr/pull/1393)** — **7/12**. NIP-44 v2 for NWC and embedded-relay kind blacklists pass scope, but unreleased library work is excluded from the app/client-only section.
- **[NIP-B0 ambiguity PR #2425](https://github.com/nostr-protocol/nips/pull/2425)** — **4/12**. The body points outside the PR and does not establish a concrete protocol delta.
- **[Scoped data grants PR #2411](https://github.com/nostr-protocol/nips/pull/2411)** — **5/12**. Concrete encrypted-record and revocation design, but the same PR received full treatment in #31 and has no new implementation source.
- **[Agent passports PR #2378](https://github.com/nostr-protocol/nips/pull/2378)** — **5/12**. Broad NIP-90 extension, but noncanonical citations and excessive surface prevent a bounded update.
- **[NIP-58 badge workflow PR #2204](https://github.com/nostr-protocol/nips/pull/2204)** — **5/12**. Request/denial events are concrete, but no implementation evidence and no current-window merge.
- **[Push-notification proposal PR #2194](https://github.com/nostr-protocol/nips/pull/2194)** — **6/12**. Calling-client implementations make it relevant, but the assigned label remains noncanonical and stronger protocol proposals fill the section.
- **[Encrypted medical records PR #357](https://github.com/nostr-protocol/nips/pull/357)** — **5/12**. The FHIR/consent model is concrete, but this long-running draft lacks current implementation evidence.
- **[Barattolo 1.3](https://barattolo.store)** — **4/12**. A thin NIP-99 website wrapper without a direct implementation repository fails the source/depth threshold.
- **[ngit external-helper commit](https://codeberg.org/DanConwayDev/ngit-cli/commit/d5337a83d12e343f129e37927eaff79174d88f84)** — **7/12**. Remote-helper delegation and graph-walk preservation are useful, but GitWorkshop takes the NIP-34 tooling slot.
- **[Ditto Relay aggregation fix](https://gitlab.com/soapbox-pub/ditto-relay/-/commit/ed038d182d95d6f57e391f9b2ef277e2f27f12ed)** — **5/12**. NIP-85 aggregation cost improves, but no benchmark establishes operator impact.
- **[Nostrify IndexedDB 0.2.0](https://gitlab.com/soapbox-pub/nostrify/-/tags/%40nostrify%2Findexeddb%400.2.0)** — **7/12**. Browser-side NIP-50 search is substantive, but release slots favor complete user applications and signer/interoperability work.
- **[Pollerama release event](https://primal.net/e/d4730768cdcefb4ba072c29d036dd8fbb4d194ac2e2a3512ed1e1f7bbcd464c1)** — **6/12**. Relay-published runs and restored follow state are useful, but cumulative multi-version notes and untracked status weaken the unit.
- **[SkateSpots release event](https://primal.net/e/a05f00668750570828aaa87e8ba3632dcecf2ef86cd5f25e8972c85543ce4f1a)** — **5/12**. Spot-status consensus and Amber fixes pass scope, but old repeated release notes obscure the current delta.
- **[Logbook announcement](https://primal.net/e/67fa9de440ee190a197905180f12b9e77ca3da3f9bac91a6457827998a99ca9e)** — **6/12**. Nostr voice-podcast collaboration is in scope, but the announcement alone lacks release evidence; Hanami uses the sole Discovery slot.
- **[gittr launch announcements](https://primal.net/e/40a49288339ab3a1aa13408889129c32dc6f74a09ae5b300f23a185497d7c6b6)** — **7/12**. The forge family is broad, but five related repositories need implementation-level validation and would overrun the one-project/header rule.
- **[scored-relay announcement](https://primal.net/e/dabc63be99236dde59f91036b295661881a17f64dff68588c1fb7b146736506b)** — **6/12**. PoW/recency bounded storage is novel, but announcement-only evidence incurs the no-working-release demotion.
- **[drydock announcement](https://primal.net/e/9d335862987eb67c1b28b234c6d0bbb236a4e027261eb44e0e56786f14db9dd1)** — **5/12**. NIP-34 code review passes scope, but no shipped implementation details.
- **[grasp-ci announcement](https://primal.net/e/c4688ae00627a56227a3a20aa1ec0368ee04c7232a6a6e8406b05a3a13b0b646)** — **6/12**. Reproducible CI for GRASP repositories is relevant, but announcement-only evidence and the Discovery cap exclude it.
- **[marmot-openclaw announcement](https://primal.net/e/ad6ad80aea70fe943b0df4465a2d629764ddc298e9aa84c3c37474e100edbf3f)** — **6/12**. Per-group session-key isolation is relevant, but a repository announcement is insufficient to prove a shipped plugin release.
- **[Nostr Glasses announcement](https://primal.net/e/da4737019af5cacfe3002234de079f94123323b40e632bc5aa81b014cb409c6f)** — **4/12**. No implementation detail or release evidence.
- **[Budabit widget announcements](https://primal.net/e/0d60243499f7d3af5da70922e097ac8b9c0a391a7be1561abbe1442cff26da97)** — **5/12**. Four smart-widget concepts are relevant, but implementation evidence is thin and one proposed label is noncanonical.
- **[nosnap announcement](https://primal.net/e/98ec39e5547d5fdeffd35b54721772134b40cd86e5cc1c164e9dc5e557a31e2f)** — **4/12**. Photo publishing is in scope, but no release notes or protocol detail.
- **[zapthreads-codonaft announcement](https://primal.net/e/fb6f3d6fe044c7368741ba844b50e05d5b25306746c05beda93b62622f05eb81)** — **4/12**. The source cannot separate new voting/moderation work from inherited fork behavior.
- **[tclnostr announcement](https://primal.net/e/d133147f9b6ac9761f2f19e5f0b6fc9f662b301216787843900dc836208eef00)** — **4/12**. No supported-NIP list, API surface, or release state.
- **[nos_pico announcement](https://primal.net/e/e0ae4538f9d90f212948a4633e3161e0b91937ca558a72b623ae78fa425e2072)** — **4/12**. Signing hardware is relevant, but the threat model and firmware evidence are absent.
- **[Clestr announcement](https://primal.net/e/ca4dfbecff3bfed88770fbd223dd9ffde607bf1d329efe60797d75286b21ab2c)** — **4/12**. No shipped behavior is documented.
- **[continuum-identity-workspace announcement](https://primal.net/e/32134bd9df063bcbd180e1c6ce8d6b078d5873b83c6fe8e270cf713a2e29b14a)** — **4/12**. Multi-identity management lacks a key-isolation model.
- **[nostrd announcement](https://primal.net/e/4257dc80745651e82c795d7a4cfdc3dadf0ce72b6641540220f88c8d1ece3f7a)** — **4/12**. No differentiated relay behavior.
- **[broadcastr announcement](https://primal.net/e/c5ce58feb4694b0818360d79541970803a2df8046aff3996c1ab8f54796527b2)** — **4/12**. Forwarding policy, loop prevention, and release evidence are absent.
- **[asymmetric-vanity-npubs announcement](https://primal.net/e/31afd64084bd6f457a63438b9ad8bffeead0028b4b03b1277fb2258cbeb18743)** — **4/12**. The offset-sale model needs a security review before promotion.
- **[Pyramid 1.3.1](https://github.com/fiatjaf/pyramid/releases/tag/v1.3.1)** — **4/12**. Community-stat fix is too small and the forge open-kinds work closed unmerged.
- **[ZSP 0.4.15](https://github.com/zapstore/zsp/releases/tag/v0.4.15)** — **7/12**. Certificate/private-key proof validation is substantive, but the developer-tool release loses the slot to GitWorkshop and pakstr.
- **[LumiLumi PR #1082](https://github.com/TsukemonoGit/lumilumi/pull/1082)** — **4/12**. A merged emoji menu is modest UI work below the depth threshold.
- **[44Billion commit 44ea149](https://github.com/44Billion/44billion/commit/44ea14990184454f2bc743a98b80b85ab5662fe4)** — **5/12**. Event-store access and vault migration are relevant, but one commit lacks release context and a primary impact narrative.
- **[MOAR PR #32](https://github.com/barrydeen/moar/pull/32)** — **5/12**. Custom Blossom base URLs are relevant, but the PR remains open and has no shipped release.
- **[nsite gateway PR #26](https://github.com/hzrd149/nsite-gateway/pull/26)** — **5/12**. Root-host routing is useful, but the same open PR spans duplicate repos and has no release.
- **[44b-vault commit ae97849](https://github.com/44Billion/44b-vault/commit/ae97849ed11c62bdec463fd4851a9aa59e116c6e)** — **5/12**. Vault-backup routing affects recovery, but a single commit provides insufficient release context.
- **[Notedeck PR #1494](https://github.com/damus-io/notedeck/pull/1494)** — **6/12**. NIP-51 bookmark publication and a bookmark column are substantive, but the PR remains open.
- **[llama.garden](https://github.com/etemiz/llama.garden)** — **7/12**. Signed relay events for model torrents and Blossom viewer builds pass scope, but Hanami takes the sole Discovery slot and has a developer-signed release with clearer user impact.

## Self-approval

Selection is self-approved under the continuous kanban instruction. All 94 GREEN/MAYBE candidates are either allocated once or listed on SKIP. The month-end override, immediate-prior exclusion, discovery cap, direct-source requirement, and app/spec section boundaries pass.

GATE: PASS