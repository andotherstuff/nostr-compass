---
title: 'Nostr Compass #12'
date: 2026-03-04
publishDate: 2026-03-04
draft: true
type: newsletters
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** The [Marmot Development Kit](https://github.com/marmot-protocol/mdk) ships its [first public release](#marmot-development-kit-ships-first-public-release) with encrypted media and multi-language bindings. [Nostrability](https://github.com/nostrability/outbox) publishes [outbox model benchmarks](#outbox-model-under-the-microscope) across 14 relay selection algorithms. [Wisp](https://github.com/barrydeen/wisp) goes from [first alpha to beta](#wisp-ships-from-alpha-to-beta) in eight days with Tor and [NIP-55](/en/topics/nip-55/) (Android Signer Application) signing. [NIP-91](#nip-updates) (AND filters) merges. [Vector v0.3.1](#vector-v031) delivers negentropy sync with 15x performance gains. This issue also includes the Five Years of Nostr Februaries retrospective, tracing the protocol from a spec rewrite serving three relays through the Damus App Store explosion to mesh networking and AI agent proposals.

## News

### Outbox Model Under the Microscope

[Nostrability](https://github.com/nostrability/outbox) published a series of outbox model benchmarks testing how well different relay selection algorithms retrieve events from the decentralized relay network. The project merged 16 PRs and 76 commits in ten days, producing what may be the most thorough empirical analysis of [NIP-65](/en/topics/nip-65/) (Relay List Metadata) implementation strategies to date.

The benchmarks test 14 relay selection algorithms against real-world follow lists across 15 clients and libraries in five languages. A baseline approach of querying only popular relays retrieves roughly 26% of events. Greedy set-cover with Thompson Sampling reaches 80-90% recall. Adding a latency-aware variant using hyperbolic discounting and EWMA relay latency tracking pushed completeness from 62-80% to 72-96% at the 2-second mark across six test profiles.

[NIP-66](/en/topics/nip-66/) (Relay Monitoring) dead relay filtering proved consequential. Pre-filtering relay candidates against [nostr.watch](https://nostr.watch) liveness data removed 40-64% of dead relays and doubled relay success rates from 30% to 75-85%. Feed load times dropped 39% (from 40 seconds to 24 seconds across 10 profiles). An EOSE-race simulation found that waiting for EOSE plus a 200ms grace period improved completeness over stopping at the first relay to finish.

For clients that cannot fully rewrite their relay routing, a "hybrid outbox enrichment" approach adds per-author outbox queries on top of existing hardcoded app relays. This hybrid achieved 80% one-year event recall versus the 26% baseline, offering a migration path for clients with legacy relay architectures.

### ContextVM Opens MCP NIP and Ships Ephemeral Gift Wraps

[ContextVM](https://contextvm.org), the protocol bridging Nostr with the [Model Context Protocol](https://modelcontextprotocol.io/), opened two proposals in the [NIPs repository](https://github.com/nostr-protocol/nips) this week. [PR #2246](https://github.com/nostr-protocol/nips/pull/2246) formalizes CVM as a convention for transporting MCP JSON-RPC messages over Nostr using ephemeral kind 25910 events. [PR #2245](https://github.com/nostr-protocol/nips/pull/2245) extends [NIP-59](/en/topics/nip-59/) (Gift Wrap) with an ephemeral kind (21059) that follows [NIP-01](/en/topics/nip-01/) (Basic Protocol Flow) ephemeral semantics, letting relays discard wrapped messages after delivery.

The ephemeral gift wrap convention shipped as [CEP-19](https://docs.contextvm.org/spec/ceps/cep-19/) in the ContextVM SDK v0.6.x release family. The [SDK implementation](https://github.com/ContextVM/sdk) adds a `GiftWrapMode` enum with three settings: OPTIONAL (accept both kinds and auto-detect peer capability), EPHEMERAL (kind 21059 only), and PERSISTENT (kind 1059 only). For AI tool calls, ephemeral mode avoids storing intermediate request-response traffic on relays, reducing both storage costs and privacy exposure.

New public MCP servers appeared on the network from independent operators, including a Wolfram Alpha query server. The ContextVM team published CEP-15 (common tools schema) and CEP-17 (server relay list publication) alongside the v0.6.x release cycle.

### Marmot Development Kit Ships First Public Release

[MDK](https://github.com/marmot-protocol/mdk) (Marmot Development Kit), the Rust library powering [Marmot](/en/topics/mls/)-encrypted messaging across [Pika](https://github.com/sledtools/pika) and [White Noise](https://github.com/marmot-protocol/whitenoise), shipped [v0.6.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.6.0) as its first public release. Over 200 PRs merged into this version, with six new contributors.

The release includes encrypted media support (MIP-04) with HKDF seed derivation (MIP-01 v2), deterministic commit race resolution (MIP-03), encrypted local storage, admin authorization validation for Marmot commits and proposals, and GREASE support for protocol extensibility. Bindings ship for Kotlin, Python, Ruby, and Windows alongside Android cross-compilation. The library upgrades to OpenMLS 0.8.0 with security advisory fixes and a `Secret<T>` type that zeroizes sensitive values in memory.

A companion protocol change ([MIP-03](https://github.com/marmot-protocol/marmot/pull/48)) replaced [NIP-44](/en/topics/nip-44/) (Encrypted Payloads) encryption with ChaCha20-Poly1305 for kind 445 messages. NIP-44 required UTF-8 string input per its specification, making it impossible to pass raw Marmot message bytes through standard TypeScript Nostr libraries. The replacement derives keys directly from the Marmot exporter secret. This breaking change required coordinated updates across the [core spec](https://github.com/marmot-protocol/marmot/pull/48), [MDK](https://github.com/marmot-protocol/mdk/pull/208), and [TypeScript SDK](https://github.com/marmot-protocol/marmot-ts/pull/54).

[marmot-ts](https://github.com/marmot-protocol/marmot-ts), the TypeScript implementation maintained by hzrd149, merged four PRs with breaking API changes in its own right. An [omnibus update](https://github.com/marmot-protocol/marmot-ts/pull/52) added a key package manager for create/publish/rotate lifecycle, a `sendChatMessage` convenience method, invite preview without joining (`readInviteGroupInfo`), self-update for forward-secrecy rotations, and structured debug logging. Group decryption APIs were renamed from `readGroupMessage` to `decryptGroupMessage` with richer result variants (processed/skipped/rejected/unreadable). gzuuus contributed example cleanup with NIP-65 relay support and last-resort key package handling per MIP-00.

The [White Noise CLI](https://github.com/marmot-protocol/whitenoise-rs) (`wn`), the Rust backend powering both the mobile app and the new TUI, merged 16 PRs in ten days. Signer lifecycle handling gained cancellation safety through an RAII scope guard ([PR #538](https://github.com/marmot-protocol/whitenoise-rs/pull/538)), fixing a class of bugs where aborted operations could leak signer state. Login now blocks when required relay lists (kind 10002/10050/10051) are missing ([PR #515](https://github.com/marmot-protocol/whitenoise-rs/pull/515)), and giftwrap subscriptions fall back to [NIP-65](/en/topics/nip-65/) relays when inbox lists are absent ([PR #518](https://github.com/marmot-protocol/whitenoise-rs/pull/518)). A debug mode ([PR #528](https://github.com/marmot-protocol/whitenoise-rs/pull/528)) exposes database queries and MLS ratchet-tree inspection as JSON output. Other fixes addressed subscription recovery after signer re-registration, welcome message catch-up timing, relay filter validation, and user search radius limits.

Marmot saw significant expansion beyond the core Rust stack this week. [White Noise TUI](https://github.com/marmot-protocol/wn-tui), a terminal-based interface to the White Noise messaging stack, launched March 3. It wraps the `wn` CLI as a subprocess and renders its JSON output through an Elm-inspired unidirectional architecture, providing multi-conversation navigation with unread indicators, group creation and member search, real-time message streaming, and emoji reactions from the terminal.

[DavidGershony](https://github.com/DavidGershony) published a complete C# Marmot stack mirroring the Rust toolchain's layered architecture. [dotnet-mls](https://github.com/DavidGershony/dotnet-mls) implements MLS RFC 9420 cryptographic primitives in C#. [marmot-cs](https://github.com/DavidGershony/marmot-cs) builds on it to add Nostr relay transport, functioning as a C# equivalent of MDK. [OpenChat](https://github.com/DavidGershony/openChat), a cross-platform desktop app built with .NET 9 and Avalonia UI, ties both together into a working chat client with NIP-44 DMs, Marmot group encryption, [NIP-46](/en/topics/nip-46/) (Nostr Connect) remote signing, and multi-relay status indicators.

[MDK PWA Reference](https://github.com/zerosats/mdk-pwa-reference) provides a Progressive Web App template for building Marmot-encrypted applications, with experimental support for AI agent participation in group chats and Bitcoin payments via Arkade wallet infrastructure.

### Wisp Ships from Alpha to Beta

[Wisp](https://github.com/barrydeen/wisp) is a new Android Nostr client that went from [first alpha](https://github.com/barrydeen/wisp/releases/tag/v0.1.0-alpha) on February 24 to [v0.3.4-beta](https://github.com/barrydeen/wisp/releases/tag/v0.3.4-beta) on March 3, producing 19 releases, 115 merged PRs, and 276 commits in eight days.

The feature trajectory covers ground that most clients take months to reach. v0.1.0 shipped with outbox/inbox relay model support and onboarding flows. By v0.1.3, the client had [NIP-55](/en/topics/nip-55/) intent-based signing for Amber, an embedded Tor SOCKS5 proxy for `.onion` relay connectivity, and [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect). v0.2.0 graduated to beta with mute list filtering and custom emoji support, while v0.2.4 added content warning overlays. The v0.3.x series introduced [NIP-13](/en/topics/nip-13/) proof-of-work for notes, background PoW mining with persistent settings, `.onion` relay storage, and mute thread notifications.

On-device translation via Google ML Kit runs locally without network access after the initial model download. An interactive social graph visualization uses a velocity Verlet physics simulation at approximately 30fps with pinch-to-zoom navigation and profile inspection.

## Releases

### Vector v0.3.1

[Vector](https://github.com/VectorPrivacy/Vector), the Marmot-encrypted messaging app, shipped [v0.3.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.1) with group management improvements and performance work. Multi-admin groups, bulk invites, invite-by-npub, and group avatars expand the collaboration features. Android background notifications now support inline Reply and Mark Read actions.

[Negentropy](/en/topics/negentropy/)-based deterministic sync retrieves full conversation history including messages that were missed during offline periods. Voice-to-text rebuilt with GPU acceleration on Android. File attachment handling was overhauled with download progress, retry states, directory zip-and-send, and live progress indicators throughout. Performance improved over 15x across boot time, image processing, audio playback, and general UI responsiveness. App install size dropped by more than a third, with the frontend reduced by roughly half. 32-bit ARM Android support was added.

### Alby Hub v1.21.5

[Alby Hub](https://github.com/getAlby/hub), the self-custodial Lightning node with Nostr Wallet Connect ([NIP-47](/en/topics/nip-47/)) support, shipped [v1.21.5](https://github.com/getAlby/hub/releases/tag/v1.21.5). A second relay was added to the default NWC configuration, improving reliability during relay restarts. A fix for invalid zap data in the transaction list resolves a display issue with malformed [NIP-57](/en/topics/nip-57/) (Lightning Zaps) events. New app store entries include Alby CLI and LNVPS.

### nospeak v0.12.x

[nospeak](https://github.com/psic4t/nospeak), the text-based Nostr messaging client, shipped three releases across the period. [v0.12.0](https://github.com/psic4t/nospeak/releases/tag/v0.12.0) added a PIN app lock with 4-digit keypad and over 15 new language translations including Bengali, Thai, Vietnamese, Hindi, Arabic, Hebrew, Urdu, Turkish, Japanese, Chinese, Korean, Dutch, Polish, Russian, and Persian with RTL support. [v0.12.1](https://github.com/psic4t/nospeak/releases/tag/v0.12.1) introduced a Cypher theme with pure black backgrounds and cyan accents, plus Android video poster generation. [v0.12.2](https://github.com/psic4t/nospeak/releases/tag/v0.12.2) added chat export and View Profile in contact menus.

### Citrine v2.0.0-pre2

[Citrine](https://github.com/greenart7c3/Citrine), the Android personal relay by greenart7c3, shipped [v2.0.0-pre2](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre2) with relay performance improvements through new database indexes and restructured Kotlin coroutines. Each hosted web app now starts on its own port. Full-text search and a redesigned events screen with event expansion round out the changes.

### NoorNote v0.5.x

[NoorNote](https://github.com/77elements/noornote), a Nostr-based note-taking application, shipped 8 releases from [v0.5.0](https://github.com/77elements/noornote/releases/tag/v0.5.0) through [v0.5.7](https://github.com/77elements/noornote/releases/tag/v0.5.7). The v0.5.0 launch on Android added [NIP-55](/en/topics/nip-55/) Amber signer support and [NIP-71](/en/topics/nip-71/) (Video Events) note publishing. A redesigned welcome page in v0.5.1 included public timeline previews and reduced the APK to 15 MB. The Relay Browser in v0.5.2 lets users browse public relay timelines via shareable URLs, alongside media download and [NIP-30](/en/topics/nip-30/) custom emoji reactions. Subsequent releases through v0.5.7 addressed sync race conditions in the collaborative "tribes" note-sharing system.

### NosCall v0.5.1

[NosCall](https://github.com/sanah9/noscall), the Nostr voice and video calling app, shipped [v0.5.1](https://github.com/sanah9/noscall/releases/tag/v0.5.1-release) with voice message support, an optimized desktop experience with group entry, contact favorites on desktop, contact notes and filtering, data export and cleanup options, and system font size accessibility support.

### Shosho v0.13.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), the Nostr live streaming app, shipped [v0.13.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.13.0) with MP4 replay downloads from stream card menus and [NIP-05](/en/topics/nip-05/) (DNS-Based Verification) for profiles. The RTMP publisher migrated to Expo Modules API. Streaming performance on lower-bandwidth connections improved, and crashes on older devices and iOS streaming to [Zap.Stream](https://zap.stream) are fixed.

### nostr-java v2.0.0

[nostr-java](https://github.com/tcheeric/nostr-java) shipped [v2.0.0](https://github.com/tcheeric/nostr-java/releases/tag/v2.0.0) with configurable WebSocket buffer sizes, allowing applications to handle larger Nostr events without truncation. The major version bump reflects breaking changes to the connection API.

### Prism 1.1.0

[Prism](https://github.com/hardran3/Prism) shipped [1.1.0](https://github.com/hardran3/Prism/releases/tag/1.1.0) with long-form content support (kind 30023 articles) and a Markdown editor for composing directly in the app, followed by a [1.1.1](https://github.com/hardran3/Prism/releases/tag/1.1.1) bug fix release.

### Angor v0.2.6

[Angor](https://github.com/block-core/angor), the Bitcoin crowdfunding platform, shipped [v0.2.6](https://github.com/block-core/angor/releases/tag/v0.2.6) with Boltz integration and a 1-click invest flow. Both invest and fund project types work end-to-end on testnet. The team notes the UI is approximately 70% complete.

## NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-91: AND Operator for Filters](https://github.com/nostr-protocol/nips/pull/1365)**: Adds AND filter semantics for tag arrays in relay subscriptions. Currently, specifying multiple values in a tag filter (e.g., multiple `p` tags) matches events containing any of them. NIP-91 lets clients require events matching all specified tag values simultaneously, reducing bandwidth and enabling faster index operations. Multiple relay implementations already exist including nostr-rs-relay, satellite-node, worker-relay, and applesauce. Formerly numbered NIP-119.

- **[NIP-30: Emoji Set Address in Tags](https://github.com/nostr-protocol/nips/pull/2247)**: Custom emoji tags in [NIP-30](/en/topics/nip-30/) can now include an optional emoji set address. Clicking an emoji in a client can open the set it belongs to for bookmarking or browsing. Originated from the [Chachi](https://github.com/purrgrammer/chachi) client.

- **[NIP-29: Add unallowpubkey and unbanpubkey](https://github.com/nostr-protocol/nips/pull/2111)**: Two new admin commands for [NIP-29](/en/topics/nip-29/) group chat. `unallowpubkey` removes a pubkey from the allowed list without banning them. `unbanpubkey` lifts a ban without re-adding the pubkey to the member list. Previously, the only way to remove someone from the allowed list also banned them, and unbanning required re-adding the user as a member.

**Open PRs and Discussions:**

- **[NIP-A7: Spells](https://github.com/nostr-protocol/nips/pull/2244)** (opened Feb 27): Proposed by purrgrammer, spells are portable saved Nostr queries published as kind 777 events. A spell encodes a REQ or COUNT filter in structured tags (`k` for kinds, `authors` for pubkeys, `tag` for arbitrary tag filters) with runtime variables: `$me` resolves to the logged-in user's pubkey, `$contacts` expands to the user's kind 3 follow list. Relative timestamps (`7d`, `2w`, `1mo`) let spells define rolling time windows without hardcoded dates. Already implemented in [nak](https://github.com/fiatjaf/nak) and [Grimoire](https://github.com/purrgrammer/grimoire), spells let users create, share, and subscribe to curated feeds that travel across clients.

- **[NIP-59: Ephemeral Gift Wrap (kind 21059)](https://github.com/nostr-protocol/nips/pull/2245)** (opened Feb 27): Adds an ephemeral variant of [NIP-59](/en/topics/nip-59/) gift wraps. Kind 21059 follows NIP-01 ephemeral semantics, so relays discard events after delivery. Proposed by ContextVM for MCP transport where message persistence is unnecessary.

- **[ContextVM: MCP JSON-RPC over Nostr](https://github.com/nostr-protocol/nips/pull/2246)** (opened Feb 27): Specifies how to transport Model Context Protocol messages over Nostr using ephemeral kind 25910 events with `p` and `e` tags for addressing and correlation. Intentionally thin, deferring protocol detail to the [ContextVM spec](https://docs.contextvm.org).

- **[NIP-29: Audio/Video Live Spaces](https://github.com/nostr-protocol/nips/pull/2238)** (opened Feb 25, draft): fiatjaf's draft extending [NIP-29](/en/topics/nip-29/) groups with live audio and video. The proposal adds optional `livekit` and `no-text` tags to group metadata events. When a user wants to join a voice space, the client requests a JWT from the relay at `/.well-known/nip29/livekit/{groupId}`. The relay checks group membership and issues a token with the user's hex pubkey as the `sub` claim, which is passed to [LiveKit](https://livekit.io/) for media transport. Voice room access inherits the group's existing permission model, so relay-side membership rules govern who can speak. Being tested in Pyramid and Chachi.

- **[Collaborative Event Ownership](https://github.com/nostr-protocol/nips/pull/2235)** (opened Feb 24): pablof7z proposes a pointer event (kind 39382) that declares a collaborative space by listing co-owner pubkeys in `p` tags and a target event kind in a `k` tag. Any listed owner can publish events of that kind with the same `d` tag, and clients resolve the current state by querying all owners and taking the most recent event. Co-authorship attribution only displays when a verifiable `a` tag back-references the pointer and the author appears in its `p` tags, preventing spoofed claims. This enables shared wiki pages and co-authored resources without assigning control to a single keypair.

- **[NIP-09: Cascading Deletion of Reposts](https://github.com/nostr-protocol/nips/pull/2234)** (opened Feb 24): When an original author deletes a note, relays should also delete any kind 6 or kind 16 reposts referencing it. Motivated by privacy concerns: reposts can preserve accidentally leaked information after the author deletes the source. The change is relay-side only, requiring no client modifications.

- **[NIP-07: peekPublicKey](https://github.com/nostr-protocol/nips/pull/2233)** (opened Feb 23): Adds a `peekPublicKey()` method to [NIP-07](/en/topics/nip-07/) browser extensions. Unlike `getPublicKey()`, it returns the current pubkey without prompting for user confirmation, enabling silent auto-login when the user has auto-login enabled.

- **[NIP-BB: Book](https://github.com/nostr-protocol/nips/pull/2248)** (opened Feb 28, draft): Defines four addressable event kinds (30300-30303) for structured book publishing on Nostr. A Cover event holds root metadata including title, cover image, license via [NIP-32](/en/topics/nip-32/) (Labeling) labels, and language code. An Index event maps each chapter to its position using base62 fractional indexing, which lets authors insert new chapters between existing ones without renumbering. Chapter events act as structural headers with optional images, while Episode events carry the actual prose capped at 30,000 characters with positioned image tags. Reviews use Zaps on Cover events with the Zap description as review text.

- **[NIP-54: Switch from Asciidoc to Djot](https://github.com/nostr-protocol/nips/pull/2242)** (opened Feb 26): Following the [d-tag internationalization fix](/en/newsletters/2025-12-31-newsletter/) in December, this PR proposes replacing [NIP-54](/en/topics/nip-54/) wiki's Asciidoc markup format with [Djot](https://djot.net/), adding a rationale section and wikilink examples for non-Latin scripts.

- **[NIP-66: Defensive Measures](https://github.com/nostr-protocol/nips/pull/2240)** (opened Feb 26): Based on learnings from the [nostrability/outbox](#outbox-model-under-the-microscope) benchmarks, adds explicit callouts for [NIP-66](/en/topics/nip-66/) edge cases. A companion [PR #2241](https://github.com/nostr-protocol/nips/pull/2241) defines output tags for SSL, geolocation, network, and connectivity checks.

- **NIP-C1: Cryptographic Identity Proofs** (wiki entry, kind 30817): Proposes kind 30509 events that cryptographically link APK signing certificates to Nostr profiles. The proof works by signing a canonical message containing the Nostr pubkey with the certificate's private key (supporting ECDSA, RSA PKCS1v15, Ed25519, and other standard algorithms), then publishing the signature in a kind 30509 event signed with the Nostr key. Verifiers can confirm that the person who controls an app's Android signing certificate also controls the Nostr pubkey claiming to publish it. Proofs expire after one year by default and can be explicitly revoked. Implemented in the [Zapstore](https://github.com/zapstore/zapstore) toolchain.

- **NIP-31402: SARA Revenue Share Offering Registry** (wiki entry, kind 30817): Defines kind 31402 addressable events for publishing Simple Autonomous Revenue Agreement (SARA) offerings on Nostr relays. Issuers advertise Lightning-settled revenue share terms including pool share percentage, payout trigger, threshold in sats, term length, and tiered pricing. Agents and humans can discover offerings across relays and subscribe autonomously without a central platform. The kind number mirrors kind 30402 (L402 Service Registry, published by the same author as a companion wiki entry) since SARA represents the return leg of the L402 payment relationship.

## Open PRs and Project Updates

### Damus: [NIP-89](/en/topics/nip-89/) (Recommended Application Handlers)

[PR #3337](https://github.com/damus-io/damus/pull/3337) implements NIP-89 client tag support for [Damus](https://github.com/damus-io/damus). The app now emits a client tag on all posting paths (main app, share extension, highlighter, drafts) and displays "via ClientName" beside timestamps when other apps include their tags. A Privacy toggle in Appearance settings lets users disable tag emission. [PR #3652](https://github.com/damus-io/damus/pull/3652) adds a Storage section in Settings with an interactive pie chart breaking down NostrDB and Kingfisher cache disk usage with export support.

Open: [PR #3657](https://github.com/damus-io/damus/pull/3657) adds [NIP-65](/en/topics/nip-65/) relay fallback for quoted notes. When an inline `nevent` includes an author pubkey but no relay hints and the note is missing from the user's pool, Damus fetches the author's kind 10002 relay list and retries from their write relays.

### Amethyst: [NIP-39](/en/topics/nip-39/) (External Identities), NIP-C0, [NIP-66](/en/topics/nip-66/)

[Amethyst](https://github.com/vitorpamplona/amethyst) merged a wave of NIP implementations across 28 PRs. External identity claims now publish as dedicated kind 10011 events under [NIP-39](/en/topics/nip-39/) ([PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747)), separating social identity from kind 0 metadata with backward-compatible fallback. Code snippet support via NIP-C0 ([PR #1744](https://github.com/vitorpamplona/amethyst/pull/1744)) adds kind 1337 events with accessors for language, extension, runtime, license, and dependencies. The [NIP-66](/en/topics/nip-66/) relay monitoring implementation ([PR #1742](https://github.com/vitorpamplona/amethyst/pull/1742)) covers both event kinds with full tag parsing for RTT metrics, network type, supported NIPs, and geohash.

Encrypted DMs arrived on Amethyst Desktop ([PR #1710](https://github.com/vitorpamplona/amethyst/pull/1710)) with a split-pane chat layout supporting both [NIP-04](/en/topics/nip-04/) (Encrypted Direct Messages) and [NIP-17](/en/topics/nip-17/) (Private Direct Messages). A new relay feed screen ([PR #1733](https://github.com/vitorpamplona/amethyst/pull/1733)) lets users browse posts from a specific relay with follow/unfollow functionality. Open: censorship-resistant NIP-05 verification ([PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734)) adds a parallel verification path for `.bit` identifiers that resolves against the Namecoin blockchain instead of HTTP DNS. When Amethyst detects a `.bit` suffix in a NIP-05 field, it queries an ElectrumX-NMC server for the name's transaction history, parses the `NAME_UPDATE` script from the latest output to extract the Nostr pubkey, and rejects names older than 36,000 blocks (Namecoin's expiry window). ElectrumX connections route through SOCKS5 when Tor is enabled, with dynamic server selection between clearnet and `.onion` endpoints. An LRU cache with a one-hour TTL prevents repeated blockchain queries.

### Notedeck: Outbox Architecture

[PR #1303](https://github.com/damus-io/notedeck/pull/1303) migrates [Notedeck](https://github.com/damus-io/notedeck) from ad-hoc relay pool management to a centralized outbox model with account-scoped subscriptions. The Messages module now publishes a default DM relay list if none exists and routes DMs to recipients' preferred relays per kind 10050.

### Pika: Per-Group Profiles and Tutorial Feed

[Pika](https://github.com/sledtools/pika), the Marmot-encrypted messaging app available on iOS and Android with a desktop build, gained per-group profiles ([PR #368](https://github.com/sledtools/pika/pull/368)). Users can now set a separate display name and picture for each group chat, along with a custom bio. These profiles publish as encrypted kind 0 events inside the Marmot group, invisible to anyone outside it, with a fallback to the user's global Nostr profile when no group-specific profile is set. When new members join, the admin rebroadcasts all stored group profiles and each member republishes their own on commit. Profile pictures are Marmot-media-encrypted before Blossom upload. The PR includes 16 new unit tests and exposes the feature both through a CLI command (`update-group-profile`) and the UI.

A new `pika-news` web app ([PR #401](https://github.com/sledtools/pika/pull/401)) monitors Pika's own GitHub PRs and auto-generates step-by-step tutorial walkthroughs from PR diffs, publishing them as server-rendered pages with [NIP-07](/en/topics/nip-07/) authentication. Users can discuss specific tutorials in real time through Nostr-authenticated chat.

### diVine: Embeddable Widgets and Video Replies

[diVine](https://github.com/divinevideo/divine-mobile), the Nostr-native video sharing platform, merged 132 PRs in ten days. Embeddable iframe widgets ([PR #1843](https://github.com/divinevideo/divine-mobile/pull/1843)) provide a self-contained `/embed?npub=...` page that renders a user's profile and latest videos. Video reply functionality ([PR #1915](https://github.com/divinevideo/divine-mobile/pull/1915)), gated behind a feature flag, uses Kind 1111 comments ([NIP-22](/en/topics/nip-22/)) with [NIP-92](/en/topics/nip-92/) (Media Attachments) imeta metadata. Bluesky-inspired three-way content filters ([PR #1797](https://github.com/divinevideo/divine-mobile/pull/1797)) offer Show/Warn/Hide controls across 17 [NIP-32](/en/topics/nip-32/) content warning categories.

### strfry: REQ Filter Validation

[PR #163](https://github.com/hoytech/strfry/pull/163) adds configurable REQ filter validation to [strfry](https://github.com/hoytech/strfry), the C++ Nostr relay. Operators can set maximum filters per REQ, required author or tag presence, allowed kind whitelists, and per-filter kind limits. The feature targets NWC relay deployments that need strict filter enforcement. Open: [PR #173](https://github.com/hoytech/strfry/pull/173) adds optional zstd compression for event payloads at ingest time.

### rust-nostr: [NIP-62](/en/topics/nip-62/) Request to Vanish

[rust-nostr](https://github.com/rust-nostr/nostr), the Rust Nostr protocol library, added [NIP-62](/en/topics/nip-62/) (Request to Vanish) support across all three database backends: [LMDB](https://github.com/rust-nostr/nostr/pull/1268), [SQLite](https://github.com/rust-nostr/nostr/pull/1270), and [in-memory](https://github.com/rust-nostr/nostr/pull/1272). The LMDB implementation includes configurable options to enable or disable [NIP-09](/en/topics/nip-09/) and NIP-62 enforcement per deployment.

### NDK: Collaborative Events and NIP-46 Timeout

[NDK](https://github.com/nostr-dev-kit/ndk), the Nostr Development Kit for JavaScript/TypeScript, merged [PR #380](https://github.com/nostr-dev-kit/ndk/pull/380) introducing `NDKCollaborativeEvent` for multi-author collaborative documents using an addressable pointer event (kind 39382) that defines authorized authors. A configurable timeout for `NDKNip46Signer` ([PR #381](https://github.com/nostr-dev-kit/ndk/pull/381)) prevents [NIP-46](/en/topics/nip-46/) remote signing operations from hanging indefinitely when a bunker does not respond.

### TENEX: Agent Categorization and Pubkey Gating

[TENEX](https://github.com/tenex-chat/tenex), the Nostr-native AI agent orchestration platform, merged two security-related PRs. TIP-01 role-based agent categorization ([PR #91](https://github.com/tenex-chat/tenex/pull/91)) maps agent categories (principal, orchestrator, worker, advisor, auditor) to automated tool restrictions via a denied-tools map. Front-door pubkey gating ([PR #87](https://github.com/tenex-chat/tenex/pull/87)) ensures only events from whitelisted or backend-signed pubkeys are routed alongside known agents; unknown pubkeys are silently dropped with OpenTelemetry spans for audit.

### Zap Cooking: Membership Dashboard

[Zap Cooking](https://github.com/zapcooking/frontend), the Nostr-based recipe sharing platform, merged 25 PRs and 85 commits in ten days. A membership dashboard ([PR #228](https://github.com/zapcooking/frontend/pull/228)) shows subscription status with expiration dates and manage/upgrade options, re-enables feature gates for Sous Chef and Zappy tiers with both client-side and server-side checks, and standardizes tier naming across 26 files. Two-phase group message loading ([PR #227](https://github.com/zapcooking/frontend/pull/227)) provides a fast 3-day initial fetch for instant display followed by a background 40-day backfill.

Wallet mnemonic storage moved from pubkey-derived encryption to [NIP-44](/en/topics/nip-44/) encrypt-to-self ([PR #224](https://github.com/zapcooking/frontend/pull/224)), fixing a vulnerability where the old scheme derived its key from `SHA-256(pubkey)`, which is effectively unencrypted since pubkeys are public. Existing wallets are silently migrated on first load. [NIP-29](/en/topics/nip-29/) group chat gained unread indicators with red dot badges and invite-only access with kind 9009 invite codes ([PR #213](https://github.com/zapcooking/frontend/pull/213)). Link previews and Nostr event embeds now render in DMs and group messages ([PR #218](https://github.com/zapcooking/frontend/pull/218)). A Nostr backup section in Settings ([PR #210](https://github.com/zapcooking/frontend/pull/210)) stores follows and mute lists via [NIP-78](/en/topics/nip-78/) (Application-specific Data) encrypted storage with rotating 3-slot versioning. Startup performance improved through deferred notification services, lazy DOM rendering via IntersectionObserver (reducing DOM nodes from ~15,000 to ~3,000 on a 200-event feed), and extended outbox cache TTLs ([PR #208](https://github.com/zapcooking/frontend/pull/208)). A customizable print recipe modal ([PR #205](https://github.com/zapcooking/frontend/pull/205)) lets users toggle which sections to include with a live preview. [Branta SDK](https://github.com/BrantaOps/branta-core) integration ([PR #222](https://github.com/zapcooking/frontend/pull/222)) adds verification guardrails for POST and GET requests.

### Keep: Rust-Driven State Migration

[Keep](https://github.com/privkeyio/keep-android), the Nostr-based private key manager for Android, merged [PR #178](https://github.com/privkeyio/keep-android/pull/178), deleting four Kotlin configuration stores in favor of Rust-driven shared state from the keep-mobile layer. A 10-second polling loop was replaced with push-based `KeepStateCallback` from Rust. [PR #179](https://github.com/privkeyio/keep-android/pull/179) adds encrypted backup and restore with passphrase protection.

### Mostro Mobile: Dispute Chat Encryption

[Mostro Mobile](https://github.com/MostroP2P/mobile), the mobile client for the Mostro P2P Bitcoin trading platform, shipped a two-phase migration of dispute chat encryption. The first step ([PR #495](https://github.com/MostroP2P/mobile/pull/495)) switches from mostro-specific wrapping to shared key encryption derived from the admin's pubkey. Building on that, [PR #501](https://github.com/MostroP2P/mobile/pull/501) unifies the message model with `NostrEvent` and stores gift wrap events encrypted on disk, consistent with the peer-to-peer chat pattern. A BIP-340 signature fix ([PR #496](https://github.com/MostroP2P/mobile/pull/496)) overrides the bip340 dependency to 0.2.0, resolving a `bigToBytes()` padding bug that caused 1-2% of Schnorr signatures to be invalid and 100% failure for keys whose public key starts with `0x00`. Order Details now shows human-readable status labels instead of raw protocol values, localized across English, Spanish, Italian, and French ([PR #502](https://github.com/MostroP2P/mobile/pull/502)). HalCash was added and SEPA removed as a payment method ([PR #493](https://github.com/MostroP2P/mobile/pull/493)), since SEPA transfers can exceed 24 hours (SEPA Instant remains).

On the server side, [Mostro](https://github.com/MostroP2P/mostro) fixed dispute session restore to include the initiator field ([PR #599](https://github.com/MostroP2P/mostro/pull/599)) and now automatically closes active disputes when a seller releases funds, publishing a settled Nostr event so admin clients see the resolution ([PR #606](https://github.com/MostroP2P/mostro/pull/606)).

## Five Years of Nostr Februaries

[Last month's newsletter](/en/newsletters/2026-01-28-newsletter/#five-years-of-nostr-januaries) traced Nostr's January milestones from early development through the Damus breakout to security infrastructure in 2026. This retrospective covers what happened each February from 2021 through 2026.

### February 2021: The Rewrite

Three months into its existence, Nostr's February produced the protocol's most consequential early change. On February 14-15, fiatjaf [rewrote NIP-01](https://github.com/nostr-protocol/nostr/commit/33a1a70), replacing the original message format with the EVENT/REQ/CLOSE model that the protocol still uses. Before this rewrite, clients and relays communicated through a simpler structure. Separating event publishing (EVENT) from subscription management (REQ/CLOSE) enabled relay-side filtering that would prove essential for scaling.

[NIP-04](/en/topics/nip-04/) arrived the same month, adding encrypted direct messages using shared secrets derived from Diffie-Hellman key exchange over secp256k1. Its encryption was basic (AES-256-CBC) and would later be replaced by [NIP-44](/en/topics/nip-44/)'s audited cryptography, but it gave the handful of early users their first private communication channel on the protocol.

Tooling expanded with [noscl](https://github.com/fiatjaf/noscl), a Go command-line client for terminal-based relay interaction, and futurepaul started [nostr-rs](https://github.com/futurepaul/nostr-rs), an early Rust implementation. The entire network ran on two or three relays, coordinated through a [Telegram group](https://t.me/nostr_protocol), with roughly seven active contributors.

### February 2022: Building Momentum

The [Hacker News post](https://news.ycombinator.com/item?id=29749061) from December 31, 2021 continued to draw developers into February. The [nostr-protocol/nostr](https://github.com/nostr-protocol/nostr) repository (the formal [NIPs repository](https://github.com/nostr-protocol/nips) would not exist until May 2022) received six pull requests in February, including NIP-13 (Proof of Work) from vinliao, NIP-14 (Reputation) from fiatjaf, NIP-15 (Resource Relations) from Cameri, and [NIP-17](https://github.com/nostr-protocol/nostr/pull/75) (Git Updates Over Nostr) from melvincarvalho. The NIP number was later reassigned to Private Direct Messages; git collaboration on Nostr continued separately through what became [gitworkshop.dev](https://gitworkshop.dev).

Greg Heartsfield's [nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay) was the month's workhorse with 34 commits and three releases. Version 0.5.0 on February 12 added [NIP-05](/en/topics/nip-05/) verified user publishing limits. Versions 0.5.1 and 0.5.2 followed over the next two weeks, and the relay handled the bulk of the network's traffic alone.

Robert C. Martin (Uncle Bob) was building [more-speech](https://github.com/unclebob/more-speech), a Clojure desktop client, logging 69 commits between January 18 and the end of February. His involvement brought attention from the broader software engineering community. fiatjaf's [nos2x](https://github.com/fiatjaf/nos2x) browser extension shipped [NIP-04](/en/topics/nip-04/) decrypt support and relay preference policies in February, implementing the `window.nostr` interface ([NIP-07](/en/topics/nip-07/)) that web clients still use for key delegation.

[Branle](https://github.com/fiatjaf/branle), still the primary web client, gained `web+nostr` protocol handler registration on February 13, an early attempt at deep linking between Nostr applications. [nostr-tools](https://github.com/nbd-wtf/nostr-tools) tightened NIP-05 validation. [go-nostr](https://github.com/nbd-wtf/go-nostr) added NIP-04 encrypted DM support and NIP-12 (Generic Tag Queries) parsing across 11 commits. The network operated on roughly 7-15 relays with an active user base likely in the low hundreds. Damus and Nostream did not yet exist and would not appear until April 2022.

### February 2023: International Attention

February 2023 brought Nostr its largest wave of public attention. [Damus](https://github.com/damus-io/damus), the iOS client by William Casarin, had been [approved on Apple's App Store on January 31](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store) after repeated rejections. By February 1 it reached the top 10 in U.S. Social Networking. Two days later, on February 2, [Apple pulled Damus from China's App Store](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/) reportedly at the request of the Cyberspace Administration of China.

Major outlets including TechCrunch and CoinDesk covered the removal, amplifying awareness of both the app and the protocol. Unique public keys with metadata on nostr.directory crossed 300,000 by February 3. All relays were operated by enthusiasts paying out-of-pocket, and infrastructure scrambled to handle the load. Approximately 289 relays were tracked by early February, a number that continued to climb.

The [NIPs repository](https://github.com/nostr-protocol/nips) logged 29 merged pull requests that month, the highest single-month count in the protocol's history to that point. [NIP-57](https://github.com/nostr-protocol/nips/pull/224) (Lightning Zaps) and [NIP-23](https://github.com/nostr-protocol/nips/pull/220) (Long-form Content) both merged on February 13, adding Bitcoin micropayments and expanding Nostr beyond short posts in a single day. [NIP-65](/en/topics/nip-65/) (Relay List Metadata) had merged a week earlier on February 7, enabling the outbox model that followed. [NIP-46](/en/topics/nip-46/) (Nostr Connect) and [NIP-58](/en/topics/nip-58/) (Badges) also landed before month's end.

The Human Rights Foundation [granted $50,000 to William Casarin for Nostr and Damus development](https://hrf.org/devfund2023q1) on February 21, one of the first institutional grants to a Nostr project. OpenSats had not yet launched its Nostr fund (that would come in [July 2023](https://opensats.org/blog/nostr-grants-july-2023)).

### February 2024: Protocol Durability

February 2024 shifted focus from growth to protocol durability. [NIP-17](/en/topics/nip-17/) (Private Direct Messages), open since the previous July, was working toward a replacement for the aging [NIP-04](/en/topics/nip-04/) encryption using [NIP-44](/en/topics/nip-44/)'s audited cryptography and [NIP-59](/en/topics/nip-59/) gift wrapping. NIP-04 leaked metadata to relay operators, who could see sender-recipient pairs. NIP-17 hides sender identity behind disposable keypairs and merged that spring after a final round of review in March.

[NIP-29](/en/topics/nip-29/) (Simple Groups) [merged February 28](https://github.com/nostr-protocol/nips/pull/566) after months of discussion, defining how relays can host moderated group chats with admin roles and access control. [NIP-92](/en/topics/nip-92/) (imeta tags) merged February 1, standardizing how clients attach image dimensions and blurhash previews to media events.

On February 16, the NIPs repository added [BREAKING.md](https://github.com/nostr-protocol/nips/commit/62c48eff), a file tracking backward-incompatible changes to the protocol specification. Its creation acknowledged that Nostr had reached a maturity level where breaking changes needed formal documentation.

Twenty-two pull requests merged that month. [npub.cash](https://github.com/cashubtc/npubcash-server) launched as a Lightning address service letting any npub receive payments without running a server. An [academic paper](https://arxiv.org/abs/2402.05709) published February 8 found that 95% of free-to-use relays could not cover operational costs through donations, with 35% of paid relays charging admission fees below 1,000 sats (roughly $0.45 at the time).

### February 2025: Infrastructure Growth

February 2025 produced 28 merged pull requests to the NIPs repository. A [Right to Vanish](/en/topics/nip-62/) NIP merged February 19, defining how users can request deletion of their data from relays in response to regulatory questions around data portability and user control.

[NIP-60](/en/topics/nip-60/) (Cashu Wallet) and NIP-61 (Nutzaps) received simplification updates, streamlining the ecash token storage format. A q-tag (quote tag) rollout continued across multiple NIPs, standardizing how events reference other events for quoting and threading.

Client releases marked steady progress. [Notedeck](https://github.com/damus-io/notedeck) v0.3.0 alpha shipped on the last day of January, with adoption continuing into February. Primal v2.1 followed on February 7, and [GRAIN](https://github.com/0ceanSlim/grain) v0.3.0, a Go relay implementation, released on February 21.

NOSTRLDN v5 brought the London Nostr community together for its fifth meetup. A DVMCP bridge connected Nostr's Data Vending Machines ([NIP-90](/en/topics/nip-90/)) with the Model Context Protocol, prefiguring the AI agent integration work that arrived the following month.

### February 2026: Beyond Social Media

*February 2026 activity is drawn from Nostr Compass issues [#8](/en/newsletters/2026-02-04-newsletter/) through [#11](/en/newsletters/2026-02-25-newsletter/).*

February 2026 produced the broadest range of application-layer development in any single Nostr month. [Mostro](https://github.com/MostroP2P/mostro) shipped its [first public beta](/en/newsletters/2026-02-11-newsletter/#mostro-ships-first-public-beta) for decentralized peer-to-peer Bitcoin trading, and [Zapstore](https://github.com/zapstore/zapstore) reached [1.0 stable](/en/newsletters/2026-02-11-newsletter/#zapstore-v100) after months in release candidate testing. [White Noise v0.3.0](/en/newsletters/2026-02-25-newsletter/#white-noise-v030) delivered real-time [Marmot](/en/topics/mls/)-encrypted messaging with Amber signer support and over 160 merged improvements.

Competing AI agent proposals from pablof7z (NIP-AE for agent workflows, NIP-AD for MCP server announcements) and joelklabo (AI Agent Messages) arrived alongside a [DVM Agent Coordination proposal](/en/newsletters/2026-02-25-newsletter/#nip-updates) extending [NIP-90](/en/topics/nip-90/). [ContextVM](/en/newsletters/2026-02-25-newsletter/#contextvm-mcp-over-nostr) shipped SDK improvements connecting the Model Context Protocol to Nostr transport. [Burrow](/en/newsletters/2026-02-25-newsletter/#burrow-mls-messaging-for-ai-agents) added [Marmot](/en/topics/mls/)-encrypted messaging for both AI agents and humans, extending Nostr's identity and relay infrastructure into machine-to-machine communication.

[FIPS](/en/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking) shipped a working Rust implementation of Nostr-native mesh networking, using secp256k1 keypairs as node identities with transport-agnostic routing over UDP, Ethernet, Bluetooth, or LoRa radio. Its design showed that Nostr's key model extends beyond social media into physical network infrastructure.

[OpenSats announced its fifteenth wave of Nostr grants](https://opensats.org/blog/fifteenth-wave-of-nostr-grants), funding projects including ContextVM and Nostube. Protocol changes included [NIP-47](/en/topics/nip-47/) hold invoice support for Nostr Wallet Connect and [NIP-45](/en/topics/nip-45/) (Counting Results) HyperLogLog for relay-side count estimation. [NIP-85](/en/topics/nip-85/) (Trusted Assertions) service provider discoverability for [Web of Trust](/en/topics/web-of-trust/) scoring also merged. [rust-nostr](https://github.com/rust-nostr/nostr) began a full API redesign while Nostria 3.0 and [Frostr](https://github.com/FROSTR-ORG) (iOS TestFlight) both shipped. [Blossom](/en/topics/blossom/)'s local cache layer addressed media availability across relays.

### Looking Ahead

Five Februaries of protocol history show a consistent progression from foundational work to application-layer diversification, with the 2023 user influx as the turning point. In 2021, seven contributors worked across three relays. By 2026, the same protocol supported mesh networking and autonomous agent proposals running on production infrastructure.

---

That's it for this week. Building something or have news to share? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Reach out via [NIP-17](/en/topics/nip-17/) DM</a> or find us on Nostr.
