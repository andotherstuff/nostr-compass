---
title: "Nostr Compass #33"
date: 2026-07-29
publishDate: 2026-07-29
draft: false
type: newsletters
description: "Amethyst 1.13.1 ships Nostr apps, Mosaico coordinates coding agents, and Nostrology maps NIP-65 relay-list concentration."
---

Welcome back to [Nostr Compass](https://github.com/andotherstuff/nostr-compass), your weekly guide to Nostr.

**This week:** [Amethyst 1.13.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.1) ships embedded Nostr apps, collaboration surfaces, authenticated relay and Blossom access, and new payment paths. [Code Call 0.2.66](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.66) keeps remote coding sessions moving from a phone, [GitWorkshop](https://github.com/DanConwayDev/gitworkshop) coordinates maintainers and repository synchronization, and [Mosaico 0.1.2](https://github.com/pablof7z/mosaico/releases/tag/v0.1.2) gives coding agents a shared Nostr awareness layer. [Nostrology](https://dev.nostrolo.gy/relays) maps how profiles divide read and write duties across their published relay lists. Android releases from [Mafrend](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.0), [Hanami](https://github.com/Letdown2491/hanami-android/releases/tag/v0.1.0), and [Cordn](https://github.com/Cordn-msg/cordn-web/releases/tag/v0.2.1) lead the tagged releases, while [FIPS](https://github.com/jmcorgan/fips/pull/126) opens an OpenWrt access layer and begins a FreeBSD port. Protocol coverage reports NIPs, BUDs, NAPs, Marmot, Gamma Markets, Concord, and NWC, while [Six Years of Nostr Julys](https://github.com/nostr-protocol/nips/commits/master/) follows July changes from early domain lookup through relay-group state.
## Top Stories

### Amethyst 1.13.1 ships Nostr apps, collaboration, and new payment paths

[Amethyst 1.13.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.1), the July 29 follow-up to 1.13.0 for the Android and multiplatform Nostr client, opens napplets and NIP-5A nsites inside an isolated, keyless browser process. A consent-gated `window.nostr` bridge can sign and use selected capabilities through the active account, while per-site and per-account permission screens let users review or revoke those grants. Favorite apps can stay pinned in the bottom bar without sharing cookies, login state, or grants across accounts.

The same [Amethyst release](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.1) adds Git repository trees, issues, and pull requests alongside Concord communities, NIP-29 relay groups, Buzz group chat, wiki pages, and RSS feeds. Those surfaces let a user move between code, community, publishing, and social views under the same Nostr identity.

Payments and identity also widened in [version 1.13.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.1). Amethyst can create and pay BOLT12 offers, starts remote-signer accounts automatically, adds Blossom fallback servers, and expands Web of Trust controls for badges, communities, and relay groups. The follow-up adds a [CORD-02 dissolution seal](https://github.com/vitorpamplona/amethyst/pull/3767), kind `9008` [group and channel deletion](https://github.com/vitorpamplona/amethyst/pull/3779), [NIP-29 host-relay authentication](https://github.com/vitorpamplona/amethyst/pull/3788), and authenticated [BUD-01 retries](https://github.com/vitorpamplona/amethyst/pull/3789) for gated Blossom downloads. The release notes also record a large accessibility, translation, desktop, performance, and stability pass.

### Code Call 0.2.66 keeps several remote work sessions moving from a phone

[Code Call 0.2.66](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.66), an Android remote for computer-side coding sessions, can ask a routed worker for a concise catch-up from the latest phone message. It keeps multiple sessions independent, accepts replies only from the expected sender, and keeps its inbox connected to each configured worker relay for background delivery. Encrypted [NIP-17 (Private Direct Messages)](/en/topics/nip-17/) keeps requests and replies private, while encrypted [Blossom](/en/topics/blossom/) attachments can arrive with their original file type intact. These releases let the phone maintain and catch up with multiple independently routed computer-side sessions.

### GitWorkshop coordinates maintainers and keeps repository sync independent

[GitWorkshop's July 27 signed release](https://primal.net/e/869e01f9a74d98f468a66f3b83865d198a82cc718c1db36324398b1b88a17c60) adds Android login through [NIP-55 (Android Signer Application)](/en/topics/nip-55/) to the browser-based [NIP-34 (`git` stuff)](/en/topics/nip-34/) forge. Its [source repository](https://github.com/DanConwayDev/gitworkshop) now coordinates lead maintainers recursively, preserves each maintainer's relay hints, and keeps repository synchronization independent from invitation acceptance. Cross-repository work-item references connect related work across repositories, while GRASP copies repository data to selected Git endpoints without coupling that transfer to invitation delivery. The developer-signed [3.1.1 update](https://primal.net/e/01d0939e9960cb82f1f7aba6f1900af2c61ce384e38352221bf9d5878116ae2d) repairs Android signer intent delivery, recursive maintainer resolution, and path-preserving repository links.

### Mosaico 0.1.2 gives coding agents a shared Nostr coordination fabric

[Mosaico 0.1.2](https://github.com/pablof7z/mosaico/releases/tag/v0.1.2) gives coding-agent sessions in Claude Code, Codex, Goose, Hermes, OpenCode, and Grok a shared-awareness fabric over [NIP-29 (Relay-based Groups)](/en/topics/nip-29/). Sessions broadcast short status updates and can find related active work across hosts while keeping their transcripts and context separate.

Named Codex profile discovery and Goose's Top Of Mind view expose the fabric inside two more harnesses ([PR #618](https://github.com/pablof7z/mosaico/pull/618), [PR #619](https://github.com/pablof7z/mosaico/pull/619)). Hosted agents can acquire a public fabric again, and setup now requires an explicit relay choice ([PR #626](https://github.com/pablof7z/mosaico/pull/626), [PR #629](https://github.com/pablof7z/mosaico/pull/629)). Mosaico remains an awareness layer, not an agent host, orchestrator, or transcript merger.

### Nostrology maps relay-list concentration from published NIP-65 events

[Nostrology's relay observatory](https://dev.nostrolo.gy/relays) derives its dataset from each profile's latest [NIP-65 (Relay List Metadata)](/en/topics/nip-65/) kind `10002` event, following the [published specification](https://github.com/nostr-protocol/nips/blob/master/65.md). It separates read, write, and combined relay roles, charts how many relays each profile lists, and exposes the underlying counts in a sortable table. The current page contains 34,427 distinct relay URL values and groups 520,468 profiles at exactly one listed relay, compared with 150,657 at three and 60,710 at four.

The same [Nostrology dataset](https://dev.nostrolo.gy/relays) shows overlapping concentration around `relay.momostr.pink` at 298,859 profiles, `relay.damus.io` at 287,181, `nos.lol` at 279,468, and `relay.primal.net` at 225,336. Those counts measure published routing preferences, not availability: the raw table retains malformed URLs, local addresses, and unreachable endpoints, while the [NIP-65 specification](https://github.com/nostr-protocol/nips/blob/master/65.md) defines routing metadata and does not test relay health. The observatory makes adoption and data-quality problems visible without treating a listed relay as a live one.

## Tagged Releases

### Kairos 0.1.1 adds reminders and a local Astraea handoff

[Kairos 0.1.1](https://primal.net/e/ffb054280008dc3ba488d5d3a2cbfec6c4123489a874683545a29a466682fd90) adds due-date reminders, a versioned local handoff to Astraea, and stricter relay and URL handling. The [0.1.0 signed release](https://primal.net/e/6e02430844abdabf5421bbf5745a09ef2870e4ade93f56627ee14ba8db58a00a) introduced the [offline-first task manager](https://github.com/Lwb89dev/kairos), whose optional sync layer writes [NIP-44 (Encrypted Payloads)](/en/topics/nip-44/)-encrypted records to user-selected relays. Kairos uses deterministic task coordinates and encrypted tombstones with [NIP-09 (Event Deletion Request)](/en/topics/nip-09/) deletion requests, while local-only tasks never leave the device.

### Shosho 1.0.0 expands its live-streaming marketplace

[Shosho 1.0.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.0.0) redesigns the live-streaming marketplace around creators, live sessions, clips, and products that users can find through configurable relay search. A unified notification feed now collects mentions, reactions, reposts, and zaps and supports replies without leaving the feed. Viewers can publish clips from live streams or replays, while the release also improves threaded chat, clip replies, profile loading, and network usage.

### Mafrend v1.0 previews place-based Nostr chat on Android

[Mafrend v1.0](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.0) is the first public Android alpha of a planned place-based Nostr chat app. Its [project page](https://mafrend.com) labels the feature set as still in active development and describes each map location as a dedicated chat room for conversations around a place. A public release repository carries the installable Zapstore package while the main app remains private.

### Hanami 0.1.0 gives Blossom servers a signer-mediated Android path

[Hanami 0.1.0](https://github.com/Letdown2491/hanami-android/releases/tag/v0.1.0), an Android companion for [Blossom](/en/topics/blossom/) servers, lets people sign in, upload, and download from a phone. The app uses [NIP-55 (Android Signer Application)](/en/topics/nip-55/) for approval-mediated signing and a native [NIP-98 (HTTP Auth)](/en/topics/nip-98/) handshake for the server session. Hanami locks its web shell and signing bridge to the chosen server origin, keeping credentials with the signer while the server's existing web interface supplies the application experience. The first public release requires Android 8 or later, a reachable Hanami server, and a compatible signer app.

### Cordn launches its Nostr-identity group chat on Android

Cordn, a private group-messaging client, now gives Android users Nostr identity onboarding, profile links through [NIP-05 (Mapping Nostr Keys to DNS-Based Internet Identifiers)](/en/topics/nip-05/), and verified links that open Cordn destinations in the app. The [0.2.1 release published July 24](https://github.com/Cordn-msg/cordn-web/releases/tag/v0.2.1) introduces that native line alongside the existing web client. Messages use [MLS](/en/topics/mls/), a group-encryption protocol, with coordinator-assisted delivery, so groups retain ordered encrypted conversations without requiring an email address or phone number.

### Nostur 1.30.1 tightens sharing, threads, and duplicate-post protection

[Nostur 1.30.1](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.30.1), a Nostr client for iPhone, iPad, and Mac, lets people work through nested reply threads without the expansion and collapse failures that disrupted the new layout. It also prevents the same draft from publishing twice, including when media-upload callbacks repeat. The release follows [1.30.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.30.0), which added disappearing direct messages and a share-sheet route for sending media into Nostr, so the app now pairs new messaging and publishing paths with fixes to their everyday thread and posting flows.

### Formstr Drive 0.0.2 pairs Nostr file metadata with Blossom blobs

[Formstr Drive 0.0.2](https://github.com/formstr-hq/formstr-drive/releases/tag/v0.0.2), a Nostr-native file manager, gives users in-app previews and the option to open office documents in Nostr Docs. Underneath, it adds chunked [Blossom](/en/topics/blossom/) storage, the blob-server layer for Nostr media, plus deletion that removes the remote blob when a user removes a file. A local relay keeps the app's Nostr metadata close at hand while Blossom holds the file data, separating file organization from the large bytes themselves.

### NoorNote 1.3.1

[NoorNote 1.3.1](https://github.com/77elements/noornote/releases/tag/v1.3.1), a Nostr client for web, desktop, and Android, adds disappearing-message timers and configures working default DM relays for newly created accounts. It filters global articles without cover images and routes repost notifications into the article reader. The preceding [1.3.0 release](https://github.com/77elements/noornote/releases/tag/v1.3.0) added [NIP-53 (live activities)](/en/topics/nip-53/) cards, [NIP-68 (Picture-first feeds)](/en/topics/nip-68/) person tags, a [NIP-78 (application-data)](/en/topics/nip-78/) soft mute, and relay-seen status for notes.

### algia 0.0.133

[algia 0.0.133](https://github.com/mattn/algia/releases/tag/v0.0.133), a Go command-line client for Nostr, follows [0.0.132](https://github.com/mattn/algia/releases/tag/v0.0.132), which added [NIP-29 (Relay-based Groups)](/en/topics/nip-29/) listing, timelines, posting, reactions, deletions, and join and leave flows. The same release added [NIP-42 (Authentication of clients to relays)](/en/topics/nip-42/) pre-authentication for relays configured to require it. Version 0.0.133 then added local-image uploads to regular, channel, and group posting commands, attaching the resulting URLs and [NIP-92 (Media Attachments)](/en/topics/nip-92/) tags to each event. Image-only posts work as well, and group posts target the group's relay media store by default while other posts use configured file servers.

### swift-nostr 0.7.0

For Swift applications, [swift-nostr 0.7.0](https://github.com/yysskk/swift-nostr/releases/tag/0.7.0), a Nostr library for Apple platforms, lets one [NIP-46 remote signer](/en/topics/nip-46/) drive every client feature through its signing abstraction. The release adds [NIP-98 (HTTP Auth)](/en/topics/nip-98/) and [NIP-29 (Relay-based Groups)](/en/topics/nip-29/) support, including group joining, posting, and moderation flows. It also validates [NIP-44 (Encrypted Payloads, Versioned)](/en/topics/nip-44/) padding against the official vectors, rejecting payloads that carry a valid MAC over noncanonical padding.

### lawallet-nwc 2.0.0

[LaWallet NWC 2.0.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.0.0), a Nostr-connected wallet and [NIP-47 (Nostr Wallet Connect)](/en/topics/nip-47/) service, adds passkey login that derives the Nostr signing key in the browser with the WebAuthn PRF extension. The server never receives that secret, and the same passkey can recover the same key on another synced device. Accounts can now link and merge multiple Nostr pubkeys, while the optional listener service relays wallet-connect events and retries webhook delivery after an unreachable endpoint.

### MDK 0.9.10

[MDK 0.9.10](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.10), the Rust implementation of the [Marmot protocol](/en/topics/marmot/), retains pending sends while a transport is inactive and [supervises relay-notification forwarding](https://github.com/marmot-protocol/mdk/pull/1157) so inbound delivery recovers after lag, panic, or closure. [PR #1159](https://github.com/marmot-protocol/mdk/pull/1159) adds durable, paginated conversation history and full reply context for local agents, and [PR #1167](https://github.com/marmot-protocol/mdk/pull/1167) republishes the current signed KeyPackage event instead of generating a replacement. The release also preserves manual chat ordering, supports terminal group disbanding, and expands Web of Trust-ranked search, relay policy APIs, and language bindings.

### pakstr 0.3.1

[pakstr 0.3.1](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.3.1) lets web teams packaging a Nostr client for Android supply runtime configuration and an API proxy without rebuilding the app shell. Its [same-day release series](https://git.nostrdev.com/stuff/pakstr/releases) added an Amber signer bridge, [NIP-44 (encrypted payloads)](/en/topics/nip-44/) encryption and decryption, and corrected Android permission injection before the 0.3.x runtime-configuration work. The scaffold keeps bundled web assets local while deployment-specific settings arrive at runtime, and the proxy gives the wrapped app a controlled route for API requests alongside its ordinary relay connections.

### Ditto 2.34.2

[Ditto 2.34.2](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.34.2), a customizable Nostr social client, renders user statuses as cards in feeds, detail pages, and quote embeds, including custom emoji, expiry, and optional link previews. Zaps with comments now appear as replies beneath the referenced post. The release also retains the optional profile globe button from 2.34.1 for owners who publish a [NIP-5A (website manifest)](/en/topics/nip-5a/) root site, and fixes homepage navigation, live-stream search, external-link handling, and broken custom emoji.

### Earthly 0.0.9

[Earthly 0.0.9](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.0.9), a collaborative map editor built on Nostr, now keeps likes visible when a map entity drawer closes, reopens, or refreshes. Its [NIP-57 (Lightning zaps)](/en/topics/nip-57/) flow sends valid zap-request JSON so Lightning providers can publish verified receipts to publicly reachable relays, including during local development. Generated invoices remain visible across entity-surface changes, and the app shows confirmation after a verified receipt arrives.

## In Development

### Keep adds kind-scoped NIP-44 v3 signing and tightens approval policy

Keep merged five Android signer changes that carry [NIP-44 (Encrypted Payloads)](/en/topics/nip-44/) v3 encrypt and decrypt requests through both [NIP-55 (Android Signer Application)](/en/topics/nip-55/) transports and its [NIP-46 (Nostr Connect)](/en/topics/nip-46/) bunker. [PRs #451](https://github.com/privkeyio/keep-android/pull/451), [#452](https://github.com/privkeyio/keep-android/pull/452), and [#453](https://github.com/privkeyio/keep-android/pull/453) keep v3 grants separate from v2, scope them by event kind, reject missing or invalid kinds, and preserve approval requests opened from notifications. [PRs #454](https://github.com/privkeyio/keep-android/pull/454) and [#455](https://github.com/privkeyio/keep-android/pull/455) stop treating the Basic signing policy as Auto and move the global selection into the core-owned encrypted store. The Keep maintainers merged all five changes after the latest tagged Android release.

### Routstrd changes its default network bind after an unauthenticated exposure

Routstrd [PR #56](https://github.com/Routstr/routstrd/pull/56) changes the local Nostr inference router's default bind address from all network interfaces to `127.0.0.1`. The former default exposed unauthenticated wallet balance, history, unlock, send, refund, API-key, provider, client, usage, and daemon-stop endpoints to any host that could reach the port. Operators can still configure a non-local bind explicitly, but the merged change makes a fresh deployment local-only by default and has not yet appeared in a tagged release.

### Imwald Android clarifies offline publishing status

Imwald Android, an Android Nostr client, now treats acknowledgement from a local relay as a completed publish only when every configured target is local. Its [offline-publishing and outbox fix](https://git.imwald.eu/silberengel/imwald-android/commit/f4de9f61df35110c77d2e5f99d764c0df176962b) keeps remote delivery pending when a local relay has accepted the event but configured remote relays have not, so the publish report distinguishes device-local storage from relay delivery.

### FIPS opens an OpenWrt access layer and starts a FreeBSD port

The Free Internetworking Peering System now lets an OpenWrt router expose an open `!FIPS` access network through [merged PR #126](https://github.com/jmcorgan/fips/pull/126). The parallel [FreeBSD PR #129](https://github.com/jmcorgan/fips/pull/129) ports the daemon, TUN data path, `.fips` name resolution, service management, and native package build. Together, the changes widen the paths into the encrypted peer-to-peer network from dedicated routers to another general-purpose operating system.

A July 26 [FIPS project update](https://primal.net/e/d0afe733f75e909341ab7f39834883968df097472238a474df3a3346c5d38f51) reported more than 300 nodes on its public UDP overlay and a broader mesh approaching 2,000 nodes. The [FIPS repository](https://github.com/jmcorgan/fips) spent the same week hardening concurrent network tests, rekey continuity, hop-limit behavior, firewall checks, and NAT-lab isolation. Those changes give operators reproducible behavior checks as the network grows.

### Zap Cooking schedules posts and binds scanner requests

Zap Cooking, a Nostr recipe-sharing and meal-planning app, can now retain a scheduled post in encrypted storage and publish it when due through a periodic relay sweep ([PR #566](https://github.com/zapcooking/frontend/pull/566), [PR #569](https://github.com/zapcooking/frontend/pull/569)). That gives users a scheduled-publishing path without leaving unsigned post content exposed in the scheduler's database.

Its fridge scanner now authenticates the exact request body with [NIP-98](/en/topics/nip-98/) HTTP authentication, so membership checks rely on the key that signed the scan request instead of a pubkey supplied in its body ([PR #599](https://github.com/zapcooking/frontend/pull/599)).

### Citrine turns an Android device into a manageable relay

Citrine, an Android-hosted Nostr relay, can now send events it has stored to external relays, giving an operator a way to rebroadcast local history ([PR #179](https://github.com/greenart7c3/Citrine/pull/179)). It also adds [NIP-86 (Relay Management API)](/en/topics/nip-86/) commands so compatible clients can administer the relay ([PR #150](https://github.com/greenart7c3/Citrine/pull/150)).

Group operators can administer [NIP-29](/en/topics/nip-29/) relay-based groups through Amber signing in [PR #178](https://github.com/greenart7c3/Citrine/pull/178), while [PR #174](https://github.com/greenart7c3/Citrine/pull/174) keeps Tor-backed relay configuration and lifecycle state aligned through restarts.

### Wired recovers complete conversations in the browser

Wired, a browser-based Nostr client, now follows feed roots, replies, and referenced events to completion instead of stopping at fixed breadth or result limits ([PR #148](https://github.com/smolgrrr/Wired/pull/148), [PR #147](https://github.com/smolgrrr/Wired/pull/147), [PR #146](https://github.com/smolgrrr/Wired/pull/146)). Users can therefore recover deeper threads and feed context when the relevant events are available from their relays.

The browser also preserves relay hints on referenced events and uses them only for still-missing context, restoring conversations that configured relays do not carry ([PR #145](https://github.com/smolgrrr/Wired/pull/145), [PR #144](https://github.com/smolgrrr/Wired/pull/144)). Incomplete retrieval is kept distinct from a completed snapshot, so a partial response does not overwrite the prior cached view.

## Protocol and Spec Work

### NIPs: NIP-34 hosting boundary, group migration, and three live drafts

Two specification changes merged this week. [NIP-34 commit 6d2979b](https://github.com/nostr-protocol/nips/commit/6d2979b3f503a8539c983efbcdcf901bbcf9ed23) removes GRASP hosting instructions from the `kind:1618` pull-request description, leaving hosting and fallback behavior outside the event contract. [NIP-29 commit db5fe3d](https://github.com/nostr-protocol/nips/commit/db5fe3de8c5d1443b634c9bbf66ecb004f337057) defines how relay-group metadata migrates to another relay and how clients distinguish a valid move from a fork that continues independently.

[PR #2424](https://github.com/nostr-protocol/nips/pull/2424) proposes mutual `kind:10045` key-set declarations, so one identity cannot attach another key without a reciprocal event. [PR #2421](https://github.com/nostr-protocol/nips/pull/2421) proposes BOLT12 zap intents and payer proofs that clients can validate against the target, amount, offer, and settled payment without depending on a recipient-operated receipt server.

[PR #2425](https://github.com/nostr-protocol/nips/pull/2425) would let NIP-B0 bookmarks retain non-HTTP schemes such as `nostr:` alongside web URLs. That keeps native Nostr identifiers, payment requests, and other application schemes intact inside the same private or public bookmark lists that already carry web addresses.

### Mill implements a draft for cloud-account key backup

Mill [announced](https://primal.net/e/6362d9b00662fa64200530f8a29ae547521bac0a1e3c9379ef9086eac7d2030b) an implemented [cloud-account key-backup draft](https://github.com/0ceanSlim/nostr-mill/blob/main/docs/nip-cloud-key-backup.md) that combines a Google OIDC account identifier with a high-entropy passphrase to derive a disposable backup key. Its [reference implementation](https://github.com/0ceanSlim/nostr-mill/blob/main/src/nipbackup.js) encrypts the user's real key as a [NIP-49 (Private Key Encryption)](/en/topics/nip-49/) `ncryptsec`, then stores it in a provisional parameterized-replaceable kind `30049` event on configured relays. The project [merged the flow to main](https://github.com/0ceanSlim/nostr-mill/commit/eeb4b9114d02114b703a6823ad36ca8063b224da), but no post-v1.0.0 release includes it and the feature stays disabled unless an operator supplies dedicated `backupRelays`. The draft pins a versioned relay set whose concrete purpose-run endpoints remain provisional and warns that published ciphertext remains available for offline passphrase guessing. The design depends on a high-entropy passphrase, and readers should treat it as an implemented experiment.

### BUDs: Blossom servers may identify unknown uploads from their bytes

[BUD-02 PR #110](https://github.com/hzrd149/blossom/pull/110) now recommends server-side MIME detection when an uploader omits `Content-Type` or sends `application/octet-stream`. A Blossom server would inspect the first bytes with a maintained file-type library, preserve a specific client-supplied type, and fall back to the generic binary type when detection fails. That keeps images, audio, video, and agent-produced files renderable without making byte sniffing mandatory for every upload.

### NAPs: conventions replace numbered tracks as capture and filesystem contracts develop

[PR #87](https://github.com/napplet/naps/pull/87) removes the numbered cross-napplet protocol track and keeps runtime capabilities under named contracts while application messages converge on `napplet:<archetype>/<intent>` convention URIs. The merged [topic-identity change](https://github.com/napplet/naps/pull/89) separates a stable, queryless convention path from per-message payload data, and [PR #90](https://github.com/napplet/naps/pull/90) applies that transposition rule to discovery and handler metadata.

Two NAP drafts extend the trusted shell boundary. [NAP-CAPTURE PR #94](https://github.com/napplet/naps/pull/94) keeps microphone consent, platform permission, limits, retention, and teardown in the runtime while returning a bounded media artifact to a sandboxed napplet. [NAP-FS PR #88](https://github.com/napplet/naps/pull/88) is the parallel virtual-filesystem proposal, with policy-bound handles instead of unrestricted host paths.

### Marmot: the specification defines a terminal group state

[Marmot PR #409](https://github.com/marmot-protocol/marmot/pull/409) adds an authenticated, irreversible `Disbanded` state because MLS itself has no group-deletion operation. An authorized admin commit moves a group out of `Active`, blocks old branches, messages, and Welcomes from reviving it, and gives existing groups an explicit compatibility path before they can disband. The preceding [specification issue sweep](https://github.com/marmot-protocol/marmot/pull/408) also reconciled group-state authority, convergence, key packages, acknowledgements, media rules, registry language, and 200 tracked specification issues.

### Gamma Markets: no public specification changes landed

The [Gamma Markets specification repository](https://github.com/GammaMarkets/market-spec) recorded no public commits or pull-request activity from July 21 through July 28. Its published order, settlement, and market-data documents remain the current baseline; this no-change entry keeps Gamma visible in the weekly specification sweep.

### Concord: read and write capabilities may split inside one plane

[Concord PR #12](https://github.com/concord-protocol/concord/pull/12) remains an open draft for planes whose readers should not all be writers. It moves the Control Plane toward separate read and write stream capabilities and sketches restricted-write channels, invites, and rekey scopes. The write key is a spam gate in the draft, while signed inner actors and roster checks continue to carry authority.

### NWC: one wallet method can choose between BOLT11 and BOLT12

[NWC PR #2](https://github.com/nostr-wallet-connect/nwc/pull/2) proposes optional `pay` and `receive` methods for BIP-321 payment URIs. A wallet service can advertise support, choose one compatible BOLT11 invoice or BOLT12 offer from a URI, reject a mismatched Bitcoin network before payment, and report which instruction type it used. The proposal stays outside the NWC core so wallets without BIP-321 or BOLT12 support do not have to implement it.

## Six Years of Nostr Julys

July's history records Nostr moving its trust boundaries outward. It began by making a public key legible through a domain, then taught relays what they could retrieve and reject, then gave applications portable objects for work and payment. The later Julys focus on preserving privacy, state, and interoperability when identity, clients, relays, signers, wallets, and ordinary web URLs no longer live in one place. [The first NIP-05 implementation](https://github.com/nbd-wtf/nostr-tools/commit/1ce00bd3b6909f78f212a7a172cf845b55280599) and [this month's addressable-discovery draft merge](https://github.com/nostr-protocol/nips/commit/2f4b09335c54a993d483bc220195e3f4a33df1ec) mark the ends of that arc.

### July 2021

On July 19, 2021, [nostr-tools commit 1ce00bd](https://github.com/nbd-wtf/nostr-tools/commit/1ce00bd3b6909f78f212a7a172cf845b55280599) added a `nip05.js` module and raised the package to version 0.5.0. Its `keyFromDomain` function built a DNS TXT request for `_nostrkey.<domain>`, posted the binary query to one of eight rotating DNS-over-HTTPS providers, and returned the first key in the answer. A browser client could therefore translate a human-controlled domain into a public key without operating a DNS resolver or relying on one hard-coded provider.

That first approach solved lookup but not names within a domain, and its trust boundary sat in DNS plus the selected resolver. The modern [NIP-05 specification](https://github.com/nostr-protocol/nips/blob/master/05.md) moved discovery to `/.well-known/nostr.json`, where a domain maps local names to pubkeys and can attach relay hints. The 2021 code records the earlier design pressure: public keys were portable, but people still needed identifiers they could read, verify, and move between clients.

### July 2022

On July 10, [NIP-12 commit 3771186](https://github.com/nostr-protocol/nips/commit/3771186c0351656a675576051b75d253f26c0f0b) limited generic relay queries to single-letter tags. That decision made filters such as `#r`, `#g`, and `#t` useful for URL references, geohashes, and hashtags without asking relays to index every arbitrary metadata key. Ten days later, the first [NIP-20 web-comments draft](https://github.com/nostr-protocol/nips/commit/9f9a864ce1e1ebfdcfdd4835cd60807440f038e8) used that query model directly: a kind `34` comment carried a normalized webpage URL in an `r` tag, allowing a site and independent clients to recover the same discussion from relays.

Relay policy and social feedback followed. The original [NIP-22 commit](https://github.com/nostr-protocol/nips/commit/f51ce9dc0efaf61f39a76e112c310a9f58af1c87) let relays reject events whose `created_at` timestamp was implausibly old, and [commit 8bef0e9](https://github.com/nostr-protocol/nips/commit/8bef0e9d79ebb4b11f8fd2bea11dc8f1668bc9d0) added future timestamps to the same policy. On July 30, [NIP-25 commit dcbd504](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88) defined kind `7` reactions with target `e` and `p` tags; the next commit assigned `-` to a negative reaction, and [commit 6903ff5](https://github.com/nostr-protocol/nips/commit/6903ff5b2c395a550a26069f6e2b5460ae1fdca6) made `+` the explicit generic like. By month's end, relays had clearer admission rules and clients had interoperable comments, likes, dislikes, emoji, and tag-based retrieval.

### July 2023

July 2023 pushed coordination beyond short notes. The [NIP-37 lost-key draft](https://github.com/nostr-protocol/nips/commit/e057fa01ca3928a32bdc0e9a44c27f946f267041) explored irreversible key retirement, social recovery thresholds, and precommitted replacement keys while explicitly refusing to call the result universal key rotation. Five days later, [NIP-53](https://github.com/nostr-protocol/nips/commit/141197c564d97073f0293e3b2f367f0b6b3619c2) introduced addressable kind `30311` live activities and kind `1311` chat messages, giving streams, stages, and live rooms a shared event model for hosts, participants, status, and conversation.

Applications also began advertising work and commerce. The first [Data Vending Machine draft](https://github.com/nostr-protocol/nips/commit/67e950a2009e81df1b8c91b0a2ade0596e83f168) described kind `68001` job requests, kind `68002` results, bids, expirations, chaining, and competitive providers for tasks such as transcription, summarization, and translation. On July 13, the [classified-listing draft](https://github.com/nostr-protocol/nips/commit/451c06a3c572a13afe45c1d80616f8e6dd9bb1de) added addressable kind `30402` offers with title, summary, price, location, and status metadata. Those drafts later became NIP-90 and NIP-99, but their July forms already separated a request or listing from the server that displayed it.

Payment routing became composable too. The July 31 [NIP-57 zap-splits merge](https://github.com/nostr-protocol/nips/commit/5d63b1570c490007252b10e757f7f68ef1f4b717) changed a single `zap` destination into a weighted list of recipient pubkeys and relay hints. A client could divide one zap among collaborators, omit unweighted recipients when some weights were present, and show the split before payment. That small tag change made revenue sharing a signed-event field portable among applications.

### July 2024

On July 4, [NIP-29 commit c60ca88](https://github.com/nostr-protocol/nips/commit/c60ca888efbdc9b8fa4bbfbace372409d0b2161a) added the `kind:9007` relay moderation action for creating a group. Six days later, [NIP-70](https://github.com/nostr-protocol/nips/commit/ae1906ec7943a6bd756f05d2cd2fb2a041398921) defined protected events: a `-` tag tells a relay to accept publication only from the event's authenticated author. One change gave relays an explicit group-state transition; the other let authors prevent third parties from replaying otherwise valid signed events into relays.

On July 17, one [Cashu specification commit](https://github.com/nostr-protocol/nips/commit/506b38916ab67a37b2d98b46b62cf0c0c5fde5a4) introduced both NIP-60 wallets and NIP-61 nutzaps. NIP-60 placed wallet metadata in kind `37375`, unspent proofs in encrypted kind `7375` events, and optional transaction history in kind `7376`. NIP-61 paired the recipient's kind `10019` mint and relay preferences with P2PK-locked kind `7337` nutzaps. Wallet state and bearer tokens could now move through relays, while redemption still depended on Cashu mint proofs and careful prevention of double claims.

Two late-July edits tightened deterministic state. [NIP-01 commit 9c54549](https://github.com/nostr-protocol/nips/commit/9c54549f1842245b842d8a66f3bade744da24189) required event IDs as the tie-breaker after equal `created_at` timestamps, so clients could sort identical result sets the same way. The [NIP-09 deletion merge](https://github.com/nostr-protocol/nips/commit/722ac7a58695a365be0dbb6eccb33ccd7890a8c7) clarified that kind `5` requests may target event IDs or addressable coordinates and should include `k` tags identifying the kinds that relays should delete. Both changes narrowed places where two correct implementations could otherwise disagree.

### July 2025

Ecash discovery gained its own social directory on July 16. [NIP-87 commit 1afb6da](https://github.com/nostr-protocol/nips/commit/1afb6da049e57dd628ef46a3b0f90300653a66ee) defined kind `38172` Cashu-mint records, kind `38173` Fedimint records, and kind `38000` recommendations that can point to those records with relay hints. Wallets could query trusted authors' recommendations before connecting to a mint, while the specification warned that unfiltered global discovery could steer users toward malicious operators.

Voice acquired a portable record one week later. The first [NIP-A0 commit](https://github.com/nostr-protocol/nips/commit/e50f37a527ace39cc3057827d52295c6b6de1112) assigned kind `1222` to a voice-message root and kind `1244` to a reply, carrying an audio URL plus media metadata. The July 27 [format follow-up](https://github.com/nostr-protocol/nips/commit/4984b057c20397eae919ee5e463bc8a5d3fb2dc0) recommended Opus in an Ogg container and standardized a compressed waveform. Clients could exchange short audio without agreeing on one recorder, host, or waveform representation.

Private messaging and wallet connections then added visible state negotiation. [NIP-17 commit 3d76da3](https://github.com/nostr-protocol/nips/commit/3d76da368e157934e056d95b3b3d8d6eaa105b09) defined a replaceable kind `30016` record whose ordered `seen` tags let a client distinguish read messages from gaps it may have missed. On July 31, [NIP-47 encryption negotiation](https://github.com/nostr-protocol/nips/commit/f30a43bd37e08516923b96dd0d860122c9ffe04e) let wallet services advertise NIP-44 v2 or legacy NIP-04, while the [transaction-state commit](https://github.com/nostr-protocol/nips/commit/0595d438aaa163dd33ed00748026698a411a0861) added `pending`, `settled`, `accepted`, `expired`, and `failed` states. Delivery, encryption, and payment progress became explicit protocol data instead of local inference.

### July 2026

This July began by connecting ordinary web addresses to relay queries. [Addressable-discovery commit 2f4b093](https://github.com/nostr-protocol/nips/commit/2f4b09335c54a993d483bc220195e3f4a33df1ec) defines a `/.well-known/nostr.json?ad=<path>` lookup whose answer contains a Nostr filter and relay list. A normal browser can still open the URL as HTML, while a Nostr client can resolve the same address into a group, nsite, feed, event, or other native object. The pattern revisits 2021's domain-to-key problem at a broader layer: one human-readable URL can now name both an identity and a query.

NIP-29 then grew from flat relay groups into structured spaces. The July 15 [subgroup commit](https://github.com/nostr-protocol/nips/commit/223ddb3b0c282f2a133adb9f4a9c098a31b36937) added parent and ordered-child relations; adjacent commits added invite-code suffixes, banners, ordered pin snapshots, and addressable-event pins. On July 22, the [migration and fork clarification](https://github.com/nostr-protocol/nips/commit/db5fe3de8c5d1443b634c9bbf66ecb004f337057) defined when metadata legitimately moves a group to another relay and when a still-active branch is an independent fork. The group identifier stayed simple while hierarchy, presentation, and relay changes became explicit state.

Two smaller edits clarified implementation boundaries. [NIP-46 commit f0af204](https://github.com/nostr-protocol/nips/commit/f0af20484c5e0d12e2d1936f87c5a6681a08daff) requires a remote signer to return an error for unknown or unsupported methods instead of leaving a client to time out silently. [NIP-34 commit 6d2979b](https://github.com/nostr-protocol/nips/commit/6d2979b3f503a8539c983efbcdcf901bbcf9ed23) removes GRASP-specific hosting directions from the pull-request event description. One gives callers a terminal response; the other keeps a portable git event from silently inheriting one server protocol.

---

Send a NIP-17 DM to share a project or news item through the [Nostr Compass project](https://github.com/andotherstuff/nostr-compass).
