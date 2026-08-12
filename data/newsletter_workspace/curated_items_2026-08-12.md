# Curated Items — 2026-08-12

Scoring uses the NewsletterAgent 0–12 rubric: four 0–3 dimensions plus at most +2 history novelty, followed by demotions. Minimum selection score is 5. Coverage window: 2026-08-03..2026-08-11.

## Feature Candidates

- [nostr-wot-extension 0.4.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.4.0) — Score: 10/12 (3 relevance, 3 impact, 2 breadth, 3 novelty; -1 recent-history discipline). Derives ML-KEM and ML-DSA keys beside an existing Nostr identity, publishes a proof-of-possession attestation, and adds opt-in post-quantum direct messages combined with the existing encrypted-message key.
  - Continuity: #31 covered v0.3.86; 0.4.0 is a distinct primary release with the post-quantum key, attestation, and messaging transition.
- [Divine Mobile 1.0.19](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.19) — Score: 9/12 (2,3,2,2). Adds multi-account isolation, stronger private-message validation, recovered missing DMs, awaited relay publication, addressable-video tag preservation, and observed deletion handling. Non-Nostr caption/editor features are excluded.
  - Continuity: Divine appeared in #34, but this release URL and its user-facing changes are new.
- [MDK 0.9.11](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.11) — Score: 10/12 (3,2,2,3). Ships a large Marmot convergence and recovery tranche, secure deletion/zeroization work, mobile bindings, account-import recovery, and multi-agent message support.
  - Continuity: 0.9.10 appeared in #33; 0.9.11 is a distinct release with distinct convergence and security behavior.
- [Nostria 4.1.53](https://github.com/nostria-app/nostria/releases/tag/v4.1.53) — Score: 8/12 (2,3,1,2). Adds experimental relay-managed groups and encrypted Concord groups alongside video and profile improvements.
  - Continuity: distinct new release; no exact URL reuse.
- [Safebox Acorn: Digital Go-Bag](https://trbouma.github.io/safebox-acorn/digital-go-bag/) — Score: 11/12 (2,3,1,3 +2 first mention). A separately installable Nostr identity and data-portability CLI with canonical repository and maintainer identity verified during intake.
  - Continuity: new component extracted from tracked Safebox, not a rename.
- [Amber 6.4.0](https://github.com/greenart7c3/Amber/releases/tag/v6.4.0) — Score: 9/12 (3,3,2,1). Reworks grouped signing approvals into explicit per-request decisions, returns proper errors for denied bunker requests, and labels 113 additional event kinds.
  - Continuity: new release and approval behavior, distinct from prior Amber coverage.
- [Mostro Core 0.14.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.2) — Score: 8/12 (3,2,2,1). Replaces gift wrapping in its chat protocol with a conversation/signing-key kind-14 envelope.
  - Continuity: distinct protocol release URL and message-envelope transition.
- [LaWallet NWC 2.3.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.3.0) — Score: 9/12 (3,3,2,1). Adds Nostr notifications, zap receipts, invoice verification, and capability reporting. Weighted receive routing is excluded as Lightning-only.
  - Continuity: 2.0.0 appeared in #33; 2.3.0 has a distinct release source and new Nostr-facing contracts.
- [nostr-double-ratchet TypeScript 0.0.166](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.166) — Score: 8/12 (3,2,2,1). Requires session-key ownership proof in reusable-invite responses and rejects malformed rumor fields.
  - Continuity: distinct release and identity/session-binding change.
- [Cliprelay 0.1.3](https://github.com/tajava2006/cliprelay/releases/tag/desktop/v0.1.3) — Score: 7/12 (2,2,1,2). Adds typed cross-device text and reconstructs dead relay/signing connections after long idle periods.
  - Continuity: #32 introduced Cliprelay; the desktop and Android 0.1.3 tags are distinct sources for a new cross-platform workflow and recovery change.
- [cln-nip47 0.2.0](https://github.com/daywalker90/cln-nip47/releases/tag/v0.2.0) — Score: 8/12 (3,2,2,1). Adds hold-invoice methods and notifications, bounds transaction responses, removes methods dropped from the spec, and isolates notification failures by client.
  - Continuity: new release source and protocol-capability change.
- [NoorNote 1.3.2](https://github.com/77elements/noornote/releases/tag/v1.3.2) — Score: 6/12 (2,2,1,1). Changes article discovery to a friend-of-friend graph and repairs replayed-message notification storms.
  - Continuity: 1.3.1 appeared in #33; this distinct release has a new feed-selection behavior.
- [Bray 2.4.0](https://github.com/forgesworn/bray/releases/tag/v2.4.0) — Score: 6/12 (2,2,1,1). Adds a compact signing dialect alongside the standard remote-signing protocol. Build reproducibility is verification context, not the selected feature.
  - Continuity: 2.3.0 appeared in #33; 2.4.0 has one distinct signer interoperability change.

## Notable Candidates

- [nostrord PR #250](https://github.com/nostrord/nostrord/pull/250) — Score: 8/12 (3,2,1,2). Synchronizes per-group mute state across devices as self-encrypted application-data events and makes relay acceptance authoritative for the UI.
  - Continuity: 2.5.0 appeared in #34; this is a distinct merged PR and behavior.
- [Amethyst PR #3888](https://github.com/vitorpamplona/amethyst/pull/3888) — Score: 8/12 (3,2,2,1). Completes the Concord invite-list, re-mint, and revocation lifecycle.
  - Continuity: Amethyst appeared in #33; this merged PR is a distinct implementation transition.
- [Buzz PR #3653](https://github.com/block/buzz/pull/3653) and [PR #3767](https://github.com/block/buzz/pull/3767) — Score: 8/12 (3,2,2,1). Synchronize encrypted per-community appearance state between desktop and mobile via relays.
  - Continuity: Buzz appeared in #33; both URLs and cross-client state behavior are distinct.
- [Divine PR #6804](https://github.com/divinevideo/divine-mobile/pull/6804) — Score: 7/12 (3,2,1,1). Limits language self-labels to user-declared values and applies standard label semantics to published content.
  - Continuity: assign to Divine’s single Top Stories header, not a second project header.

## NIP Changes

The direct `gh pr list --state open --search updated:>=2026-08-03` query returned nine open PRs. The durable spec-family sweep contains 10 in-window PR records (8 open, 2 closed); final Selection retains only 3 open PRs plus 2 closed-unmerged status transitions after continuity filtering.

- [PR #2434](https://github.com/nostr-protocol/nips/pull/2434), post-quantum identity keys — Score: 8/12.
- [PR #2431](https://github.com/nostr-protocol/nips/pull/2431), browser signer key pinning — Score: 7/12.
- [PR #2430](https://github.com/nostr-protocol/nips/pull/2430), sticker packs — Score: 7/12; no assigned NIP file exists, describe by PR title only.
- [PR #2429](https://github.com/nostr-protocol/nips/pull/2429), Gopher documents — Score: 7/12; unnumbered proposal.
- [PR #2428](https://github.com/nostr-protocol/nips/pull/2428), epoch-ticketed private groups — Score: 8/12; cited numeric label is not an existing NIP filename, describe without it.
- [PR #2421](https://github.com/nostr-protocol/nips/pull/2421), BOLT12 zaps — Score: 7/12.
- [PR #2303](https://github.com/nostr-protocol/nips/pull/2303), web applets — Score: 7/12; proposed label is not an existing NIP file.
- [PR #1975](https://github.com/nostr-protocol/nips/pull/1975), Internet radio — Score: 6/12; unnumbered proposal.
- [PR #1813](https://github.com/nostr-protocol/nips/pull/1813), double ratchet — Score: 8/12.

## Potential NIP Deep Dive Topics

- NIP-09 (Event Deletion Request) + NIP-56 (Reporting): both are merged, absent from the normalized archive rotation, and form a moderation pair: users can report signed content and authors can request removal of their own published events. Current NIP-09 evidence includes [Divine PR #6623](https://github.com/divinevideo/divine-mobile/pull/6623), [strfry PR #251](https://github.com/hoytech/strfry/pull/251), and current Amethyst/nostrord source support. Current NIP-56 evidence includes [Divine PR #6591](https://github.com/divinevideo/divine-mobile/pull/6591), [Conduit PR #250](https://github.com/Conduit-BTC/conduit-mono/pull/250), and [nostrord’s NIP-56 implementation](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/nostr/Nip56.kt).
- NIP-32 and NIP-78 were rejected because case-normalized archive headings show both were already deep-dived in #26; the earlier case-sensitive scan was invalid.

## Discovery Candidates

**Tracked-worthy:** none.

**One-time mention:** none. BlindOracle and Crawlstr expose working pages, but no canonical repository, ownership chain, current release, or concrete recent change was established.

**Skipped:**

- BlindOracle — descriptor plus live page only; no canonical repo/current release.
- Crawlstr — descriptor plus live page only; no canonical repo/current release.
- gopherkind — descriptor lacks repository/product URL; the related spec proposal does not establish a product release.
- Let’s Fo Live — supplied API URL returns 404 and no canonical repository was found.
- Stash — GitWorkshop page resolves, but no independently verified current release or ownership chain.

## Omitted Items

- Buzz desktop 0.5.4–0.5.9 aggregate — Score: 4 after -2 recent-coverage demotion; selected merged cross-client preference PRs carry the distinct story instead.
- nostrord 2.5.1–2.8.0 aggregate — Score: 4 after recent-coverage and patch demotions; PR #250 is the stronger distinct source.
- nostr-calendar 2.2.0/2.3.0 — Score: 3; vague “app improvements/bug fixes” fail the depth minimum.
- RSSNotes 0.1.0 — Score: 4; empty primary release notes cannot support two substantive sentences.
- Lightning.Pub 0.0.33–0.0.35 — Score: 4; primarily Lightning swap/debit hardening with no distinct relay-facing API change.
- Myco 0.5.0 — Score: 4; mesh/deep-link work does not change the Nostr relay surface.
- pakstr 0.7.0–0.8.6 — Score: 3; Android signing/build pipeline and diagnostics, not Nostr protocol behavior.
- Bitcredit Core 0.5.15 — Score: 1; token-format update fails Nostr scope.
- bitcoin-safe, noble-ciphers, Feeder, CDK, Nutshell — Score: 0–3; Bitcoin/Cashu/feed-reader or generic cryptography work fails scope.
- Remaining MAYBE/SKIP triage entries — below 5 because their primary source is vague, maintenance-only, duplicate, outside the window, or lacks a verified Nostr-facing change.
