---
title: 'Nostr Compass #19'
date: 2026-04-22
publishDate: 2026-04-22
draft: false
type: newsletters
description: 'Amethyst ships Marmot MIP compliance, NIP-72 community creation, NIP-75 zap goals, and a MoQ-transport audio rooms stack; TollGate v0.1.0 stabilizes pay-per-use internet over Nostr and Cashu; nostream lands NIP-45 counts, NIP-62 vanish, query hardening, and complete NIP-11 parity; the Formstr suite hardens Pollerama security, ships Forms i18n and Google Form import, and lands RRULE support in Nostr Calendar v1.3.0 and v1.4.0; Forgesworn publishes a new signing, identity, and paid-API stack for Nostr; ShockWallet uses Nostr for multi-device Lightning wallet sync; StableKraft ships v1.0.0 as a music-and-podcast feed PWA with Nostr features; WoT Relay v0.2.1 migrates its eventstore to LMDB; and topaz ships as a Nostr relay for Android.'
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** [Amethyst](https://github.com/vitorpamplona/amethyst) lands a large Marmot, communities, and MoQ audio rooms pass, [TollGate](https://github.com/OpenTollGate/tollgate) stabilizes pay-per-use internet access over Nostr and Cashu in [v0.1.0](#tollgate-v010-stabilizes-pay-per-use-internet-over-nostr-and-cashu), and [nostream](https://github.com/Cameri/nostream) closes a week of relay work around [NIP-45](/en/topics/nip-45/), [NIP-62](/en/topics/nip-62/), compression, query hardening, and complete [NIP-11](/en/topics/nip-11/) parity. [Forgesworn](#forgesworn-publishes-a-29-repo-cryptographic-toolkit-for-nostr) drops a full signing, identity, and paid-API stack for Nostr. [ShockWallet](#shockwallet-ships-nostr-native-lightning-wallet-sync-and-multi-node-connections) keeps pushing Nostr-native Lightning wallet flows. The Formstr suite ([Pollerama](#formstr-suite-pollerama-security-pass-forms-i18n-calendar-rrule-support), Forms, Calendar) merges 26 PRs across security hardening and RRULE support. [StableKraft](#stablekraft-v100-ships-the-first-stable-pwa-release), [Keep](#keep-android-v100-ships-with-reproducible-builds-and-zero-trackers), [topaz](#topaz-v002-ships-a-nostr-relay-for-android), [WoT Relay](#wot-relay-v021-migrates-eventstore-to-lmdb), [Flotilla](#flotilla-173-and-174-add-kind-9-wrapping-for-richer-nip-29-rooms), and [NipLock](#niplock-ships-a-nip-17-based-password-manager) round out the shipping list. Deep dives cover [NIP-72 moderated communities](/en/topics/nip-72/) and [NIP-57 zaps](/en/topics/nip-57/).

## Top Stories

### Amethyst ships Marmot MIP compliance, NIP-72 communities, zap goals, and MoQ audio rooms

[Amethyst](https://github.com/vitorpamplona/amethyst), the Android client maintained by vitorpamplona, merged 57 PRs this week. The week's headline themes are [Marmot](/en/topics/marmot/) encrypted-group compliance, first-class moderated communities, zap goals on live streams, and a new audio-rooms stack built on Media over QUIC.

On Marmot compliance, [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) aligns the embedded [MDK](https://github.com/marmot-protocol/mdk) implementation with the MIP-01 and MIP-05 wire formats, adding VarInt encoding of TLS-style length prefixes and round-trip validation against MDK test vectors. [PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) adds MIP-00 KeyPackage Relay List support so invitees advertise which relays serve their KeyPackages, and [PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436) closes the remaining admin-gate and media-handling gaps flagged by cross-client testing with [White Noise](https://github.com/marmot-protocol/whitenoise). Two correctness fixes land the same day: [PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466) corrects MLS commit framing so encrypted welcomes serialize to the same bytes [mdk-core](https://github.com/marmot-protocol/mdk) produces, and [PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471) resolves an outer-layer decryption bug that caused state divergence between Marmot co-admins. A second compliance pass in [PR #2477](https://github.com/vitorpamplona/amethyst/pull/2477) and [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493) closes additional commit-path and message-encryption gaps and adds a full MLS commit cryptography validator that checks signatures, key schedules, and welcome-message derivation against the reference vectors.

Alongside the protocol work, [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) ships `amy`, a command-line tool for Marmot and MLS group operations driven from Amethyst's implementation. Amy gives integrators a scriptable way to create groups, generate KeyPackages, simulate welcomes, and validate commits against a real Amethyst signer, which closes the biggest debugging gap for cross-client Marmot interop today.

[PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) adds first-class [NIP-72](/en/topics/nip-72/) community creation and management. Users can author the kind `34550` community definition, add moderators and relay hints, submit posts with an `a` tag pointing at the community, and manage pending approvals through kind `4549` approval events. The feature closes a long-standing gap between Amethyst and [noStrudel](https://github.com/hzrd149/nostrudel) on community moderation. [PR #2458](https://github.com/vitorpamplona/amethyst/pull/2458) and [PR #2473](https://github.com/vitorpamplona/amethyst/pull/2473) add emoji-set support and a full [NIP-30](https://github.com/nostr-protocol/nips/blob/master/30.md) emoji-pack management UI so users can curate their own custom emoji libraries.

[PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) wires [NIP-75](/en/topics/nip-75/) zap goals into the [NIP-53](/en/topics/nip-53/) Live Activities screen. Each live stream now carries a fundraising goal header with a progress bar, a one-tap zap button, and a top-zappers leaderboard. The leaderboard reads kind `9735` zap receipts bound to the stream's kind `30311` event and tallies them against the goal's `amount` target. [PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486) rounds out the live-stream surface with a dedicated Live Streams feed screen, [PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) adds NIP-53 proof-of-agreement and event-builder helpers, and [PR #2461](https://github.com/vitorpamplona/amethyst/pull/2461) adds lowest-resolution HLS in feed, picture-in-picture playback, and automatic resolution selection in full screen.

The most ambitious new surface is real-time audio. [PR #2494](https://github.com/vitorpamplona/amethyst/pull/2494) adds a [Media over QUIC](https://datatracker.ietf.org/group/moq/about/) transport client and audio-rooms support. MoQ's pub-sub model over QUIC fits live audio better than WebSocket relays because clients can subscribe to specific tracks and priorities and let the transport handle congestion. Paired with the new Public Chats screen in [PR #2487](https://github.com/vitorpamplona/amethyst/pull/2487), Amethyst now has an end-to-end surface for public audio rooms that sits alongside its Marmot encrypted messaging.

On the discovery and reliability side, [PR #2485](https://github.com/vitorpamplona/amethyst/pull/2485) and [PR #2490](https://github.com/vitorpamplona/amethyst/pull/2490) add a Follow Packs discovery feed and wire curated follow sets into the default onboarding preference, giving new users a populated timeline on first launch. [PR #1983](https://github.com/vitorpamplona/amethyst/pull/1983) lands an always-on notification service for real-time relay connections so Marmot DMs and mentions arrive without the app being foregrounded, and [PR #2480](https://github.com/vitorpamplona/amethyst/pull/2480) adds on-demand HLS video caching with adaptive cache sizing.

### TollGate v0.1.0 stabilizes pay-per-use internet over Nostr and Cashu

[TollGate](https://github.com/OpenTollGate/tollgate) cut its [v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0) on April 21, the first tagged snapshot of its specification set for pay-per-use network access. The protocol lets a device that can gate connectivity, such as a WiFi router, an Ethernet switch, or a Bluetooth tether, advertise pricing, accept [Cashu](/en/topics/cashu/) ecash tokens, and manage sessions through prepaid local tokens instead of accounts or subscriptions. A customer with a few sats in a local Cashu wallet can buy the next minute or megabyte of connectivity from any compatible TollGate on the network.

The release pins three layers of the architecture. The protocol layer, defined in [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md), specifies three base event shapes (Advertisement, Session, Notice), and [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) layers Cashu payments on top so a customer can redeem tokens from any mint the gate advertises. Above that sits the interface layer: [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md) through HTTP-03 define a plain-HTTP surface for devices on restrictive operating systems, and [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md) defines the Nostr-relay transport for clients that can open WebSockets. Finally, [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md) covers the medium layer by describing the captive-portal routing for paying customers.

The payment asset is a bearer token, so a customer can arrive with Cashu already in a local wallet and spend it immediately for the first minute of connectivity. Gates can also buy uplink from each other, so reach extends beyond a single operator. The new [TollGate topic page](/en/topics/tollgate/) covers the full layer stack.

### nostream merges 53 PRs for NIP-45, NIP-62, compression, and query hardening

[nostream](https://github.com/Cameri/nostream), the TypeScript relay implementation by Cameri, merged 53 PRs in a single week covering new NIP support, query performance, security hardening, and operational polish.

On feature work, [PR #522](https://github.com/Cameri/nostream/pull/522) adds [NIP-45](/en/topics/nip-45/) `COUNT` support so clients can ask the relay how many events match a filter without fetching them, and [PR #544](https://github.com/Cameri/nostream/pull/544) adds [NIP-62](/en/topics/nip-62/) right-to-vanish to the advertised feature list. [PR #548](https://github.com/Cameri/nostream/pull/548) extends the filter schema to accept uppercase tag filters (`#A` through `#Z`) per the recent tag-case conventions, and [PR #514](https://github.com/Cameri/nostream/pull/514) adds gzip and xz compression to event import and export so operators can move large event dumps between nodes without extra tooling.

Query performance and correctness land via [PR #534](https://github.com/Cameri/nostream/pull/534), which introduces a benchmarking harness and an optimization pass on the filter-to-SQL translation. [PR #524](https://github.com/Cameri/nostream/pull/524) fixes a whitelist/blacklist pubkey matching bug by replacing prefix matching with exact-match checks, [PR #553](https://github.com/Cameri/nostream/pull/553) adds a deterministic tie-breaker to `upsertMany` so concurrent inserts no longer race on equal `created_at` timestamps, and [PR #493](https://github.com/Cameri/nostream/pull/493) restricts the relay to trusting `X-Forwarded-For` only from configured trusted proxies. [PR #557](https://github.com/Cameri/nostream/pull/557) brings the relay to complete [NIP-11](/en/topics/nip-11/) relay information parity by aligning every advertised field with the current specification, including retention limits, authentication hints, and the trimmed optional-field set.

## Shipping This Week

### Primal Android ships Explore tab, NIP-05 verification, and audio player

[Primal Android](https://github.com/PrimalHQ/primal-android-app) pushed 11 merged PRs on top of last week's feed redesign. [PR #1021](https://github.com/PrimalHQ/primal-android-app/pull/1021) introduces a new Explore tab built around popular users, follow packs, and curated feeds, and [PR #1015](https://github.com/PrimalHQ/primal-android-app/pull/1015) adds a feed editor that prepopulates from Primal's Advanced Search DSL. [PR #994](https://github.com/PrimalHQ/primal-android-app/pull/994) ships [NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md) verification UI for profiles, and [PR #997](https://github.com/PrimalHQ/primal-android-app/pull/997) embeds an in-feed audio player that plays audio file attachments inline. [PR #1018](https://github.com/PrimalHQ/primal-android-app/pull/1018) adds [NIP-46](/en/topics/nip-46/) nostr-connect pairing from the wallet QR scanner, reusing the same camera path for signer pairing and wallet linking.

### strfry adds Prometheus write-path metrics and fixes NIP-42 AUTH envelope

[strfry](https://github.com/hoytech/strfry) shipped a batch of operator-facing improvements. [PR #194](https://github.com/hoytech/strfry/pull/194) adds a dedicated Prometheus write-path metrics exporter and a new connection gauge, and [PR #197](https://github.com/hoytech/strfry/pull/197) logs per-connection bytes up and down plus compression ratios for operators tracking bandwidth. [PR #192](https://github.com/hoytech/strfry/pull/192) promotes the hard-coded filter tag limit to a runtime-configurable option so operators can tune it without a recompile. On protocol correctness, [PR #201](https://github.com/hoytech/strfry/pull/201) changes [NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) AUTH failure responses from a `NOTICE` message to the `OK` envelope the NIP actually specifies, which was a long-standing interop wart for auth-gated relays.

### Shopstr hardens storefront security across 13 PRs

[Shopstr](https://github.com/shopstr-eng/shopstr), the Nostr marketplace client, merged 13 PRs this week dominated by security fixes. [PR #434](https://github.com/shopstr-eng/shopstr/pull/434) closes a stored-JavaScript hole in storefront links that allowed seller-to-visitor script execution, [PR #417](https://github.com/shopstr-eng/shopstr/pull/417) escapes storefront policy HTML rendering to block reflected XSS, and [PR #418](https://github.com/shopstr-eng/shopstr/pull/418) closes an unauthenticated cached-event deletion API that allowed cross-user data removal. [PR #433](https://github.com/shopstr-eng/shopstr/pull/433) requires authentication for cached-message reads, [PR #419](https://github.com/shopstr-eng/shopstr/pull/419) secures storefront mutation and event-cache endpoints behind proper auth, and [PR #435](https://github.com/shopstr-eng/shopstr/pull/435) and [PR #414](https://github.com/shopstr-eng/shopstr/pull/414) fix two server-side request forgery findings from code scanning. On functional bugs, [PR #421](https://github.com/shopstr-eng/shopstr/pull/421) makes the failed-relay-publish queue safe against replay, [PR #425](https://github.com/shopstr-eng/shopstr/pull/425) repairs a broken wallet-events fetch, and [PR #392](https://github.com/shopstr-eng/shopstr/pull/392) revalidates stored cart discounts before checkout.

### Nostria v3.1.26 through v3.1.28 add background music playback on Android

[Nostria](https://github.com/nostria-app/nostria) cut six releases this week from [v3.1.22](https://github.com/nostria-app/nostria/releases/tag/v3.1.22) through [v3.1.28](https://github.com/nostria-app/nostria/releases/tag/v3.1.28). The headline change in [v3.1.26](https://github.com/nostria-app/nostria/releases/tag/v3.1.26) is Android background music playback: the app keeps itself alive while audio is playing, with media controls available in the notification bar and on the lock screen. Follow-up releases [v3.1.27](https://github.com/nostria-app/nostria/releases/tag/v3.1.27) and [v3.1.28](https://github.com/nostria-app/nostria/releases/tag/v3.1.28) harden that new media-service surface. [Newsletter #18](/en/newsletters/2026-04-15-newsletter/#nostria-v3119-through-v3121-add-local-ai-image-generation) covered the preceding v3.1.19 through v3.1.21 local-image-generation release.

### Wisp v0.18.0-beta adds Normie Mode, For You feed, and NIP-29 group config

[Wisp](https://github.com/barrydeen/wisp), the Android client that spun out of Amethyst, shipped [v0.18.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.18.0-beta) on April 16. The release targets users arriving from non-Bitcoin-native contexts: [PR #462](https://github.com/barrydeen/wisp/pull/462) adds a Normie Mode that surfaces fiat-denominated amounts throughout the app, and [PR #464](https://github.com/barrydeen/wisp/pull/464) overhauls onboarding with a topics picker and a first-post coach. [PR #469](https://github.com/barrydeen/wisp/pull/469) adds a For You feed that blends extended follows, trending events, and followed hashtags.

On protocol work, [PR #471](https://github.com/barrydeen/wisp/pull/471) adds [NIP-29](/en/topics/nip-29/) group configuration for flags, invites, roles, and AUTH prompts, and [PR #478](https://github.com/barrydeen/wisp/pull/478) fixes an ordering bug so Wisp waits for [NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) AUTH before issuing group `9021`, `9007`, and `9009` events and surfaces admin-side failures. [PR #481](https://github.com/barrydeen/wisp/pull/481) broadcasts notes to the [NIP-65](/en/topics/nip-65/) inbox relays of mentioned pubkeys so replies reach their targets even when the sender's and recipient's relay sets do not overlap.

### NoorNote v0.8.4 adds Scheduled Posts and live stream zapping

[NoorNote](https://github.com/77elements/noornote) shipped [v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) and [v0.8.5](https://github.com/77elements/noornote/releases/tag/v0.8.5). The headline addition in v0.8.4 is a Scheduled Posts add-on: the app hands a fully signed event to a NoorNote-operated relay which publishes it at the scheduled moment, so private keys never leave the device. The same release adds one-tap zapping from live-stream cards, where the sats appear in the stream's chat overlay via [NIP-53](/en/topics/nip-53/), and keeps the wallet balance visible when the fiat-rate API is briefly unavailable. v0.8.5 fixes a timeline deduplication bug that caused duplicate posts on long Android scrolls.

### topaz v0.0.2 ships a Nostr relay for Android

[topaz](https://github.com/fiatjaf/topaz), a new Nostr relay that runs on Android phones from [fiatjaf](https://github.com/fiatjaf), published its [v0.0.2](https://github.com/fiatjaf/topaz/releases/tag/v0.0.2) release on 2026-04-17. The project is Kotlin-first and positions the phone as an always-available personal relay. At this stage the scope is narrow: a working relay in an installable Android package.

### StableKraft v1.0.0 ships the first stable music-and-podcast PWA release

[StableKraft](https://github.com/ChadFarrow/stablekraft-app) is a Next.js PWA for discovering, organizing, and streaming music pulled from podcast feeds, with Nostr for auth and social features and Lightning for V4V payments. It reached [v1.0.0](https://github.com/ChadFarrow/stablekraft-app/releases/tag/v1.0.0) on 2026-04-18. The same week tightened feed ingestion with a [15-minute OPML cache and illegal-XML stripping](https://github.com/ChadFarrow/stablekraft-app/commit/7ac90f6), and shrank the nightly reparse window from 720 hours to 24 hours in a [follow-up fix](https://github.com/ChadFarrow/stablekraft-app/commit/fbf337b) so newly added feeds self-heal faster.

### NipLock ships a NIP-17-based password manager

[NipLock](https://gitworkshop.dev/npub1z5jf78uhd68znuwwwu926th55rzd0wy8nd9clkr03cx22mwme0jqazk56h/relay.ngit.dev/passwd) is a password manager that stores and syncs credentials across devices using [NIP-17](/en/topics/nip-17/) gift-wrapped direct messages. Each password entry is a NIP-17 DM from the user's key to itself, so the same events replicate to any device that authenticates with the same key. Signing works with a raw `nsec`, browser extensions like [nos2x](https://github.com/fiatjaf/nos2x), or [Amber](https://github.com/greenart7c3/Amber) via [NIP-46](/en/topics/nip-46/), which keeps the master key off the client device.

### flotilla-budabit polishes its NIP-34 repo surface

The Budabit community's fork of [Flotilla](https://gitea.coracle.social/coracle/flotilla), [flotilla-budabit](https://github.com/Pleb5/flotilla-budabit), shipped a cluster of fixes to its NIP-34 git-over-nostr workflow. Updates this week [restore repo discussion controls](https://github.com/Pleb5/flotilla-budabit/commit/a6fb67e), [keep sticky repo tabs visible on detail pages](https://github.com/Pleb5/flotilla-budabit/commit/e2b891a), [load repo announcements from saved GRASP relays](https://github.com/Pleb5/flotilla-budabit/commit/43d5e9e), and [keep maintainer-applied patch status in sync](https://github.com/Pleb5/flotilla-budabit/commit/2dbb9f0). Staying close to upstream Flotilla, the fork prioritizes the repo view for Budabit community contributors.

### rx-nostr 3.7.2 through 3.7.4 add default verifier and optional constructor args

[rx-nostr](https://github.com/penpenpng/rx-nostr), the RxJS-based Nostr library, shipped [3.7.2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.2), [3.7.3](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.3), and [3.7.4](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.4). [PR #192](https://github.com/penpenpng/rx-nostr/pull/192) adds a default Schnorr signature verifier so callers no longer have to wire one up manually, and a paired [crypto@3.1.6](https://github.com/penpenpng/rx-nostr/releases/tag/crypto%403.1.6) corrects a `@noble/curves` usage bug that was producing spurious verification failures. [PR #195](https://github.com/penpenpng/rx-nostr/pull/195) in 3.7.4 makes the arguments of `createRxNostr()` optional so quick integrations can instantiate the library with zero configuration.

### Keep Android v1.0.0 ships with reproducible builds and zero trackers

[Keep](https://github.com/privkeyio/keep-android), a Nostr-native password and secret manager, shipped [v1.0.0](https://github.com/privkeyio/keep-android/releases/tag/v1.0.0) on April 21 after a run of hardening PRs. [PR #241](https://github.com/privkeyio/keep-android/pull/241) adds a reproducible build recipe with a pinned and verified toolchain, [PR #248](https://github.com/privkeyio/keep-android/pull/248) swaps Google ML Kit for ZXing to remove a Google Play Services dependency, and [PR #252](https://github.com/privkeyio/keep-android/pull/252) publishes an [Exodus Privacy scan](https://reports.exodus-privacy.eu.org/en/) showing zero trackers on the v1.0.0 build. [PR #256](https://github.com/privkeyio/keep-android/pull/256) adds a `zapstore.yaml` manifest so the v1.0.0 APK can be distributed through [zapstore](https://zapstore.dev) without an intermediate publisher.

### Flotilla 1.7.3 and 1.7.4 add kind-9 wrapping for richer NIP-29 rooms

[Flotilla](https://gitea.coracle.social/coracle/flotilla), hodlbod's [NIP-29](/en/topics/nip-29/) groups client, shipped [1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3) and [1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4). The main protocol change is kind-9 wrapping of non-chat content types, announced in [hodlbod's release note](nostr:nevent1qvzqqqqqqypzp978pfzrv6n9xhq5tvenl9e74pklmskh4xw6vxxyp3j8qkke3cezqyvhwumn8ghj76rzwghxxmmjv93kcefwwdhkx6tpdshszrnhwden5te0dehhxtnvdakz7qgawaehxw309a5x7ervvfhkgtnrdaexzcmvv5h8xmmrd9skctcqyrrclae7mhmm5dnumwfzhg3fxu74a4hh24jd8pvn8v0hye9w3g6tuljtr85) and tracked against [NIP PR #2310](https://github.com/nostr-protocol/nips/pull/2310). Wrapping calendar events, polls, and other non-chat payloads in kind `9` preserves the room context when those objects are sent into a group, so clients can render the embedded object without losing which room it came from.

The same release line adds polls, support for the Aegis URL scheme for [NIP-46](/en/topics/nip-46/) login, native share support for space invites, room mentions, mobile clipboard image paste, drafts, video in calls, and feed-pagination improvements. This is the first Flotilla release since [1.7.0 and 1.7.1](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.0), which [Newsletter #16](/en/newsletters/2026-04-01-newsletter/#flotilla-v170-adds-voice-rooms-and-email-login) covered for voice rooms and email login.

### WoT Relay v0.2.1 migrates eventstore to LMDB

[WoT Relay](https://github.com/bitvora/wot-relay), the web-of-trust-filtered relay by bitvora, shipped [v0.2.1](https://github.com/bitvora/wot-relay/releases/tag/v0.2.1) on 2026-04-22. [PR #97](https://github.com/bitvora/wot-relay/pull/97) migrates the eventstore to [LMDB](http://www.lmdb.tech/) and retunes the WoT bootstrap fetches so the relay builds its initial trust graph without exhausting upstream read budgets, and [PR #99](https://github.com/bitvora/wot-relay/pull/99) bumps `golang.org/x/crypto` to v0.45.0 for the corresponding security fixes. [PR #100](https://github.com/bitvora/wot-relay/pull/100) updates the advertised [NIP-11](/en/topics/nip-11/) software URL and version string for the release.

### Formstr suite: Pollerama security pass, Forms i18n, Calendar RRULE support

The Formstr suite merged 26 PRs across Pollerama, Formstr forms, and Nostr Calendar this week, with a clear security theme on the polling app and feature work on the rest.

[Pollerama](https://pollerama.fun), the [nostr-polls](https://github.com/formstr-hq/nostr-polls) web app for creating and voting on Nostr polls, hardened its key handling. [PR #182](https://github.com/formstr-hq/nostr-polls/pull/182) expires cached direct messages on logout so a shared device does not leak prior-user state, [PR #175](https://github.com/formstr-hq/nostr-polls/pull/175) moves the local key to secure browser storage, and [PR #171](https://github.com/formstr-hq/nostr-polls/pull/171) guards `JSON.parse` of kind `0` profile content across every login path so a malformed profile cannot crash the session. On the product side, [PR #186](https://github.com/formstr-hq/nostr-polls/pull/186) wires HTTPS deep linking for `pollerama.fun` so shared poll URLs open the app directly, and [PR #169](https://github.com/formstr-hq/nostr-polls/pull/169) makes author names clickable in poll results.

[Formstr](https://formstr.app), the [nostr-forms](https://github.com/formstr-hq/nostr-forms) suite for Nostr-native forms, broadened its input and onboarding surface. [PR #475](https://github.com/formstr-hq/nostr-forms/pull/475) adds audio and video URL support so a form can embed media directly, [PR #439](https://github.com/formstr-hq/nostr-forms/pull/439) introduces i18n to the web app, and [PR #466](https://github.com/formstr-hq/nostr-forms/pull/466) ships a Google Forms onboarding importer so existing form creators can migrate without rebuilding surveys. [PR #463](https://github.com/formstr-hq/nostr-forms/pull/463) closes a privacy leak by removing sensitive key logs from the browser console.

[Nostr Calendar by Formstr](https://calendar.formstr.app) cut [v1.3.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.3.0) and [v1.4.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.4.0) on the same day, headlined by a proper recurrence-rule surface. [PR #107](https://github.com/formstr-hq/nostr-calendar/pull/107) adds multiple and custom RRULE support so events can repeat on complex schedules beyond the single-cadence case, and [PR #101](https://github.com/formstr-hq/nostr-calendar/pull/101) corrects a long-standing bug by interpreting floating RRULE dates as UTC per RFC 5545, which had been causing event-time drift across timezones. [PR #97](https://github.com/formstr-hq/nostr-calendar/pull/97) lets users add shared events to their calendar, [PR #86](https://github.com/formstr-hq/nostr-calendar/pull/86) introduces list-level notification preferences, and [PR #112](https://github.com/formstr-hq/nostr-calendar/pull/112) ships the reworked login and loading path that lands in v1.4.0. All three projects build on [NIP-52](/en/topics/nip-52/) calendar events and share a common login stack.

### Also shipped: notedeck, nostr.blue, cliprelay, Captain's Log

A handful of clients cut iterative releases without headline features. Damus's Rust desktop and mobile client [notedeck](https://github.com/damus-io/notedeck) published [v0.10.0-beta.4](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.4) with column-rendering and relay-pool fixes. The Dioxus-based Rust client [nostr.blue v0.8.6](https://github.com/patrickulrich/nostr.blue/releases/tag/v0.8.6) pulled in [Dioxus 0.7.5](https://github.com/patrickulrich/nostr.blue/commit/d90b4ff) and unblocked the Android build by [converting the native audio bridge](https://github.com/patrickulrich/nostr.blue/commit/4207f0c) to a `manganis::ffi` plugin. [cliprelay](https://github.com/tajava2006/cliprelay), a cross-device clipboard-sync tool that relays entries through Nostr, shipped [Desktop v0.0.3](https://github.com/tajava2006/cliprelay/releases/tag/desktop%2Fv0.0.3) and [Android v0.0.4](https://github.com/tajava2006/cliprelay/releases/tag/android%2Fv0.0.4), tightening the sync loop and dropping 32-bit Android variants. [Captain's Log](https://github.com/nodetec/comet) published three alpha builds whose most useful addition is sync-relay [liveness detection](https://github.com/nodetec/comet/releases/tag/alpha-95f47bd) so dropped sockets are replaced without user action.

## In Development

### whitenoise-rs refactors to session-scoped account views

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs), the Rust daemon under the [Marmot](/en/topics/marmot/) client, merged 15 PRs advancing a multi-phase refactor from global singletons to per-account `AccountSession` views. The goal is to break one shared monolith into smaller per-account surfaces that are easier to reason about, test, and evolve without side effects leaking across the whole daemon.

The foundation landed in [PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743) with the `AccountSession` and `AccountManager` scaffolding, followed by scoped relay handles in [PR #753](https://github.com/marmot-protocol/whitenoise-rs/pull/753). Subsequent phases moved drafts and settings, message ops, group read and write, membership, push notifications, key-package reads, and group creation onto session-owned surfaces across [PRs #760 through #769](https://github.com/marmot-protocol/whitenoise-rs/pulls?q=is%3Apr+is%3Amerged+768+OR+763+OR+766). Phase 15 closed the loop in [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770), which rehomes event dispatch onto the session so each account consumes its own relay traffic without contention on a shared dispatcher.

### White Noise app adds block/unblock UI, leave-group, and offline notices

[White Noise](https://github.com/marmot-protocol/whitenoise), the [Marmot](/en/topics/marmot/) client, added the missing group-lifecycle controls. [PR #578](https://github.com/marmot-protocol/whitenoise/pull/578) ships the block and unblock UI on top of a block hook landed in [PR #573](https://github.com/marmot-protocol/whitenoise/pull/573), and [PR #571](https://github.com/marmot-protocol/whitenoise/pull/571) pairs with [PR #572](https://github.com/marmot-protocol/whitenoise/pull/572) to wire Rust-side `clear_chat`, `delete_chat`, and `leave_and_delete_group` into the app. [PR #569](https://github.com/marmot-protocol/whitenoise/pull/569) and [PR #576](https://github.com/marmot-protocol/whitenoise/pull/576) add offline notices on chat and settings screens so users know when the daemon cannot reach its relays. [PR #585](https://github.com/marmot-protocol/whitenoise/pull/585) narrows the broad "delete all key packages" path to a "delete legacy key packages" operation so a client migrating between KeyPackage formats no longer wipes its current keys along with the legacy ones.

### MDK adds mixed-version invite support and SelfUpdate convergence

[MDK](https://github.com/marmot-protocol/mdk), the [Marmot](/en/topics/marmot/) Development Kit, merged seven PRs. The thread running through the work is compatibility, keeping clients on slightly different Marmot versions able to invite each other, rotate their own state, and recover cleanly from malformed inputs.

The headline fix is [PR #261](https://github.com/marmot-protocol/mdk/pull/261), which computes a group's `RequiredCapabilities` as the LCD of invitee capabilities and unblocks mixed-version invites between [Amethyst](https://github.com/vitorpamplona/amethyst) and [White Noise](https://github.com/marmot-protocol/whitenoise). [PR #264](https://github.com/marmot-protocol/mdk/pull/264) converges the SelfUpdate wire format across implementations; SelfUpdate is the control message a group member sends when rotating its own KeyPackage or capability state, so drift there silently breaks self-rotation across clients even when invites and welcomes still parse. On robustness, [PR #262](https://github.com/marmot-protocol/mdk/pull/262) parses invitee key packages before persisting the creator's signer so a malformed invitee cannot leave stray state, [PR #256](https://github.com/marmot-protocol/mdk/pull/256) fixes receiver-side admin depletion validation, and [PR #259](https://github.com/marmot-protocol/mdk/pull/259) prevents the in-memory storage backend from evicting security-critical state under pressure. [PR #265](https://github.com/marmot-protocol/mdk/pull/265) exposes a `group_required_proposals` accessor so clients can inspect the proposals that MUST land before the next commit is valid without reaching into MDK internals.

### nostter adds NIP-44 encryption across people lists, bookmarks, and mutes

[nostter](https://github.com/SnowCait/nostter) merged 10 PRs. [PR #2088](https://github.com/SnowCait/nostter/pull/2088) adds [NIP-44](/en/topics/nip-44/) encryption to mute lists, [PR #2089](https://github.com/SnowCait/nostter/pull/2089) adds it to bookmarks, and [PR #2090](https://github.com/SnowCait/nostter/pull/2090) adds it to people lists, all migrating away from [NIP-04](/en/topics/nip-04/) where applicable. [PR #2087](https://github.com/SnowCait/nostter/pull/2087) removes a legacy kind-30000 mute migration path now that the encrypted kind-10000 flow has stabilized.

### zap.cooking ships Nourish scoring and a reusable comment thread

[zap.cooking](https://github.com/zapcooking/frontend), the Nostr recipe client, merged 20 PRs this week. The headline feature is a new Nourish recipe-scoring module ([PR #317](https://github.com/zapcooking/frontend/pull/317), [PR #319](https://github.com/zapcooking/frontend/pull/319)) that rates recipes on nutritional axes. Alongside it, a four-stage refactor from [PR #299](https://github.com/zapcooking/frontend/pull/299) through [PR #302](https://github.com/zapcooking/frontend/pull/302) pulls the Comments module into a reusable `CommentThread` that can be dropped into any view. Recipe-side polish includes scaling in [PR #309](https://github.com/zapcooking/frontend/pull/309), a unified media-upload button in [PR #307](https://github.com/zapcooking/frontend/pull/307), and a profile Replies tab in [PR #310](https://github.com/zapcooking/frontend/pull/310).

### ridestr extracts shared rider coordinator

[ridestr](https://github.com/variablefate/ridestr), the decentralized ride-sharing app, merged 10 PRs refactoring its Compose screens into focused components and extracting rider and driver protocol logic into a shared `:common` coordinator module ([PR #70](https://github.com/variablefate/ridestr/pull/70)). [PR #60](https://github.com/variablefate/ridestr/pull/60) adds a kind `3189` driver-ping receiver for the Roadflare side of the app.

### Blossom drafts a BUD-01 Sunset header for blob expiration

[Blossom](https://github.com/hzrd149/blossom), hzrd149's protocol for storing blobs on HTTP servers keyed by SHA-256 hash, opened [PR #99](https://github.com/hzrd149/blossom/pull/99) to add a `Sunset` header to BUD-01. A server can use the header to advertise a future timestamp at which a blob will stop being served, so clients can plan around limited retention without first hitting a 404. Because the proposal uses standard [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html) semantics and is advisory only, a server is free to keep the blob longer or to honor the declared expiration on a best-effort basis.

## New Projects

### Forgesworn publishes a 29-repo cryptographic toolkit for Nostr

[Forgesworn](https://github.com/forgesworn) shipped 29 open-source repositories over five days covering signing, identity, attestations, web-of-trust, and paid-API discovery on Nostr.

The signing stack anchors on [nsec-tree](https://github.com/forgesworn/nsec-tree), a deterministic sub-identity derivation scheme that turns one master secret into unlimited unlinkable Nostr identities, and on [Heartwood](https://github.com/forgesworn/heartwood), an NIP-46 remote signer that runs on a Raspberry Pi with Tor on by default. [Sapwood](https://github.com/forgesworn/sapwood) adds a web management UI for shaping a Heartwood signer, and [heartwood-esp32](https://github.com/forgesworn/heartwood-esp32) ships a spike of the same signing token logic on a Heltec WiFi LoRa 32 board. [nsec-tree-cli](https://github.com/forgesworn/nsec-tree-cli) exposes the derivation, proof, and Shamir recovery flows for offline-first operation.

On identity and trust, [Signet](https://github.com/forgesworn/signet) reached [v1.6.0](https://github.com/forgesworn/signet/releases/tag/v1.6.0) as a decentralized identity verification protocol for Nostr, with a QR-based pairing flow whose session pubkey is validated and pinned to the relay. [nostr-attestations](https://github.com/forgesworn/nostr-attestations) defines a single kind `31000` event (NIP-VA) for credentials, endorsements, vouches, provenance, licensing, and trust, consolidating what today is spread across ad-hoc event shapes. [nostr-veil](https://github.com/forgesworn/nostr-veil) builds a privacy-preserving web of trust on top: NIP-85 assertions backed by [LSAG ring signatures](https://github.com/forgesworn/ring-sig) on secp256k1, so a vouch can prove group membership without revealing which member issued it.

The monetization side covers paid APIs over Lightning and Nostr. [toll-booth](https://github.com/forgesworn/toll-booth) is an L402 middleware for Express, Hono, Deno, Bun, and Cloudflare Workers that turns any API into a Lightning toll booth in one line, with [toll-booth-dvm](https://github.com/forgesworn/toll-booth-dvm) exposing the gated API as a [NIP-90](/en/topics/nip-90/) Data Vending Machine and [toll-booth-announce](https://github.com/forgesworn/toll-booth-announce) bridging to [402-announce](https://github.com/forgesworn/402-announce), which publishes kind `31402` parameterised replaceable events for HTTP 402 service discovery on Nostr. [402-indexer](https://github.com/forgesworn/402-indexer) is the crawler that picks those announcements up. The org also published a [29-NIP draft collection](https://github.com/forgesworn/nip-drafts) covering service coordination, trust, payments, disputes, key hierarchy, resource curation, and paid API discovery.

Everything is TypeScript, zero-dependency where possible, and released through a new bash-only supply-chain-hardened tool called [anvil](https://github.com/forgesworn/anvil) with multi-runner reproducible-build attestation and OIDC trusted publishing. Several primitives in the set, including ring signatures, range proofs, and Shamir word shares, fill long-standing gaps in the Nostr library layer.

### ShockWallet ships Nostr-native Lightning wallet sync and multi-node connections

[ShockWallet](https://github.com/shocknet/wallet2) is a Lightning wallet that uses Nostr as its transport for connecting to self-custodial Lightning nodes. The app pairs with one or more [Lightning.Pub](https://github.com/shocknet/Lightning.Pub) nodes over Nostr via an `nprofile`, then signs payment authorizations end-to-end between the wallet and the node. The team shipped [PR #608](https://github.com/shocknet/wallet2/pull/608) on 2026-04-18 with a channels-dashboard UI pass, landing alongside an admin-invite-link QR flow for new PUB users ([PR #606](https://github.com/shocknet/wallet2/pull/606)) and a readability fix for the metrics dashboard ([PR #607](https://github.com/shocknet/wallet2/pull/607)).

ShockWallet uses [NIP-78](/en/topics/nip-01/) application-specific data events for multi-device wallet state sync, so a user's wallet view stays consistent between a desktop browser and a phone without a centralized sync server. That puts it one layer below [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect): NIP-47 is the interface an app uses to ask an existing wallet to pay, while ShockWallet uses Nostr as the wallet's own account and session transport to the underlying Lightning node. Alongside the wallet, the team is pushing [CLINK](https://github.com/shocknet/CLINK), a Nostr-based session-pairing protocol for wallet-to-app connections, and maintaining a single TypeScript codebase that builds to web, Android, and iOS.

### Nostrability issues migrate to git over Nostr after GitHub censorship

[Nostrability](https://gitworkshop.dev/elsat@habla.news/nostrability/issues), elsat's interoperability tracker for Nostr clients and relays, is moving its issue workflow to git over Nostr after the Nostrability organization was taken down on GitHub with no response from GitHub support for two weeks. The migrated issue tracker now lives on GitWorkshop/ngit, where existing issues have been carried over and future interop reports can stay inside Nostr-native infrastructure.

### nowhere encodes full websites into URL fragments and routes orders through Nostr

[nowhere](https://github.com/5t34k/nowhere) is a new AGPL-3.0 project from [5t34k](https://github.com/5t34k) that serializes an entire site into the URL fragment after `#`, compresses it with a dictionary substitution pass and raw DEFLATE, and base64url-encodes the result. Because HTTP prohibits browsers from sending fragments to servers, the host that delivers the page never sees the content, and the site itself is never stored on a server. The project ships eight site types (event, fundraiser, store, petition, message, drop, art, forum), and each one can be cryptographically signed by its creator and password-encrypted at the URL.

Five of the eight types are purely static, but store, forum, and petition need live communication for orders, posts, and signatures, and that traffic runs through Nostr relays using ephemeral keys with [NIP-44](/en/topics/nip-44/) encryption, so the relay stores events it cannot read from throwaway keys it cannot trace. A single-item store fits in roughly 120 characters, which means a nowhere link works as a printable QR code for offline use via the companion [nowhr.xyz](https://nowhr.xyz/install) reader. The repo is a pnpm workspace split into a standalone `codec` package, a Svelte 5 `web` component library with Nostr integration and payment handling, and the `nowhr` app shell at [nowhr.xyz](https://nowhr.xyz/app).

### Small new surfaces: relayk.it and Brainstorm Search

Two small projects worth a mention without a heavy changelog hook. [relayk.it](https://relayk.it), built by [sam](https://nostr.com/sam@relayk.it) from the Soapbox team, is a [Shakespeare](https://shakespeare.diy)-built relay-discovery client that runs entirely in the browser and points users toward active Nostr relays. [Brainstorm Search](https://brainstorm.world) ships as a single-page Nostr search UI focused on surfacing content across the network.

## Protocol and Spec Work

### NIP Updates

Recent proposals and discussions in the [NIPs repository](https://github.com/nostr-protocol/nips):

**Open PRs and Discussions:**

- **[NIP-67](/en/topics/nip-67/): EOSE Completeness Hint** ([PR #2317](https://github.com/nostr-protocol/nips/pull/2317)): Proposes adding an optional third element to the [NIP-01](/en/topics/nip-01/) `EOSE` message so a relay can signal whether it has delivered every stored event matching the filter. Today, `EOSE` marks the boundary between stored and real-time events but carries no information about completeness: a client that asks for 500 events from a relay capped at 300 receives 300 events and an `EOSE`, with no way to distinguish "this is all of it" from "we stopped partway through." The proposal adds the form `["EOSE", "<sub_id>", "finish"]` when the relay has delivered all matches, and leaves the legacy two-element form as an unchanged no-claim case. The design is backwards-compatible, since relays that do not advertise support fall through to today's heuristic, and clients that know their relay supports it can stop paginating as soon as they see the positive signal.

- **NIP-5D: Nostr Applets** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): Proposes a new kind for distributing interactive applets on Nostr. Where [NIP-5A](/en/topics/nip-5a/) covers static websites and the in-progress [NIP-5C](/en/topics/nip-5c/) covers executable WASM scrolls, NIP-5D targets the middle ground of self-contained front-end applets that run in a client's sandboxed iframe or WebView, addressable by Nostr event and updateable through a replaceable tag. Clients gain a way to ship third-party experiences (polls, calculators, mini-games) without each one wiring up a full plugin system. The open PR is actively iterating on the security model for message passing between the applet and host.

- **NIP-29: Subgroups spec** ([PR #2319](https://github.com/nostr-protocol/nips/pull/2319)): Extends [NIP-29](/en/topics/nip-29/) relay-based groups with a subgroup hierarchy so a single group can host multiple parallel channels without spawning independent groups on the same relay. The PR defines a subgroup identifier that piggybacks on the existing `h` tag, specifies how kind `9000`-range moderation events scope to a subgroup, and clarifies how clients should render the hierarchy. The change preserves the single-`h`-tag shape for plain messages so older clients keep working in a subgrouped room.

- **NIP-29: Explicit role permissions on kind 39003** ([PR #2316](https://github.com/nostr-protocol/nips/pull/2316)): Defines an explicit permissions schema on the [NIP-29](/en/topics/nip-29/) kind `39003` role event. Each role becomes a named set of granted operations (invite, add-user, remove-user, edit-metadata, delete-event, add-permission) with an optional time-bound expiry. Two NIP-29 relays running the same group can currently disagree on what a "moderator" can do, and clients have no way to reflect that difference to the user; the schema fixes that.

- **NIP-11: access_control field for gated-relay discovery** ([PR #2318](https://github.com/nostr-protocol/nips/pull/2318)): Adds a new optional `access_control` object to the [NIP-11](/en/topics/nip-11/) relay information document, listing the relay's gating mode (open, invite, payment, allowlist) and any endpoint a client can use to request access. The field is advisory only, and it lets clients and directories filter gated relays out of public-discovery lists and show users upfront why a relay refuses writes.

- **NIP-63a: Minimal Payment Gateway Descriptor** ([PR #2315](https://github.com/nostr-protocol/nips/pull/2315)): Covered in [Newsletter #18](/en/newsletters/2026-04-15-newsletter/#nip-updates). The PR continues to iterate on the kind `10164` payment-gateway-descriptor shape and on the field layout for per-tier subscription rules.

- **NIP-XX: Agent Reputation Attestations (Kind 30085)** ([PR #2320](https://github.com/nostr-protocol/nips/pull/2320)): Proposes a kind `30085` addressable event for signed attestations about autonomous agents and services on Nostr, covering reliability, honest-advertising, and dispute-resolution claims. Each attestation points to a target pubkey, carries a score in a bounded range, and references the evidence event that justifies the score. The motivation is that [NIP-90](/en/topics/nip-90/) Data Vending Machines and other service markets currently lack a standard way for customers to publish verifiable feedback that other customers can filter on.

- **NIP-TPLD: Transient Private Location Data** ([PR #2309](https://github.com/nostr-protocol/nips/pull/2309)): Continues from [Newsletter #18](/en/newsletters/2026-04-15-newsletter/#nip-updates) with further iteration on the kind `20411` ephemeral range, the per-recipient [NIP-44](/en/topics/nip-44/) encryption shape, and the `ttl` tag semantics for relay retention.

- **marmot-ts 0.5.0 release PR** ([PR #70](https://github.com/marmot-protocol/marmot-ts/pull/70)): The pending release PR for `@internet-privacy/marmot-ts@0.5.0` bundles the first planned breaking changes in the TypeScript Marmot client. The release switches `KeyPackageManager` to support both legacy kind `443` and new kind `30443` events, removes the `KeyPackageStore` and group-state storage classes in favor of passing a generic key-value store directly into `KeyPackageManager` and `MarmotGroup`, and moves invite and group management onto `MarmotClient.invites` and `MarmotClient.groups`. Projects embedding marmot-ts directly will need constructor and storage-layer changes before they can pick the release up.

## NIP Deep Dive: NIP-72 (Moderated Communities)

[NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md) defines a model for topic-based communities on Nostr in which moderators curate a read view over otherwise-unrestricted writes. Unlike [NIP-29](/en/topics/nip-29/) relay-based groups, where the relay is the authority for both membership and moderation, a NIP-72 community lives in plain Nostr events and every relay that carries the relevant kinds can serve it. Anyone can post to a community, and only posts that a recognized moderator has approved appear in the community feed.

A community is defined by a kind `34550` addressable event published by its creator. The event is a `d`-tagged replaceable event, so the creator can edit the community's metadata over time without losing the identity. The `d` tag is the community's stable slug, the `name`, `description`, `image`, and `rules` tags carry display metadata, and a series of `p` tags with a `"moderator"` marker list the pubkeys whose approvals count. Optional `relay` tags with an `author`, `requests`, or `approvals` marker hint at where each kind of event should be published and fetched from:

```json
{
  "id": "f1e2d3c4b5a69788f1e2d3c4b5a69788f1e2d3c4b5a69788f1e2d3c4b5a69788",
  "pubkey": "c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2",
  "created_at": 1745280000,
  "kind": 34550,
  "tags": [
    ["d", "bitcoin-devs"],
    ["name", "Bitcoin Devs"],
    ["description", "A moderated community for Bitcoin protocol discussion."],
    ["image", "https://example.com/bitcoin-devs.png"],
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876", "", "moderator"],
    ["p", "a1b2c3d4e5f6a7b8c9d0a1b2c3d4e5f6a7b8c9d0a1b2c3d4e5f6a7b8c9d0a1b2", "", "moderator"],
    ["relay", "wss://relay.example.com", "author"],
    ["relay", "wss://relay.moderator.com", "approvals"]
  ],
  "content": "",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

A user submits a post by publishing any ordinary event (a kind `1` note, a kind `30023` long-form article, a kind `31922` calendar event, and so on) and adding an `a` tag whose value is the community's coordinate `34550:<creator_pubkey>:<slug>`. The post is a fully valid Nostr event on its own, and clients without NIP-72 support simply see a note addressed to a community-shaped coordinate. Community-aware clients filter their community view to posts that a recognized moderator has approved.

Approval is a separate kind `4549` event published by a moderator. The approval references the submission by `e` tag, the submitter by `p` tag, and the community by `a` tag, and embeds the stringified submission event in the `content` field as a cached copy. That embedded copy keeps the approved post renderable even if the original author later deletes the source event.

```json
{
  "id": "a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1745283600,
  "kind": 4549,
  "tags": [
    ["a", "34550:c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2:bitcoin-devs"],
    ["e", "b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4"],
    ["p", "e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5"],
    ["k", "1"]
  ],
  "content": "{\"id\":\"b3c4d5e6...\",\"pubkey\":\"e4f5a6b7...\",\"kind\":1,\"content\":\"Question about sighash flags\",\"tags\":[[\"a\",\"34550:c3d2e1f0...:bitcoin-devs\"]],\"created_at\":1745283500,\"sig\":\"...\"}",
  "sig": "bbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aa"
}
```

The approval model has three useful properties. Moderation decisions are transparent: every approval is a signed Nostr event that anyone can fetch, so a skeptical user can audit which moderator approved which post and at what time. Moderation is non-exclusive: the same submission can be approved by multiple communities, and a post that one community rejects may be approved by another, because the `a` tag is just an address on a curated view. Moderation is reversible at the read layer: if a community deletes a moderator from its kind `34550` event, prior approvals from that moderator stop counting in clients that respect the current moderator list.

The read side is where clients differ. Most community-aware clients render the feed by filtering for kind `4549` events tagged with the community's coordinate, deduplicating by the underlying event ID, and then rendering the embedded post. Some clients also fetch the submission events directly and use approvals only as a whitelist, which makes sense when approvals are incomplete or stale. A few clients (including [noStrudel](https://github.com/hzrd149/nostrudel) and, as of [PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) this week, [Amethyst](https://github.com/vitorpamplona/amethyst)) expose the pending submission queue to moderators as a separate view.

Compared to [NIP-29](/en/topics/nip-29/) relay-based groups, the tradeoff is clear. NIP-72 communities work over any relay network with no special support, so the write path is portable, and moderation is visible and forkable. A submission is public the moment it is published, and unapproved posts are hidden at the client-render layer. For spaces where spam must stay off the wire entirely, NIP-29 is the better fit. For public topic communities where approvals function more like a curated front page than a gate, NIP-72 fits better.

## NIP Deep Dive: NIP-57 (Zaps)

[NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md) defines zaps, a way to attach Lightning payments to Nostr identities and events and to publish a verifiable receipt of payment back onto relays. A zap proves that a specific sender paid a specific amount to a specific recipient for a specific target, and the proof is readable by any Nostr client without trusting the sender's word. The spec reaches across three systems (LNURL, Lightning, and Nostr) and pins down how each of them must cooperate.

The flow has four actors. A sender's client discovers the recipient's LNURL endpoint from either the recipient's kind `0` profile metadata (`lud06` or `lud16` field) or a `zap` tag on the event being zapped. That client then signs a kind `9734` zap request event describing the intended payment and posts it to the recipient's LNURL callback, not to relays. On the other side, the recipient's LNURL server validates the request, returns a Lightning invoice whose description hash commits to the stringified request event, and, once the sender pays, publishes a kind `9735` zap receipt to the relay set the sender requested.

A zap request (kind `9734`) is a signed event that declares the payment's intent. The critical fields are a `p` tag with the recipient pubkey, an optional `e` or `a` tag identifying the event or addressable content being zapped, an `amount` tag in millisats, and a `relays` tag listing where the receipt should be published. The `content` carries an optional sender-supplied message that accompanies the zap. A `k` tag records the target kind so a consumer can filter zaps by the type of content they fund:

```json
{
  "id": "c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2",
  "pubkey": "a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876",
  "created_at": 1745280000,
  "kind": 9734,
  "tags": [
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876"],
    ["e", "b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4"],
    ["amount", "21000"],
    ["relays", "wss://relay.damus.io", "wss://nos.lol", "wss://relay.nostr.band"],
    ["k", "1"]
  ],
  "content": "great post",
  "sig": "ccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbcc"
}
```

The zap receipt (kind `9735`) is published by the recipient's wallet server after payment confirmation. It is not signed by the sender; it is signed by the wallet server using the `nostrPubkey` that the recipient advertised in their LNURL response. A valid receipt carries the stringified zap request in the `description` tag, the paid invoice in the `bolt11` tag, and a `preimage` tag proving the invoice was settled:

```json
{
  "id": "d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3",
  "pubkey": "e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0",
  "created_at": 1745280060,
  "kind": 9735,
  "tags": [
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876"],
    ["P", "a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876"],
    ["e", "b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4"],
    ["bolt11", "lnbc210n1pj...bolt11invoicestring"],
    ["description", "{\"id\":\"c1d2e3f4...\",\"pubkey\":\"a5b4c3d2...\",\"kind\":9734,\"content\":\"great post\",\"tags\":[...]}"],
    ["preimage", "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"]
  ],
  "content": "",
  "sig": "ddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccdd"
}
```

The validation rule is where NIP-57 earns its trust guarantees. A client that displays a kind `9735` receipt as a zap should verify four things: the receipt's signature matches the `nostrPubkey` advertised in the recipient's LNURL response, the `bolt11` invoice amount matches the `amount` tag in the embedded zap request, the invoice's description hash commits to the stringified zap request, and the `preimage` hashes to the invoice's `payment_hash`. A receipt that fails any of these checks is only a claim of payment, not proof of it. Clients that render tallied zap counts without performing these checks are trivially spoofable by an attacker who publishes forged kind `9735` events.

Private zaps add a confidentiality layer on top. A sender can encrypt the zap request's `content` for the recipient and include an `anon` tag on the outer zap request, so the relay network sees the payment target but cannot read the attached note. Some clients go one step further and generate a fresh ephemeral keypair for the zap request itself, so the receipt still proves a payment happened but the recipient cannot link the zap back to the sender's long-lived pubkey. That "anonymous zap" pattern is stronger than a plain private zap, where the message is hidden but the sender key can still be visible in the request path.

NIP-57 also underpins the zap-goal system specified in [NIP-75](/en/topics/nip-75/). A goal is a kind `9041` event that declares a target amount and a relay set where receipts count, and any zap receipt bound to the goal's event ID contributes to its progress. Clients tally goal progress by summing the validated `bolt11` amounts of matched kind `9735` events. [Amethyst](https://github.com/vitorpamplona/amethyst)'s [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) this week wires goals into the [NIP-53](/en/topics/nip-53/) Live Activities screen and renders a top-zappers leaderboard from the same receipts.

Zap splits are defined in an appendix to the NIP. A recipient can publish a kind `0` profile with multiple `zap` tags, each carrying a weight, so a single zap payment is divided among several pubkeys according to the published weights. Content creators, collaborators, and platform fee recipients can all be paid atomically from a single sender-signed zap request. Several clients, including [Amethyst](https://github.com/vitorpamplona/amethyst), [Damus](https://github.com/damus-io/damus), and [noStrudel](https://github.com/hzrd149/nostrudel), implement split-paying end-to-end.

---

That's it for this week. If you're building something or have news to share, DM us on Nostr or find us at [nostrcompass.org](https://nostrcompass.org).
