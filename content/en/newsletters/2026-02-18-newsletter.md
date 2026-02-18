---
title: 'Nostr Compass #10'
date: 2026-02-18
publishDate: 2026-02-18
draft: false
type: newsletters
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** A Blossom local cache layer takes shape as independent projects converge on offline media access for Android. Alby launches an [NWC developer sandbox](https://sandbox.albylabs.com) for building and testing Nostr Wallet Connect integrations without risking real funds. Competing proposals for AI agent communication on Nostr arrive in the same week from two authors. fiatjaf strips unused fields from [NIP-11](https://github.com/nostr-protocol/nips/pull/1946), removing retention policies, country codes, privacy policy, and community preference tags that relay operators never adopted. [NIP-85](https://github.com/nostr-protocol/nips/pull/2223) merges service provider discoverability guidance for Trusted Assertions. A new `D` tag in [NIP-52](https://github.com/nostr-protocol/nips/pull/1752) enables day-granularity timestamp indexing of calendar events. New projects include [Mapnolia](https://github.com/zeSchlausKwab/mapnolia) for decentralized map tile distribution, [Pika](https://github.com/sledtools/pika) for MLS-encrypted messaging, [Keep](https://github.com/privkeyio/keep-android) for FROST threshold signing on Android, [Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree) for content-addressed storage with Nostr integration, and [Prism](https://github.com/hardran3/Prism) for sharing content to Nostr from any Android app. [Primal Android](https://github.com/PrimalHQ/primal-android-app) merges 11 NWC PRs adding dual wallet support and automatic service lifecycle. [Mostro Mobile](https://github.com/MostroP2P/mobile) ships a [built-in Lightning wallet](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2) through NWC integration. [Notedeck](https://github.com/damus-io/notedeck) prepares for Android App Store release while HAVEN reaches [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3) with multi-npub support and cloud backup. Deep dives this week cover NIP-85's Trusted Assertions system for delegating Web of Trust calculations to service providers, and NIP-52's Calendar Events protocol following its day-granularity indexing update.

## News

### Blossom Local Cache Layer Emerges

Multiple independent projects are converging on the same problem: offline access to [Blossom](/en/topics/blossom/) media on mobile devices.

[Morganite](https://github.com/greenart7c3/Morganite), a new Android app from greenart7c3 (the developer behind [Amber](https://github.com/greenart7c3/amber) and [Citrine](https://github.com/greenart7c3/Citrine)), implements client-side caching for Blossom media. Users can access previously viewed images and files without a network connection.

[Aerith](https://github.com/hardran3/Aerith) shipped [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2) with image labeling, bulk mirror/tag/delete operations, filtering by label and file type, plus initial local Blossom cache support. Aerith is a management interface for users who store media across multiple Blossom servers and need to organize and mirror their blobs.

A new [local cache implementation guide](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md) in the Blossom specification documents client-side blob storage, while [Prism](https://github.com/hardran3/Prism) (from the same developer as Aerith) adds Blossom upload integration to its Android share-to-Nostr flow. Four independent projects converged on the same problem this week: a dedicated caching app, a media manager, a reference specification, and a share tool with Blossom integration, all implementing persistent local storage beyond simple upload-and-retrieve.

### Alby NWC Developer Sandbox

[Alby](https://sandbox.albylabs.com) launched a sandbox environment for developers building with [Nostr Wallet Connect (NIP-47)](/en/topics/nip-47/). The sandbox provides a hosted NWC wallet service where developers can create test connections and send simulated payments without connecting to a real Lightning wallet, while observing the full request/response cycle of NWC events in real time. Developers generate a `nostr+walletconnect://` connection string from the sandbox and pass it to their client. The sandbox then shows the resulting kind 23194 request and kind 23195 response events as they flow between client and wallet service.

This lowers the barrier for new NWC integrations. Previously, testing required either a personal Lightning wallet or a self-hosted NWC service. The sandbox abstracts that away, giving developers an immediate feedback loop for implementing `pay_invoice`, `get_balance`, `make_invoice`, `lookup_invoice`, and `list_transactions` methods against a live NWC endpoint.

### AI Agent NIPs Arrive

Proposals for AI agent communication on Nostr appeared within days of each other, approaching the problem from different angles.

[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226) from joelklabo defines a complete protocol for AI agent interaction: event kinds for prompts, responses, streaming deltas, status updates, tool telemetry, errors, cancellations, and capability discovery. An `ai.info` discovery event (kind 31340, replaceable) lets agents announce their supported models, tools with schemas, streaming support, and rate limits. joelklabo's proposal includes run correlation via prompt ID, session management, stream reconciliation with sequence ordering, and [NIP-59](/en/topics/nip-59/) guidance for metadata privacy.

[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220) from pablof7z takes a different approach, defining kinds for agent instantiation: definitions and lessons. These are the event types pablof7z uses in [TENEX](https://github.com/tenex-chat/tenex), the autonomous learning system built on Nostr. A companion proposal, [NIP-AD: MCP Server and Skill Announcements](https://github.com/nostr-protocol/nips/pull/2221), also from pablof7z, defines events for announcing [Model Context Protocol](https://modelcontextprotocol.io/) servers and skills on Nostr. [NIP-22](/en/topics/nip-22/) comments are supported, so the community can discuss and rate MCP servers directly on Nostr.

NIP-XX covers full agent communication while NIP-AE and NIP-AD address identity and tool discovery. These proposals may converge into a unified standard or coexist as complementary layers.

## Releases

### HAVEN v1.2.0-rc3

[HAVEN](https://github.com/bitvora/haven), the all-in-one personal relay that bundles four relay functions with a [Blossom](/en/topics/blossom/) media server, reached [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3). This release candidate adds support for multiple npubs, letting a single HAVEN instance serve several Nostr identities. Earlier RCs added `--from-cloud` and `--to-cloud` flags for cloud backup (RC2) and fixed a Web of Trust double-counting bug (RC1).

### Mostro Mobile v1.2.0: Built-In Lightning Wallet

[Mostro Mobile](https://github.com/MostroP2P/mobile), the mobile client for the [Mostro](https://github.com/MostroP2P/mostro) P2P Bitcoin exchange ([v1.1.0 covered last week](/en/newsletters/2026-02-11-newsletter/#mostro-ships-first-public-beta)), shipped [v1.2.0](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2) with a built-in Lightning wallet through full [NWC (NIP-47)](/en/topics/nip-47/) integration. Buyers and sellers no longer need to switch apps to handle invoices. The app detects hold invoices for sellers and pays them automatically through the connected wallet, while buyers get automatic invoice generation. The release follows [v1.1.1](https://github.com/MostroP2P/mobile/releases/tag/v1.1.1%2B1) from earlier in the week, which added multi-Mostro node support with a curated registry of trusted instances, kind 0 metadata fetching for node display, custom node management by pubkey, and automatic fallback when a selected node goes offline.

On the server side, [Mostro v0.16.2](https://github.com/MostroP2P/mostro/releases/tag/v0.16.2) landed with fixes for duplicate dev fee payments, rate limiting on the password validation RPC endpoint, and proper dispute cleanup on cooperative cancellation.

A new companion project, [mostro-skill](https://github.com/MostroP2P/mostro-skill), enables agents to trade on Mostro through Nostr.

### Aerith v0.2

[Aerith](https://github.com/hardran3/Aerith), the [Blossom](/en/topics/blossom/) image manager, shipped [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2) with image labels for organizing media, bulk mirror/tag/delete operations across servers, filtering by label and file type, plus initial local cache support. See [News section](#blossom-local-cache-layer-emerges) for context on the broader local cache trend.

### Mapnolia: Decentralized Map Tiles Over Nostr

[Mapnolia](https://github.com/zeSchlausKwab/mapnolia) is a new geospatial data server that chunks [PMTiles](https://github.com/protomaps/PMTiles) map archives into geographic regions and announces them over Nostr for decentralized discovery. It publishes kind 34444 parametrized replaceable events to Nostr relays containing a complete index of map tile chunks with layer metadata, geohash regions, file references, and [Blossom](/en/topics/blossom/) server details.

Clients discover and retrieve map data through the Nostr network instead of centralized tile servers, with announcement events carrying enough metadata to request only needed geographic regions from listed Blossom servers. Mapnolia is the first project to bring geospatial data distribution to Nostr, opening possibilities for offline-capable mapping applications.

### Pika: Marmot-Based Encrypted Messaging

[Pika](https://github.com/sledtools/pika) is a new end-to-end encrypted messaging app for iOS and Android using the [Marmot](/en/topics/marmot/) protocol, which layers [Messaging Layer Security (MLS)](/en/topics/mls/) over Nostr relays. The architecture separates concerns into a Rust core (`pika_core`) handling MLS state management and message encryption/decryption over Nostr relays, with thin native UI shells in SwiftUI (iOS) and Kotlin (Android). State flows unidirectionally: the UI dispatches actions to the Rust actor, which mutates state and emits snapshots with revision numbers back to the UI via UniFFI and JNI bindings.

Pika joins a growing field of MLS-on-Nostr messengers alongside [White Noise](https://github.com/marmot-protocol/whitenoise), [Vector](https://github.com/VectorPrivacy), and [0xchat](https://0xchat.com). All use Nostr relays as the transport layer for MLS-encrypted ciphertext, keeping relay operators unable to read message content. Pika uses the Marmot Development Kit (MDK) for its MLS implementation and nostr-sdk for relay connectivity.

### Keep: [FROST](/en/topics/frost/) Threshold Signing for Android

[Keep](https://github.com/privkeyio/keep-android) is a new Android application for [FROST](/en/topics/frost/) threshold signing where no single device holds the complete private key. It implements [NIP-55](/en/topics/nip-55/) (Android Signer) and [NIP-46](/en/topics/nip-46/) (remote signing), so compatible Nostr clients can request signatures while key material stays distributed across devices. The default configurations are 2-of-3 and 3-of-5, though any t-of-n threshold is supported.

Keep's distributed key generation (DKG) ceremony runs over Nostr relays using custom event kinds: kind 21101 for group announcements, kind 21102 for round 1 commitment polynomials (broadcast publicly), and kind 21103 for round 2 secret shares ([NIP-44](/en/topics/nip-44/) encrypted point-to-point between participants). The group private key scalar is never computed or assembled anywhere during DKG. Each device holds only its polynomial evaluation share, and any t shares can produce a valid Schnorr signature through a two-round commit-then-sign protocol. The resulting 64-byte signature is indistinguishable from a single-signer Schnorr signature. Under the hood, Keep uses the Zcash Foundation's `frost-secp256k1-tr` crate with Taproot tweaking, so the group public key works directly as a Nostr npub.

Keep joins the [Frostr](https://frostr.org) family of projects alongside [Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop), [Igloo for Android](https://github.com/FROSTR-ORG/igloo-android), [Frost2x](https://github.com/FROSTR-ORG/frost2x), and [Igloo for iOS](https://github.com/FROSTR-ORG/igloo-ios), expanding options for threshold key management on Nostr.

### Prism: Share Anything to Nostr from Android

[Prism](https://github.com/hardran3/Prism) is a new Android app (Kotlin/Jetpack Compose, API 26+) that registers as a system share target, letting users publish text, URLs, images, and video to Nostr from any app on their phone. Shared URLs pass through a tracking parameter stripper before being composed into notes. Prism fetches OpenGraph metadata to generate rich link previews and renders native Nostr references (`note1`, `nevent1`) inline.

The scheduling engine uses a hybrid `AlarmManager`/`WorkManager` approach to bypass Android battery optimizations: AlarmManager handles precise wake-up timing while expedited WorkManager tasks ensure delivery, with exponential backoff retry for offline scenarios. Media uploads go through configurable [Blossom](/en/topics/blossom/) servers with thumbnail generation for images and video frames. All event signing is delegated to [NIP-55](/en/topics/nip-55/) external signers like [Amber](https://github.com/greenart7c3/amber), with multi-account support for switching between identities. Prism also supports [NIP-84 (Highlights)](/en/topics/nip-84/) posts. From the same developer as [Aerith](#aerith-v02).

### Hashtree: Content-Addressed Storage with Nostr Integration

[Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree) is a filesystem-based content-addressed blob storage system that publishes Merkle roots on Nostr to create mutable npub/path addresses. The system uses "dumb storage" that works with any key-value store, chunking content into 2MB blocks optimized for [Blossom](/en/topics/blossom/) uploads. Unlike BitTorrent, no active Merkle proof computation is needed, just store and retrieve blobs by hash.

The Nostr integration enables git remote URLs like `htree://npub.../repo-name` for cloning repositories, with commands like `htree publish mydata <hash>` to publish content hashes to `npub.../mydata` addresses. The comprehensive CLI supports both encrypted (default) and public storage modes, content pinning, pushing to Blossom servers, and managing Nostr identities. Each stored item is either raw bytes or a tree node, providing a foundation for decentralized content distribution through Nostr's relay network.

### Espy: Color Palette Capture on Shakespeare

[Espy](https://espy.you), built on the [Shakespeare](https://soapbox.pub/tools/shakespeare/) platform, lets users capture color palettes from photos and share them as Nostr events. Shakespeare is an AI-powered app builder that authenticates users via NIP-07 browser extensions and provides built-in Nostr relay connectivity, so developers ship apps without implementing their own key management or relay pool. Espy extracts dominant colors from camera input into shareable palette cards discoverable through standard Nostr feeds.

### Flotilla 1.6.4

[Flotilla](https://gitea.coracle.social/coracle/flotilla), hodlbod's Discord-like Nostr client that organizes relays as groups, shipped [1.6.4](https://gitea.coracle.social/coracle/flotilla/releases/tag/1.6.4). The Coracle family of projects has migrated from GitHub to a self-hosted [Gitea instance](https://gitea.coracle.social/coracle). This release adds push notifications via NIP-9a and a wallet receive flow, plus classified listings and space URL support. Interface improvements include cleaned-up modals and notification handling. Room muting and safe area insets on mobile round out the changes, alongside fixes for Safari image uploads and calendar event details.

### Shosho v0.12.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), the mobile live-streaming app with Nostr integration, shipped [v0.12.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.12.0). This release adds video Clips with in-player replies and custom emoji integration. Thread protection blocks indirect mention spam, and a new QR sharing feature lets users exchange profiles offline. A new horizontal playback mode gives streams a Twitch-style viewing experience, and the browse screen now features creator clips alongside live streams.

### Granary v10.0

[Granary](https://github.com/snarfed/granary), a social web translation library that converts data between Nostr, Bluesky, ActivityPub, and other platforms into a common format, shipped [v10.0](https://github.com/snarfed/granary/releases/tag/v10.0) with breaking changes. The release switches Nostr's default ActivityStreams 1 IDs from bech32 to hex and adds expanded Nostr support including [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) mention parsing and article tags. A new multiple-output option across converters lets developers translate between protocols in batch.

### Nostr MCP Server v3.0.0

[Nostr MCP Server](https://github.com/AustinKelsay/nostr-mcp-server), a [Model Context Protocol](https://modelcontextprotocol.io/) server that enables AI agents to interact with the Nostr network, shipped [v3.0.0](https://github.com/AustinKelsay/nostr-mcp-server/releases/tag/v3.0.0). This major release adds social actions (follows, reactions, reposts, replies) and relay list management with [NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md) support plus optional [NIP-42](/en/topics/nip-42/) authentication. Direct messaging via [NIP-17](/en/topics/nip-17/) and [NIP-44](/en/topics/nip-44/) is also new. The release pairs with this week's [AI agent NIP proposals](#ai-agent-nips-arrive) as practical tooling for agents operating on Nostr.

### Aegis v0.3.8

[Aegis](https://github.com/ZharlieW/Aegis), the cross-platform Nostr signer, shipped [v0.3.8](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.8) with multilingual UI support and an incremental update manager for its built-in Nostr app browser. The new update mechanism diffs incrementally against local state, keeping the in-app directory of Nostr web apps current with lower bandwidth usage. The release also introduces 5-minute key material caching to reduce database round-trips when signing multiple events in succession.

### SNSTR v0.3.1

[SNSTR](https://github.com/AustinKelsay/snstr) (Secure Nostr Software Toolkit for Renegades), a TypeScript library for the Nostr protocol, shipped [v0.3.1](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.1). The release adds package verification guards ensuring all entry points are included in npm tarballs, with CI enforcement on Node and Bun. [v0.3.0](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.0) shipped the same week.

### Citrine v2.0.0-pre1

[Citrine](https://github.com/greenart7c3/Citrine), the Android Nostr relay from greenart7c3, released [v2.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre1) with performance improvements through optimized database indexes and better Kotlin coroutine handling. The release also enhances support for hosting web apps, with each app now running on its own port.

## Project Updates

### Primal Android: NWC Infrastructure Expansion

[Primal Android](https://github.com/PrimalHQ/primal-android-app) merged 11 NWC-related PRs this week, continuing the buildout [started two weeks ago](/en/newsletters/2026-02-04-newsletter/#primal-android-ships-nwc-encryption). This batch adds dual wallet NWC support, automatic service start/stop tied to backend notifications, connection routing by wallet type, and proper data cleanup on wallet deletion. The NWC service now manages its own lifecycle based on wallet connection state, reducing manual user intervention.

### Notedeck: Android App Store Prep

[Notedeck](https://github.com/damus-io/notedeck), the multi-platform Nostr client from the [Damus](https://github.com/damus-io/damus) team, merged [Android App Store release preparation](https://github.com/damus-io/notedeck/pull/1287) this week. The PR adds a UGC (User Generated Content) compliance plan required by Google Play, including a Terms of Service acceptance screen, user blocking via context menus and settings, [NIP-56 (Reporting)](/en/topics/nip-56/) functionality that publishes report events to relays, and a Content & Safety settings section. Build infrastructure was added for generating signed release APKs and AABs (Android App Bundles) via new Makefile targets. An EULA document establishes a 17+ age requirement and Nostr-specific disclaimers about decentralized content. The compliance features themselves ship in follow-up PRs; this merge lays the documentation and signing groundwork.

On the Damus iOS side, a fix landed for an [infinite loading spinner regression](https://github.com/damus-io/damus/pull/3593) where the spinner would persist indefinitely after content had loaded.

### Nostria: Discovery Relays and DM Fixes

[Nostria](https://github.com/nostria-app/nostria), the cross-platform Nostr client focused on global scale, merged 9 PRs this week. The most notable adds [auto-initialization of Discovery Relays](https://github.com/nostria-app/nostria/pull/460) for profile lookup, giving new users working relay connectivity without manual configuration. Other fixes address [DM textarea wrapping](https://github.com/nostria-app/nostria/pull/466), [fullscreen video viewport fill](https://github.com/nostria-app/nostria/pull/479), [article metadata extraction in repost previews](https://github.com/nostria-app/nostria/pull/481), and [nostr: URI resolution in notifications](https://github.com/nostria-app/nostria/pull/458).

### Camelus: Riverpod v3 Migration

[Camelus](https://github.com/camelus-hq/camelus), the Flutter-based Nostr client, merged 5 PRs this week centered on a [Riverpod v3 API migration](https://github.com/camelus-hq/camelus/pull/158) and [generic feed refactor](https://github.com/camelus-hq/camelus/pull/159). An [embedded note cache](https://github.com/camelus-hq/camelus/pull/161) avoids redundant relay fetches for quoted notes.

## NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-85: Service Provider Discoverability](https://github.com/nostr-protocol/nips/pull/2223)**: vitorpamplona added guidance on client discovery of [NIP-85 Trusted Assertions](/en/topics/trusted-relay-assertions/) service providers, including relay hints and algorithm-specific service keys. See the [deep dive below](#nip-deep-dive-nip-85-trusted-assertions) for full coverage.

- **[NIP-11: Relay Information Cleanup](https://github.com/nostr-protocol/nips/pull/1946)**: fiatjaf removed `privacy_policy`, the `retention` array, `relay_countries`, and the community preferences block from [NIP-11](/en/topics/nip-11/). Relay operators rarely populated these fields and clients did not act on them.

- **[NIP-52: Day-Granularity Timestamp Tag](https://github.com/nostr-protocol/nips/pull/1752)**: staab added a required `D` tag to [NIP-52](/en/topics/nip-52/) time-based calendar events (kind 31923) representing the day-granularity Unix timestamp, calculated as `floor(unix_seconds / 86400)`. Multiple `D` tags cover multi-day events, enabling efficient temporal indexing without parsing full timestamps.

- **[NIP-47: Simplification](https://github.com/nostr-protocol/nips/pull/2210)**: The simplification PR [discussed in Newsletter #9](/en/newsletters/2026-02-11-newsletter/) merged this week, removing `multi_pay_invoice` and `multi_pay_keysend` from [NIP-47 (Nostr Wallet Connect)](/en/topics/nip-47/). See [Newsletter #8](/en/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-47-nostr-wallet-connect) for the full NWC protocol deep dive.

**Open PRs and Discussions:**

- **[NIP-74: Podcasts](https://github.com/nostr-protocol/nips/pull/2211)**: Covered in [Newsletter #8](/en/newsletters/2026-02-04-newsletter/), this podcast specification proposal saw heated discussion this week. staab noted at least three competing podcast standards already exist in the wild, and derekross pointed to an existing six-month-old implementation with active apps and podcasts. The path forward requires convergence between implementations before a NIP number can be assigned.

- **[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226)**: joelklabo proposes a complete AI agent communication protocol with event kinds for prompts, responses, streaming, tool telemetry, errors, and capability discovery. See [News section](#ai-agent-nips-arrive) for coverage of all AI proposals this week.

- **[NIP-PNS: Private Note Storage](https://github.com/nostr-protocol/nips/pull/1893)**: jb55's private note system defines kind 1080 events for storing encrypted personal notes on relays without revealing who wrote them. The scheme derives a deterministic pseudonymous keypair from the user's nsec via HKDF: `pns_key = hkdf_extract(ikm=device_key, salt="nip-pns")`, then generates a secp256k1 keypair from that derived key. A second derivation produces a symmetric encryption key: `pns_nip44_key = hkdf_extract(ikm=pns_key, salt="nip44-v2")`. Inner notes are encrypted with [NIP-44](/en/topics/nip-44/) v2 using this key and published under the pseudonymous pubkey, so relays see kind 1080 events from an identity unlinked to the user's main key. Unlike [NIP-59](/en/topics/nip-59/) gift wraps, PNS is not spammable (the pseudonymous key is deterministic, not random) and carries zero public metadata (no `p` tags needed since there is no recipient). This week, jb55 posted findings from implementing PNS in Notedeck's Rust backend (`enostr::pns` module). He identified that the spec's `hkdf_extract` call is ambiguous because RFC 5869 HKDF has two phases (Extract and Expand) that produce different output, and most libraries expect both. He clarified that `pns_nip44_key` bypasses NIP-44's normal ECDH key agreement and is used directly as the conversation key, a detail implementers need to know since most NIP-44 libraries default to ECDH. He also flagged an undefined variable in the reference implementation's TypeScript. The PR, originally from April 2025, is now being actively implemented.

- **[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220)**: pablof7z defines four event kinds for agent identity on Nostr, drawn from his work on [TENEX](https://github.com/tenex-chat/tenex). The base template is kind 4199 (Agent Definition), carrying title, role description, system instructions, tool declarations, and version. Behavioral modifiers live in kind 4201 (Agent Nudge), which uses `only-tool`, `allow-tool`, and `deny-tool` tags for runtime capability control. Agents publish what they learn as kind 4129 (Agent Lesson) events, categorized and linked back to the parent definition via `e` tags, refinable through [NIP-22](/en/topics/nip-22/) comment threads. Ownership verification uses kind 14199, a replaceable event where human operators list their agent pubkeys, establishing a bidirectional chain when matched against the agent's kind 0 profile `p` tag.

- **[NIP-AD: MCP Server and Skill Announcements](https://github.com/nostr-protocol/nips/pull/2221)**: pablof7z defines events for announcing [Model Context Protocol](https://modelcontextprotocol.io/) servers and individual skills on Nostr. MCP server announcements carry the server's endpoint URL and supported protocol version alongside a list of available tools with their input schemas. [NIP-22](/en/topics/nip-22/) comments are supported on server announcements, so the community can discuss and rate MCP servers directly on Nostr.

- **[NIP-73: OSM Tag Kind](https://github.com/nostr-protocol/nips/pull/2224)**: DestBro proposes adding OpenStreetMap identifiers to [NIP-73 (External Content IDs)](/en/topics/nip-73/), which standardizes how Nostr events reference external content like books (ISBN), movies (ISAN), podcast feeds (GUID), geohashes, and URLs via `i` and `k` tags. The proposed OSM kind would let events reference specific map features (buildings, roads, parks) by their OpenStreetMap node or way ID, connecting Nostr content to the open geographic database.

- **[NIP-XX: Responsive Image Variants](https://github.com/nostr-protocol/nips/pull/2219)**: woikos proposes extending [NIP-94](/en/topics/nip-94/) file metadata events with tags for responsive image variants at different resolutions. Clients could select the appropriate variant based on display size and network conditions, reducing bandwidth for mobile users viewing high-resolution images hosted on [Blossom](/en/topics/blossom/) servers.

## NIP Deep Dive: NIP-85 (Trusted Assertions)

[NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) defines a system for delegating expensive calculations to trusted service providers who publish signed results as Nostr events. Web of Trust scores and engagement metrics require crawling many relays and processing large event volumes, work that is impractical on mobile devices. This week's [merge](https://github.com/nostr-protocol/nips/pull/2223) added guidance on the client discovery process for these providers.

**Delegation:**

Calculating a user's Web of Trust score requires crawling follow graphs multiple hops deep across many relays, and computing accurate follower counts means deduplicating across the entire relay network. Mobile devices and browser clients cannot perform these operations, yet the results are essential for spam filtering and content ranking. NIP-85 bridges this gap by letting users designate trusted providers to run the computations and publish results as standard Nostr events.

**Protocol Design:**

NIP-85 uses four event kinds for assertions about different subject types. User assertions (kind 30382) carry follower count, post/reply/reaction counts, zap amounts, normalized rank (0-100), common topics, and active hours:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30382,
  "tags": [
    ["d", "e88a691e98d9987c964521dff60025f60700378a4879180dcbbb4a5027850411"],
    ["rank", "89"],
    ["followers", "4521"],
    ["first_created_at", "1609459200"],
    ["post_cnt", "1283"],
    ["reply_cnt", "647"],
    ["reactions_cnt", "8920"],
    ["zap_amt_recd", "850000"],
    ["zap_amt_sent", "320000"],
    ["zap_cnt_recd", "412"],
    ["zap_cnt_sent", "198"],
    ["zap_avg_amt_day_recd", "1150"],
    ["zap_avg_amt_day_sent", "430"],
    ["reports_cnt_recd", "2"],
    ["reports_cnt_sent", "0"],
    ["t", "nostr"],
    ["t", "bitcoin"],
    ["active_hours_start", "14"],
    ["active_hours_end", "22"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Event assertions (kind 30383) rate individual notes with comment count, quote count, reposts, reactions, and zap data:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30383,
  "tags": [
    ["d", "<target event id>"],
    ["rank", "72"],
    ["comment_cnt", "45"],
    ["quote_cnt", "12"],
    ["repost_cnt", "89"],
    ["reaction_cnt", "310"],
    ["zap_cnt", "23"],
    ["zap_amount", "125000"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

For addressable events (long-form articles, wiki pages), kind 30384 applies the same engagement metrics across all versions collectively. Kind 30385 rates external identifiers (books, movies, websites, locations, hashtags) referenced through [NIP-73 (External Content IDs)](/en/topics/nip-73/), which standardizes how Nostr events reference external content via `i` and `k` tags:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30385,
  "tags": [
    ["d", "isbn:9780765382030"],
    ["k", "isbn"],
    ["rank", "94"],
    ["comment_cnt", "67"],
    ["reaction_cnt", "203"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Each assertion is a replaceable addressable event where the `d` tag contains the subject: a pubkey, event ID, event address, or NIP-73 identifier. Service providers sign these events with their own keys, and clients evaluate them based on trust relationships.

**Provider Discovery:**

Users declare which assertion providers they trust by publishing kind 10040 events. Each entry specifies the assertion type with the provider pubkey and relay hint, plus optional algorithm variants:

```json
{
  "id": "<event hash>",
  "pubkey": "<user pubkey>",
  "created_at": 1739836800,
  "kind": 10040,
  "tags": [
    ["30382:rank", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30382:rank", "3d842afe...", "wss://nostr.wine"],
    ["30382:zap_amt_sent", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30383:rank", "4fd5e210...", "wss://nip85.nostr.band"]
  ],
  "content": "",
  "sig": "<user signature>"
}
```

Users can encrypt the tag list in `.content` using [NIP-44](/en/topics/nip-44/) to keep their provider preferences private. Clients build a provider list by checking which providers their followed accounts trust, creating a decentralized reputation layer for the assertion providers themselves.

**Security Model:**

Providers must use different service keys for distinct algorithms, and a unique key per user when algorithms are personalized, preventing cross-correlation of queries across users. Each service key gets a kind 0 metadata event describing the algorithm's behavior, giving users transparency into what they are trusting. Assertion events should only be updated when the underlying data actually changes, preventing unnecessary relay traffic and letting clients cache results with confidence.

**Current Adoption:**

NIP-85 formalizes a pattern already emerging informally. Primal's cache server computes engagement metrics and Web of Trust scores. [Antiprimal](https://gitlab.com/soapbox-pub/antiprimal), covered in [Newsletter #9](/en/newsletters/2026-02-11-newsletter/#antiprimal-standards-compliant-gateway-to-primals-cache), bridges these calculations to standard Nostr clients using NIP-85 event kinds. [Nostr.band](https://nostr.band) operates the `wss://nip85.nostr.band` relay referenced in the spec's own examples, serving assertion events for its search index data. On the client side, [Amethyst](https://github.com/vitorpamplona/amethyst) (authored by vitorpamplona, who also wrote this NIP) has experimental Trusted Assertions support in its `quartz` library, parsing assertion events and service provider declarations. [Vertex](https://vertexlab.io) computes similar Web of Trust metrics but [chose a different approach](https://vertexlab.io/blog/dvms_vs_nip_85/), using a direct API instead of NIP-85 events, citing the discovery problem and computational overhead of assertion-based architectures. With NIP-85, any client can consume assertions from any provider through a standard event format, and providers compete on accuracy while users choose whom to trust.

## NIP Deep Dive: NIP-52 (Calendar Events)

[NIP-52](https://github.com/nostr-protocol/nips/blob/master/52.md) defines calendar events on Nostr, giving clients a standard way to represent and discover occurrences at specific moments or between moments. This week's [D tag merge](https://github.com/nostr-protocol/nips/pull/1752) added day-granularity indexing, completing a missing piece in the spec's query infrastructure.

**Two Event Types:**

NIP-52 separates calendar events into two kinds based on temporal precision. Date-based events (kind 31922) represent all-day occurrences like holidays or multi-day festivals. They use ISO 8601 date strings in their `start` and optional `end` tags, with no time zone consideration:

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1735689600,
  "kind": 31922,
  "content": "Annual celebration of Bitcoin's genesis block",
  "tags": [
    ["d", "bitcoin-independence-day-2026"],
    ["title", "Bitcoin Independence Day"],
    ["start", "2026-01-03"],
    ["end", "2026-01-04"],
    ["location", "Worldwide"],
    ["g", "u4pruydqqv"],
    ["t", "bitcoin"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["r", "https://bitcoinindependenceday.com"]
  ],
  "sig": "<event creator signature>"
}
```

Time-based events (kind 31923) represent specific moments with Unix timestamps in their `start` and optional `end` tags, plus IANA time zone identifiers (`start_tzid`, `end_tzid`) for display. Both kinds are parameterized replaceable events, so organizers update details by publishing a new event with the same `d` tag.

**Calendars and RSVPs:**

Kind 31924 events define calendars as collections, referencing events via `a` tags that point to kind 31922 or 31923 events by their address coordinates:

```json
{
  "id": "<event hash>",
  "pubkey": "<calendar owner pubkey>",
  "created_at": 1739836800,
  "kind": 31924,
  "content": "Nostr community events worldwide",
  "tags": [
    ["d", "nostr-community-calendar"],
    ["title", "Nostr Community Events"],
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["a", "31922:<organizer-pubkey>:bitcoin-independence-day-2026"]
  ],
  "sig": "<calendar owner signature>"
}
```

Users can maintain multiple calendars (personal, work, community) and clients can subscribe to calendars from specific pubkeys. Calendar events can include an `a` tag referencing a calendar to request inclusion, enabling collaborative calendar management where multiple users contribute events to calendars they do not own.

RSVPs use kind 31925, where users publish their attendance status along with an optional free/busy indicator:

```json
{
  "id": "<event hash>",
  "pubkey": "<attendee pubkey>",
  "created_at": 1739836800,
  "kind": 31925,
  "content": "Looking forward to it",
  "tags": [
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["e", "<kind 31923 event id>", "wss://relay.example.com"],
    ["d", "<unique-rsvp-id>"],
    ["status", "accepted"],
    ["fb", "busy"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com"]
  ],
  "sig": "<attendee signature>"
}
```

Valid `status` values are "accepted", "declined", "tentative", and the optional `fb` tag marks the user as free or busy for that period. RSVP events reference the calendar event's `a` tag and carry the organizer's `p` tag, so the organizer's client can aggregate responses across relays.

**The D Tag Addition:**

Before this week's merge, clients querying for events in a date range had to fetch all events from a pubkey or calendar and filter client-side. The new required `D` tag on time-based events (kind 31923) contains a day-granularity Unix timestamp calculated as `floor(unix_seconds / 86400)`. Multi-day events carry multiple `D` tags, one per day. Relays can now index events by day and respond to filtered queries efficiently, turning what was a client-side filtering problem into a relay-side index lookup.

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1739836800,
  "kind": 31923,
  "content": "Monthly meetup for Nostr developers in Austin",
  "tags": [
    ["d", "nostr-meetup-2026"],
    ["title", "Nostr Developer Meetup"],
    ["summary", "Talks and demos from local Nostr builders"],
    ["image", "https://example.com/meetup-banner.jpg"],
    ["start", "1740067200"],
    ["end", "1740078000"],
    ["start_tzid", "America/New_York"],
    ["end_tzid", "America/New_York"],
    ["D", "20139"],
    ["location", "Bitcoin Commons, Austin TX"],
    ["g", "9v6knb2pg"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["p", "<speaker-pubkey>", "wss://relay.example.com", "speaker"],
    ["t", "nostr"],
    ["t", "meetup"],
    ["r", "https://bitcoincommons.com"]
  ],
  "sig": "<event creator signature>"
}
```

The `D` value `20139` equals `floor(1740067200 / 86400)`, placing this event on February 20, 2025. Clients querying for "all events this week" send a filter with the corresponding `D` range, and relays return only matching events.

**Design Decisions:**

NIP-52 intentionally omits recurring events. The spec leaves recurrence rules (RRULE from iCalendar) out entirely, delegating that complexity to clients. An organizer publishes individual events for each occurrence, keeping the relay-side data model simple. Participant tags carry optional roles ("host", "speaker", "attendee"), and location tags can include geohash `g` tags for spatial queries alongside human-readable addresses.

**Implementations:**

[Flockstr](https://github.com/zmeyer44/flockstr) is the primary calendar client built on NIP-52. [Coracle](https://gitea.coracle.social/coracle/coracle) displays calendar events in its social feed. The `D` tag addition this week enables relay-side temporal indexing that both clients can use to reduce bandwidth when querying for events in a specific date range.

---

That's it for this week. Building something or have news to share? Want us to cover your project? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Reach out via [NIP-17](/en/topics/nip-17/) DM</a> or find us on Nostr.
