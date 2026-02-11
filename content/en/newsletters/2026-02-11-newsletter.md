---
title: 'Nostr Compass #9'
date: 2026-02-11
publishDate: 2026-02-11
draft: false
type: newsletters
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** Mostro ships its first public beta after three years of development, bringing P2P Bitcoin trading to mobile via Nostr. OpenSats awards its sixteenth wave of Bitcoin grants, with Minibits Wallet receiving a renewal for its Nostr-integrated Cashu wallet. **Zapstore reaches 1.0 stable release**, marking the maturation of the decentralized Android app store. Coracle 0.6.29 adds topics and highlight commenting. Igloo Desktop v1.0.3 ships major security hardening for Frostr threshold signing. Amber v4.1.2-pre1 migrates to Flow architecture. Angor reaches v0.2.5 with a revamped funding UI and NIP-96 image server configuration. NostrPress launches as a tool that converts Nostr profiles into static blogs. Antiprimal ships a standards-compliant gateway that bridges Primal's proprietary cache server to standard Nostr NIPs. Primal Android merges 18 PRs expanding NWC infrastructure with dual wallet support, audit logging, and the `lookup_invoice` method. diVine ships API-first video feeds. The Marmot TypeScript SDK spins out its reference chat app into a standalone repo and begins migrating to ts-mls v2. The NIPs repository merges HyperLogLog approximate counting for NIP-45 and extracts identity tags from kind 0. A wave of proposals from vitorpamplona begins systematically slimming kind 0 metadata events. New protocol proposals include Nostr Relay Connect for NAT traversal and Nostr Web Tokens for signed web claims. This week's deep dives cover NIP-45's new HyperLogLog approximate counting for cross-relay event metrics and NIP-96's HTTP file storage protocol, now deprecated in favor of Blossom, as projects navigate the transition between the two media standards.

## News

### Mostro Ships First Public Beta

[Mostro](https://github.com/MostroP2P/mostro), the peer-to-peer Bitcoin exchange built on Nostr, released its [mobile app v1.1.0](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0), the project's first public beta after three years of development. The app enables users to trade Bitcoin directly using Nostr for order coordination, with Lightning for settlement and no custodial intermediary.

The release introduces push notifications with improved background reliability on Android, an optional logging system that lets users capture and share diagnostic data when issues arise, smoother relay updates using additive initialization, and Phase 2 UI refinements with internationalization support. The app is available on [Zapstore](https://zapstore.dev) and as a direct [GitHub download](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0).

Mostro joins Shopstr and Plebeian Market as a Nostr-native commerce application, with the distinction that it focuses on fiat-to-Bitcoin exchange coordination. The underlying [Mostro daemon](https://github.com/MostroP2P/mostro) handles order matching and dispute resolution through Nostr relays.

### OpenSats Sixteenth Wave of Bitcoin Grants

[OpenSats](https://opensats.org/blog/sixteenth-wave-of-bitcoin-grants) announced grants to 17 open-source projects. The Nostr-relevant highlight: [Minibits Wallet](https://github.com/minibits-cash/minibits_wallet), the Android [Cashu](/en/topics/cashu/) wallet with [NIP-60](/en/topics/nip-60/) wallet event support and nutzap integration, received a renewal grant. Minibits uses Nostr events to store ecash token state, making wallet backups portable across devices through relay sync.

### NostrPress: Nostr Profile to Static Blog

[NostrPress](https://github.com/besoeasy/NostrPress) ([blog.besoeasy.com](https://blog.besoeasy.com)) is a new tool that converts a Nostr profile into a fully static blog deployable anywhere. Users publish articles on Nostr through any client, and NostrPress generates a standalone website from those events, complete with local media hosting and RSS feeds.

Built with Nunjucks templating and JavaScript, NostrPress produces sites with zero platform lock-in. The generated output is plain HTML/CSS that can be hosted on any static file server, GitHub Pages, Netlify, or a personal VPS. The tool joins [Npub.pro](https://github.com/nostrband/nostrsite) and [Servus](https://github.com/servus-social/servus) as options for turning Nostr content into traditional websites.

### Antiprimal: Standards-Compliant Gateway to Primal's Cache

[antiprimal](https://gitlab.com/soapbox-pub/antiprimal) ([antiprimal.net](https://antiprimal.net)), a new project from Alex Gleason and the Soapbox team, is a WebSocket gateway that bridges Primal's proprietary cache server to standard Nostr protocol messages. Primal offers features like event statistics, content search, and Web of Trust calculations through `wss://cache.primal.net/v1`, but accessing these requires a proprietary message format with a non-standard `cache` field that standard Nostr clients cannot use. Antiprimal translates standard NIP requests into Primal's format and converts responses back.

The gateway supports [NIP-45](/en/topics/nip-45/) COUNT queries (reactions, replies, reposts, zap counts, follower counts), [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md) search, [NIP-11](/en/topics/nip-11/) relay information, and [NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) Trusted Assertions for Primal's precomputed Web of Trust data. A companion bot publishes NIP-85 kind 30382 (user statistics) and kind 30383 (event engagement) events to configurable relays. The project is built with TypeScript on Bun and uses the Nostrify library. Created February 6, it has 53 commits in its first three days of development and is live at antiprimal.net.

### Ikaros: AI Agent Messaging Gateway for Signal and Nostr

[Ikaros](https://gitlab.com/soapbox-pub/ikaros), a new project from the Soapbox team, is a messaging gateway that enables AI agents to communicate through both Signal and Nostr encrypted DMs. The bridge uses the [Agent Client Protocol](https://agentclientprotocol.org) (ACP) to connect any ACP-compatible AI coding assistant to real messaging networks. Three pull requests constitute the project's initial build this week.

[PR #1](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/1) implements a complete [NIP-04](/en/topics/nip-04/) encrypted DM adapter with send/receive support, response buffering with explicit flush on completion, `nsec` and hex private key formats, multi-relay publishing with automatic reconnection, and an interactive setup wizard. The adapter uses nostr-tools v2.23.0 and updates the ACP SDK to v0.14.1.

[PR #2](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/2) fixes a silent message drop caused by a session update race condition: incoming notifications that arrived before a session was registered in the map were silently lost, and the fix buffers those notifications for replay once registration completes. [PR #3](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/3) adds Signal user and group name/UUID metadata to agent interactions, so the AI agent knows who it is talking to and in which group. The project opens a new design space: AI agents addressable via Nostr DMs that can also be reached from Signal, or vice versa.

### Kind 0 Slimming Campaign

vitorpamplona opened a series of PRs this week proposing systematic extraction of data from kind 0 (user metadata) events into dedicated event kinds. The campaign addresses a growing problem: kind 0 events have accumulated fields over time that most clients do not use, inflating the size of every profile fetch.

[PR #2216](https://github.com/nostr-protocol/nips/pull/2216) (merged) moves identity tags (`i` tags) from kind 0 to a new kind 10011, since adoption of these tags has been minimal. [PR #2213](https://github.com/nostr-protocol/nips/pull/2213) proposes moving [NIP-05](/en/topics/nip-05/) verification to kind 10008, which would enable users to have multiple NIP-05 identifiers and allow filtering events by NIP-05 address. [PR #2217](https://github.com/nostr-protocol/nips/pull/2217) proposes extracting Lightning addresses (lud06/lud16) to a new kind, stopping all kind 0 users from carrying zap-related fields that only matter to clients with Lightning integration.

The proposals have revived discussion on the broader question of kind 0 structure, including [PR #1770](https://github.com/nostr-protocol/nips/pull/1770), the long-standing proposal to replace stringified JSON in kind 0 content with structured tags.

### NIP-70 Relay Support Critical for Encrypted Messaging Security

The [Marmot](/en/topics/marmot/) protocol's White Noise implementation has [identified a critical gap](https://blog.jgmontoya.com/2026/02/10/nip70-relay-status.html) in relay support for [NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md) (Protected Events) and [NIP-42](/en/topics/nip-42/) (Authentication). Testing revealed that major public relays including Damus, Primal, and nos.lol reject protected events outright with `blocked: event marked as protected` errors instead of initiating the required authentication challenge.

This breaks a key security feature: NIP-70 enables secure deletion of spent MLS KeyPackages, preventing "harvest now, decrypt later" attacks. Without relay support, encrypted messaging protocols cannot protect users from future key compromise. White Noise has disabled NIP-70 by default in response, keeping an optional flag for users with supportive relays.

**Call to action for relay operators:** Implement the complete NIP-42 authentication flow. When receiving protected events, challenge clients to prove ownership, then accept validated writes. Rejecting protected events without authentication breaks protocol security guarantees that encrypted messaging applications depend on.

## Releases

### Coracle 0.6.29

[Coracle](https://github.com/coracle-social/coracle) ([coracle.social](https://coracle.social)), hodlbod's web client, shipped [0.6.29](https://github.com/coracle-social/coracle/releases/tag/0.6.29). The release adds display of topics and comments on kind 9802 highlights. A new list navigation item gives quick access to user-curated lists from the main UI. Under the hood, Coracle upgraded to a new version of Welshman, the shared Nostr library that powers Coracle's relay management and event handling. The default relay list was refreshed, and Glitchtip error tracking was removed from the codebase.

### Igloo Desktop v1.0.3

[Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop), the [FROST](/en/topics/frost/)-based threshold signer and key management application, shipped [v1.0.3](https://github.com/FROSTR-ORG/igloo-desktop/releases/tag/v1.0.3) with extensive security hardening. The release introduces IPC validation, Electron isolation, and SSRF-aware relay checks for defense against server-side request forgery. A new onboarding and share-import flow simplifies key distribution, relay planning now includes normalization and priority merging, and a preload-based Electron API architecture improves the security boundary between the renderer and main process. A signer keep-alive system maintains threshold signing session stability, and recovery UX improvements reduce the friction of key restoration.

### Amber v4.1.2-pre1

[Amber](https://github.com/greenart7c3/Amber), the Android event signer, released [v4.1.2-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.2-pre1) fixing the missing relay trust score display introduced in v4.1.1, resolving JSON parsing issues for non-Nostr encrypt/decrypt requests, and migrating the account model from LiveData to Flow for more predictable state management. The release switches bunker secrets to full UUIDs and upgrades to Gradle plugin 9.

### Mostro Mobile v1.1.0 and Daemon v0.16.1

See the [News section above](#mostro-ships-first-public-beta) for full coverage of the mobile release. On the server side, the [Mostro daemon](https://github.com/MostroP2P/mostro) shipped [v0.16.1](https://github.com/MostroP2P/mostro/releases/tag/v0.16.1), adding automatic publishing of NIP-01 kind 0 metadata on startup ([PR #575](https://github.com/MostroP2P/mostro/pull/575)), so the daemon now announces its identity to the network when it comes online. The release also fixes dev fee calculation documentation ([PR #571](https://github.com/MostroP2P/mostro/pull/571)).

### Angor v0.2.5

[Angor](https://github.com/block-core/angor) ([angor.io](https://angor.io)), the decentralized P2P funding protocol built on Bitcoin and Nostr, shipped [v0.2.5](https://github.com/block-core/angor/releases/tag/v0.2.5) with three merged PRs. [PR #649](https://github.com/block-core/angor/pull/649) redesigns the Funds management section (V2), replacing the previous layout with a new interface for tracking individual UTXOs and investment positions. [PR #651](https://github.com/block-core/angor/pull/651) overhauls the InvoiceView with updated button styles, closeable dialogs, a new "Copy Address" command, cancellation support for address monitoring, and improved investment flow handling. [PR #652](https://github.com/block-core/angor/pull/652) adds configurable [NIP-96](/en/topics/nip-96/) ([spec](https://github.com/nostr-protocol/nips/blob/master/96.md)) image servers in settings, letting users choose which media upload endpoint handles their project images and documentation. [v0.2.4](https://github.com/block-core/angor/releases/tag/v0.2.4) shipped the previous week.

### Ridestr v0.2.2 and v0.2.3

[Ridestr](https://github.com/variablefate/ridestr), the decentralized rideshare platform [covered last week](/en/newsletters/2026-02-04-newsletter/#ridestr-v020-roadflare-release), continued rapid iteration with [v0.2.2](https://github.com/variablefate/ridestr/releases/tag/v0.2.2) (Bridge Payment Hotfix) and [v0.2.3](https://github.com/variablefate/ridestr/releases/tag/v0.2.3) following the v0.2.0 "RoadFlare Release." The v0.2.2 hotfix addresses a bug where cross-mint [Cashu](/en/topics/cashu/) bridge payments were auto-canceling rides while the payment was still processing or would eventually succeed, preventing premature ride cancellation on slower settlements. The release also fixes UI flickering and broken touch-hitboxes on the "my location" button. v0.2.3 ships additional bug fixes. Both releases include separate APKs for Ridestr (rider app) and Drivestr (driver app).

### Nostr PHP 1.9.4

[Nostr PHP](https://github.com/nostrver-se/nostr-php) ([nostr-php.dev](https://nostr-php.dev)), the PHP helper library for the Nostr protocol, shipped [1.9.4](https://github.com/nostrver-se/nostr-php/releases/tag/1.9.4) adding a configurable `timeout` property to the request class ([PR #106](https://github.com/nostrver-se/nostr-php/pull/106)). This lets developers set custom timeout durations for relay connections and message requests, preventing indefinite hangs when a relay is unresponsive or slow to reply.

### ZSP v0.3.1

[ZSP](https://github.com/zapstore/zsp), the Go CLI tool from the [Zapstore](https://github.com/zapstore/zapstore) team that replaces Zapstore's previous publishing tooling for signing and uploading Android apps to Nostr relays, released [v0.3.1](https://github.com/zapstore/zsp/releases/tag/v0.3.1). ZSP handles APK acquisition from GitHub, GitLab, Codeberg, F-Droid, or local files, then parses metadata, signs Nostr events (via private key, [NIP-46](/en/topics/nip-46/) bunker, or [NIP-07](/en/topics/nip-07/) browser extension), and uploads artifacts to [Blossom](/en/topics/blossom/) servers. This release adds a full offline mode for keystore linking without a network connection, `Content-Digest` headers on Blossom uploads for protocol compliance, fixed arm64-v8a APK detection from F-Droid repositories, GitLab trailing query parameter fixes, and full `.env` file support for configuration.

### Damus iOS 1.17

[Damus](https://github.com/damus-io/damus), the iOS Nostr client, bumped to version 1.17 ([PR #3606](https://github.com/damus-io/damus/pull/3606)). The release fixes a RelayPool issue where connections would close after ephemeral lease release ([PR #3605](https://github.com/damus-io/damus/pull/3605)), which could cause subscriptions to drop unexpectedly. It also resolves a bug where the favorites timeline would not display events when switching between tabs ([PR #3603](https://github.com/damus-io/damus/pull/3603)).

### nak v0.18.3

[nak](https://github.com/fiatjaf/nak), the Nostr army knife CLI, shipped [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3) with three stability fixes: preventing a panic when AUTH challenge tags are nil or too short, checking dateparser errors before using the parsed value, and handling Cashu mint URLs that lack a `://` separator.

### Mi: Browser-Based Local Relay

[Mi](https://git.shakespeare.diy/npub1scvyzz02ayma34hesz62pdrd5nhsmxp74hjq8msmfs9khh3r3drsnw68d8/mi.git) ([mi.shakespeare.wtf](https://mi.shakespeare.wtf)), a new [Shakespeare](https://shakespeare.wtf) MiniApp, is a browser-based local relay that archives a user's Nostr events in IndexedDB. Mi fetches profiles (kind 0), contact lists (kind 3), relay lists (kind 10002), and wallet events from connected relays and stores them locally, giving users offline access to their own data. Built with React and nostr-tools 2.15.0.

### Agora v1.0.2

[Agora](https://gitlab.com/soapbox-pub/agora) ([agora.spot](https://agora.spot)), a decentralized activism and fundraising platform from the Soapbox team, shipped [v1.0.2](https://gitlab.com/soapbox-pub/agora/-/releases/v1.0.2) with an Android APK available for direct install. This is the first Compass mention of Agora, which launched on January 17 with a mission statement: "Join the global movement for freedom. Send support to activists on the ground internationally and take part in local actions."

The platform centers on a world map where users browse by country, create location-tagged "actions" (protests, campaigns, community organizing), and discuss them through threaded comments. All content propagates through Nostr relays, so no central server can be taken offline to silence coordination. Agora supports multiple languages with CI-enforced translation parity, integrates [Blossom](/en/topics/blossom/) media servers for uploads, and includes search, hashtag browsing with global/regional toggle, user profiles, and reaction systems. The v1.0.2 release is the current Android build, available as a direct APK download.

### xonos v0.1.6

[xonos](https://codeberg.org/xonos/xonos), the experimental 3D Nostr client built with the Bevy game engine, shipped [v0.1.6](https://codeberg.org/xonos/xonos/releases/tag/v0.1.6). xonos renders Nostr events in a 3D spatial environment with text-to-speech capabilities, exploring how social protocol data might work outside of conventional 2D interfaces.

### Zapstore v1.0.0

[Zapstore](https://github.com/zapstore/zapstore/releases/tag/1.0.0) ([zapstore.dev](https://zapstore.dev)), the permissionless Android app store built on Nostr, **reached its stable 1.0 release milestone** this week after months of release candidates.

The 1.0 release includes critical stability improvements: install button state handling that ensures Delete appears immediately after installation completes, user-friendly error messages with expandable technical details, and a "Report issue" button that sends encrypted DMs via Nostr using ephemeral keys. The release also ships a new updates screen with polling and batch tracking, better download watchdog for stalled transfers, dynamic concurrent download limits based on device performance, more frequent installed package syncing, and improved version comparison logic. The team fixed a critical flutter_secure_storage issue and enhanced package manager handling of edge cases.

This milestone represents the maturation of Nostr's first dedicated app distribution platform, enabling developers to publish Android applications directly to users without centralized app store gatekeeping.

## Project Updates

### Primal Android Expands NWC Infrastructure

[Primal Android](https://github.com/PrimalHQ/primal-android-app) merged 18 PRs this week, continuing the NWC buildout [started last week](/en/newsletters/2026-02-04-newsletter/#primal-android-ships-nwc-encryption). [PR #883](https://github.com/PrimalHQ/primal-android-app/pull/883) adds support for NWC connections across both wallets (Spark and external), and [PR #879](https://github.com/PrimalHQ/primal-android-app/pull/879) implements the `lookup_invoice` NWC method for checking payment status.

[PR #880](https://github.com/PrimalHQ/primal-android-app/pull/880) adds NWC request-response audit logging for debugging wallet interactions. [PR #877](https://github.com/PrimalHQ/primal-android-app/pull/877) adds multi-account support to `PrimalNwcService`, enabling users with multiple profiles to maintain separate wallet connections. [PR #882](https://github.com/PrimalHQ/primal-android-app/pull/882) implements periodic cleanup of expired budget holds, preventing stale payment reservations from blocking wallet operations.

UI work includes wallet upgrade screen redesigns ([PR #889](https://github.com/PrimalHQ/primal-android-app/pull/889)), a wallet upgrade FAQ ([PR #885](https://github.com/PrimalHQ/primal-android-app/pull/885)), Lightning address setting during onboarding ([PR #888](https://github.com/PrimalHQ/primal-android-app/pull/888)), and a fix for zap transactions appearing as regular payments for non-Lightning types ([PR #887](https://github.com/PrimalHQ/primal-android-app/pull/887)).

### diVine Ships API-First Video Feeds

[diVine](https://github.com/divinevideo/divine-mobile), the short-form video client, merged 19 PRs this week, shifting toward an API-first architecture. [PR #1468](https://github.com/divinevideo/divine-mobile/pull/1468) introduces API-first video feeds, and [PR #1466](https://github.com/divinevideo/divine-mobile/pull/1466) adds trending, recent, and home API endpoints. [PR #1433](https://github.com/divinevideo/divine-mobile/pull/1433) indexes specific video controllers for efficient feed rendering.

Profile handling improved with [PR #1440](https://github.com/divinevideo/divine-mobile/pull/1440) implementing a cache-plus-fresh pattern for viewing other profiles, reducing load times while ensuring data freshness. The team also shipped notification fixes ([PR #1437](https://github.com/divinevideo/divine-mobile/pull/1437)), comment flow refactoring ([PR #1431](https://github.com/divinevideo/divine-mobile/pull/1431)), and tab swiping on the Notifications screen ([PR #1388](https://github.com/divinevideo/divine-mobile/pull/1388)).

### White Noise: Keyring Unification and User Search

The [White Noise](https://github.com/marmot-protocol/whitenoise-rs) backend for the [Marmot](/en/topics/marmot/) protocol merged 4 PRs this week. Two PRs improved keyring handling: [PR #468](https://github.com/marmot-protocol/whitenoise-rs/pull/468) makes the keyring service identifier configurable via `WhitenoiseConfig`, and [PR #475](https://github.com/marmot-protocol/whitenoise-rs/pull/475) unifies the implementation on a single `keyring-core` crate with platform-native stores, replacing fragmented platform-specific code. Separately, [PR #470](https://github.com/marmot-protocol/whitenoise-rs/pull/470) adds user search functionality.

### Marmot TS Extracts Reference Chat App

The [Marmot](/en/topics/marmot/) TypeScript SDK ([marmot-ts](https://github.com/marmot-protocol/marmot-ts)) merged [PR #40](https://github.com/marmot-protocol/marmot-ts/pull/40), removing the built-in reference chat application and spinning it out into a standalone repo: [marmots-web-chat](https://github.com/marmot-protocol/marmots-web-chat). The new repo, created February 6, is a reference implementation of the Marmot TypeScript SDK with its own CI pipeline, tabbed chat view, and independent build system. The separation lets the SDK focus on library concerns while the chat app iterates on UX independently.

An open PR ([#41](https://github.com/marmot-protocol/marmot-ts/pull/41)) migrates marmot-ts to ts-mls v2.0.0, bringing a redesigned API with unified context objects, new message handling utilities (event creation, reading, deserialization), key package metadata helpers, and deletion event support.

### Alby Hub Updates

[Alby Hub](https://github.com/getAlby/hub) merged 5 PRs this week. [PR #2049](https://github.com/getAlby/hub/pull/2049) adds an Alby CLI to the app store interface. [PR #2033](https://github.com/getAlby/hub/pull/2033) fixes handling of invalid zap data in the transaction list, and [PR #2046](https://github.com/getAlby/hub/pull/2046) removes the unused `ListTransactions` method from the LNClient interface.

### Notedeck Ships Dashboard and Agentium

[Notedeck](https://github.com/damus-io/notedeck), the cross-platform Nostr client from Damus, merged 6 PRs this week. [PR #1247](https://github.com/damus-io/notedeck/pull/1247) adds an initial dashboard app. [PR #1293](https://github.com/damus-io/notedeck/pull/1293) introduces Agentium, a multi-agent development environment that transforms the Dave AI assistant into a system with dual AI modes and scene-based agent management. [PR #1276](https://github.com/damus-io/notedeck/pull/1276) adds a multiline message composer with Signal-style keybindings, and [PR #1278](https://github.com/damus-io/notedeck/pull/1278) delivers media performance improvements. Open PRs of note include [outbox infrastructure](https://github.com/damus-io/notedeck/pull/1288) and [NIP-34](/en/topics/nip-34/) [Git App planning](https://github.com/damus-io/notedeck/pull/1289).

### Agora Ships Major UI Overhaul

[Agora](https://gitlab.com/soapbox-pub/agora) merged 7 PRs this week alongside its v1.0.2 release. [PR #106](https://gitlab.com/soapbox-pub/agora/-/merge_requests/106) is the largest, closing 11 UI tasks across settings, profile editing, map interactions, search results, comment filtering, and Blossom server management. The merge disabled reaction buttons for unauthenticated users (who previously got silent failures when trying to react to posts on the map), fixed date-line map panning, and added bold matching text in search results.

[PR #108](https://gitlab.com/soapbox-pub/agora/-/merge_requests/108) adds comment counts under feed posts and on thread pages. [PR #107](https://gitlab.com/soapbox-pub/agora/-/merge_requests/107) adds automatic retry on event load failures with an explicit reload button when retries exhaust. [PR #104](https://gitlab.com/soapbox-pub/agora/-/merge_requests/104) changes hashtag browsing to default to a global scope, since the previous country-scoped default often returned zero results.

[PR #109](https://gitlab.com/soapbox-pub/agora/-/merge_requests/109) adds a CI step that checks translation parity across all languages, failing the build if any key is missing a value. [PR #110](https://gitlab.com/soapbox-pub/agora/-/merge_requests/110) clips large notes in feeds to preserve scroll rhythm, and [PR #111](https://gitlab.com/soapbox-pub/agora/-/merge_requests/111) fixes an iOS mobile zoom issue when commenting on actions caused by small font sizes.

### Clawstr Ships CLI and Lightning Zap Buttons

[Clawstr](https://gitlab.com/soapbox-pub/clawstr), the Reddit-inspired platform where AI agents create and manage communities on Nostr, merged 3 PRs this week. [PR #11](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/11) replaces all manual nak commands in the AI agent skill definitions with the new `@clawstr/cli` package (`npx -y @clawstr/cli@latest`), removing manual JSON event construction in favor of CLI commands and adding wallet operations (init, balance, zap, npc) and [NIP-50](/en/topics/nip-50/) full-text search.

[PR #13](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/13) adds a "For Humans" documentation page and a `ProfileZapDialog` component. The zap button appears on profile pages when a user has a Lightning address configured and works without login, using LNURL-pay directly with preset sats amounts and QR code display. [PR #12](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/12) documents the `wallet sync` command, explaining how payments to Lightning addresses are held by NPC until agents explicitly sync their wallets.

## NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-45: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)** - [NIP-45 (Event Counting)](/en/topics/nip-45/) now supports HyperLogLog (HLL) approximate counting. Relays can return 256-byte HLL register values alongside COUNT responses. Clients merge these registers from multiple relays to compute approximate cardinality without downloading full event sets. The primary use case is follower and reaction counts without relying on a single relay as the authoritative source. Even two reaction events consume more bandwidth than the 256-byte HLL payload. Clients can apply HyperLogLog++ corrections for improved accuracy on small cardinalities.

- **[NIP-39: Identity Tags Moved from Kind 0](https://github.com/nostr-protocol/nips/pull/2216)** - [NIP-39](/en/topics/nip-39/) identity claim tags (`i` tags) have been extracted from kind 0 metadata events to a new dedicated kind 10011. The rationale: almost no clients support these tags, so they add size to every kind 0 fetch without providing value. This is the first in a series of kind 0 extraction PRs from vitorpamplona (see [News section](#kind-0-slimming-campaign)).

**Open PRs and Discussions:**

- **[NIP-XX: Nostr Relay Connect (NRC)](https://github.com/nostr-protocol/nips/pull/2214)** - woikos proposes a protocol for accessing Nostr relays through encrypted tunneling via a public rendezvous relay. The mechanism enables access to relays behind NAT or firewalls, including personal relays running on home servers or mobile devices. The tunneling uses kind 24891/24892 events with [NIP-44](/en/topics/nip-44/) encryption through a rendezvous relay that cannot decrypt the traffic. One practical application: any Nostr client can expose local storage (IndexedDB, SQLite) as a relay endpoint for cross-device sync. Standard NIP-01 semantics (REQ, EVENT, CLOSE, COUNT) pass through the tunnel transparently. Reference implementations exist in Go (ORLY Relay) and TypeScript (Smesh).

- **[Nostr Web Tokens (NWT)](https://github.com/nostr-protocol/nips/pull/2187)** - pippellia-btc proposes Nostr Web Tokens, a Nostr event format for conveying signed claims between web parties, inspired by JSON Web Tokens (JWTs). NWT can represent both [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) (HTTP Auth) and [Blossom authorization events](/en/topics/blossom/), giving clients flexibility in how and how long tokens remain valid. A reference Go library is available. A [video explanation](https://github.com/pippellia-btc/nostr-web-tokens) and [detailed comparison](https://github.com/pippellia-btc/nostr-web-tokens?tab=readme-ov-file#comparisons) with NIP-98 and Blossom Auth are linked in the PR.

- **[NIP-47 Simplification](https://github.com/nostr-protocol/nips/pull/2210)** - rolznz proposes removing the `multi_` methods from [NIP-47 (Nostr Wallet Connect)](/en/topics/nip-47/), which were complex to implement and did not gain adoption. The PR also reduces duplication in encryption and backward compatibility handling, cleaning up the spec after [last week's hold invoice addition](/en/newsletters/2026-02-04-newsletter/#nip-updates).

- **[NIP-05: Move to Own Event Kind](https://github.com/nostr-protocol/nips/pull/2213)** - vitorpamplona proposes moving NIP-05 verification from kind 0 to a new kind 10008, enabling multiple NIP-05 identifiers per user and filtering by NIP-05 address. Part of the kind 0 slimming campaign.

- **[NIP-57: Lightning Addresses from Kind 0](https://github.com/nostr-protocol/nips/pull/2217)** - vitorpamplona proposes extracting lud06/lud16 (Lightning addresses) from kind 0 to a dedicated event kind per [NIP-57](/en/topics/nip-57/), continuing the kind 0 slimming effort.

- **[Profile Hypercustomization](https://github.com/nostr-protocol/nips/pull/2165)** - fiatjaf proposes extended profile customization capabilities beyond what kind 0 currently supports.

## NIP Deep Dive: NIP-45 (Event Counting) and HyperLogLog

[NIP-45](/en/topics/nip-45/) ([spec](https://github.com/nostr-protocol/nips/blob/master/45.md)) defines how clients can ask relays to count events matching a filter without transferring the events themselves. This week's merge of [HyperLogLog support](https://github.com/nostr-protocol/nips/pull/1561) adds a probabilistic data structure that solves a fundamental problem: how to count things across multiple independent relays.

**The Problem:**

Counting events on a single relay is simple: send a COUNT request, get a number back. Counting across the network is harder. If relay A reports 50 reactions and relay B reports 40, the total is not 90 because many events exist on both relays. Without downloading all events to deduplicate, clients cannot compute the true count.

**HyperLogLog:**

HyperLogLog (HLL) is a probabilistic algorithm that estimates the number of distinct elements in a set using a fixed amount of memory. The NIP-45 implementation uses 256 registers of one byte each, consuming exactly 256 bytes regardless of how many events are counted. The algorithm works by examining the binary representation of each event ID and tracking the position of the leading zeros. Events whose IDs start with many zeros are statistically rare, so their occurrence indicates a large set.

**How It Works in NIP-45:**

A relay responding to a COUNT request can include an `hll` field containing base64-encoded register values:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

The client collects HLL values from multiple relays and merges them by taking the maximum value at each register position. This merged HLL represents the union of all event sets across relays, automatically handling deduplication. The final cardinality estimate is computed from the merged registers.

**Accuracy:**

With 256 registers, the standard error is approximately 5.2%. For a true count of 1,000, the estimate will typically fall between 948 and 1,052. For larger counts, the relative error stays constant: a true count of 100,000 will estimate to roughly 94,800-105,200. HyperLogLog++ corrections improve accuracy for small cardinalities (under ~200), where the basic algorithm tends to overestimate.

**Why It Matters:**

Social metrics (follower counts, reaction counts, repost counts) are a core feature of social media clients. Without HLL, clients must either query a single "trusted" relay (centralizing the count) or download all events from all relays (wasting bandwidth). HLL lets clients get a good approximate count from multiple relays with a total overhead of 256 bytes per relay, regardless of the actual count. Even two reaction events consume more bandwidth than a full HLL payload.

The spec fixes the number of registers at 256 for interoperability. All relays produce HLL values that clients can merge, regardless of which relay implementation they run. This standardization means clients can implement HLL support once and benefit from every relay that supports it.

**Current Status:**

The PR was opened by fiatjaf and had been under discussion for several months before merging this week. Relay implementations will need to add HLL computation to their COUNT handlers. Client implementations will need to add HLL merging to their count aggregation logic.

## NIP Deep Dive: NIP-96 (HTTP File Storage) and the Transition to Blossom

[NIP-96](/en/topics/nip-96/) ([spec](https://github.com/nostr-protocol/nips/blob/master/96.md)) defined how Nostr clients upload, download, and manage files on HTTP media servers. Now marked as "unrecommended" in favor of [Blossom](/en/topics/blossom/) (BUD-based media hosting), NIP-96 remains relevant this week because Angor v0.2.5 [added NIP-96 server configuration](#angor-v025) and ZSP v0.3.1 [uploads to Blossom servers](#zsp-v031), illustrating a protocol transition in progress.

**How NIP-96 Works:**

A client discovers a file server's capabilities by fetching `/.well-known/nostr/nip96.json`, which returns the API URL, supported content types, size limits, and available media transformations:

```json
{
  "api_url": "https://file-server.example/api",
  "download_url": "https://cdn.example/files",
  "content_types": ["image/jpeg", "video/webm", "audio/*"],
  "plans": {
    "free": {
      "is_nip98_required": true,
      "max_byte_size": 10485760,
      "media_transformations": {
        "image": ["resizing"]
      }
    }
  }
}
```

To upload, the client sends a `multipart/form-data` POST to the API URL with a [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) authorization header (a signed Nostr event proving the uploader's identity). The server returns a [NIP-94](/en/topics/nip-94/) file metadata structure containing the file URL, original and transformed SHA-256 hashes, MIME type, and dimensions:

```json
{
  "status": "success",
  "nip94_event": {
    "tags": [
      ["url", "https://cdn.example/files/<hash>.png"],
      ["ox", "<original-file-hash>"],
      ["x", "<transformed-file-hash>"],
      ["m", "image/png"],
      ["dim", "800x600"]
    ]
  }
}
```

Downloads use GET requests to `<api_url>/<sha256-hash>`, with optional query parameters for server-side transforms like image resizing (`?w=320`). Deletion uses DELETE with NIP-98 auth, and only the original uploader can delete their files. A file listing endpoint returns paginated results of a user's uploads.

Users publish kind 10096 events to declare their preferred upload servers, letting clients automatically select the right server without manual configuration.

**Why It Was Deprecated:**

NIP-96 tied file URLs to specific servers. If `files.example.com` went down, every Nostr note referencing that server's URLs lost its media. The server was the address, and the address was fragile.

[Blossom](/en/topics/blossom/) (Blobs Stored Simply on Mediaservers) inverts this by making the SHA-256 hash of the file content the canonical identifier. A Blossom URL looks like `https://blossom.example/<sha256>.png`, but any Blossom server hosting the same file serves it at the same hash path. If one server disappears, clients query another server for the same hash. Content addressing makes the data portable across servers by default.

Blossom also simplifies the API. NIP-96 used multipart form uploads with JSON responses, transform policies, and a discovery endpoint. Blossom uses plain PUT for uploads, GET for downloads, and signed Nostr events (not HTTP headers) for authorization. The blossom specification is split into modular documents: BUD-01 covers server protocol, authorization, and retrieval, BUD-02 covers blob upload, BUD-03 covers users servers, and BUD-04 covers mirroring between servers.

The deprecation happened in September 2025 via [PR #2047](https://github.com/nostr-protocol/nips/pull/2047), which marked NIP-96 as "unrecommended" in the NIPs index.

**The Transition in Practice:**

Servers like nostr.build and void.cat supported NIP-96 and have added or migrated to Blossom endpoints. Clients are at various stages: Angor's v0.2.5 release this week added NIP-96 server configuration for project images, while ZSP's v0.3.1 release uploads artifacts exclusively to Blossom servers with `Content-Digest` headers for protocol compliance. Amethyst and Primal support Blossom uploads. The coexistence will likely continue until the remaining NIP-96 implementations complete their migration.

**What Carries Over:**

Kind 10096 server preference events remain useful for Blossom server selection. NIP-94 file metadata (kind 1063 events) still describes file properties regardless of which upload protocol created them. The SHA-256 hashing that NIP-96 used for download URLs became the foundation of Blossom's content addressing. NIP-96's design informed what Blossom simplified: the lesson was that media hosting on a decentralized network requires content-addressed storage to match the censorship resistance of the relay layer.

---

That's it for this week. Building something? Have news to share? Want us to cover your project? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Reach out via NIP-17 DM</a> or find us on Nostr.
