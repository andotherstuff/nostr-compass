---
title: 'Nostr Compass #16'
date: 2026-04-01
publishDate: 2026-04-01
draft: false
type: newsletters
description: 'Amethyst ships pinned notes and relay management, NIP-5A merges to bring static websites to Nostr, Flotilla adds voice rooms and email login, Nymchat adopts Marmot for group chats, and nospeak launches 1.0.'
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** [Amethyst](https://github.com/vitorpamplona/amethyst) ships [v1.07.0](#amethyst-ships-pinned-notes-relay-management-and-request-to-vanish) with pinned notes, relay management via [NIP-86](/en/topics/nip-86/), and [NIP-62](/en/topics/nip-62/) Request to Vanish support. [NIP-5A](#nip-5a-merges-bringing-static-websites-to-nostr) (Static Websites) merges into the NIPs repository, defining how to host websites under Nostr keypairs using [Blossom](/en/topics/blossom/) storage. [Flotilla](https://gitea.coracle.social/coracle/flotilla) ships [v1.7.0](#flotilla-v170-adds-voice-rooms-and-email-login) with voice rooms, email/password login, and proof-of-work DMs. [White Noise](https://github.com/marmot-protocol/whitenoise) fixes relay churn in [v2026.3.23](#white-noise-fixes-relay-churn-and-expands-client-controls), [nospeak](https://github.com/psic4t/nospeak) launches its [1.0.0](#nospeak-launches-as-a-10-private-messenger) as a no-signup encrypted messenger. [Nymchat](https://github.com/Spl0itable/NYM) [adopts Marmot](#nymchat-ships-marmot-powered-group-chats) for MLS-encrypted group chats with NIP-17 fallback. [Calendar by Form*](https://github.com/formstr-hq/nostr-calendar) reaches [v1.0.0](#calendar-by-form-v100) with private calendar lists and ICS import, [Amber](https://github.com/greenart7c3/Amber) adds [mnemonic recovery and NIP-42 relay auth whitelisting](#amber-v502-through-v504), and the [Marmot spec](#marmot-moves-keypackages-to-addressable-events-and-tightens-push-notifications) moves KeyPackages to addressable events while tightening MIP-05 push notification formatting.

## News

### Amethyst ships pinned notes, relay management, and Request to Vanish

[Amethyst](https://github.com/vitorpamplona/amethyst), the Android client maintained by vitorpamplona, shipped six releases in three days, from [v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) through [v1.07.5](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.5). The headline feature set spans six protocol surfaces: pinned notes, a dedicated polls feed screen, [NIP-62](/en/topics/nip-62/) (Request to Vanish) support for requesting full event deletion from relays, [NIP-86](/en/topics/nip-86/) (Relay Management API) from within the client, [NIP-66](/en/topics/nip-66/) (Relay Discovery and Liveness Monitoring) assessments in the relay info screen, and [NIP-43](/en/topics/nip-43/) (Relay Access Metadata and Requests) member information display.

[NIP-86](/en/topics/nip-86/) defines a JSON-RPC interface for relay operators, letting clients send administrative commands such as banning pubkeys, allowing pubkeys, and listing banned users over a standardized API. Amethyst now exposes this directly in its relay management UI, so users running their own relays can administer them from the same client they use for posting. [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) replaces the old hex-input dialog for ban and allow pubkeys with an interactive user search dialog.

v1.07.2 added GIF keyboard uploads and fixed a signing regression where Amber rejection responses were being misread because older Amber versions returned an empty string for the `rejected` field ([PR #2042](https://github.com/vitorpamplona/amethyst/pull/2042)). v1.07.5 fixes an image uploading crash. The [v1.06.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.2) and [v1.06.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.3) releases earlier in the week added a poll type selector for single vs. multiple choice polls, drag-to-seek on video progress bars, and anonymous posting improvements.

### NIP-5A merges, bringing static websites to Nostr

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md) (Static Websites) merged via [PR #1538](https://github.com/nostr-protocol/nips/pull/1538), defining how to host static websites under Nostr keypairs. The spec uses two event kinds: kind `15128` for a root site, one per pubkey, and kind `35128` for named sites identified by a `d` tag. Each manifest maps URL paths to SHA256 hashes, with optional `server` tags pointing to [Blossom](/en/topics/blossom/) storage hosts where the actual files live.

The hosting model works like this: a site author builds a static site, uploads the files to one or more Blossom servers, then publishes a signed manifest event that maps paths to content hashes. A host server receives web requests, resolves the author's pubkey from the subdomain, fetches the manifest from the author's [NIP-65](/en/topics/nip-65/) relay list, and serves files by downloading the matching blobs from Blossom. The site stays under the author's control because only that key can sign an updated manifest. The host server is replaceable because any server that understands NIP-5A can serve the same site from the same manifest.

The spec builds on infrastructure that already exists. [nsite](https://github.com/lez/nsite), the NIP-5A reference host implementation built by lez, and [nsite-manager](https://github.com/hzrd149/nsite-manager), hzrd149's management UI, were already running before the NIP merged. The merge makes the event kinds and URL resolution rules official, which gives second and third implementations a stable target.

### White Noise fixes relay churn and expands client controls

[White Noise](https://github.com/marmot-protocol/whitenoise), the private messenger built on the [Marmot](/en/topics/marmot/) protocol, shipped [v2026.3.23](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.3.23) on March 25. The main work is relay stability. Login no longer waits for every relay-list publish before moving on, because relay-list publishing now uses quorum logic and retries the rest in the background. One-off fetches and publishes use scoped ephemeral relay sessions instead of lingering in the long-lived pool, restored sessions recover their group refresh path after startup, and the app now exposes relay diagnostics and relay state inspection through [PR #495](https://github.com/marmot-protocol/whitenoise/pull/495) and [PR #502](https://github.com/marmot-protocol/whitenoise/pull/502).

The same release changes how conversations behave. [PR #468](https://github.com/marmot-protocol/whitenoise/pull/468) adds NIP-C7 reply threading with `q` tags and `nostr:nevent` references, [PR #471](https://github.com/marmot-protocol/whitenoise/pull/471) and [PR #512](https://github.com/marmot-protocol/whitenoise/pull/512) keep deleted messages visible as deleted placeholders instead of silently removing them, [PR #478](https://github.com/marmot-protocol/whitenoise/pull/478) adds an in-app bug report flow using [NIP-44](/en/topics/nip-44/) (Encrypted Payloads) anonymous reports, and [PR #486](https://github.com/marmot-protocol/whitenoise/pull/486) adds support chat directly in the client. User-facing message controls also landed in the same window: [PR #532](https://github.com/marmot-protocol/whitenoise/pull/532) archives chats, [PR #541](https://github.com/marmot-protocol/whitenoise/pull/541) adds mute and unmute with configurable durations, and [PR #535](https://github.com/marmot-protocol/whitenoise/pull/535) adds notification settings. [PR #539](https://github.com/marmot-protocol/whitenoise/pull/539) is preparatory push-registration work, wiring APNs registration on iOS and Play Services detection on Android so registration can be built on top of it. On the backend side, the [MDK](https://github.com/marmot-protocol/mdk) (Marmot Development Kit) added MIP-05 push notification primitives and a notification request builder ([PR #235](https://github.com/marmot-protocol/mdk/pull/235), [PR #238](https://github.com/marmot-protocol/mdk/pull/238)), while [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) added push notification registration persistence ([PR #688](https://github.com/marmot-protocol/whitenoise-rs/pull/688)), background task cancellation fixes ([PR #696](https://github.com/marmot-protocol/whitenoise-rs/pull/696)), and key package recovery on startup ([PR #693](https://github.com/marmot-protocol/whitenoise-rs/pull/693)).

### Nostr VPN reaches v0.3.0 with roster sync and invite v2

[Following last week's launch coverage](/en/newsletters/2026-03-25-newsletter/#nostr-vpn-launches-as-a-tailscale-alternative), [nostr-vpn](https://github.com/mmalmi/nostr-vpn), the peer-to-peer VPN that uses Nostr relays for signaling and WireGuard for encrypted tunnels, continued its rapid release pace, shipping releases through [v0.3.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.3). The version bump brings two breaking changes: the invite format moves to v2 (0.3.0 can still import v1 invites, but older builds cannot import v2 invites), and admin-signed roster sync was added to the signaling protocol. Mixed-version peers can still connect at the mesh layer, but older peers will not participate in roster synchronization.

The roster sync addition starts the move toward a managed network. An admin node can now push membership changes to all peers, so adding or removing a device from the mesh does not require each peer to manually update its configuration. The v0.2.x releases during the same week addressed specific deployment problems: [v0.2.22](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.22) through [v0.2.28](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.28) fixed Windows service management, added Android build scripts, and refined the LAN pairing flow.

### nospeak launches as a 1.0 private messenger

[nospeak](https://github.com/psic4t/nospeak), a private messenger built on Nostr, shipped its [1.0.0](https://github.com/psic4t/nospeak/releases/tag/v1.0.0) release on March 27. The project includes one-on-one and group conversations, contact management, and a self-hostable architecture. One-on-one chats use [NIP-17](/en/topics/nip-17/) (Private Direct Messages), which combines [NIP-59](/en/topics/nip-59/) (Gift Wrap) with [NIP-44](/en/topics/nip-44/) (Encrypted Payloads) to hide the sender from relays. For media, files are encrypted client-side with AES-256-GCM before upload to Blossom servers. The release also ships as a container image for self-hosting.

### Flotilla v1.7.0 adds voice rooms and email login

[Flotilla](https://gitea.coracle.social/coracle/flotilla), hodlbod's Discord-like [NIP-29](/en/topics/nip-29/) (Relay-based Groups) client built around the "relays as groups" model, shipped [v1.7.0](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.0) and [v1.7.1](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.1) on March 30 and 31. The headline feature is voice rooms, contributed by mplorentz. Users can now join voice calls within group channels, with a join dialog ([PR #109](https://gitea.coracle.social/coracle/flotilla/pulls/109)) that lets them select an audio input device and choose whether to join the voice call or just view the text chat. The dialog solves a UX problem from the previous iteration: entering a voice-enabled room previously forced microphone activation even when the user only wanted to read messages or check room settings.

The same release adds email and password login as an alternative to Nostr key-based auth, proof-of-work on DMs, DM editing, redesigned relay onboarding and settings, Blossom support detection via `supported_nips`, improved notification badges, Android push notification fallback, and file upload fixes on Android. v1.7.1 follows with a fix for pomade registration fallback when using an offline signer.

Hodlbod is also building [Caravel](https://gitea.coracle.social/coracle/caravel), a hosting manager and dashboard for zooid relays, which logged 40 commits this week in initial development.

### Nymchat ships Marmot-powered group chats

[Nymchat](https://github.com/Spl0itable/NYM) (also known as NYM, Nostr Ynstant Messenger), the ephemeral chat client bridged with Bitchat, announced that all new group chats now use the [Marmot](/en/topics/marmot/) protocol for MLS-encrypted messaging. The integration uses kinds `443`, `444`, and `445` for key packages, welcome messages, and group messages respectively, providing forward secrecy, post-compromise security, and zero metadata leakage. If a recipient cannot use MLS, Nymchat falls back to its earlier [NIP-17](/en/topics/nip-17/) (Private Direct Messages) group chat path, which is still end-to-end encrypted but lacks the ratchet-tree properties of MLS.

The v3.55 and v3.56 series this week focused on group chat edge cases: loading on new devices, leave behavior, notification routing, and unread badge counts. The same cycle also patched an XSS vulnerability from unescaped HTML and added keyword and phrase blocking extended to user nicknames. This makes Nymchat yet another Marmot client joining [White Noise](#white-noise-fixes-relay-churn-and-expands-client-controls) and [OpenChat](#openchat-v024-through-v030), broadening the set of apps that can exchange MLS-encrypted group messages over the same protocol.

## Releases

### Calendar by Form* v1.0.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), the decentralized calendar app built on [NIP-52](/en/topics/nip-52/) (Calendar Events), reached [v1.0.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.0.0) on March 29. The release adds private calendar lists using encrypted Nostr events (kind `32123`) with [NIP-44](/en/topics/nip-44/) (Encrypted Payloads) self-encryption, so users can organize events into private collections without exposing the grouping to relays. The same release adds ICS intent handling for importing calendar data from other applications and invitation requests for sharing events between users.

### Amber v5.0.2 through v5.0.4

[Amber](https://github.com/greenart7c3/Amber), the [NIP-55](/en/topics/nip-55/) (Android Signer Application) signer app, shipped three point releases: [v5.0.2](https://github.com/greenart7c3/Amber/releases/tag/v5.0.2), [v5.0.3](https://github.com/greenart7c3/Amber/releases/tag/v5.0.3), and [v5.0.4](https://github.com/greenart7c3/Amber/releases/tag/v5.0.4). The most visible addition is mnemonic recovery phrase login ([PR #358](https://github.com/greenart7c3/Amber/pull/358)), which lets users restore their signer from a BIP39 seed phrase instead of requiring the raw nsec or ncryptsec string. [PR #357](https://github.com/greenart7c3/Amber/pull/357) adds a [NIP-42](/en/topics/nip-42/) relay auth whitelist, so users can restrict which relays are allowed to request client authentication. [PR #353](https://github.com/greenart7c3/Amber/pull/353) adds encryption scope selection for decrypt permissions, letting users grant NIP-04-only or NIP-44-only decrypt access instead of a blanket permission. v5.0.4 fixes a bug where rejection was not respecting scoped encrypt and decrypt permissions and improves performance when receiving multiple bunker requests.

### Aegis v0.4.0

[Aegis](https://github.com/ZharlieW/Aegis), the cross-platform signer, shipped [v0.4.0](https://github.com/ZharlieW/Aegis/releases/tag/v0.4.0) on March 26. The release adds Full and Selective authorization modes in Settings and fixes multiple QR-scanning problems. Follow-up commits [d4f799f](https://github.com/ZharlieW/Aegis/commit/d4f799fe51dd82968d54f72ac77f2de29d0cfe6b), [3313af9](https://github.com/ZharlieW/Aegis/commit/3313af92e55e449ebc98fbd91a085bd444d716e7), [3b214e4](https://github.com/ZharlieW/Aegis/commit/3b214e4176f5dbe7f18690d0996e69dd151fe00f), and [e4f40b6](https://github.com/ZharlieW/Aegis/commit/e4f40b6f1f48c2dae1bb5e4246df26c26dba419e) continue the same work with batch select controls, reusable batch selection stats, set-all-groups selection APIs, and per-permission usage statistics on the app permissions page.

### Schemata v0.2.7 through v0.3.0

[Schemata](https://github.com/nostrability/schemata), the JSON Schema definitions for validating Nostr event kinds, shipped four releases from [v0.2.7](https://github.com/nostrability/schemata/releases/tag/v0.2.7) through [v0.3.0](https://github.com/nostrability/schemata/releases/tag/v0.3.0) with 21 merged PRs. The v0.3.0 release brings pattern consistency fixes across relay URLs, hex IDs, MIME types, and BOLT-11 strings ([PR #126](https://github.com/nostrability/schemata/pull/126)), centralized relay URL patterns ([PR #117](https://github.com/nostrability/schemata/pull/117)), [NIP-19](/en/topics/nip-19/) bech32 base type schemas ([PR #118](https://github.com/nostrability/schemata/pull/118)), and validation for kind 777 spell events ([PR #125](https://github.com/nostrability/schemata/pull/125)). The release pipeline now publishes a kind `1` note to Nostr on each release ([PR #120](https://github.com/nostrability/schemata/pull/120)), so the project announces itself through the protocol it validates. Schemata now supports a dozen languages beyond the canonical JS/TS package: Rust, Go, Python, Kotlin, Java, Swift, Dart, PHP, C#/.NET, C++, Ruby, and C.

Alongside Schemata, the team published [schemata-codegen](https://github.com/nostrability/schemata-codegen), an experimental code generator that takes a different approach to the same validation problem. Where Schemata's validator packages require a JSON Schema runtime dependency, schemata-codegen ports schemas directly into typed native-language constructs (typed tag tuples, kind interfaces, and runtime validators), removing the need for a validator library at runtime. The [codegen-vs-validators comparison](https://github.com/nostrability/schemata-codegen/blob/main/CODEGEN-VS-VALIDATORS.md) documents when each approach fits.

### BigBrotr v6.5.0 through v6.5.4

[BigBrotr](https://github.com/BigBrotr/bigbrotr), the relay analytics platform, shipped five releases from [v6.5.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.0) through [v6.5.4](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.4). The v6.5.0 release centralizes relay URL validation with a `parse_relay_url()` factory function and adds URL length checking and path sanitization. The monitoring infrastructure also received fixes: announcement events now include geohash location tags (following [NIP-52](/en/topics/nip-52/)), and timeout protection was added to the Geo/Net [NIP-66](/en/topics/nip-66/) metadata tests that had no deadline and could hang indefinitely. [PR #410](https://github.com/BigBrotr/bigbrotr/pull/410) upgrades PostgreSQL from 16 to 18, which brings the async I/O subsystem and improved WAL throughput to the relay analytics pipeline.

### Vertex Lab relay adds NIP-50 profile search

[Vertex Lab](https://vertexlab.io), the team behind [npub.world](https://github.com/vertex-lab/npub.world) and the [Vertex](https://github.com/vertex-lab/vertex) Web of Trust engine, announced that `wss://relay.vertexlab.io` now supports [NIP-50](/en/topics/nip-50/) (Search) for profile queries. NIP-50 extends the standard Nostr `REQ` filter with a `search` field, letting clients send full-text search queries to relays that support indexing. Adding profile search to a relay that already serves Web of Trust data means clients connected to `relay.vertexlab.io` can discover users by name or description without a separate search service.

### Hashtree v0.2.17 and v0.2.18 ship WebRTC mesh and Iris Desktop

[Hashtree](https://github.com/mmalmi/hashtree), mmalmi's content-addressed blob storage system that publishes Merkle roots on Nostr, shipped [v0.2.17](https://github.com/mmalmi/hashtree/releases/tag/v0.2.17) and [v0.2.18](https://github.com/mmalmi/hashtree/releases/tag/v0.2.18) on March 31. The two releases cap a 30-commit sprint that adds three distinct capabilities. First, the `hashtree-webrtc` crate (renamed to `hashtree-network` in v0.2.18) adds WebRTC-based peer-to-peer blob distribution with unified mesh signaling across the Rust CLI, the simulation harness, and the TypeScript client. Second, the release pipeline now builds Windows artifacts (CLI zip and Iris installer), bringing cross-platform coverage to macOS, Linux, and Windows. Third, both releases bundle Iris Desktop 0.1.0, mmalmi's Nostr social client, as AppImage, .deb, and Windows installer assets alongside the hashtree CLI. [Hashtree was first covered in Newsletter #10](/en/newsletters/2026-02-18-newsletter/) when it launched as a filesystem-based [Blossom](/en/topics/blossom/)-compatible store. The WebRTC layer is the first step toward peer-to-peer content distribution without depending on centralized Blossom servers.

### Nostr Mail Client v0.7.0 through v0.7.2

[Nostr Mail Client](https://github.com/nogringo/nostr-mail-client), the Flutter mail-style client built on Nostr identities, shipped [v0.7.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.0), [v0.7.1](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.1), and [v0.7.2](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.2) in three days. The visible product work centered on onboarding ([PR #9](https://github.com/nogringo/nostr-mail-client/pull/9)) and profile editing ([PR #10](https://github.com/nogringo/nostr-mail-client/pull/10)), which are basic pieces for any client trying to present Nostr as a mailbox. The later point releases packaged that work into fresh Android and Linux builds.

### Wisp v0.14.0 through v0.16.1

[Wisp](https://github.com/barrydeen/wisp), the Android Nostr client, shipped 13 more releases from [v0.14.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.14.0-beta) through [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta). The work this week includes NIP-17 rumor JSON fixes ([PR #385](https://github.com/barrydeen/wisp/pull/385)), repost badges on gallery cards ([PR #383](https://github.com/barrydeen/wisp/pull/383)), expandable reaction details ([PR #382](https://github.com/barrydeen/wisp/pull/382)), persistent emoji sets ([PR #381](https://github.com/barrydeen/wisp/pull/381)), and video autoplay controls ([PR #380](https://github.com/barrydeen/wisp/pull/380)). The latest [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta) also fixes custom emoji shortcodes with hyphens and missing emoji tags.

### Primal Android 3.0.17

[Primal Android](https://github.com/PrimalHQ/primal-android-app) shipped [3.0.17](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.17) on March 24. [PR #1000](https://github.com/PrimalHQ/primal-android-app/pull/1000) maps WalletException types to error codes in NWC responses, giving [NIP-47](/en/topics/nip-47/) clients structured failure information instead of generic errors. [PR #995](https://github.com/PrimalHQ/primal-android-app/pull/995) fixes poll zap votes appearing as Top Zaps, and [PR #998](https://github.com/PrimalHQ/primal-android-app/pull/998) hides wallet balance and action buttons when no wallet is configured.

### OpenChat v0.2.4 through v0.3.0

[OpenChat](https://github.com/DavidGershony/openChat), the Avalonia-based chat client built on the [Marmot](/en/topics/marmot/) stack, shipped six releases from [v0.2.4](https://github.com/DavidGershony/openChat/releases/tag/v0.2.4) through [v0.3.0](https://github.com/DavidGershony/openChat/releases/tag/v0.3.0) in four days. The commit log tells the story of a client filling in the gaps between "Marmot works" and "someone can actually use this daily." [NIP-42](/en/topics/nip-42/) relay authentication landed, followed by a relay picker UI with duplicate event filtering. Voice messages gained pause, resume, seek, and time display. The signer path was hardened: Amber connections were fixed with an updated [NIP-46](/en/topics/nip-46/) URI format, the WebSocket auto-reconnects before sending requests, and duplicate Amber requests are now caught by checking for replayed responses. On the storage side, Linux and macOS got AES-256-GCM secure storage with file-backed keys, and user metadata fetching now uses [NIP-65](/en/topics/nip-65/) relay discovery and caches results in a local database.

### Igloo Signer 1.1

[Igloo](https://github.com/FROSTR-ORG/igloo-ios-prototype), the iOS [FROST](/en/topics/frost/) threshold signer from the FROSTR project, shipped [v1.1](https://github.com/FROSTR-ORG/igloo-ios-prototype/releases/tag/v1.1) on March 28. FROST (Flexible Round-Optimized Schnorr Threshold) signatures let a group of signers collectively control a Nostr keypair, where any t-of-n participants can sign an event without any single party holding the full private key. Igloo is one of the first mobile implementations of this approach for Nostr.

### nak v0.19.3 and v0.19.4

[nak](https://github.com/fiatjaf/nak), fiatjaf's command-line Nostr toolkit, shipped [v0.19.3](https://github.com/fiatjaf/nak/releases/tag/v0.19.3) and [v0.19.4](https://github.com/fiatjaf/nak/releases/tag/v0.19.4) on March 26 and 30. Both releases fix panic conditions: [PR #118](https://github.com/fiatjaf/nak/pull/118) replaces `strings.Split` with `strings.Cut` to prevent a potential out-of-bounds access, and [PR #119](https://github.com/fiatjaf/nak/pull/119) prevents the same class of panic in curl flag parsing.

### Flora v0.3.0

[Flora](https://github.com/shawnyeager/flora-extension), a Chrome extension for decentralized screen recording and sharing on Nostr, shipped [v0.3.0](https://github.com/shawnyeager/flora-extension/releases/tag/v0.3.0). The release adds private encrypted video sharing with public, unlisted, and private modes. Private recordings are encrypted with AES-256-GCM and delivered to recipients via [NIP-17](/en/topics/nip-17/) (Private Direct Messages), so the recording never touches a server in cleartext.

### YakiHonne Mobile 2.0.3

[YakiHonne](https://github.com/YakiHonne/mobile-app), the mobile Nostr client, shipped [2.0.3](https://github.com/YakiHonne/mobile-app/releases/tag/YakiHonne-2.0.3) with relay reviews and join requests, expanded nested replies, auto-translation for notes, and NWC multi-relay support.

## Project Updates

### Zap Cooking adds zap polls and Branta payment verification

[Zap Cooking](https://github.com/zapcooking/frontend), the recipe and content platform, merged 11 PRs this week focused on interactive content and payment flows. [PR #277](https://github.com/zapcooking/frontend/pull/277) adds zap polls (kind 6969), where users vote by sending sats and can view voter lists with profile pictures. [PR #274](https://github.com/zapcooking/frontend/pull/274) redesigns the poll UX so the voting interface sits more naturally in the feed.

[PR #276](https://github.com/zapcooking/frontend/pull/276) adds camera-based QR scanning to the Send Payment flow and integrates [Branta](https://branta.pro/), a verification service that checks whether a payment destination is legitimate before send. Branta checks payment destinations against phishing, address swaps, and man-in-the-middle interception before send. In Zap Cooking's implementation, a Branta-verified platform name and logo show up directly in the payment flow, and Branta-enabled QR codes can carry `branta_id` and `branta_secret` parameters so the wallet can verify the destination from the scanned code itself.

### diVine lays groundwork for unified search and hardens video delivery

[diVine](https://github.com/divinevideo/divine-mobile), the short-form video client, spent the week tightening search, feed navigation, playback recovery, and upload behavior. [PR #2540](https://github.com/divinevideo/divine-mobile/pull/2540) lays down the foundation for a unified search screen, with grouped sections for Videos, People, and Tags. [PR #2623](https://github.com/divinevideo/divine-mobile/pull/2623) hardens pagination across profile feeds, inbox, notifications, discover lists, classic vines, search, and the composable grid feeds by moving them onto a shared pagination controller.

Video delivery also got several concrete fixes. [PR #2643](https://github.com/divinevideo/divine-mobile/pull/2643) retries Divine-hosted derivative sources in order and falls back to the raw blob before surfacing a playback error, so transient failures on one source do not kill playback immediately. [PR #2634](https://github.com/divinevideo/divine-mobile/pull/2634) keeps resumable uploads on the Divine-owned path when capability probing fails transiently, reducing broken uploads from short network faults. [PR #2637](https://github.com/divinevideo/divine-mobile/pull/2637) also changes the sensitive-content gate so videos are only hard-gated for actual warning labels, not merely for creator-supplied content warning labels.

### Shopstr adds custom storefronts and Milk Market keeps shipping marketplace work

[Shopstr](https://github.com/shopstr-eng/shopstr), the Nostr-based marketplace, merged [PR #245](https://github.com/shopstr-eng/shopstr/pull/245) adding custom storefronts. That gives sellers a more distinct home surface instead of forcing every listing into the same generic presentation.

[Milk Market](https://github.com/shopstr-eng/milk-market), a dedicated marketplace for milk, continued with storefront optimizations ([PR #18](https://github.com/shopstr-eng/milk-market/pull/18)), account recovery ([PR #17](https://github.com/shopstr-eng/milk-market/pull/17)), beef splits ([PR #15](https://github.com/shopstr-eng/milk-market/pull/15)), and MCP tool typing fixes ([PR #16](https://github.com/shopstr-eng/milk-market/pull/16)).

### Notedeck adds sound effects and extends its updater path toward Android

[Notedeck](https://github.com/damus-io/notedeck), the desktop client from the Damus team, merged [PR #1412](https://github.com/damus-io/notedeck/pull/1412) adding a sound effects subsystem with UI interaction sounds using rodio, and [PR #1399](https://github.com/damus-io/notedeck/pull/1399) with Agentium updates including a CLI title flag and collapsible session folders. An open [PR #1417](https://github.com/damus-io/notedeck/pull/1417) proposes APK self-update via Nostr/Zapstore on Android, building on [Notedeck's Nostr-native updater work from Newsletter #14](/en/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr).

### Nostria adds repost relay hints and NIP-98 alignment

[Nostria](https://github.com/nostria-app/nostria) merged [PR #583](https://github.com/nostria-app/nostria/pull/583) adding [NIP-18](/en/topics/nip-18/) (Reposts) relay hints to repost `e` tags for kind 6 and kind 16 events, [PR #582](https://github.com/nostria-app/nostria/pull/582) aligning Brainstorm HTTP auth (kind 27235) with [NIP-98](/en/topics/nip-98/) (HTTP Auth) required tags, and [PR #576](https://github.com/nostria-app/nostria/pull/576) adding Schemata schema validation tests. The NIP-98 change means Nostria can authenticate to external services using the same HTTP auth format other clients use.

### Nostr-Doc adds desktop packaging and offline-first work

[Nostr-Doc](https://github.com/formstr-hq/nostr-docs), the collaborative editor from Form*, had a busy week of packaging and editor work. [commit fcdc00a](https://github.com/formstr-hq/nostr-docs/commit/fcdc00a564c8d76f094c586b06efce07592a60e4) adds a desktop app, [commit 3977a8e](https://github.com/formstr-hq/nostr-docs/commit/3977a8eb2e62b84a67de756c2776e14de8470927) starts native app work, and [commit 413a030](https://github.com/formstr-hq/nostr-docs/commit/413a030f5b47fb8e32a5dff81bcef557ad9b5869) pushes the app toward offline-first behavior. On the editor side, [commit 1855ce8](https://github.com/formstr-hq/nostr-docs/commit/1855ce86ee83ad504e14e47d9c339baffb114786) adds Ctrl+S save, save warnings, link preview fixes, and corrected strikethrough rendering.

### rust-nostr optimizes NIP-21 parsing and adds relay-side NIP-62 support

[rust-nostr](https://github.com/rust-nostr/nostr) merged eight PRs. The most notable is [PR #1308](https://github.com/rust-nostr/nostr/pull/1308), which optimizes [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) URI parsing in `PublicKey::parse` by aligning it with standard bech32 parsing performance. Previously NIP-21 URIs took roughly twice as long to parse as raw bech32 keys. The project also has four open PRs adding relay-specific [NIP-62](/en/topics/nip-62/) (Request to Vanish) support across the memory, LMDB, SQLite, and database test backends ([PR #1315](https://github.com/rust-nostr/nostr/pull/1315), [PR #1316](https://github.com/rust-nostr/nostr/pull/1316), [PR #1317](https://github.com/rust-nostr/nostr/pull/1317), [PR #1318](https://github.com/rust-nostr/nostr/pull/1318)).

### nostr-tools adds bunker relay control and fixes NIP-47 multi-relay parsing

[nostr-tools](https://github.com/nbd-wtf/nostr-tools) merged [PR #530](https://github.com/nbd-wtf/nostr-tools/pull/530) adding `skipSwitchRelays` to BunkerSignerParams for manual relay management, and [PR #529](https://github.com/nbd-wtf/nostr-tools/pull/529) fixing [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect) connection string parsing to support multiple relays as the spec allows.

### Nostrability integrates Sherlock audit data and publishes Schemata overview

[Nostrability](https://github.com/nostrability/nostrability), the interoperability tracker for Nostr clients, merged 14 PRs. [PR #306](https://github.com/nostrability/nostrability/pull/306) integrates Sherlock scan statistics into the dashboard. Sherlock is Nostrability's automated audit tool that connects to Nostr clients, captures the events they publish, and validates each event against the Schemata JSON Schema definitions to detect spec violations. The dashboard now shows per-client schema fail rates ([PR #315](https://github.com/nostrability/nostrability/pull/315)) so developers can see which event kinds their client gets wrong. [PR #323](https://github.com/nostrability/nostrability/pull/323) overhauls the Nostr publish workflow so release announcements run as a separate job that cannot be cancelled by earlier CI steps.

elsat also published [Schemata for nostr devs](https://njump.me/naddr1qvzqqqr4gupzq96n3hp2vfmf6z2y8uvvxl97xk86kkalnqghx4p25lzl79c76a7yqy2hwumn8ghj7un9d3shjtnyv9kh2uewd9hj7qgwwaehxw309ahx7uewd3hkctcqz4fnx4rkw3x57nrcwdn8zt22xd982jehfptsgqtrww) on March 30, describing how schemata, schemata-codegen, and Sherlock fit together and giving current coverage numbers: 179 event kind schemas across 65 NIPs, 154 tag schemas, 13 protocol messages, and 310 sample events.

### Nalgorithm adds digest generation and local score caching

[Nalgorithm](https://github.com/jooray/nalgorithm), a new relevance-ranked Nostr feed project, started public development this week. [commit cf6c501](https://github.com/jooray/nalgorithm/commit/cf6c501e754ef95a1b4fecc1a76288471a101f43) lays down the initial web app that fetches posts from follows and scores them against a user-defined preference prompt. [commit 8e931b6](https://github.com/jooray/nalgorithm/commit/8e931b6ae85d470e73603752134ff49b7ba4bb86) adds a CLI digest tool that turns top-ranked posts into a spoken-word summary, while [commit 4cb9c63](https://github.com/jooray/nalgorithm/commit/4cb9c635489a9a3429e8d71f3861dc2a11624153) adds file-based score caching and incremental learned-prompt evolution from recent likes. [commit c2edfb8](https://github.com/jooray/nalgorithm/commit/c2edfb8b89fadbe0028c3f5729bda7e23b2e3c03) also stops caching fallback scores from failed batches, so a transient scoring failure does not permanently flatten a post's rank.

### TENEX adds RAG vector store and targeted MCP startup

[TENEX](https://github.com/tenex-chat/tenex), the Nostr-native agent framework that bridges AI agents to Nostr channels via Telegram, merged seven PRs this week. [PR #101](https://github.com/tenex-chat/tenex/pull/101) adds a pluggable vector store abstraction with SQLite-vec, LanceDB, and Qdrant backends, giving agents retrieval-augmented generation without locking into one vector database. [PR #102](https://github.com/tenex-chat/tenex/pull/102) makes MCP startup targeted: only MCP servers whose tools an agent actually uses are started, instead of eagerly launching all servers on first execution. [PR #100](https://github.com/tenex-chat/tenex/pull/100) adds a `send_message` tool so agents with Telegram channel bindings can proactively push messages instead of only responding to incoming ones. [PR #106](https://github.com/tenex-chat/tenex/pull/106) avoids a subprocess spawn that triggered a 9GB Bun/JSC memory pre-allocation by reading `.git/HEAD` directly instead of running `git branch`.

### Dart NDK moves Amber signer and adds Alby Go 1-click

[Dart NDK](https://github.com/relaystr/ndk), the Flutter Nostr development kit, shipped 11 merged PRs. [PR #525](https://github.com/relaystr/ndk/pull/525) moves Amber signer support into the ndk_flutter package, and [PR #552](https://github.com/relaystr/ndk/pull/552) adds Alby Go one-click wallet connection to the sample app. [PR #502](https://github.com/relaystr/ndk/pull/502) adds an install.sh script for the CLI, and [PR #523](https://github.com/relaystr/ndk/pull/523) removes the Rust verifier dependency in favor of native asset handling.

## Protocol and Spec Work

### Marmot moves KeyPackages to addressable events and tightens push notifications

The [Marmot specification](https://github.com/marmot-protocol/marmot) merged four PRs that change how the protocol handles key material and group membership. [PR #54](https://github.com/marmot-protocol/marmot/pull/54) migrates KeyPackage events from regular `kind:443` to addressable `kind:30443` with a `d` tag, eliminating the need for [NIP-09](/en/topics/nip-09/) event deletion during key rotation. Addressable events overwrite in place, making rotation self-contained. [PR #57](https://github.com/marmot-protocol/marmot/pull/57) allows non-admin users to commit SelfRemove proposals (voluntary group departure), and [PR #62](https://github.com/marmot-protocol/marmot/pull/62) requires admins to relinquish admin status before using SelfRemove, preventing an admin from disappearing while still holding elevated privileges.

[PR #61](https://github.com/marmot-protocol/marmot/pull/61) tightens the [MIP-05](/en/topics/mip-05/) push notification format, making the single-blob base64 encoding, versioning, token wire format, and x-only key usage explicit. The effect is one defined wire representation for token blobs and x-only keys across spec, client libraries, and app backends. Implementation of these spec changes landed in the White Noise stack this week and is covered in the [White Noise v2026.3.23 section above](#white-noise-fixes-relay-churn-and-expands-client-controls).

### NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md): Static Websites** ([PR #1538](https://github.com/nostr-protocol/nips/pull/1538)): Defines kind `15128` (root site) and kind `35128` (named site) manifest events for hosting static websites under Nostr keypairs using Blossom storage. See the [deep dive below](#nip-deep-dive-nip-5a-static-websites).

- **[NIP-30](/en/topics/nip-30/) (Custom Emoji): Allow hyphens in shortcodes** ([PR #2297](https://github.com/nostr-protocol/nips/pull/2297)): Updates the shortcode description to include hyphens. Hyphenated shortcodes have been used in practice since the NIP was introduced, so the spec now documents current usage.

**Open PRs and Discussions:**

- **NIP-C1: Agent TUI Messages** ([PR #2295](https://github.com/nostr-protocol/nips/pull/2295)): Proposes a structured message format for agents to send interactive UI elements through encrypted DMs, including typed `text`, `buttons`, `card`, and `table` payloads. The draft keeps everything inside existing [NIP-17](/en/topics/nip-17/) and [NIP-04](/en/topics/nip-04/) direct-message content as JSON. It does not define a new event kind, and it uses a simple callback string format for button responses.

- **NIP-95: Hybrid Peer-to-Peer Relay Protocol** ([PR #2293](https://github.com/nostr-protocol/nips/pull/2293)): Proposes a hybrid relay model where relays stay authoritative but can also coordinate peer-to-peer distribution of recent events over WebRTC. The draft introduces relay messages such as `PEER_REGISTER`, `PEER_REQUEST`, and `PEER_OFFER`, with stable clients acting as Super Peers and the relay acting as the seed node and fallback.

- **NIP-B9: Zap Poll Events** ([PR #2284](https://github.com/nostr-protocol/nips/pull/2284)): Reopens the old NIP-69 zap-poll idea now that [NIP-88](https://github.com/nostr-protocol/nips/blob/master/88.md) (Polls) covers free polls. The draft uses kind `6969` poll definitions and kind `9734` zaps as votes, making it a paid polling system with economic Sybil resistance. It complements free one-key-one-vote polls.

- **NIP-AD: Super Zap** ([PR #2289](https://github.com/nostr-protocol/nips/pull/2289)): Proposes a convention where zaps sent to a relay's pubkey or a client's pubkey are displayed as specialized promotional notes, effectively turning zap receipts into an ad surface. Relay operators and clients would publish profiles with `lud16`, fetch those receipts, extract the embedded content from zap descriptions, and optionally set minimum-sats thresholds to suppress spam.

- **NIP-XX: Agent Reputation Attestations** ([PR #2285](https://github.com/nostr-protocol/nips/pull/2285)): Proposes kind `30085` as a parameterized replaceable event for structured reputation attestations about Nostr agents. The draft avoids a single global score by making reputation observer-dependent, adds temporal decay so old attestations fade, supports negative ratings with evidence requirements, and sketches both simple weighted scoring and graph-diversity scoring for better Sybil resistance.

- **NIP-XX: Paid API Service Announcements** ([PR #2291](https://github.com/nostr-protocol/nips/pull/2291)): Proposes kind `31402` addressable events for advertising paid HTTP APIs, with Nostr handling discovery and HTTP 402 handling payment. The draft is tags-first so relays can filter on payment methods, prices, and capabilities without parsing JSON content, and it allows optional request and response schemas so clients or agents can auto-generate calls.

- **NIP-XX: Key Derivation from LNURL-auth via SplitSig** ([PR #2294](https://github.com/nostr-protocol/nips/pull/2294)): Proposes deriving a Nostr keypair from an LNURL-auth ECDSA signature combined with a client-side random nonce. The derivation formula is `nsec = SHA256(ecdsa_signature || nonce)`. The server sees the ECDSA signature (inherent to the LNURL-auth handshake) but never sees the nonce, and the browser generates the nonce but does not control the signature. Neither piece alone can derive the nsec. The intended outcome is that the same Lightning wallet produces the same Nostr key across devices, with the wallet as the recovery anchor and no server able to reconstruct the private key.

- **[NIP-55](/en/topics/nip-55/): Document rejected field** ([PR #2290](https://github.com/nostr-protocol/nips/pull/2290)): Documents the `rejected` field for intent-based signer responses, formalizing the behavior that [Amethyst's v1.07.x fix](#amethyst-ships-pinned-notes-relay-management-and-request-to-vanish) had to work around.

## NIP Deep Dive: NIP-5A (Static Websites)

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md) defines how to host static websites under Nostr keypairs, using two event kinds and existing blob storage infrastructure to turn signed events into served web pages. The [specification](https://github.com/nostr-protocol/nips/blob/master/5A.md) was merged on March 25 via [PR #1538](https://github.com/nostr-protocol/nips/pull/1538).

The model uses kind `15128` for a root site, one per pubkey, and kind `35128` for named sites identified by a `d` tag. Each manifest maps absolute URL paths to SHA256 hashes. Here is a root site manifest:

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["path", "/favicon.ico", "fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["description", "A static website hosted on Nostr"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

The serving flow works in three steps. A host server receives an HTTP request, extracts the author's pubkey from the subdomain (either an npub for root sites or a base36-encoded pubkey for named sites), fetches the author's relay list via [NIP-65](/en/topics/nip-65/), and queries for the site manifest. Once the manifest is found, the server resolves the requested path to a content hash, downloads the matching blob from the Blossom server or servers listed in the `server` tags, and returns it.

The DNS subdomain format is tightly specified. Root sites use the standard npub as the subdomain. Named sites use a 50-character base36 encoding of the raw pubkey followed by the `d` tag value, all in a single DNS label. Because DNS labels are limited to 63 characters and the base36 encoding always takes 50, the `d` tag is limited to 13 characters. The spec also requires `d` tags to match `^[a-z0-9-]{1,13}$` and not end with a hyphen, preventing DNS resolution ambiguities.

Using content hashes means the same site can be served by different host servers, and file integrity is verifiable without trusting the server. A host server does not need to store any files itself. It fetches them on demand from Blossom using the hashes in the manifest. That means the author controls what is served, the Blossom server stores the raw files, and the host server just connects the two. Any of these three components can be replaced independently.

Existing implementations include [nsite](https://github.com/lez/nsite), the host server that resolves manifests and serves files, and [nsite-manager](https://github.com/hzrd149/nsite-manager), a UI for building and publishing manifests. The spec also added a `source` tag for linking to the site's source code repository, and the README update merged separately in [PR #2286](https://github.com/nostr-protocol/nips/pull/2286) registered both kind `15128` and `35128` in the NIP kind index.

## NIP Deep Dive: NIP-62 (Request to Vanish)

[NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md) defines kind `62` as a request for relays to delete all events from the requesting pubkey. The [specification](https://github.com/nostr-protocol/nips/blob/master/62.md) is legally motivated: in jurisdictions with right-to-be-forgotten laws, having a standardized, signed deletion request gives relay operators a clear signal to act on.

```json
{
  "id": "a7b8c9d0e1f23456789012345678901234567890abcdef1234567890abcdef12",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1743465600,
  "kind": 62,
  "tags": [
    ["relay", "wss://relay.example.com"]
  ],
  "content": "Requesting deletion of all events from this relay.",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

The spec separates targeted and global vanish requests. A targeted request includes specific `relay` tags identifying which relays should act. A global request uses the literal string `ALL_RELAYS` as the relay tag value, asking every relay that sees the event to delete all events from that pubkey. Relays that comply must also ensure deleted events cannot be re-broadcast back into the relay, making the deletion sticky.

NIP-62 goes beyond [NIP-09](/en/topics/nip-09/) (Event Deletion) in both scope and intent. NIP-09 lets you delete individual events, and relays MAY comply. NIP-62 requests deletion of everything, and the spec says relays MUST comply if their URL is tagged. It also asks relays to delete [NIP-59](/en/topics/nip-59/) (Gift Wrap) events that p-tagged the requesting pubkey, which means incoming DMs get cleaned up alongside the user's own events. Publishing a NIP-09 deletion against a NIP-62 vanish request has no effect: once you vanish, you cannot un-vanish by deleting the vanish request.

This week, [Amethyst v1.07.0](#amethyst-ships-pinned-notes-relay-management-and-request-to-vanish) shipped client-side NIP-62 support, letting users initiate vanish requests from the app. On the relay side, [rust-nostr](https://github.com/rust-nostr/nostr) has four open PRs adding NIP-62 support across the memory, LMDB, SQLite, and database test backends ([PR #1315](https://github.com/rust-nostr/nostr/pull/1315), [PR #1316](https://github.com/rust-nostr/nostr/pull/1316), [PR #1317](https://github.com/rust-nostr/nostr/pull/1317), [PR #1318](https://github.com/rust-nostr/nostr/pull/1318)). This puts client support and relay support work into the same week.

The protocol design raises a practical tension. Nostr's value proposition includes censorship resistance, meaning relays should not be able to prevent publication. NIP-62 introduces a case where a relay MUST prevent re-publication from a specific pubkey. The two properties coexist because the request is self-directed: you are asking for deletion of your own events, not someone else's. The censorship-resistance property remains intact for everyone except the person who explicitly opted out.

---

That's it for this week. Building something or have news to share? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Reach out via [NIP-17](/en/topics/nip-17/) (Private Direct Messages) DM</a> or find us on Nostr.
