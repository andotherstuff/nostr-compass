# Selection Review — 2026-08-12

Newsletter: #35
Edition type: Regular (next Wednesday is 2026-08-19, same calendar month)
Coverage window: 2026-08-03..2026-08-11
Selection status: self-approved under task instruction, subject to the four independent reviews recorded below
Scoring source: [curated_items_2026-08-12.md](curated_items_2026-08-12.md)

## Archive and continuity evidence

The full English issues for 2026-08-05 (#34), 2026-07-29 (#33), and 2026-07-22 (#32) were read before allocation. `data/coverage_history.json` was queried for every selected repository. Every selected project release/PR URL is distinct from the archive. Required protocol-family status links are explicitly exempt from that statement: a standing repository URL may recur solely to document a mandatory active/quiet sweep result, never as a reused news story.

The recent archive makes several exclusions material: #34 already explains nostrord 2.5.0 and Divine’s prior relay timeout work; #33 covers Amethyst 1.13.0/1.13.1, Buzz 0.5.0, MDK 0.9.10, NoorNote 1.3.1, Bray 2.3.0, and LaWallet NWC 2.0.0; #32 covers a different set of relay-access and client changes. Each repeated project retained below therefore records both a distinct primary URL and a distinct behavior.

## Selected structure

- Top Stories: 6
- Tagged Releases: 7
- In Development: 3
- Protocol and Spec Work: 7 mandatory family paragraphs, selecting 3 open NIP PRs, 2 closed-unmerged status transitions, and 1 merged documentation commit
- NIP Deep Dive: 2 merged NIPs
- Estimated reading time: 24–28 minutes

## Top Stories — 5 items

### 1. nostr-wot-extension 0.4.0 — 10/12

- Primary source: [release 0.4.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.4.0), 2026-08-11.
- Angle: derive post-quantum encryption and signing keys beside an existing Nostr identity; publish proof of possession; opt into direct messages whose key combines the post-quantum secret with the established encrypted-message key.
- Why it clears depth: the release supplies explicit cryptographic construction, relay event behavior, downgrade policy, recovery constraints, and user workflow.
- Continuity: #31 covered v0.3.86. Version 0.4.0 is a distinct release and adds the post-quantum key, proof-of-possession, and messaging behavior not explained there.

### 2. Divine Mobile 1.0.19 — 9/12

- Primary source: [release 1.0.19](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.19), 2026-08-08.
- Angle: multi-account isolation, private-message rumor/seal validation, recovered missing messages, awaited relay publishes, addressable-video tag preservation, and observed Nostr deletion handling. Omit captions, clip provenance, and other video-editor work without an event-level Nostr change.
- Distinct change: #34 discussed per-relay query timeouts; this source covers publishing, messaging integrity, accounts, and creator video tools not explained there.
- Supporting merged primary sources: [PR #6804](https://github.com/divinevideo/divine-mobile/pull/6804) for user-declared language labels and [PR #6591](https://github.com/divinevideo/divine-mobile/pull/6591) for truthful report delivery.
- Single-header rule: NIP-09/NIP-56 implementation evidence is folded into this header, not repeated under In Development.

### 3. MDK 0.9.11 — 10/12

- Primary source: [release 0.9.11](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.11), 2026-08-10.
- Angle: Marmot group convergence recovery, atomic capability projection, secure deletion/zeroization, resumable account import, mobile bindings, and agent-album delivery.
- Distinct change: #33 covered 0.9.10’s pending sends, notification supervision, history, and KeyPackage republishing; 0.9.11 is a new URL and materially advances convergence, recovery, storage secrecy, and host integrations.
- Collapse rule: snapshot, MarmotKit, and wn-agent companion tags are assets of this one release story, not separate paragraphs.

### 4. Nostria 4.1.53 — 8/12

- Primary source: [release 4.1.53](https://github.com/nostria-app/nostria/releases/tag/v4.1.53), 2026-08-09.
- Angle: experimental relay-managed groups and encrypted Concord groups. Omit clip playback and profile-photo editing because those changes do not touch a Nostr event or relay surface.
- Continuity: distinct release URL; no exact source reuse.

### 5. Amber 6.4.0 — 9/12

- Primary source: [release 6.4.0](https://github.com/greenart7c3/Amber/releases/tag/v6.4.0), 2026-08-07.
- Angle: explicit per-request Approve/Deny controls for grouped signing, correct denial errors for remote signer requests, and human-readable labels for 113 more event kinds.
- Continuity: distinct release and signer workflow; no source reuse.

### 6. Safebox Acorn — 11/12

- Primary sources: [Digital Go-Bag guide](https://trbouma.github.io/safebox-acorn/digital-go-bag/) and [canonical repository](https://github.com/trbouma/safebox-acorn).
- Angle: a separately installable Python component and CLI for carrying and restoring Nostr identity/data state; canonical ownership and relay-backed maintainer identity were verified in intake.
- Continuity: extracted from tracked Safebox, but it is neither a rename nor a duplicate repository.
- Discovery status: this is a verified user-intake project, not one of the unverified descriptor candidates.

## Tagged Releases — 7 items

### Mostro Core 0.14.2 — 8/12

- Source: [0.14.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.2), 2026-08-06.
- Distinct change: its chat protocol replaces gift wrapping with a conversation/signing-key kind-14 envelope. This is a wire-format transition, not a version-only follow-up.

### LaWallet NWC 2.3.0 — 9/12

- Source: [2.3.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.3.0), 2026-08-06.
- Distinct change from #33’s 2.0.0: Nostr notifications, NIP-57 zap receipts, LUD-21 invoice verification, and an address capability view. Omit weighted receive forwarding because that payment-routing feature has no demonstrated Nostr-event change.

### nostr-double-ratchet TypeScript 0.0.166 — 8/12

- Source: [0.0.166](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.166), 2026-08-10.
- Distinct change: reusable public invites now require a session-key ownership proof, preventing identity/session misbinding; malformed rumor fields are rejected.

### cln-nip47 0.2.0 — 8/12

- Source: [0.2.0](https://github.com/daywalker90/cln-nip47/releases/tag/v0.2.0), 2026-08-09.
- Distinct change: hold-invoice methods and notifications, bounded transaction responses, current method set, and per-client notification isolation.

### Cliprelay 0.1.3 — 7/12

- Source: [desktop 0.1.3](https://github.com/tajava2006/cliprelay/releases/tag/desktop/v0.1.3) and [Android 0.1.3](https://github.com/tajava2006/cliprelay/releases/tag/android/v0.1.3), 2026-08-05.
- Angle: one cross-platform story. Typed text can travel to another device’s clipboard; dead relay and signer connections rebuild after idle periods.

### NoorNote 1.3.2 — 6/12

- Source: [1.3.2](https://github.com/77elements/noornote/releases/tag/v1.3.2), 2026-08-08.
- Distinct change from #33’s 1.3.1: article discovery moves from a flat global feed to a friend-of-friend graph, and replayed-message toast storms are suppressed.

### Bray 2.4.0 — 6/12

- Source: [2.4.0](https://github.com/forgesworn/bray/releases/tag/v2.4.0), 2026-08-07.
- Distinct change from #33’s 2.3.0: a compact signing dialect now works alongside the standard relay-mediated signer flow. Reproducible-build metadata is verification context, not a selected Nostr feature.

## In Development — 3 items

### nostrord synchronizes group muting — 8/12

- Primary source: [merged PR #250](https://github.com/nostrord/nostrord/pull/250), merged 2026-08-10.
- Distinct behavior: per-group mute state becomes self-encrypted application-data events synchronized across devices; UI state rolls back if signing/publication fails.
- Allocation: this is nostrord’s only selected placement. Releases 2.5.1–2.8.0 remain omitted at 4/12, consistent with the curated score; do not reintroduce them.

### Amethyst completes Concord invite lifecycle — 8/12

- Primary source: [merged PR #3888](https://github.com/vitorpamplona/amethyst/pull/3888), merged 2026-08-10.
- Distinct change from #33’s launch: invite listing, re-minting after refounding, and revocation close a later part of the encrypted-community lifecycle.
- Do not repeat the 1.13.0/1.13.1 releases.

### Buzz synchronizes per-community appearance — 8/12

- Primary sources: [merged desktop PR #3653](https://github.com/block/buzz/pull/3653) and [merged mobile PR #3767](https://github.com/block/buzz/pull/3767), merged 2026-08-05.
- Distinct change from #33’s 0.5.0 invitations/search: encrypted relay state carries each community’s appearance choices across desktop and mobile with cache, replacement ordering, and reconnect handling.
- Do not summarize the six patch releases or repeat agent-invitation coverage.

## Protocol and Spec Work

Every family was audited, but the published section includes only substantive in-window activity. Quiet families and metadata-only updates remain in this review artifact rather than becoming newsletter filler.

### NIPs — active

Direct query found zero merged NIP PRs. Select only new proposals and material state transitions; unchanged open PRs already explained by prior issues are excluded even when the overlapping fetch reports a new `updated_at` value:

- [#2434](https://github.com/nostr-protocol/nips/pull/2434): post-quantum identity keys.
- [#2431](https://github.com/nostr-protocol/nips/pull/2431): browser clients pinning the user key under the existing browser-signing specification.
- [#1813](https://github.com/nostr-protocol/nips/pull/1813): double ratchet.
- [#2433](https://github.com/nostr-protocol/nips/pull/2433): relay-auth error clarification, opened and closed unmerged in-window; report the closed status, not a shipped change.
- [#2378](https://github.com/nostr-protocol/nips/pull/2378): the previously covered sovereign-agent proposal closed unmerged on 2026-08-09; this closed status is the material transition and the only reason its URL may recur.

Continuity exclusions: #2430, #2429, and #2428 were already explained in #34; #2421 in #33; #2303 in several issues including #32. #1975 has no verified material transition. None enters the issue.

Also record the merged [NIP-29 example clarification commit](https://github.com/nostr-protocol/nips/commit/656cecc7c0a815b6a2b218d3b5d6f078b3f4dbab) as documentation-only, not a feature.

### BUDs — quiet

- Primary source: [Blossom repository](https://github.com/hzrd149/blossom).
- Status: no public commits or PRs in the spec sweep.

### NAPs — metadata-only; omitted

- Primary source: [NAP repository](https://github.com/napplet/naps).
- Status: the only in-window commit changes maintainer merge criteria. The proposal branches used in the earlier draft have no in-window commits; their apparent activity came from metadata updates. All NAP paragraphs were removed as unchanged or process-only material.

### Marmot/MIPs — quiet

- Primary source: [Marmot spec repository](https://github.com/marmot-protocol/marmot).
- Status: no spec-repository commits or PRs. MDK implementation work belongs in Top Stories and does not make the spec family “active.”

### Gamma Markets — quiet

- Primary source: [market-spec repository](https://github.com/GammaMarkets/market-spec).
- Status: no public commits or PRs.

### Concord/CORD — active

- Primary source: [Concord repository](https://github.com/concord-protocol/concord).
- Status: six commits and seven PRs in the sweep. Explain the material CORD changes once; connect implementation evidence through Amethyst without duplicating its project paragraph.

### NWC — no new shipped change; omitted

- Primary source: [NWC repository](https://github.com/nostr-wallet-connect/nwc).
- Status: the only returned PR merged on August 2 and was already covered in Newsletter #34. A later `updated_at` value did not establish a new commit or status transition, so the duplicate paragraph was removed.

## NIP Deep Dive — NIP-09 and NIP-56

- Primary: [NIP-09 (Event Deletion Request)](https://github.com/nostr-protocol/nips/blob/master/09.md).
- Secondary: [NIP-56 (Reporting)](https://github.com/nostr-protocol/nips/blob/master/56.md).
- Merge verification: both files exist on the NIPs repository’s master branch; they are established merged specifications.
- Rotation verification: a case-insensitive scan of every English deep-dive heading found no prior NIP-09 or NIP-56 dive. The scan explicitly catches #26’s lowercase headings for NIP-32 and NIP-78, which are therefore excluded. The legacy memory path is absent, so normalized archive headings are authoritative.
- Connection: NIP-56 lets a user publish a signed report about an event or account; NIP-09 lets an author request removal of their own published event. Together they explain two distinct moderation signals without pretending either one guarantees relay deletion or platform action.
- NIP-09 current implementation evidence (three independent tools): [Divine PR #6623](https://github.com/divinevideo/divine-mobile/pull/6623) purges deleted videos from its event store; [strfry PR #251](https://github.com/hoytech/strfry/pull/251) lets gift-wrap recipients issue valid deletion requests; [Amethyst’s current NIP-09 source support](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md) documents client support. [nostrord’s current group-client source](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/network/NostrGroupClient.kt) is a fourth implementation pointer.
- NIP-56 current implementation evidence (three independent applications): [Divine PR #6591](https://github.com/divinevideo/divine-mobile/pull/6591) fixes truthful report delivery; [Conduit PR #250](https://github.com/Conduit-BTC/conduit-mono/pull/250) reads reports as bounded buyer context; [nostrord’s NIP-56 implementation](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/nostr/Nip56.kt) publishes and handles report events. [Amethyst’s current support declaration](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md) is additional corroboration.
- Real-event requirement for Stage 5: recover real kind 5 and kind 1984 examples from public relays if prose includes JSON. If suitable events cannot be recovered, omit JSON rather than inventing placeholders.

## Discovery verification

| Candidate | Evidence checked | Decision |
|---|---|---|
| BlindOracle | Signed descriptor; live product page HTTP 200; no canonical GitHub repository found | SKIP: ownership/current-release bar not met |
| Crawlstr | Signed descriptor; live page HTTP 200; no canonical repository found | SKIP: ownership/current-release bar not met |
| gopherkind | Signed descriptor only; no repository or product URL | SKIP: cannot verify working product or ownership |
| Let’s Fo Live | Signed descriptor; supplied API URL HTTP 404; no canonical repository found | SKIP: product surface unavailable |
| Stash | Signed descriptor; GitWorkshop page HTTP 200; no verified current release or independent ownership chain | SKIP: insufficient current primary evidence |

## Topic-page audit

Existing and usable:

- `content/en/topics/nip-09.md`
- `content/en/topics/nip-56.md`
- `content/en/topics/marmot.md`
- `content/en/topics/concord-protocol.md`

Missing project/topic pages to queue before assembly:

- nostr-wot-extension
- Divine
- Nostria
- Safebox Acorn
- Amber
- Mostro
- LaWallet NWC
- nostr-double-ratchet
- Cliprelay
- cln-nip47
- NoorNote
- Bray
- nostrord
- Amethyst
- Buzz

Each created page must contain a Primary sources section. Writers may link directly to primary project sources until the corresponding page exists.

## Required SKIP list

- nostr-calendar 2.2.0/2.3.0 — score 3; vague notes cannot support the depth minimum.
- RSSNotes 0.1.0 — score 4; empty release notes.
- Lightning.Pub 0.0.33–0.0.35 — score 4; Lightning/debit/swap hardening without a distinct Nostr route change.
- Myco 0.5.0 — score 4; mesh diagnostics and deep links do not change Nostr relay behavior.
- pakstr 0.7.0–0.8.6 — score 3; Android build/signing tooling.
- Bitcredit Core, bitcoin-safe, noble-ciphers, Feeder, CDK, Nutshell — score 0–3; fail Nostr scope.
- Code Call’s 48-tag run — omitted despite activity; #33 already covered it and the tag churn lacks one clearly bounded, distinct newsletter-scale transition.
- Remaining triage MAYBE/SKIP items — below 5, duplicate, maintenance-only, outside the window, or missing primary evidence.

## Independent selection validation

Four independent reviews are mandatory. Their reports and resulting deltas are recorded in `validation_selection_2026-08-12.md`. Any critical continuity, scope, NIP-validity, discovery, or slot-allocation finding must be resolved here before the terminal gate.

## Approval

Task instruction makes selection self-approved unless genuine human input is required. No unresolved choice requires human input: all selected items have a concrete section, score, primary source, and continuity rationale.

GATE: PASS — self-approved after the final continuity and interest audit; 6 Top Stories, 7 Tagged Releases, 3 In Development items, substantive NIP and Concord activity, and 2 non-rotated merged NIP deep dives
