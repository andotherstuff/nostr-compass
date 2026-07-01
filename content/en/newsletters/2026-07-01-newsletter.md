---
title: 'Nostr Compass #29'
date: 2026-07-01
publishDate: 2026-07-01
draft: false
type: newsletters
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** [FIPS v0.4.0](#fips-v040-ships-nym-mixnet-transport-mdns-discovery-and-a-data-plane-overhaul) ships a Nym mixnet transport, opt-in mDNS LAN discovery, hitless rekey under loss, and a data-plane overhaul, wire-compatible with v0.3.0. [Whitenoise Linux](#whitenoise-linux-surfaces-as-a-desktop-marmot-client) surfaces as a desktop Marmot client in Rust and Slint with a protocol proposal to move message effects to a dedicated kind-9 event. [CustID v0.1.10-beta](#custid-launches-as-a-mobile-identity-vault-with-nip-46-and-nfc-challenge-flow) launches as a hardware-backed mobile identity vault acting as a NIP-46 remote signer and answering physical access challenges over NFC. [myco](#myco-launches-peer-to-peer-nsite-sharing-over-the-fips-mesh) launches peer-to-peer nsite sharing over the FIPS mesh with a new BLE L2CAP transport in v0.1.0. [Nostr Codex Phone](#nostr-codex-phone-launches-as-a-mobile-control-surface-for-a-local-codex-worker-over-nostr) launches as an Android control surface for a local Codex coding-assistant over encrypted Nostr DMs. [Amethyst's unreleased line](#amethyst-builds-nip-89-aware-ui-a-git-repositories-feed-and-a-napplet-browser-discover-section) adds NIP-89 app-handler parsing, a Git Repositories feed for NIP-34, and a Discover section for nSites and napplets. [Notedeck](#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments) lands NIP-37, NIP-52, and NIP-22 in one week. [Applesauce](#applesauce-ships-12-sub-packages-in-a-coordinated-62x-cut) cuts 12 sub-package releases with nbunksec NIP-46 helpers and a Cashu-ts v4 wallet upgrade. [Meiso v1.4.0](#meiso-v140-ships-shared-key-collaborative-lists-that-replace-mls-for-task-sharing) ships Shared-Key Collaborative Lists on addressable kind-35000. The NIPs repository merged five PRs including a relay roles event, the NIP-44 65,535-byte limit removal, NIP-34 fork semantics, NIP-46 client metadata, and a NIP-86 signevent method. Deep dives cover [NIP-86 (Relay Management API)](#nip-deep-dive-nip-86-relay-management-api) and [NIP-89 (Recommended Application Handlers)](#nip-deep-dive-nip-89-recommended-application-handlers).

---

## Lead stories

### FIPS v0.4.0 ships Nym mixnet transport, mDNS discovery, and a data-plane overhaul

[FIPS](https://github.com/jmcorgan/fips) is a private, self-organizing peer-to-peer mesh network for Nostr where nodes discover each other and route traffic without central infrastructure. [FIPS v0.4.0](https://github.com/jmcorgan/fips/releases/tag/v0.4.0) lands a Nym mixnet transport, opt-in mDNS LAN discovery, a data-plane overhaul, hitless rekey under packet loss, a rewritten `fipstop` TUI on a render-snapshot harness, an off-hot-path observability plane, and new OpenWrt apk and Nix flake packaging targets, all wire-compatible with v0.3.0 so mixed meshes interoperate during a rolling upgrade. Two new transports for peer discovery anchor the release. A new [outbound Nym mixnet transport](https://github.com/jmcorgan/fips/releases/tag/v0.4.0) routes FIPS traffic through a `nym-socks5-client` SOCKS5 proxy, mixing it into the [Nym](https://nymtech.net/) cover-traffic network so link-level observers cannot correlate which mesh peers are talking, and an `examples/sidecar-nostr-mixnet-relay/` directory demonstrates a Nostr relay reachable over a FIPS link peered end-to-end across the mixnet. Opt-in mDNS / DNS-SD LAN discovery lets nodes on the same local link find each other with no address configuration and no STUN, advertising and adopting peers through a standard service record on `node.discovery.lan.enabled: true`.

The data plane was reworked for higher single-node throughput. Per-peer encrypt and decrypt now run on dedicated worker tasks off the receive loop, so one busy peer cannot serialize the whole node's crypto. The Linux send path uses generic segmentation offload and a connected-UDP socket where available, the receive hot path avoids buffer copies it previously made per packet, and macOS picks up a `recvmsg_x` batched receive to mirror the Linux `recvmmsg` batching from v0.3.0. The entire `show_*` read surface for `fipsctl` and `fipstop` now serves from a per-tick snapshot published into a lock-free `ArcSwap` from the control accept task, so operator queries answer promptly on a node whose receive loop is busy. A new counter-only `show_metrics` query (surfaced as `fipsctl stats metrics`) enables Prometheus scraping at no hot-path cost.

FMP and FSP session rekey are now hitless under packet loss and reordering in both directions: inbound frames authenticate against the pending session before the K-bit cutover promotes it (so a stale or spoofed frame cannot derail rekey), rekey message-1 retransmission is bounded, the link-dead heartbeat is rekey-aware, and dual-initiation races on high-latency links are desynchronized with symmetric jitter. The `fipstop` TUI is rebuilt on a render-snapshot harness that asserts the exact text grid and per-cell style of every view against canned control-socket output. New packaging targets ship alongside: an OpenWrt `.apk` for OpenWrt 25+ (built SDK-free, reusing the existing `.ipk` cross-compile and installed-filesystem payload) and a `flake.nix` at the project root that builds all four binaries (`fips`, `fipsctl`, `fips-gateway`, `fipstop`) from source on Nix/NixOS with the pinned toolchain.

### Whitenoise Linux surfaces as a desktop Marmot client

[Whitenoise Linux](https://relay.ngit.dev/npub1ven4zk8xxw873876gx8y9g9l9fazkye9qnwnglcptgvfwxmygscqsxddfh/darkmatter-linux.git) is a desktop [Marmot](/en/topics/marmot/) client: MLS group messaging over Nostr relays, packaged as a single Rust binary with a Slint UI that keeps every secret in one password-encrypted vault.

The most consequential thread this week proposes carrying Whitenoise message effects as a dedicated kind-9 event referencing the parent message. Today's wire format appends a marker like `dmfx:sparkle` to the end of the message body, which pollutes the text for any renderer that does not know the convention. Moving effects to their own event keeps message text clean, and it opens a design question the wider Marmot stack is going to face: inline body conventions or sidecar events for optional rich features.

### CustID launches as a mobile identity vault with NIP-46 and NFC challenge flow

[CustID v0.1.10-beta](https://zapstore.dev/apps/naddr1qq9rzqtdwfshxwf0wccsygqv94d2qg37755z67q9yjz6q60lcejldsc3ttak83333gjqgyvf3aqpsgqqqyf6w24n0c) is the first public beta of CustID, a mobile identity vault built on Nostr and the SISTR protocol. CustID stores multiple Nostr identities in hardware-backed secure storage, acts as a [NIP-46](/en/topics/nip-46/) remote signer for other clients, and answers physical and online access challenges over NFC and QR codes.

The beta is feature-complete for the NIP-46 signer and NFC challenge-response flow; zero-knowledge-proof access flows remain a future milestone. This release also drops the app's background [NIP-65](/en/topics/nip-65/) keep-alive layer, which had been opening a WebSocket per profile per read relay and ingesting kinds the client immediately discarded. Only the NIP-46 sockets that carry signing-request notifications are kept alive in the background now, which is the fix that makes running CustID as a bunker for other clients viable on a phone.

### myco launches peer-to-peer nsite sharing over the FIPS mesh

[myco v0.1.0](https://github.com/Origami74/myco/releases/tag/v0.1.0) opened this week on June 27 and reached v0.1.0 on July 1. myco is a Rust Android app that installs apps from the people around you: peer-to-peer [nsite](/en/topics/nip-5a/) sharing over a FIPS mesh, with any transport the mesh can carry (UDP, TCP, Tor, Bluetooth), working fully offline. The design pairs directly with FIPS as the transport substrate and with NIP-5A's static-website event format as the payload, letting an app distributed as an nsite move between mesh peers without depending on relays or HTTP.

v0.1.0 adds an L2CAP Bluetooth radio path so two phones with FIPS installed can peer over BLE without any network, plus a per-peer speedtest and NFC-triggered sharing from the app's Circle bottom-sheet. myco is also published to Zapstore for direct install.

### Nostr Codex Phone launches as a mobile control surface for a local Codex worker over Nostr

[Nostr Codex Phone v0.1.122](https://github.com/tidley/nostr-codex-phone) launches this week as an Android client that controls a local Codex coding-assistant worker over encrypted Nostr direct messages. The app supports multiple repository sessions, voice transcription, routed worker sessions, Blossom media uploads, and optional spoken responses, so a developer running a Codex worker at home can dispatch requests from their phone anywhere the phone has relay access.

The project is a direct sibling to [CodeDeck](/en/newsletters/2026-06-24-newsletter/#codedeck-remote-agentic-coding-over-nostr) launched in #28. Both put agentic-coding workflows on Nostr transport with encrypted DMs, and both treat Nostr as the pairing and messaging layer that lets a phone reach a home worker without punching holes through the network. Nostr as a control-plane for local agents is becoming an established pattern.

### Coop Mobile publishes its first versioned builds

[Coop Mobile v0.2.1](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.1) and [v0.2.2](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.2) shipped this week as the first versioned builds of Coop Mobile, a [NIP-17](/en/topics/nip-17/) encrypted direct-messaging client for Android. The two releases tighten crash safety around message parsing and QR handling, and wipe all stored data on logout.

### Amethyst builds NIP-89-aware UI, a Git Repositories feed, and a napplet Discover section

[Amethyst's](https://github.com/vitorpamplona/amethyst) main branch built out several new surfaces this week. A [Git Repositories feed](https://github.com/vitorpamplona/amethyst/pull/3406) turns [NIP-34](/en/topics/nip-34/) repos into a browsable Android timeline category, filterable by community and author, paired with a [smart-HTTP git browser](https://github.com/vitorpamplona/amethyst/pull/3415) that reads repo contents and commits without leaving the app. The napplet host gained a [Discover section](https://github.com/vitorpamplona/amethyst/pull/3409) listing curated web apps plus followed nSites and napplets, sourced from [NIP-89](/en/topics/nip-89/) handler events and [NIP-5A](/en/topics/nip-5a/) site events. Note display now [reveals which Nostr app authored an event](https://github.com/vitorpamplona/amethyst/pull/3422) via NIP-89 tags. On the sync side, [NIP-77 negentropy support](https://github.com/vitorpamplona/amethyst/pull/3434) lands with streaming reconciliation and automatic `created_at` windowing to work around relay-side result caps, cutting bandwidth needed to keep large local event sets in sync with a relay.

### Buzz v0.3.38 hardens the relay attack surface and adds provider-agnostic model selection

[Buzz v0.3.38](https://github.com/block/buzz/releases/tag/v0.3.38) hardens the [relay attack surface](https://github.com/block/buzz/pull/1369) that Buzz exposes when it publishes personas, teams, managed agents, and NIP-OA owner attestations as signed Nostr events. A Buzz relay is a public record of the team's Nostr identities and their state, and this release tightens input validation and replay protection on the well-known event kinds Buzz defines. The release also generalizes model selection so a Buzz team can point at any provider Buzz has adapters for, including a new Databricks AI Gateway v2 backend.

### Notedeck implements NIP-37 private-sync relays, NIP-52 calendar, and NIP-22 comments

[Notedeck](https://github.com/damus-io/notedeck), the Damus team's native Rust desktop client, landed three protocol implementations in one week. Private-sync relays now persist as a kind `10013` [NIP-37](/en/topics/nip-37/) list, separating the user's private-content relay set from their public NIP-65 outbox. The `horizon` calendar pane reads [NIP-52](/en/topics/nip-52/) events from nostrdb and got a three-pane layout redesign. The `headway` pane added a [NIP-22](/en/topics/nip-22/) comment-event model on kind `1111`, the kind NIP-22 defines for the unified comment surface that replaces NIP-10 reply threading.



### Applesauce lands nbunksec NIP-46 sessions and a Cashu v4 wallet upgrade

[Applesauce](https://github.com/hzrd149/applesauce), the modular Nostr toolkit for signers, relays, wallets, and content, cut a coordinated [6.2.x release](https://github.com/hzrd149/applesauce/releases) across its sub-packages. The signers package gained `nbunksec` import and export helpers, treating a [NIP-46](/en/topics/nip-46/) bunker session as a portable artifact that can move between clients. The wallet package upgraded its [Cashu](/en/topics/nip-60/) bindings to `@cashu/cashu-ts` v4, where proof amounts become `Amount` value objects and the token-decoding API changes.

---

## Tagged releases

### mostro-core v0.14.0

[mostro-core v0.14.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.0) lands the next protocol iteration for the [Mostro](/en/topics/nip-69/) P2P fiat trading network. The release follows [v0.13.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.2) and ships alongside [mostro-cli v0.16.0](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.0) which adopts the new core. Three merged PRs landed in the core repository this week; the surrounding stack (mostro daemon and Mostro mobile) tracks against v0.14.0 of the shared types crate.

### ngit v2.6.1

[ngit v2.6.1](https://github.com/DanConwayDev/ngit-cli), the canonical git-over-nostr CLI for [NIP-34](/en/topics/nip-34/) repositories, implements this week's merged [NIP-34 GRASP-06 fork semantics](https://github.com/nostr-protocol/nips/pull/2395) that replace the `personal-fork` tag with a `u` tag on repo-state events.

### mesh-llm v0.72.0 and v0.72.1

[mesh-llm](https://github.com/Mesh-LLM/mesh-llm), the inference component of the ContextVM stack that runs open-source LLMs behind a Nostr-addressable JSON-RPC surface, shipped [v0.72.0](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.0) and [v0.72.1](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.1) with a fix for a batching crash on large single prompts and an MCP-bridge migration off deprecated helpers.

### Meiso v1.4.0 ships Shared-Key Collaborative Lists that replace MLS for task sharing

[Meiso v1.4.0](https://github.com/higedamc/meiso/releases/tag/v1.4.0) introduces a Shared-Key Collaborative Lists model that replaces the project's prior MLS-based task sharing with a simpler addressable-event design. Each shared list generates a dedicated Nostr key distributed to members, tasks are addressable events on kind `35000` keyed by `d=task-id` with [NIP-44](/en/topics/nip-44/) self-encrypted content, and relays enforce Last-Write-Wins per task. The design surrenders MLS's forward secrecy and post-compromise security in exchange for simpler client implementation and relay-level conflict resolution.

### Cordn 0.3.2

[Cordn 0.3.2](https://github.com/Cordn-msg/cordn) ships a "more-private-coordinator" track that removes ephemeral sender pubkeys from group message posting and hardens the join-request flow against stale re-requests. Cordn is the MLS-based messaging stack covered in [#28's Cordn Ad-hoc CVM launch](/en/newsletters/2026-06-24-newsletter/#cordn-ad-hoc-cvm-a-browser-based-mls-coordinator); this release is the matching coordinator-side update.

---

## Unreleased changes

### diVine pushes 108 merged PRs of post-launch polish

[diVine](https://github.com/divinevideo/divine-mobile), the short-form looping video client bringing back Vine, is in a heavy post-launch polish wave. The Nostr-visible work this week is a [NIP-46](/en/topics/nip-46/) connect-flow stability pass that migrates `nostrconnect://` failures onto structured reason codes.

### Zap Cooking continues the cross-project NIP-46 fix and composer overhaul

[Zap Cooking](https://github.com/zapcooking/frontend) is a Nostr recipe-sharing client where recipes are published as long-form Nostr events. This week's work continues the cross-project [NIP-46](/en/topics/nip-46/) fix and composer overhaul covered as unreleased in [#28](/en/newsletters/2026-06-24-newsletter/#unreleased-changes).

### Conduit hardens listing flow and marketplace correctness

[Conduit](https://github.com/Conduit-BTC/conduit-mono) is a three-app marketplace monorepo on Nostr covering the buyer market, merchant portal, and store builder. This week's work continues the marketplace correctness push covered in [#28's launch coverage](/en/newsletters/2026-06-24-newsletter/#conduit-hardens-the-marketplace-mvp-and-switches-to-its-public-relay-by-default), building on the [NIP-99](/en/topics/nip-99/) commerce wave that was the protocol-side story last issue.

### Pollerama v1.12 through v1.13.1 add client-tag choice, profile tabs, and thread caps

[Pollerama](https://github.com/formstr-hq/nostr-polls), an Android Nostr client focused on polls and notes with a strong web-of-trust discovery layer, shipped v1.12.0, v1.13.0, and v1.13.1 to Zapstore this week. Users can now pick which client tag is attached to their authored notes and polls, choosing from a preset list or entering their own. Deeply nested comment and reply chains now stop after a few levels and link out to the full thread on the note's page. Profile pages open on Notes by default, split into a Posts tab and a Conversations tab. A follow-persistence bug where newly-followed accounts disappeared after an app restart is fixed, and follow buttons now show progress.

### getwired.app and get-tao.app fix the NIP-13 confess submission flow

[getwired.app](https://github.com/smolgrrr/Wired) and [get-tao.app](https://github.com/smolgrrr/TAO), which share an anonymous-posting flow that adds NIP-13 proof-of-work to suppress spam at submit time, fixed the [confess submission flow](https://github.com/smolgrrr/Wired/pull/57) so the UX during PoW mining is coherent.

### nostui adds a mention timeline tab

[nostui](https://github.com/akiomik/nostui), a terminal Nostr client in Rust, added a [mention timeline tab](https://github.com/akiomik/nostui/pull/463) that surfaces kind:1 events tagging the active pubkey as a dedicated view in the TUI.

### Heartwood lands per-identity NIP-46 bunker URIs and an HSM-mode signing bridge

[Heartwood](https://github.com/forgesworn/heartwood) is a [NIP-46](/en/topics/nip-46/) signer where the signing key never reaches the client at all: the client speaks NIP-46 to a small relay, and the relay speaks a serial frame protocol to an attached hardware device that performs the signature. This week the project landed a [relay-to-serial signing bridge](https://github.com/forgesworn/heartwood/pull/11) and [per-identity bunker connections](https://github.com/forgesworn/heartwood/pull/16), so a single hardware device holding multiple identities exposes a distinct bunker URI for each one.

### Nostter auth and signer refactor

[Nostter](https://github.com/SnowCait/nostter) reworked its [auth and signer layer](https://github.com/SnowCait/nostter/pulls?q=is%3Amerged+auth) this week, moving login state onto a single signal and extracting the signer dispatch into strategy modules. The trajectory is a clean signer abstraction where NIP-07 web extension, NIP-46 remote bunker, and raw nsec all share one code path.

### Dart NDK extracts the NIP-07 signer and randomizes NIP-59 timestamps

[Dart NDK](https://github.com/relaystr/dart_ndk) moved its [NIP-07](/en/topics/nip-07/) signer out of the core package and into `ndk_flutter` (where the Flutter WebView lives), and [randomized its NIP-59 gift-wrap timestamps](https://github.com/relaystr/dart_ndk/pull/667) to harden against timing correlation of encrypted messages.

### Milk Market adds NIP-23 storefront pages and Square payment processing

[Milk Market](https://github.com/shopstr-eng/milk-market), the Shopstr-team marketplace storefront, gave every storefront a blog page backed by the seller's [NIP-23](/en/topics/nip-23/) long-form events, with editable sections and a direct blog-setting route. The same week added [Square](https://github.com/shopstr-eng/milk-market/pull/30) as an alternative payment processor for sellers and automatic shipping-label purchases for paid orders.

### Calendar by Formstr ships an iOS app

[Calendar by Formstr](https://github.com/formstr-hq/nostr-calendar) merged [PR #159 IOS App](https://github.com/formstr-hq/nostr-calendar/pull/159) this week, bringing the [NIP-52](/en/topics/nip-52/) calendar client to iOS. [PR #197](https://github.com/formstr-hq/nostr-calendar/pull/197) fixes calendar-date parsing in local time, and [PR #201](https://github.com/formstr-hq/nostr-calendar/pull/201) adds a Playwright E2E workflow triggered by a `run-tests` label.

### cagliostr enforces NIP-22, NIP-09 by coordinate, and NIP-13 proof-of-work

[cagliostr](https://github.com/mattn/cagliostr), a Go relay implementation, tightened three enforcement paths this week: [configurable NIP-13 proof-of-work](https://github.com/mattn/cagliostr/pull/7) on incoming events, [NIP-09 deletion by addressable coordinate](https://github.com/mattn/cagliostr/pull/8) so replaceable events can be deleted by their `a` tag (which event-id deletion alone cannot reach), and [configurable NIP-22 timestamp limits](https://github.com/mattn/cagliostr/pull/9) that reject events stamped too far in past or future.

---

## Newly tracked and discovered

The [Vanderwarker wellbeing suite](https://git.vanderwarker.family/wellbeing) publishes physical-world telemetry as Nostr events under a shared publisher signing key. It consists of five sibling apps: [Holy Fit](https://git.vanderwarker.family/wellbeing/holyfit-android) is a step tracker anchoring fitness data to Nostr as `kind:30078`, [Nunlock](https://git.vanderwarker.family/wellbeing/nunlock-android) publishes a daily phone-unlock counter, [Saint Stream](https://git.vanderwarker.family/wellbeing/saintstream-android) publishes current media playback as a User Status, [Sister Charge](https://git.vanderwarker.family/wellbeing/sistercharge-android) publishes battery level, voltage, and temperature every 15 minutes, and [Cellibacy](https://git.vanderwarker.family/wellbeing/cellibacy-android) publishes daily data usage. All five appeared on Zapstore between June 24 and June 30.

[ntrack v0.1.9](https://github.com/f321x/ntrack/releases/tag/v0.1.9) is an encrypted serverless live location-sharing Android app built in Rust and Slint, released June 29. It is a sibling to the [Haven](https://github.com/mehmetefeumit/Haven-App) [Marmot](/en/topics/marmot/)-based location sharer covered in [#28](/en/newsletters/2026-06-24-newsletter/#haven-launches-private-location-sharing-on-marmot), with a different transport architecture: encrypted Nostr DMs carry the location updates, where Haven uses Marmot group messages.

[NostrAppShell](https://git.nostrdev.com/stuff/NostrAppShell) is an early-stage application shell scaffold for building Nostr apps. The project published its first user-facing documentation this week.

[NIPs by Pollerama](https://nips.pollerama.fun) (repository [abh3po/better-nips](https://github.com/abh3po/better-nips), created 2026-06-29) is a new client for [NostrHub's](https://nostrhub.io) `kind:30817` community-authored NIPs, positioned as a trust-weighted alternative surface to nostrhub.io. Each `kind:30817` NIP has its own shareable URL (`#/nip/<naddr>`) with full Markdown rendering and the event kinds it defines. The client offers three feeds: Following, Web of Trust (follows-of-follows), and Global, each sortable by trust-weighted approvals or by newest. Approvals publish as [NIP-32](/en/topics/nip-32/) labels on kind `1985` with tags `["L","nostrhub"]` and `["l","approve","nostrhub"]` plus an `a` tag pointing at the target NIP address and a `client` tag advertising `better-nips`, which is the exact event shape NostrHub itself signs so approvals are cross-compatible between the two clients. A direct follow's approval carries more weight in the ranking than a second-degree follows-of-follows approval.

The signing stack is [`@formstr/signer`](https://www.npmjs.com/package/@formstr/signer) with a full login modal covering [NIP-07](/en/topics/nip-07/), [NIP-46](/en/topics/nip-46/) bunker and nostrconnect, [NIP-49](/en/topics/nip-49/) ncryptsec, and [NIP-55](/en/topics/nip-55/) Android signer, and sessions silently re-attach on reload. The network layer runs through [`@formstr/local-relay`](https://www.npmjs.com/package/@formstr/local-relay), a Web Worker that partitions the user's [NIP-65](/en/topics/nip-65/) outbox across relays so a large web-of-trust set does not fan out to a single relay. The design position is that community NIPs (whether hosted at NostrHub, in `better-nips`, or by other future clients) are all equal at the protocol level; ranking comes from the social graph, not from moderator curation, which pairs directly with the NIP-32 labeling flow the deep dive in [#25](/en/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-32-labeling) covered.

Two new [NIP-34](/en/topics/nip-34/) repo clusters appeared this week. [Vidstr](https://git.shakespeare.diy/npub14rg4vrt2v374q95ezeeydu3hkdhmzglcj950mggacap4x0lv0gyq04wun7/vidstr.git) is a video-focused Nostr client, and a [nostrapps.com cluster](wss://gitnostr.com) publishes three sibling projects: [verdana](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/verdana.git) (a napp VM for desktop), [hallway](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/hallway.git) (a customizable communities client), and [napps](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/napps.git) (an HTML microapps spec and runtime). The cluster sits parallel to the [napplet](/en/topics/nip-5d/) work covered in last issue's lead story.

---

## Protocol work and NIP updates

### Merged: NIP-44 lifts the 65,535-byte payload limit

[PR #1907](https://github.com/nostr-protocol/nips/pull/1907) merged on June 28 after sitting open since 2024-09. The change removes the 65,535-byte upper bound on the plaintext payload of a [NIP-44](/en/topics/nip-44/) versioned-encryption envelope, raising it to a 4-GiB cap (`uint32_max`). NIP-44 encodes payload length as a `uint16` in the wire format, which the original spec required strictly for interop; the merged change adopts a longer-length field tagged into the version byte so v2 implementations stay wire-compatible and v3+ implementations carry the longer length. Clients using NIP-44 for [NIP-17](/en/topics/nip-17/) direct messages, [NIP-59](/en/topics/nip-59/) gift wraps, [NIP-46](/en/topics/nip-46/) remote-signer payloads, or any other NIP-44-encrypted Nostr message can now exchange single events larger than 64 KiB without splitting at the application layer.

### Merged: NIP-86 gains a signevent method and a Relay Roles event

[PR #2389](https://github.com/nostr-protocol/nips/pull/2389) adds a `signevent` method to the [NIP-86](/en/topics/nip-86/) relay management JSON-RPC API, letting an administrator ask the relay to sign an event with the relay's own pubkey. The companion [PR #2390](https://github.com/nostr-protocol/nips/pull/2390) defines a Relay Roles event: a replaceable event a relay publishes to declare its administrators and moderators. Together they let NIP-86 clients introspect a relay's admin list and verify an authenticated request came from a current admin, without out-of-band trust. Deep dive on both changes below.

### Merged: NIP-34 replaces personal-fork with `u` for GRASP-06

[PR #2395](https://github.com/nostr-protocol/nips/pull/2395) merged on June 24 and replaces the [NIP-34](/en/topics/nip-34/) `personal-fork` tag on repo-state events (`kind:30618`) with a `u` tag (for "upstream"), aligning the wire format with the GRASP-06 fork semantics the GitWorkshop suite has been implementing. The change closes [PR #2384](https://github.com/nostr-protocol/nips/pull/2384) (`NIP-34: remove maintainers to solve expiry issues`), which proposed a different fork-semantics fix. The merged direction is the one ngit v2.6.x implements, so the merged spec and the reference CLI are now aligned. Existing repos using `personal-fork` continue to interoperate; new repos and the ngit v2.6 line publish the `u` tag.

### Merged: NIP-46 client metadata (now upstream after Amber shipped it)

[PR #2381](https://github.com/nostr-protocol/nips/pull/2381) merged on June 23 and adds optional client metadata to the [NIP-46](/en/topics/nip-46/) `connect` request, letting a client publish its name, an icon URL, and a homepage URL at signer-connect time. [Amber v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2) shipped the metadata extension last week (covered in [#28](/en/newsletters/2026-06-24-newsletter/#amber-v622-implements-nip-46-client-metadata)); this week the upstream NIP catches up to the shipping implementation.

### Open: epoch-based deterministic NIP-17 wrapper keys

[PR #2397](https://github.com/nostr-protocol/nips/pull/2397) and [PR #2396](https://github.com/nostr-protocol/nips/pull/2396) cover two converging NIP-17 wrap-key proposals. PR #2397 proposes that the ephemeral signing key used to author a [NIP-59](/en/topics/nip-59/) gift wrap be derived deterministically from a per-conversation seed tied to a coarse time epoch, so a recipient who knows the conversation key can predict which pubkeys to subscribe to. The current spec requires a fresh random key per wrap, which makes that prediction impossible. PR #2396 is the companion change: wraps for a given conversation should be signed with the conversation key directly so the wrap pubkey doubles as the conversation identifier. Together they define a path to filterable NIP-17 conversations without metadata leakage. Both are open and under discussion.

### Open: NIP-59 should reject kind:13 seal events at the relay

[PR #2399](https://github.com/nostr-protocol/nips/pull/2399) proposes that relays should reject kind:13 events (the inner seal of a [NIP-59](/en/topics/nip-59/) gift wrap) when they appear at the top level of a publish request, because a seal event is only meaningful inside a wrap and a leaked seal exposes the recipient pubkey. The companion [issue #2398](https://github.com/nostr-protocol/nips/issues/2398) goes further and argues that the seal should be re-defined as an ephemeral kind (NIP-01 ephemeral kinds are not stored by relays), which would harden the rule at the protocol level and remove the dependence on per-relay policy.

### Open: NIP-29 group states

[PR #2372](https://github.com/nostr-protocol/nips/pull/2372) adds explicit group-state semantics to [NIP-29](/en/topics/nip-29/) (relay-based groups), defining what it means for a group to be open, closed, public, private, or archived, and how state transitions interact with member events. The proposal pulls semantics that have been client-specific into the relay spec.

### Open: NIP-34 optional multi-maintainer support

[PR #2324](https://github.com/nostr-protocol/nips/pull/2324) is the companion proposal to the merged [PR #2395](https://github.com/nostr-protocol/nips/pull/2395) (GRASP-06 fork semantics covered above). PR #2324 adds optional multi-maintainer support to [NIP-34](/en/topics/nip-34/) repo announcement events (`kind:30617`), letting a repository declare more than one canonical maintainer pubkey via repeated `maintainer` tags. Patches and issues signed by any declared maintainer are then trusted by clients as official, which addresses the long-standing gap where NIP-34 repos with co-maintainers must either route everything through one pubkey or fall back to off-protocol coordination.

### Open: NIP-91 AND operator for filters (the proposal is open, not merged)

[PR #2252](https://github.com/nostr-protocol/nips/pull/2252) is the AND-operator proposal for Nostr [filters](/en/topics/nip-01/), reopening a design first discussed in the earlier closed [PR #1365](https://github.com/nostr-protocol/nips/pull/1365). Implementations already exist in [nostr-rs-relay](https://github.com/v0l/nostr-rs-relay), applesauce, [Amethyst](https://github.com/vitorpamplona/amethyst), and worker-relay, but the spec PR itself remains open.

### Closed: four pats2sats commerce NIPs

Four commerce-on-Nostr proposals closed this week: Escrow ([#2334](https://github.com/nostr-protocol/nips/pull/2334)), Reservations ([#2335](https://github.com/nostr-protocol/nips/pull/2335)), a [NIP-99](/en/topics/nip-99/) Marketplace Listing Extension ([#2346](https://github.com/nostr-protocol/nips/pull/2346)), and an Accommodation Listing Profile ([#2333](https://github.com/nostr-protocol/nips/pull/2333)). The same commerce surface is now being consolidated in the [Gamma Market Spec](https://github.com/GammaMarkets/market-spec), a project-owned extension repository that composes on top of NIP-99 marketplace listings with orders, checkout, escrow, and dispute semantics. Compass now tracks this repository alongside Marmot and Blossom as a protocol-spec repo external to the NIPs repository itself; open PRs there this week include client-attribution clarification ([#11](https://github.com/GammaMarkets/market-spec/pull/11)), a supersedes-tag for product-identity changes ([#8](https://github.com/GammaMarkets/market-spec/pull/8)), and merchant-review semantics ([#7](https://github.com/GammaMarkets/market-spec/pull/7)).

### Open: Bitcoin identity linkage

Two proposals opened this week for linking Bitcoin identities to Nostr identities: a [NIP-352 Bitcoin Silent Payment Address](https://github.com/nostr-protocol/nips/pull/2392) and a [Bitcoin-OTC Identity Linkage Proof](https://github.com/nostr-protocol/nips/pull/2401).

---

## NIP Deep Dive: NIP-86 (Relay Management API)

[NIP-86](/en/topics/nip-86/) defines a JSON-RPC interface for relay management, letting authorized clients send administrative commands to relays over a standardized API. A single client can manage any NIP-86-compatible relay without per-relay tooling. Two spec merges this week ([PR #2389](https://github.com/nostr-protocol/nips/pull/2389) and [PR #2390](https://github.com/nostr-protocol/nips/pull/2390)) close the loop between relay-signed events and relay-declared administrators.

### The transport

A NIP-86 management request is an HTTP POST to the same URI the relay serves WebSocket connections from, with `Content-Type: application/nostr+json+rpc`. The request body is a JSON document of the form:

```json
{
  "method": "<method-name>",
  "params": [<arg1>, <arg2>, ...]
}
```

Authentication uses a [NIP-98](/en/topics/nip-98/) HTTP-auth signed event in the `Authorization` header. The relay verifies the signing pubkey is on its administrator list before executing the method. The relay's response is a JSON document of the form:

```json
{
  "result": <return-value>,
  "error": "<error-string-if-any>"
}
```

### The methods that existed before this week

The pre-existing method set covers pubkey bans (`banpubkey`, `allowpubkey`, `listbannedpubkeys`), event bans (`banevent`, `allowevent`, `listbannedevents`), relay metadata (`changerelayname`, `changerelaydescription`, `changerelayicon`), allowed-pubkey list management (`allowkind`, `disallowkind`, `listallowedkinds`), and a `stats` method that returns relay statistics. The shape is intentionally close to a standard JSON-RPC service so a client can layer typed bindings on top of it.

### What changed this week

[PR #2389](https://github.com/nostr-protocol/nips/pull/2389) adds a `signevent` method to the spec. The method takes a partial event template (kind, tags, content) as its argument and asks the relay to sign and return a complete event with the relay's own pubkey as the `pubkey` field. This is the precondition for a relay to publish protocol-level events about itself: blocked-pubkey announcements, relay metadata, and the new Relay Roles event below all require the relay to sign with its operator-controlled key, but most relay operators do not want to hold a private key in their administrative client.

[PR #2390](https://github.com/nostr-protocol/nips/pull/2390) defines a Relay Roles event: a parameterised replaceable event kind that a relay publishes (signed with its own pubkey via `signevent`) declaring the pubkeys of its administrators and moderators with explicit role semantics. A NIP-86-aware client can fetch the Relay Roles event from any tracked relay, build the admin list from the event tags, and validate that an authenticated NIP-86 request came from a current admin without out-of-band trust or per-relay configuration. The two PRs together close the loop: `signevent` is the mechanism, Relay Roles is the first event kind built on top of it.

### A NIP-86 request example

A complete NIP-86 `banpubkey` request looks like:

```json
{
  "method": "banpubkey",
  "params": [
    "<64-char-hex-pubkey-to-ban>",
    "spam"
  ]
}
```

with an `Authorization` header carrying a NIP-98 signed event:

```json
{
  "id": "5e1c2f9e1d3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c",
  "pubkey": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
  "created_at": 1782824400,
  "kind": 27235,
  "tags": [
    ["u", "https://relay.example.com/"],
    ["method", "POST"],
    ["payload", "<sha256-of-request-body>"]
  ],
  "content": "",
  "sig": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100"
}
```

The signing pubkey must be present in the relay's admin set (now declared in the relay-roles event); the `u` tag must match the relay's HTTPS URL; the `payload` tag must match the SHA-256 of the JSON request body. The relay returns:

```json
{
  "result": true,
  "error": null
}
```

### Implementations

- [Amethyst](https://github.com/vitorpamplona/amethyst) ships a NIP-86 relay management UI on Android (v1.07.0+).
- The reference relays that implement the spec include [strfry](https://github.com/hoytech/strfry), [khatru](https://github.com/fiatjaf/khatru), and several smaller implementations the spec links from its `Implementation Status` section.

NIP-86-aware clients will begin treating the relay-roles event as the canonical source for a relay's admin list, once implementers pick up the `signevent` and Relay Roles changes.

---

## NIP Deep Dive: NIP-89 (Recommended Application Handlers)

[NIP-89](/en/topics/nip-89/) defines two parameterised replaceable event kinds, `kind:31990` (the application handler an app developer publishes) and `kind:31989` (the recommendation a user publishes for an app they use). Together they let clients discover applications that handle an unknown event kind without out-of-band coordination: a longform reader that hits a `kind:30030` event it does not handle natively can query the NIP-89 graph for handlers and offer the user an `Open in...` flow to a published app that does. NIP-89 is the original infrastructure for the same cross-app routing problem that the napplet/napps work appearing across this issue is now extending into composable Nostr-native applets.

### The application handler event (`kind:31990`)

An app developer publishes one or more handler events describing which event kinds the app supports and how to open a Nostr entity in the app:

```json
{
  "id": "8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b",
  "pubkey": "c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2",
  "created_at": 1782824400,
  "kind": 31990,
  "tags": [
    ["d", "longform-reader-v1"],
    ["k", "30023"],
    ["k", "30024"],
    ["web", "https://reader.example.com/a/<bech32>", "naddr"],
    ["ios", "longformreader://open/<bech32>"],
    ["android", "longformreader://open/<bech32>"]
  ],
  "content": "{\"name\": \"Longform Reader\", \"picture\": \"https://reader.example.com/icon.png\", \"about\": \"A native reader for NIP-23 longform.\"}",
  "sig": "1f2e3d4c5b6a798877665544332211000ffeeddccbbaa99887766554433221100ffeeddccbbaa99887766554433221100ffeeddccbbaa9988776655443322110a"
}
```

The `d` tag identifies the handler (so it can be replaced), each `k` tag declares an event kind the app handles, and each platform tag (`web`, `ios`, `android`, ...) gives a URL template with `<bech32>` as the placeholder for a [NIP-19](/en/topics/nip-19/) encoded entity that the calling client substitutes at open time. One handler event can advertise several supported kinds if they share the same routing pattern, which keeps app discovery compact and avoids one handler event per kind.

### The user recommendation event (`kind:31989`)

A user publishes a recommendation declaring which apps they use for a given event kind:

```json
{
  "id": "9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d",
  "pubkey": "d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3",
  "created_at": 1782824500,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com", "web"],
    ["a", "31990:e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6:reader-pro", "wss://relay.example.com", "ios"]
  ],
  "content": "",
  "sig": "2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6"
}
```

The `d` tag carries the event kind being recommended. Each `a` tag is a NIP-01 address pointer to a `kind:31990` handler event, with the suggested relay and the platform the recommendation applies to. The same recommendation can list multiple apps for different platforms.

### The client tag and the privacy tradeoff

NIP-89 also defines an optional `client` tag that any publishing app can attach to events it authors:

```
["client", "Longform Reader", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com"]
```

This lets any client showing the event surface the app it came from, look up richer handler metadata, and respect handler-declared rendering hints. The spec also explicitly notes the privacy cost: a client that emits a `client` tag on every event publishes the user's software identity, which over time discloses usage patterns. The spec recommends clients give users an opt-out.

Amethyst's [PR #3422](https://github.com/vitorpamplona/amethyst/pull/3422) parses and displays NIP-89 `t`, `i`, `a`, and `client` tags on event display, surfacing which app authored a note directly in the timeline.

### How the discovery flow runs in practice

A client receiving an unknown event kind takes the following steps. (1) Query the user's follow graph for `kind:31989` events with a `d` tag matching the event kind. (2) Resolve each recommended `a` tag to its `kind:31990` handler event. (3) Pick the handler whose `web`, `ios`, or `android` URL template matches the current platform. (4) Substitute the entity's `bech32` encoding into the URL template. (5) Offer the resulting URL to the user as an `Open in...` choice. The flow is socially filtered: a client that queries arbitrary handler events from untrusted relays could end up redirecting users to malicious apps, so starting from people the user follows is a safer default than treating every published handler as equally trustworthy.

### NIP-89 and the napplet layer

Amethyst's Discover section, napplet-host runtime, and `client`-tag display together build a full NIP-89 consumer surface on Android. The napplet spec, launched last issue, extends what those NIP-89 handler events can target: sandboxed applets that run a composable Nostr-native runtime over Nostr and Blossom. NIP-89 is the discovery and routing graph; the napplet runtime is one execution target it can point at.

---

*Feedback, corrections, and projects we missed: open an issue on [github.com/andotherstuff/nostr-compass](https://github.com/andotherstuff/nostr-compass) or reach us over NIP-17 DM at npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923.*
