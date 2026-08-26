# Stage 4 selection review — Newsletter #37 (2026-08-26)

Selection is Sol-owned and based on `triage_2026-08-26.md`, `coverage_history.json`, complete reading of Newsletters #34–#36, and four parallel Sol review passes over tracked updates, discovery feeds, protocol feeds, and month-end history. This artifact is the complete writing brief for Stage 5. It authorizes no publication action.

## Editorial frame

Newsletter #37 is the August month-end issue. Its through-line is **trust boundaries becoming concrete across keys, relays, app distribution, and protocol evolution**. The issue introduces the four projects the editor explicitly requested, but does not turn discovery into a directory dump.

## Selected: Top Stories

1. **Shopstr removes serialized NIP-46 and NWC secrets from browser persistence**
   - Sources: https://github.com/shopstr-eng/shopstr/pull/436 and https://github.com/shopstr-eng/shopstr/pull/437
   - Explain the prior persistence boundary and the new behavior. Do not imply all browser compromise risk is eliminated.

2. **Routstr SDK hardens relay-sourced provider discovery**
   - Source: https://github.com/Routstr/routstr-sdk/pull/47
   - Explain signature verification, far-future-event rejection, and fail-closed trusted-review behavior as three distinct protections.

3. **Postr launches as a deliberately small Android composer**
   - Sources: https://gitworkshop.dev/npub1qwkd5wzftcxquuhtkcg0xn9ed7evksluuppf7qdmdh34ywe9uncs5uqfvl/relay.ngit.dev/postr and NIP-34 event `0335c6e9ed4cbd2b4ea5a0539884785ae448903641385302ca5090c672a38f56`
   - Cover Amber signing, relay-list use, drafts/outbox, attachments, and publish readback. State that the NIP-34 announcement and signed project profile were recovered from `relay.ngit.dev`.

4. **Infans encrypts family tracking and co-parent sync over Nostr**
   - Source: https://github.com/TurkeyNostr/infans
   - Explain offline-first Room storage, NIP-44 encryption, and kind 30078 backup/sync. Do not claim medical-grade accuracy or security review.

5. **pakstr makes Nostr app packaging and Zapstore publication more explicit**
   - Sources: https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.0, https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.1, https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.2, https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.3, https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.14.0, and https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.15.0
   - Synthesize the release chain instead of writing six mini changelogs. Distinguish automatic versioning, Blossom fixes, publisher validation, and Zapstore metadata.

6. **nostr-tools corrects protocol validation behavior**
   - Source: https://github.com/nbd-wtf/nostr-tools/pull/545
   - Read the full diff before prose and state only the exact validation contracts changed.

## Selected: Tagged Releases

1. **Nostr Java v2.0.8** — https://github.com/tcheeric/nostr-java/releases/tag/v2.0.8 — subscription isolation plus NIP-44 provider portability.
2. **NoorNote 1.3.6** — https://github.com/77elements/noornote/releases/tag/v1.3.6 — NIP-38 profile statuses and NIP-99 listing display.
3. **nostrord 2.9.0** — https://github.com/nostrord/nostrord/releases/tag/v2.9.0 — relay-scoped leave/delete markers and media rendering.

No release receives fewer than two substantive sentences. Drop it rather than pad it if full release-note review cannot establish reader impact.

## Selected: Newly Discovered

1. **Heterodyne** — https://radicle.network/nodes/iris.radicle.network/rad%3Az2zX5XvPiggGJvCn8DPkp1hRNGA5
   - User-required inclusion and tracking addition. Frame as an introduction to a specification family, not a current-week release. Name the Nostr, Radicle, Marmot, and KERI boundaries without implying production adoption.

Postr and Infans are also newly tracked but are already allocated to Top Stories; do not duplicate them here. The ordinary discovery slot is therefore Heterodyne. The other 599 reviewed candidates remain omitted unless a later source refresh establishes a materially stronger reason.

## Selected: Protocol and Spec Work

- **NIP-22 kind 1111 rollout:** https://github.com/nostr-protocol/nips/pull/2448 plus Snort commit https://github.com/v0l/snort/commit/a55ff3878b558ac9ac97a69c48bc713def2ae432 and Ditto commit https://github.com/soapbox-pub/ditto/commit/d341358f08f5765bd03dc3f6965f80de751df7d1. Verify current PR state before prose. Use PR #2358 only as prior-history context, not as a new source.
- **NIP-47 maximum-fee proposal:** https://github.com/nostr-protocol/nips/pull/2444. Label proposed until merge readback says otherwise.
- **NWC payment lookup proposal:** https://github.com/getAlby/nwc-developer-docs/pull/5. Label proposed until merge readback says otherwise.
- **NAP-DISPLAY:** https://github.com/napplet/naps/pull/97. Explain that the runtime owns permission mediation and hardware policy.
- **Marmot multi-device experiment:** https://github.com/marmot-protocol/marmot/pull/417. Keep clearly experimental and include only if the full diff supports a distinct protocol behavior.

All seven spec families were checked. BUDs, Gamma, and Concord were quiet. Do not create filler paragraphs for quiet families.

## Selected: Six Years of Nostr Augusts

This replaces both NIP Deep Dive slots. Required structure: one H3 for each year **2021, 2022, 2023, 2024, 2025, 2026**, with at least two sourced paragraphs per year.

- **2021 — quiet protocol core:** source the no-commit August window in the original protocol repository, then research one surviving client/relay/application artifact from August 2021 before writing. If no defensible artifact exists, describe the quiet period without inventing a milestone and use two primary sources that establish the baseline.
- **2022 — reactions become general:** anchor on https://github.com/nostr-protocol/nips/commit/7af2540c6e392d5cb789c743b1dd237294388649 and trace the resulting NIP-25 behavior into current clients with primary implementation evidence.
- **2023 — select after full-diff verification:** choose the strongest August 2023 interoperability change from `data/history_research/2026-08-candidates.json`, then verify its complete diff and at least one current implementation. The writing stage must not infer this from the commit title.
- **2024 — addressable events become shared vocabulary:** anchor on https://github.com/nostr-protocol/nips/commit/ca3c52e3e74f0a4679f1c6c0d9ac6461ea748d2d and show how the terminology maps to stable event coordinates in current implementations.
- **2025 — select after full-diff verification:** choose one August 2025 change with present-day implementation evidence and no prior-history source collision.
- **2026 — comment threads reach clients:** use the NIP-22 kind 1111 rollout above as the endpoint. Avoid duplicating full prose between the protocol section and the history section; the protocol section should carry status, while the history section carries the six-year comparison.

The unresolved 2021/2023/2025 research points are deterministic writing-stage verification work, not a human editorial decision. If any year cannot support two sourced paragraphs, Stage 5 must fail that section rather than fabricate.

## Explicit omissions

- Amethyst 1.14.0: substantial but immediately consecutive coverage after Newsletter #36; hold unless a later delta makes it unavoidable.
- Mostro 0.18.5: held pending complete release-note separation of Nostr-facing changes from marketplace-only work.
- Zapstore launch/update claims: unusable zero-release fetch.
- NIP PR #2438, PR #2421, and PR #2303: prior coverage without a newly verified status change.
- Generic NIP-34 repositories, owner siblings, and #SovEng posts that do not name a concrete Nostr surface or project progress.
- CI, dependency, docs-only, build-only, and version-only changes.

## Selection review verdicts

- **Tracked-update reviewer:** PASS — security, protocol, and release candidates were ranked against source dates and coverage history; recent repeats were demoted.
- **Discovery reviewer:** PASS — all 603 rows, including 561 owner siblings, were reviewed as candidates rather than treated as Nostr-positive by provenance; all four user submissions were verified independently.
- **Protocol reviewer:** PASS — seven spec families and relay-backed feeds were checked; proposals remain labeled proposals and prior sources were excluded.
- **History reviewer:** PASS WITH WRITING OBLIGATIONS — the compliant six-year span is 2021–2026; 2021/2023/2025 require full primary-source research before prose and cannot be filled from titles.
- **Orchestrator reconciliation:** PASS — each selected item appears in one section, every ordinary item scores at least 5, the four user-required items are preserved, and no owner decision is needed.

GATE: PASS (6 Top Stories, 3 releases, 1 discovery slot, 5 protocol/spec items, and a six-year month-end history brief selected after four Sol review passes; exact sources, continuity exclusions, user-required inclusions, and deterministic writing-stage research obligations are recorded; no human selection input required)
