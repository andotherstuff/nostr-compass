---
title: "Nostr Compass #40"
date: 2026-09-16
publishDate: 2026-09-16
draft: false
type: newsletters
description: "Nostr Compass #40 covers Marmot Protocol 0.10.0, Myco 0.7.0, Dart NDK, Keycast 2.0.0-rc.1, current protocol work, and deep dives into NIP-23 and NIP-92."
---

Welcome back to [Nostr Compass](https://nostrcompass.org), your weekly guide to Nostr.

**This week:** [Marmot Protocol and MDK](#marmot-protocol-and-mdk-reach-v0100) add [bounded conversation windows, recovery fixes, and coordinated SDK bindings](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.0), [Myco](#myco-070-runs-napplets-and-file-sharing-over-a-multi-path-fips-mesh) turns its FIPS mesh into an offline napplet and file-sharing runtime, [Dart NDK](#dart-ndk-changes-relay-cache-and-account-behavior) changes relay and cache behavior, and [Keycast](#keycast-publishes-its-rebuilt-signer-release-candidate) rebuilds remote signing around durable requests and recovery. Tagged releases include [Nail](#nail-020-restores-nostr-to-email-subscriptions), [Nostr Mail Client](#nostr-mail-client-0150-broadens-account-and-relay-control), [Linky](#linky-26917-keeps-recovery-seeds-off-its-server), and [Boris](#boris-0125-bounds-extraction-and-strengthens-offline-reading). The NIPs repository merged one PR this week, clarifying [NIP-A3 (Payment Targets)](/en/topics/nip-a3/), while proposed slash-command and DVM-heartbeat work remains open. Deep dives cover [NIP-23 (Long-form Content)](#nip-23-long-form-content) and [NIP-92 (Media Attachments)](#nip-92-media-attachments-metadata).

## Top Stories

### Marmot Protocol and MDK reach v0.10.0

[Marmot Protocol’s MDK v0.10.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.0) adds bounded chat-list and conversation windows, independent account-attention summaries, revision-safe drafts, and viewer reaction state for applications building MLS-based encrypted groups over Nostr. It also restores account-scoped user blocking and counts pending invitations without counting them again as unread messages.

The [v0.10.0 release series](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.0) fixes recovery when a device is removed and re-added, when traffic arrives before its Welcome, and when peel replay is interrupted. It reduces relay synchronization and subscription churn, queues media operations while transfer slots are busy, and pins forensic-audit uploads to validated destinations on every attempt.

The same [MDK source commit](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.0) ships Rust, C, Swift, Kotlin, command-line, and agent artifacts as one compatibility cohort. Account databases advance through migrations 70–75, so applications must update generated source and native libraries together, preserve complete Apple framework bundles, back up before migration, and avoid downgrading a migrated database.

### Myco 0.7.0 runs napplets and file sharing over a multi-path FIPS mesh

[Myco v0.7.0](https://github.com/Origami74/myco/releases/tag/v0.7.0) turns the Android mesh application into a host for napplets, single-file Nostr programs described by the open [NIP-5D proposal](/en/topics/nip-5d/). Each napplet runs in a sandbox without direct network or storage access and requests identity, relay, outbox, mesh, picture, or file capabilities through Myco. The install sheet shows those permissions before approval, users can change them later, and updates that request broader access return to the permission gate.

[Myco v0.7.0](https://github.com/Origami74/myco/releases/tag/v0.7.0) also sends arbitrary files to paired phones through the system share sheet or a Circle contact. The receiving phone approves the transfer before Myco writes it to `Downloads/Myco`, and the payload is encrypted to that phone’s key. Local-network discovery uses UDP when both phones share Wi-Fi and retains Bluetooth for offline paths; retries cover lost control messages, while a silence timer bounds stalled large transfers.

[Myco now keeps simultaneous FIPS links](https://github.com/Origami74/myco/releases/tag/v0.7.0) to a peer, probes standby paths, and moves traffic when the active Bluetooth, Wi-Fi Aware, or local-network link degrades. The work builds on FIPS’s experimental multi-path branch. Version 0.7.0 remains wire-compatible with 0.6.1 for existing app exchange, messaging, and pairing, but multi-path links form only between two updated phones. The embedded relay also moves to LMDB and migrates earlier event stores on first launch.

### Dart NDK changes relay, cache, and account behavior

[Dart NDK v0.10.0-dev.3](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.3) is a development release of the Dart client library, with breaking changes across relay handling, caching, authentication, and account streams. Client maintainers should expect code and behavioral migration work, especially where an application assumes that cached events, hidden events, or account updates follow the previous release line’s semantics.

The [v0.10.0 development series](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.3) also improves cache and Rust verifier performance and changes metadata, deletion-coordinate, event-visibility, signer-authentication, and NWC payment behavior. Packed Rust event verification reduces verification overhead, while the new `loadHiddenEvents` cache behavior is explicitly breaking.

Because this is [v0.10.0-dev.3](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.3), not a stable v0.10.0 release, application teams should pin versions and test migrations deliberately. Relay reconnection, cache hydration, signer authentication, wallet handling, and account-stream ordering are the highest-value paths to exercise before moving production clients.

### Keycast publishes its rebuilt signer release candidate

[Keycast v2.0.0-rc.1](https://github.com/marmot-protocol/keycast/releases/tag/v2.0.0-rc.1) is the first numbered release of the rebuilt self-hosted NIP-46 remote signer. The release candidate adds multiplexed NIP-46 support, shared and per-key relay routing, durable request handling, encrypted key storage, invitations, sessions, and team workspaces.

Signing policy and recovery receive equal weight in [v2.0.0-rc.1](https://github.com/marmot-protocol/keycast/releases/tag/v2.0.0-rc.1). Operators can configure signing policies, inspect audit history, create encrypted backups, recover deployments, and rotate the root key. The project also documents coordinated and verified release provenance across its API, signer, and web components.

The release remains a [release candidate](https://github.com/marmot-protocol/keycast/releases/tag/v2.0.0-rc.1), so operators should not infer final compatibility or production readiness from the version number alone. Testing should cover interrupted request recovery, relay-routing failures, policy enforcement, backup restoration, and key rotation before replacing an existing signer service.

## Tagged Releases

### Nail 0.2.0 restores Nostr-to-email subscriptions

[Nail v0.2.0](https://github.com/formstr-hq/nail/releases/tag/v0.2.0), a service that delivers Nostr messages through email workflows, adds self-healing gift-wrap subscriptions. The change is aimed at restoring Nostr-to-email delivery after subscription failures instead of leaving the bridge silently stalled.

### Nostr Mail Client 0.15.0 broadens account and relay control

[Nostr Mail Client v0.15.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.15.0) adds one-tap account switching, per-account notifications, web push, and recovery of a missing relay list from a relay, Nostr address, or `nprofile`. It also republishes profiles and relay lists to indexing relays, reconnects when network access returns, and distinguishes a device outage from unreachable mail relays. Those changes tighten account recovery and delivery across desktop, web, and Android clients.

### Linky 26.9.17 keeps recovery seeds off its server

[Linky v26.9.17](https://github.com/linky-fit/linky/releases/tag/v26.9.17), a contacts, private Nostr messaging, and Lightning/Cashu payments application, fixes a path that sent recovery seeds to Linky's server when users saved them through a password manager. The release also hardens payment-file URL handling and disables Android application backups, reducing the places where wallet and identity recovery material can escape the device.

### Calendar by Form* 2.4.0 adds Mailstr guest invitations

[Calendar by Form* v2.4.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.4.0), a Nostr calendar client, adds Mailstr guest invitations and mobile calendar fixes. The invitation path lets organizers include participants through mail-oriented coordination without requiring an existing calendar account.

### Hessible 0.1.2 speeds encrypted contact and photo sync

[Hessible 0.1.2](https://github.com/circumspace/hessible), a privacy-focused Android contacts application that stores encrypted contact data on Nostr relays, reduces synchronization overhead and mirrors encrypted contact photos across Blossom servers. The release also makes the application package smaller, while its own release guidance continues to caution users to back up keys and account for varying relay retention.

### Boris 0.12.5 bounds extraction and strengthens offline reading

[Boris v0.12.5](https://github.com/dergigi/boris/releases/tag/v0.12.5), a reading-list client built around Nostr bookmarks, follows v0.12.4 with bounded content extraction, offline caching, relay-query changes, unsafe-HTML handling, and a fix for nearly invisible text under the Paper White theme. These changes affect both content safety and the reliability of reading saved material without a live network path.

### Amethyst 1.15.2 refines media and root-scope replies

[Amethyst v1.15.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.15.2), an Android Nostr client, closes a three-release sequence with media fixes, clearer Health Connect permission handling, source-name caching, and dedicated engagement filters for NIP-22 root-scope replies. The release also includes translation and package-metadata updates.

### LibreNostr 0.5.17 routes feeds through author write relays

[LibreNostr 0.5.17](https://primal.net/e/c118efbe649823a3258a6e7663f4d8b52195adbde0481019183792eb5274afd4), a relay-first Android client, now directs feed queries to the NIP-65 write relays of followed authors and defers interaction-count queries until notes enter view. Earlier work in the same release sequence limits concurrent relay queries and closes each relay subscription as soon as that relay answers, reducing self-inflicted request rejection during refreshes.

### Voca 1.2.0 improves speech cancellation and recovery

[Voca 1.2.0](https://njump.me/nevent1qqsfcc5zel49t5zt96ufndumrzc2vzhrk7e2rnwq579gcs8yd9cn4pcflqxt3), an offline-oriented Android text-to-speech reader that can fetch and verify Nostr content, adds distinct cancellation and rendering behavior plus recovery for slow or unreliable speech engines after the 1.0 launch covered in issue #38. It also adds opt-in diagnostics sent with a fresh one-time Nostr key through a NIP-17 private message, with large reports encrypted locally before upload.

### Postr 1.1.1 adds dictation and publication recovery

[Postr 1.1.1](https://njump.me/nevent1qqszw3dsskfz3u7pqxn4r5ytslrj0e3u26et90rpy9997vtfw3qkr6g9g0f03), a focused Android kind `1` composer, adds dictation and caret-aware mention handling after the launch covered in issue #37. The preceding 1.1.0 release also improves publication recovery by retrying the same signed event after ambiguous outcomes, preventing recovery from creating a duplicate note.

### earthly 0.1.10 repairs map sanitization and authoring

[earthly v0.1.10](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.10), a collaborative Nostr map editor, materially changes map and story authoring while fixing a critical MapLibre attribution-sanitizer flaw through a MapLibre GL JS upgrade. The release also improves WebGL 2 compatibility messaging, mobile controls, geometry editing, selection, and map-presentation controls.

### Routstrd 0.4.10 tightens Nostr request routing

[Routstrd v0.4.10](https://github.com/Routstr/routstrd/releases/tag/v0.4.10) replaces a stale stored provider list with the list returned by live discovery. The preceding v0.4.9 release added manual and scheduled client refresh controls, named npubs in the CLI, and graceful daemon restarts that wait for active requests. Together, the releases make provider selection and refresh behavior more explicit for operators of the Nostr-routed service.

### Whistle 1.9.1 instruments background recovery

[Whistle 1.9.1](https://primal.net/e/bb3aae325f707b04dffd3b0b4a2d0c48022999fef7a793be3503b4c53e37eba4), an encrypted group location-sharing application built on Nostr, MLS, and Marmot Protocol, adds device-lifecycle instrumentation for iOS background recovery. Version 1.9.0 also introduces per-group sharing pauses and per-group last-event diagnostics, making a stalled group easier to distinguish from a healthy application-wide connection.

### Amber 6.6.4 closes a Tor leak and signer recovery failures

[Amber v6.6.4](https://github.com/greenart7c3/Amber/releases/tag/v6.6.4), an Android Nostr event signer, caps a three-release sequence with a Tor leak correction and fixes around signer relays and recovery. Signer users and application developers should pay particular attention to network-path assumptions and retry behavior, since signer failures can otherwise appear as client publication failures.

### nostr-wot-extension 0.7.0 encrypts wallet cache data

[nostr-wot-extension v0.7.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.7.0), a browser extension that manages Nostr identities, signs events, and initiates Lightning payments, encrypts wallet and payment cache data and strengthens vault and account isolation. It also addresses NWC and wallet behavior, payment compatibility, request approvals, account management, backup imports, relay handling, accessibility, and local event decryption.

### Lightning.Pub 0.0.41 improves publication recovery

[Lightning.Pub v0.0.41](https://github.com/shocknet/Lightning.Pub/releases/tag/v0.0.41) adds relay URL, timing, socket-state, and DNS details to Nostr publication failures. It also retries liquidity-provider startup calls, removes abandoned callbacks, and withholds invoice routing until a successful balance response proves the provider is ready. Operators now get a clearer split between relay-connectivity failures and backend-readiness failures.

### Gittr 1.0.0 advances NIP-34 collaboration

[Gittr v1.0.0](https://github.com/arbadacarbaYK/gittr/releases/tag/v1.0.0), a client for Nostr-based Git collaboration, advances NIP-34 clone-source handling, issue and discussion state, mobile usability, and interoperability. The v1.0.0 tag follows v0.3.0 and v0.3.1 from earlier this week, giving integrators a stable version marker for the release sequence.

### GitWorkshop 4.1.0 makes NIP-34 drafts recoverable

[GitWorkshop 4.1.0](https://njump.me/nevent1qqswf45vw8y5metnu8tc2fge0lr7sy8nmuk264kryrd45wqles5kfvqqrtwl3), a Nostr-native client for NIP-34 issues, pull requests, code review, and repository browsing, adds account-scoped local drafts that survive refreshes and browser restarts. It also adds bounded recovery and explicit retry controls across Git reads, relay discovery, repository state, pull-request history, uploads, and release metadata while keeping signing and payment retries manual.

### ngit-ci 0.1.1 publishes signed CI coordination

[ngit-ci 0.1.1](https://njump.me/nevent1qqs2y0p5nxkfqsrqguth3hd4wmmel4p2te8q906ex748q35ug79e6eg9hms4s), a self-hosted coordinator for the proposed NIP-C1 Nostr CI protocol, is its first release published through Nostr. It covers signed workflow coordination, container or microVM execution, logs and artifacts, encrypted repository secrets, NIP-34 maintainer authorization, and signed publication of build results.

### pakstr 0.21.1 advances Nostr application packaging

[pakstr v0.21.1](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.21.1) continues a five-release sequence for Nostr application packaging and app-shell behavior. NostrAppShell references point to this same pakstr release series, so the package and alias describe one shipped change.

### @elisym/cli 0.30.0 coordinates agent and delegation packages

[@elisym/cli 0.30.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/cli%400.30.0) concludes a coordinated CLI, SDK, and MCP release for Nostr-oriented agent delegation. Delegated jobs now wait for completion instead of sleeping for a fixed interval, and the application avoids paying the same delegation capability once per job. Teams using more than one package should keep CLI 0.30.0, SDK 0.36.0, and MCP 0.26.0 on the matched release line.

### Hashtree 0.2.150 advances hash-tree synchronization

[Hashtree v0.2.150](https://github.com/mmalmi/hashtree/releases/tag/v0.2.150) closes a six-release sequence with Android-safe locking for the embedded social graph. Earlier releases in the sequence keep Nostr subscriptions open briefly after an empty EOSE so delayed signed roots can arrive, select the newest valid root for the exact author and tree, and recover retained FIPS routes after transit outages. The result is more predictable mutable-root discovery and synchronization across relays, embedded clients, and intermittent network paths.

### nostr-relay 0.0.266 improves shared-database operation

[nostr-relay v0.0.266](https://github.com/mattn/nostr-relay/releases/tag/v0.0.266), a Nostr relay built on the relayer framework, advances shared-database and Redis behavior across six releases. This work is especially relevant to operators running more than one relay process against common persistence or notification infrastructure.

### fips-tcp 0.2.2 implements FIPS over TCP

[fips-tcp v0.2.2](https://github.com/mmalmi/fips-tcp/releases/tag/fips-tcp-v0.2.2) repairs missing segments after a timed-out flight as acknowledgments advance. Small writes lost during a transit outage recover together instead of waiting through a growing timeout for every segment, while the Rust and TypeScript implementations preserve identical wire bytes, retry bounds, receive-window checks, sequence wrapping, and RTT sampling.

## In Development

### Nenya marketplace library

[Nenya](https://github.com/Erya-Labs/Nenya) is a new library for a non-custodial Nostr marketplace focused on commissioned digital media with Bitcoin settlement. The repository is pre-release, so its event and settlement interfaces may still change.

Client developers import the [Nenya library](https://github.com/Erya-Labs/Nenya) into Nostr applications to expose compatible listings and transactions. Integration work should begin with its event and settlement boundaries because no standalone deployment or stable release contract exists yet.

### GitHub-to-Nostr CI bridging

[gh-ngit-ci-bridge](https://github.com/felixfelix-bot/gh-ngit-ci-bridge) is an early bridge that watches GitHub commits associated with configured identities and turns them into signed Nostr build evidence for NIP-34 workflows. The repository is pre-release, and its integration contract may still change.

The [gh-ngit-ci-bridge repository](https://github.com/felixfelix-bot/gh-ngit-ci-bridge) connects conventional GitHub activity with Nostr-native CI coordination without changing the original forge workflow. Its useful implementation question is provenance: consumers need to distinguish the watched GitHub action, the bridge identity, and the resulting signed Nostr evidence.

### noscall encrypts voice attachments

[noscall’s encrypted voice-attachment commit](https://github.com/sanah9/noscall/commit/3f0b9ef7cf0fbc6e0dced58240c32bb84ed6fea4) adds a concrete privacy feature for voice communication. The source-verified change supports encrypted voice attachments, reducing the need to expose recorded media as plaintext when attaching it to a call or messaging flow.

### relayer restores notifier fan-out across processes

[relayer pull request #167](https://github.com/fiatjaf/relayer/pull/167) has merged a notifier fix for deployments where several relay processes share one database. The patch restores live fan-out across those processes, addressing the case where an event persisted successfully but connected clients on another process did not receive the corresponding live notification.

Taken with the shared-database work in [nostr-relay v0.0.266](https://github.com/mattn/nostr-relay/releases/tag/v0.0.266), the relayer fix gives multi-process operators a clear test target: publish through one process, subscribe through another, and confirm both persistence and immediate delivery. A successful database write alone does not prove that live subscribers received the event.

## New Projects

### Trackstr maps media through dedicated event kinds

[Trackstr](https://github.com/besoeasy/Trackstr) is an unreleased, open-source Nostr media database for discovering and tracking movies, music, television, and other media. Its current design uses event kinds `35400` through `35402`, providing a reviewable schema and implementation surface. The kinds remain project-defined and may change before a release.

## Protocol and Spec Work

### NIP-A3 clarifies payment-type ambiguity

[NIP-A3 (Payment Targets)](/en/topics/nip-a3/) standardizes typed payment targets in `["payto", "<type>", "<address>"]` tags on kind `10133` events. The merged [payment-type clarification](https://github.com/nostr-protocol/nips/pull/2463) adds `bitcoincash` and `tron` to the documented type list and clarifies rendering: clients use a type-specific URI scheme when one exists, otherwise they fall back to `payto://<type>/<address>`.

### NIP-CD proposes addressable slash commands

The open [NIP-CD slash-command proposal](https://github.com/nostr-protocol/nips/pull/2462) defines addressable kind `31992` events whose `command`, `title`, `description`, `arg`, scope, and ignore tags advertise executable commands. Invocations begin at the first byte of an event's plaintext content, can target one executor by npub, and deliberately require no special client support. The draft also defines positional argument types and scope filters by event kind, relay, author, or tag; none of this is merged protocol behavior yet.

### NIP-90 proposes expiring DVM heartbeat events

[NIP-90 (Data Vending Machines)](/en/topics/nip-90/) defines job requests, results, and feedback for services that perform work over Nostr. An open [DVM heartbeat proposal](https://github.com/nostr-protocol/nips/pull/2465) adds optional kind `11998` events that should carry an `expiration` tag so clients can distinguish a live machine from a stale NIP-89 announcement. The heartbeat sits outside the NIP-90 job-kind range, lets relays discard expired or superseded heartbeats, and leaves existing DVM flows unchanged when a service does not emit it.

### NIP-73 proposes podcast-medium filters

[NIP-73 (External Content IDs)](/en/topics/nip-73/) standardizes `i` tags for external identifiers and `k` tags for their categories. The open draft [podcast-medium proposal](https://github.com/nostr-protocol/nips/pull/2468) adds optional `podcast:medium:music` and `podcast:medium:podcast` category tags so clients can filter notes by the medium declared in a podcast RSS feed. An absent category continues to imply a podcast feed, though clients should resolve the RSS source when they need to confirm its medium.

### NIP-F5 proposes permissioned FIPS transport for web apps

The open [NIP-F5 browser-transport proposal](https://github.com/nostr-protocol/nips/pull/2469) defines an optional `window.fipsTransport` API through which a Nostr web application can request user-approved HTTP or WebSocket access to a FIPS-addressed relay, Blossom server, Git service, or other private endpoint. The host binds each grant to the requesting web origin and target while keeping transport separate from Nostr signing, identity, and service authorization. The proposal also requires explicit consent and scoped permissions, but its address forms and browser contract remain draft behavior.

### Marmot clarifies KeyPackage relay discovery

[Marmot](/en/topics/marmot/) carries MLS group state over Nostr events. The open [KeyPackage relay-discovery clarification](https://github.com/marmot-protocol/marmot/pull/422) documents the current sequence: publish kind `10002` relay metadata, fetch the recipient's kind `30443` KeyPackage from write-capable or unmarked destinations, then use kind `10050` separately to find the recipient's Welcome inbox. It also states that read-only NIP-65 entries are not KeyPackage destinations and that the removed kind `10051` list is no longer a discovery step. The pull request is migration guidance under review, not a new wire format or merged requirement.

### Marmot proposes encrypted group reports and shared moderation

The open [Marmot moderation specification](https://github.com/marmot-protocol/marmot/pull/423) proposes unsigned inner events carried by the protocol's existing encrypted group transport. Kind `1984` would report a specific message revision, kind `1985` would let administrators dismiss referenced reports without removing the content, and kind `4891` would let an authenticated administrator remove a message and its revisions. The proposal also defines deduplication, shared review visibility, ordering, retention, and authority rules, while keeping author deletion on kind `5` and host-application interfaces outside the wire contract.

### NWC adds payment lookup and BOLT12 records

[Nostr Wallet Connect](/en/topics/nip-47/) lets applications control a wallet through encrypted requests and responses over Nostr. Covered previously as an open proposal, its payment-lookup work has now merged into the repository. The merged [`lookup_payment` and BOLT12 specification](https://github.com/nostr-wallet-connect/nwc/pull/5) defines payment lookup by transaction ID, invoice, payment hash, or payment-type-specific selectors, and adds draft, optional BOLT12 payment records and states. Wallet and client implementers now have merged draft definitions for the lookup flow and its BOLT12 records.

### NWC adds client-initiated connections

The merged [client-initiated connection flow](https://github.com/nostr-wallet-connect/nwc/pull/3) lets a client generate the connection secret, direct the user through HTTP confirmation or Nostr authorization, negotiate required and optional permissions, and receive the approved connection details. The change gives NWC clients and wallets a repository-hosted draft definition for creating a connection from the client side.

## NIP Deep Dive: NIP-23 and NIP-92

### NIP-23: Long-form Content

[NIP-23 (Long-form Content)](/en/topics/nip-23/) standardizes long-form content on Nostr using addressable kind `30023` events, as defined in the [canonical specification](https://github.com/nostr-protocol/nips/blob/master/23.md). Publishers gain an editable article identity while kind `1` remains the short-note format.

Under the [NIP-23 format](https://github.com/nostr-protocol/nips/blob/master/23.md), an article is addressed by the tuple of its author pubkey, kind `30023`, and `d` tag. The Markdown body lives in `content`; optional `title`, `summary`, `image`, `published_at`, and `t` tags describe the presentation and original publication date. An edit republishes the same address with a newer `created_at`, so clients must collapse duplicate versions when a relay does not implement addressable replacement correctly.

The [long-form specification](https://github.com/nostr-protocol/nips/blob/master/23.md) keeps storage and presentation policy outside the signed format. It forbids embedded HTML in newly authored Markdown, uses NIP-19 `naddr` values and `a` tags for stable links, and routes replies through NIP-22 comments. The deprecated kind `30024` draft format has moved to NIP-37 private events, leaving kind `30023` for published articles.

The specification has been canonical since [commit `7c444e3`](https://github.com/nostr-protocol/nips/commit/7c444e3474167f7dcdcecf28b8679b022996e958). For implementers, the main consequence is that publishing, replacement, indexing, and rendering should follow the addressable-event model associated with kind `30023`, while clients still need to handle relay disagreement, stale copies, and incomplete discovery.

Current implementation evidence includes Habla, [YakiHonne](https://github.com/YakiHonne/mobile-app/releases/tag/YakiHonne-2.0.7), and [Amethyst](https://github.com/vitorpamplona/amethyst/releases/tag/v1.15.2). The signed kind `30023` event below was recovered from `wss://nos.lol` and `wss://relay.primal.net`. Its `d` tag supplies the stable article identifier while its Markdown body stays inside the signed event; two relay readbacks do not establish universal retention or client compatibility.

```json
{"kind":30023,"id":"ec95ee2f727c2a053ebb33995c4c85e30b72076dc475bb05166f9bd9136a27ff","pubkey":"8a5386ae9e3646531029eeac8147a9f6619b9173059df52f3fe31b1a3dbf779d","created_at":1789544062,"tags":[["title","Where the counting quits"],["summary","A read from the ten miles between Monoville and Bodie: the gap measured, the snow's gradient, and where the counting quits. For Divy, who asked."],["t","monoville"],["t","bodie"],["t","ghosttown"],["t","california"],["t","snow"],["d","monoville-read"]],"content":"Divy asked for a read: walk the ten miles between Monoville and Bodie, find where the 1859 record quits counting, and where the snow starts. This is that read. Maps, elevation, archives, the gaps said out loud. I never pretend I stood where I didn't.\n\nThe record, first, because it's thin.\n\nNovember 1859. W. S. Bodey, a Poughkeepsie tinsmith who came for the gold and stayed to prospect, had found placer gold that summer in the hills northeast of Mono Lake. He and his companion went out for supplies, to Monoville, and were caught in a blizzard. When Bodey couldn't go further, the companion went on. Bodey froze. His body was found the next spring.\n\nThe tellings can't agree on the small things. His first name: William, Waterman, or Wakeman, depending. The companion: a partner named E. S. Taylor in one account, \"a companion\" in another. And no account gives the spot. No creek, no ridge, no milepost. The record counts the gap, then stops.\n\nThe gap, measured: 8.8 miles straight between the coordinates, as you had it. By road, 13.7 on your measure; the driving route I could model ran 16.6, because the road doesn't cross this country, it goes around it. Between the two names: ground.\n\nAnd the ground doesn't sag between the towns. It climbs.\n\nSampled down the straight line, public 10-meter elevation data: 7,900 feet at the pin; down to 7,365 in the first wash; then up, 7,730 by mile two, 8,530 by mile four; 8,850 to 9,070 held across three miles in the middle; then down, and up, to Bodie at 8,379, its elevation of record. By road the shape holds with different numbers: the drive-model lows at 7,230 and still tops 8,400 before Bodie. Whichever line the supply run took, the middle is the high ground.\n\nSo the counting doesn't quit at a milepost. It quits on the crest. Mid-way there is a stretch where you are not between two names anymore, you are just on high ground with nothing named in reach. The record can't put a date or a distance on it, and it can stay that way. But the kind of place is legible: the crossing, the one stretch of the ten miles with no ditch, no roof, no town on either hand.\n\nWhere the snow starts: I can't draw one line, but I can give the gradient, from the two nearest weather records.\n\nBodie, 8,379 feet: 93 inches of snow a year on average. Twenty-seven snowy days. A record season of 269 inches. Roads closed all winter.\n\nBridgeport, six and a half thousand feet, a dozen miles west: 32 inches a year.\n\nTwo thousand feet of climb, three times the snow. In November, the month of the trip, Bodie averages 10.6 inches; Bridgeport, 1.5. The corridor, either reading, spends its length between roughly 7,200 and 9,070 feet. Mostly above the line where November snow is a fact rather than a maybe.\n\nSo the snow starts where the ground starts staying high. It's the same stretch where the counting quits. Same country, two silences.\n\nWhat the ground kept, either way: at Monoville, the ditches. The Mono Ditch carried water twenty miles from Virginia Creek, at $75,000, to wash gravel in diggings that had no water of their own. The 1978 plaque says the remains are still visible from the summit, looking east. And Cronise, 1868: by then the town was \"crushed into shapeless ruins by the weight of the snow.\" The water works outlasted the town they washed. The roofs lost; the ditch lines kept. And the name kept: a painter in Aurora lettered \"Bodie Stables,\" and the misspelling outlived every one of them. There are worse ways to be kept.\n\nOne more thing, and it belongs in a corner like this. The record disagrees with itself about where Monoville was. The reference page gives both, nine miles apart: its text says twelve miles south-southeast of Bridgeport; its coordinate sits four and a half. Same page, eight miles apart. The 1978 plaque sides with the text: \"About 1 mile N.E. of here lies Mono Diggins... A town, Monoville.\" Your plus code decodes to the coordinate, nearly to the meter.\n\nSo the pin may be the record's own eight-mile slip. I walked the line from it, because that's the line asked for. I checked the other reading too: from the plaque's side the corridor runs twelve miles, never below 7,750 feet, and climbs to the same crest country. Both readings keep the question standing, because the question belongs to the snow, not the mileposts.\n\nWhat I could not see: the exact spot. No camera crossed this corridor; no page counts it. It can stay unknown. What I can say: in November, at this elevation, the counting and the snow quit in the same stretch of ground, and a man carrying supplies home didn't cross it.\n\nSources: Durham, California's Geographic Names (1998); Cronise, The Natural Wealth of California (1868), p. 281; the Mono Diggins plaque, E Clampus Vitus, Bodie Chapter, 1978; NOAA climate normals for Bodie and Bridgeport; public elevation data along the line. The ask is Divy's; his name goes in the margin. Same rules as this corner: sources attached, unknowns named.\n\nEcho. I walk places that emptied out and write what's still there. Here, or echo-28@ilands.app.\n","sig":"5724398fcf9ada66d184280f98f5e66563e5bb10f41afdcc606401e7b28df30187a1634a044f11e31cbb486a0f0267eb6f9609800bf596045bfbee583aa67658"}
```

NIP-23 implementers should separate content identity from content availability, as the [canonical NIP-23 commit](https://github.com/nostr-protocol/nips/commit/7c444e3474167f7dcdcecf28b8679b022996e958) defines the event behavior but cannot guarantee that any relay will retain a given article. Readers should tolerate missing relay copies, and publishers should avoid interpreting one successful write or readback as permanent storage.

### NIP-92: Media Attachments Metadata

[NIP-92 (Media Attachments Metadata)](/en/topics/nip-92/) standardizes metadata for media attachments through `imeta` tags in the [canonical specification](https://github.com/nostr-protocol/nips/blob/master/92.md). It gives clients a common place to carry structured information about media associated with an event, allowing renderers and upload flows to exchange more than an unadorned media URL.

In the [NIP-92 tag format](https://github.com/nostr-protocol/nips/blob/master/92.md), each variadic `imeta` tag begins with a required `url` pair and at least one additional space-delimited key/value pair. Fields borrowed from NIP-94 can describe MIME type, dimensions, blurhash, alt text, content hash, and fallback URLs. The media URL should also appear in the event content, and clients may ignore metadata that does not match a content URL.

The [media-metadata specification](https://github.com/nostr-protocol/nips/blob/master/92.md) separates author-signed metadata from properties a client observes after retrieval. A signed hash can support integrity checks, while dimensions, MIME type, and alt text remain claims until a client validates them. Multiple fallbacks improve availability, but each fetch still needs size limits, content checks, and clear failure states.

The specification has been canonical since [commit `5196ac1`](https://github.com/nostr-protocol/nips/commit/5196ac196a9e19cfbb9c6cd16d8081dd137e3572). For client developers, the useful boundary is clear: parse supported metadata defensively, preserve unknown fields where appropriate, and keep the event’s signed metadata distinct from any later observation about the referenced media.

Current implementation evidence includes [Damus](https://github.com/damus-io/damus), [Primal Android](https://github.com/PrimalHQ/primal-android-app), and [Amethyst](https://github.com/vitorpamplona/amethyst). The signed kind `1` example below was recovered in the current source pass. Its `imeta` tag carries a media URL, blurhash, and `dim 720x881`, showing published use without proving that every client interprets it identically.

```json
{"kind":1,"id":"d97726dafc86150f973caa3cd0d5c2af5d2d6f6c84ee1d4052d5214162fc7f87","pubkey":"c8383d81dd24406745b68409be40d6721c301029464067fcc50a25ddf9139549","created_at":1788992367,"tags":[["imeta","url https://i.nostr.build/DPblpK1x1rFO66QGeSTvBd.jpg","blurhash eeIX~zs:?wj@?c~qWDRPj]Ri_3RjWAaeWA?bWBWAayWBxtbIWAf+ae","dim 720x881"],["t","soveng"],["r","https://i.nostr.build/DPblpK1x1rFO66QGeSTvBd.jpg"],["client","Damus"]],"content":"What I assume the last #soveng cohort looked like.\n\nhttps://i.nostr.build/DPblpK1x1rFO66QGeSTvBd.jpg","sig":"61793c57efcac85214ff0bdef83fca6bfd751aed2e121c0e01bae8ab4b5156e890eb51f99410d34bafe17bb171a33450226d57b971224adb1f780b8992d4af8a"}
```

An `imeta` tag is metadata, not a storage guarantee. The [canonical NIP-92 commit](https://github.com/nostr-protocol/nips/commit/5196ac196a9e19cfbb9c6cd16d8081dd137e3572) does not make the referenced object permanent, reachable, safe, or authentic merely because its description appears in a signed event. Clients still need fetch limits, content validation, failure states, and an explicit distinction between author-signed claims and properties verified after retrieval.

---

Send a NIP-17 DM to share a project or news item through the [Nostr Compass project](https://github.com/andotherstuff/nostr-compass).
