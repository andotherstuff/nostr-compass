---
title: 'Nostr Compass #7'
date: 2026-01-28
publishDate: 2026-01-28
draft: false
type: newsletters
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** Ridestr brings decentralized ridesharing to Nostr with [Cashu](/en/topics/cashu/) payments and encrypted location sharing. Pomade introduces email-based recovery for multisig signers. Damus ships [negentropy](/en/topics/negentropy/) for reliable DM syncing. Amethyst's desktop app adds search, bookmarks, and zaps. Amber v4.1.1 displays relay trust scores. Marmot merges MIP-03 and builds a TypeScript reference chat app. diVine adds [NIP-46](/en/topics/nip-46/) QR authentication and mentions support. New NIP proposals address community management, sequence-based sync, and encrypted file storage. We also take a look back at five years of Nostr Januaries, tracing the protocol's evolution from a handful of early adopters in 2021 through Damus's explosive App Store launch in 2023 to the maturing client ecosystem of 2025.

## News

### Ridestr Brings Decentralized Ridesharing to Nostr

[Ridestr](https://github.com/variablefate/ridestr) is developing a peer-to-peer rideshare application built entirely on Nostr, enabling direct driver-rider transactions with Bitcoin and [Cashu](/en/topics/cashu/) payments. The protocol uses custom event kinds (30173, 3173-3175, 30180/30181) to coordinate rides while maintaining privacy through progressive location disclosure and [NIP-44](/en/topics/nip-44/) encryption.

The system works through a carefully choreographed flow: drivers broadcast availability using geohash-encoded locations (~5km precision) via kind 30173 events, riders request rides with fare estimates through kind 3173, and payments are secured using HTLC escrow tokens before the ride begins. Location privacy is preserved through progressive disclosure, where pickup details are only revealed when drivers arrive and destinations are shared after PIN verification. All communication between parties uses [NIP-44](/en/topics/nip-44/) encryption for privacy.

Ridestr implements payment security through HTLC escrow with P2PK signatures. When a rider accepts a driver's offer, they lock [Cashu](/en/topics/cashu/) tokens with a payment hash that only the driver can claim after ride completion. The protocol currently operates with single-mint architecture, requiring riders and drivers to use the same [Cashu](/en/topics/cashu/) mint. The project's Kotlin-based Android implementation handles proof verification and recovery of stale proofs through NUT-07 state checks.

Ridestr tackles challenges that most Nostr applications avoid: real-time location coordination, payment escrow with dispute resolution, and reputation systems for physical-world interactions. The project is in beta and demonstrates that Nostr's event model can support peer-to-peer service marketplaces, not just content sharing.

### Pomade Launches Alpha Recovery System for Multisig Signers

[Pomade](https://github.com/coracle-social/pomade), developed by hodlbod, builds on the existing [FROSTR](https://github.com/FROSTR-ORG) ecosystem to provide a recovery-focused threshold signing service. Using [FROST](/en/topics/frost/) (Flexible Round-Optimized Schnorr Threshold) signatures via the @frostr/bifrost library, Pomade adds email-based recovery flows on top of the threshold cryptography. The system shards a user's secret key using Shamir Secret Sharing, distributing shares across multiple independent signers with a configurable threshold (2-of-3, 3-of-5, etc.).

The protocol operates entirely over Nostr using a single event kind (28350) with [NIP-44](/en/topics/nip-44/) encrypted payloads. When signing, the client requests partial signatures from at least `threshold` signers, then aggregates these into a valid Schnorr signature. For encryption, signers collaborate to derive shared secrets via ECDH without any single party learning the full key.

Recovery works through two authentication methods: password-based (using argon2id with the signer's pubkey as salt) or email OTP. To prevent MITM attacks during OTP recovery, each signer generates its own verification code with a client-provided prefix, requiring users to authenticate independently with each signer. The protocol requires proof-of-work on registration events (20+ bits per [NIP-13](/en/topics/nip-13/)) to prevent spam.

The trust model is explicit: if `threshold` signers collude, they can steal the key. Email providers are fully trusted since they can intercept OTPs. Users cannot independently recover their full secret key; doing so requires cooperation from `threshold` signers. The protocol is designed for onboarding new users unfamiliar with key management, with the explicit recommendation that users migrate to self-custody once comfortable. Pomade warns about potential "key loss, theft, denial of service, or metadata leakage" given its unaudited alpha status.

## Releases

### Damus Ships Negentropy for Reliable DM Syncing

[Damus v1.13](https://github.com/damus-io/damus/releases/tag/v1.13-6) ships the negentropy implementation [we previewed as an open PR last week](/en/newsletters/2026-01-21-newsletter/#damus-ios-client---open-prs). [PR #3536](https://github.com/damus-io/damus/pull/3536) adds base [negentropy](/en/topics/negentropy/) support to the networking layer, enabling set reconciliation with relays that support the protocol. A companion [PR #3547](https://github.com/damus-io/damus/pull/3547) adds pull-to-refresh DM syncing that uses negentropy to recover missing messages when standard REQ subscriptions fail.

The implementation follows a conservative approach: normal DM loading continues unchanged, with [negentropy](/en/topics/negentropy/) available as a recovery mechanism when users manually refresh. Automated tests demonstrate the fix by generating a DM with an old timestamp that standard queries would miss, then using [negentropy](/en/topics/negentropy/) sync to successfully retrieve it. While [negentropy](/en/topics/negentropy/) support requires compatible relays, the implementation gracefully handles mixed relay environments by using the protocol where available.

### Amber v4.1.1 - Relay Trust Scores

[Amber v4.1.1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.1) ships relay trust score display ([PR #289](https://github.com/greenart7c3/Amber/pull/289)), implementing the relay evaluation concepts discussed in [last week's Trusted Relay Assertions NIP coverage](/en/newsletters/2026-01-21-newsletter/#nip-updates). Trust scores now appear in the Relays page and for NostrConnect connection requests, helping users assess relay reliability before authorizing connections. The release also includes a redesigned login/events/permissions UI and support for the `switch_relays` method. Performance improvements cache keystore operations, addressing reports of 20+ second load times on older devices.

### nak v0.18.2 - MCP Integration

fiatjaf's [nak](https://github.com/fiatjaf/nak) (Nostr Army Knife) [v0.18.2](https://github.com/fiatjaf/nak/releases/tag/v0.18.2) adds [Model Context Protocol](https://nostrify.dev/mcp) support via `nak mcp`, enabling AI agents to search for people on Nostr, publish notes, mention users, and read content using the outbox model. The release also introduces a [one-line installer](https://github.com/fiatjaf/nak/blob/master/install.sh) (`curl -sSL https://raw.githubusercontent.com/fiatjaf/nak/master/install.sh | sh`) that downloads pre-built binaries, eliminating the Go toolchain requirement for end users. Bunker mode now supports Unix sockets and `switch_relays`.

### Zeus v0.12.2 Beta - NWC Fixes

[Zeus v0.12.2-beta1](https://github.com/ZeusLN/zeus/releases) ships multiple NWC fixes addressing issues covered in [last week's Zeus coverage](/en/newsletters/2026-01-21-newsletter/#zeus-lightning-wallet-with-nostr-wallet-connect).

## Project Updates

### Amethyst Desktop - Phase 2A Ships

[Amethyst](https://github.com/vitorpamplona/amethyst) rolled out [Phase 2A of its desktop app](https://github.com/vitorpamplona/amethyst/pull/1676), adding Search, Bookmarks, Zaps, Thread views, and long-form content (Reads) to the desktop experience. A companion [PR #1683](https://github.com/vitorpamplona/amethyst/pull/1683) adds transparent event broadcasting feedback so users now see real-time per-relay status as their events propagate across the network, making it easier to diagnose connectivity issues.

### Notedeck Progress: Calendar App and UX Polish

The Damus team's [Notedeck](https://github.com/damus-io/notedeck) desktop client merged auto-hide toolbar behavior ([PR #1268](https://github.com/damus-io/notedeck/pull/1268)) that responds to scroll velocity for more screen space on mobile views. A [draft PR #1271](https://github.com/damus-io/notedeck/pull/1271) adds a full [NIP-52](/en/topics/nip-52/) Calendar app with month/week/day/agenda views, RSVP support, and [NIP-22](/en/topics/nip-22/) comments on calendar events, currently feature-flagged for testing.

### Jumble Adds Community Mode

[Jumble](https://github.com/CodyTseng/jumble), the relay-focused web client, added [community mode](https://github.com/CodyTseng/jumble/pull/738) and support for [relay set presets via environment variables](https://github.com/CodyTseng/jumble/pull/736), making it easier to deploy themed instances like [nostr.moe](https://nostr.moe/).

### Shopstr Orders Dashboard

[Shopstr](https://github.com/shopstr-eng/shopstr) replaced its chat-based order management with a dedicated [Orders Dashboard](https://github.com/shopstr-eng/shopstr/pull/219). The new interface provides a centralized view for merchants to track order status, mark messages as read, and manage fulfillment without scrolling through chat threads. The update deprecates IndexedDB caching in favor of server-side order status APIs and revises how order DMs are tagged for better filtering.

### Formstr Adds Grid Questions

[Formstr](https://github.com/abh3po/nostr-forms), the Nostr-native forms app, added [grid questions](https://github.com/abh3po/nostr-forms/pull/419) and [rewrote its SDK](https://github.com/abh3po/nostr-forms/pull/410) with embed support. A [fix for non-[NIP-07](/en/topics/nip-07/) signers](https://github.com/abh3po/nostr-forms/pull/418) resolved issues for users with bunker or local signers trying to submit forms with their identity.

### nostr-tools Upgrades Crypto Dependencies

[nostr-tools](https://github.com/nbd-wtf/nostr-tools), the core JavaScript library, [upgraded to @noble/curves v2.0.1](https://github.com/nbd-wtf/nostr-tools/pull/520), addressing breaking API changes across 27 files and adopting the latest audited noble libraries. fiatjaf also added `switch_relays` support to [NIP-46](/en/topics/nip-46/), enabling bunker clients to dynamically change relay connections.

### Zeus Working on NIP-87 Mint Reviews

[Zeus](https://github.com/ZeusLN/zeus) has an [open PR for [NIP-87](/en/topics/nip-87/) mint reviews](https://github.com/ZeusLN/zeus/pull/3576), allowing users to discover and review [Cashu](/en/topics/cashu/) mints filtered by Nostr follows. Reviews include star ratings and can be submitted anonymously or with a user's nsec.

### Camelus Ships Full DM Support

[Camelus](https://github.com/camelus-hq/camelus), a Flutter-based Android client built with Dart NDK for battery-efficient mobile performance, added comprehensive direct messaging with 20+ commits this week. The update includes chat categories, message dates, optimistic send UI, note-to-self functionality, and proper DM relay handling.

### Marmot Protocol Updates

The MIP-03 deterministic commit resolution [we covered as an open PR last week](/en/newsletters/2026-01-21-newsletter/#marmot-protocol-white-noise-encrypted-group-chat-library) has now merged. [MDK PR #152](https://github.com/marmot-protocol/mdk/pull/152) ensures all [MLS](/en/topics/mls/)-based group chats converge on the same state when multiple valid commits arrive for the same epoch.

A companion [spec PR #28](https://github.com/marmot-protocol/marmot/pull/28) adds init_key lifecycle requirements addressing gaps from implementation audits: private key material from Welcome messages must be securely deleted after processing (zeroization, storage cleanup), and new members must perform self-updates within 24 hours for forward secrecy.

The TypeScript SDK ([marmot-ts](https://github.com/marmot-protocol/marmot-ts)) is building a reference chat application. [PR #37](https://github.com/marmot-protocol/marmot-ts/pull/37) adds group creation/listing, key package management with publish/broadcast/delete flows, and QR code invitations. An [open PR #38](https://github.com/marmot-protocol/marmot-ts/pull/38) by hzrd149 implements message history persistence with pagination. On whitenoise-rs, there were 8 PRs merged to master this week, most notably Add event id to user reaction which enables reaction deletion by exposing reaction event IDs, and fix(message_aggregator/emoji_utils): improve is_valid_emoji to capture more valid emoji which broadens emoji validation to support extended Unicode blocks, regional indicators, and keycap sequences. Other updates include language preference storage for client-side localization and removal of default pet names to give clients full control over signup metadata.

### diVine Adds Nostr Integration Features

[diVine](https://github.com/divinevideo/divine-mobile), the short-form video app, continues rapid Nostr integration.

Recent merges include [NIP-46](/en/topics/nip-46/) QR code authentication ([PR #1019](https://github.com/divinevideo/divine-mobile/pull/1019)) and [NIP-17](/en/topics/nip-17/) encrypted direct messaging ([PR #834](https://github.com/divinevideo/divine-mobile/pull/834)). This week's activity focused on [mentions support](https://github.com/divinevideo/divine-mobile/pull/1098) converting `nostr:` URIs and @mentions to clickable profile links, [Classic Viners avatar fallbacks](https://github.com/divinevideo/divine-mobile/pull/1097) using Nostr profiles, and video editing tools including [drawing](https://github.com/divinevideo/divine-mobile/pull/1056), [filters](https://github.com/divinevideo/divine-mobile/pull/1053), and [stickers](https://github.com/divinevideo/divine-mobile/pull/1050).

## NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Open PRs and Discussions:**

- **[Trusted Relay Assertions](https://github.com/nostr-protocol/nips/pull/1534)** - The draft proposal for standardizing relay trust scoring [we covered last week](/en/newsletters/2026-01-21-newsletter/#nip-updates) continues discussion. The core debate centers on whether trust scores should be "global" (computed once for all users) or "personalized" (relative to each observer's social graph). PageRank-style algorithms like [nostr.band's Trust Rank](https://trust.nostr.band/) and [GrapeRank](https://github.com/Pretty-Good-Freedom-Tech/graperank-nodejs) resist sybil attacks by dividing any rank passed through fake accounts by the size of the bot farm. Critics argue that truly personalized scores are more accurate but require expensive per-user computation. The discussion also explores whether to use DVMs for on-demand scoring versus pre-computed kind 30382 attestation events that clients can cache.

- **Communikeys** - A [comprehensive proposal](https://nostrhub.io) for community management that uses existing npubs as community identifiers instead of relay-based approaches. Any npub can become a community by publishing a kind 10222 event; publications target communities via kind 30222 events. Access control uses [NIP-58](/en/topics/nip-58/) badges, enabling delegated membership management with cold storage for community keys.

- **[NIP-CF: Changes Feed](https://njump.me/nevent1qqsyxrrdu09yktr7x5cqqrcj9v2hrqqqefem6f3stkrzwf8anr236sgcpzfmhxue69uhkummnw3ezu7nzvshxwec4wa0qn)** - A draft proposing sequence-based event synchronization as an alternative to timestamp-based `since` filters. The problem: standard Nostr sync using `since` timestamps can miss events when multiple events share the same second-precision timestamp, client and relay clocks drift apart, or checkpointing is imprecise. NIP-CF solves this by having relays assign monotonically increasing sequence numbers to stored events, providing strict total ordering. Clients request changes since a specific sequence number and receive events in guaranteed order, with precise checkpointing that never misses events. The proposal also supports live/continuous mode where subscriptions stay open after initial sync for real-time updates.

- **[NIP-XX: Encrypted File Sync](https://njump.me/nevent1qqsr98tvcy7c4y5w03rd6cdujq9dpdt75uzv4kmkgpdlq7ggdmzptrqcpzfmhxue69uhkummnw3ezu7nzvshxwec4wa0qn)** - A protocol defining kinds 30800 (encrypted files), 30801 (vault indices), and 30802 (shared documents) for syncing encrypted content across devices using Nostr relays. The protocol enables local-first note-taking apps to provide end-to-end encrypted sync without centralized servers. File contents, paths, names, and folder structure are all encrypted using [NIP-44](/en/topics/nip-44/) self-encryption, so relays store blobs they cannot read. Binary attachments like images use [Blossom](/en/topics/blossom/) servers with client-side encryption. Kind 30802 enables document sharing between users by encrypting to the recipient's public key.

## Five Years of Nostr Januaries

[Last month's newsletter](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers) traced Nostr's December milestones from fiatjaf's first client release through Jack Dorsey's catalytic donation. This retrospective charts what happened each January from 2021 through 2025, focusing on verified technical developments.

### January 2021: Early Development

Nostr's third month saw continued development on Branle, fiatjaf's Vue.js client that had launched in December 2020. A small group of early adopters, likely fewer than 15 people, coordinated through the Telegram group [@nostr_protocol](https://t.me/nostr_protocol) (created November 16, 2020), testing the protocol across one or two experimental relays. The command-line client noscl provided terminal-based interaction.

The technical foundation was already locked: users identified by secp256k1 public keys, posts cryptographically signed with Schnorr signatures, and relays serving as dumb storage that don't communicate with each other. This was deliberately Bitcoin-native cryptography, a design choice that would shape adoption patterns years later.

### January 2022: Developer Discovery

January 2022 opened with Nostr still buzzing from its [first Hacker News appearance](https://news.ycombinator.com/item?id=29749061) (December 31, 2021), which generated 110 points and 138 comments. At the time of that post, only about seven relays powered the entire network, with commenters noting "spam is not a problem yet because nostr is super new and no one uses it yet." Robert C. Martin ("Uncle Bob") had endorsed Nostr as potentially "the endgame solution for social communication." The discussion continued into January, with developers debating relay architecture versus true P2P, censorship resistance versus moderation, and whether simplicity could scale.

The HN post sparked a wave of new implementations. Uncle Bob himself started [more-speech](https://github.com/unclebob/more-speech), a Clojure desktop client, on January 18. fiatjaf's [go-nostr](https://github.com/nbd-wtf/go-nostr) library (created January 2021) and [noscl](https://github.com/fiatjaf/noscl) command-line client provided Go tooling, while [nostr-tools](https://github.com/nbd-wtf/nostr-tools) offered JavaScript support. By December 2022, approximately 800 profiles had bios. Branle remained the primary web client, receiving updates including private key import and multi-relay support. Technical challenges were evident: 64-character hex keys proved unintuitive, message delays frustrated users, and the community questioned whether the architecture could handle Twitter-scale traffic.

### January 2023: The Breakout

January 2023 transformed Nostr from experiment to movement. Damus, the iOS client by William Casarin (jb55), battled Apple's App Store approval process. Rejected January 1, rejected again January 26, it was finally [approved January 31](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store). That approval unleashed a cascade: Damus immediately reached #10 in U.S. Social Networking. Jack Dorsey [called it](https://www.theblock.co/post/207448/nostr-based-decentralized-twitter-alternative-damus-goes-live-on-apple-app-store) "a milestone for open protocols."

Eight days earlier, on January 23, [Edward Snowden announced](https://x.com/Snowden/status/1617623779626352640) his presence on Nostr: "One of the cool things about Nostr... beyond censorship resistance, is that you aren't limited to 280 characters." His endorsement from an NSA whistleblower carried weight in privacy-conscious circles, and users immediately began zapping him sats via Lightning.

Web clients raced to onboard the influx. [Snort](https://github.com/v0l/snort), created by kieran in December 2022, emerged as a feature-packed React client; on January 13, Snort integrated NIP-05 registration via the Nostr Plebs API, letting new users claim human-readable identities during onboarding. [Iris](https://iris.to), developed full-time by Martti Malmi (an early Bitcoin contributor who received the second-ever Bitcoin transaction from Satoshi), offered both web and mobile interfaces with free NIP-05 identities at iris.to. [Astral](https://github.com/monlovesmango/astral), built by monlovesmango with Quasar (Vue.js) as a Branle fork, focused on relay management with its relay grouping feature that let users organize relays into sets for posting and filtering. TestFlight betas for iOS clients filled within hours, and Amethyst dominated Android.

Infrastructure scrambled to keep pace. All relays were operated by enthusiasts paying out-of-pocket. Paid relays using Lightning micropayments created natural spam filtering but introduced access friction. [Damus was pulled from China's App Store](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/) just two days after approval, reportedly per request by China's top internet watchdog.

### January 2024: Protocol Hardening

January 2024 focused on protocol standardization and community building. [Nostr PHX](https://www.nostrphx.com/events) kicked off the year with a meetup on January 5 in Phoenix, bringing together local cypherpunks. This was the first of many community events that year including BTC Prague (June), Nostriga in Riga (August), and Nostrasia.

The most significant protocol development was [NIP-59 (Gift Wrap)](https://github.com/nostr-protocol/nips/pull/716) being merged on January 29, providing metadata protection for encrypted communications. Gift Wrap builds on [NIP-44's encryption standard](https://github.com/paulmillr/nip44) (which had been [audited by Cure53](https://cure53.de/audit-report_nip44-implementations.pdf) in December 2023) to hide sender identity from relays. The protocol wraps encrypted messages inside an outer event signed by a random, one-time-use keypair. Relays see only the disposable pubkey, while the real sender's identity is buried in the encrypted payload that only the recipient can decrypt. This prevents relay operators and network observers from learning who is messaging whom. Timestamps can also be randomized to defeat timing analysis.

The ecosystem expanded beyond social media. [Plebeian Market](https://plebeian.market) went fully Nostr-native with [NIP-15](/en/topics/nip-15/) compliance, enabling cross-stall shopping carts and a stall browser for discovering merchants. [Shopstr](https://github.com/shopstr-eng/shopstr) emerged as a permissionless marketplace facilitating Bitcoin commerce. [Zap.stream](https://zap.stream/), built by kieran, brought live streaming to Nostr with Lightning payments at 21 sats/minute. Developer tooling matured with [NDK](https://github.com/nostr-dev-kit/ndk) providing TypeScript abstractions and [rust-nostr](https://github.com/rust-nostr/nostr) offering Rust bindings. [Zeus v0.8.1](https://blog.zeusln.com/new-release-zeus-v0-8-1/) shipped with Nostr contact import and persistent LND, laying groundwork for Nostr Wallet Connect integration in later releases.

Yet infrastructure sustainability [remained challenging](https://arxiv.org/abs/2402.05709). Academic research from this period found 95% of relays struggled to cover operational costs, with 20% experiencing significant downtime. The admission fee for paid relays averaged less than 1,000 sats (~$0.45), insufficient to sustain operations.

*A note on scams: The "Nostr Assets Protocol" and associated "$NOSTR" token that launched around this time [were publicly denounced by fiatjaf](https://www.aicoin.com/en/article/377704) as "100% fraudulent" and "an affinity scam" with no connection to the actual Nostr protocol.*

### January 2025: Client Maturation

January 2025 saw continued client development across the ecosystem. [Nostur 1.17.0](https://www.nobsbitcoin.com/nostur-v1-17-0/) shipped January 13 with cross-device sync for read states, [FROST](/en/topics/frost/) multi-sig login support, and optimized local database performance. Amethyst continued its transition to the outbox model, automatically compiling relay sets based on follow lists rather than requiring manual configuration.

Major clients began moving away from [NIP-04](/en/topics/nip-04/) for direct messages, migrating toward [NIP-17](/en/topics/nip-17/) and the proposed [NIP-104](/en/topics/nip-104/) for enhanced encryption and metadata protection. The Gossip model (outbox/inbox communication) gained adoption as the ecosystem converged on more efficient relay usage patterns. Industry observers predicted this would be the year Nostr transitions from niche protocol to mainstream recognition, with a potential high-profile platform migration that could double daily activity.

### January 2026: Security and Signing Infrastructure

January 2026 brought significant advances in security and signing infrastructure. [Primal Android 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) shipped [NIP-46](/en/topics/nip-46/) remote signing and [NIP-55](/en/topics/nip-55/) local signer support, joining Amber and Aegis as a full signing hub for other Android apps. [Bitchat completed a Cure53 security audit](https://github.com/permissionlesstech/bitchat/pulls), the same firm that audited Signal and NIP-44, with 17+ PRs fixing critical findings including DH secret clearing and thread safety issues. Both Bitchat and Damus migrated from C Tor to Rust Arti for improved reliability and memory safety.

Protocol work continued with [NIP-71](https://github.com/nostr-protocol/nips/pull/1669) (addressable video events) merging and a post-quantum cryptography NIP opening discussion on future-proofing Nostr against quantum attacks. The Trusted Relay Assertions draft proposed standardizing relay trust scoring through signed attestations. The [Marmot Protocol](https://github.com/marmot-protocol/mdk) hardened its [MLS](/en/topics/mls/)-based encrypted messaging with 18 merged PRs addressing audit findings.

Real-world applications expanded with [Ridestr](https://github.com/variablefate/ridestr) developing decentralized ridesharing using [Cashu](/en/topics/cashu/) escrow and [NIP-44](/en/topics/nip-44/) encryption, and [Pomade](https://github.com/coracle-social/pomade) adding email-based recovery flows to [FROST](/en/topics/frost/) threshold signing. Damus shipped [negentropy](/en/topics/negentropy/) for reliable DM syncing, while Amethyst's desktop app reached Phase 2A with search, bookmarks, and zaps.

### Looking Ahead

Six years of Januaries reveal Nostr's evolution from early development (2021) to public discovery (2022) to explosive growth (2023) to protocol hardening (2024) to client maturation (2025) to security infrastructure (2026). The pattern is familiar to anyone who has watched open protocols grow: years of quiet building, a sudden explosion when conditions align, then the longer work of making it all reliable. What started with seven relays and a Hacker News thread is now audited infrastructure with real applications. The question for 2027: when someone hails a ride, sends an encrypted message, or recovers a lost key using Nostr, will they even know they're using it?

---

That's it for this week. Building something? Have news to share? Want us to cover your project? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Reach out via NIP-17 DM</a> or find us on Nostr.
