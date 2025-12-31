---
title: 'Nostr Compass #3'
date: 2025-12-31
publishDate: 2025-12-31
draft: false
type: newsletters
---

Welcome back to Nostr Compass, your weekly guide to the Nostr protocol ecosystem.

**This week:** As 2025 closes, we look back at five years of December milestones in Nostr's evolution. From fiatjaf's first client release in December 2020, through Jack Dorsey's pivotal 14 BTC donation in December 2022, to this month's NIP-55 signer proliferation and NDK's 162x cache speedup, December has consistently marked turning points for the protocol. This special issue traces the technical history through each December, documenting the protocol's growth from two experimental relays to 2,500+ nodes across 50 countries. Plus: Amethyst's desktop module takes shape via Quartz, Notedeck gains messaging, Citrine hosts web apps, and NIP-54 fixes internationalization for non-Latin scripts.

## December Recap: Five Years of Nostr Decembers

Nostr turns five this year. fiatjaf initiated the protocol on November 7, 2020, and every December since has marked a distinct phase in its evolution: from proof-of-concept to global movement to production ecosystem. This is a technical retrospective of December 2020 through December 2025, the formative years that established Nostr's foundation and catalyzed its breakout moment.

### December 2020: Genesis

The first full month of Nostr's existence saw fiatjaf release [Branle](https://github.com/fiatjaf/branle), the protocol's first client, built with Quasar (Vue.js) and absurd-sql for local storage. fiatjaf had already established the core architecture: users identified by secp256k1 public keys, all posts cryptographically signed, relays serving as dumb storage that don't communicate with each other. One or two experimental relays served a handful of early adopters coordinating in the Telegram group [@nostr_protocol](https://t.me/nostr_protocol), which had launched November 16. The [original documentation](https://fiatjaf.com/nostr.html) described "the simplest open protocol that is able to create a censorship-resistant global social network," a premise that would take two more years to prove.

### December 2021: Early Development

On December 31, 2021, Nostr hit the [Hacker News front page](https://news.ycombinator.com/item?id=29749061) with 110 points and 138 comments, submitted by Cameri. This marked the protocol's first significant exposure to the broader developer community. The network ran on approximately seven relays with fewer than 1,000 users. Branle received updates including private key import (December 31) and multi-relay support. A command-line client, noscl, provided terminal-based interaction. The protocol specifications existed in fiatjaf's documentation, though the formal [NIPs repository](https://github.com/nostr-protocol/nips) wouldn't be created until May 2022. The protocol was, as fiatjaf described it, "a work in progress."

### December 2022: The Tipping Point

December 2022 transformed Nostr from a niche experiment into a mainstream movement. The catalyst came on December 15, when Jack Dorsey donated [14.17171699 BTC](https://www.coindesk.com/tech/2022/12/15/jack-dorsey-gives-decentralized-social-network-nostr-14-btc-in-funding) (~$245,000-$250,000) to fiatjaf after discovering the protocol and declaring it "100 percent what we wanted from Bluesky, but it wasn't developed from a company." On December 16, fiatjaf announced splitting funds with Damus developer William Casarin (jb55), and Dorsey verified his Nostr account (npub: `npub1sg6plzptd64u62a878hep2kev88swjh3tw00gjsfl8f237lmu63q0uf63m`). The funding legitimized the project overnight.

The same week, Twitter's chaos accelerated adoption. December 14-15 saw suspensions of prominent journalists from the New York Times, CNN, and Washington Post. On December 18, Twitter [announced bans](https://techcrunch.com/2022/12/18/twitter-wont-let-you-post-your-facebook-instagram-and-mastodon-handles/) on accounts promoting Nostr, Mastodon, and other platforms. The policy was reversed the following day after backlash. The exodus drove users to explore alternatives.

Protocol development surged. On December 16, [NIP-19](/en/topics/nip-19/) was merged ([#57](https://github.com/nostr-protocol/nips/pull/57)), introducing bech32-encoded identifiers (npub, nsec, note, nprofile, nevent) that made keys human-readable and distinguishable. The NIPs repository logged 36+ commits that month, including NIP-40 and NIP-07 updates. Clients proliferated: Damus filled its TestFlight beta within hours, Astral forked Branle for profile creation, Snort launched as a "fast, censorship-resistant" web client, and Vitor Pamplona began Amethyst development. Alby v1.22.1 "Kemble's Cascade of Stars" shipped December 22 with NIP-19 support. By December 7, Nostr had approximately 800 users with profiles; when Damus hit the App Store on January 31, 2023, the floodgates opened, driving growth to 315,000+ users by June 2023.

### December 2023: Ecosystem Maturation

December 2023 marked a critical inflection point for Nostr protocol security. On December 20, [NIP-44 revision 3 was merged](https://github.com/nostr-protocol/nips/pull/746) following an independent Cure53 security audit (NOS-01) that identified 10 issues in the TypeScript, Go, and Rust implementations, including timing attacks and forward secrecy concerns. The updated spec replaced the flawed [NIP-04](/en/topics/nip-04/) encryption with ChaCha20 and HMAC-SHA256, establishing the cryptographic foundation that now underpins [NIP-17](/en/topics/nip-17/) private DMs and [NIP-59](/en/topics/nip-59/) gift wrapping. The same week, [OpenSats announced their fourth wave of grants](https://opensats.org/blog/nostr-grants-december-2023) on December 21, funding seven projects including Lume, noStrudel, ZapThreads, and an independent NIP-44 audit. This followed the [first wave in July 2023](https://opensats.org/blog/nostr-grants-july-2023) that had funded Damus, Coracle, Iris, and others, bringing total Nostr Fund allocation to approximately $3.4 million across 39 grants.

The month also exposed sustainability tensions in the ecosystem. On December 28, William Casarin (jb55) [posted on Stacker News](https://stacker.news/items/368863) that 2024 would "likely be the last year of Damus," citing that "nostr clients don't make money" after Apple's restrictions on in-app zaps severely limited revenue potential. The Damus team had previously rejected VC funding. Meanwhile, [Nostr Wallet Connect v0.4.1](https://github.com/getAlby/nostr-wallet-connect/releases/tag/0.4.1) shipped on December 26, extending [NIP-47](/en/topics/nip-47/) with `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance`, and `get_info` methods, laying groundwork for the wallet integrations that would become standard across clients.

### December 2024: Protocol Advancement

December 2024 opened with the [Notedeck Alpha launch](https://damus.io/notedeck/) on November 30, the Damus team's Rust-based desktop client featuring a multi-column interface with multiple account support. Built for Linux, macOS, and Windows (Android planned for 2025), Notedeck initially shipped to Damus Purple subscribers and represented a strategic expansion beyond iOS. Two weeks later, [OpenSats announced their ninth wave of grants](https://opensats.org/blog/9th-wave-of-nostr-grants) on December 16, funding AlgoRelay (the first algorithmic relay for personalized feeds), Pokey (Android app with Bluetooth mesh for restricted internet), Nostr Safebox ([NIP-60](/en/topics/nip-60/) Cashu token storage), and LumiLumi (lightweight accessible web client), pushing total Nostr Fund allocation to approximately $9 million, a 67% year-over-year increase.

The month saw significant client maturation across the ecosystem. [Gossip 0.13.0](https://github.com/mikedilger/gossip/releases/tag/v0.13.0) landed on December 23 with File Metadata ([NIP-92](/en/topics/nip-92/)/[NIP-94](/en/topics/nip-94/)) support, Blossom integration, and [NIP-50](/en/topics/nip-50/) relay search. [Coracle 0.5.0](https://github.com/coracle-social/coracle/releases/tag/0.5.0) shipped December 12 with reworked onboarding and nostr-editor integration. Protocol development remained active with 30 pull requests submitted between December 9-22 (10 merged), including [NIP-46](/en/topics/nip-46/) rewrites to use only NIP-44 encryption and continued work on [NIP-104](/en/topics/nip-104/) for Signal-level double ratchet encryption. Network statistics showed 224,000+ daily trusted pubkey events, 4x year-over-year growth in new profiles with contact lists, and a 50% increase in public writing events.

### December 2025: Ecosystem Expansion

December 2025 brought continued protocol maturation and ecosystem expansion. On December 21, [OpenSats announced their fourteenth wave of Nostr grants](https://opensats.org/blog/fourteenth-wave-of-nostr-grants), funding three projects: YakiHonne (a multi-platform client with creator portal for long-form content and Cashu/Nutzaps payment integration), Quartz (Vitor Pamplona's Kotlin Multiplatform library that powers Amethyst and will enable an iOS version), and Nostr Feedz (RSS-to-Nostr bidirectional integration by PlebOne). Grant renewals went to Dart NDK and Mattn's nostr-relay.

Protocol evolution continued with [NIP-BE](/en/topics/nip-be/) (Bluetooth Low Energy messaging, [#1979](https://github.com/nostr-protocol/nips/pull/1979)) merged in November, enabling offline device synchronization. [NIP-A4](/en/topics/nip-a4/) (Public Messages, kind 24, [#1988](https://github.com/nostr-protocol/nips/pull/1988)) landed later in the month, defining notification-screen messages that use `q` tags to avoid threading complications. [NIP-29](/en/topics/nip-29/) received major clarification ([#2106](https://github.com/nostr-protocol/nips/pull/2106)), introducing the `hidden` tag for truly private, undiscoverable groups. The [NIP-55](/en/topics/nip-55/) spec also saw refinement ([#2166](https://github.com/nostr-protocol/nips/pull/2166)), addressing a common implementation mistake where developers called `get_public_key` from background processes.

On the client side, [Primal Android became a full NIP-55 signer](/en/newsletters/2025-12-24-newsletter/#news) through eight merged PRs implementing `LocalSignerContentProvider`, joining Amber and Aegis as Android signing options. The [NDK library achieved 162x faster cache queries](/en/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes) (from ~3,690ms to ~22ms) by eliminating duplicate writes and unnecessary LRU cache lookups ([PR #371](https://github.com/nostr-dev-kit/ndk/pull/371), [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372)). Shopstr introduced [Zapsnags](/en/newsletters/2025-12-24-newsletter/#news) for flash sales via zaps. White Noise shipped [MIP-05](/en/topics/mip-05/) privacy-preserving push notifications. See [Newsletter #1](/en/newsletters/2025-12-17-newsletter/) and [Newsletter #2](/en/newsletters/2025-12-24-newsletter/) for complete coverage.

---

Five years ago, fiatjaf released Branle to a handful of users across two experimental relays. Today, the protocol supports 140+ clients, 2,500+ relays across 50 countries, and a growing web of trust linking hundreds of thousands of keypairs. December's pattern of major releases continued this month with Bluetooth messaging, Android signer proliferation, and infrastructure grants signaling sustained investment in cross-platform tooling.

## News

**Amethyst Desktop Takes Shape** - The Quartz grant from OpenSats' fourteenth wave is already producing results. [PR #1625](https://github.com/vitorpamplona/amethyst/pull/1625) creates a full `:desktopApp` module for Amethyst using Compose Multiplatform, with login and global feed screens functional on Desktop JVM. The architecture converts the `:commons` module to Kotlin Multiplatform with a clean source set structure (`commonMain`, `jvmAndroid`, `androidMain`, `jvmMain`), enabling shared UI components between Android and desktop while leaving platform-specific decisions to each target. This lays the foundation for the eventual iOS version via the same Kotlin Multiplatform approach.

**Amethyst Voice Replies** - A Christmas delivery from davotoula: [PR #1622](https://github.com/vitorpamplona/amethyst/pull/1622) adds dedicated voice reply screens with waveform visualization, re-record support, media server selection, and upload progress indicators. Users can now reply to both root voice messages and voice replies with audio.

**Notedeck Adds Messaging** - Notedeck, the Damus desktop client, gained a messages feature in [PR #1223](https://github.com/damus-io/notedeck/pull/1223), expanding beyond timeline browsing into direct communication.

**Citrine Hosts Web Apps** - Citrine can now [host web applications](https://github.com/greenart7c3/Citrine/pull/81), turning your phone into a local-first Nostr web server. A separate [PR #85](https://github.com/greenart7c3/Citrine/pull/85) adds automatic reconnection and event broadcasting when network connectivity returns, with comprehensive test coverage across Android API levels.

**Nostrability Developer Toolkit Registry** - The [Developer Kits & Tooling](https://github.com/nostrability/nostrability/issues/264) tracker maintains a curated registry of SDKs, libraries, and developer tools across languages (TypeScript, Rust, Python, Go, Dart, Swift, and more). If you're new to Nostr development, this is a useful starting point for finding the right toolkit for your stack.

## NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

- **[NIP-54](/en/topics/nip-54/)** - Critical internationalization fix for wiki d-tag normalization ([#2177](https://github.com/nostr-protocol/nips/pull/2177)). Previous rules converted all non-ASCII characters to `-`, breaking support for Japanese, Chinese, Arabic, Cyrillic, and other scripts. The updated spec preserves UTF-8 letters, applies lowercase only to characters with case variants, and includes comprehensive examples: `"ウィキペディア"` stays `"ウィキペディア"`, `"Москва"` becomes `"москва"`, and mixed scripts like `"日本語 Article"` normalize to `"日本語-article"`.

## Releases

**Zapstore 1.0-rc1** - The Nostr-based permissionless app store ships the [first release candidate](https://github.com/zapstore/zapstore/releases/tag/1.0-rc1) of its new architecture, featuring a complete UI refresh, rewritten package manager with improved error handling, App Stacks for curated discovery, redesigned profile screens, background update checking, and infinite scrolling in release lists.

**KeyChat v1.38.1** - The MLS-based encrypted messaging app [adds UnifiedPush support](https://github.com/keychat-io/keychat-app/releases/tag/v1.38.1%2B6489) for Android and Linux push notifications, plus biometric authentication for privacy operations. Available for Android, Windows, macOS, and Linux.

**Alby Go v2.0.0** - The mobile Lightning wallet companion [ships a visual redesign](https://github.com/getAlby/go/releases/tag/v2.0.0) with new logo, updated color palette, redesigned address book, and improved amount input keyboard. BTC Map is now accessible from the home screen, and transaction descriptions appear in notifications.

**nak v0.17.4** - fiatjaf's command-line Nostr tool [released](https://github.com/fiatjaf/nak/releases/tag/v0.17.4), following v0.17.3's LMDB Linux restriction fix from last week.

## Notable code and documentation changes

*Open pull requests and early-stage work worth watching.*

### Damus (iOS)

[NIP-19 relay hints](https://github.com/damus-io/damus/pull/3477) implements relay hint consumption for event fetching. When users open nevent, nprofile, or naddr links, Damus now extracts relay hints from the bech32 TLV data and connects to ephemeral relays to fetch content not in the user's relay pool. The implementation includes ref-counted cleanup to prevent race conditions during concurrent lookups. [Image URL detection](https://github.com/damus-io/damus/pull/3474) automatically converts pasted image URLs into preview thumbnails in the composer, with a carousel position badge for multiple images. [npub paste conversion](https://github.com/damus-io/damus/pull/3473) transforms pasted npub/nprofile strings into mention links with async profile resolution.

### Amethyst (Android)

[Payment targets](https://github.com/vitorpamplona/amethyst/pull/1627) adds an event interface for NIP-57 zap splits, allowing posts to specify multiple recipients who share incoming zaps (useful for collaborations, revenue sharing, or tipping both content creators and the tools they use). [Quartz feature parity documentation](https://github.com/vitorpamplona/amethyst/pull/1624) adds a detailed table tracking which features are implemented across Android, Desktop JVM, and iOS targets, noting that iOS is missing core cryptography (`Secp256k1Instance`), JSON serialization, and data structures.

### Notedeck (Desktop)

[Timeline filter rebuild](https://github.com/damus-io/notedeck/pull/1226) fixes a bug where unfollowed accounts kept appearing in feeds. Timeline filters were built once from the contact list and never updated; the fix adds `contact_list_timestamp` tracking and an `invalidate()` method to trigger rebuilds when follow state changes.

### Citrine (Android Relay)

[ContentProvider API](https://github.com/greenart7c3/Citrine/pull/86) exposes the local relay's event database to other Android apps via `ContentResolver`. Unlike the WebSocket interface (which requires apps to maintain a persistent connection and speak the Nostr relay protocol), ContentProvider offers direct synchronous database access through Android's native IPC mechanism. External apps can query events by ID, pubkey, kind, or date range, insert new events with validation, and delete events without managing socket connections.

### rust-nostr (Library)

[NIP-40 relay-level support](https://github.com/rust-nostr/nostr/pull/1183) adds expiration handling at the relay builder level. Expired events are now rejected before storage and filtered out before sending to clients, eliminating the need for each database implementation to handle expiration checks independently.

### nak (CLI)

[Blossom mirror](https://github.com/fiatjaf/nak/pull/91) implements blob mirroring functionality for the command-line tool.

### Mostro (P2P Trading)

[Dev fee audit events](https://github.com/MostroP2P/mostro/pull/559) adds transparent audit trails for development fund payments through kind 8383 Nostr events. The implementation publishes non-blocking audit events after successful fee payments, including order details and payment hashes while excluding buyer/seller pubkeys for privacy.

### MDK (Marmot Development Kit)

Three security audit fixes landed: [Author verification](https://github.com/marmot-protocol/mdk/pull/40) enforces that rumor pubkeys match MLS sender credentials, preventing impersonation attacks. [KeyPackage identity binding](https://github.com/marmot-protocol/mdk/pull/41) verifies credential identity matches event signers. [Admin update validation](https://github.com/marmot-protocol/mdk/pull/42) prevents empty admin sets and non-member admin assignments.

### Shopstr (Marketplace)

[HODL invoice escrow](https://github.com/shopstr-eng/shopstr/pull/217) implements a trust-minimized payment system for physical goods. The architecture uses Alby's `makeHoldInvoice` to lock buyer funds in their own wallet, with settlement triggered only after merchant inventory verification. The handshake protocol flows through [NIP-17](/en/topics/nip-17/) encrypted DMs: buyer sends order request, merchant responds with HODL invoice, buyer pays (funds locked), merchant confirms stock and shipping, then settlement releases funds. Multi-merchant cart support splits payments across vendors.

### Jumble (Web Client)

[Per-relay discovery mode](https://github.com/CodyTseng/jumble/pull/713) adds a toggle to hide posts from followed users on specific relays, enabling language-based discovery feeds (e.g., nostr.band/lang/*). The feature filters out posts where the author pubkey appears in the user's follow list, persisting toggle state per relay URL in localStorage.

### White Noise (Encrypted Messaging)

[Media upload retry](https://github.com/marmot-protocol/whitenoise/pull/937) adds retry options for failed uploads. [Profile edit warnings](https://github.com/marmot-protocol/whitenoise/pull/927) alert users about profile changes. On the backend, [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs/pull/422) fixes a race condition in AccountGroup creation.

### npub.cash (Lightning Address Service)

[v3 rewrite](https://github.com/cashubtc/npubcash-server/pull/40) migrates to Bun for the monorepo and server, adds SQLite support, drops v1 compatibility, implements LUD-21, and adds realtime mint quote updates.

### nostr-java (Library)

[v1.1.1](https://github.com/tcheeric/nostr-java/releases/tag/v1.1.1) ships WebSocket handling refactors and improved test robustness across [two PRs](https://github.com/tcheeric/nostr-java/pull/499).

### NIPs Repository

[NIP-54 Djot migration](https://github.com/nostr-protocol/nips/pull/2180) proposes a separate change to the wiki spec: switching the content format from Asciidoc to Djot, a lightweight markup language with cleaner syntax. The PR introduces reference-style links for wikilinks, making cross-references between wiki articles more readable in source form. [NIP-XX Quorum](https://github.com/nostr-protocol/nips/pull/2179) introduces threshold multi-signature governance for Nostr groups using FROST (Flexible Round-Optimized Schnorr Threshold signatures). A Quorum is an nsec shared among members through a T-of-N scheme where members can represent themselves or delegate to a council of representatives. When the council changes, the old nsec becomes obsolete and a new one is distributed—the final act of any council is signing the governance transition event. The spec defines membership (public or private), elections and polls (popular votes, votes of no confidence), optional natural-language "laws," and crucially, quorum ontologies where quorums can be members of other quorums, enabling hierarchical structures like localities joining regional bodies. Use cases span source code development, company boards, HOAs, and moderated communities.

---

That's it for this week and this year. Building something? Have news to share? Want us to cover your project? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Reach out via NIP-17 DM</a> or find us on Nostr.
