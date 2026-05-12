---
title: 'Nostr Compass #22'
date: 2026-05-13
publishDate: 2026-05-13
draft: false
type: newsletters
description: 'Nostr VPN ships eight releases in a week culminating in v4.0.10, advancing from a redesigned device-pairing flow through a BoringSSL AEAD swap that doubles TCP throughput to sendmmsg batching and a full device-pairing UX overhaul; Marmot Protocol (White Noise) ships a frontend release completing the user-blocking feature and 31 merged PRs across MDK and backend; Grain v0.6.0 adds NIP-40, NIP-50, NIP-70, and NIP-45 in one milestone; Citrine v3.0.0-pre1 lands built-in Tor and relay aggregation; Amber v6.1.0-pre2 improves the new-app connection flow; Alby Hub v1.22.2 adds an AI and Agents page and Core Lightning support; Mostro ships concurrent taker bonds and v0.11.0 of mostro-core; Jumble ships five releases from v26.5.2 to v26.5.6 including notification grouping, recent search, and account-data persistence; Nostrord ships v1.0.0 through v1.0.2 with group share modals and Arch Linux packages; Flotilla 1.8.0 adds video calls, email rendering, and room mentions; Calendar by Formstr v1.5.1 ships appointment scheduling and Android calendar sync; Tamagostrich launches a decentralized NIP-78 Tamagotchi with sats rewards via NIP-47; NIP discussions surface Reservations, Escrow Services, Accommodation Listings, Onchain Zaps, and verifiable community rules. Two NIP deep dives cover NIP-78 (app-specific data) and NIP-98 (HTTP Auth).'
---

Welcome back to Nostr Compass, your weekly guide to Nostr protocol development.

**This week:** [Nostr VPN](https://github.com/mmalmi/nostr-vpn) ships [eight releases in seven days](#nostr-vpn-ships-eight-releases-culminating-in-v4010) from a redesigned device-pairing flow through a FIPS AEAD swap that roughly doubles TCP throughput. [Marmot Protocol](https://github.com/marmot-protocol) (the foundation for [White Noise](https://github.com/marmot-protocol/whitenoise)) ships a [frontend release completing the user-blocking feature](#marmot-white-noise-ships-blocking-complete-frontend-and-31-merged-prs-across-mdk-and-backend) and 31 merged PRs across MDK and backend. [Grain](https://github.com/0ceanSlim/grain) ships [v0.6.0](#grain-v060-adds-nip-40-nip-50-nip-70-and-nip-45) with four new NIP implementations in one milestone. [Citrine](https://github.com/greenart7c3/Citrine) ships [v3.0.0-pre1](#citrine-v300-pre1-lands-built-in-tor-and-relay-aggregation) with built-in Tor and relay aggregation. [Amber](https://github.com/greenart7c3/Amber) ships [v6.1.0-pre2](#amber-v610-pre2-improves-new-app-connection-flow) with connection-flow and signing improvements. [Alby Hub](https://github.com/getAlby/hub) ships [v1.22.2](#alby-hub-v1222-adds-ai-and-agents-page-and-core-lightning-support) with an AI and Agents page and Core Lightning integration. [Mostro](https://github.com/MostroP2P/mostro) ships concurrent taker bonds and [mostro-core v0.11.0](#mostro-ships-concurrent-taker-bonds-and-mostro-core-v0110). [Jumble](https://github.com/CodyTseng/jumble) ships [five releases](#jumble-ships-five-releases-with-recent-search-and-account-persistence) with recent search history and account-data persistence fixes. [Nostrord](https://github.com/nostrord/nostrord) ships [three releases](#nostrord-ships-group-share-modals-media-upload-and-arch-linux-packages) with group share modals and Arch Linux packages. [Flotilla](https://flotilla.social) ships [1.8.0](#flotilla-180-ships-video-calls-email-rendering-and-room-mentions) with video calls, email rendering, and room mentions. [Calendar by Formstr](https://calendar.formstr.app) ships [v1.5.0](#calendar-by-formstr-ships-v150-with-appointment-scheduling-and-android-calendar-sync) with appointment scheduling and Android calendar sync. [FIPS](https://github.com/jmcorgan/fips) ships [v0.3.0](#fips-v030-ships-cross-platform-reach-nostr-peer-discovery-and-a-gateway-for-unmodified-lans) going cross-platform with Nostr-mediated peer discovery, NAT hole-punching via NIP-59 gift-wrap, and a new gateway binary for unmodified LAN hosts. [Amethyst](https://github.com/vitorpamplona/amethyst) merges [scheduled posts, NIP-9A community rule enforcement, and an embedded desktop relay](#amethyst-adds-scheduled-posts-nip-9a-community-rules-and-a-desktop-local-relay) across 78 PRs. [Sprout](https://github.com/block/sprout) ships [v0.0.10 and v0.0.11](#sprout-ships-v0010-and-v0011) with image handling and agent error fixes. [Clave](https://github.com/DocNR/clave) [continues its multi-account NostrConnect rollout](#clave-continues-multi-account-nostrconnect-rollout) with a unified Connect tab and a bunker connection-cap security fix. [Tamagostrich](https://github.com/Negr087/tamagostrich) [launches](#tamagostrich-launches-a-decentralized-nip-78-tamagotchi-with-sats-rewards) as a decentralized NIP-78 Tamagotchi where your pet's state lives on Nostr and milestones pay out sats via NIP-47. The NIP discussions surface [five new proposals](#protocol-and-spec-work) including Reservations, Escrow Services, Accommodation Listings, Onchain Zaps, and verifiable community rules. Two NIP deep dives cover [NIP-78](/en/topics/nip-78/) (app-specific data) and [NIP-98](/en/topics/nip-98/) (HTTP Auth).

## Top Stories

### Nostr VPN ships eight releases culminating in v4.0.10

[Nostr VPN](https://github.com/mmalmi/nostr-vpn), the Rust-based decentralized mesh VPN using Nostr for peer discovery and a FIPS-backed noise protocol for the data plane, shipped eight releases from [v4.0.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.1) to [v4.0.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.10) across macOS, Linux, Windows, and Android this week.

The headline change is in [v4.0.8](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.8): the AEAD was swapped from the RustCrypto `chacha20poly1305` soft backend to BoringSSL's ChaCha20-Poly1305 in `ring` 0.17, which uses hand-tuned NEON on aarch64 and AVX2/AVX-512 on x86_64. Docker benchmarks on identical hardware showed 2-node direct TCP throughput jumping from 437 to 1097 Mbps. The wire format is unchanged.

Earlier in the week, [v4.0.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.1) rebuilt the device-pairing flow with exit-node leak protection, a unified WireGuard config block under Exit Nodes, and signed/notarized macOS artifacts. [v4.0.2](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.2) improved LAN discovery with reusable multicast sockets so same-LAN peers prefer direct underlay paths. [v4.0.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.6) fixed a NAT traversal regression where a tunnel MTU bump caused full-sized datagrams to drop silently on adopted UDP transports. [v4.0.9](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.9) added `sendmmsg(2)` batching on the UDP send path, amortising per-packet `sendto` syscalls across 8-packet batches and pushing TCP single-stream from 1066 to 1548 Mbps (1.45×). [v4.0.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.10) shipped a full UX overhaul for device pairing: Invite Devices and Join Network are now separate cards, auto-import fires on paste of an `nvpn://invite/` string, scan/paste/from-file buttons gained text labels, and nearby pairing split into two independent 15-minute toggles. Windows multicast now joins every non-loopback interface so same-LAN peers are reliably discovered on multi-NIC hosts. A userspace WireGuard upstream runtime (boringtun-based) lands for macOS, enabling Mullvad/Proton-style exit routing without a kernel WG implementation.

### Marmot / White Noise ships frontend release completing user-blocking and 31 merged PRs across MDK and backend

[White Noise](https://github.com/marmot-protocol/whitenoise), the private group messaging app built on the [Marmot](/en/topics/marmot/) MLS-based protocol, shipped [v2026.5.7+24](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.5.7+24) on May 7 as the frontend release that completes the blocking feature set. The previous release shipped mute, search, and archive; this one finishes blocking. A blocked user is now hidden from invites, chat previews, message timelines, search results, and notifications, and their messages no longer count toward unread badges. Video attachments work end to end across devices. The offline notice now covers every screen.

The supporting work spans 31 merged PRs across MDK and the backend. MDK landed [PR #258](https://github.com/marmot-protocol/mdk/pull/258) with the extension v3 wire format and `disappearing_message_secs` schema, laying the groundwork for disappearing messages.

Frontend work includes [PR #653](https://github.com/marmot-protocol/whitenoise/pull/653) fixing archived chat summaries by switching to a point query so archived chats render correctly, [PR #644](https://github.com/marmot-protocol/whitenoise/pull/644) exposing a `subscribe_to_group_state` stream to Dart for reactive UI updates, and [PR #635](https://github.com/marmot-protocol/whitenoise/pull/635) fixing Android external signer notification recovery when the signer app is cold-started.

### Grain v0.6.0 adds NIP-40, NIP-50, NIP-70, and NIP-45

[Grain](https://github.com/0ceanSlim/grain), the Go-based Nostr relay and client library, shipped [v0.6.0](https://github.com/0ceanSlim/grain/releases/tag/v0.6.0) on May 6 with four new NIP implementations and a production-hardening pass. The v0.6 milestone adds [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md) event expiration, [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md) full-text search, [NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md) protected events, and [NIP-45](https://github.com/nostr-protocol/nips/blob/master/45.md) event counts.

Event expiration via [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md) lets publishers set an expiry timestamp so the relay discards events after they expire, used in practice for ephemeral presence events and time-limited announcements. [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md) full-text search lets clients issue `search` filters in REQ messages and let the relay do the matching work. Protected events via [NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md) prevent relays from resharing events without the author's explicit permission. [NIP-45](https://github.com/nostr-protocol/nips/blob/master/45.md) count queries let clients ask a relay to return a count of matching events, reducing bandwidth for "how many notes does this user have" style queries.

The release also ships production hardening: safer default configurations, corrected NIP-01 rejection responses, and better backpressure for slow consumers.

## Shipping this week

### Citrine v3.0.0-pre1 lands built-in Tor and relay aggregation

[Citrine](https://github.com/greenart7c3/Citrine), the Android app that turns a phone into a Nostr relay node, shipped [v3.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v3.0.0-pre1) as a pre-release this week. The headline additions are built-in Tor support for privacy-preserving relay access and relay aggregation, where Citrine can pull events from multiple upstream relays and serve them to local clients. [PR #139](https://github.com/greenart7c3/Citrine/pull/139) adds [NIP-77 (Negentropy Reconciliation)](/en/topics/nip-77/) support for efficient set-reconciliation-based event sync. [PR #137](https://github.com/greenart7c3/Citrine/pull/137) routes all URLs through the Tor proxy, [PR #133](https://github.com/greenart7c3/Citrine/pull/133) relieves UI thread pressure on the event-receive path, and [PR #132](https://github.com/greenart7c3/Citrine/pull/132) reduces battery drain from the relay aggregator. The release also adds an event analytics view with a pie chart breaking down stored events by kind.

### Amber v6.1.0-pre2 improves new-app connection flow

[Amber](https://github.com/greenart7c3/Amber), the Android signer app for [NIP-55 (Android Signer Application)](/en/topics/nip-55/) and [NIP-46](/en/topics/nip-46/), shipped [v6.1.0-pre2](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre2). The main fixes: the signer dialog now closes correctly after accepting a bunker request, malformed bunker requests show an invalid-request screen, and rate limiting is added for intent-based signing requests. [PR #430](https://github.com/greenart7c3/Amber/pull/430) fixes memory leaks and hot-path inefficiencies in the signing flow.

### Alby Hub v1.22.2 adds AI and Agents page and Core Lightning support

[Alby Hub](https://github.com/getAlby/hub), the self-custodial Lightning node and Nostr Wallet Connect server, shipped [v1.22.2](https://github.com/getAlby/hub/releases/tag/v1.22.2) with several major additions. The new AI and Agents page exposes Alby Hub's Lightning and NWC capabilities to AI agents and MCP-compatible tools. An integrated on-chain wallet mode lets users receive and send on-chain Bitcoin directly from Alby Hub. Custom user labels for transactions improve bookkeeping. Settings pages were redesigned for clarity, and budget selection was improved when creating app connections. The most-requested feature since launch shipped: Core Lightning (CLN) is now a supported backend alongside LND and LDK.

### Mostro ships concurrent taker bonds and mostro-core v0.11.0

[Mostro](https://github.com/MostroP2P/mostro), the peer-to-peer Bitcoin trading protocol on Nostr, merged 11 PRs this week advancing the taker bond feature that prevents griefing by requiring both parties to lock funds before a trade proceeds. [PR #733](https://github.com/MostroP2P/mostro/pull/733) implements concurrent taker bonds where multiple takers can submit bond invoices simultaneously and the first to lock wins, discarding the others. [PR #735](https://github.com/MostroP2P/mostro/pull/735) aligns the bond invoice memo with spec section 6.1, and [PR #730](https://github.com/MostroP2P/mostro/pull/730) documents `cancel_action` handling for the `WaitingTakerBond` status.

[mostro-core](https://github.com/MostroP2P/mostro-core) shipped [v0.11.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.11.0) with the matching library additions: [PR #144](https://github.com/MostroP2P/mostro-core/pull/144) adds `Action::PayBondInvoice` and `Status::WaitingTakerBond`, and [PR #143](https://github.com/MostroP2P/mostro-core/pull/143) adds the `BondResolution` payload for admin settle and cancel actions. [mostro-cli](https://github.com/MostroP2P/mostro-cli) shipped [v0.15.0](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.15.0) updating to mostro-core 0.11.0 and handling the anti-abuse bond flow.

### Jumble ships five releases with recent search and account persistence

[Jumble](https://github.com/CodyTseng/jumble), the relay-centric Nostr client available as both a web app and Electron desktop app, shipped five releases this week: [v26.5.2](https://github.com/CodyTseng/jumble/releases/tag/v26.5.2) through [v26.5.6](https://github.com/CodyTseng/jumble/releases/tag/v26.5.6). [v26.5.2](https://github.com/CodyTseng/jumble/releases/tag/v26.5.2) groups notifications by Today / This week / This month / Earlier with sticky date headers and replaces the third-party pull-to-refresh library with a native component. [v26.5.3](https://github.com/CodyTseng/jumble/releases/tag/v26.5.3) ships a macOS `.zip` alongside the `.dmg` so the Electron desktop build can apply in-place auto-updates (electron-updater cannot install from a `.dmg`). [v26.5.4](https://github.com/CodyTseng/jumble/releases/tag/v26.5.4) adds a self-implemented emoji picker with emoji-pack tabs. [v26.5.5](https://github.com/CodyTseng/jumble/releases/tag/v26.5.5) adds recent search history. A critical persistence bug is fixed in [v26.5.6](https://github.com/CodyTseng/jumble/releases/tag/v26.5.6): accounts and cached data now survive a full app restart after the renderer was moved to a stable `app://` origin.

### Nostrord ships group share modals, media upload, and Arch Linux packages

[Nostrord](https://github.com/nostrord/nostrord), a Nostr client targeting NIP-29 relay-based groups, shipped [v1.0.0](https://github.com/nostrord/nostrord/releases/tag/v1.0.0), [v1.0.1](https://github.com/nostrord/nostrord/releases/tag/v1.0.1), and [v1.0.2](https://github.com/nostrord/nostrord/releases/tag/v1.0.2) this week. [v1.0.1](https://github.com/nostrord/nostrord/releases/tag/v1.0.1) ships Arch Linux packages via AUR as `nostrord-bin` with PGP-signed `.pkg.tar.zst` artifacts ([PR #44](https://github.com/nostrord/nostrord/pull/44)), a jump-to-latest button when scrolled up in a busy channel ([PR #45](https://github.com/nostrord/nostrord/pull/45)), and image and media pasting directly in the chat input ([PR #46](https://github.com/nostrord/nostrord/pull/46)). [v1.0.2](https://github.com/nostrord/nostrord/releases/tag/v1.0.2) adds group sharing via [PR #49](https://github.com/nostrord/nostrord/pull/49) with a share modal that generates both a `nostr:naddr` URI (kind 39000, NIP-19 + NIP-21) and a web-friendly `nostrord.com/open/` link so groups can be shared across clients and platforms.

### FIPS v0.3.0 ships cross-platform reach, Nostr peer discovery, and a gateway for unmodified LANs

[FIPS](https://github.com/jmcorgan/fips) (Free Internetworking Peering System), the Nostr-native mesh networking project covered in [#20](/en/newsletters/2026-04-29-newsletter/#fips-adds-nostr-based-udpnat-bootstrap), shipped [v0.3.0](https://github.com/jmcorgan/fips/releases/tag/v0.3.0) this week, a major milestone that widens the project from Linux-only to Linux, macOS, Windows, and OpenWrt.

The headline addition is Nostr-mediated peer discovery with STUN-assisted UDP NAT traversal. Nodes now publish signed overlay adverts as kind:37195 parameterized replaceable events (the digits spell FIPS: 7=F, 1=I, 9=P, 5=S) on public Nostr relays. When both peers are behind NAT, the daemon coordinates a hole punch using [NIP-59 (Gift Wrap)](/en/topics/nip-59/) signaling for the offer/answer exchange. Previously, nodes could only peer if they already knew each other's address.

A new `fips-gateway` binary lets unmodified LAN hosts reach mesh destinations without running the FIPS daemon. DNS lookups for `.fips` names get virtual IPs from a `fd01::/112` pool; `gateway.port_forwards` config exposes LAN services to mesh peers. The gateway is enabled by default in the OpenWrt build, targeting consumer-grade router deployments.

The same ring 0.17 ChaCha20-Poly1305 swap that powered the Nostr VPN throughput jump this week also lands in FIPS v0.3.0, contributed by [@mmalmi](https://github.com/mmalmi), the Nostr VPN maintainer. Benchmarks on aarch64 show two-node TCP single-stream going from 437 to 1097 Mbps and three-node relay-path ping latency dropping from 7.68 ms average to 0.72 ms. Peer ACL via `/etc/fips/peers.allow` and `/etc/fips/peers.deny` files and an opt-in default-deny nftables baseline for the mesh interface also ship in this release.

### Camelus v1.10.1 ships desktop builds

[Camelus](https://github.com/leo-lox/camelus), the Nostr client for Android and desktop, shipped [v1.10.1](https://github.com/leo-lox/camelus/releases/tag/v1.10.1) with Windows and Linux desktop builds, expanding from mobile-only distribution.

### Flotilla 1.8.0 ships video calls, email rendering, and room mentions

[Flotilla](https://flotilla.social), the [NIP-29](/en/topics/nip-29/) relay-based group chat app from hodlbod, shipped [1.8.0](https://gitea.coracle.social/coracle/flotilla/src/tag/1.8.0) this week with several notable additions. Voice rooms now support video: participants can turn on cameras or share their screen mid-call, with a grid layout that switches to a pinnable single-feed view for screen sharing. Email rendering arrives via an update to the welshman library: Flotilla can now receive messages that embed HTML email content, such as forwards from email bridges or email-to-Nostr gateways, and renders the HTML inline with formatting, images, and links intact. Interoperability projects routing email into NIP-29 group spaces can now deliver readable, formatted messages to Flotilla users without stripping HTML. Room mentions let users reference other rooms and relays with clickable inline links. Space search now includes message content and local matches alongside channel names. The native share sheet on iOS and Android now works for space invite links. Calendar events embedded in chat always show the date.

### Calendar by Formstr ships v1.5.1 with appointment scheduling and Android calendar sync

[Calendar by Formstr](https://calendar.formstr.app) ([github.com/formstr-hq/nostr-calendar](https://github.com/formstr-hq/nostr-calendar)), a Nostr-native calendar app for public and private events, shipped [v1.5.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.0) on May 10 and [v1.5.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.1) on May 11. Appointment scheduling arrives in [PR #89](https://github.com/formstr-hq/nostr-calendar/pull/89), letting users create bookable time slots on their calendar. Read-only Android calendar integration in [PR #123](https://github.com/formstr-hq/nostr-calendar/pull/123) syncs Nostr events to the device calendar so they appear alongside other calendar apps. Event notifications ship in [PR #130](https://github.com/formstr-hq/nostr-calendar/pull/130). Users can now add or remove events from their busy list via [PR #134](https://github.com/formstr-hq/nostr-calendar/pull/134), and relay publish progress feedback in [PR #118](https://github.com/formstr-hq/nostr-calendar/pull/118) shows which relays accepted an event save. [v1.5.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.1) follows with a URL bug fix and ZSP metadata update.

## In Development

### Amethyst adds scheduled posts, NIP-9A community rules, and a desktop local relay

[Amethyst](https://github.com/vitorpamplona/amethyst), the feature-rich Android client, merged 78 PRs this week across several significant feature areas.

Scheduled posts land on Android in [PR #2765](https://github.com/vitorpamplona/amethyst/pull/2765): users can compose a note and set a future publish time, with the queue managed locally on device. A desktop build gains an embedded local relay with SQLite event persistence in [PR #2841](https://github.com/vitorpamplona/amethyst/pull/2841), allowing the desktop client to serve as its own relay node and handle high connection counts without an external relay.

Three PRs implement NIP-9A community rules directly in the client: [PR #2798](https://github.com/vitorpamplona/amethyst/pull/2798) validates posts against community rules in the composer before sending, [PR #2799](https://github.com/vitorpamplona/amethyst/pull/2799) adds a structured NIP-9A rules editor to the new-community flow, and [PR #2800](https://github.com/vitorpamplona/amethyst/pull/2800) adds an opt-in NIP-9A feed filter so community members can hide posts that violate the published rules. This is the first client-side implementation of the NIP-9A draft proposed in the NIPs repo this week.

[PR #2812](https://github.com/vitorpamplona/amethyst/pull/2812) redacts secrets and sensitive payloads from debug logs across both Quartz and Amethyst, a security fix for users who share crash reports. [PR #2842](https://github.com/vitorpamplona/amethyst/pull/2842) adds LAN video casting via Chromecast in the Google Play build. Two-stage zap progress shows in [PR #2831](https://github.com/vitorpamplona/amethyst/pull/2831) so users can see when a zap is pending vs confirmed. [PR #2855](https://github.com/vitorpamplona/amethyst/pull/2855) splits the notifications tab into "Following" and "Everyone" views. [PR #2821](https://github.com/vitorpamplona/amethyst/pull/2821) adds rich [NIP-92 (imeta)](/en/topics/nip-92/) tags to every published HLS event and auto-publishes a kind:1 sibling note so live streams appear in standard feeds and are discoverable by clients that do not support [NIP-53 (Live Activities)](/en/topics/nip-53/).

### Shopstr adds MCP audit logging and session security

[Shopstr](https://github.com/shopstr-eng/shopstr), the decentralized marketplace on Nostr, merged five PRs this week. Audit logging for the MCP tool layer lands in [PR #456](https://github.com/shopstr-eng/shopstr/pull/456) so marketplace operators can trace agent actions. Session security tightens in [PR #477](https://github.com/shopstr-eng/shopstr/pull/477), which pins MCP sessions to their originating API key and adds TTL eviction to prevent session hijacking. Missing app routes were added to `RESERVED_SLUGS` in [PR #476](https://github.com/shopstr-eng/shopstr/pull/476) so short usernames that match route paths cannot be registered as shop handles.

### Dart NDK adds web support and seal signature verification

[Dart NDK](https://github.com/relaystr/dart_ndk), the Dart library for Nostr protocol development used in Flutter apps, merged six PRs this week. Web support arrives in `SembastCacheManager` via [PR #571](https://github.com/relaystr/dart_ndk/pull/571) so web builds can persist cached events to browser storage. Seal signature verification lands in [PR #595](https://github.com/relaystr/dart_ndk/pull/595) for the [NIP-59 (Gift Wrap)](/en/topics/nip-59/) flow so clients can confirm the inner seal was created by the expected sender. A tag-parsing fix in [PR #597](https://github.com/relaystr/dart_ndk/pull/597) corrects handling of public tags on private lists where tags appear in both encrypted and unencrypted portions of a list event.

### rust-nostr refactors tags and proxy connection

[rust-nostr](https://github.com/rust-nostr/nostr), the Rust SDK with bindings for Python, Kotlin, Swift, and JavaScript, merged three PRs this week. [PR #1347](https://github.com/rust-nostr/nostr/pull/1347) is a large tags rework that normalizes tag access across the SDK. [PR #1351](https://github.com/rust-nostr/nostr/pull/1351) replaces the `Connection` type with `Proxy` in the SDK layer for cleaner proxy configuration, and [PR #1349](https://github.com/rust-nostr/nostr/pull/1349) fixes subscription verification for multi-filter REQs where a subscription with multiple filters was not correctly matched against incoming events.

### Sprout ships v0.0.10 and v0.0.11

[Sprout](https://github.com/block/sprout), Block's Nostr client and relay covered in [#21](/en/newsletters/2026-05-06-newsletter/#sprout-ships-desktop-v004-and-v005-alongside-nip-oa-agent-authentication-and-the-pair-relay-sidecar), shipped [v0.0.10](https://github.com/block/sprout/releases/tag/v0.0.10) and [v0.0.11](https://github.com/block/sprout/releases/tag/v0.0.11) with mention autocomplete improvements, image download support, and agent error-handling fixes.

### Clave continues multi-account NostrConnect rollout

[Clave](https://github.com/DocNR/clave), the iOS NIP-46 remote signer covered in [#21](/en/newsletters/2026-05-06-newsletter/#clave-v020-launches-multi-account-on-ios-with-nip-46-nostr-connect-signing), shipped further builds this week advancing its multi-account NostrConnect work. [PR #52](https://github.com/DocNR/clave/pull/52) promotes Connect from a sheet presented from the home view to a top-level cross-account tab, with all account-binding for pairing flows going through a unified picker. A security fix in build 71 closes a per-account 5-connection cap bypass that existed due to a timing bug in the bunker flow, now enforced at three layers: the entry gate, the in-sheet rotation gate, and the NSE-side check.

## New Projects

### Tamagostrich launches a decentralized NIP-78 Tamagotchi with sats rewards

[Tamagostrich](https://github.com/Negr087/tamagostrich) is a browser-based virtual pet game launched at IDENTITY Hackathon 2026 where a baby ostrich, Nori, evolves through your Nostr social activity. Pet state lives in a [NIP-78](/en/topics/nip-78/) kind:30078 event so it syncs across every device sharing the same keypair. Zaps, reactions, reposts, and new followers grant XP; without activity, happiness and energy decay 100 points per 24 hours. Milestone rewards pay out in sats automatically via [NIP-47 (Nostr Wallet Connect)](/en/topics/nip-47/): 50 sats at level 5, 210 sats at level 10, and 420 sats at the maximum level 21, sent to the user's `lud16` address with claim state recorded in the NIP-78 event to prevent double payment.

## Protocol and spec work

The NIPs repository merged [PR #2338](https://github.com/nostr-protocol/nips/pull/2338) fixing README reference links for Marmot event kinds and the geocaching kind 37516. Five new proposals opened this week:

[PR #2331](https://github.com/nostr-protocol/nips/pull/2331) proposes **NIP-9A: Verifiable Community Rules**, introducing kind:34551, a parameterized replaceable event that lets a community owner publish a machine-readable, cryptographically signed rules document. Clients fetch the rules before the user submits a post and reject the draft locally if it violates any rule, surfacing the violation before send. This addresses a gap in NIP-72 (Reddit-style communities), where the community definition event (kind:34550) already carries a freeform `rules` tag for human readers but has no machine-readable counterpart. The companion [PR #2337](https://github.com/nostr-protocol/nips/pull/2337) adds an optional `nip9a` field to NIP-11 relay information documents, carrying an addressable event coordinate so clients can discover which kind:34551 rules document a relay enforces for relay-wide write policies independent of any community page.

[PR #2335](https://github.com/nostr-protocol/nips/pull/2335) proposes **Reservation Events for Nostr Marketplaces**, defining kind:32122 (parameterized replaceable reservation events), kind:1326 (append-only transition audit records), and kind:32124 (post-trade reviews). Negotiation is private: draft proposals are sent as NIP-59 gift-wrapped structured-message child events between buyer and seller, so they never hit public relays. Once both parties agree, a commit-stage kind:32122 event goes public and affects listing availability. A per-trade temporary key lets buyers participate without exposing their long-lived pubkey publicly; a `participant_proof` tag binds the temp key to the real identity for escrow and review verification. Calendar by Formstr shipped appointment scheduling this week using an app-specific flow; a standard kind:32122 would let any calendar app, marketplace, or scheduling service interoperate on bookings.

[PR #2334](https://github.com/nostr-protocol/nips/pull/2334) proposes **Escrow Services for Nostr Marketplaces**, using kind:30303 (parameterized replaceable service advertisements) for escrow operators to declare their EVM contract address, bytecode hash (for client-side contract verification), supported chain (e.g. Rootstock chainId 30), fee schedule, and accepted tokens. Buyers and sellers publish kind:17388 replaceable events declaring their trusted escrow providers and accepted payment forms; clients use these to match compatible parties to an escrow before a trade begins. Mostro ships concurrent taker bonds this week for Lightning P2P trades; this NIP extends similar trustless settlement mechanics to Shopstr-style EVM-settled goods markets.

[PR #2333](https://github.com/nostr-protocol/nips/pull/2333) proposes **Accommodation Listing Profiles for NIP-99 Marketplace Listings**, extending NIP-99 classified listings with H3 geospatial index `g` tags and accommodation-specific promoted fields for short-term rental listings. H3 tags allow clients to query listings by geographic cell without a centralized mapping service. Generic marketplace fields like instant-book and negotiability stay in the NIP-99 base; only accommodation-specific tags go in this profile. Combined with the Reservations and Escrow proposals this week, the three drafts form an interlocking stack: list a property (2333), receive and negotiate a booking (2335), and settle payment with dispute resolution (2334).

[PR #2332](https://github.com/nostr-protocol/nips/pull/2332) proposes **NIP-BC: Onchain Zaps (kind 8333)**, exploiting a direct identity between Nostr keys and Bitcoin Taproot addresses: a Nostr pubkey is a 32-byte x-only secp256k1 key, and so is a BIP-341 P2TR internal key, meaning any Nostr user already has a deterministic mainnet Bitcoin address derivable from their pubkey alone — no LNURL, custodian, or Lightning address required. The kind number mirrors NIP-57's convention: 9735 is the Lightning P2P port; 8333 is Bitcoin mainnet's P2P port. A `kind:8333` event contains the txid in an `i` tag (using NIP-73 external content identifiers), the recipient pubkey in a `p` tag, a self-reported `amount` in satoshis, and an optional `e` or `a` tag for the zapped event. Because the amount is self-reported, clients must verify the event by fetching the transaction and summing outputs that pay the derived Taproot address. Senders can optionally include an inline SPV proof via `block` and `proof` tags so verifiers with only the 75 MB block header chain can validate without a remote API call. The spec also extends NIP-07 and NIP-46 with a `signPsbt` method so browser signers and remote signers can sign the underlying Bitcoin transaction using the same key. The proposal draws on an existing Ditto implementation and clients should present verified onchain zaps alongside NIP-57 Lightning zap receipts and NIP-61 Nutzaps in aggregate zap totals.

## NIP deep dive: NIP-78 (App-specific data)

[NIP-78](/en/topics/nip-78/) defines a standard way for applications to store arbitrary private or public data on behalf of a user using Nostr events. The core event kind is 30078, a parameterized replaceable event where the `d` tag is an application-defined identifier string. An application gives its storage slot a unique `d` tag (for example `tamagostrich-pet-state` or `amethyst-settings`) and publishes a 30078 event with whatever JSON or text content it needs to persist. Because 30078 is replaceable and scoped by `d` tag, the application can update the stored state by publishing a new event with the same `d` tag, and the relay retains only the latest version.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 30078,
  "tags": [
    ["d", "tamagostrich-pet-state"]
  ],
  "content": "{\"level\":7,\"xp\":1420,\"happiness\":82,\"energy\":61}",
  "sig": "<128-char hex>"
}
```

The primary motivation is cross-device synchronization without a centralized server. Any client that knows a user's public key and the application's `d` tag can fetch the current state from the user's relay set and reconstruct the application state on any device. The user owns the data because it lives in events signed by their keypair, and they can choose which relays to publish to based on their relay list from [NIP-65 (Relay List Metadata)](/en/topics/nip-65/).

For private application data, NIP-78 events can encrypt the content field using [NIP-44 (Versioned Encryption)](/en/topics/nip-44/) or the older [NIP-04](/en/topics/nip-04/) before publishing, so the relay stores ciphertext that only the key holder can decrypt. Public application data, like Tamagostrich's achievement badges displayed on the user's profile, can be stored unencrypted so other clients can read and display it.

The spec deliberately leaves the content format open. Applications choose their own schema; NIP-78 only standardizes the event kind and the `d`-tag scoping mechanism. This means different apps using NIP-78 do not interfere with each other as long as they choose distinct `d` tag prefixes. The common convention is to prefix `d` tags with the application name to reduce collision risk.

Current users of NIP-78 include Tamagostrich (pet state sync), Wisp (kind:30078 wallet backup and cross-device security settings sync), NosPress (CMS orchestration state), and several Nostr client settings sync implementations.

---

**Primary sources:**
- [NIP-78 Specification](https://github.com/nostr-protocol/nips/blob/master/78.md)
- [Tamagostrich](https://github.com/Negr087/tamagostrich): production implementation this week

**See also:**
- [NIP-51: Lists](/en/topics/nip-51/)
- [NIP-65: Relay List Metadata](/en/topics/nip-65/)

## NIP deep dive: NIP-98 (HTTP Auth)

[NIP-98](/en/topics/nip-98/) defines an HTTP authentication scheme that lets Nostr keypairs authorize requests to HTTP servers, eliminating the need for usernames, passwords, or OAuth tokens for server-side API access. A client constructs a short-lived Nostr event of kind 27235, signs it with their private key, base64-encodes the JSON, and sends it in an `Authorization: Nostr <base64>` HTTP header.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 27235,
  "tags": [
    ["u", "https://files.example.com/upload"],
    ["method", "POST"],
    ["payload", "<sha256-hash-of-request-body>"]
  ],
  "content": "",
  "sig": "<128-char hex>"
}
```

The kind 27235 event includes the HTTP method in a `method` tag, the full request URL in a `u` tag, and a `created_at` timestamp. The server validates the signature, checks that the method and URL match the actual request, and verifies that the timestamp is recent (within a few minutes) to prevent replay attacks. If validation passes, the server treats the requesting pubkey as the authenticated identity.

The design means any server that implements NIP-98 can authenticate Nostr users without any prior registration, account creation, or shared secret. From the user's perspective, authentication is transparent: their Nostr signing key is also their API credential. From the server's perspective, a valid NIP-98 header is a cryptographic proof that the holder of a specific keypair intentionally made this request at this time to this URL.

NIP-98 is used in Blossom ([BUD-01](https://github.com/hzrd149/blossom/blob/master/buds/01.md)) for authenticating blob uploads and downloads. Routstr uses it for per-request HTTP API access control with npub-level RBAC. Sprout uses it for git transport auth and REST relay access, replacing Bearer token auth entirely in a recent refactor. Clave uses it for proxy pairing calls. Alby Hub uses NIP-98-derived authentication for its admin API, and Nostr.build uses it for upload authorization.

The spec defines one optional extension: a `payload` tag containing the SHA-256 hash of the request body, which lets the server verify that the signed event and the request body were created together, preventing a MITM from substituting a different body after the client signed the auth event.

---

**Primary sources:**
- [NIP-98 Specification](https://github.com/nostr-protocol/nips/blob/master/98.md)
- [BUD-01: Blossom upload auth](https://github.com/hzrd149/blossom/blob/master/buds/01.md)

**See also:**
- [NIP-96: HTTP File Storage Integration](/en/topics/nip-96/)
