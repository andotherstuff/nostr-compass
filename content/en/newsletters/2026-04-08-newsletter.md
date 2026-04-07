---
title: 'Nostr Compass #17'
date: 2026-04-08
publishDate: 2026-04-08
draft: false
type: newsletters
description: 'Amethyst ships Arti Tor and redesigned Shorts UI, Nostur adds video recording and private replies, Shosho launches Shows with OBS integration, Nymchat reverts Marmot for enhanced NIP-17 group chats, and Nostr VPN ships six releases.'
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** [Amethyst](https://github.com/vitorpamplona/amethyst) ships [v1.08.0](#amethyst-ships-arti-tor-merges-pure-kotlin-mls-and-marmot) with Arti Tor integration and a redesigned Shorts UI, while merging pure Kotlin implementations of [MLS](/en/topics/mls/) and [Marmot](/en/topics/marmot/) into its [Quartz](/en/topics/quartz/) library. [Nostur](https://github.com/nostur-com/nostur-ios-public) ships [v1.27.0](#nostur-v1270-adds-video-recording-and-private-replies) with video recording, animated GIF profiles, and private replies. [Shosho](https://github.com/r0d8lsh0p/shosho-releases) launches [v0.15.0](#shosho-v0150-launches-shows-and-vertical-video-carousel) with Shows (custom live stream info connected to OBS) and a TikTok-style vertical video carousel. [Nymchat](https://github.com/Spl0itable/NYM) [reverts Marmot and ships enhanced NIP-17 group chats](#nymchat-reverts-marmot-ships-enhanced-nip-17-group-chats) with rotating ephemeral keys. [Nostr VPN](https://github.com/mmalmi/nostr-vpn) ships [exit node support and Umbrel packaging](#nostr-vpn-ships-exit-node-support-and-umbrel-packaging) across six releases. [Amber](https://github.com/greenart7c3/Amber) jumps to [v6.0.0-pre1](#amber-v600-pre1-adds-per-connection-nip-46-signing-keys) with per-connection [NIP-46](/en/topics/nip-46/) signing keys and Zapstore in-app updates. [Notedeck](https://github.com/damus-io/notedeck) reaches [v0.10.0-beta](#notedeck-v0100-beta-ships-zapstore-self-update) with APK self-update via Zapstore, and [NIP-58](/en/topics/nip-58/) (Badges) gets a [kind migration](#nip-updates). Two NIP deep dives cover [NIP-17](/en/topics/nip-17/) (Private Direct Messages) and [NIP-46](/en/topics/nip-46/) (Nostr Remote Signing).

## Top Stories

### Amethyst ships Arti Tor, merges pure Kotlin MLS and Marmot

[Amethyst](https://github.com/vitorpamplona/amethyst), the Android client maintained by vitorpamplona, shipped four releases from [v1.07.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.3) through [v1.08.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.08.0) and merged a large batch of unreleased work into its [Quartz](/en/topics/quartz/) library (the shared Kotlin Multiplatform Nostr module). The headline release is v1.08.0 "Arti Tor," which migrates the app's Tor connectivity from the C-based Tor library to [Arti](https://gitlab.torproject.org/tpo/core/arti), the Tor Project's Rust implementation. The migration addresses random crashes that occurred under the previous C Tor bindings. Arti is the Tor Project's long-term replacement for the C codebase, written from scratch in Rust for memory safety and async I/O.

The v1.07.3 release redesigned the Shorts UI, replacing the paged design with edge-to-edge feeds for pictures, shorts, and long videos. The same release migrated badges to kind `10008` and bookmarks to kind `10003`, aligning with the [NIP-58](/en/topics/nip-58/) kind migration [merged this week](#nip-updates). v1.07.4 fixed a Nostr Wallet Connect secret handling issue, and v1.07.5 fixed an image upload crash.

On main but not yet in a tagged release, the team wrote a full Kotlin implementation of both [MLS](/en/topics/mls/) and the [Marmot](/en/topics/marmot/) protocol, replacing the need for native C/Rust library bindings. [PR #2147](https://github.com/vitorpamplona/amethyst/pull/2147) adds the core Marmot MLS group messaging layer, [PR #2149](https://github.com/vitorpamplona/amethyst/pull/2149) adds the group chat UI, [PR #2146](https://github.com/vitorpamplona/amethyst/pull/2146) adds inbound and outbound message processors with a subscription manager, [PR #2141](https://github.com/vitorpamplona/amethyst/pull/2141) adds MLS group state persistence and KeyPackage rotation management, [PR #2150](https://github.com/vitorpamplona/amethyst/pull/2150) adds a full MLS test suite with improved GroupInfo signing, and [PR #2158](https://github.com/vitorpamplona/amethyst/pull/2158) adds KeyPackage publication status tracking. [PR #2166](https://github.com/vitorpamplona/amethyst/pull/2166) adds a pure Kotlin secp256k1 implementation for Nostr cryptographic operations, replacing the native C library dependency. Combined with the Kotlin MLS implementation, [Quartz](/en/topics/quartz/) can run Nostr signing and Marmot group messaging without any native bindings, which opens the door to Kotlin Multiplatform targets including iOS.

The team is also building [NIP-AC](/en/topics/nip-ac/) (P2P Voice and Video Calls) support: [PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143) adds a full test suite for the NIP-AC call state machine, and [PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164) prevents stale call offers from retriggering after app restart.

### Nostur v1.27.0 adds video recording and private replies

[Nostur](https://github.com/nostur-com/nostur-ios-public), the iOS Nostr client, shipped [v1.27.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/v1.27.0) on April 2. The release adds in-app video recording with trim-before-upload, so users can capture short clips, cut them to length, and publish without leaving the client. Animated GIF support extends to profile and banner photos, with animated WebP rendering added as well. A new Shortcuts integration lets users send Nostr posts from Apple Shortcuts automations. The release also adds private replies and fixes DM compatibility issues that affected message delivery between Nostur and other clients.

### Shosho v0.15.0 launches Shows and vertical video carousel

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), the Nostr live streaming app, shipped [v0.15.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.0) and [v0.15.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.1) on April 7. The headline feature is Shows: streamers can set up custom show info before going live and connect their show to OBS or any external encoder. This separates the "what am I streaming" metadata from the act of going live, so streamers can prepare titles, descriptions, and products before they start broadcasting. The same release adds a TikTok-style vertical video carousel for swiping through lives, clips, and replays in a full-screen feed, and Quick Add for publishing video clips and adding products directly from a profile page. v0.15.1 fixes a bug where the keyboard was hiding the live stream chat input.

## Shipping This Week

### Notedeck v0.10.0-beta ships Zapstore self-update

[Notedeck](https://github.com/damus-io/notedeck), the desktop and mobile client from the Damus team, shipped [v0.10.0-beta.1](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.1) and [v0.10.0-beta.2](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.2) as test prereleases for APK self-update. [PR #1417](https://github.com/damus-io/notedeck/pull/1417) adds APK self-update via the Nostr/Zapstore updater on Android, building on the [Nostr-native update discovery work from Newsletter #14](/en/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr). The update flow discovers new releases through Nostr events published to relays, then downloads the APK from wherever the developer hosts it (GitHub releases, Blossom CDN, or other sources), verifies the SHA-256 hash against the signed Nostr event, and installs it. [PR #1438](https://github.com/damus-io/notedeck/pull/1438) fixes a welcome screen bug where Login and CreateAccount buttons immediately navigated back, and [PR #1424](https://github.com/damus-io/notedeck/pull/1424) fixes text overflow in the Agentium AI session view.

### Amber v6.0.0-pre1 adds per-connection NIP-46 signing keys

[Amber](https://github.com/greenart7c3/Amber), the [NIP-55](/en/topics/nip-55/) (Android Signer Application) signer app, shipped [v6.0.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.0-pre1) on April 4. The most important change is per-connection signing keys for the [NIP-46](/en/topics/nip-46/) (Nostr Remote Signing) bunker protocol. Instead of using a single keypair for all bunker connections, Amber now generates a distinct key for each connected client. If one client connection is compromised, the attacker cannot impersonate the signer to other clients.

[PR #377](https://github.com/greenart7c3/Amber/pull/377) adds in-app update checking and installation via Zapstore, joining [Notedeck](#notedeck-v0100-beta-ships-zapstore-self-update) in adopting Nostr-native app distribution. [PR #375](https://github.com/greenart7c3/Amber/pull/375) handles AndroidKeyStore failures gracefully by displaying a warning to users instead of crashing, and [PR #371](https://github.com/greenart7c3/Amber/pull/371) adds database cleanup with size limits and content truncation to prevent unbounded storage growth. The pre-release also carries the [NIP-42](/en/topics/nip-42/) relay auth whitelist and mnemonic recovery phrase login from the [v5.0.x cycle covered last week](/en/newsletters/2026-04-01-newsletter/#amber-v502-through-v504).

### Nostria ships native mobile app

[Nostria](https://github.com/nostria-app/nostria), the cross-platform Nostr client maintained by SondreB, released a native mobile app for Android with eight releases from [v3.1.11](https://github.com/nostria-app/nostria/releases/tag/v3.1.11) through [v3.1.18](https://github.com/nostria-app/nostria/releases/tag/v3.1.18). The most important new capability is native local signer support for signers such as [Amber](https://github.com/greenart7c3/Amber) and Aegis. [Desktop installers](https://www.nostria.app/download) for Linux, macOS, and Windows are also available. [PR #610](https://github.com/nostria-app/nostria/pull/610) reduces feed memory pressure with adaptive runtime limits and preview URL cleanup. v3.1.14 fixes integration with Brainstorm, a [Web of Trust](/en/topics/web-of-trust/) provider. v3.1.15 focuses on music improvements. The new Android app is available on [Zapstore](https://zapstore.dev/apps/app.nostria).

### diVine 1.0.8 ships resumable uploads and DMs

[diVine](https://github.com/divinevideo/divine-mobile), the short-form video client, shipped [1.0.8](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.8) with 87 merged PRs. Resumable uploads let creators pick up interrupted uploads chunk by chunk instead of restarting from scratch on a flaky connection. The release adds video quality and bitrate settings, double-tap to like, and DM improvements. [PR #2722](https://github.com/divinevideo/divine-mobile/pull/2722) adds a macOS camera plugin for desktop video capture, and [PR #2820](https://github.com/divinevideo/divine-mobile/pull/2820) migrates the notification system to a BLoC architecture with enrichment and grouping. The team also replaced AI-generated stickers and category art with OpenMoji SVGs ([PR #2844](https://github.com/divinevideo/divine-mobile/pull/2844), [PR #2842](https://github.com/divinevideo/divine-mobile/pull/2842)).

### Manent v1.3.0 adds sensitive note blurring and NIP-42 auth

[Manent](https://github.com/dtonon/manent), the private encrypted notes and file storage app, shipped [v1.3.0](https://github.com/dtonon/manent/releases/tag/v1.3.0) on April 2. Users can now mark notes as sensitive to blur them in the list view, keeping private content hidden during casual scrolling. The release also adds [NIP-42](/en/topics/nip-42/) (Authentication of Clients to Relays) support, letting Manent authenticate to relays that require it before accepting events. Manent stores all data encrypted on Nostr relays using the user's keypair, so NIP-42 support expands the set of relays it can use for storage.

### Wisp v0.17.0 through v0.17.3 add live stream zaps and wallet backup

[Wisp](https://github.com/barrydeen/wisp), the Android Nostr client, shipped six releases from [v0.16.2-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.2-beta) through [v0.17.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.17.3-beta) with 44 merged PRs. The v0.17.0 release adds wallet backup safety prompts and zap UX improvements. [v0.17.1](https://github.com/barrydeen/wisp/releases/tag/v0.17.1-beta) adds live stream chat visibility across platforms and live stream zap functionality. [PR #423](https://github.com/barrydeen/wisp/pull/423) adds auto-search profiles, a zap success animation, and user status improvements. [PR #426](https://github.com/barrydeen/wisp/pull/426) fixes an out-of-memory crash in `computeId` for events with large tag lists. The v0.16.x releases added emoji shortcode autocomplete, group chat UI improvements, and blocked user filtering across all notification paths.

### Mostro ships deep links, Nostr exchange rates, and a duplicate payment fix

[Mostro](https://github.com/MostroP2P/mostro), the peer-to-peer Bitcoin exchange built on Nostr, saw updates across both its server daemon and mobile client this week. On the server side, [PR #692](https://github.com/MostroP2P/mostro/pull/692) prevents stale order writes from causing duplicate payments, a bug that could result in a seller being paid twice for the same trade. [PR #693](https://github.com/MostroP2P/mostro/pull/693) uses targeted updates for dev_fee writes instead of full order overwrites.

[Mostro Mobile](https://github.com/MostroP2P/mobile), the Flutter client, shipped [v1.2.3](https://github.com/MostroP2P/mobile/releases/tag/v1.2.3) on April 3. The release handles deep links from different Mostro instances, so users can tap links that route to the correct exchange server. [PR #498](https://github.com/MostroP2P/mobile/pull/498) detects admin and dispute DMs in the background notification pipeline, and the app now fetches exchange rates from Nostr with an HTTP/cache fallback. [PR #560](https://github.com/MostroP2P/mobile/pull/560) fixes a relay connection blocking bug that prevented the app from reaching relays under certain network conditions.

### Unfiltered v1.0.12 adds hashtags and comments

[Unfiltered](https://github.com/dmcarrington/unfiltered), a Nostr client focused on image-forward content, shipped [v1.0.12](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.12). [PR #69](https://github.com/dmcarrington/unfiltered/pull/69) adds hashtag support and [PR #72](https://github.com/dmcarrington/unfiltered/pull/72) adds the ability to write and display comments on posts. [PR #71](https://github.com/dmcarrington/unfiltered/pull/71) fixes navigation issues with multiple images per post.

### Primal Android ships wallet multi-account sharing and remote signer auto-reconnect

[Primal](https://github.com/PrimalHQ/primal-android-app), the Android Nostr client, shipped a release on April 7. The update adds wallet multi-account sharing and overflow menu with wallet deletion in Dev Tools. The remote signer now auto-reconnects on connection drops, and the wallet service gained its own auto-reconnect logic. Fixes include poll zap votes no longer appearing as Top Zaps, empty poll option crash prevention, wallet balance hiding when no wallet exists, and WalletException type mapping to error codes in NWC responses.

### Titan v0.1.0 launches native nsite:// browser with Bitcoin name registration

[Titan](https://github.com/btcjt/titan), a native desktop browser for the Nostr web, shipped [v0.1.0](https://github.com/btcjt/titan/releases/tag/v0.1.0) on April 7. Titan resolves `nsite://` URLs by looking up human-readable names registered on Bitcoin, querying Nostr relays for the site's content events, and rendering pages fetched from [Blossom](/en/topics/blossom/) servers. The result is a web browsing experience with no DNS, no TLS certificates, and no hosting providers. Names are registered through a [web interface](https://npub1hmq6xuqnplk5lw0h3700cujmx5gymqn5wrn42u6432r6ntzumezqc3marw.nsite.lol/register) tied to Bitcoin transactions. The initial release ships as a macOS `.dmg` (ARM, with Rosetta 2 support for Intel) and includes Nix development environment support.

### Bikel v1.5.0 ships native foreground service for de-Googled phones

[Bikel](https://github.com/Mnpezz/bikel), a decentralized cycling tracker that turns rides into public infrastructure data using Nostr, shipped [v1.5.0](https://github.com/Mnpezz/bikel/releases/tag/v1.5.0) on April 4. The release migrates from GMS-dependent Expo TaskManager to a custom native foreground service, ensuring reliable background ride tracking on LineageOS, GrapheneOS, and other de-Googled Android variants. The Bikel Bot gained dual-pocket architecture with autonomous eCash collection via Cashu nutzaps. v1.4.3 and v1.4.2 fix background tracking sync for non-standard Android environments, and the app adds OSM bike rack map point toggles.

### Sprout adds NIP-01, NIP-23, and NIP-33 support

[Sprout](https://github.com/block/sprout), a communication platform by Block with a built-in Nostr relay, shipped [desktop/v0.1.0-rc7](https://github.com/block/sprout/releases/tag/desktop/v0.1.0-rc7) on April 6. This week the team added support for [NIP-23](/en/topics/nip-23/) (Long-form Content) kind `30023` articles, [NIP-33](/en/topics/nip-33/) parameterized replaceable events with `d`-tag keyed replacement, and [NIP-01](/en/topics/nip-01/)/[NIP-02](/en/topics/nip-02/) kind `1` text notes and kind `3` follow lists. The release also adds an adaptive IDE theme system with 54 themes, workflow and agent run history UX polish, and a members sidebar cleanup.

### mesh-llm v0.56.0 ships distributed config protocol

[mesh-llm](https://github.com/michaelneale/mesh-llm), a distributed LLM inference system that uses Nostr keypairs for node identity, shipped [v0.56.0](https://github.com/michaelneale/mesh-llm/releases/tag/v0.56.0) on April 7. The release adds a distributed config protocol with ownership semantics, asymmetric KV cache quantization (Q8_0 keys with Q4 values) for reduced memory usage, OS keychain storage for identity keystores, smooth chat streaming with message queuing, and fixes for fullscreen layout and KV cache splitting with flash attention.

### Nostr VPN ships exit node support and Umbrel packaging

[Nostr VPN](https://github.com/mmalmi/nostr-vpn), a peer-to-peer VPN that uses Nostr relays for signaling and WireGuard for encrypted tunnels, shipped six releases from [v0.3.0](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.0) through [v0.3.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.6) this week. The v0.3.x cycle adds exit node support on Windows and macOS, letting peers route internet traffic through other nodes in the network. Invite and alias propagation now sync over Nostr, so users can share network access without out-of-band coordination. The releases add Umbrel packaging for self-hosted deployment, NAT punch-through using remembered public endpoints, automatic stale exit node cleanup, and a published protocol specification. The project also stabilized macOS route handling with self-healing default routes and underlay repair, and added an Android build via Tauri. Builds are available for macOS (Apple Silicon and Intel), Linux (AppImage and .deb), Windows, and Android.

### Nymchat reverts Marmot, ships enhanced NIP-17 group chats

[Nymchat](https://github.com/Spl0itable/NYM), the MLS-capable chat client, shipped 14 releases from [v3.56.261](https://github.com/Spl0itable/NYM/releases/tag/3.56.261) through [v3.58.274](https://github.com/Spl0itable/NYM/releases/tag/v3.58.274). The most significant change is a protocol pivot: [v3.57.261](https://github.com/Spl0itable/NYM/releases/tag/v3.57.261) added Marmot MLS group chats, but [v3.58.268](https://github.com/Spl0itable/NYM/releases/tag/v3.58.268) reverted back to [NIP-17](/en/topics/nip-17/) because Marmot's multi-device support is not yet finished, which caused issues with group chat state synchronization across devices. v3.58.271 introduces enhanced NIP-17 group chats with rotating ephemeral keys for all messages, designed to prevent timing and correlation attacks. The week also brought a friend system with granular control over settings ([v3.58.262](https://github.com/Spl0itable/NYM/releases/tag/v3.58.262)), MLS group chat message sync in encrypted app settings, and multiple relay connectivity fixes.

### nak v0.19.5 adds Blossom multi-server and outbox publishing

[nak](https://github.com/fiatjaf/nak), fiatjaf's command-line Nostr toolkit, shipped [v0.19.5](https://github.com/fiatjaf/nak/releases/tag/v0.19.5). The `blossom` command now accepts multiple `--server` flags for uploading to several [Blossom](/en/topics/blossom/) servers in one call. A new `key` command expands partial keys by left-padding with zeroes. The `event` command gains an `--outbox` flag for publishing events through the outbox model, and `fetch` now exits with an error code when no event is returned.

## In Development

### White Noise adds thumbhash previews and push registration bridge

[White Noise](https://github.com/marmot-protocol/whitenoise), the private messenger built on the [Marmot](/en/topics/marmot/) protocol, merged five PRs. [PR #549](https://github.com/marmot-protocol/whitenoise/pull/549) replaces blurhash image previews with thumbhash, a newer algorithm that produces sharper placeholder images at a smaller payload size (typically under 30 bytes versus blurhash's ~50-100 bytes) while preserving the aspect ratio and color distribution of the original image. Blurhash is retained as a fallback for older content. [PR #548](https://github.com/marmot-protocol/whitenoise/pull/548) updates whitenoise-rs and adds the [MIP-05](/en/topics/mip-05/) push registration bridge, connecting the [push notification spec work from last week](/en/newsletters/2026-04-01-newsletter/#marmot-moves-keypackages-to-addressable-events-and-tightens-push-notifications) to the client. [PR #493](https://github.com/marmot-protocol/whitenoise/pull/493) adds cursor-based pagination for chat messages, replacing the previous loading strategy with a scroll-driven approach.

### Route96 adds dynamic label configuration and zero-egress cleanup

[Route96](https://github.com/v0l/route96), the [Blossom](/en/topics/blossom/) media server by v0l, merged three PRs. [PR #80](https://github.com/v0l/route96/pull/80) adds dynamic label model configuration via the admin API, letting operators swap content classification models without restarting the server. [PR #82](https://github.com/v0l/route96/pull/82) adds label configuration fields to the admin UI. [PR #79](https://github.com/v0l/route96/pull/79) adds a zero-egress file cleanup policy that automatically removes files that have never been downloaded, keeping storage costs down for operators.

### Snort ships security hardening and DVM payment invoices

[Snort](https://github.com/v0l/snort), the web client, shipped two releases this week with a comprehensive security audit. Fixes include Schnorr signature verification, [NIP-46](/en/topics/nip-46/) relay message forgery protection (preventing attackers from injecting signing requests through compromised relays), PIN encryption improvements, and removal of NIP-26 delegation trust. Performance gains come from batched Schnorr verification in WASM, lazy-loaded routes, pre-compiled translations, and elimination of double verification per event. [PR #618](https://github.com/v0l/snort/pull/618) adds [NIP-90](/en/topics/nip-90/) (Data Vending Machine) kind `7000` payment-required invoice display, so when a DVM responds with a payment requirement, Snort renders the Lightning invoice directly in the feed.

### Damus improves LMDB compaction

[Damus](https://github.com/damus-io/damus), the iOS client, merged [PR #3719](https://github.com/damus-io/damus/pull/3719) adding automatic LMDB compaction on a schedule, preventing the local database from growing unbounded over time. [PR #3663](https://github.com/damus-io/damus/pull/3663) improves the BlurOverlayView to look protective instead of broken.

### Captain's Log adds tag indexing and note sync

[Captain's Log](https://github.com/nodetec/captains-log) (Comet), the Nostr-native long-form writing tool from Nodetec, merged four PRs this week. [PR #156](https://github.com/nodetec/captains-log/pull/156) adds tag indexing and sync support across notes, [PR #157](https://github.com/nodetec/captains-log/pull/157) refactors note sync and tag handling, and [PR #159](https://github.com/nodetec/captains-log/pull/159) fixes trashed note sync so deleted notes stay deleted across devices.


### Relatr v0.2.x redesigns plugin system with Nostr-native validator marketplace

[Relatr](https://github.com/ContextVM/relatr), a [Web of Trust](/en/topics/web-of-trust/) scoring engine that computes trust rankings from social graph distance and configurable validators, shipped the v0.2.x family with a complete plugin system redesign. Validators are now written in Elo, a portable functional expression language forked to support multi-step host-orchestrated capabilities (Nostr queries, social graph lookups, NIP-05 resolution). Plugins are published as kind `765` Nostr events, making distribution native to the relay network. A new [plugin marketplace](https://relatr.net) lets operators discover, install, and weight validators from the browser, with a CLI (`relo`) for local authoring and publishing. The architecture is sandboxed: plugins can only invoke capabilities the host explicitly provides, so a malicious validator cannot escape its defined scope. Relatr instances can now be managed from the website, with full visibility into which plugins compose the scoring algorithm and their individual weights.

### Shopstr improves mobile navigation and access control

[Shopstr](https://github.com/shopstr-eng/shopstr), the Nostr-native marketplace for buying and selling with Bitcoin, pushed 158 commits across its main app and the [Milk Market](https://github.com/shopstr-eng/milk-market) companion project this week. Fixes include mobile community layout improvements, menu close-on-navigation behavior, and dropdown auto-close. Protected routes can no longer be accessed via direct URL without signing in, and the slug matching logic now handles multiple exact matches correctly.

### Pollerama adds notifications, movie search, and rating UI

[Pollerama](https://github.com/formstr-hq/nostr-polls), a polling, survey, and social rating app built on Nostr, added thread notifications, a movie search feature, and a rating UI overhaul. The release also fixes feed loading issues and bumps dependency versions.

### Purser builds Nostr-native payment daemon with Marmot encryption

[Purser](https://github.com/EthnTuttle/purser), a Nostr-native payment daemon designed as a Zaprite replacement, merged nine PRs this week building out its core architecture. The project uses [Marmot](/en/topics/marmot/) MLS via MDK for encrypted merchant-customer messaging, with Strike and Square as payment providers. This week landed config and catalog loading, message schema validation, the MDK communication layer, Strike and Square provider implementations, a polling engine, anti-spam rate limiting, pending payment persistence, and the order processing pipeline. All 99 tests now exercise actual mdk-core MLS operations after the team removed mock MLS in favor of real encryption in local mode.

### Vector refactors DM attachments and adds profile editing

[Vector](https://github.com/VectorPrivacy/Vector), the privacy-focused Nostr messenger built with Tauri, merged [PR #55](https://github.com/VectorPrivacy/Vector/pull/55) refactoring the frontend. DM attachment decryption and saving moved to the vector-core library, and the app now supports profile editing. The upload cancel flag is properly wired through TauriSendCallback, and unused attachment preview callbacks were cleaned up.

## Protocol and Spec Work

### NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-58](/en/topics/nip-58/) (Badges): Profile Badges move to kind 10008, Badge Sets to kind 30008** ([PR #2276](https://github.com/nostr-protocol/nips/pull/2276)): Migrates Profile Badges from kind `30008` to kind `10008` (a replaceable event, one per pubkey) and introduces kind `30008` for Badge Sets. Previously, Profile Badges used the same kind (`30008`) as Badge definitions, making them parameterized replaceable events keyed by a `d` tag. The new kind `10008` is a simple replaceable event: one per pubkey, no `d` tag needed. Clients query a single replaceable event per user instead of scanning parameterized replaceable events. Amethyst v1.07.3 already ships with this migration.

- **[NIP-34](/en/topics/nip-34/) (Git Stuff): Add git-related follow lists** ([PR #2130](https://github.com/nostr-protocol/nips/pull/2130)): Adds follow list conventions for NIP-34 repository and issue tracking. Users publish kind `30000` follow sets with `d` tags like `git-repos` or `git-issues` containing `a` tag references to repositories (kind `30617`) they want to track. Clients can subscribe to these follow sets to show repository activity in a user's feed, similar to how kind `3` contact lists work for pubkeys.

**Open PRs and Discussions:**

- **NIP-AC: P2P Voice and Video Calls over WebRTC** ([PR #2301](https://github.com/nostr-protocol/nips/pull/2301)): Expands the original NIP-100 (implemented by 0xChat) with three changes: migration to [NIP-44](/en/topics/nip-44/) encryption wrapped in [NIP-59](/en/topics/nip-59/) gift wraps to eliminate metadata leaks, a specified WebRTC workflow for voice and video call setup (offer, answer, ICE candidates), and a mesh group call model where each peer establishes a direct WebRTC connection to every other peer. The spec is not backwards-compatible with NIP-100. Amethyst is already building against it, with a call state machine test suite ([PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143)) and stale call offer handling ([PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164)) landing this week.

- **[NIP-340](/en/topics/nip-340/) (FROST Quorum)** ([PR #2299](https://github.com/nostr-protocol/nips/pull/2299)): Proposes conventions for [FROST](/en/topics/frost/) (Flexible Round-Optimized Schnorr Threshold) threshold signing on Nostr. FROST lets a group of signers collectively control a Nostr identity where any t-of-n members can sign events without reconstructing the full private key. The NIP defines how to coordinate signing rounds, distribute key shares, and publish threshold-signed events, building on the Igloo signer work from the [FROSTR project](/en/newsletters/2026-04-01-newsletter/#igloo-signer-11).

- **[NIP-5D](/en/topics/nip-5d/) (Nostr Web Applets)** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): Defines a `postMessage` protocol for sandboxed web applications ("napplets") running in iframes to communicate with a hosting application ("shell"). The shell provides the napplet with Nostr signing, relay access, and user context through a structured message API, while the iframe sandbox prevents direct key access. This extends the static website hosting model from [NIP-5A](/en/topics/nip-5a/) toward interactive applications that can read and write Nostr events. The NIP is under active development with a working runtime implementation.

- **[NIP-5C](/en/topics/nip-5c/) (Scrolls)** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): Renamed from the earlier NIP-A5 proposal. Defines conventions for publishing and discovering WebAssembly programs on Nostr. WASM binaries are stored as Nostr events, and clients can download and execute them in a sandboxed runtime. A [demo app](https://nprogram.netlify.app/) shows scrolls running in-browser, with example programs published as Nostr events that any client can fetch and execute.

- **[NIP-85](/en/topics/nip-85/) (Trusted Assertions): Clarifications** ([PR #2304](https://github.com/nostr-protocol/nips/pull/2304)): Tightens the specification language around multiple keys and relays per service provider, clarifying how clients should handle assertions from providers that operate across several pubkeys or relay endpoints.

- **[NIP-24](/en/topics/nip-24/) (Extra Metadata Fields): published_at for replaceable events** ([PR #2300](https://github.com/nostr-protocol/nips/pull/2300)): Generalizes the `published_at` tag from [NIP-23](/en/topics/nip-23/) (Long-form Content) to all replaceable and addressable events. The tag is display-only: if `published_at` equals `created_at`, clients show the event as "created" at that time; if they differ (because the event was updated), clients can show "updated" instead. This lets kind `0` profiles display "joined at" dates and other replaceable events preserve their original publication timestamp across updates. A complementary [NIP-51](/en/topics/nip-51/) proposal ([PR #2302](https://github.com/nostr-protocol/nips/pull/2302)) adds the same tag to list events.

- **[NIP-59](/en/topics/nip-59/) (Gift Wrap): Ephemeral gift wrap kind** ([PR #2245](https://github.com/nostr-protocol/nips/pull/2245)): Adds kind `21059` as an ephemeral counterpart to the existing kind `1059` gift wrap. Ephemeral events (kinds `20000`-`29999`) follow [NIP-01](/en/topics/nip-01/) semantics: relays are not expected to store them and may discard them after delivery. This lets applications send gift-wrapped messages that disappear from relays once delivered, reducing storage requirements for high-volume messaging while keeping the same three-layer encryption model as regular [NIP-17](/en/topics/nip-17/) DMs.

### OpenSats announces sixteenth wave of Nostr grants

[OpenSats](https://opensats.org) announced its [sixteenth wave of Nostr grants](https://opensats.org/blog/sixteenth-wave-of-nostr-grants) on April 8, funding four first-time grants and one renewal. [Amethyst Desktop](https://github.com/vitorpamplona/amethyst/tree/main/desktopApp) receives funding for contributor Robert Nagy to build a standalone desktop app on top of the [Quartz](/en/topics/quartz/) and Commons modules, bringing the Android client's feature set to mouse-driven interfaces with persistent relay connections. [Nostr Mail](https://github.com/nogringo/nostr-mail) receives funding to build a full email system on Nostr using kind `1301` events wrapped in [NIP-59](/en/topics/nip-59/) gift wraps, with a Flutter client and SMTP bridge servers for Gmail/Outlook compatibility. [Nostrord](https://github.com/Nostrord/nostrord) receives funding for a Kotlin Multiplatform [NIP-29](/en/topics/nip-29/) relay-based group client with Discord-like group messaging, moderation, and threads. [Nurunuru](https://github.com/tami1A84/null--nostr) receives funding to build a native iOS version of the Japanese-focused Nostr client modeled on LINE's familiar interface, with passkey-based biometric login for onboarding. HAMSTR received a grant renewal (first funded in the [eleventh wave](https://opensats.org/blog/eleventh-wave-of-nostr-grants#hamstr)).

## NIP Deep Dive: NIP-17 (Private Direct Messages)

[NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md) defines the current standard for private direct messages on Nostr. It replaces the older [NIP-04](/en/topics/nip-04/) (Encrypted Direct Messages) scheme, which leaked metadata (sender, receiver, and timestamps were all visible on relays) and used a weaker encryption construction. NIP-17 combines [NIP-44](/en/topics/nip-44/) (Encrypted Payloads) for encryption with [NIP-59](/en/topics/nip-59/) (Gift Wrap) for metadata protection, creating a three-layer system where relays cannot see who is talking to whom.

The protocol uses three event kinds stacked inside each other. The innermost layer is the actual message, an unsigned kind `14` event:

```json
{
  "id": "a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744108800,
  "kind": 14,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef", "wss://inbox.example.com"],
    ["subject", "Project update"]
  ],
  "content": "The new relay config is deployed. Let me know if you see any issues.",
  "sig": ""
}
```

The kind `14` event is deliberately unsigned (empty `sig`). The spec describes this as providing deniability, but in practice the protection is limited. The kind `13` seal that wraps the rumor is signed by the sender's real key. A recipient can show the signed seal to a third party, proving the sender communicated with them, even without revealing the message content. With zero-knowledge proofs, a recipient can prove the exact message content without revealing their own private key. The unsigned rumor is like an unsigned letter in a signed envelope: the envelope's signature links the sender to the contents. True deniability would require symmetric authentication (like Signal's HMACs), which is incompatible with Nostr's decentralized relay model where messages must be self-authenticating. NIP-17's real strengths are metadata privacy and content secrecy, not deniability.

This unsigned message gets wrapped in a kind `13` seal, which is signed by the actual sender and encrypted with [NIP-44](/en/topics/nip-44/) to the recipient:

```json
{
  "id": "b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744022400,
  "kind": 13,
  "tags": [],
  "content": "<nip44-encrypted kind 14 payload>",
  "sig": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4"
}
```

The seal has no tags, so even if decrypted it would not reveal the recipient. The seal is signed by the sender's real key, which lets the recipient authenticate the message by checking that the seal's `pubkey` matches the inner kind `14`'s `pubkey`.

The seal then gets wrapped in a kind `1059` gift wrap, signed by a random throwaway key and addressed to the recipient:

```json
{
  "id": "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744065600,
  "kind": 1059,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef"]
  ],
  "content": "<nip44-encrypted kind 13 payload>",
  "sig": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210"
}
```

The gift wrap's `pubkey` is a random key generated just for this message, and the `created_at` is randomized up to two days in the past. This is the outermost layer that relays actually see: a message from an unknown pubkey addressed to the recipient, with a timestamp that does not reflect when the message was actually sent. The randomized timestamp protects against after-the-fact analysis of stored events, but an adversary actively connected to relays can still observe when the gift wrap first appeared, so this defense is limited to passive observers who query relay data later. Because the pubkey is random and the timestamp is fake, relays cannot determine the real sender. To read the message, the recipient decrypts the gift wrap using their own key and the random pubkey, finds the seal inside, decrypts the seal using their own key and the sender's pubkey from the seal, and finds the kind `14` message inside.

NIP-17 does not provide forward secrecy. All messages are encrypted using the static Nostr keypair (via NIP-44's key derivation from the sender and recipient's keys). If a private key is compromised, every past and future message encrypted to that key can be decrypted. This is a deliberate tradeoff: because encryption depends only on the nsec, a user who backs up their nsec can recover their entire message history from any relay that still stores the gift wraps. Protocols like MLS (used by [Marmot](/en/topics/marmot/)) provide forward secrecy through rotating key material, but at the cost of requiring state synchronization and making historical message recovery impossible after key rotation.

NIP-17 also defines kind `15` for encrypted file messages, which adds `file-type`, `encryption-algorithm`, `decryption-key`, and `decryption-nonce` tags so the recipient can decrypt an attached file that was encrypted with AES-GCM before upload to a Blossom server. Kind `10050` is used to publish the user's preferred DM relay list, so senders know where to deliver gift wraps. The set of `pubkey` + `p` tags in a message defines a chat room; adding or removing a participant creates a new room with clean history.

Implementations cover most major clients. [nospeak](https://github.com/psic4t/nospeak) uses NIP-17 for all one-on-one messaging. [Flotilla](https://gitea.coracle.social/coracle/flotilla) uses NIP-17 for its proof-of-work DMs. [Amethyst](https://github.com/vitorpamplona/amethyst), [Primal](https://github.com/PrimalHQ/primal-android-app), [Nostur](https://github.com/nostur-com/nostur-ios-public), [Damus](https://github.com/damus-io/damus), [noStrudel](https://github.com/hzrd149/nostrudel), and [Coracle](https://github.com/coracle-social/coracle) all implement NIP-17 as their primary DM protocol. The spec also supports disappearing messages by setting an `expiration` tag in the gift wrap.

## NIP Deep Dive: NIP-46 (Nostr Remote Signing)

[NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) defines a protocol for separating the user's private key from the client application. Instead of pasting an nsec into a web app, the user runs a remote signer (also called a "bunker") that holds the private key and responds to signing requests over Nostr relays. The client never sees the private key. This reduces the attack surface: a compromised client can request signatures but cannot extract the key itself.

The protocol uses kind `24133` for both requests and responses, encrypted with [NIP-44](/en/topics/nip-44/) (Encrypted Payloads). A client generates a disposable `client-keypair` for the session and communicates with the remote signer through NIP-44 encrypted messages tagged with each other's pubkeys. Here is a signing request from a client to a remote signer:

```json
{
  "id": "aa11bb22cc33dd44ee55ff6677889900aabbccdd11223344556677889900aabb",
  "pubkey": "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86",
  "created_at": 1744108800,
  "kind": 24133,
  "tags": [
    ["p", "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52"]
  ],
  "content": "<nip44-encrypted JSON-RPC request>",
  "sig": "1122334455667788990011223344556677889900aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff0011223344556677"
}
```

The encrypted `content` contains a JSON-RPC-like structure:

```json
{
  "id": "random-request-id-1",
  "method": "sign_event",
  "params": ["{\"kind\":1,\"content\":\"Hello from remote signing\",\"tags\":[],\"created_at\":1744108800}"]
}
```

The remote signer decrypts the request, presents it to the user for approval (or auto-approves based on configured permissions), signs the event with the user's private key, and returns the signed event in a response:

```json
{
  "id": "bb22cc33dd44ee55ff6677889900aabb11223344556677889900aabbccddeeff",
  "pubkey": "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52",
  "created_at": 1744108801,
  "kind": 24133,
  "tags": [
    ["p", "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86"]
  ],
  "content": "<nip44-encrypted JSON-RPC response>",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

Connections can be initiated from either side. A remote signer provides a `bunker://` URL containing its pubkey and relay information. A client provides a `nostrconnect://` URL with its client pubkey, relays, and a secret for connection verification. The `secret` parameter prevents connection spoofing: only the party that received the URL out-of-band can complete the handshake.

Eight methods are defined: `connect` for establishing the session, `sign_event` for signing events, `get_public_key` for learning the user's pubkey, `ping` for keepalive, `nip04_encrypt`/`nip04_decrypt` for legacy encryption, `nip44_encrypt`/`nip44_decrypt` for current encryption, and `switch_relays` for relay management. Relay migration is handled by the remote signer, which can move the connection to new relays over time without breaking the session.

Clients request specific capabilities at connection time through a permission system. A permission string like `nip44_encrypt,sign_event:1,sign_event:14` requests NIP-44 encryption access and signing access for kind `1` and kind `14` events only. The remote signer can accept, reject, or modify these permissions. This means a web client for reading and posting notes might only get `sign_event:1` permission, while a DM client might also get `sign_event:14` and `nip44_encrypt` permissions.

[Amber](https://github.com/greenart7c3/Amber) implements NIP-46 on Android, and its [v6.0.0-pre1](#amber-v600-pre1-adds-per-connection-nip-46-signing-keys) this week adds per-connection signing keys for isolation between clients. [nsec.app](https://github.com/nicktee/nsecapp) (formerly Nostr Connect) provides a web-based bunker. [nostr-tools](https://github.com/nbd-wtf/nostr-tools) includes `BunkerSigner` for JavaScript clients, and [last week's PR #530](/en/newsletters/2026-04-01-newsletter/#nostr-tools-adds-bunker-relay-control-and-fixes-nip-47-multi-relay-parsing) added `skipSwitchRelays` for manual relay management. The protocol also supports auth challenges: when a remote signer needs additional authentication (password, biometric, or hardware token), it responds with an `auth_url` that the client opens in a browser for the user to complete.

---

That's it for this week. Building something or have news to share? DM us on Nostr or find us at [nostrcompass.org](https://nostrcompass.org).
