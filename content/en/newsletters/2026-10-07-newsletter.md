---
title: "Nostr Compass #43"
date: 2026-10-07
publishDate: 2026-10-07
draft: true
type: newsletters
description: "Compound searches, encrypted app and messaging changes, Sidecar web highlights, relay and wallet progress, and a focused guide to domain names and public profiles."
---

[Ants](#ants) keeps [compound search constraints aligned](https://github.com/dergigi/ants/pull/313). [Myco](#myco), a host for small Nostr apps, adds permission-gated uploads; [Marmot MDK](#marmot-mdk), an encrypted messaging toolkit, improves account discovery and attachment recovery. [Iris Chat](#iris-chat) adds message editing, and [Sidecar](#sidecar) publishes web highlights. The [profile tutorial](#nip-deep-dive-nip-05-and-nip-24) explains signatures and separately verified internet identifiers.

## Top Stories

### Ants

Ants, a Nostr search client, now supports nested AND/OR searches across its [native Android release](https://github.com/dergigi/ants-android/releases/tag/v0.34.0) and [released web query compiler](https://github.com/dergigi/ants/pull/313), keeping author, event-type and date constraints tied to each branch. Android also filters result language locally. Results remain limited by selected relays, event caps and deadlines; text matching depends on relay support for [NIP-50, relay-side search](/en/topics/nip-50/).

The web app's [v0.6.0](https://github.com/dergigi/ants/releases/tag/v0.6.0) adds zap, nutzap and public mute-list cards; displayed amounts come from published invoices or proofs and do not establish settlement. Later [follow, pin and bookmark cards](https://github.com/dergigi/ants/commit/a81a1e2c628cc5aca5c5f2064652ba3bce1b7d30) read public entries while leaving encrypted private contents undisplayed.

Later Android [0.35.0](https://github.com/dergigi/ants-android/releases/tag/v0.35.0) loads zap and nutzap targets inline, including addressable notes, and adds profile-scoped media filters. [0.36.0](https://github.com/dergigi/ants-android/releases/tag/v0.36.0) shares submitted searches as ants.sh links. These links expose query text and omit local language-filter settings; results still depend on the receiving client and its relays.

### Myco

Myco, a host for small Nostr apps, [ships permission-gated uploads](https://github.com/Origami74/myco/pull/125) in [v0.10.0](https://github.com/Origami74/myco/releases/tag/v0.10.0). The shell selects [Blossom file servers](/en/topics/blossom/) and signs upload authorization without exposing the user's key to apps, returning confirmed file URLs and hashes. Uploads are capped at 16 MiB; consent comes from installation approval, with no per-upload preview or EXIF stripping.

### Marmot MDK

Marmot MDK, an encrypted messaging toolkit, [releases v0.12.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.12.0) with broader account-import discovery, separate inbox defaults and source-epoch attachment keys with bounded recovery, supported by its [implementation changes](https://github.com/marmot-protocol/mdk/pull/2138) and [companion release work](https://github.com/marmot-protocol/mdk/pull/2141). Later [merged queued-send preservation](https://github.com/marmot-protocol/mdk/pull/2172) keeps sibling failures from stopping eligible sends, but is outside that release. History beyond five epochs can remain undecryptable.

Later master work adds [beta per-account C sessions](https://github.com/marmot-protocol/mdk/pull/2154) using [NIP-46 remote signing](/en/topics/nip-46/) for remote-signer login and restore, and [backports the KEM dependency fix to 0.0.10](https://github.com/marmot-protocol/mdk/pull/2208) while retaining HPKE 0.7 compatibility. Hosts must encrypt exported signer credentials. These changes are outside v0.12.0.

Agent integrations add a [Goose terminal harness](https://github.com/marmot-protocol/mdk/pull/2199) and [admin-gated group-profile tools](https://github.com/marmot-protocol/mdk/pull/2115); [opaque draft-revision markers](https://github.com/marmot-protocol/mdk/pull/2132) help hosts distinguish newer edits during send handoff. Goose attachments and autonomous mode remain unsupported, and real-binary interoperability is unverified. Draft markers require host adoption and matching bindings; they do not authorize deletion.

### Iris Chat

Iris Chat, an encrypted messaging app, [adds message edits, edit history and deletion controls](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.10.5.1). Its [author-authenticated mutation handling](https://github.com/irislib/iris-chat-rs/blob/90af94addbbaa8b9f34024f74def3b297499586f/core/src/core/message_mutations.rs) preserves deletion tombstones through replay and applies edits only after encrypted enqueue succeeds. Editing is limited to delivered, unexpired outgoing text without attachments; delete-for-everyone requests removal by compatible clients and cannot prove recipients erased their copies.

Later [device-link updates](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.10.6.1) start chosen history transfer after verified local approval and preserve routed transfers when a direct link disappears. Sign-in codes remain usable until cancellation; completion waits for observed authorization. [Older-account recovery](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.10.7) repairs equivalent signed device lists while stripping retired encrypted labels; conflicting authorization still fails.

## Tagged Releases

### Nostr WoT

Signing policies now apply global rules, site/account overrides and exact-origin defaults for [NIP-98 HTTP authentication](/en/topics/nip-98/), with denials taking precedence and money requests reviewed individually in the [extension release](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.10). Nostr WoT's trust and signing tools also gain a [published bunker responder](https://registry.npmjs.org/@nostr-wot%2fbunker/0.2.0) for [NIP-46 remote signing](/en/topics/nip-46/), with verified replay bounds and authenticated pairing state. Hosts still own approvals, key storage and durable revocation state.

[Account Archive](https://github.com/nostr-wot/nostr-wot-extension/pull/39) in [v0.8.11](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.11) synchronizes original signed events across relays with checkpoints and encrypted local storage. [Version 0.8.12](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.12) makes exported archive files passwordless while checking signatures and account ownership on import; older encrypted exports remain supported. Exported files and encrypted local storage have different privacy boundaries.

### Scramble

Still-sealed messages arriving ahead of the current group epoch now survive restarts and replay when the epoch advances in [Scramble v0.7.9](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.9). The group messenger also binds KeyPackage identifiers before relay exposure. Recovery is bounded by a 256-envelope cap per group and a retention window.

### Sonar

Active conversations gain [chat catchup](https://github.com/hedwig-corp/bitchat-to-sonar/pull/649), while [queue isolation and bounded push-token sharing](https://github.com/hedwig-corp/bitchat-to-sonar/pull/657) improve how Sonar, a chat application, handles background work. These changes ship in [v0.1-alpha.15.4](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.15.4); relay caps and queue overflow still limit catchup.

### Chama

Creator checks now compare the full creator identity when known, discard provisional link claims after failed loads and refuse ambiguous fresh legacy links in [Chama v6.4.20](https://github.com/jesuspirate/chama/releases/tag/v6.4.20). The Nostr peer-to-peer escrow client also [waits for relay acknowledgement before on-chain locking](https://github.com/jesuspirate/chama/releases/tag/v6.4.19). Cold-start wakes after swiping the app away have regressed in v6.4.20.

### Mostro

Funded hold invoices are protected from cancellation, failed lookups are deferred and bonds are paid exactly in [Mostro v0.19.1](https://github.com/MostroP2P/mostro/releases/tag/v0.19.1), the peer-to-peer trading daemon. Core progress adds [weighted imported reputation](https://github.com/MostroP2P/mostro-core/pull/177) and [signed reputation validation](https://github.com/MostroP2P/mostro-core/pull/181), with issuer trust left to callers. Unreleased main-branch work adds [Cashu ecash discovery and order creation](https://github.com/MostroP2P/mostro/pull/1045) plus [taking orders and locking escrow](https://github.com/MostroP2P/mostro/pull/1047); release, cancellation and dispute operations remain rejected. Additional unreleased main-branch [payer declarations](https://github.com/MostroP2P/mostro/commit/bd6a723248e60dfa8b4657e4c50c38b489ab96ec) let buyers exchange a fiat-account hash bound to the current trade. It is disabled by default and unavailable in Cashu mode; guessable account hashes do not prove identity.

Main-branch [Mostro core user-info messages](https://github.com/MostroP2P/mostro-core/pull/185) add a restore-only request and reply for a user's own reputation, including rating, review count, operating days and first-trade date. Daemon identity-proof and lookup integration remain separate.

### Earthly

Map, Story and Atlas authoring now share [native Chrome WebMCP browser-agent operations](https://github.com/zeSchlausKwab/earthly/pull/31), with [confirmation tied to the exact preview and account revision](https://github.com/zeSchlausKwab/earthly/pull/33). Earthly, a map-based publishing tool, adds [signed-byte recovery and explicit draft-preserving rebase](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.15). Chrome support remains experimental, and later observation of a publication is distinct from an acknowledgement whose outcome was unknown.

### nostream

Multiple tag constraints and per-filter limits now produce correct query results through the [filter-query repair](https://github.com/cameri/nostream/pull/792) included in nostream v3.2.0. The Nostr relay's [release](https://github.com/cameri/nostream/releases/tag/v3.2.0) also includes optional HAProxy/readiness support and Redis fanout. Existing sockets do not migrate during cutover, and Redis unavailability can drop fanout messages.

### Grain

Event serialization and replacement preflight checks improve in [Grain v0.8.0](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0), a Nostr relay. Malformed subscription and count constraints now fail without widening queries, while newly tracked late backfills use receipt time for purging. Replacement preflight is not a durable commit: deletion can still precede asynchronous ingestion, leaving a write gap.

### Ditto

Ditto, a Nostr social client, adds file posts and a tap-to-load 3D attachment viewer in [v2.43.0](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.43.0), with 200 MiB download limits. [v2.44.0](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.44.0) adds [event-native 3D objects](https://gitlab.com/soapbox-pub/ditto/-/commit/2be9431f9c89a84c94c250430fe34fcff6fd1641), customizable Blobbi rooms and addressable videos, plus NSFW and blocked-term filtering in public feeds and search. Release notes also report interrupted-wallet repairs and add Lightning-address fallback for failed Lightning URLs. Zap invoice amounts must match, but description-hash mismatches only warn: automatic payment can proceed with unverified sender or post binding. [v2.44.1](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.44.1) reads notifications from account-declared inbox relays with per-relay paging, retrieves own saved lists from write relays and repairs WebLN payment-provider handling. List edits use the latest observed event; withheld or stale relay copies remain a limit. Separate relay-source [mention parsing](https://gitlab.com/soapbox-pub/ditto-relay/-/commit/8a4537a86a3f662cd30debd50fa2a3d5a23ab1c6) continues past truncated references.

### Nostr Double Ratchet journals received controls

Private control messages now share a durable journal row with advanced receiver state in [the TypeScript v0.0.176 release](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.176). The encrypted messaging library retains them until the application's durable acknowledgement, enabling replay after failure or restart. Callbacks must be idempotent and validate authorized siblings; newly ratcheted AppKeys labels do not retroactively protect older records.

### nostr-social-graph

Private-contact edits now persist before notification, with owner-bound controls, fieldwise clocks and exact pending acknowledgements in [nostr-social-graph v2.0.3](https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.3). The social-graph library retains rejected handoffs for bounded retries. Callers must provide authenticated, durable sibling transport; a ready status means acceptance into an outbox, not delivery to every device.

### nostr-pubsub

Ordinary subscriptions start immediately, followed by optional bounded [NIP-77 inventory reconciliation](/en/topics/nip-77/) in [nostr-pubsub TypeScript v0.5.14](https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.14). The subscription library fetches missing event IDs over the existing relay socket and verifies events through the normal admission path. Reconciliation does not upload local-only events or change history-completion semantics.

The separate [Rust FIPS package v0.5.20](https://crates.io/api/v1/crates/nostr-pubsub-fips/0.5.20) [preserves pending replies and subscriptions](https://github.com/mmalmi/nostr-pubsub/commit/03dab368850b391b8874e42b19521311e3ebdfd7) when an inbound peer becomes a discovered outgoing peer, reusing its established stream. Physical-link changes and advertised service restarts still reset that stream.

### FIPS

Missing routed sessions can recover through authenticated discovery after a browser restart that retains identity in [FIPS runtime v0.0.53](https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.53). The Nostr-keyed transport bounds recovery attempts and checks for a usable route before signaling. Recovery completion can clear pending state only in its original node generation, preventing stale work from clearing a replacement node's state.

Later [TypeScript runtime v0.0.56](https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.56) restricts nonforwarding browser nodes to advertising their own identity and refreshes cached routing announcements after a fresh authenticated responder carrier. Wire formats, identity checks and session authentication remain unchanged.

Separate Rust source changes [adopt pending key sessions only after authentication](https://github.com/jmcorgan/fips/commit/06312d0c3a5410eb165703afc50a3c6793f25879), even when key-epoch bits match. [Failed decryptions no longer evict live peers](https://github.com/jmcorgan/fips/commit/a52b54b246baffde4d3e97cf3505ef36e601726c) using public receiver indices; authenticated liveness still determines expiry. [Session backoff](https://github.com/jmcorgan/fips/commit/c7fee893c6bf1ee93f55877f08ccb20b0083803f) temporarily refuses repeated silent sessions, while [BLE connection arbitration](https://github.com/jmcorgan/fips/commit/29c89c20374b9cd52989b3f1124802725c398968) addresses shared-connection races. [Rekey guards](https://github.com/jmcorgan/fips/commit/7dde5bf628e7c22f1a0a45c174655b44f804dbe6) reject copied setup messages and off-link attempts, [age and drain floors](https://github.com/jmcorgan/fips/commit/027c3ab3246c0f46be5af0808a7bcfa1567e0e5b) protect session transitions, and [bounded child-filter checks](https://github.com/jmcorgan/fips/commit/ba441c282186a085adcbcab1bf0f625d9e2ec98e) reject apparent echoes with threshold exemptions. These are development changes, with no new Rust release or device validation established.

### Elisym

Elisym, a merchant payment tool, adds [webhook signature and freshness verification](https://github.com/elisymlabs/elisym/pull/166) in [commerce 0.9.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.9.0), [merchant-node 0.9.1](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/merchant-node%400.9.1) and [MCP 0.32.1](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/mcp%400.32.1), an AI-tool interface using the Model Context Protocol. [Checkout changes](https://github.com/elisymlabs/elisym/pull/165) reset closed or reloaded modals while existing payments continue, checking unresolved payments before another wallet request. Those pages lose the order’s onPaid callback; signed backend webhooks remain authoritative. A [durable paid-order webhook outbox](https://github.com/elisymlabs/elisym/pull/155) queues signed retries alongside ledger changes. [Receipts travel over Nostr](https://github.com/elisymlabs/elisym/pull/161), but fulfilment and event-ID deduplication remain merchant-owned; payment completion does not confirm delivery.

### Hashtree

Remote blocks can retain peer-readable provenance after restart through [durable verified-block sharing](https://github.com/mmalmi/hashtree/commit/94918ff549c9c1b716fdd899d2bcccf689bc3128), included in [Hashtree runtime v0.5.19](https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.19). The content-addressed sharing runtime persists hash-verified bytes and authorization before returning. A full or unavailable cache still permits a valid download, but durable sharing cannot be promised for that read.

Later Rust source adds [automatic, bounded peer archive intake](https://github.com/mmalmi/hashtree/commit/6eafa7049e1e78e38391342c2baa7d2061f29e92) alongside relay catchup, using an ephemeral identity and verified events. Peer observations cannot satisfy missing required relay coverage. [Interrupted appends resume](https://github.com/mmalmi/hashtree/commit/849dd9e03a616b0df56c86026545a86d49a9de74) only from matching durable input; author coverage advances after the whole author is durable.

A [standalone Git reader](https://github.com/mmalmi/hashtree/commit/78c4d2f504ff0a5cd956e750203a35ec0e28e877) combines bounded relay observations with public signed index roots while preserving original signatures. Unreachable sources remain distinct from absent repositories. An [explicit expected release root](https://github.com/mmalmi/hashtree/commit/5d2d81c92881aa9934c8c39df9220c7a341bcec0) preserves existing history or stops on conflict; it does not guarantee concurrent publication safety.

### Amethyst

[Amethyst v1.17.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.17.0), an Android Nostr client, includes [document-bound browser signing](https://github.com/vitorpamplona/amethyst/pull/4260) through [NIP-07 browser signing](/en/topics/nip-07/) and [profile updates](https://github.com/vitorpamplona/amethyst/pull/4320). Departed-document messages are discarded; Tor-required pages fail closed on proxy failure, but WebView proxy settings affect other views process-wide. Later merged [QR safety changes](https://github.com/vitorpamplona/amethyst/pull/4359) require confirmation before opening an ambiguous 64-character hex scan as a public profile, avoiding automatic transmission of possible private-key bytes to relays. [Software-release handling](https://github.com/vitorpamplona/amethyst/pull/4355) trusts app branding and downloads only from its publisher or a declared maintainer, and separates stable versions from prereleases.

Later development [limits browser signing prompts](https://github.com/vitorpamplona/amethyst/pull/4352) to 120 seconds and always asks before signing reports. [Encrypted-message history](https://github.com/vitorpamplona/amethyst/pull/4338) now pages only the visible account, prioritizes its DM relay list and offers bounded searches with retry controls. [Relay-hint and search repairs](https://github.com/vitorpamplona/amethyst/pull/4335) reject malformed relay URLs, stop indexing encrypted emoji-pack contents and stop linking anonymous or private zap sender keys; expanded public-text search requires existing stores to be reindexed. The [amy command-line client](https://github.com/vitorpamplona/amethyst/pull/4342) adds posting, threads and deletion while restricting group content to its host relay and refusing group reposts or quotes. The Android app’s own group-repost path remains unchanged. [Paired clients](https://github.com/vitorpamplona/amethyst/commit/9d78ecb0642a3271a2ce5eb386f91e5ef753995c) using [NIP-46, Nostr's remote-signing protocol](/en/topics/nip-46/) bypass the unpaired-client rate limiter; unpaired traffic remains limited to 10 requests per author and 100 combined per minute. Queue and concurrency bounds and per-request authorization remain.

### My Signet

Per-app phone approval is available, default off, in [My Signet v0.18.2](https://github.com/forgesworn/signet-app/releases/tag/v0.18.2), a hardware-signer companion. It requires an imported Heartwood hardware-signer operator key, compatible firmware and a connected, unlocked inbox. Possession of that phone key authorizes enabled requests without touching hardware; "Approve once" can permit the same event kind for ten minutes, while wallet pairing and login codes still require the hardware button.

### Nsync

Signed Nostr address announcements now help paired devices find each other in [Nsync v0.3.0](https://github.com/alanbimbati/Nsync/releases/tag/v0.3.0), a Syncthing-based file synchronizer. Pairing binds each Nostr identity to a Syncthing device ID, and receivers require newer announcements. Files still transfer through Syncthing; relay announcements expose address and online-timing metadata, even with public-IP announcement disabled.

### PsstPsst

[PsstPsst v26.10.1](https://github.com/CodyTseng/psstpsst/releases/tag/v26.10.1) adds small private groups for text, reactions and files through [PsstPsst's group-send implementation](https://github.com/CodyTseng/psstpsst/blob/9da073ad10ad786799e27f4735852b0e2f519814/src/lib/nostr/group-messaging.ts). The messenger extends [NIP-17 private messaging](/en/topics/nip-17/) and [NIP-59 gift wrapping](/en/topics/nip-59/) with encrypted group identifiers and membership actions, using per-recipient [NIP-44 encryption](/en/topics/nip-44/). These extensions remain draft and optional: other clients may split rooms, and any current member can publish membership changes.

### Write Nostr

Encrypted draft and account-settings sync arrives in [Write Nostr's v0.4.11 changes](https://github.com/imattau/write_nostr/compare/v0.4.4...v0.4.11). The writing client commits a draft revision only after every chunk and its head record reach at least one common accepting relay, preserving local content on incomplete or invalid recovery. Signers without NIP-44 support retain local drafts but cannot use encrypted sync.

### Flotilla

Screen sharing joins existing calls through [Flotilla's cross-platform sharing implementation](https://gitea.coracle.social/api/v1/repos/coracle/flotilla/git/commits/e6d4e18f0b68111077a1eba3457661fbc27eabda), released in [Flotilla 1.12.0](https://gitea.coracle.social/coracle/flotilla/releases/tag/1.12.0). The community chat client provides web, Electron and native adapters, including Android MediaProjection and an iOS broadcast-extension path. The release also preserves drafts when sending fails, allowing users to retry without rewriting their message.

### Blitz Wallet

Native Android background handling for [NIP-47 wallet requests](/en/topics/nip-47/) arrives in the [Blitz Wallet Android prerelease](https://github.com/BlitzWallet/BlitzWallet/releases/tag/Android-v0.7.16-pre3). The Lightning wallet shares SQL-backed budget reservations, payment-hash claims and uncertain-payment markers with JavaScript handling, alongside startup fallback and background crash containment. Firebase Cloud Messaging is required, and Android may still need JavaScript execution or an open app.

### Sidecar

Selected web text can be published as [NIP-84 highlights](/en/topics/nip-84/) in [Sidecar v1.15.6](https://github.com/dmnyc/sidecar/releases/tag/v1.15.6). The browser extension's [v1.15.8 composer changes](https://github.com/dmnyc/sidecar/releases/tag/v1.15.8) align mention and quote tags, convert pasted identifiers and skip unanswered relays after 12 seconds, so delivery can remain partial. The [server-discovery repair](https://github.com/dmnyc/sidecar/pull/478) in [v1.15.9](https://github.com/dmnyc/sidecar/releases/tag/v1.15.9) finds Blossom servers through account-declared relays, including write-only relays, and retries failed discovery on the next upload. The same fix covers profile images; nostr.build remains the fallback.

### BuhoGO

BuhoGO, a Bitcoin wallet, releases [1.10.0](https://zapstore.dev/apps/mybuho.buhogo). [Purchased NIP-05 identity names](/en/topics/nip-05/) now survive restarts and delayed relay replies through [durable profile synchronization](https://github.com/Buho-Ecosystem/Buho_go/pull/323). Activation continues after checkout closes, and verified recovery requires no second payment; newer username choices remain authoritative. Android installations older than 1.9.1 use another signing key: back up recovery phrases before uninstalling and reinstalling.

### Staircase

Staircase, an MLS group-chat client over Nostr, releases [0.1.20](https://zapstore.dev/apps/tools.relay.staircase). Its [forwarding and synchronization changes](https://code.relay.tools/opensauce/staircase/-/compare/v0.1.19...v0.1.20) re-encrypt forwarded attachments; captions default off, with no original author, chat or reply metadata. Folders stay local unless multi-device sync encrypts them under derived keys. Search excludes deleted messages and covers device-held history. New accounts use cordn.feeds.relay.tools; existing coordinators remain. Startup key-package reconciliation survives leaving onboarding.

### KithMoot

KithMoot, an encrypted room messenger over Nostr, releases [0.6.62](https://zapstore.dev/apps/dev.forgesworn.kithmoot). [Queued messages](https://github.com/forgesworn/kithmoot-android/pull/177) retry oldest first using their original signed events. Never-sent messages remain editable or deletable; possibly delivered messages can only leave the local pending list. [Saved-room synchronization](https://github.com/forgesworn/kithmoot-android/pull/175) republishes missing relay records using their original signed events, preserving deletion records.

Later merged [0.6.63 preparation](https://github.com/forgesworn/kithmoot-android/pull/195) adds [VMLS rooms on user-operated Bothy servers](https://github.com/forgesworn/kithmoot-android/pull/189), with Nostr invitations and signer-authorized access grants. This preview has no persistent VMLS message history. [Compromised-device removal](https://github.com/forgesworn/kithmoot-android/pull/194) holds new sends and joins until witnessed, revokes keeper-owned grants without grace, and retries unconfirmed revocations; existing traffic may arrive first. Tor-only rooms pause server traffic. Signing, publication and handset acceptance remain pending; downgrades discard removal journals and compromise marks.

Rooms have no end by default; when one is chosen, [self-destruct defaults on](https://github.com/forgesworn/kithmoot-android/pull/192), with a read-only alternative. Cleanup runs with background ringing or delivery enabled, otherwise at next start. It requests deletion of this device's signed events and attempts local cleanup; failed stores, relays or recipients may retain copies. Without a reachable relay, cleanup retries while retaining its signing key.

### Nostr Vault

Nostr Vault, an Android client with an on-device relay, releases [2.7.2](https://zapstore.dev/apps/com.nostrvault.app) with marketplace listings, polls, article highlights and nostrconnect signer pairing. Release notes also report cross-device DM catchup and signature checks; [NIP-29 relay groups](/en/topics/nip-29/) are removed. These are publisher-reported release behaviors, without independent security or background-delivery validation.

### Private Provider

[Private Provider](https://zapstore.dev/apps/xyz.privateprovider) is an Android AI coding workspace that builds APKs on the phone and publishes Nostr repositories through ngit. [Version 0.7.2](https://njump.me/nevent1qqs0yvswv6w9yvz2vv02dgul5hyuppuu0vngcm9gj8lpa3jtem20llspz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzqnjky26htndmf4w76zf7frrge5lhynad23c59uxpkzhv9u4j5zewhq40ud) lets the in-app agent, Pi, request issues, comments and pull requests with explicit command approval and signatures from the Amber Android signer. [0.7.5](https://njump.me/nevent1qqsf6aufz2g20m6uyyqchc86uyhrda5xxw0xxyuw7t6q49ssahz2ksgpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzqnjky26htndmf4w76zf7frrge5lhynad23c59uxpkzhv9u4j5zew0fpk4h) pins Blossom and Zapstore publication targets in a committed manifest and rejects tag/commit mismatches. Wallet recovery remains unavailable; the documentation cautions users to keep only small balances.

### Haps v0.1.11: social-graph package discovery

[Haps v0.1.11](https://github.com/mmalmi/haps/releases/tag/v0.1.11), a Nostr-key package publisher and installer, adds signed immutable bootstrap discovery and publisher-maintained catalogs, preserving custom sources and publisher pins. Search and bare-name installs require a publisher or release voucher from the user's social graph, excluding muted or overmuted people. Explicit `npub/package` installs warn outside that graph; trusted warnings block installation. The installer [retains its verified selection](https://github.com/mmalmi/haps/commit/f8f999123465b1bb64bf41a1903746bf5fa64459). Signatures establish authorship, not safety: native programs and build recipes remain unsandboxed; package formats remain unstable.

### soyLI

soyLI [v0.25.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.25.0), a toolkit for publishing sandboxed Nostr apps, uses creators' own [NIP-34 Git repositories](/en/topics/nip-34/), checking signed refs and clone reachability again on resume. It avoids duplicate repositories and retains linked source on deletion. Remote dynamic backends still require soyLI-managed source. [Earlier changes](https://github.com/zeSchlausKwab/napplet-soy/commit/8f809650b2fe4d1fd4f6bf045159d28868a893ae) accept [NIP-22 replies](/en/topics/nip-22/) with extra mentions and prevent a relay-handshake timeout race from terminating the web process.

### fips2go

fips2go, an Android mesh client using Nostr-signed domain bindings, releases [0.9.4](https://github.com/fr34aky/fips2go/releases/tag/v0.9.4) and [0.9.5](https://github.com/fr34aky/fips2go/releases/tag/v0.9.5). [Fallback TTLs](https://github.com/fr34aky/fips-pub-domains/pull/21) [follow retries](https://github.com/fr34aky/fips2go/pull/74), initially 20 seconds, tripling to three hours. [Cached mesh answers](https://github.com/fr34aky/fips-pub-domains/pull/23) [avoid parallel DNS](https://github.com/fr34aky/fips2go/pull/79); ordinary fallback still queries upstreams. [First denials](https://github.com/fr34aky/fips-pub-domains/pull/22) release fallback while validation continues. Its resolver supports [configured offline witness quorums](https://github.com/fr34aky/fips-pub-domains/pull/12), [excluding self-vouching](https://github.com/fr34aky/fips-pub-domains/pull/17); pins and DNS retain precedence. Desktop operators may [disable plain probes](https://github.com/fr34aky/fips-pub-domains/pull/20) with DNSSEC; default probing remains enabled. Phone probing follows connectivity validation. Denials do not authenticate targets.

## In Development

### Dart NDK

Dart NDK, a Dart and Flutter Nostr toolkit, adds [authentication consent controls](https://github.com/relaystr/ndk/pull/862) for relays and Blossom servers. Without an explicit policy or consent handler, relay operations stop authenticating automatically as the logged account and default Blossom writes use throwaway keys. Signed events still identify their authors. Its [NIP-46 relay switching](https://github.com/relaystr/ndk/pull/851) follows a signer's replacement relay list; applications must persist the updated connection. These are merged changes, with no tagged release established.

### MintRadar

MintRadar, a Cashu mint directory with signed Nostr reviews, [restricts shared-link relay hints](https://github.com/hroomnik007/MintRadar/commit/be94d29852963fca47570d974b997e4ab57e1915) to three known relays plus its defaults, and caps account-list connections at ten public secure-WebSocket hosts. Its new [server profile index](https://github.com/hroomnik007/MintRadar/commit/f6e5e07d354f2e0ba380e709119c33b91d810890) supplies reviewer names when browser lookup finds none; internet identifiers remain labeled as claims until separately verified. These are main-branch changes, with deployment unverified.

### LNbits

LNbits, a Lightning service with Nostr notifications, [lets WASM extensions request user notifications](https://github.com/lnbits/lnbits/pull/4222) under an explicit permission. The host selects the current user or invocation wallet owner and their saved Nostr, email or Telegram settings; extensions cannot supply an arbitrary recipient. This is merged development work, and a queued response does not guarantee delivery.

### Zeus

Zeus, a Lightning wallet, [repairs LDK routing-fee reporting](https://github.com/ZeusLN/zeus/pull/4353) used by [Nostr Wallet Connect](/en/topics/nip-47/), allowing responses and connection spending to include the reported fee. Budget checks still cover the invoice amount before settlement and debit rounded fees afterward; the service uses a separate 1,000-satoshi routing-fee cap. This is merged source work, with no release established in the window.

### Pollerama

[Pollerama](https://pollerama.fun), a Nostr polls and feeds client, [repairs encrypted-message delivery](https://github.com/formstr-hq/nostr-polls/pull/249) by waiting for relay-authentication acknowledgement before replaying subscriptions on relay.formstr.app. Its local-relay library discards signing results from replaced sockets and directs outgoing gift-wrapped messages to the recipient's declared inbox relays.

### Nostur

Nostur, an iOS Nostr client, [adds kind 16 generic repost support](https://github.com/nostur-com/nostur-ios-public/commit/74e5fbe12ad983af0dad1c37257a726f68df35d6) across feeds, rendering and event references, so reposts of other event types can resolve their original content. A [saved-repost repair](https://github.com/nostur-com/nostur-ios-public/commit/f286a8c8c01ccdf2febe2d566f7bce443ae26daa) restores missing target links when those reposts are reopened, validating embedded events before using them. Existing repost counts are preserved.

### Gittr

Gittr, a Nostr-based Git platform, [repairs Settings deletion requests that could fail to reach Amber](https://github.com/arbadacarbaYK/gittr/commit/92a25de1ec8bb58f945711c66e5f1ed54f2df82f). Subscriptions measure their wait from the current signer-connection pause, and a saved signer identity can proceed to signing when the initial connection warmup finds no open socket. This repairs signer contact; it does not establish that deletion has completed across relays.

### NosTube

NosTube, a Nostr video client, [adds a separate instance build](https://github.com/flox1an/nostube/commit/296ef99bed50771ea3d2a11c08343575608d222b) that loads server configuration before starting the app and limits its video catalog to configured creators and sources. [Signer and wallet connections](https://github.com/flox1an/nostube/commit/1b02423abdfc4f26b1b74081e2ab396310ac1ba6) retain their own relay access. [Admin routes](https://github.com/flox1an/nostube/commit/047ec6ad9af2ef487a3bce2f9510f8a0d35da2a1) are served by nostube-server. Search remains disabled in this initial instance variant.

### eHagaki

eHagaki, a Nostr client, [stores content-warning bodies separately](https://github.com/Lokuyow/ehagaki/pull/284) in verified kind 36 payloads before publishing the original event structure. [Only compatible clients](https://github.com/Lokuyow/ehagaki/pull/294) retrieve and display those bodies; the warning does not encrypt them. [Local history search](https://github.com/Lokuyow/ehagaki/pull/290) now streams its first 50 matches while scanning continues, then reports the exact total.

### Nostr Components

Nostr Components, a web-component toolkit, [adds signed profile and relay records and URL-activity APIs](https://github.com/saiy2k/nostr-components/pull/164). Zap capability stays unknown until checked, and ingestion stores an event only after a sweep relay returns it. These changes are merged development work; deployment remains pending.

### Holoboard

Holoboard, a paid Nostr note-promotion board, [preserves unfinished promotion payments](https://github.com/ptrio42/holoboard.space/commit/55b26ff3f06846a8ca15bac9ad28ff0c56157650) when users return to editing or switch notes. Earlier invoices remain available for explicit resume, and late wallet replies update their own payment record. Unconfirmed payments retain a warning that they may already have succeeded. Issued invoices remain payable; returning to the editor neither cancels them nor refunds a payment. Failed browser storage leaves a visible notice.

### Milk Market

Milk Market, a Nostr marketplace, adds [mobile seller shipping](https://github.com/shopstr-eng/self-sown/pull/33), [return labels and optional activity alerts](https://github.com/shopstr-eng/self-sown/pull/34), and [native catalog editing](https://github.com/shopstr-eng/self-sown/pull/36). Return labels preserve outbound tracking and order status; uncertain label purchases keep their duplicate-prevention records. Catalog editors reject stale or wrong-owner edits and protect sold stock from duplicate retries. Server push remains disabled unless explicitly configured.

### NYM

NYM, a Nostr chat client, changes [notification handling](https://github.com/Spl0itable/NYM/commit/c2488e4052c646b1d0a3bbc944b23518ad355dec) so service-worker notification clicks reopen the relevant private, group or location conversation, with page notifications as a fallback. Unread in-app toasts held while a sheet was open remain eligible after their ordinary timeout. System notifications still require permission and browser support.

[Client AI consent and account-deletion changes](https://github.com/Spl0itable/NYM/commit/5c36b87cc05e850ba9ffb2b20d7416d8f7cf1aa2) add prompts before bot processing and translation; bot consent can also enable translation. Requests may share conversation or channel context, including other people’s recent messages and approximate location, with the service and selected model providers. Deletion attempts cover usable saved identities and local wiping, but public relay copies, inaccessible identities and external backups can remain, and some server-cleanup errors are not surfaced. Closed-app ringing is opt-in for one identity per phone.

### Nostr Inspect

Nostr Inspect, an event-inspection tool formerly called Nostr Events Monitor, adds [browser-side signature and content-ID checks](https://github.com/Catrya/nostr-inspect/pull/26), [address lookup and relay-copy status](https://github.com/Catrya/nostr-inspect/pull/28), plus [exact-event or latest-address sharing](https://github.com/Catrya/nostr-inspect/pull/30). Latest means the newest valid copy observed from queried relays, which may withhold other copies. [Shared search filters](https://github.com/Catrya/nostr-inspect/pull/31) run ordinary searches on opening; streaming needs a user start. The [rename](https://github.com/Catrya/nostr-inspect/pull/32) resets existing browser settings and repeats the walkthrough once. These changes are merged source work.

### Bark

Bark, a browser extension using [NIP-46](/en/topics/nip-46/) remote signing, [serializes signer handshakes](https://github.com/forgesworn/bark/pull/47) so concurrent requests wait for the existing attempt. Each handshake keeps its own signer; superseded work cannot clear a replacement connection or return its signer. Failed candidates close, stale relay-health results are ignored, and the current signer can still request approval. This is merged recovery work; live Heartwood hardware-signer acceptance remains unverified.

### NoorNote

NoorNote, a Nostr client, adds [website-manifest cards](https://github.com/77elements/noornote/commit/f516a76eea45995452c96d0904b029218c2937ea) with normal note interactions, a Websites profile tab and named-site address routing. [Unsupported-event cards](https://github.com/77elements/noornote/commit/e4cdb976503712bbec452a67de1fff29eaf1281e) gain navigation and copy/raw-event menus. Website support is display-side development: it neither publishes sites nor adds manifests to ordinary feed filters. Gateway and source links open on user clicks; the client does not automatically fetch or validate website contents.

### Wisp

Wisp, a Nostr client, adds [Android signature verification before delivery and deduplication](https://github.com/barrydeen/wisp/pull/665), preventing invalid events with matching IDs from hiding valid posts. Verification uses bounded workers and fails closed; authentication also fences stale identities. The write queue remains unbounded.

### Meiso

Meiso, a task app, adds [automatic synchronization safeguards in 1.4.1](https://github.com/higedamc/meiso/pull/180): failed reads no longer become empty lists, publishing requires a successful session fetch, and large list shrinkage needs confirmation. Failed sends remain pending synchronization. Manual sync bypasses these guards, and local tasks absent remotely for 24 hours can still be deleted without causal deletion tracking.

### ZapTracker

ZapTracker, a publishing dashboard, adds source-level [RSS and Atom publishing](https://github.com/pratik227/zap_dashboard/pull/136) as articles or short posts, plus [media and self-thread export/import](https://github.com/pratik227/zap_dashboard/pull/137). Automatic publishing requires the app to remain open with a signer and handles at most three new items per feed; backlog publishing is manual. Deduplication is account-local, so clearing history can permit repeats.

### Formstr Drive

Formstr Drive, an encrypted file-sharing app, moves files into [single encrypted Blossom blobs](https://github.com/formstr-hq/formstr-drive/pull/69) and adds [range previews and key-separated sharing links](https://github.com/formstr-hq/formstr-drive/pull/72). Partial previews require server range support. Folder-share creation remains unwired, and old sharing links are intentionally incompatible, although old blobs remain readable.

### Safebox Acorn

Safebox Acorn, a wallet component, adds a [validated private-message reader and recipient inbox routing](https://github.com/trbouma/safebox-acorn/commit/2b20845816615a71d6577aa130a0550972669dc7) using [NIP-17](/en/topics/nip-17/), Nostr's private messaging protocol. Landed code checks envelope signatures and author/recipient agreement, separates payment envelopes from ordinary chat, and reports absent routes explicitly. Ambiguous sends require checking before resending. Retrieval stops at 100 outer events, including excluded payment envelopes.

### Minibits

Minibits, an ecash wallet, adds [persistent NIP-17 conversations for text, ecash and payment requests](https://github.com/minibits-cash/minibits_wallet/commit/ca896f364ba7a6a51f387af94d2094648133cbf5), with unread indicators and unknown-contact requests. Separate sender copies and message deduplication prevent outgoing funds from being counted as incoming. Conversations display at most 500 messages without paging; relay acceptance leaves delivery and reading unconfirmed.

### LaWallet

LaWallet, a wallet service, merges an [OAuth 2.1 MCP interface for balance, invoice and payment tools](https://github.com/lawalletio/lawallet-nwc/pull/327), with explicit permissions and daily connection budgets. A companion [listener-secret safeguard](https://github.com/lawalletio/lawallet-nwc/pull/326) restricts stored-secret fallback to the configured origin. Pending and unknown payments remain accounted for, but concurrent grants lack a global exactly-once guarantee, and fee reserves do not enforce a total fee cap.

### Zap Cooking

Zap Cooking, a recipe-sharing client, makes [Fresh the default feed](https://github.com/zapcooking/frontend/pull/785), with an isolated relay connection and public 14-day access. Deeper history and topic access request [NIP-42](/en/topics/nip-42/) relay authentication lazily, limiting unsolicited identity disclosure. Merged [comment interoperability changes](https://github.com/zapcooking/frontend/pull/767) preserve root and parent relationships when reading and replying. Relay policy controls access; reply counters still omit some comments.

Later main changes route [reactions, comments and zap-receipt requests](https://github.com/zapcooking/frontend/pull/791), plus [reposts and lists](https://github.com/zapcooking/frontend/pull/792), through authors' write relays, recipient read relays and the app list. Lists omit recipient fan-out; group events stay on Pantry. Routing failure can still fall back to the pool. Extension and remote-signer relay login gets one attempt per account, relay and page load; reconnects may remain logged out until reload. Pantry and local keys are exempt. Members also gain [topic-labeled day and month archives](https://github.com/zapcooking/frontend/pull/793), subject to relay access and paging limits.

### Kehto / Paja

Kehto's Paja transport, for [ContextVM remote tool calls over Nostr](/en/topics/contextvm/), adds [bounded oversized transfers and streaming progress](https://github.com/kehto/web/pull/265). Server identity and typed request tokens prevent chunks or progress from attaching to the wrong concurrent request; completed transfers require matching byte length and hash. Idle probes monitor streams, while the final response or deadline determines completion.

### Notedeck

Notedeck, a desktop Nostr client, lets its Dave AI-agent conversations exceed individual note limits through [UTF-8-safe signed multipart messages and reassembly](https://github.com/damus-io/notedeck/commit/a3551845a504711641b95829bda36ae02a6a2789). Readers check authorship and part completeness before reconstructing messages. Older devices display separate parts; reconstruction requires every part locally.

### diVine

diVine, a video-sharing client, adds [author-checked comment deletion across pages, reconnects and live updates](https://github.com/divinevideo/divine-mobile/pull/9751) using [NIP-09](/en/topics/nip-09/), Nostr's deletion-request protocol. Merged code waits for a relay acknowledgement before reporting deletion success and caches the user's deletion requests for offline reads. A two-second lookup timeout leaves comments visible, and live filtering requires a comment-kind tag.

### Conduit

Conduit's public Nostr reader/writer adds [verification against detached canonical signed fields](https://github.com/Conduit-BTC/conduit-mono/pull/606), separating relay provenance from mutable events. [Relay settings](https://github.com/Conduit-BTC/conduit-mono/pull/638) permit another explicit edit and review while an earlier signed update awaits confirmation; exact retry preserves unsigned drafts, with counts behind “Confirmation details.” Signing and publication still serialize, with independent relay-list and inbox checkpoints. Observed provenance is not exhaustive relay coverage; external-signer behavior and public-relay convergence remain unverified.

### Buzz

Buzz, a community relay, adds [community-scoped federation enforcement](https://github.com/block/buzz/pull/8028): the request host selects the community, which must authorize the issuer before signing-key retrieval, and the assertion audience must match that community. Merged [shadow-mode evaluation](https://github.com/block/buzz/pull/8034) records would-deny outcomes across HTTP, WebSocket and audio without denying admission or closing observed sessions. Enforcement requires operator-supplied community configuration; shadow metrics exclude some earlier refusals.

Merged work keeps [agent-to-agent replies inside threads](https://github.com/block/buzz/pull/8124) and [retries uncertain sibling-agent authorization lookups](https://github.com/block/buzz/pull/7216) while denying the current event. An optional [read-state/sidebar API](https://github.com/block/buzz/pull/7906) remains disabled by default: database operators can read its plaintext state, and it does not synchronize with legacy read-state events. [Deletion cleanup](https://github.com/block/buzz/pull/8128) purges retention-free read-state and heartbeat rows with their mentions; ordinary deleted history remains soft-deleted.

## New Projects

### cvm-registry

[cvm-registry caches ContextVM service discovery](https://gitworkshop.dev/npub1nng5mxkdh2mu593twukfr7j3fk5wxfy0v8ujf0e5g8nwwtzlphhqksqpew/relay.ngit.dev/cvm-registry), using a curator allowlist and explicit fresh or expired catalog states to help users assess service listings. This static discovery dashboard makes catalog age visible, but its restaurant demonstration does not invoke services, make payments or settle transactions.

### Nostr Workshop

[Nostr Workshop's phone milestone](https://npub1nhf36h08krl0ts8r9amkwq5eq9mjhq82kz7dxcfza2hmlkqdhn3qt2t4q6.nsite.lol/) provides phone-oriented learning tasks, a signer bridge and encrypted key backups, with published results updating task progress. The browser signer holds the unlocked private key in plaintext per-tab sessionStorage until Lock; lasting use calls for transferring the encrypted backup to a dedicated signer. The newer source milestone is not attested to the listed APK.

### Nostella

[Nostella's experimental relay mesh authenticates forwarded requests](https://relay.ngit.dev/npub1600yr4qg5vcfp7svf6ysj0008tn7aphnu0gjs6lw5hjn74n0laasjx889v/nostella.git) and gives them stable identities to stop recursive amplification. Bounded forwarding to ordinary relays preserves filters and limits. Remote results arrive after the local end-of-stored-events signal, so clients that close their subscription at that signal miss those results.

### nope-mcp

[nope-mcp adds connector metadata and default open-license filtering](https://gitworkshop.dev/npub1r30l8j4vmppvq8w23umcyvd3vct4zmfpfkn4c7h2h057rmlfcrmq9xt9ma/relay.ngit.dev/amb-mcp) to educational-resource search across Nostr relays, exposing it through a public MCP interface without signing or mutation tools. Resources missing license tags are excluded by default.

### Vitals

[Vitals implements owner-authorized monitoring sessions](https://npub1zzndrnyy0cf6n4m3y5flcndavp08p05cesmacqylq6r6ca8pldhshda6w9.nsite.lol/), with a Linux daemon sending ephemeral machine reports encrypted using [NIP-44, Nostr's encrypted-message format](/en/topics/nip-44/). Five-minute keepalives extend a seven-minute session timeout. Closing the browser sends no signed stop, leaving monitoring to expire by timeout; the daemon is a prototype.

### grasp-go-proxy

[grasp-go-proxy exposes Nostr repository discovery to Go tooling](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/grasp-go-proxy.git), resolving npub, naddr and [NIP-05 human-readable identifiers](/en/topics/nip-05/) for [NIP-34 Git repository announcements](/en/topics/nip-34/) into go-import metadata pointing at existing Git hosts.


### Keythra

[Keythra adds a Mac-mediated remote signer](https://github.com/gmkbenjamin/keythra/commit/155eec9bc635cc1f2cbc37302d461e45caaa49ab) using [NIP-46, Nostr's remote-signing protocol](/en/topics/nip-46/), forwarding authorized applications' requests to an iPhone or local authenticator. Each signing, encryption or decryption operation requests user verification, with event IDs derived from approved fields. This remains a prototype source milestone: the Mac bridge must stay running, Nostr keys remain in software storage.

## Protocol and Spec Work

### Profile image metadata matched by exact URL

The merged [NIP-92 profile metadata change](https://github.com/nostr-protocol/nips/pull/2494) lets clients associate profile pictures and banners with [NIP-92](/en/topics/nip-92/), the media metadata format, only when URLs match exactly. Clients ignore unmatched tags and may use fallback URLs if the primary fails. Updates preserve metadata for unchanged fields and drop obsolete tags; the merge establishes specification behavior, not shipped client support.

### Signed descriptors for napplets

The open napplet proposal, for self-contained HTML applications, now uses a [signed descriptor tied to one HTML hash](https://github.com/nostr-protocol/nips/commit/020cb8b33a9e4c6b8ca4b2f9d0ed0a67843b68f7). It declares required and optional capabilities, intents, icons and a plaintext description, replacing the aggregate/path model. HTML publishing metadata cannot override the signed descriptor's authority; this remains proposed protocol text.

The [napplet CLI v0.7.0](https://github.com/napplet/web/releases/tag/%40napplet/cli%400.7.0) [implements the descriptor format and offline migration](https://github.com/napplet/web/pull/224). Unattended publishing defaults to the current format; a temporary explicit legacy option supports older shells. Migration verifies the original signed event and emits an unsigned template for review, without fetching, executing, signing or publishing its HTML. Ambiguous multi-file manifests must be rebundled, and permission and storage identities change to the artifact hash. [Explicit unknown capability declarations](https://github.com/napplet/web/pull/223) are retained with warnings; shells still decide whether they can load the app.

### Financial cashtags with separate binding and indexing

The [financial cashtag proposal](https://github.com/nostr-protocol/nips/pull/2491) separates a cashtag's location in text from its indexed financial identity. Non-indexed `cashtag` tags bind text using UTF-8 byte offsets, while [NIP-73](/en/topics/nip-73/), the external-identifier tagging convention, supplies `i` tags for symbol and instrument indexing. The proposal covers ISIN, FIGI, CAIP-19 and ISO-4217 identities, not prices or payments; implemented adoption is not established.

### Marmot membership requests and receipts

A proposed [Marmot membership workflow](https://github.com/marmot-protocol/marmot/pull/432), for encrypted group messaging, adds optional inner kind-458 requests, rejections, withdrawals and Applied receipts. Administrators independently validate KeyPackages, and an Applied receipt requires a matching accepted Commit. These checks tie receipts to accepted membership changes; the fixtures assume Messaging Layer Security group-key authorization facts and do not prove convergence.

### Marmot multi-device pairing security

Merged [Marmot multi-device design notes](https://github.com/marmot-protocol/marmot/pull/430) introduce private, single-use KeyPackages, a device-group roster, commitment-based pairing and ordered settings. The design addresses substitution, KeyPackage reuse and offline-searchable pairing. Normative wire definitions and interoperable device support remain unfinished.

### Wallet Connect commission invoices

The unimplemented [Nostr Wallet Connect commission proposal](https://github.com/nostr-wallet-connect/nwc/pull/9), for wallet-to-app communication, adds an optional `make_commission_invoice` permission governed by user-confirmed rate, payee, fee and budget limits. Shared-hash hold invoices coordinate payments, with idempotent retries to prevent duplicate requests. A preimage does not prove payment, and client delays and colluding routing remain risks.

### Cyberspace virtual brackets

The Cyberspace spatial protocol [specifies virtual brackets](https://github.com/arkin0x/cyberspace/pull/44) for games identified by their public keys. An `enter-virtual` action names the game in a `p` tag and records base and game positions; an exit returns to the entry’s base position. Verifiers follow links through unrecognized actions and compare recognized positions with the preceding recognized action, so a skipped action that moved the identity invalidates the chain. Existing client verifiers still need implementation changes.

## NIP Deep Dive: NIP-05 and NIP-24

[NIP-05](/en/topics/nip-05/), human-readable account identifiers, connects `local@domain` to a public key; [NIP-24](/en/topics/nip-24/), additional profile metadata, makes public presentation portable across clients. The [NIP-05 specification](https://github.com/nostr-protocol/nips/blob/master/05.md) is merged, final and optional. The [NIP-24 specification](https://github.com/nostr-protocol/nips/blob/master/24.md) is merged, draft and optional: draft describes its maturity, not a newly opened proposal.

### Checking an account name

After validating the signed profile, read `nip05` from its JSON-string `content`. Split the identifier and request `https://<domain>/.well-known/nostr.json?name=<local>` over HTTPS, ignoring redirects. The local part permits `a-z0-9-_.`; the response's `names[local]` must equal the author's hexadecimal public key. Optional `relays` supplies discovery hints, not authenticated relay endorsements. `_@domain` is a root identifier that may display as the domain, according to the [lookup specification](https://github.com/nostr-protocol/nips/blob/master/05.md).

Identifier-first discovery fetches the mapping, then the key's profile and matching claim. Follows retain the public key: domain reassignment invalidates the old name association without transferring the follow. This proves an association, not legal identity or biography; the email-like string implies no mailbox. Missing names, mismatched keys, invalid JSON, redirects and unreachable endpoints cannot establish it. Browser CORS failures are indistinguishable from other fetch failures under the [NIP-05 rules](https://github.com/nostr-protocol/nips/blob/master/05.md).

The identifier server receives the requested name and may observe the client's network origin. External profile images can also reveal browsing activity to their hosts. Neither specification supplies a universal privacy proxy or cache policy; changing mappings require revalidation. NIP-05 began with [June 18, 2021's DNS-name introduction](https://github.com/nostr-protocol/nostr/commit/1aebb3911c5cc024a1de24cdc7087790b5c092ee), followed by [December's well-known JSON revision](https://github.com/nostr-protocol/nostr/commit/012ebff47d2649b37158db5105f10e3bc777f43c).

### Portable metadata and its limits

NIP-24 adds optional `display_name`, `website`, `banner`, Boolean `bot` and object `birthday`, whose year, month and day may each be omitted. Authors should still supply `name`; deprecated `displayName` and `username` should be ignored or removed. Partial birthdays reduce disclosure, but supplied details remain public. The [metadata specification](https://github.com/nostr-protocol/nips/blob/master/24.md) defines fields, not universal recovery from wrong types, invalid dates or duplicate keys.

Generic `r`, `i`, `title` and lowercase `t` tags mean web URL, external identifier, named item and hashtag unless a more specific specification overrides them. Historical kind-3 relay-map content is deprecated in favor of [NIP-65](/en/topics/nip-65/), relay-list metadata. [NIP-24's introduction](https://github.com/nostr-protocol/nips/commit/44c21c9d82dfa9fbe04655668c03400fa0ac1e34) was authored September 24 and committed September 26, 2023. [NIP-92](/en/topics/nip-92/), media attachment metadata, now permits [profile-image descriptions](https://github.com/nostr-protocol/nips/pull/2494) through URL-matched `imeta` tags.

### One signed profile, both specifications

This kind-0 profile was recovered from relay.damus.io on October 6. Under [NIP-01](/en/topics/nip-01/), basic event structure, `id` is the canonical event hash, `pubkey` the signing identity, `created_at` the author-provided Unix timestamp, `kind:0` the replaceable profile type, `tags` the event tags, `content` the exact profile JSON string, and `sig` the signature. The [event specification](https://github.com/nostr-protocol/nips/blob/master/01.md) authenticates payload integrity, not its truth.

```json
{
  "kind": 0,
  "id": "700f005cff9fcd93268053f9fda0d4f3cccb0847fc6aa4547ba80c622b98aa3a",
  "pubkey": "208ad03138eb32da4b3fb2edb79d13a8e3532842db627d76aff8168db564a0e9",
  "created_at": 1791295764,
  "tags": [
    [
      "client",
      "Nostrich"
    ]
  ],
  "content": "{\"name\":\"calavera\",\"nip05\":\"calavera@primal.net\",\"about\":\"Audentes Fortuna Iuvat\\nLe mie gesta sul video ludo 👇\",\"lud16\":\"solartern74@nostrich.org\",\"display_name\":\"Manny Calavera\",\"picture\":\"https://m.primal.net/OHcz.jpg\",\"banner\":\"https://m.primal.net/OHdW.gif\",\"website\":\"https://rumble.com/user/HomoLudensArchive\"}",
  "sig": "9bc7be81b87a7db10f812e23181fda38d5e369c49d9a52757b16fb4ff0ad544abb24486b346382d5f43fc127794ac0562d80e6e4a7df8489512f40ffbedcf670"
}
```

Here `name` is the short label, `display_name` the richer label, and `nip05` the separately checked association. `picture` and `banner` are image URLs, `website` an author-supplied link, and `about` self-description. `lud16` is a payment-address extension, not identity verification. The `client` tag self-asserts application context. No `imeta`, bot or birthday appears; [NIP-24's optional fields](https://github.com/nostr-protocol/nips/blob/master/24.md) need not all be present.

### Implementation boundaries

Amethyst's [lookup client](https://github.com/vitorpamplona/amethyst/blob/c9901247666feb0485f4b0137831092cbc924d74/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip05DnsIdentifiers/Nip05Client.kt) compares the mapped key, while its [birthday decoder](https://github.com/vitorpamplona/amethyst/blob/c9901247666feb0485f4b0137831092cbc924d74/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip01Core/metadata/BirthdayTolerantSerializer.kt) ignores undecodable birthday fields and retains the profile. The Damus client's [lookup](https://github.com/damus-io/damus/blob/4a94f666d7e159e380e10b4dbbb2967d1688709e/damus/Features/NIP05/Models/NIP05.swift) models names without explicit redirect rejection in that file, and its [profile bindings](https://github.com/damus-io/damus/blob/4a94f666d7e159e380e10b4dbbb2967d1688709e/nostrdb/src/bindings/swift/NdbProfile.swift) expose display name, website and banner. The rust-nostr library's [identifier types](https://github.com/rust-nostr/nostr/blob/463f0c2d48e1d3c9e295cc231715d8a3855c65d3/nostr/src/nips/nip05.rs) support root lookup and relay hints, while its [metadata decoder](https://github.com/rust-nostr/nostr/blob/463f0c2d48e1d3c9e295cc231715d8a3855c65d3/nostr/src/nips/nip01/mod.rs) preserves custom JSON but can reject wrong types in known fields.
