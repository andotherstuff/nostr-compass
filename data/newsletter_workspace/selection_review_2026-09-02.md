# Stage 4 selection review — Newsletter #38 (2026-09-02)

Selection is Sol-owned and based on `triage_2026-09-02.md`, `coverage_history.json`, complete reading of Newsletters #35–#37, and four independent Sol review passes over tracked updates, discovery feeds, protocol/deep-dive eligibility, and editorial balance. This artifact is the complete writing brief for Stage 5. It authorizes no publication action.

## Editorial frame

Newsletter #38 is a regular issue. Its through-line is **interoperability hardening from relay admission through synchronization, signed events, direct messages, wallets, and app publication**. Recent projects return only for exact new sources supporting distinct behavior; repeated Newsletter #37 sources are excluded.

## Selected: Top Stories

1. **nostream expands relay-side DVM routing and authenticated operation** — Score: 10
   - Sources: https://github.com/cameri/nostream/pull/737, https://github.com/cameri/nostream/pull/734, https://github.com/cameri/nostream/pull/716, and https://github.com/cameri/nostream/pull/730
   - Explain NIP-89 handler discovery, NIP-90 job ingestion/worker dispatch, NIP-42 session tracking, and NIP-98 admin authorization as separate relay boundaries. Do not re-cover PR #709 from Newsletter #37.

2. **NDK for Dart fixes negentropy, multi-relay request lifetimes, and signature verification** — Score: 9
   - Sources: https://github.com/relaystr/ndk/pull/722, https://github.com/relaystr/ndk/pull/705, and https://github.com/relaystr/ndk/pull/726
   - Treat `relaystr/dart_ndk` and `relaystr/ndk` as one project. Explain the observable synchronization and event-validation failures these changes prevent.

3. **Divine Mobile makes wrapped direct-message deletion and signing deterministic** — Score: 9
   - Sources: https://github.com/divinevideo/divine-mobile/pull/8174, https://github.com/divinevideo/divine-mobile/pull/8173, https://github.com/divinevideo/divine-mobile/pull/8164, https://github.com/divinevideo/divine-mobile/pull/8163, and https://github.com/divinevideo/divine-mobile/releases/tag/1.0.22
   - Limit the story to signed/wrapped Nostr DM creation and deletion; omit the repository's generic UI and product batch.

4. **Conduit Relay hardens its NIP-42 protected inbox** — Score: 8
   - Source: https://github.com/Conduit-BTC/conduit-relay/pull/8
   - Explain what authentication now gates and why protected-inbox behavior matters. Do not substitute similarly numbered changes from another Conduit repository.

5. **Amethyst ships NIP-84 highlights and fixes two relay-facing failure paths** — Score: 8
   - Sources: https://github.com/vitorpamplona/amethyst/releases/tag/v1.14.0, https://github.com/vitorpamplona/amethyst/pull/3983, and https://github.com/vitorpamplona/amethyst/pull/3987
   - The release itself and these two changes were held from Newsletter #37, so they are not duplicate coverage. Center NIP-84 highlights, trusted-list NIP-50 search, and visible NWC refusal handling. Omit PR #3991, which Newsletter #37 covered in depth, plus translations, icons, IME, PDF, and generic UI work.

6. **Mostro validates signed orders before expensive work and preserves order audit events** — Score: 8
   - Sources: https://github.com/MostroP2P/mostro/releases/tag/v0.18.5, https://github.com/MostroP2P/mostro/pull/892, https://github.com/MostroP2P/mostro/pull/924, and https://github.com/MostroP2P/mostro/pull/830
   - Cover only the Nostr-carried order, audit, and escrow state. Do not generalize this into a claim that all marketplace abuse or escrow risk is solved.

## Selected: Tagged Releases

1. **MDK v0.9.15** — Score: 8 — https://github.com/marmot-protocol/mdk/releases/tag/v0.9.15 plus https://github.com/marmot-protocol/mdk/pull/1516, https://github.com/marmot-protocol/mdk/pull/1550, https://github.com/marmot-protocol/mdk/pull/1551, and https://github.com/marmot-protocol/mdk/pull/1559. Explain final-send deduplication, newest valid KeyPackage selection, membership activity, and epoch-divergence handling as group-state durability work.
2. **Nostr Java v2.0.8** — Score: 7 — https://github.com/tcheeric/nostr-java/releases/tag/v2.0.8. Cover subscription routing and NIP-44 v2 vectors; use the Nostr Recap event only as corroboration, not primary proof.
3. **pakstr v0.16.0** — Score: 7 — https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0 plus pull requests 63, 64, 65, and 67 in the same repository. Continue from Newsletter #37 only with these distinct new sources: Blossom digest correctness, publish ordering, publisher validation, and kind-32267 identifier generation.

No release receives fewer than two substantive sentences. Drop it rather than pad it if full release-note review cannot establish reader impact.

## Selected: Notable Changes

1. **ZapCooking scopes NIP-46 bunker relays and protects a NIP-98 endpoint** — Score: 7 — https://github.com/zapcooking/frontend/pull/633 and https://github.com/zapcooking/frontend/pull/630.
2. **nostrord repairs wrapped-DM and multi-device interoperability after v2.9.0** — Score: 7 — https://github.com/nostrord/nostrord/pull/297, https://github.com/nostrord/nostrord/pull/295, https://github.com/nostrord/nostrord/pull/292, and https://github.com/nostrord/nostrord/pull/293. Frame these as new follow-up fixes after Newsletter #37's v2.9.0 coverage; do not repeat that release's old features.


## Selected: Newly Discovered

1. **Napstr v0.2.0** — Score: 10 — https://github.com/lnbits/napstr/releases/tag/v0.2.0, https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0, and https://github.com/lnbits/napstr. Describe Nostr catalogue and seeder discovery, NIP-C7 discussion, NIP-17 private negotiation, Tor transfer, audiobook/Napstrfy support, and handshake/download hardening from the canonical repository and comparison. This is a verified in-window release and first Compass introduction, not a proven first-ever launch.

RSSNotes is a backup compact tracked-project update, not discovery. All returned owner siblings and NIP-89 rows failed the verified in-window shipping gate. The first-run Zapstore baseline proves no weekly delta.

## Selected: Protocol and Spec Work

- **Nostr Wallet Connect transaction totals:** https://github.com/nostr-wallet-connect/nwc/pull/4, https://github.com/nostr-wallet-connect/nwc/commit/ff3e49a47d040075edc46ee42fc0e33f10f1ef67, and https://github.com/nostr-wallet-connect/nwc/commit/06315e735f744b1afd3df0b57436fdce8a7bfc2e. Cover only merged NWC-05 optional `list_transactions.total_count`, including that the count excludes pagination.

Do not advance NIP-22/NIP-30 reply convergence, NWC `max_fee`, NIP-32 language labels, NIP-51 static-site curation, NIP-10 kind-1111 preferences, NAP-DISPLAY, or Marmot same-account enrollment. The first two groups were materially covered in Newsletter #37; the remaining behavior is open or draft.

All seven spec families were checked. BUDs, Gamma, and Concord were quiet. NAP-DISPLAY and Marmot same-account enrollment were already selected as proposals in Newsletter #37 and remain omitted unless writing-stage readback establishes a new status or distinct source.

## Selected: NIP Deep Dive

- **Primary: NIP-18 — Reposts** — https://github.com/nostr-protocol/nips/blob/master/18.md
- **Secondary: NIP-25 — Reactions** — https://github.com/nostr-protocol/nips/blob/master/25.md
- **Connection:** NIP-18 redistributes existing events through kind 6 note reposts, kind 16 generic reposts, and `q`-tag quotes, while NIP-25 attaches signed kind-7 reactions. Both are merged canonical optional NIPs and neither has been used as a prior NIP Deep Dive.
- **Implementation floor:** cite at least Amethyst's pinned `RepostEvent.kt` and `ReactionEvent.kt` at `d06b83bd53c510e589d5ce13d46f6bd1a8206394`, Snort's `nip18.ts` and `nip25.ts` at `8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95`, and Ditto's `RepostMenu.tsx` and `nostrEvents.ts` at `570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade`.
- **Writing boundary:** keep the dive spec-first, distinguish repost and reaction event kinds precisely, and do not present either NIP as newly merged this week.

## Explicit omissions

- Shopstr PRs #436, #437, #601, and #616: exact sources already covered in Newsletter #37.
- Prior nostream source PR #709: exact source already covered in Newsletter #37.
- NAP-DISPLAY PR #97 and Marmot PR #417: already selected in Newsletter #37 and no independently verified new status is established here.
- Infans release history: timestamp anomaly remains unresolved; do not turn historical tags into current-week claims.
- 0xchat PR #76, RSSNotes, Iris Drive, and other MAYBE entries: hold unless the discovery reviewer establishes an exact in-window source and enough substance for two sentences.
- First-run Zapstore records: baseline inventory, not launch/update evidence.
- GitHub owner-sibling provenance by itself: not evidence of a Nostr surface.
- Candidate-only NIP-89 listings, generic NIP-34 issues, quiet Shakespeare/NIP-discussion/Sovereign Engineering buckets, CI, dependency, docs-only, build-only, and version-only changes.

### Publication-day release-digest dispositions

- **Amber v6.6.0** and **Nostur 1.31.0:** skip this issue. Both are immediate follow-ups to recently covered clients, and the bounded final refresh did not establish a distinct change strong enough to displace the already selected client work.
- **mostro-core v0.14.6** and **mostro-cli v0.16.1:** skip as separate release items. The issue already covers Mostro's verified signed-order and audit-event changes from the canonical Mostro repository; the digest supplies only a documented-change marker for `mostro-core` and a component/version marker for `mostro-cli`, not a separate reader-facing Nostr development.
- **nostr-dart v11.0.0:** skip after review. The major library tag spans platform, messaging, and encryption surfaces, but the refresh did not isolate one primary-source-backed compatibility or protocol transition suitable for a compact release item.
- **Nostr-Doc 0.9.8:** skip. The digest identifies a possible first release but provides no independently verified launch claim or release-note delta beyond the tag.
- **Nostrube v0.2.39:** skip. The digest flags a possible first release and new platform, but no documented Nostr behavior was verified beyond the version tag.
- **Brezn build-130:** skip. The digest reports a new component and documented changes, but the final refresh did not verify a distinct Nostr-facing change with enough substance for the two-sentence release floor.
- **noble-ciphers 2.4.0:** skip. This is a general cryptography-library release; no issue-window Nostr protocol or client behavior was established.
- **Cellibacy v2.0.5/v2.0.6**, **Holy Fit v2.0.5**, **Nunlock v2.0.5**, **Saint Stream v2.0.7**, and **Sister Charge v2.0.5/v2.0.6:** skip. The release digest records version tags but no substance classification or verified Nostr-facing delta for any of the five applications.

## Selection review verdicts

- **Tracked-update reviewer:** PASS — 15 GREEN tracked candidates were ranked against exact source history; duplicate Shopstr and earlier nostream sources were excluded, and high-volume repositories were reduced to pinned relay-facing changes.
- **Discovery reviewer:** PASS — promoted Napstr v0.2.0 with canonical compare evidence, retained RSSNotes only as a backup, and rejected every owner-sibling/NIP-89 row plus NIP-34 issue-only activity as a standalone slot.
- **Protocol reviewer:** PASS — approved only merged NWC-05 `total_count`; rejected immediate continuity duplicates and open/draft spec behavior; selected NIP-18 plus NIP-25 with current evidence from Amethyst, Snort, and Ditto.
- **Editorial-balance reviewer:** PASS — slot pressure, source saturation, section uniqueness, and a 30-minute reading ceiling were checked; this orchestrator keeps one project in one section and records all intentional omissions.
- **Orchestrator reconciliation:** PASS — all four independent reviews were read and reconciled; disagreements are resolved in favor of exact-source continuity, merged behavior, and primary evidence.

GATE: PASS (15 GREEN triage candidates exceeded the minimum; all four independent Sol selection reviews passed and were reconciled; Napstr v0.2.0 is the sole verified discovery slot; only merged NWC-05 `total_count` advances as protocol work; NIP-18 plus NIP-25 meet the merged-spec, no-prior-deep-dive, and three-current-client evidence requirements; exact Newsletter #37 source duplicates, issue-only NIP-34 activity, partial discovery negatives, and first-run Zapstore claims are explicitly excluded)
