---
title: "Nostr Compass #41"
date: 2026-09-23
publishDate: 2026-09-23
draft: true
type: newsletters
description: "Nostr Compass #41 covers readable FIPS mesh names, remote LUKS unlock over FIPS, MintRadar, Grain's relay release candidate, Marmot Protocol 0.10.4, new web-of-trust tools, napplet.soy, RelayKit, Threshold Sessions, current protocol work, and deep dives into custom emoji and video events."
---

Welcome back to [Nostr Compass](https://nostrcompass.org), your weekly guide to Nostr.

**This week:** [fips2go](#fips2go-060-gives-mesh-nodes-readable-names) gives FIPS mesh nodes readable local names, [fips-initramfs](#fips-initramfs-brings-remote-luks-unlock-into-early-boot) brings remote LUKS unlock into early boot, and [MintRadar](#mintradar-makes-cashu-mints-easier-to-compare) makes Cashu mints easier to compare. [Grain 0.8.0-rc4](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc4) turns relay health into an operator dashboard, while [Marmot Protocol's MDK](#marmot-protocol-0104-makes-local-sends-durable) makes local sends and attachment acquisition durable. New projects include [napplet.soy](#nappletsoy-publishes-small-sandboxed-nostr-programs), [RelayKit](#relaykit-installs-a-self-hosted-nostr-stack), and [Threshold Sessions](#threshold-sessions-turn-coding-transcripts-into-private-training-data). Protocol work covers petnames, WebRTC signaling, relay administration, payment-address proofs, Blossom directories, encrypted group moderation, and Nostr Wallet Connect budgets. The deep dives explain [NIP-30 custom emoji](#nip-30-custom-emoji) and [NIP-71 video events](#nip-71-video-events).

## Top Stories

### fips2go 0.6.0 gives mesh nodes readable names

[fips2go](https://github.com/fr34aky/fips2go) is an Android client that lets selected applications reach peers and services over the FIPS encrypted mesh. [Version 0.6.0](https://github.com/fr34aky/fips2go/releases/tag/v0.6.0) adds device-local mesh names, so a user can map a long node key to a name such as `home` and connect through `home.fips` anywhere a hostname is accepted.

The [mesh-name resolver](https://github.com/fr34aky/fips2go/releases/tag/v0.6.0) applies additions, removals, and changed mappings to the next lookup without reconnecting the mesh. Names remain local to the phone and outside identity backups, which makes the feature an address book instead of a global naming system; the release also documents that only its ARM64 build received physical-device verification.

### fips-initramfs brings remote LUKS unlock into early boot

[fips-initramfs](https://github.com/jmcorgan/fips-initramfs) is a Linux initramfs package that starts a FIPS mesh node before normal boot so an operator can remotely unlock a LUKS-encrypted root through its npub-addressed node. The user-submitted [0.1.0 release](https://github.com/jmcorgan/fips-initramfs/releases/tag/v0.1.0), published September 6, packages the mesh client, SSH access, and unlock scripts for systems that need unattended or remote encrypted-root startup.

The [first release](https://github.com/jmcorgan/fips-initramfs/releases/tag/v0.1.0) documents the security tradeoffs instead of hiding them: the initramfs contains the node key, the passphrase crosses SSH over FIPS, and local console unlock remains available. This is a catch-up item from a prior user submission rather than a release from the current collection window.

### Grain 0.8.0-rc4 turns relay health into an operator dashboard

[Grain](https://github.com/0ceanSlim/grain) is a self-hosted Nostr relay with an integrated reference client and administration interface. [Version 0.8.0-rc4](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc4) adds a live vitals panel for event volume, connections, uptime, storage, memory, and writer health, plus per-kind storage charts and reorganized access, policy, and retention controls.

The [release candidate](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc4) also makes its client escalate missing-event lookups from the local relay to author outbox relays, embedded relay hints, and NIP-50 search. NIP-50 standardizes relay-side search filters, while NIP-01 defines the core event and subscription rules that include identifier and author prefix matching. Grain adds those prefix matches and configurable full-text kinds to its database, while the release-candidate label makes clear that operators should test the new dashboard and database behavior before treating it as a stable line.

### Marmot Protocol 0.10.4 makes local sends durable

[Marmot Protocol's MDK](https://github.com/marmot-protocol/mdk) is an SDK for MLS-encrypted group messaging whose transport and discovery run over Nostr. [Version 0.10.4](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.4) persists local sends before network completion, lowers draft and pending-message latency, prevents repeated automatic attachment downloads, and exposes retention state in chat-list previews.

The [same release](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.4) adds group creation to agent-control integrations and opt-in reaction consent for approval prompts. It also repairs a halted-wrapper edge case and bounds retry backoff during epoch backfill, continuing the post-0.10.0 reliability work without changing the requirement that generated bindings and native libraries move together.

### MintRadar makes Cashu mints easier to compare

[MintRadar](https://mintradar.org) is a privacy-focused Cashu dashboard that uses Nostr to discover mints and bind community reviews to signed identities. Its [current source](https://github.com/hroomnik007/MintRadar) adds persistent NIP-87 mint announcements, same-operator detection from NUT-06 pubkeys, shareable comparison URLs, and Nostr `naddr` deep links.

NIP-87 standardizes discovery and review events for Cashu mints, while NUT-06 defines the mint information document that exposes a mint's public keys and supported capabilities. A [signed user-submitted update](https://njump.to/nevent1qqs9hwth0rgsprqaml9xuuve2s47x08w2ltjujgwwr4zyqw0qjptecqpzamhxue69uhhyetvv9ujuurjd9kkzmpwdejhgtczyqt40x2js6hcc27delgn5vqwn3qtcjn8uas3rrzmxe2hxsrvdvmmcqcyqqqqqqgyqg6ap) brought MintRadar back into the intake after it was missed in an earlier pass; the project has since accumulated substantial current-window work around those comparison and discovery paths.

### Nostr WoT Oracle 0.3.1 makes trust queries restart-safe

[Nostr WoT Oracle](https://github.com/nostr-wot/nostr-wot-oracle) is a server that ingests public follow and mute events and answers bounded web-of-trust path queries. [Versions 0.3.0 and 0.3.1](https://github.com/nostr-wot/nostr-wot-oracle/releases/tag/v0.3.1) add independently persisted public mute evidence, readiness and ingestion status, revision-bound caches, deterministic replaceable-event selection, and rollback behavior that prevents unpersisted graph changes from becoming queryable.

The [0.3.1 performance pass](https://github.com/nostr-wot/nostr-wot-oracle/releases/tag/v0.3.1) restores graph edges directly into numeric adjacency lists, coalesces superseded follow and mute events before publication, and batches distance-cache misses. These changes matter to clients that need explainable follow distance or mute evidence without silently serving a relationship graph from an older revision.

### Nostr WoT SDK 1.0.2 compresses browser graph storage

[Nostr WoT SDK](https://github.com/nostr-wot/nostr-wot-sdk) is a JavaScript toolkit for crawling, storing, and querying Nostr follow graphs in applications. [Version 1.0.2](https://github.com/nostr-wot/nostr-wot-sdk/releases/tag/nostr-wot-sdk%401.0.2) adopts a graph engine that batches up to 100 authors per relay request, stores edges with compact delta encoding, reuses compatible traversals, and exposes batch distance queries.

The [graph 0.3.0 storage migration](https://github.com/nostr-wot/nostr-wot-sdk/releases/tag/%40nostr-wot/graph%400.3.0) upgrades IndexedDB namespaces to schema 2 and cannot be reopened by older SDK versions. Applications that need rollback should use a separate namespace or clear the upgraded graph instead of assuming the earlier client can read it.

### napplet.soy publishes small sandboxed Nostr programs

[napplet.soy](https://napplet.soy) is a web playground and creator toolkit for building, publishing, playing, inspecting, and remixing small sandboxed Nostr programs called napplets. NIP-34 defines signed Nostr events for Git repository discovery and collaboration. The [soyLI 0.18.2 release](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.18.2) follows the project's September launch with signed listings, Blossom-hosted assets, Git and NIP-34 source references, and relay-discovered manifests.

The [project source](https://github.com/zeSchlausKwab/napplet-soy) keeps network and storage access behind declared capabilities instead of giving each napplet unrestricted browser authority. Its project identity remains unresolved because the canonical site and repository do not bind a project or maintainer npub, so no identity claim is attached here.

### RelayKit installs a self-hosted Nostr stack

[RelayKit](https://relayk.it) is a one-command installer for a self-hosted Nostr stack that can include relays, Blossom media, nsites, Git services, and notifications. The current project is materially broader than the browser relay-discovery client covered in April, and its [current source repository](https://github.com/samthomson/relaykit) documents the new operator-focused deployment surface.

The [installation site](https://relayk.it) presents the services as one coordinated stack instead of requiring operators to assemble each component independently. This coverage therefore treats RelayKit as a changed project direction, not as its first appearance.

### Threshold Sessions turns coding transcripts into private training data

[Threshold Sessions](https://gitworkshop.dev/npub17m2ual3pdjvhd8yc6a3m8snzjsgnmtl26hwen48ne937qgyjyshs2zgvse/relay.ngit.dev/threshold) is a command-line tool that converts AI coding sessions into normalized, redacted, and encrypted training-data epochs. Its repository supports Codex, Claude Code, Cursor, OpenCode, and pi transcripts, stores encrypted artifacts on Blossom, and publishes signed references through Nostr.

Recent [Threshold Sessions source history](https://relay.ngit.dev/npub17m2ual3pdjvhd8yc6a3m8snzjsgnmtl26hwen48ne937qgyjyshs2zgvse/threshold.git) adds timestamp randomization, provenance, extractors, and a ledger for produced epochs. The design lets a contributor preserve auditability and later data use without publishing the readable session transcript to relays.

## Tagged Releases

### Nostr Mail Client 0.16.0 adds per-recipient delivery choices

[Nostr Mail Client](https://github.com/nogringo/nostr-mail-client) is a web, desktop, and Android mail client that exchanges messages through Nostr relays while supporting conventional email delivery. [Version 0.16.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.16.0) lets a sender choose SMTP or Nostr delivery for each recipient and strips location, capture time, and device metadata from photos and videos before upload.

The [release](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.16.0) also requires every account to establish a relay list, keeps at least one relay configured, and adds safer permanent deletion from trash. Those changes make routing and attachment privacy explicit at the point where a mixed email/Nostr message leaves the device.

### Amber 6.6.5 separates backup encryption from app permissions

[Amber](https://github.com/greenart7c3/Amber) is an Android signer that keeps Nostr private keys outside the applications requesting signatures or encryption. NIP-44 standardizes encrypted payloads between Nostr keys, while NIP-46 lets an application request signing and encryption from a remote signer over relays. [Version 6.6.5](https://github.com/greenart7c3/Amber/releases/tag/v6.6.5) encrypts application backups with a dedicated key derived from the account key, preventing an application with remembered NIP-44 decryption permission from reading backup payloads that contain local keys or per-app NIP-46 secrets.

The [migration path](https://github.com/greenart7c3/Amber/releases/tag/v6.6.5) can still restore older identity-encrypted backups until the next publish replaces them, and the release fixes a restore prompt that disappeared after logout when backup publishing was disabled. Users receive both a tighter permission boundary and a recovery path for existing backups.

### Amethyst 1.16.0 expands video, calendars, and geocaching

[Amethyst](https://github.com/vitorpamplona/amethyst) is a feature-rich Android Nostr client with social, media, wallet, and signer integrations. NIP-71 standardizes video events, NIP-51 defines user-curated lists, NIP-CC defines geocache records, and NIP-52 defines calendar events and responses. [Version 1.16.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.16.0) adds interoperability across those four event families and attaches relay hints to calendar responses.

The [release series](https://github.com/vitorpamplona/amethyst/releases/tag/v1.16.0) also adds BOLT12 offers with BOLT11 fallback, improves notification replies and deep links, and keeps QR key material off screen and out of logs. That mix broadens the event types users can act on while tightening sensitive scanner behavior.

### Alby Extension 3.15.0 hardens website-initiated requests

[Alby Extension](https://github.com/getAlby/lightning-browser-extension) is a browser wallet and Nostr signer that grants websites scoped Lightning and signing capabilities. [Version 3.15.0](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.15.0) blocks website-supplied LNURLs from local or private network addresses, requires cross-host LNURL-auth confirmation, and removes remembered approval for raw Schnorr-signing methods.

The [security release](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.15.0) also debits allowance budgets before sending concurrent payments and removes the generic WebLN request method. Integrators must use dedicated WebLN methods, while users gain clearer boundaries around network targets, authentication hosts, and site spending limits.

### LaWallet NWC 2.7.1 unifies zap receipts across wallets

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) is an open-source Lightning wallet service that exposes accounts to applications through Nostr Wallet Connect. NIP-57 standardizes signed Lightning zap requests and settlement receipts for Nostr profiles and events. [Version 2.7.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.7.0) decouples that receipt publication from wallet-specific settlement paths so every supported NWC wallet can emit zap receipts, then [2.7.1](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.7.1) brings receive and activity screens onto the same receipt flow as sends.

The [2.7.1 package](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.7.1) also aligns StartOS storage and backup layout between sideload and community packages. Operators upgrading the first 2.7.0 sideload need the corrected package before relying on the database volume transition.

### NoorNote 1.6.1 adds encrypted calendars

[NoorNote](https://github.com/77elements/noornote) is a Nostr notes application with optional productivity modules and local reminders. [Version 1.6.0](https://github.com/77elements/noornote/releases/tag/v1.6.0) adds public and encrypted calendar events, month, week, and list views, Android reminders, and interactive timeline cards for shared events.

[Version 1.6.1](https://github.com/77elements/noornote/releases/tag/v1.6.1) reorganizes addons into a per-account dashboard and fixes URLs containing `naddr` or `npub` identifiers being misread as cards or mentions. The release turns calendar data into a usable Nostr workflow while repairing identifier parsing in ordinary notes.

### Citrine 3.2.0 bounds relay-aggregator memory

[Citrine](https://github.com/greenart7c3/Citrine) is an Android Nostr relay that gives other applications a local event store and relay interface. [Version 3.2.0](https://github.com/greenart7c3/Citrine/releases/tag/v3.2.0) streams matching events in batches, caps aggregator fan-out at 200 relays, and bounds caches to prevent large queries from exhausting memory.

The [release](https://github.com/greenart7c3/Citrine/releases/tag/v3.2.0) also exposes out-of-memory failures in the in-app log and lets operators hide the event graph. A phone acting as both relay and aggregator now fails more visibly and holds a defined memory boundary.

### Wisp 1.2.5 routes threads through inbox relays

[Wisp](https://github.com/barrydeen/wisp) is a privacy-oriented Nostr client with built-in Cashu and Lightning wallet support. NIP-22 defines generic kind `1111` comments that can reply to many kinds of Nostr content. [Version 1.2.4](https://github.com/barrydeen/wisp/releases/tag/v1.2.4) sends thread and notification reads only to inbox relays, treats those comments as replies, and lets users withdraw their full wallet balance on chain.

[Version 1.2.5](https://github.com/barrydeen/wisp/releases/tag/v1.2.5) packages the follow-up release after those changes. Inbox-only routing reduces unnecessary relay exposure while the comment handling keeps NIP-22 conversations visible in threads, counts, and notifications.

### nostr-wot-extension 0.8.0 restores opt-in graph queries

[nostr-wot-extension](https://github.com/nostr-wot/nostr-wot-extension) is a browser signer and identity extension with wallet payments and local web-of-trust analysis. [Version 0.8.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.0) restores its experimental web-of-trust API as a menu-only opt-in with local, remote, and hybrid query modes, scalable graph synchronization, mute-aware scoring, and per-account storage controls.

The [release](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.0) also requires confirmation before replacing a known follow list with zero or one contact, even when a saved permission or remote signer is present. That guard uses verified relay, signed-event, and synchronized graph history to make destructive follow-list changes harder to approve silently.

### pakstr 0.24.0 expands its Android Nostr runtime

[pakstr](https://git.nostrdev.com/stuff/pakstr) is a packaging system and application shell for distributing web applications with native Nostr capabilities. NIP-46 defines remote-signer sessions, NIP-98 defines signed HTTP authentication, and NIP-55 lets Android applications request signatures from an external signer. [Versions 0.21.0 through 0.24.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.24.0) add production bunker pairing, proxied authenticated requests, external signing through a bunker, a persistent Android API endpoint, and Zapstore icons.

The [release sequence](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.24.0) also repairs invalid-relay cleanup and Amber pairing. NostrAppShell entries point to the same package series, so they are one implementation and are covered here once.

### Nail 0.2.2 makes mail attachments fail soft

[Nail](https://github.com/formstr-hq/nail) is a bridge and application that carries Nostr messages into email workflows. [Version 0.2.2](https://github.com/formstr-hq/nail/releases/tag/v0.2.2) retries a message without attachments when a relay refuses the attachment payload, adds a size ceiling to prevent bridge restarts, and changes the default bridge relay.

The [application update](https://github.com/formstr-hq/nail/releases/tag/v0.2.2) also restores link opening and opt-in image viewing. Delivery can now degrade to the message body instead of losing the entire email when its attachment path fails.

### Mostro CLI 0.16.2 removes its legacy chat transport

[Mostro CLI](https://github.com/MostroP2P/mostro-cli) is a terminal client for coordinating peer-to-peer Bitcoin trades through Mostro's Nostr protocol. [Version 0.16.2](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.2) removes the version-one gift-wrap dual-read and dual-write path, migrates peer chat to the current envelope, and lets a trader reach the solver through dispute chat.

The [release](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.2) also adds an operator command for cancelling pending orders. Deployments should update client and coordinator expectations together because the old chat transport is no longer a fallback.

### Dart NDK dev.5 adds signed app-update releases

[Dart NDK](https://github.com/relaystr/ndk) is a Dart client library for relay connections, signing, caching, wallet operations, and Nostr application state. NIP-82 standardizes signed application-release metadata and downloadable artifacts. [Version 0.10.0-dev.5](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.5) adds those application-update events, while the preceding development release makes Cashu quote recovery resumable and lets a broadcast declare the identity to which it may be attributed.

The [development series](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.5) also avoids anonymous connections when a broadcast requires authentication and stops waking relays for deliveries parked on a missing identity. The prerelease label still signals migration risk for applications adopting the new broadcast and wallet behavior.

### BitBlik 0.11.0 brings disputes into the app

[BitBlik](https://github.com/bit-blik/bitblik) is a mobile peer-to-peer Bitcoin trading client that coordinates orders and chat over Nostr. [Version 0.11.0](https://github.com/bit-blik/bitblik/releases/tag/v0.11.0) adds coordinator dispute chat, BOLT12 payouts where supported, Android self-updates sourced from NIP-82 release events, and wallet backup and recovery fixes.

The [release](https://github.com/bit-blik/bitblik/releases/tag/v0.11.0) also handles refunds after dispute rulings and preserves wallet state during Neko recovery. Traders can now remain inside the client for the dispute conversation instead of switching to a separate coordinator channel.

## Protocol and Spec Work

### NIP-02 clarifies petnames in follow lists

[NIP-02 (Follow List)](/en/topics/nip-02/) standardizes the kind `3` event that records whom an account follows and can attach a local petname to each followed key. The [merged petname clarification](https://github.com/nostr-protocol/nips/pull/2472) allows display-safe characters while preserving the field as a user's local label, not a globally verified name.

### NIP-AC proposes relay-bootstrapped WebRTC signaling

[NIP-AC](https://github.com/nostr-protocol/nips/pull/2461) is an open proposal for using signed Nostr events to discover peers and exchange WebRTC offers, answers, and ICE candidates before traffic moves to a direct connection. NIP-59 standardizes gift wrapping that hides an event's sender and metadata inside encrypted envelopes. The proposal covered last week has since shipped a revised draft that keeps relays out of the established data path, uses ordinary `p` and `e` tags for recipients and session correlation, and recommends that gift-wrapping scheme when signaling metadata needs concealment.

### NIP-86 proposes clear and list methods for relay management

[NIP-86 (Relay Management API)](/en/topics/nip-86/) standardizes authenticated administrative calls for banning, allowing, inspecting, and configuring a relay. [PR #2477](https://github.com/nostr-protocol/nips/pull/2477) proposes methods for clearing pubkeys or events from both allow and ban lists and for listing roles, allowed events, and disallowed kinds, including behavior already present in the khatru relay framework and the go-nostr library.

### NIP-69 proposes a stable creation time for trading orders

[NIP-69 (Peer-to-Peer Trading)](/en/topics/nip-69/) standardizes addressable order events that let multiple trading applications share buy and sell liquidity. [PR #2476](https://github.com/nostr-protocol/nips/pull/2476) proposes an optional creation-time tag that stays fixed across status updates, so a returned or republished order does not look newly created merely because its event timestamp changed.

### NIP-A3 proposes proof of payment-address ownership

[NIP-A3 (Payment Targets)](/en/topics/nip-a3/) lets an account publish portable payment addresses for multiple networks in one replaceable event. [PR #2475](https://github.com/nostr-protocol/nips/pull/2475) proposes an optional signature made by the payment address's own key, giving compatible address types a proof that binds the destination to the Nostr author while treating missing proofs as neutral.

### BUD-16 proposes deterministic directory manifests

[BUD-16](https://github.com/hzrd149/blossom/pull/105) is an open Blossom proposal for grouping content-addressed blobs into named directory trees with reproducible manifest hashes. The draft defines deterministic MessagePack encoding, named links, metadata, optional encryption keys, and `.bdir` path resolution while leaving servers to store ordinary blobs.

### Marmot adds encrypted group polls

[Marmot Protocol](/en/topics/marmot/) defines interoperable application events inside MLS-encrypted groups carried over Nostr. NIP-88 defines poll questions and signed response events. [Merged MIP work](https://github.com/marmot-protocol/marmot/pull/425) recognizes those polls inside a group while keeping relay selection bound to authenticated group routing and explicitly stating that they are not anonymous or election-grade.

### Marmot merges group reports and admin deletion

[Marmot group moderation](https://github.com/marmot-protocol/marmot/pull/423) defines encrypted report, dismissal, and administrator-deletion events that converge under the group's authenticated state. The proposal covered last week has now merged, fixing a status transition that lets implementations align report review and message removal against the accepted specification.

### NWC-13 proposes connection budget queries

[Nostr Wallet Connect](/en/topics/nip-47/) lets an application request narrowly scoped wallet operations through encrypted Nostr events. [NWC-13](https://github.com/nostr-wallet-connect/nwc/pull/7) proposes a separate `get_budget` permission and response so an application can inspect used, total, and renewal allowance without receiving permission to read the wallet's balance.

## NIP Deep Dive: Custom Emoji and Video Events

### NIP-30: Custom Emoji

[NIP-30 (Custom Emoji)](/en/topics/nip-30/) standardizes how a signed event maps readable `:shortcodes:` to image URLs, with an optional address that points to a reusable emoji set. The [specification](https://github.com/nostr-protocol/nips/blob/master/30.md) permits letters, numbers, hyphens, and underscores in a shortcode and applies the mapping to profiles, short text notes, comments, reactions, and live activities. NIP-51 defines public and private list formats, including the kind `30030` parameterized replaceable events that hold named emoji sets.

Clients should preserve the literal shortcode when an image fails to load, reject malformed mappings, and treat every image host as an external network request that can observe the viewer's address and timing. [Amethyst's Android implementation](https://github.com/vitorpamplona/amethyst/blob/96bec0cc7c1df4c05d4208fb1cfd6aac06fe97e7/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip30CustomEmoji/EmojiUrlTag.kt) parses the optional set address and enforces the allowed shortcode characters. [Wisp's mobile client implementation](https://github.com/barrydeen/wisp/blob/b48be58271131c6062be2cc5449777cdd4fe6d31/app/src/main/kotlin/com/wisp/app/nostr/Nip30.kt) builds emoji sets and removes duplicate shortcodes from rendered content. [Nostria's web client implementation](https://github.com/nostria-app/nostria/blob/e861946f4ef4e70f3ec49997a4be27615b9b6f5e/src/app/utils/emoji-shortcode.ts) normalizes separators before validating shortcodes, which shows why producers should test common clients before depending on punctuation permitted by the specification.

[NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) defines the canonical serialization, event ID, and signature rules used to authenticate Nostr events. The following kind `30030` emoji-set event was recovered from `wss://nos.lol` and `wss://relay.primal.net` during review and passed those ID rules plus BIP-340 signature verification. Its `d` tag supplies the replaceable set identifier, and its `emoji` tag maps `:liberlandflag:` to the hosted image.

```json
{"kind":30030,"id":"438814476db249b50067d167e50c85530e317126179546a584365c8371bdd97f","pubkey":"6e1897660c62153be7355a82a62549b09993fb12b50de73a32610725d1a5de6b","created_at":1790025651,"tags":[["d","1962f3e8-5a74-4327-b88d-4697bdd2119d"],["client","Amethyst"],["emoji","liberlandflag","https://nogues.ca/emoji/liberlandflag.png"],["title","Liberland"],["description","#Liberland"],["image","https://npub1dcvfwesvvg2nhee4t2p2vf2fkzve87cjk5x7ww3jvyrjt5d9me4szmscg7.blossom.band/a8aa38949d3d7a17e369703391de0406f50b518a1a6ca9791ebf38c94b51a0e1.jpg"]],"content":"","sig":"5f7dd5b8879311689e95cbab26edd6f65611d517d22d12d568a9de219c8a8fc6999365c83205d02ec74844b4b9944ed5419ec17ea9d8cbf4e347504cc3685304"}
```

[Alex Gleason introduced NIP-30 in April 2023](https://github.com/nostr-protocol/nips/commit/e91ce3409e1ce8267fc07a21784d2538621267c3). That original proposal, covered previously, has now shipped three years of specification changes, including an [August 2026 update](https://github.com/nostr-protocol/nips/commit/735a25e44b8e7a01539864f2a2dcf3e728977fd3) that added kind `1111` comments to its supported event kinds. The design keeps emoji meaning local to each signed event or referenced set, so clients do not need a global shortcode registry.

### NIP-71: Video Events

[NIP-71 (Video Events)](/en/topics/nip-71/) standardizes Nostr events for landscape and short-form video, including playback metadata, alternate files, captions, chapters, participants, and imported-source provenance. The [canonical specification](https://github.com/nostr-protocol/nips/blob/master/71.md) assigns kinds `21` and `22` to immutable landscape and portrait video posts, while kinds `34235` and `34236` use a `d` tag to create addressable videos whose metadata can be updated under a stable coordinate. Each `imeta` tag describes one playable variant with a URL and media type plus optional dimensions, hash, preview image, fallback, service, bitrate, and duration.

Clients must validate media URLs and hashes, bound downloads, handle missing variants, and make external-host requests visible to users because a video server can observe playback traffic. [Amethyst's Android implementation](https://github.com/vitorpamplona/amethyst/blob/96bec0cc7c1df4c05d4208fb1cfd6aac06fe97e7/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip71Video/VideoEvent.kt) separates video and audio tracks and chooses a playable variant. [Wisp's mobile client implementation](https://github.com/barrydeen/wisp/blob/b48be58271131c6062be2cc5449777cdd4fe6d31/app/src/main/kotlin/com/wisp/app/nostr/Nip71.kt) parses and builds regular video events with structured `imeta` fields. [Resonote's browser-extension implementation](https://github.com/ikuradon/Resonote/blob/4ac14e1206608315d6507da405d4c5df3312d4d0/packages/core/src/nip71-video.ts) builds and parses all four event kinds, media variants, text tracks, segments, participants, and origin metadata.

The following kind `22` short-video event was recovered from `wss://relay.damus.io` and `wss://nos.lol` during review and passed the [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) ID rules plus BIP-340 signature verification. Its `imeta` tag binds the MP4 URL to its MIME type, SHA-256 hash, dimensions, and duration, while the surrounding tags provide a title, publication time, accessibility text, and searchable topics.

```json
{"kind":22,"id":"dd1fcfe7ce6db5450e362879897138ca4e639ef39654dfe3b1f669310fd9545d","pubkey":"870ce6f7aa9ee05025667245343278eccfb8e3eafc08bcab68824ad0f4cfa675","created_at":1790094714,"tags":[["title","Why Pepe moves 3x Bitcoin"],["published_at","1790094714"],["alt","Why Pepe moves 3x Bitcoin"],["imeta","url https://the-bitcoin-strategy.com/nostr-relay/pKy3my2zzMhCVNL1.mp4","m video/mp4","x 3dafddd0b1730213212bcaf96136684f15e20ee5f20a1252052a58f3a8b36652","dim 1080x1920","duration 62"],["duration","62"],["t","bitcoin"],["t","pepe"],["t","memecoin"],["t","altcoin"]],"content":"Why Pepe moves 3x Bitcoin\n\nPepe jumped about twenty percent in a single day, roughly triple Bitcoin's move. Most of the trading is not the token itself: on Binance, the volume in bets on the price was about eight times the volume in the actual token. Those bets are made with borrowed money, so every dollar tends to move the price more, in both directions.\n\nAsk Gerhard AI For Free:\nhttps://mybtcguy.com\n\n#bitcoin #pepe #memecoin #altcoin","sig":"0da305b00f4b1631b14b8fd33fcc6a2a0e54e24233dba541db3d2bce3705ac0dcf61401764b47555015e2566dcf4a8886cd3f767ea26ed2da76b3ac9bb23d680"}
```

[The NIP-71 file history began in December 2023](https://github.com/nostr-protocol/nips/commit/7afd1049d98a82aa7754f80de80d97dd686cf40e) when zmeyer44 moved the video-event proposal to its current number. The [addressable-video update](https://github.com/nostr-protocol/nips/pull/1669), covered previously, has now shipped across multiple current implementations; its kinds `34235` and `34236` give publishers a stable coordinate for corrected metadata and migrated hosting.

### How the two specifications relate

The [NIP-30 specification](https://github.com/nostr-protocol/nips/blob/master/30.md) controls presentation metadata for a limited set of social event kinds, while [NIP-71](https://github.com/nostr-protocol/nips/blob/master/71.md) defines media-centered events and their playback data. NIP-30 does not currently list the four NIP-71 video kinds, so clients should display custom emoji around videos through supported profiles, comments, reactions, or live activities and should not assume shortcode replacement inside a video event. That boundary gives implementers a precise interoperability rule while both specifications expand the media that a Nostr interface can render.

---

NIP-17 defines private direct messages whose sender and metadata are hidden inside gift-wrapped events. Send a NIP-17 DM to share a project or news item through the [Nostr Compass project](https://github.com/andotherstuff/nostr-compass).
