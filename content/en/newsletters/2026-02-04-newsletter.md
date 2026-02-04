---
title: 'Nostr Compass #8'
date: 2026-02-04
publishDate: 2026-02-04
draft: false
type: newsletters
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** rust-nostr ships a major API redesign with 21 PRs overhauling the SDK's architecture. Nostria 3.0 launches with dual pane navigation, lists management, and a complete UI overhaul. Vector adds SIMD acceleration achieving 65x-184x speedups and ships [Marmot](/en/topics/marmot/) protocol support for encrypted group messaging. Frostr brings threshold signing to iOS via TestFlight. Damus implements [NIP-19 (Bech32 Encoded Entities)](/en/topics/nip-19/) relay hints for cross-relay content discovery. Primal Android adds NWC encryption and wallet transaction exports. nostr-tools and NDK receive reliability improvements. NIP-82 (Software Applications) expands to cover 98% of device platforms. The NIPs repository merges hold invoice support for [NIP-47 (Nostr Wallet Connect)](/en/topics/nip-47/). New protocol proposals include NIP-74 for podcasting, NIP-DB for browser event databases, and a TRUSTed Filters suite for decentralized content curation. New projects include Instagram to Nostr v2 for content migration, Pod21 launching a decentralized 3D printing marketplace, Clawstr introducing AI agent-managed communities, and Shosho and NosCall expanding live streaming and video calling capabilities.

## News

### rust-nostr Ships Major API Redesign

The [rust-nostr](https://github.com/rust-nostr/nostr) SDK underwent a significant architecture overhaul this week with 21 merged PRs introducing breaking changes across the library. The redesign affects core APIs that most Rust developers rely on.

[PR #1245](https://github.com/rust-nostr/nostr/pull/1245) redesigns notification APIs, while [PR #1244](https://github.com/rust-nostr/nostr/pull/1244) replaces `RelayNotification::Shutdown` with `RelayStatus::Shutdown` for cleaner state handling. The signer APIs now align with other SDK patterns via [PR #1243](https://github.com/rust-nostr/nostr/pull/1243). Client and Relay methods received cleanup in [PR #1242](https://github.com/rust-nostr/nostr/pull/1242), and client options now use a builder pattern ([PR #1241](https://github.com/rust-nostr/nostr/pull/1241)).

Message sending APIs were redesigned in [PR #1240](https://github.com/rust-nostr/nostr/pull/1240), REQ unsubscription in [PR #1239](https://github.com/rust-nostr/nostr/pull/1239), and relay removal in [PR #1229](https://github.com/rust-nostr/nostr/pull/1229). An [open PR #1246](https://github.com/rust-nostr/nostr/pull/1246) adds support for blocking APIs to round out the redesign.

The changes bring consistency to the SDK but will require migration effort from existing projects. Developers building on rust-nostr should review the changelog carefully before upgrading.

### Instagram to Nostr v2 Enables Content Migration

A new tool enables creators to migrate their existing content from centralized platforms to Nostr. [Instagram to Nostr v2](https://github.com/primalpaul1/instagram-to-nostr-v2) supports importing from Instagram, TikTok, Twitter, and Substack without requiring access to the user's private keys.

The tool addresses a common onboarding barrier: users hesitant to start fresh on a new platform can now preserve their content history. It also supports gifting Nostr accounts to new users or proposing content to existing accounts, making it useful for helping others transition to the protocol.

### Pod21: Decentralized 3D Printing Network

[Pod21](https://pod21.com) connects 3D printer operators with buyers using Nostr for marketplace coordination. The platform includes a [NIP-17 (Private Direct Messages)](/en/topics/nip-17/) compatible DM bot that handles marketplace interactions, allowing buyers to request prints and negotiate with makers through encrypted direct messages.

Makers list their printing capacity and capabilities; buyers browse listings and initiate orders via the bot. The architecture follows a similar pattern to other Nostr commerce applications: relay-based discovery, encrypted messaging for order coordination, and Lightning for settlement. Pod21 joins Ridestr and Shopstr as Nostr applications coordinating real-world transactions through the protocol.

### Clawstr: AI Agent Social Network

[Clawstr](https://github.com/clawstr/clawstr) launches as a Reddit-inspired platform where AI agents create and manage communities on Nostr. The platform enables autonomous agents to establish topical communities, curate content, and engage with users. Communities function like subreddits but with AI moderators and curators guiding discussions. The architecture uses Nostr's open protocol for agent-to-agent and agent-to-human interactions, establishing a new model for community formation on decentralized social media.

## Releases

### Ridestr v0.2.0: RoadFlare Release

[Ridestr](https://github.com/variablefate/ridestr) shipped [v0.2.0](https://github.com/variablefate/ridestr/releases/tag/v0.2.0), dubbed the "RoadFlare Release," introducing personal rideshare networks. The feature lets riders add favorite drivers to a trusted network. Drivers approve followers and share encrypted locations, enabling riders to see when trusted drivers are online and nearby. Ride requests go directly to known drivers.

Payment reliability improved with automatic escrow recovery, better wallet sync across devices, and faster payment processing via progressive polling. [PR #37](https://github.com/variablefate/ridestr/pull/37) adds the Phase 5-6 infrastructure supporting these features. [v0.2.1](https://github.com/variablefate/ridestr/releases/tag/v0.2.1) followed with hotfixes for payment dialog bugs and the post-ride "Add to Favorites" flow.

### Nostria 3.0

[Nostria](https://github.com/nostria-app/nostria), sondreb's cross-platform client built for global scale, shipped version 3.0 with a complete UI overhaul, new logo, and hundreds of fixes. The release represents an intensive six-week development cycle.

Dual pane navigation is the biggest UX change, allowing desktop users to reduce context switching when moving between lists, details, and threads. A new Home section provides an overview of all available features, and all screens share a unified toolbar, layout, and functionality.

Lists management is the most significant feature update, integrating throughout the application. Users can manage profile lists and filter content in any feature: Streams, Music, or Feeds. Tired of spam in threads? Filter by favorites to see only their replies. Quick Zaps adds one-tap zapping with configurable values. Copy/Screenshot generates clipboard screenshots for sharing events anywhere. Muted Words now filters on profile fields (name, display_name, NIP-05), enabling users to block all bridged profiles with a single banned word. Settings became searchable for faster configuration changes.

The release adds BOLT11 and BOLT12 payment request rendering, text-size and font selection, and "Note-to-Self" messaging in the Messages section with rendering of referenced content like articles and events. The new Share dialog enables quick sharing via email, websites, or direct messages to multiple recipients. Additional features include custom emoji sets, Interests (hashtag lists as dynamic feeds), Bookmarks, Public Relay Feeds, and full menu customization including which option the Nostria icon opens.

Available on Android, iOS, Windows, and web at [nostria.app](https://www.nostria.app/).

### Applesauce v5.1.0

hzrd149's [Applesauce](https://github.com/hzrd149/applesauce) library suite released v5.1.0 across all packages. [applesauce-signers](https://github.com/hzrd149/applesauce/releases/tag/applesauce-signers%405.1.0) adds support for `switch_relays` and `ping` methods on Nostr Connect remote signers, useful for managing signer connections programmatically. [applesauce-loaders](https://github.com/hzrd149/applesauce/releases/tag/applesauce-loaders%405.1.0) introduces `loadAsyncMap` for parallel async loading. [applesauce-react](https://github.com/hzrd149/applesauce/releases/tag/applesauce-react%405.1.0) adds padding arguments to `useAction().run()`. [applesauce-core](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.1.0) updates event-to-store mapping to handle strings directly without requiring `onlyEvents`.

### nak v0.18.3

fiatjaf's [nak](https://github.com/fiatjaf/nak) (Nostr Army Knife) reached [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3) with stability fixes from mattn. The release prevents panics when mint URLs lack the `://` separator, validates dateparser errors before using date values, and handles edge cases in AUTH challenge tag parsing. These defensive fixes make the CLI more resilient when processing malformed inputs.

### Aegis v0.3.7

[Aegis](https://github.com/ZharlieW/Aegis), the cross-platform desktop signer, shipped [v0.3.7](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.7) adding Nostr App Browser support with [NIP-07 (Browser Extension Interface)](/en/topics/nip-07/) signing. The release records [NIP-04 (Encrypted Direct Messages)](/en/topics/nip-04/) and [NIP-44 (Versioned Encryption)](/en/topics/nip-44/) encryption events, allowing users to track which applications request encryption operations. The browser segment now filters by platform to show only web apps.

### Bitchat v1.5.1 (iOS)

[Bitchat](https://github.com/permissionlesstech/bitchat), the offline-capable messaging app using Nostr and Bluetooth mesh, released [v1.5.1](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.1) with iOS security hardening. [PR #1012](https://github.com/permissionlesstech/bitchat/pull/1012) validates Nostr event signatures before processing, rejects invalid giftwraps and embedded packets, caps oversized payloads, and blocks spoofed BLE announce sender IDs. [PR #998](https://github.com/permissionlesstech/bitchat/pull/998) fixes iOS BLE mesh authentication by binding sender IDs to connection UUIDs, preventing identity spoofing in the mesh network. [PR #972](https://github.com/permissionlesstech/bitchat/pull/972) adds notification rate limiting to prevent peer discovery floods when multiple mesh devices are nearby.

### KeyChat v1.39.2

[KeyChat](https://github.com/keychat-io/keychat-app) released [v1.39.2](https://github.com/keychat-io/keychat-app/releases/tag/v1.39.2%2B6495) adding [NIP-47](/en/topics/nip-47/) Nostr Wallet Connect support via [PR #148](https://github.com/keychat-io/keychat-app/pull/148). Users can now connect external Lightning wallets for payments within the messaging app. The release also adds macOS desktop notifications.

### Nostrmo v3.5.0

[Nostrmo](https://github.com/haorendashu/nostrmo), the cross-platform Flutter client, shipped [v3.5.0](https://github.com/haorendashu/nostrmo/releases/tag/3.5.0) overhauling its feed system. The update replaces fixed feeds with customizable alternatives: General Feed, Mentioned Feed, and Relay Feed, each configurable through new edit pages. The release implements outbox model support for better event routing and expands local relay functionality with configurable size limits and subscription support.

### Shosho v0.11.1

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), the live streaming app for Nostr, released [v0.11.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.11.1) with recording and VOD capabilities. The update adds room presence indicators showing who is watching streams, threaded chat conversations for better discussion organization, and Nostr Connect support on iOS via [NIP-46](/en/topics/nip-46/). Streamers can now save their broadcasts for later viewing while maintaining real-time chat interactions with their audience.

### NosCall v0.5.0

[NosCall](https://github.com/sanah9/noscall), the audio and video calling app for Nostr, shipped [v0.5.0](https://github.com/sanah9/noscall/releases/tag/v0.5.0-release) with contact groups for organizing calls by category, relay management for connection optimization, and configurable ICE server settings for improved NAT traversal. The release also adds dark mode support. NosCall uses Nostr for call signaling and coordination, enabling peer-to-peer calls without centralized servers.

### diVine 1.0.4

[diVine](https://github.com/divinevideo/divine-mobile), rabble's short-form looping video client, released [1.0.4](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.4) as an Android pre-release alpha ahead of its Zapstore submission. The release focuses on testing Nostr key management, including nsec import, [NIP-46 (Nostr Connect)](/en/topics/nip-46/) remote signing with nsecBunker and Amber, and nostrconnect:// URL handling. The team is soliciting feedback on relay compatibility and video interoperability with other clients. [PR #1265](https://github.com/divinevideo/divine-mobile/pull/1265) fixes iOS file path handling that caused video clips to become unusable after app updates by storing relative paths instead of absolute container paths. [PR #1251](https://github.com/divinevideo/divine-mobile/pull/1251) fixes navigation issues when viewing profiles from comments.

### Zeus v0.12.2

[Zeus](https://github.com/ZeusLN/zeus) shipped [v0.12.2](https://github.com/ZeusLN/zeus/releases/tag/v0.12.2) as a stable release, consolidating the [NWC fixes covered in previous editions](/en/newsletters/2026-01-28-newsletter/#zeus-v0122-beta---nwc-fixes).

### Frostr Igloo iOS TestFlight

[Frostr](https://frostr.org/) launched [Igloo for iOS](https://github.com/FROSTR-ORG/igloo-ios-prototype) on [TestFlight](https://testflight.apple.com/join/72hjQe3J), expanding threshold signing to Apple devices. Frostr uses FROST (Flexible Round-Optimized Schnorr Threshold) signatures to split nsec keys into shares distributed across devices, enabling k-of-n signing with fault tolerance. Users joining in "demo mode" participate in a live 2-of-2 threshold signature experiment, demonstrating the protocol's real-time coordination capabilities. The iOS release joins [Igloo for Android](https://github.com/FROSTR-ORG/igloo-android) (v0.1.2), which shipped in December with [NIP-55 (Android Signer)](/en/topics/nip-55/) support for cross-app signing requests. Both mobile clients complement [Igloo desktop](https://github.com/FROSTR-ORG/igloo-desktop) and the [Frost2x](https://github.com/FROSTR-ORG/frost2x) browser extension.

## Project Updates

### Damus Implements NIP-19 Relay Hints

[Damus](https://github.com/damus-io/damus) merged [PR #3477](https://github.com/damus-io/damus/pull/3477), implementing [NIP-19](/en/topics/nip-19/) relay hint consumption for event fetching. The feature enables viewing notes on relays not in the user's configured pool by extracting hints from [NIP-10 (Reply Threads)](/en/topics/nip-10/), [NIP-18 (Reposts)](/en/topics/nip-18/), and NIP-19 references. The implementation uses ephemeral relay connections with reference-counted cleanup, avoiding permanent relay pool expansion.

Additional fixes include Lightning invoice parsing ([PR #3566](https://github.com/damus-io/damus/pull/3566)), wallet view loading ([PR #3554](https://github.com/damus-io/damus/pull/3554)), relay list timing ([PR #3553](https://github.com/damus-io/damus/pull/3553)), and profile preloading to reduce visual "popping" ([PR #3550](https://github.com/damus-io/damus/pull/3550)). A [draft PR #3590](https://github.com/damus-io/damus/pull/3590) shows [NIP-17](/en/topics/nip-17/) private DM support in progress.

### Primal Android Ships NWC Encryption

[Primal Android](https://github.com/PrimalHQ/primal-android-app) had a very active week with 18 merged PRs focused on wallet infrastructure. The app now integrates with Spark, Lightspark's self-custodial Lightning protocol. [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874) adds NWC encryption support, while [PR #872](https://github.com/PrimalHQ/primal-android-app/pull/872) sends NWC info events when connections establish.

[PR #870](https://github.com/PrimalHQ/primal-android-app/pull/870) enables CSV export for wallet transactions, useful for accounting and tax purposes. [PR #716](https://github.com/PrimalHQ/primal-android-app/pull/716) adds a local account switcher in the Note Editor. Multiple wallet restore fixes ([PR #876](https://github.com/PrimalHQ/primal-android-app/pull/876), [PR #875](https://github.com/PrimalHQ/primal-android-app/pull/875), [PR #873](https://github.com/PrimalHQ/primal-android-app/pull/873)) address edge cases for users with non-Spark wallet configurations.

### Marmot TypeScript SDK Adds Message History

The [Marmot](https://github.com/marmot-protocol/marmot) protocol's TypeScript implementation continues development. [PR #38](https://github.com/marmot-protocol/marmot-ts/pull/38) by hzrd149 implements message history persistence with pagination for the reference chat application, while [PR #39](https://github.com/marmot-protocol/marmot-ts/pull/39) improves library ergonomics.

On the Rust side, [PR #161](https://github.com/marmot-protocol/mdk/pull/161) implements retryable state handling to preserve message context on failure, and [PR #164](https://github.com/marmot-protocol/mdk/pull/164) switches to std::sync::Mutex to avoid tokio panics with SQLite. The whitenoise-rs backend adds [Amber integration](https://github.com/marmot-protocol/whitenoise-rs/pull/418) ([PR #418](https://github.com/marmot-protocol/whitenoise-rs/pull/418)), [upgrades to MDK and nostr-sdk 0.44](https://github.com/marmot-protocol/whitenoise-rs/pull/467) ([PR #467](https://github.com/marmot-protocol/whitenoise-rs/pull/467)), and introduces real-time notification streaming via [PR #460](https://github.com/marmot-protocol/whitenoise-rs/pull/460) with NewMessage and GroupInvite event types.

### HAVEN Adds Periodic WoT Refresh

[HAVEN](https://github.com/bitvora/haven), the personal relay, merged [PR #108](https://github.com/bitvora/haven/pull/108) adding periodic [Web of Trust](/en/topics/web-of-trust/) refresh. The feature ensures trust scores stay current as users' social graphs evolve, improving spam filtering accuracy over time.

### nostr-tools

[nostr-tools](https://github.com/nbd-wtf/nostr-tools), the core JavaScript library, received multiple improvements this week. Commits include a [fix for hashtag parsing after newlines](https://github.com/nbd-wtf/nostr-tools/commit/c2423f7f31853d97fef2e3d649204cec328e81d5) in [NIP-27 (Text Note References)](/en/topics/nip-27/) mentions, [automatic pruning of broken relay objects with idle tracking](https://github.com/nbd-wtf/nostr-tools/commit/ab802c8dbe35d29feb732ba54e82a346c21c32e2) for connection cleanup, [message queue removal](https://github.com/nbd-wtf/nostr-tools/commit/be9b91318fea6a0cb154b8734a15b50a4c1e7638) for single-threaded performance optimization, and [source file exports](https://github.com/nbd-wtf/nostr-tools/commit/05b1fba5113182ac0aa3c72d1f511cd956a7c139) for better TypeScript imports.

### NDK

[NDK](https://github.com/nostr-dev-kit/ndk) shipped [beta.71](https://github.com/nostr-dev-kit/ndk/commit/26abea24726ed844fdd091744ac9f768f1a530a0) with a [fix for reconnection after device sleep/wake cycles and stale connection handling](https://github.com/nostr-dev-kit/ndk/commit/33e759508bc656dc45d3d77c741edf581af323f3), addressing reliability issues for mobile applications.

### Notedeck

[Notedeck](https://github.com/damus-io/notedeck), the Damus team's desktop client, has an [open PR #1279](https://github.com/damus-io/notedeck/pull/1279) adding a [NIP-34 (Git Collaboration)](/en/topics/nip-34/) viewer. This would enable browsing git repositories, patches, and issues published to Nostr relays directly within the client, making Notedeck a potential front-end for ngit-based workflows.

### njump

[njump](https://github.com/fiatjaf/njump), the Nostr web gateway, added support for two [NIP-51 (Lists)](/en/topics/nip-51/) event types via [PR #152](https://github.com/fiatjaf/njump/pull/152). The gateway now renders kind:30000 Follow Sets, which are categorized groupings of users that clients can display in different contexts, and kind:39089 Starter Packs, which are curated profile collections designed for sharing and group following. These additions let njump display community-curated lists when users share nevent links.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), the Android client, fixed a bug preventing video sharing from the player view ([PR #1695](https://github.com/vitorpamplona/amethyst/pull/1695)). The "Share video" option was failing to appear because the content parameter was not being passed to the control buttons component. Users can now share Nostr video content to other apps directly from the player. [PR #1693](https://github.com/vitorpamplona/amethyst/pull/1693) fixes Jackson JSON deserialization crashes that occurred when parsing certain malformed events.

### Jumble

[Jumble](https://github.com/CodyTseng/jumble), the web client focused on relay feed browsing, added audio file uploads via clipboard in [PR #743](https://github.com/CodyTseng/jumble/pull/743). Users can now paste audio files directly into the post editor, which uploads them to configured media servers and embeds the URL in the note. The feature mirrors existing image paste functionality.

### Flotilla

[Flotilla](https://github.com/coracle-social/flotilla), hodlbod's [NIP-29 (Relay-Based Groups)](/en/topics/nip-29/) communities client, shipped notifications via [PR #270](https://github.com/coracle-social/flotilla/pull/270). The update refactors the alert system from anchor-based polling to local pull notifications for web and push notifications for mobile. The architecture implements the proposed NIP-9a standard (see [PR #2194](https://github.com/nostr-protocol/nips/pull/2194) below), where users register webhook callbacks with relays and receive encrypted event payloads when filters match.

### Formstr

[Formstr](https://github.com/abh3po/nostr-forms), the Nostr-native forms application, added form import and encrypted form support in [PR #422](https://github.com/abh3po/nostr-forms/pull/422). Users can now import existing forms from JSON or other Formstr instances. The encryption feature allows form creators to restrict responses so only designated recipients can read submissions, useful for surveys collecting sensitive information.

### Pollerama

[Pollerama](https://pollerama.fun), built on the [nostr-polls](https://github.com/abh3po/nostr-polls) library, added [NIP-17](/en/topics/nip-17/) DM sharing for polls via [PR #141](https://github.com/abh3po/nostr-polls/pull/141) and [PR #142](https://github.com/abh3po/nostr-polls/pull/142). Users can now share polls directly to contacts through encrypted direct messages.

### Nostrability Schemata

[Nostrability schemata](https://github.com/nostrability/schemata), the JSON verification schema collection for Nostr events, added [NIP-59 (Gift Wrap)](/en/topics/nip-59/) coverage via [PR #59](https://github.com/nostrability/schemata/pull/59). The update includes schemas for kind 13 (seal) and kind 1059 (gift wrap) events, complementing existing [NIP-17](/en/topics/nip-17/) schema coverage.

### Vector

[Vector](https://github.com/VectorPrivacy/Vector), the privacy-focused desktop messenger using [NIP-17](/en/topics/nip-17/), [NIP-44](/en/topics/nip-44/), and [NIP-59](/en/topics/nip-59/) for zero-metadata encryption, merged [PR #39](https://github.com/VectorPrivacy/Vector/pull/39) introducing SIMD-accelerated performance optimizations. Hex encoding runs 65x faster, image preview generation up to 38x faster, and message lookups 184x faster via binary search indexing. The PR adds ARM64 NEON intrinsics for Apple Silicon and x86_64 AVX2/SSE2 with runtime detection for Windows and Linux. Memory usage dropped with message structs reduced from 472 to 128 bytes and npub storage cut by 99.6% through interning.

Vector v0.3.0 (December 2025) integrated [MDK (Marmot Development Kit)](https://github.com/marmot-protocol/mdk) for MLS protocol-based group messaging, bringing end-to-end encrypted groups with forward secrecy to the client. MIP-04 file sharing now handles imeta attachments for MLS groups, designed for interoperability with [White Noise](/en/newsletters/2026-01-28-newsletter/#marmot-typescript-sdk-adds-message-history). The release also introduced a Mini Apps platform with WebXDC-based P2P multiplayer games, a decentralized app store called The Nexus, PIVX wallet integration for in-app payments, message editing with full history tracking, and 4x memory reduction during image uploads.

## NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-47: Hold Invoice Support](https://github.com/nostr-protocol/nips/pull/1913)** - [NIP-47 (Nostr Wallet Connect)](/en/topics/nip-47/) now supports hold invoices, enabling advanced payment workflows where receivers must explicitly settle or cancel payments. The PR adds three new RPC methods: `make_hold_invoice` creates a hold invoice using a pre-generated preimage and payment hash, `settle_hold_invoice` claims payment by providing the original preimage, and `cancel_hold_invoice` rejects payment using its payment hash. A new `hold_invoice_accepted` notification fires when a payer locks in payment. This enables use cases like pay-to-unlock content, marketplace escrow systems, and payment gating. Implementations are already underway in [Alby Hub](https://github.com/getAlby/hub/pull/1298), [Alby JS-SDK](https://github.com/getAlby/js-sdk/pull/382), and [dart NDK](https://github.com/relaystr/ndk/pull/147).

- **[NIP-05: Lowercase Requirement](https://github.com/nostr-protocol/nips/pull/2208)** - [NIP-05 (Domain Verification)](/en/topics/nip-05/) now explicitly requires lowercase for both hex public keys and local names in the `nostr.json` file. This was implicit in the spec but not stated, causing interoperability issues when some implementations used mixed case while others normalized to lowercase. Clients validating NIP-05 identifiers should now reject any `nostr.json` responses containing uppercase characters in keys or names.

- **[NIP-73: Country Codes](https://github.com/nostr-protocol/nips/pull/2205)** - [NIP-73 (Geotags)](/en/topics/nip-73/) now supports ISO 3166 country codes as an alternative to geohashes. Events can include `["g", "US", "countryCode"]` tags to indicate country-level location without requiring precise coordinates. This enables country-based content filtering and discovery for applications where exact location is unnecessary or undesirable. The PR also added a missing geohash example to the spec documentation.

**Open PRs and Discussions:**

- **[NIP-82: Software Applications](https://github.com/nostr-protocol/nips/pull/1336)** - franzap announced a major update to this draft specification, which defines how software applications are distributed via Nostr using kind 30063 release events. The update now covers approximately 98% of device platforms globally, including macOS, Linux, Windows, FreeBSD, WASM environments, VS Code extensions, Chrome extensions, and Web Bundles/PWAs. The team is focusing next on Android, PWA, and iOS support, inviting developers to converge on this shared standard. Zapstore plans to migrate to the new format in the coming weeks.

- **[NIP-74: Podcasts](https://github.com/nostr-protocol/nips/pull/2211)** - Defines addressable events for podcast shows (kind 30074) and episodes (kind 30075). Shows include metadata like title, description, categories, and cover images. Episodes reference their parent show and include enclosure URLs, durations, and chapter markers. The spec integrates with Podcasting 2.0 metadata standards and includes value tags for V4V (value-for-value) monetization via Lightning. Platforms like [transmit.fm](https://transmit.fm), a Nostr-native podcast publishing platform, can publish directly to relays using this format, enabling podcasters to distribute content without intermediaries.

- **[NIP-FR: Friends-Only Notes](https://github.com/nostr-protocol/nips/pull/2207)** - Proposes a mechanism for publishing notes visible only to mutual follows. The implementation uses [NIP-59 (Gift Wrap)](/en/topics/nip-59/) to encrypt content: the author creates a regular note, then gift-wraps copies to each mutual follow. Each recipient's copy is encrypted to their pubkey using NIP-44 and sent via the gift wrap mechanism. Recipients can verify the note came from someone they follow, while non-mutuals cannot access the content. This approach reuses existing cryptographic infrastructure while enabling a frequently requested privacy feature.

- **[NIP-DB: Browser Nostr Event Database Interface](https://github.com/hzrd149/nostr-bucket)** - Proposes a standard `window.nostrdb` interface for browser extensions that provide local Nostr event storage. The API includes methods for adding events, querying by ID or filter, counting matches, and subscribing to updates. Web applications can use this interface to read from locally cached events without making relay requests, reducing bandwidth and latency. hzrd149's [nostr-bucket](https://github.com/hzrd149/nostr-bucket) browser extension provides a reference implementation, injecting the interface into all browser tabs. A companion [polyfill library](https://github.com/hzrd149/window.nostrdb.js) implements the same API using IndexedDB for environments without the extension.

- **[TRUSTed Filters](https://github.com/nostr-protocol/nips/pull/1534)** - A suite of five related proposals for decentralized content curation, building on vitorpamplona's [Trusted Assertions PR #1534](https://github.com/nostr-protocol/nips/pull/1534). The core specification introduces kind 17570 events for declaring Trust Provider Preferences, allowing users to specify which services they trust for event filtering and ranking. Trust providers publish assertions (kind 37571), statistics (kind 37572), and rankings (kind 37573) that clients can subscribe to. The system uses a plugin architecture with W/w tags to specify filter types and transformations. This enables computationally expensive operations like spam detection, reputation scoring, and content ranking to run on dedicated infrastructure while users maintain control over which providers they trust. The suite includes separate specs for filter presets, user rankings, trusted events, and plugin definitions.

- **[NIP-9a: Push Notifications](https://github.com/nostr-protocol/nips/pull/2194)** - hodlbod proposes a standard for relay-based push notifications using kind 30390 registration events. Users create a registration containing filters for events they want to receive and a webhook callback URL. The registration is encrypted to the relay's pubkey (from its NIP-11 `self` field). When matching events occur, relays POST to the callback with the event ID (plaintext for deduplication) and the event itself (NIP-44 encrypted to the user). This architecture lets relays push notifications while protecting event content from intermediary push servers. Flotilla's [PR #270](https://github.com/coracle-social/flotilla/pull/270) implements this standard.

- **[Catallax](https://github.com/SigmaEnterprise/Catallax)** - Proposes a decentralized contract work protocol with escrow using kind 33400 events. The system defines three roles: arbiters announce availability and terms, patrons create funded tasks with escrowed Bitcoin, and free agents complete work to claim payment. Arbiters resolve disputes when needed. The protocol enables trustless freelance work coordination where funds are locked until deliverables are accepted or arbitration concludes.

## NIP Deep Dive: NIP-47 (Nostr Wallet Connect)

[NIP-47](/en/topics/nip-47/) defines Nostr Wallet Connect (NWC), a protocol for remote Lightning wallet control using Nostr as the communication layer. With this week's hold invoice support addition, NWC now covers the full range of Lightning operations.

The protocol works through a simple exchange. A wallet application publishes a "wallet info" event (kind 13194) describing its capabilities. Client applications send encrypted requests (kind 23194) asking the wallet to perform operations like paying invoices, creating invoices, or checking balances. The wallet responds with encrypted results (kind 23195).

NWC uses [NIP-44](/en/topics/nip-44/) encryption between the client and wallet, with a dedicated keypair for wallet operations, keeping it separate from the user's main identity. This separation means compromising an NWC connection does not expose the user's Nostr identity.

**Supported Methods:**

The spec defines methods for core Lightning operations: `pay_invoice` sends payments, `make_invoice` generates invoices for receiving, `lookup_invoice` checks payment status, `get_balance` returns the wallet balance, and `list_transactions` provides payment history. The newly merged `pay_keysend` enables payments without invoices, and `hold_invoice` supports conditional payments.

**Example Events:**

The wallet service publishes an info event (kind 13194) advertising its capabilities:

```json
{
  "kind": 13194,
  "pubkey": "<wallet service pubkey>",
  "content": "pay_invoice get_balance make_invoice lookup_invoice list_transactions notifications",
  "tags": [
    ["encryption", "nip44_v2"],
    ["notifications", "payment_received payment_sent"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<wallet service signature>"
}
```

A client sends an encrypted request (kind 23194) to pay an invoice:

```json
{
  "kind": 23194,
  "pubkey": "<client ephemeral pubkey from connection URI secret>",
  "content": "<NIP-44 encrypted: {\"method\": \"pay_invoice\", \"params\": {\"invoice\": \"lnbc50n1...\"}}>",
  "tags": [
    ["p", "<wallet service pubkey>"],
    ["encryption", "nip44_v2"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<client ephemeral key signature>"
}
```

The wallet service responds (kind 23195) with the payment result:

```json
{
  "kind": 23195,
  "pubkey": "<wallet service pubkey>",
  "content": "<NIP-44 encrypted: {\"result_type\": \"pay_invoice\", \"result\": {\"preimage\": \"...\"}, \"error\": null}>",
  "tags": [
    ["p", "<client ephemeral pubkey>"],
    ["e", "<request event id>"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<wallet service signature>"
}
```

The `e` tag in the response references the original request, allowing clients to match responses to their requests.

**Hold Invoices:**

This week's [PR #1913](https://github.com/nostr-protocol/nips/pull/1913) added hold invoice support, enabling escrow-style payments. Unlike standard invoices where the recipient immediately claims payment by releasing the preimage, hold invoices let the recipient defer this decision. When a payer sends to a hold invoice, funds lock along the payment route. The recipient then chooses to either settle (release the preimage and claim funds) or cancel (reject payment, returning funds to the payer). If neither action occurs, the payment times out and funds return automatically. The PR adds three NWC methods: `make_hold_invoice`, `settle_hold_invoice`, and `cancel_hold_invoice`, plus a `hold_invoice_accepted` notification. This mechanism powers applications like Ridestr's rideshare escrow and marketplace dispute resolution.

**Current Implementations:**

Major wallets support NWC: Zeus, Alby, and Primal (as of this week's [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874)) all implement wallet-side support. On the client side, Damus, Amethyst, and most major Nostr clients can connect to NWC wallets for zapping and payments.

The protocol enables a separation of concerns: users can run their wallet on one device while interacting with Nostr from another, with Nostr relays serving as the communication channel. This architecture means mobile clients do not need to hold funds directly, improving security by keeping wallet infrastructure separate from social clients.

**Security Considerations:**

NWC connections should be treated as sensitive. While the encryption protects message content, the wallet pubkey and connection secret must be guarded. Applications should allow users to revoke connections and set spending limits. The protocol supports capability restrictions, so wallets can limit what operations a particular connection can perform.

## NIP Deep Dive: NIP-59 (Gift Wrap)

[NIP-59](/en/topics/nip-59/) defines a protocol for encapsulating any Nostr event in multiple layers of encryption, hiding the sender's identity from relays and observers. This week's proposals for friends-only notes (NIP-FR) and push notifications (NIP-9a) both rely on gift wrapping, making it a foundational privacy primitive worth understanding.

**The Three Layers:**

Gift wrapping uses three nested structures:

1. **Rumor** (unsigned event): The original content as a Nostr event without a signature. The rumor cannot be sent directly to relays because relays reject unsigned events.

2. **Seal** (kind 13): The rumor is encrypted using [NIP-44](/en/topics/nip-44/) and placed in a kind 13 event. The seal IS signed by the actual author's key. This is the cryptographic proof of authorship.

3. **Gift Wrap** (kind 1059): The seal is encrypted and placed in a kind 1059 event signed by a random, one-time keypair. The gift wrap includes a `p` tag for routing to the recipient.

**A Common Misconception: Deniability**

The spec mentions that unsigned rumors provide "deniability," but this is misleading. The seal layer IS signed by the real author. When the recipient decrypts the gift wrap and then the seal, they have cryptographic proof of who sent the message. The recipient could even construct a zero-knowledge proof revealing the sender's identity without exposing their own private key.

What gift wrap actually provides is **sender privacy from observers**: relays and third parties cannot determine who sent the message because they only see the gift wrap signed by a random key. But the recipient always knows, and can prove it.

**Example Events:**

Here is the complete three-layer structure from the spec (sending "Are you going to the party tonight?"):

The rumor (unsigned, cannot be published to relays):
```json
{
  "created_at": 1691518405,
  "content": "Are you going to the party tonight?",
  "tags": [],
  "kind": 1,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "id": "9dd003c6d3b73b74a85a9ab099469ce251653a7af76f523671ab828acd2a0ef9"
}
```

The seal (kind 13, signed by real author, contains encrypted rumor):
```json
{
  "kind": 13,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "content": "AqBCdwoS7/tPK+QGkPCadJTn8FxGkd24iApo3BR9/M0uw6n4RFAFSPAKKMgkzVMo...",
  "created_at": 1703015180,
  "tags": [],
  "id": "28a87d7c074d94a58e9e89bb3e9e4e813e2189f285d797b1c56069d36f59eaa7",
  "sig": "02fc3facf6621196c32912b1ef53bac8f8bfe9db51c0e7102c073103586b0d29..."
}
```

The gift wrap (kind 1059, signed by random ephemeral key, contains encrypted seal):
```json
{
  "kind": 1059,
  "pubkey": "18b1a75918f1f2c90c23da616bce317d36e348bcf5f7ba55e75949319210c87c",
  "content": "AhC3Qj/QsKJFWuf6xroiYip+2yK95qPwJjVvFujhzSguJWb/6TlPpBW0CGFwfuf...",
  "created_at": 1703021488,
  "tags": [["p", "166bf3765ebd1fc55decfe395beff2ea3b2a4e0a8946e7eb578512b555737c99"]],
  "id": "5c005f3ccf01950aa8d131203248544fb1e41a0d698e846bd419cec3890903ac",
  "sig": "35fabdae4634eb630880a1896a886e40fd6ea8a60958e30b89b33a93e6235df7..."
}
```

Notice: the seal's `pubkey` is the real author (`611df01...`), while the gift wrap's `pubkey` is a random one-time key (`18b1a75...`). Relays only see the gift wrap, so they cannot attribute the message to the real author.

**What Each Layer Protects:**

The rumor is unsigned and cannot be published to relays directly. The seal is signed by the real author and proves authorship to the recipient. The gift wrap is signed by a random one-time key, hiding the real author from relays and observers. Only the recipient can decrypt through both layers to reach the original content and verify the author's signature on the seal.

**Current Applications:**

[NIP-17 (Private Direct Messages)](/en/topics/nip-17/) uses gift wrap for encrypted DMs, replacing the older NIP-04 scheme. The proposed NIP-FR (friends-only notes) gift-wraps notes to each mutual follow. NIP-9a (push notifications) encrypts notification payloads using gift wrap principles.

**Metadata Protection:**

Timestamps should be randomized to thwart timing analysis. Relays should require AUTH before serving kind 1059 events and only serve them to the marked recipient. When sending to multiple recipients, create separate gift wraps for each.

---

That's it for this week. Building something? Have news to share? Want us to cover your project? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Reach out via NIP-17 DM</a> or find us on Nostr.
