---
title: 'Nostr Compass #18'
date: 2026-04-15
publishDate: 2026-04-15
draft: false
type: newsletters
description: 'Amethyst merges desktop Tor, C secp256k1, and WebRTC calls in a 29-PR week, nstrfy launches Nostr-native push notifications, HAMSTR adds Reticulum for Nostr over LoRa mesh, Bloom ships a self-hosted Blossom server, WaveFunc debuts as Nostr internet radio, Snort ships a security audit and performance overhaul, and Primal Android redesigns its feed layout.'
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** [Amethyst](https://github.com/vitorpamplona/amethyst) merges 29 PRs including [desktop Tor support](#amethyst-merges-desktop-tor-c-secp256k1-webrtc-calls-and-multi-wallet-nwc), a [custom C secp256k1 implementation](#amethyst-merges-desktop-tor-c-secp256k1-webrtc-calls-and-multi-wallet-nwc) with JNI bindings, a full [WebRTC call system](#amethyst-merges-desktop-tor-c-secp256k1-webrtc-calls-and-multi-wallet-nwc) for [NIP-AC](/en/topics/nip-ac/) voice and video calls, [RFC 9420 MLS compliance](#amethyst-merges-desktop-tor-c-secp256k1-webrtc-calls-and-multi-wallet-nwc) for [Marmot](/en/topics/marmot/), and [multi-wallet NWC](#amethyst-merges-desktop-tor-c-secp256k1-webrtc-calls-and-multi-wallet-nwc). [nstrfy](https://github.com/vcavallo/nstrfy-android) [launches](#nstrfy-launches-nostr-native-push-notifications-for-android) as an Android push notification app that replaces Firebase with Nostr relays using kind `7741` events. [HAMSTR](https://github.com/LibertyFarmer/hamstr) [adds Reticulum](#hamstr-adds-reticulum-for-nostr-over-lora-mesh) mesh networking, enabling Nostr events over LoRa radio with no internet connection. [Bloom](https://github.com/nostrnative/bloom) ships [v0.1.0](#bloom-v010-ships-self-hosted-blossom-server-and-relay) as a desktop app bundling a full [Blossom](/en/topics/blossom/) media server and Nostr relay. [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) debuts with [v0.1.0](#wavefunc-v010-and-v011-launch-nostr-internet-radio) as an internet radio directory and player built on Nostr. [Botburrow](https://github.com/marmot-protocol/botburrow) [starts development](#botburrow-begins-development-as-marmot-bot-platform) as a self-hosted bot platform for [Marmot](/en/topics/marmot/) encrypted group chats. [Snort](https://github.com/v0l/snort) ships [v0.5.0 through v0.5.3](#snort-ships-v050-through-v053-with-security-hardening-and-performance-overhaul) with a security audit, batched WASM verification, and a rewritten message system. [Primal Android](https://github.com/PrimalHQ/primal-android-app) [ships v3.0.21](#primal-android-ships-3021-and-redesigns-feed-layout) with a redesigned feed layout and unified main screen. Two NIP deep dives cover [NIP-29](/en/topics/nip-29/) (Relay-based Groups) and [NIP-90](/en/topics/nip-90/) (Data Vending Machines).

## Top Stories

### Amethyst merges desktop Tor, C secp256k1, WebRTC calls, and multi-wallet NWC

[Amethyst](https://github.com/vitorpamplona/amethyst), the Android client maintained by vitorpamplona, merged 29 PRs this week across cryptography, networking, calling, and wallet infrastructure.

[PR #2381](https://github.com/vitorpamplona/amethyst/pull/2381) is the largest change, adding desktop Tor support by embedding a kmp-tor daemon with a fail-closed design. If Tor is enabled, all relay connections route through the embedded Tor process, and the app refuses to connect if Tor fails to start. Privacy routing now has parity between the Android and desktop builds, backed by over 130 unit tests for the Tor integration.

[PR #2374](https://github.com/vitorpamplona/amethyst/pull/2374) adds a custom C secp256k1 implementation with JNI bindings for signature verification. The implementation uses GLV decomposition, wNAF (windowed Non-Adjacent Form) point encoding, and hardware-accelerated SHA-256 on both x86_64 and ARM64 architectures. The result is a 2-3x speedup on Schnorr signature verification compared to the previous pure Kotlin path. Additional PRs in the series ([PR #2188](https://github.com/vitorpamplona/amethyst/pull/2188), [PR #2195](https://github.com/vitorpamplona/amethyst/pull/2195), [PR #2204](https://github.com/vitorpamplona/amethyst/pull/2204)) add fused multiply-reduce operations, a dedicated Fe4 struct replacing LongArray for field element storage, and platform-specific intrinsics for an estimated 28% improvement on Android.

[PR #2202](https://github.com/vitorpamplona/amethyst/pull/2202) updates the pure Kotlin MLS implementation to comply with RFC 9420, adding reuse guard checks, additional authenticated data (AAD) in ciphertext operations, ciphertext sample derivation, commit processing fixes, and thread safety for [Marmot](/en/topics/marmot/) protocol integration. Building on [the Kotlin MLS work from last week](/en/newsletters/2026-04-08-newsletter/#amethyst-ships-arti-tor-merges-pure-kotlin-mls-and-marmot), this brings [Quartz](/en/topics/quartz/) closer to full MLS spec compliance.

A series of WebRTC PRs ([PR #2203](https://github.com/vitorpamplona/amethyst/pull/2203) through [PR #2211](https://github.com/vitorpamplona/amethyst/pull/2211)) adds a complete voice and video calling system for [NIP-AC](/en/topics/nip-ac/). The implementation covers ICE restart for dropped connections, runtime camera switching, network monitoring with automatic reconnection, configurable call settings (resolution, bitrate, TURN server selection), a foreground service fix for Android 14+ background restrictions, and thread safety across the call state machine.

[PR #1988](https://github.com/vitorpamplona/amethyst/pull/1988) adds multi-wallet [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect) support. Users can now connect multiple NWC wallets to a single account, view balance cards for each, pick a default wallet, and migrate from the legacy single-wallet configuration.

[PR #2189](https://github.com/vitorpamplona/amethyst/pull/2189) adds GIF-to-MP4 conversion with a quality slider, compressing a 3MB GIF down to approximately 159KB as MP4. The same week also brought AI tone suggestions in the post composer with automatic language detection and parallel precomputation of suggestions.

### nstrfy launches Nostr-native push notifications for Android

[nstrfy](https://github.com/vcavallo/nstrfy-android) launched on April 13 with three releases from [v1.0.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.0.0) through [v1.2.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.2.0). The app is a fork of ntfy-android with the HTTP transport replaced by Nostr. Instead of polling a server for push notifications, nstrfy subscribes to kind `7741` events on configurable relays and displays them as native Android notifications.

The notification model supports both plaintext and [NIP-44](/en/topics/nip-44/) encrypted payloads. When encryption is enabled, nstrfy uses [Amber](https://github.com/greenart7c3/Amber) for signing via [NIP-55](/en/topics/nip-55/) or a local nsec. Topic-based subscriptions let users configure per-topic sender allowlists with npub whitelisting, so only approved senders can trigger notifications for a given topic. The app imports relay lists from the user's profile using [NIP-65](/en/topics/nip-65/) and respects [NIP-40](/en/topics/nip-40/) event expiration. User search is powered by [Web of Trust](/en/topics/web-of-trust/) data from brainstorm.world.

A companion CLI tool, [nstrfy.sh](https://github.com/vcavallo/nstrfy.sh), lets users send notifications from the command line. The app is available on [Zapstore](https://zapstore.dev/apps/io.nstrfy.android).

### HAMSTR adds Reticulum for Nostr over LoRa mesh

[HAMSTR](https://github.com/LibertyFarmer/hamstr), the project that sends Nostr events and Lightning zaps over ham radio, merged [PR #10](https://github.com/LibertyFarmer/hamstr/pull/10) on April 12, adding [Reticulum](https://reticulum.network/) mesh networking as a transport backend. Reticulum is a cryptographic mesh protocol that runs over LoRa, HF, VHF/UHF radio, serial links, and TCP/IP. With this addition, HAMSTR can relay Nostr events across a mesh of RNode hardware devices with no internet infrastructure at all.

The existing AX.25 Packet Radio and VARA HF transports remain available, so operators can choose the radio link that fits their setup. HAMSTR's zero-knowledge server architecture means the relay never sees private keys, and its [NIP-57](/en/topics/nip-57/) zap compliance ensures that offline Lightning zaps appear correctly in clients like Amethyst and Primal. A setup guide for the Reticulum transport is included in [RETICULUM.MD](https://github.com/LibertyFarmer/hamstr/blob/master/RETICULUM.MD). The same week, [PR #11](https://github.com/LibertyFarmer/hamstr/pull/11) migrated the frontend to Svelte 5 and TailwindCSS v4.

## Shipping This Week

### Bloom v0.1.0 ships self-hosted Blossom server and relay

[Bloom](https://github.com/nostrnative/bloom) shipped its first release, [v0.1.0](https://github.com/nostrnative/bloom/releases/tag/v0.1.0), on April 9. Built with Tauri v2 (Rust backend) and React 19, Bloom bundles a full [Blossom](/en/topics/blossom/) protocol media server (BUD-00 through BUD-10) and a Nostr relay into a single desktop application that runs on macOS, Windows, and Linux, with Android and iOS builds planned. Users get sovereign file storage with SHA-256 content addressing, [NIP-94](/en/topics/nip-94/) file metadata support, and Blossom URI scheme (`blossom://`) resolution without managing server infrastructure. Sixteen platform-specific binary assets ship with the release.

### WaveFunc v0.1.0 and v0.1.1 launch Nostr internet radio

[WaveFunc](https://github.com/zeSchlausKwab/wavefunc) shipped [v0.1.0](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.0) and [v0.1.1](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.1) on April 13, launching as a Nostr-based internet radio directory and player. Custom event kinds define the data model: kind `31237` for radio station listings, kind `30078` for favorites lists, kind `1311` for live chat, and kind `1111` for station comments. A Khatru relay backend provides SQLite storage and Bluge full-text search supporting [NIP-50](/en/topics/nip-50/).

WaveFunc ships with a [NIP-60](/en/topics/nip-60/) Cashu wallet and nutzap support, migrated from NDK to applesauce-core. [v0.1.1](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.1) adds genre carousels, a Lightning donation popover, station management for authenticated users, and Zapstore listing. The Tauri v2 desktop build gained system tray integration, media key support, autostart, and deep linking. Builds are available for macOS, Windows, Linux, and Android at [wavefunc.live](https://wavefunc.live).

### Snort ships v0.5.0 through v0.5.3 with security hardening and performance overhaul

[Snort](https://github.com/v0l/snort), the React-based Nostr web client, shipped three releases from [v0.5.0](https://github.com/v0l/snort/releases/tag/v0.5.0) through [v0.5.3](https://github.com/v0l/snort/releases/tag/v0.5.3). The v0.5.0 release is the largest, delivering a comprehensive security audit with real Schnorr signature verification, hardened [NIP-46](/en/topics/nip-46/) protection against forged relay messages, improved PIN encryption, and removal of unverified [NIP-26](https://github.com/nostr-protocol/nips/blob/master/26.md) delegation trust. Performance improvements include batched WASM signature verification, lazy-loaded routes, a rewritten priority profile loader with batch loading and chunking, and worker-relay optimizations. The release also adds kind `7000` payment-required invoice display for [NIP-90](/en/topics/nip-90/) DVMs. [PR #620](https://github.com/v0l/snort/pull/620) reworked the messaging system for performance, persisting gift wraps in the worker relay and replacing O(n²) chat list computation with a single-pass Map-based approach.

### Primal Android ships 3.0.21 and redesigns feed layout

[Primal Android](https://github.com/PrimalHQ/primal-android-app) shipped [v3.0.21](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.21) with bug fixes for poll zap votes, wallet multi-account sharing, and auto-reconnect for the remote signer and wallet service. Seven merged PRs followed: [PR #1008](https://github.com/PrimalHQ/primal-android-app/pull/1008) unifies the main screen layout, [PR #1010](https://github.com/PrimalHQ/primal-android-app/pull/1010) implements a new feed card design with larger avatars and content indentation, [PR #1009](https://github.com/PrimalHQ/primal-android-app/pull/1009) adds video support and portrait layout to media feed cards, [PR #1012](https://github.com/PrimalHQ/primal-android-app/pull/1012) introduces a compact text field for quick replies, and [PR #1013](https://github.com/PrimalHQ/primal-android-app/pull/1013) redesigns the app bars.

### Nostria v3.1.19 through v3.1.21 add local AI image generation

[Nostria](https://github.com/nostria-app/nostria) shipped three releases from [v3.1.19](https://github.com/nostria-app/nostria/releases/tag/v3.1.19) through [v3.1.21](https://github.com/nostria-app/nostria/releases/tag/v3.1.21) with over 80 commits. The headline addition is local image generation using Janus Pro with WebGPU acceleration, so users can generate images on-device without an external API. The releases also add cloud image generation, multimodal chat, ONNX runtime support, an AI prompt library, and AI cache management. On the client side, the update brings a new dialog system, note editor overhaul, music embed improvements, and signer login flow changes. [Newsletter #17](/en/newsletters/2026-04-08-newsletter/#nostria-ships-native-mobile-app) covered the v3.1.18 native mobile release with local signer support.

### TubeStr v1.0.3 ships feed and studio updates

[TubeStr](https://github.com/Tubestr/tubestr-v2), a private family video sharing app built on Nostr, shipped [v1.0.3](https://github.com/Tubestr/tubestr-v2/releases/tag/v1.0.3) on April 13. The release adds feed and studio improvements. [PR #3](https://github.com/Tubestr/tubestr-v2/pull/3) revamps the onboarding screens and [PR #2](https://github.com/Tubestr/tubestr-v2/pull/2) fixes a video export error. The app uses NDK and MDK ([Marmot](/en/topics/marmot/) Development Kit) for encrypted media sharing between family members, with [Blossom](/en/topics/blossom/) integration planned for media storage. TubeStr is available on [Zapstore](https://zapstore.dev).

## In Development

### Botburrow begins development as Marmot bot platform

[Botburrow](https://github.com/marmot-protocol/botburrow) is a new project from the Marmot team, started on April 3. It is a self-hosted bot management platform where each bot gets its own Nostr identity, joins [Marmot](/en/topics/marmot/) MLS-encrypted group chats via Welcome messages, and sends and receives end-to-end encrypted messages. The dashboard, built with Rails 8.1, communicates with a single whitenoise-rs daemon (`wnd`) over a Unix socket.

Botburrow exposes a substantial scripting and operations layer: commands, triggers, and scheduled actions run custom Ruby code, scripts can inspect profiles, group membership, and pending invites through `wnd`, the dashboard includes a live chat view for messaging bots inside real groups, and each bot has its own file storage for configs, cached data, and generated output. A [Docker image](https://github.com/marmot-protocol/botburrow/commit/2ed012078eaab3c5b92dff16b87865c2e353bd80) with multi-arch builds targets zero-config self-hosting on Umbrel and Start9. A [trust model section](https://github.com/marmot-protocol/botburrow/commit/c8ef8c306af247560b1952878206d854cde3fe20) in the README documents the security boundaries.

### Nostr Archives adds trending feeds relay and entity resolution

[Nostr Archives](https://github.com/barrydeen/nostrarchives-api), the Nostr archival and analytics platform at [nostrarchives.com](https://nostrarchives.com), continued steady development across its [API](https://github.com/barrydeen/nostrarchives-api) (Rust) and [frontend](https://github.com/barrydeen/nostrarchives-frontend) (Next.js 16). On the API side, [PR #118](https://github.com/barrydeen/nostrarchives-api/pull/118) adds time-range filtering to the client leaderboard and [PR #117](https://github.com/barrydeen/nostrarchives-api/pull/117) adds engagement counters to reply events. On the frontend, [PR #85](https://github.com/barrydeen/nostrarchives-frontend/pull/85) resolves Nostr entities directly from URL paths (paste an npub or note ID into the URL and the site renders it), and [PR #86](https://github.com/barrydeen/nostrarchives-frontend/pull/86) adds an API documentation page. The platform runs four relay services: a NIP-50 search relay, a trending feeds relay (visible at `wss://feeds.nostrarchives.com`), a scheduler relay for future-dated events, and an indexer relay for kinds 0, 3, and 10002.

### Damus fixes favorites timeline

[Damus](https://github.com/damus-io/damus), the iOS client, merged [PR #3708](https://github.com/damus-io/damus/pull/3708) rewriting the `subscribe_to_favorites()` function with in-place filtering, deduplication rebuilding, and persisted tab selection.

### Nostur adds private zaps and custom emoji viewing

[Nostur](https://github.com/nostur-com/nostur-ios-public), the iOS client, pushed 10 commits this week adding private zap support, custom emoji viewing, an animated `.webp` rendering fix, and voice message audio format detection.

### Amber ships v6.0.1 through v6.0.3 with WebDAV backup and relay reconnection fixes

[Amber](https://github.com/greenart7c3/Amber), the Android [NIP-55](/en/topics/nip-55/) signer app, shipped three releases this week. [v6.0.1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.1) adds two new backup options (WebDAV and share to Google Drive), implements exponential backoff for relay reconnections, updates the Quartz library to 1.08.0, and fixes event validation for app update and profile events. [v6.0.2](https://github.com/greenart7c3/Amber/releases/tag/v6.0.2) adds an account index option when using seed words and fixes relay reconnection when the relay is offline at startup. [v6.0.3](https://github.com/greenart7c3/Amber/releases/tag/v6.0.3) adds an additional fix for empty request IDs when receiving intents.

### Plektos v0.6.0 redesigns with Ditto themes

[Plektos](https://github.com/derekross/plektos), the decentralized meetup and events platform built on [NIP-52](/en/topics/nip-52/) with interactive maps, shipped [v0.6.0](https://github.com/derekross/plektos/commit/7a691cdf089ceb7a8582dd5c0ee026830f2cdc77) and [v0.6.1](https://github.com/derekross/plektos/commit/3a6474ae380522d8ee1b3526423fcfc3328fd879) on April 14. The update adds Ditto-style community themes with custom background image uploads, avatar shape configuration, and a UI overhaul. [PR #6](https://github.com/derekross/plektos/pull/6) addresses a full code review covering security, architecture, and UX findings. Plektos uses Nostrify for protocol integration, [NIP-46](/en/topics/nip-46/) for remote login, and zaps for ticket payments. The Android build is available on Zapstore.

### Shadow adds Nostr OS API and Cashu wallet app

[Shadow](https://github.com/justinmoon/shadow), Justin Moon's app runtime platform, pushed over 30 commits in two days. [Commit 88cbda5](https://github.com/justinmoon/shadow/commit/88cbda5131814d2730a2d892029932136db005df) adds a Cashu wallet app running inside the Shadow runtime. [Commit 865c415](https://github.com/justinmoon/shadow/commit/865c415) adds a podcast player demo. The runtime exposes `Shadow.os.nostr` and `Shadow.os.audio` as first-class OS-level APIs, and the Pixel runtime lane runs a Wayland compositor on rooted Android devices with GPU compositing. [PR #1](https://github.com/justinmoon/shadow/pull/1) and [PR #2](https://github.com/justinmoon/shadow/pull/2) from contributor k0sti fix desktop Linux font loading and XDG state directory handling. No formal release yet.

### Lief fixes Amber login and adds Zapstore

[Lief](https://gitlab.com/chad.curtis/lief), a Nostr app for composing and sending long-form letters to other Nostr users, shipped build `v2026.04.12` on April 12. The update fixes an [Amber](https://github.com/greenart7c3/Amber) signer login issue on Android, simplifies the signer nudge flow, upgrades the nostrify dependency, and adds Zapstore integration.

### Espy overhauls color picker and fixes Amber login

[Espy](https://gitlab.com/chad.curtis/espy), a Nostr social app where users share "color moments," capturing 3-6 color palettes from real-life scenes as a form of pre-verbal visual communication, shipped build `v2026.04.12` on April 12. The update overhauls the color picker with a curved saturation arc replacing the grayscale toggle, fixes hue ring flicker bugs, and adds Easter egg characters (Alchemist and Astrologer). Compression reduced PNG assets by 703KB. The release also fixes an [Amber](https://github.com/greenart7c3/Amber) signer login issue, simplifies the signer nudge flow, upgrades the nostrify dependency, and adds Zapstore integration.

### Jumble adds per-feed kind filters and articles tab

[Jumble](https://github.com/CodyTseng/jumble), the Nostr client, pushed 13 commits this week adding per-feed kind filtering, an Articles tab, notification read status sync with a privacy-preserving option, an avatar hide mode, and an account switching race condition fix.

### Primal Web ships 8 version bumps

[Primal Web](https://github.com/PrimalHQ/primal-web-app) shipped versions 3.0.93 through 3.0.101 in one week with 21 commits. The work focused on live stream chat improvements, mention boundary fixes, bookmark pagination, duplicate like prevention, and relay proxy fixes.

## Protocol and Spec Work

### NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-34](/en/topics/nip-34/) (Git Stuff): Add `nostr://` clone URLs** ([PR #2312](https://github.com/nostr-protocol/nips/pull/2312)): [NIP-34](/en/topics/nip-34/) defines how to host git repositories on Nostr using kind `30617` repository announcements that list branches, tags, relay locations, and maintainer pubkeys. Until now, the spec lacked a formal URL scheme for referencing these repositories. This PR adds a `nostr://` clone URL format that works with `git-remote-nostr` helpers, so `git clone nostr://npub1.../relay.ngit.dev/ngit` resolves the npub (or [NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md) address), discovers the repository's relay locations, and fetches the repository data. Three URL patterns are defined: `nostr://<naddr>` for direct addressable event references, `nostr://<npub|nip05>/<identifier>` for human-readable repository references, and `nostr://<npub|nip05>/<relay-hint>/<identifier>` when the client needs a relay hint. Both the relay hint and identifier are percent-encoded per RFC 3986. The format is already implemented by Shakespeare and ngit's git-remote-nostr helper, and displayed by GitWorkshop.dev and NostrHub.io. The PR also tightens the `d` tag format for repository identifiers so that `nostr://` URLs produce valid URIs.

**Open PRs and Discussions:**

- **NIP-63a: Minimal Payment Gateway Descriptor** ([PR #2315](https://github.com/nostr-protocol/nips/pull/2315)): Proposes a new kind `10164` replaceable event that lets content creators declare payment gateways, pricing models, and subscription rules for accessing paid content. Today, payment-gated content on Nostr requires each client to implement its own payment flow, with no standard way for a creator to say "this content costs X sats via gateway Y." The proposed event would embed payment gateway descriptors directly in Nostr events, letting clients discover a creator's accepted payment methods, pricing tiers, and subscription options from a single replaceable event. This decouples payment presentation from specific providers, so a creator could accept Lightning, Cashu, or fiat gateways without each client needing custom integration for each payment method.

- **NIP-XX: Relay Self-Declaration Manifest and Retention Horizon** ([PR #2314](https://github.com/nostr-protocol/nips/pull/2314)): Proposes two wire protocol primitives for relay transparency. The first is kind `10100`, a gossipable replaceable event where relay operators declare their endpoints (clearnet, Tor, I2P), retention window, write policy, and supported NIPs. Unlike [NIP-11](/en/topics/nip-11/) relay information documents (HTTP-only, not discoverable through Nostr itself), kind `10100` manifests propagate through the Nostr event network like any other event, with TOFU key binding via the NIP-11 `pubkey` field to prevent spoofing. The second primitive is `HORIZON`, a new relay-to-client message `["HORIZON", <sub_id>, <earliest_timestamp>]` sent before `EOSE`. When a client's subscription time range extends past the relay's retention window, the relay replies with the earliest timestamp it holds, replacing silent dead-ends ("no results found") with explicit temporal boundaries ("I only have data from timestamp X onward"). The motivation is that NIP-11's `retention` field was removed in February 2026 as unused because HTTP-only delivery was a distribution failure. A reference implementation runs on nostr-rs-relay 0.9.0 with 90-day pruning.

- **NIP-TPLD: Transient Private Location Data** ([PR #2309](https://github.com/nostr-protocol/nips/pull/2309)): Proposes kind `20411` (ephemeral range) for sharing encrypted geolocation data with specific recipients. Centralized location-sharing services like Google Maps and Apple Find My require trusting a central authority with real-time movements. This NIP defines a privacy-first alternative where the event content contains a JSON map of recipient pubkeys to [NIP-44](/en/topics/nip-44/) encrypted payloads, each containing a geohash at a configurable precision level (from city-level at precision 5 to street-level at precision 8). Multiple recipients are handled in a single event with per-recipient encryption, so each person can only decrypt their own payload. A `ttl` tag sets the suggested time-to-live in seconds, and the ephemeral kind range (20000-20999) signals to relays that these events should not be stored indefinitely. The `p` tags allow clients to filter relevant events without decrypting content.

- **[NIP-5C](/en/topics/nip-5c/) (Scrolls): WASM programs update** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): Continues development of the WebAssembly program publishing and execution spec, which defines conventions for publishing and discovering WASM binaries as Nostr events. Scrolls are self-contained programs that clients can download from relays and execute in a sandboxed runtime, turning Nostr into a distribution network for executable code. The PR refines the event format and runtime interface. A [demo app](https://nprogram.netlify.app/) shows scrolls running in-browser, with example programs published as Nostr events that any client can fetch and execute. The concept extends [NIP-5A](/en/topics/nip-5a/) (static websites) from serving HTML pages to running interactive programs, all distributed through the same relay infrastructure.

- **[NIP-44](/en/topics/nip-44/) large payload support** ([PR #1907](https://github.com/nostr-protocol/nips/pull/1907)): Proposes extending [NIP-44](/en/topics/nip-44/) versioned encryption to handle payloads larger than the current 65,535-byte limit. The change is backwards-compatible: implementations that do not need large messages can ignore it entirely. The practical motivation is [NIP-46](/en/topics/nip-46/) remote signing of large kind `3` contact lists, where a user's follow list can exceed the encryption size limit when serialized as JSON. Without this change, remote signers cannot encrypt responses containing large contact lists, forcing workarounds or truncation.

- **[NIP-C7](/en/topics/nip-c7/): Restrict kind 9 to chat views** ([PR #2310](https://github.com/nostr-protocol/nips/pull/2310)): [NIP-C7](/en/topics/nip-c7/) defines kind `9` as a lightweight chat message, a short text note meant for real-time conversation in chat contexts like [NIP-29](/en/topics/nip-29/) group chats and [NIP-53](/en/topics/nip-53/) live activity streams. This PR adds a requirement that clients rendering "chat view" as a stream of ordered events MUST only fetch kind `9` events, preventing missing context when other content types (kind `1` notes, kind `30023` articles) are mixed into the chat timeline. Other content types can still be quoted within a kind `9` message following [NIP-18](/en/topics/nip-18/) reposts. The motivation comes from a community discussion about kind `9` messages appearing in general-purpose feeds where they lack context, since chat messages are typically short responses that only make sense within a conversation thread.

## NIP Deep Dive: NIP-29 (Relay-based Groups)

[NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md) defines a model for group messaging where the relay itself manages group membership and moderation. Groups live on a specific relay, identified by a random string ID, and the relay enforces who can write to the group. This is a different architecture from [Marmot](/en/topics/marmot/) (client-side MLS encryption) or [NIP-17](/en/topics/nip-17/) group chats (gift-wrapped DMs): in NIP-29, the relay is the authority, the messages are readable by the relay operator, and moderation happens at the relay level.

A group is identified by the format `<host>'<group-id>`, for example `groups.nostr.com'abcdef`. The special group ID `_` is reserved as a top-level group for relay-wide discussion. All user events sent to a group carry an `h` tag with the group ID:

```json
{
  "id": "a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744675200,
  "kind": 9,
  "tags": [
    ["h", "abcdef"],
    ["previous", "a1b2c3d4", "e5f67890", "12345678"]
  ],
  "content": "Has anyone tested the new relay config?",
  "sig": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4"
}
```

The `previous` tag is a tamper-detection mechanism. Clients include the first 8 hex characters (4 bytes) of recent events they have seen from the same relay in the last 50 messages. Relays reject events containing `previous` references to events not in their database, which prevents messages from being replayed to a forked copy of the group on another relay. This is not a full chain of custody, but it makes out-of-context rebroadcasting detectable.

Group membership is managed through a set of moderation event kinds in the `9000-9020` range. A user joins by publishing a kind `9021` join request, which the relay accepts or rejects based on its policy:

```json
{
  "id": "b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1",
  "pubkey": "f1a2b3c4d5e6f7890123456789abcdef0123456789abcdef1234567890abcdef",
  "created_at": 1744675200,
  "kind": 9021,
  "tags": [
    ["h", "abcdef"],
    ["code", "invite-xyz-123"]
  ],
  "content": "I'd like to join the dev discussion group.",
  "sig": "11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff"
}
```

The optional `code` tag ties to invite codes created by admins via kind `9009` events. A user leaves by publishing kind `9022`, and the relay automatically issues a kind `9001` removal in response. Admins can add users with roles (kind `9000`), remove users (kind `9001`), edit group metadata (kind `9002`), and delete events (kind `9005`). The roles system is flexible: roles are arbitrary labels, and what each role can do is relay policy, not protocol-defined. The relay publishes the group's configuration as addressable events: kind `39000` for metadata (name, description, picture, visibility settings), kind `39001` for the admin list, kind `39002` for the member list, and kind `39003` for the roles and their capabilities.

Groups can be public (anyone can read, only members can write), closed (only members can read and write), or fully open. The visibility and write-access settings are orthogonal and controlled by the `public`, `open`, `visible`, and `unrestricted` flags in the kind `9002` metadata edit event. A relay can host many groups simultaneously, each with independent membership and moderation.

The spec accepts any event kind inside a group, not just chat messages. Long-form articles ([NIP-23](/en/topics/nip-23/)), calendar events ([NIP-52](/en/topics/nip-52/)), live streams ([NIP-53](/en/topics/nip-53/)), and market listings can all carry an `h` tag and participate in a group context. This makes NIP-29 groups function like Discord servers or Slack workspaces where different content types coexist in the same namespace.

[Flotilla](https://gitea.coracle.social/coracle/flotilla) is the most actively developed NIP-29 client, with voice rooms, email login, and proof-of-work DMs added in [v1.7.0](/en/newsletters/2026-04-01-newsletter/#flotilla-v170-adds-voice-rooms-and-email-login). [Coracle](https://github.com/coracle-social/coracle) supports NIP-29 groups as well. On the relay side, [groups.fiatjaf.com](https://github.com/fiatjaf/relay29) is a reference implementation by fiatjaf. [Nostrord](https://github.com/Nostrord/nostrord), a Kotlin Multiplatform NIP-29 client funded by [OpenSats](/en/newsletters/2026-04-08-newsletter/#opensats-announces-sixteenth-wave-of-nostr-grants), is in early development with Discord-style moderation and threading.

The tradeoff against encrypted alternatives like [Marmot](/en/topics/marmot/) is explicit. NIP-29 groups are readable by the relay operator. There is no end-to-end encryption, no forward secrecy, and no post-compromise security. The relay is a trusted party for content integrity and membership enforcement. What you get in return is simplicity: no key material to manage, no state synchronization across devices, no MLS handshake negotiation. A relay operator spins up a group, users join, and messages flow. For public communities, dev channels, and open discussion spaces, the relay-trust model matches the use case. For private messaging where the relay should not read content, NIP-17 or Marmot are the appropriate choices.

## NIP Deep Dive: NIP-90 (Data Vending Machines)

[NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md) defines a protocol for on-demand computation over Nostr. A customer publishes a job request, service providers compete to fulfill it, and results are delivered as Nostr events. The spec describes this as "money in, data out," and the design treats Nostr as a marketplace for data processing where customers care about the output, not who produces it.

The protocol reserves kinds `5000-5999` for job requests, `6000-6999` for job results, and kind `7000` for job feedback. A result kind is always 1000 higher than its request kind: a kind `5001` request produces a kind `6001` result. Here is a job request asking for text summarization:

```json
{
  "id": "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744675200,
  "kind": 5001,
  "tags": [
    ["i", "https://example.com/article.txt", "url"],
    ["output", "text/plain"],
    ["relays", "wss://relay.damus.io", "wss://nos.lol"],
    ["bid", "5000"],
    ["param", "lang", "en"],
    ["param", "max_tokens", "280"]
  ],
  "content": "",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

The `i` tag specifies input data with a type marker. Four input types are defined: `url` (fetch and process the data at this URL), `event` (use a Nostr event as input), `job` (chain from the output of a previous job), and `text` (inline text). The `bid` tag sets a maximum payment in millisats. The `param` tag carries job-type-specific parameters, and the `output` tag specifies the expected response format.

A service provider picks up the request and publishes a result:

```json
{
  "id": "d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744675260,
  "kind": 6001,
  "tags": [
    ["request", "{\"id\":\"c3d4e5...\",\"kind\":5001,...}"],
    ["e", "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2", "wss://relay.damus.io"],
    ["i", "https://example.com/article.txt", "url"],
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876"],
    ["amount", "5000", "lnbc50n1pj..."]
  ],
  "content": "The article discusses three protocol changes proposed for the next quarter...",
  "sig": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210"
}
```

The result tags the original request event, includes the input for reference, addresses the customer's pubkey, and optionally includes a Lightning invoice in the `amount` tag. The customer can verify the result came from a specific service provider by checking the pubkey.

Job feedback (kind `7000`) provides status updates while a job is in progress. Service providers can emit feedback events with status values like `payment-required` (send a Lightning invoice before processing), `processing` (work is underway), `error` (something went wrong), or `success` (job complete). This gives customers real-time visibility into long-running jobs:

```json
{
  "id": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744675230,
  "kind": 7000,
  "tags": [
    ["status", "payment-required"],
    ["e", "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2", "wss://relay.damus.io"],
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876"],
    ["amount", "5000", "lnbc50n1pj..."]
  ],
  "content": "",
  "sig": "11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff"
}
```

Job chaining allows outputs to feed into subsequent jobs. A customer can set the input type to `job` and reference a previous job's event ID. The service provider for the downstream job waits for the upstream result, then processes it. This creates composable pipelines: transcribe audio (kind `5002`), then summarize the transcript (kind `5001`), then translate the summary (kind `5003`). Each step can be fulfilled by a different service provider.

For privacy, customers can encrypt the `i` and `param` tags using [NIP-04](/en/topics/nip-04/) encryption with the service provider's pubkey, placing the encrypted payload in the `content` field and adding an `encrypted` tag. This hides the input data and parameters from relays and other service providers, though it requires the customer to select a specific provider up front.

Specific job request types are defined in a [separate repository](https://github.com/nostr-protocol/data-vending-machines/tree/master/kinds). Current types include text generation (kind `5050`), summarization (kind `5001`), translation (kind `5002`), speech-to-text (kind `5003`), image generation (kind `5100`), and content recommendation (kind `5300`).

[Snort](https://github.com/v0l/snort) added kind `7000` payment-required invoice display in [Newsletter #17](/en/newsletters/2026-04-08-newsletter/#snort-ships-security-hardening-and-dvm-payment-invoices), rendering Lightning invoices directly in the feed when a DVM responds with a payment requirement. [noStrudel](https://github.com/hzrd149/nostrudel) has a DVM explorer for browsing available service providers. On the provider side, projects like [DVMDash](https://github.com/dtdannen/dvmdash) track DVM activity across the network, and several AI-focused services offer text generation, image creation, and content moderation through the NIP-90 protocol. The [NIP-89](/en/topics/nip-89/) (Recommended Application Handlers) spec complements NIP-90 by letting service providers publish their capabilities as discoverable Nostr events.

---

That's it for this week. Building something or have news to share? DM us on Nostr or find us at [nostrcompass.org](https://nostrcompass.org).
