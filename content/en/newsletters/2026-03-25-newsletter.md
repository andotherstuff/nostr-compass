---
title: 'Nostr Compass #15'
date: 2026-03-25
publishDate: 2026-03-25
draft: false
type: newsletters
description: 'Primal adds Follow Packs and deep links, BigBrotr publishes an nsec leak analysis, Nostr VPN launches, and DOOM runs peer-to-peer over Nostr.'
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** [Primal Android](https://github.com/PrimalHQ/primal-android-app) follows its 3.0 wallet release with [Follow Packs, zap enrichment, and `primalconnect://` deep links](#primal-adds-follow-packs-zap-enrichment-and-deep-links). [BigBrotr](https://github.com/BigBrotr/bigbrotr) publishes an [nsec leak analysis](#bigbrotr-maps-exposed-private-keys-across-the-relay-network) scanning 41 million events across 1,085 relays, finding 16,599 valid private keys, while [npub.world](https://npub.world) integrates leak warnings into profile pages the same week. Martti Malmi launches [nostr-vpn](#nostr-vpn-launches-as-a-tailscale-alternative), a Tailscale alternative that signals over Nostr relays and creates WireGuard tunnels, shipping 11 releases in seven days. The [Vector](https://github.com/VectorPrivacy/Vector) team [open-sources P2P DOOM](#open-source-doom-runs-peer-to-peer-over-nostr) over Nostr, [FIPS](https://github.com/jmcorgan/fips) ships [v0.2.0](#fips-v020-ships-tor-transport-reproducible-builds-and-sidecar-examples), and [Nostrability Schemata](https://github.com/nostrability/schemata) expands to [six languages](#nostrability-schemata-goes-multilingual) in one week.

## News

### Primal adds Follow Packs, zap enrichment, and deep links

[Following last week's 3.0.7 coverage](/en/newsletters/2026-03-18-newsletter/), [Primal Android](https://github.com/PrimalHQ/primal-android-app) spent this week on post-release work around onboarding, composer UX, and wallet context. Redesigned onboarding introduces Follow Packs ([PR #949](https://github.com/PrimalHQ/primal-android-app/pull/949)), a native GIF button joins the note composer, a zap enrichment service ([PR #979](https://github.com/PrimalHQ/primal-android-app/pull/979)) annotates wallet transactions with zap context, and a `primalconnect://` deep-linking protocol ([PR #969](https://github.com/PrimalHQ/primal-android-app/pull/969)) enables cross-app navigation.

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app) is shipping the same work through TestFlight in parallel, with the wallet switch ([PR #191](https://github.com/PrimalHQ/primal-ios-app/pull/191)), poll implementation, and onboarding refactor landing in the same window.

### BigBrotr maps exposed private keys across the relay network

[BigBrotr](https://github.com/BigBrotr/bigbrotr), the Nostr relay analytics platform, published a [detailed analysis of exposed private keys](https://bigbrotr.com/blog/exposed-nsec-analysis/) on the relay network. The study scanned 41 million events from 1,085 relays, searching for valid nsec strings embedded in event content, and found 16,599 valid private keys. That number looks alarming until you filter out a bot called "Mr.nsec" that accounts for 92% of the matches. After removing bot traffic, only 38 real accounts with more than 21,000 combined followers had exposed keys, and none showed signs of awareness that their keys were public.

The team built an nsec-leak-checker as a [NIP-90](/en/topics/nip-90/) (Data Vending Machine) service, letting users check whether their private key appears anywhere in the scanned dataset without revealing the key to the checker. [npub.world](https://npub.world) integrated the leak data the same week, displaying warning banners on profile pages where exposed keys were detected. The combination gives the network both a programmatic interface for DVMs and agents and a human-readable warning for regular users. The underlying dataset also feeds [BigBrotr v6.4.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.4.0), which adds replaceable and addressable event materialized views and a synchronizer idle timeout fix.

### Nostr VPN launches as a Tailscale alternative

Martti Malmi (mmalmi), creator of Iris, built and shipped [nostr-vpn](https://github.com/mmalmi/nostr-vpn), a peer-to-peer VPN that uses Nostr relays for signaling and WireGuard (via boringtun) for encrypted tunnels. The motivation was direct: "Got annoyed by Tailscale requiring 3rd party accounts, so created Nostr VPN." The tool creates mesh networks between devices using Nostr keypairs as identity, with no central coordination server.

The project shipped 11 releases in seven days, from [v0.2.2](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.2) through [v0.2.13](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.13). That sprint added Windows support, LAN pairing for local network discovery, and an Android sidecar for mobile devices. The architecture is simple: two devices exchange connection metadata over Nostr relays, then establish a direct WireGuard tunnel. Nostr handles discovery and NAT traversal signaling. WireGuard handles the actual traffic. Identity is a Nostr keypair.

Malmi also continued pushing [nostr-double-ratchet](https://github.com/mmalmi/nostr-double-ratchet), a Signal-style secure messaging channel library, shipping six releases from [v0.0.86](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.86) through [v0.0.93](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.93) during the same week.

### Open-source DOOM runs peer-to-peer over Nostr

The [Vector](https://github.com/VectorPrivacy/Vector) team open-sourced a peer-to-peer multiplayer DOOM implementation that uses Nostr for peer discovery, [Marmot](/en/topics/marmot/) for end-to-end encryption, and [Iroh](https://github.com/n0-computer/iroh), the QUIC networking library from n0, for gossip transport. The game ships as a 4.2 MB WebXDC file that can be sent inside chat messages, requiring no servers to host or coordinate a match.

The technical approach replaces the original 1993 lockstep netcode with a real-time hybrid sync model. Players discover each other through Nostr relay queries, negotiate sessions through Marmot-encrypted channels, then hand off to Iroh's QUIC gossip layer for the low-latency game traffic. The stack uses Nostr for discovery, Marmot for encryption, and Iroh for transport.

Vector also shipped security hardening this week. The release adds a memory-hardened key vault with anti-debug protections and zeroize for sensitive key material, user blocking with full DM and group message filtering, and WebXDC realtime channel fixes for Mini Apps.

### FIPS v0.2.0 ships Tor transport, reproducible builds, and sidecar examples

[FIPS](https://github.com/jmcorgan/fips), the Free Internetworking Peering System and Nostr-adjacent mesh networking project, shipped [v0.2.0](https://github.com/jmcorgan/fips/releases/tag/v0.2.0-rel). The release adds Tor transport support for anonymized mesh links, reproducible builds, a sidecar example that connects through a Nostr relay, and Nostr release publishing in the OpenWrt package workflow. The release also fixes post-rekey jitter spikes caused by drain-window frames. The wire format changed from v0.1.0, so existing v0.1.0 nodes cannot interoperate with v0.2.0 without upgrading.

### Nostrability Schemata goes multilingual

The [Nostrability Schemata](https://github.com/nostrability/schemata) project, which maintains JSON Schema definitions for validating Nostr event kinds, expanded from JavaScript-only to six languages in one week. New packages shipped for Rust, Go, Dart, Swift, and Python, each providing both a data package and a validator. [v0.2.6](https://github.com/nostrability/schemata/releases/tag/v0.2.6) also added 17 new event kind schemas.

The [Nostrability interop tracker](https://nostrability.github.io/nostrability/) received a parallel overhaul. A new What's New tab publishes updates through both an Atom feed and a Nostr event, app category filtering lets visitors drill into specific client types, and the tracker now auto-detects programming languages from GitHub repository metadata. Nostrability also has its own npub now, making the project itself discoverable through the protocol it documents. For library authors working across languages, the multi-language schema packages mean the same event kind definitions are available as native imports instead of requiring each project to maintain its own schema copy.

## Releases

### Amethyst v1.06.0 and v1.06.1

[Amethyst](https://github.com/vitorpamplona/amethyst), the Android client maintained by vitorpamplona, shipped [v1.06.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.0) and [v1.06.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.1) on March 23. The headline feature is poll support using [NIP-85](/en/topics/nip-85/) (Trusted Assertions) data for weighted voting, with redesigned poll and zap poll cards. The new rendering gives both standard polls and zap-weighted polls a cleaner visual layout. v1.06.1 follows with concurrent modification crash fixes that address stability regressions introduced in the poll rendering path.

### Amber v5.0.0 and v5.0.1

[Amber](https://github.com/greenart7c3/Amber), the [NIP-55](/en/topics/nip-55/) (Android Signer Application) signer app, promoted its recent 4.1.x pre-release work into stable with [v5.0.0](https://github.com/greenart7c3/Amber/releases/tag/v5.0.0) on March 18. That stable release carries the [NIP-42](/en/topics/nip-42/) relay-auth, built-in Tor, content-type-specific permissions, and encrypted PIN storage changes covered last week. [v5.0.1](https://github.com/greenart7c3/Amber/releases/tag/v5.0.1) then removes internet permission from the offline build flavor, so that build can no longer make network requests at the Android permission layer.

### Mostro v0.17.0 and Mostro Mobile v1.2.2

[Mostro](https://github.com/MostroP2P/mostro), the peer-to-peer Bitcoin exchange built on Nostr, shipped [v0.17.0](https://github.com/MostroP2P/mostro/releases/tag/v0.17.0) on March 18. The server release continues the dispute and rating work from the v0.16.x cycle, adding more complete trade reputation data for buyers and sellers as Nostr events. [Mostro Mobile](https://github.com/MostroP2P/mobile), the Flutter client, followed with [v1.2.2](https://github.com/MostroP2P/mobile/releases/tag/v1.2.2) on March 23, keeping the mobile interface in sync with the latest protocol changes.

### Shosho v0.14.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), the Nostr live streaming app, shipped [v0.14.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.14.0) on March 19 with the launch of Shosho Shop. The release adds a Shop tab on profiles, Shop in Browse, and an In-Live Shop button on lives and clips. The release notes say existing "Nostr products" appear automatically and buyers click through to the seller's Plebeian Market page for purchase. Shosho's release notes do not identify the listing event kind, so it is not yet possible to confirm whether Shosho Shop reads the same [NIP-99](/en/topics/nip-99/) classified listings that [Shopstr](https://github.com/shopstr-eng/shopstr) explicitly supports in its README.

### Applesauce v5.2.0

[Applesauce](https://github.com/hzrd149/applesauce), hzrd149's collection of helper packages for building Nostr applications, shipped [v5.2.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core@5.2.0) on March 22. The release spans six packages. The SQLite package fixes a UNIQUE constraint collision on event tags that caused duplicate inserts. The signers package adds `AndroidNativeSigner`, which wraps the [NIP-55](/en/topics/nip-55/) native Android signer interface so web-view-based apps can use hardware-backed signing without custom bridge code. The relay package adds a `challenge` field to relay and pool status objects, tracking [NIP-42](/en/topics/nip-42/) auth state so apps can detect when a relay is requesting authentication and respond programmatically. The core package gains `isEventPointerSame` and `isAddressPointerSame` methods for deduplicating event references, and the common package adds `user.blossomServers$` for resolving a user's Blossom media servers. Applesauce powers noStrudel, Satellite, and several other web clients, so these fixes propagate across the web client layer.

### Wisp ships 16 releases in one week

[Wisp](https://github.com/barrydeen/wisp), the Android Nostr client, shipped 16 releases from [v0.9.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.9.3-beta) through [v0.13.1-beta](https://github.com/barrydeen/wisp/releases/tag/v0.13.1-beta) this week. The feature additions include multi-account support, a zen notifications mode for reduced interruptions, drafts and scheduled posts, safety content filters, and a new flame icon.

### Manent v1.2.0

[Manent](https://github.com/dtonon/manent), the private encrypted notes and file storage app, shipped [v1.2.0](https://github.com/dtonon/manent/releases/tag/v1.2.0) on March 20. The release adds camera capture directly from the app, image resizing before upload to reduce storage costs, and pinch-to-zoom for reviewing stored images. Manent stores notes and files encrypted on Nostr relays using the user's keypair, making the phone or desktop app a thin client that can reconstruct its full state from relay data.

### diVine 1.0.7

[diVine](https://github.com/divinevideo/divine-mobile), the short-form video client, shipped [1.0.7](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.7) on March 21 with a video playback watchdog that auto-resumes stalled videos. After the E2E test infrastructure and direct MP4 loading in [v1.0.6](/en/newsletters/2026-03-11-newsletter/#divine-ships-v106-with-e2e-test-infrastructure-and-nip-49-import), this release targets the remaining playback failure path: videos that stop mid-stream without throwing an error.

### Alby Extension v3.14.2

[Alby Extension](https://github.com/getAlby/lightning-browser-extension), the [NIP-07](/en/topics/nip-07/) (Browser Extension Signer) browser extension, shipped [v3.14.2](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.14.2) on March 18 with Lightning address QR code display and Schnorr signing support. The Schnorr addition aligns the browser extension with the secp256k1 signature scheme that Nostr uses natively.

### NoorNote v0.6.5 through v0.6.11

[NoorNote](https://github.com/77elements/noornote), the note-taking app, shipped seven releases from [v0.6.5](https://github.com/77elements/noornote/releases/tag/v0.6.5) through [v0.6.11](https://github.com/77elements/noornote/releases/tag/v0.6.11). The headline addition is Follow Packs: curated bundles of accounts that users can browse and subscribe to in bulk, similar to Twitter Lists but designed for onboarding. Users can create, edit, and share Follow Packs with custom titles, descriptions, and cover images. The series also upgrades the underlying Nostr library from NDK v2 to v3, which brings improved relay connection handling and subscription management. Picture notes and a redesigned relay connection experience round out the run.

### nak v0.19.1 and v0.19.2

[nak](https://github.com/fiatjaf/nak), fiatjaf's command-line Nostr toolkit for interacting with relays, encoding and decoding [NIP-19](/en/topics/nip-19/) (Bech32-Encoded Entities) identifiers, signing events, and querying relay data, shipped [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1) and [v0.19.2](https://github.com/fiatjaf/nak/releases/tag/v0.19.2) on March 17 and 20. The two point releases follow the [v0.19.0](/en/newsletters/2026-03-18-newsletter/) group-forum UI addition from last week.

### Calendar by Form* v0.2.1

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), the decentralized calendar app built on [NIP-52](/en/topics/nip-52/) (Calendar Events), shipped [v0.2.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.1) on March 20. The release fixes a notification template issue that affected event reminders. Calendar stores events as Nostr kind 31922 (date-based) and kind 31923 (time-based) events, letting any Nostr client render calendar data if it chooses to support the kinds. The app is built by the Formstr team, who also maintain Formstr (decentralized forms) and Pollerama (polls).

### NYM v3.50 through v3.53

[NYM](https://github.com/Spl0itable/NYM), the lightweight ephemeral chat client bridged with Bitchat, shipped 28 releases from v3.50 through v3.53 (the patch versions increment rapidly). The most notable feature is Nymbot, a built-in chat bot that responds to `@nymbot` mentions in channels and provides relay status and management functions. A "hardcore mode" generates a fresh keypair for every sent message, making conversation threads unlinkable at the identity level. The tradeoff is clear: you lose persistent identity but gain per-message anonymity. The relay proxy layer also received work, with sharded relay proxy workers for better connectivity, geohash channel support, and clock skew tolerance for nodes with imprecise system clocks.

## Project Updates

### Ditto adds Bluesky bridge and Wikipedia integration

[Ditto](https://github.com/soapbox-pub/ditto), the Soapbox team's customizable Nostr social client, logged over 300 commits this week across three distinct feature tracks. The first is a Bluesky bridge (19 commits) that renders Bluesky posts inline as full feed-style threads, adds sidebar navigation to a Bluesky discovery page backed by the official Discover (whats-hot) feed, and wires up action buttons for commenting, sharing, reacting, and copying links. When a user replies to a Bluesky post from within Ditto, the compose modal shows a disclaimer callout noting the cross-protocol nature of the interaction. [NIP-73](/en/topics/nip-73/) (External Content IDs) kind 17 reactions power the cross-protocol model: a Nostr user reacts to a Bluesky post, and the reaction is stored as a standard Nostr event referencing the external content identifier. This is the same NIP-73 pattern that could bridge reactions to any external content, from Bluesky posts to YouTube videos to web pages.

The second track is a Wikipedia integration (9 commits). Ditto now renders rich Wikipedia article content on detail pages instead of generic link previews, adds search autocomplete with article thumbnails, and provides a `/wikipedia` page pulling featured content from the Wikipedia API. Wikipedia and Archive.org results also appear in the general search autocomplete dropdown. The third track is iOS platform support via Capacitor, with a remote build script and platform configuration landing alongside a UI overhaul (55 commits) that replaces backdrop-blur headers with a new arc-based navigation design across every page in the app. The 314 commits move Ditto from a Nostr-only client toward a multi-protocol aggregator that treats Bluesky and Wikipedia as first-class content sources alongside the Nostr feed.

### Pika builds a NIP-34 forge CI pipeline

[Pika](https://github.com/sledtools/pika), the Marmot-based encrypted messaging app, merged 33 PRs this week focused on a self-hosted [NIP-34](/en/topics/nip-34/) forge with pre-merge CI. The forge is a git hosting layer that receives patches as NIP-34 events, runs CI checks before merge, and reports structured status back through Nostr events. [PR #701](https://github.com/sledtools/pika/pull/701) adds lane-based pre-merge and nightly CI, where each code path (Rust, TypeScript, Apple builds) runs in its own lane with independent pass/fail status. [PR #715](https://github.com/sledtools/pika/pull/715) cuts managed CI agents to Incus OpenClaw containers for isolation, and [PR #733](https://github.com/sledtools/pika/pull/733) adds a `ph forge` CLI for interacting with the hosted forge from the command line. Supporting PRs handle repo write permissions for merges ([PR #736](https://github.com/sledtools/pika/pull/736)), structured CI metadata with live status badges ([PR #722](https://github.com/sledtools/pika/pull/722)), Apple nightly build splits ([PR #738](https://github.com/sledtools/pika/pull/738)), and forge auth and branch lookup fixes ([PR #734](https://github.com/sledtools/pika/pull/734)). This is one of the first working CI/CD systems built on top of NIP-34 git events, moving Nostr-based source code hosting beyond basic patch exchange toward the merge-and-test workflow that developers expect from GitHub or GitLab.

### Nostria adds communities, code snippets, and voice event handling

[Nostria](https://github.com/nostria-app/nostria), the cross-platform Nostr client maintained by sondreb, spent this week extending the app surface beyond the Web of Trust filtering covered in #14. The main addition is a full [NIP-72](/en/topics/nip-72/) (Moderated Communities) implementation with community creation, moderator and relay configuration, post approval tracking with image previews, and a dedicated community page with Posts and Moderators tabs.

The same stretch of work also adds code snippet rendering and editing with a syntax-highlighted editor, voice event reply support for audio conversations, chat relay settings for direct messages, channel sharing through the Web Share API, a toolbar docking system for the media player, in-app signup for the latest Brainstorm Web of Trust service, send and receive money flows in DMs using NWC and BOLT-11 invoices, Nostr-native GIF handling, and a stronger RSS import path for musicians that can pick up existing Lightning splits from podcast feeds.

### nostr-vpn rapid iteration

Beyond the [initial launch](#nostr-vpn-launches-as-a-tailscale-alternative), the [nostr-vpn](https://github.com/mmalmi/nostr-vpn) commit log reveals the specific problems encountered during real deployment. [v0.2.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.3) through [v0.2.5](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.5) added the initial installer script and cross-platform CLI. [v0.2.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.6) and [v0.2.7](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.7) brought Windows support, which required UAC path quoting for config writes and daemon-owned config updates. [v0.2.8](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.8) through [v0.2.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.10) fixed Windows GUI service actions, CLI subprocess handling, and machine-scoped service configuration. [v0.2.12](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.12) replaced LAN discovery with timed LAN pairing, a user-initiated flow where two devices on the same local network pair without relay signaling. The pattern is textbook early-stage field testing: each release targets a specific deployment failure, the user base is small enough to iterate daily, and the developer is using the tool personally between releases.

### Comet automated builds

[Comet](https://github.com/nodetec/comet) (formerly Captain's Log), the Nostr-native long-form writing tool from Nodetec, produced over 40 automated alpha builds this week. Comet is a desktop app for writing and publishing NIP-23 (Long-form Content) articles, with local draft storage, markdown editing, and one-click publishing to the user's relay set. The automated build pipeline generates a tagged release for every commit to the main branch, which makes the raw release count misleading as a measure of feature velocity. What the 40 builds do show is that the app is under daily active development, with each commit tested, packaged, and made available for download within minutes.

## NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips) during the March 17-24 window:

No NIP merges landed between March 18 and March 24.

**Open PRs and Discussions updated during the window:**

- **NIP-AA: Autonomous Agents on Nostr** ([PR #2259](https://github.com/nostr-protocol/nips/pull/2259)): Proposes conventions for autonomous agents operating on the Nostr network. The PR defines how agents identify themselves, discover services, and coordinate with other agents and humans through Nostr events.

- **[NIP-50](/en/topics/nip-50/) (Search): Sort extensions** ([PR #2283](https://github.com/nostr-protocol/nips/pull/2283)): Adds sort parameters to NIP-50 search queries, including top, hot, zaps, and new. This would let clients request ranked results from relays that support full-text search instead of sorting client-side.

- **NIP-A5: WASM Programs** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): Proposes a convention for publishing and discovering WebAssembly programs on Nostr. WASM binaries could be distributed as Nostr events, with relays serving as a discovery layer for portable executable code.

- **NIP-CF: Combine Forces interoperable napps** ([PR #2277](https://github.com/nostr-protocol/nips/pull/2277)): Defines a convention for interoperable Nostr applications ("napps") that can compose functionality across different clients and services.

- **Snapshots NIP** ([PR #2279](https://github.com/nostr-protocol/nips/pull/2279)): Proposes a mechanism for relay state snapshots, for relay synchronization and backup.

- **Checkpoints NIP** ([PR #2278](https://github.com/nostr-protocol/nips/pull/2278)): Proposes checkpoint events for marking known-good relay state, complementing the snapshots proposal.

- **[NIP-58](/en/topics/nip-58/) (Badges): Badge Sets refactor** ([PR #2276](https://github.com/nostr-protocol/nips/pull/2276)): Restructures how badge collections are organized and referenced.

- **[NIP-11](/en/topics/nip-11/) (Relay Information Document): Extensions** ([PR #2280](https://github.com/nostr-protocol/nips/pull/2280)): Adds additional fields to the relay information document for richer machine-readable relay metadata.

## Five Years of Nostr Marches

[Last month's newsletter](/en/newsletters/2026-03-04-newsletter/#five-years-of-nostr-februaries) covered how Nostr's Februaries progressed from the NIP-01 (Basic Protocol Flow) rewrite through the Damus App Store wave to mesh networking and agent proposals. This retrospective traces what happened each March from 2021 through 2026.

### March 2021: Two Commits

Four months into its existence, Nostr's March produced exactly two commits to the protocol repository, both on March 4. fiatjaf [added links to nostwitter instances](https://github.com/nostr-protocol/nostr/commit/dcd8cc3), pointing early visitors to working deployments, and [added kind to the basic filter definition](https://github.com/nostr-protocol/nostr/commit/54dfb46). That second commit is revealing: in March 2021, you could not yet filter Nostr events by kind. The protocol was that primitive. Two or three relays served the network. The Telegram group was the sole coordination channel. The NIPs repository did not exist yet; protocol proposals lived as files in the main nostr repo. fiatjaf was the only committer that month. The entire March 2021 output of what would become a protocol supporting VPNs, multiplayer games, and mesh networking five years later fits in a single git diff.

### March 2022: Pre-Damus Building

The main protocol repository received zero commits in March 2022. Development had shifted entirely to tool repositories. [Branle](https://github.com/fiatjaf/branle), fiatjaf's Vue.js web client and at the time the primary Nostr interface, received 5 commits including Docker deployment support and [NIP-05](/en/topics/nip-05/) (DNS-Based Verification) display name fixes that removed the `_@` prefix from verification badges. Robert C. Martin's [more-speech](https://github.com/unclebob/more-speech), the Clojure desktop client, logged 13 or more commits adding threading, keyboard navigation, and an edit window. The most famous software author actively building on Nostr that month was not a crypto developer but the person whose "Clean Code" has sold millions of copies, writing a Nostr client in Clojure, a language choice that tells you everything about the early community: these were opinionated programmers building for themselves.

The relay network had expanded to roughly 15 relays with an active user base in the hundreds. Damus did not exist yet and would not be created until April 2022. Nostream also had not appeared. The month's work was infrastructure: making the existing tools more reliable for the small community that was already using them daily.

### March 2023: Post-Explosion Infrastructure

One month after the Damus App Store wave and the surge past 300,000 public keys, March 2023 was about absorbing the growth. The [NIPs repository](https://github.com/nostr-protocol/nips) merged 28 pull requests, the second-highest monthly count in protocol history. [NIP-51](/en/topics/nip-51/) (Lists) merged, giving clients structured follow, mute, and bookmark collections. [NIP-39](/en/topics/nip-39/) (External Identities in Profiles) landed, NIP-78 (Application-Specific Data) provided a general-purpose storage kind for apps that needed private state, and a rewrite of [NIP-57](/en/topics/nip-57/) (Lightning Zaps) ([PR #392](https://github.com/nostr-protocol/nips/pull/392)) consolidated the zap flow and clarified terminology. The most-discussed PR of the month was an alternative mention handling proposal ([PR #381](https://github.com/nostr-protocol/nips/pull/381)) with over 50 comments.

The most consequential new project was [NDK](https://github.com/nostr-dev-kit/ndk) (Nostr Development Kit), the TypeScript library for relay connections, event signing, caching, and subscription management. pablof7z made the [initial commit](https://github.com/nostr-dev-kit/ndk/commit/09e5e03) on March 16, 2023, then rewrote it from scratch 11 days later on March 27 ("basically another initial commit"), and had LNURL and zap support working by March 31. NDK went from nothing to zap-capable in 15 days. Five days after NDK's creation, on March 21, the Alby team created [NWC](https://github.com/getAlby/nostr-wallet-connect) (Nostr Wallet Connect), the reference implementation of [NIP-47](/en/topics/nip-47/) that connected Lightning wallets to Nostr applications. The two projects that would underpin the next three years of web-based Nostr development were born in the same 30-day window. OpenSats had not yet launched its Nostr fund; the first wave would not come until [July 2023](https://opensats.org/blog/nostr-grants-july-2023), four months after NDK's creation.

Other notable creations that month included NostrGit, NostrChat, a nostr-signing-device project by LNbits, and nostrmo. [Gossip](https://github.com/mikedilger/gossip), the Rust desktop client focused on intelligent relay selection, shipped three releases. The protocol was in build mode, and the tools created in March 2023 are still in use three years later.

### March 2024: Protocol Maturation

March 2024 was about hardening the protocol for long-term use. The NIPs repository merged 12 pull requests. The most significant was [NIP-34](/en/topics/nip-34/) (Git Stuff), [PR #997](https://github.com/nostr-protocol/nips/pull/997), which merged on March 5 after over 130 comments and 44 days of review. The discussion thread is a time capsule of the community debating how to build a decentralized GitHub. jb55 drew parallels to `git send-email`, Giszmo proposed using root commit hashes for cross-fork discovery ("something GitHub doesn't do and we could"), mikedilger suggested [NIP-98](/en/topics/nip-98/) (HTTP Auth) event-signed authentication instead of SSH keys, and fiatjaf bluntly dismissed the need for version-control generality: "not for each version control system, just for git. No one uses the others." Within hours of opening the PR, fiatjaf had already switched nak, go-nostr, and gitstr to accept patches over Nostr. DanConwayDev, whose ngit was already an OpenSats grantee, was among the most active contributors to the discussion. A bot field for profile metadata also merged, giving clients a machine-readable way to distinguish automated accounts from human ones.

[Amethyst](https://github.com/vitorpamplona/amethyst) shipped v0.85.0 with git event support, wiki articles, medical data rendering, and content editing in a single release. [Mostro](https://github.com/MostroP2P/mostro) reached v0.10.0. [Nosflare](https://github.com/Spl0itable/nosflare), a serverless Nostr relay running on Cloudflare Workers, proved that relay logic could run at the edge. OpenSats issued a [Long-Term Support grant to Bruno Garcia](https://opensats.org/blog/long-term-support-for-bruno-garcia) for sustained contributions to the Amethyst client.

### March 2025: Infrastructure Expansion

March 2025 produced 10 merged NIPs. The headline was [NIP-66](/en/topics/nip-66/) (Relay Discovery and Liveness Monitoring), [PR #230](https://github.com/nostr-protocol/nips/pull/230), which merged on March 3 after a 25-month journey. dskvr first proposed relay monitoring in February 2023, was told it could be done client-side, explained why connecting to thousands of relays at once was impractical for individual clients, went through seven complete drafts, built monitoring nodes across eight geographic regions (Northeast US, Brazil, US-West, US-East, Australia, India, Korea, South Africa), and waited for the relay tooling to catch up. By the time it merged, implementations already existed in nostr.watch, relaypag.es, monitorlizard, Snort, noStrudel, and Jumble. The NIP-66 data would later fuel the Nostrability outbox benchmarks [covered in Newsletter #12](/en/newsletters/2026-03-04-newsletter/#outbox-model-under-the-microscope). NIP-C0 (Code Snippets) also merged ([PR #1852](https://github.com/nostr-protocol/nips/pull/1852), 63 comments), adding kind 1337 events for sharing source code.

The first MCP servers for Nostr appeared this month. [nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server) appeared on March 23 and [nwc-mcp-server](https://github.com/getAlby/nwc-mcp-server) on March 14, just four months after Anthropic announced the Model Context Protocol in November 2024. These early bridges preceded the full [ContextVM](/en/topics/contextvm/) SDK and the agent commerce work that followed in late 2025 and early 2026.

[Gossip](https://github.com/mikedilger/gossip) shipped v0.14.0. [Coracle](https://github.com/coracle-social/coracle), hodlbod's web client with relay-aware feed management, shipped three releases. OpenSats announced its [tenth wave of Nostr grants](https://opensats.org/blog/tenth-wave-of-nostr-grants), continuing the funding pipeline that had been running since mid-2023.

### March 2026: Convergence

*March 2026 activity is drawn from Nostr Compass issues [#12](/en/newsletters/2026-03-04-newsletter/) through [#15](#) (this issue).*

March 2026 is the month where disparate threads converged into working systems. The [Marmot Development Kit](/en/newsletters/2026-03-04-newsletter/#marmot-development-kit-ships-first-public-release) shipped its first public release with encrypted media, multi-language bindings, and a ChaCha20-Poly1305 migration that required coordinated updates across spec, Rust, and TypeScript. [Shopstr and Milk Market](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces) added MCP commerce surfaces for agent-driven purchasing. [NIP-42](/en/topics/nip-42/) relay auth landed simultaneously in [Amber](/en/newsletters/2026-03-11-newsletter/#nip-42-relay-auth-across-bunker-signer-and-relay), strfry, and OAuth Bunker, closing the loop between signer, relay, and bunker software. [Notedeck](/en/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr) shipped Nostr-native software updates using [NIP-94](/en/topics/nip-94/) (File Metadata) release events.

This week, [BigBrotr](#bigbrotr-maps-exposed-private-keys-across-the-relay-network) scanned the full relay network for leaked private keys and published both the analysis and a DVM checker. [Nostr VPN](#nostr-vpn-launches-as-a-tailscale-alternative) proved that Nostr's key model works for network infrastructure, not only social media. [DOOM](#open-source-doom-runs-peer-to-peer-over-nostr) demonstrated that Nostr discovery, Marmot encryption, and QUIC transport can run a real-time multiplayer game. [Amber](#amber-v500-and-v501) jumped to v5.0.0. [Wisp](#wisp-ships-16-releases-in-one-week) shipped 16 releases in seven days. Twenty-five or more tagged releases came from major projects in a single week.

Seven NIPs merged in the first 24 days of the month. The protocol added [NIP-54](/en/topics/nip-54/) (Wiki) Djot markup, [NIP-19](/en/topics/nip-19/) (Bech32-Encoded Entities) input limits, [NIP-91](/en/topics/nip-91/) (AND Operator for Filters) boolean query logic, and [NIP-85](/en/topics/nip-85/) (Trusted Assertions) Web of Trust assertions. Open proposals ranged from autonomous agents (NIP-AA) to WASM programs (NIP-A5) to search sort extensions for [NIP-50](/en/topics/nip-50/).

### Looking Ahead

Five Marches of Nostr trace a clear arc. In 2021, one person made two commits to a protocol that could not yet filter events by kind. By 2023, NDK and NWC were born five days apart to absorb the post-Damus explosion. By 2024, a 141-comment PR thread debated how git collaboration should work on a social protocol. By 2025, a relay monitoring spec that had been patiently rewritten seven times over 25 months finally merged. In 2026, someone got annoyed by Tailscale requiring an account and built a VPN using Nostr keypairs, while someone else shipped multiplayer DOOM that discovers peers through Nostr relays and encrypts gameplay through Marmot. BigBrotr's scan of 41 million events across 1,085 relays gives a concrete measure of how far the network has grown. The protocol's surface area in March 2026 would have been unrecognizable to March 2021, but the underlying model, events signed by secp256k1 keys and distributed through relays, has not changed.

---

That's it for this week. Building something or have news to share? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Reach out via [NIP-17](/en/topics/nip-17/) (Private Direct Messages) DM</a> or find us on Nostr.
