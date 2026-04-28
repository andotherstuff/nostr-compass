---
title: 'Nostr Compass #20'
date: 2026-04-29
publishDate: 2026-04-29
draft: false
type: newsletters
description: 'GitWorkshop ships an in-browser PR merge button, repository following, a bandwidth-efficient git explorer, and inline code review comments for git-over-Nostr; Routstrd launches a local inference router using Nostr provider announcements and Cashu payments; releases include ngit v2.4.2, Wisp v1.0.0, grain v0.5.2 and v0.5.3, Mostro Core v0.10.0, Mostro Mobile v1.2.5, marmot-ts v0.5.0, CruxCoach v0.1.3, Meiso v1.3.0, NoorNote, Nostria, Nostr Calendar, nos2x-fox, applesauce, and nostr-double-ratchet; unreleased work covers Amethyst Nests, nostream NIP-65/NWC, FIPS Nostr-based udp:nat bootstrap, strfry observability, Sprout owner attestations, and Zap Cooking recipe packs; newly tracked projects include Nostrord, Clave, Treasures, smesh, Surveil, Fundstr, Nod City, deploy-nsite-to-pages, and null--nostr; the month-end retrospective covers Nostr Aprils from 2021 through 2026.'
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** [GitWorkshop](#gitworkshop-ships-in-browser-pr-merge-repository-following-and-a-bandwidth-efficient-git-explorer) turns git-over-Nostr into a fuller code-review surface with an in-browser PR merge button, Stars and repository following, a bandwidth-efficient git explorer, kind `1111` inline review comments, and encrypted multi-device notification state. [Routstrd](#routstrd-launches-a-local-router-for-inference-over-nostr) launches a local daemon that discovers model providers via Nostr kind `38421` announcements and pays them with Cashu. Tagged releases include [ngit v2.4.2](#ngit-v242-fixes-grasp-relay-detection-for-pr-submissions), [Wisp v1.0.0](#wisp-v100-graduates-from-beta), [grain v0.5.2 and v0.5.3](#grain-v052-fixes-websocket-lockup-v053-continues-polish), [Mostro Core v0.10.0 and Mostro Mobile v1.2.5](#mostro-core-v0100-and-mostro-mobile-v125-adopt-nip-59-dual-key-gift-wrap), [marmot-ts v0.5.0](#marmot-ts-v050-ships-addressable-keypackages), [CruxCoach v0.1.3](#cruxcoach-v013-ships-encrypted-climbing-data-backup-with-nostr-and-blossom), [Meiso v1.3.0](#meiso-v130-adds-subtasks-blossom-attachments-and-nip-89-tagging), NoorNote, Nostria, Nostr Calendar, nos2x-fox, applesauce, nostr-double-ratchet, and more. Unreleased changes cover [Amethyst Nests](#amethyst-advances-nests-audio-rooms-with-moq-interop-testing), [nostream NIP-65 and NWC](#nostream-adds-nip-65-relay-list-support-and-nwc-payments), [FIPS Nostr-based udp:nat bootstrap](#fips-adds-nostr-based-udpnat-bootstrap), [strfry observability](#strfry-adds-per-connection-observability), [Sprout owner attestations](#sprout-adds-owner-attestation-and-multi-workspace-support), and [Zap Cooking recipe packs](#zap-cooking-adds-recipe-packs-delete-requests-and-bunker-login). Newly tracked projects include [Nostrord](#nostrord-a-nip-29-client-built-with-kotlin-multiplatform-and-wasm), [Clave](#clave-brings-nip-46-remote-signing-to-ios-via-apns), [Treasures](#treasures-decentralized-geocaching-on-nostr), [smesh](#smesh-v051-self-hosted-nostr-relay-client-and-signer-in-one-stack), [Surveil](#surveil-a-magic-the-gathering-deck-builder-on-nostr), Fundstr, Nod City, deploy-nsite-to-pages, and null--nostr. Since this is the last Compass of April, the issue closes with [Six Nostr Aprils](#six-nostr-aprils), a retrospective from 2021 through 2026.

## Lead stories

### GitWorkshop ships in-browser PR merge, repository following, and a bandwidth-efficient git explorer

[GitWorkshop](https://gitworkshop.dev), Dan Conway's web-based collaboration layer for [NIP-34](/en/topics/nip-34/) git-over-Nostr, shipped a major release this week that brings the workflow much closer to what developers expect from GitHub or GitLab, while keeping comments, repository lists, and notifications inside signed Nostr events.

The headline addition is a long-awaited in-browser PR merge button for repositories using GRASP relays. The release also adds Stars and repository following built on reactions and [NIP-51](/en/topics/nip-51/) lists, with pinned repository sets published as kind `10617` events that point at kind `30617` repo announcements via ordered `a` tags. Profile pages can now feature a portable list of repositories.

A bandwidth-efficient git explorer replaces the previous in-browser shallow clone. The new explorer leans on the underlying git client/server protocol that GRASP builds on, so it can handle large repositories without forcing the browser to fetch a full pack. Search now covers usernames and repository metadata, powered by [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md) and an `ngit-indexer` relay implementation that discovers and syncs repository announcements across the network. An in-browser repository creation workflow rounds out the discovery and onboarding path.

Review tooling is rebuilt around a Files Changed tab, a per-patch diff viewer, and a set of experimental new primitives. Inline code review comments use kind `1111`, built on [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md): each comment points to a file path (`f` tag), a commit SHA (`c` tag), and a selected line range (`line` tag) so a client can render the comment at the correct position in a diff. A second tier of experimental primitives is permissioned by author and repo maintainers and uses [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) labels: rename an Issue or PR subject after submission, add hashtags after submission, pin a version-controlled CoverNote to the top of a PR or Issue for an editable summary, and mark inline code discussion subthreads as resolved. Verdict events and `suggestion` blocks remain in draft and have not yet shipped.

Notification state across devices is also synced through Nostr, but with a privacy-preserving twist. GitWorkshop generates a dedicated notifications keypair, encrypts that nsec, and stores it inside a kind `30078` event. The notifications nsec then signs the actual notification state events. The indirection prevents the user's main signer from being spammed with frequent encrypt and decrypt requests for every read or archive action, and it stops outside observers from easily seeing when a user touches their notification state. A user can sync read and archive state across devices; relays only see encrypted blobs.

### Routstrd launches a local router for inference over Nostr

[Routstrd](https://github.com/routstr/routstrd) is a new TypeScript daemon that gives local tools an OpenAI-compatible endpoint and routes each request to a competing [Routstr](https://routstr.com) provider. The daemon discovers providers through Nostr kind `38421` announcements defined in Routstr's RIP-02 spec. It then scores providers by price, trust, and recent performance under RIP-06 and sends each request to the current best option.

Payment runs through a local Cashu wallet managed by cocod and funded with Lightning. That gives the client a sats-denominated settlement path while keeping provider discovery public and permissionless through Nostr relays. If a provider fails during a session, Routstrd can fall back to the next-ranked node. The install path is `bun install -g routstrd`, followed by `routstrd onboard` for wallet and relay setup.

The broader [Routstr org](https://github.com/routstr) maintains the daemon, the Python node software (`routstr-core`), a chat UI, and protocol specs. For users, the local port becomes the stable interface: existing OpenAI-compatible tools point at Routstrd, while the daemon handles provider discovery, routing, and payment.

## Tagged releases

### ngit v2.4.2 fixes GRASP server detection for PR submissions

[ngit](https://codeberg.org/DanConwayDev/ngit-cli) shipped [v2.4.2](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.2) with a fix for repository GRASP server detection, keeping PR submission on the happy path when a proposal uses the PR kind. Note that ngit currently defaults to the `Patch` kind for most changes unless they are large; the maintainer is working toward changing the default. [v2.4.1](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.1), shipped earlier in the week, fixed `fatal` errors during clone and fetch when an open PR's git data was unavailable on the repository's specified git servers.

### Wisp v1.0.0 graduates from beta

[Wisp](https://github.com/barrydeen/wisp), a Kotlin and Jetpack Compose Android client focused on relay routing, privacy, and a small native UI, shipped [v1.0.0](https://github.com/barrydeen/wisp/releases/tag/v1.0.0) and followed with [v1.0.2](https://github.com/barrydeen/wisp/releases/tag/v1.0.2). The 1.0.0 milestone gathers the Normie Mode fiat-denomination toggle, the For You feed, [NIP-29](/en/topics/nip-29/) relay-based group configuration, and [NIP-65](/en/topics/nip-65/) relay-list broadcasting covered in [Newsletter #19](/en/newsletters/2026-04-22-newsletter/#wisp-v0180-beta-adds-normie-mode-for-you-feed-and-nip-29-group-config). v1.0.2 adds Android 15 16 KB page-size support, a QR scan tab in the drawer sheet, a download button for inline video controls, and notification-list performance fixes.

### grain v0.5.2 fixes WebSocket lockup, v0.5.3 continues polish

[grain](https://github.com/0ceanSlim/grain), the Go relay from 0ceanSlim, cut [v0.5.2](https://github.com/0ceanSlim/grain/releases/tag/v0.5.2) as a critical hotfix for a WebSocket lockup introduced in v0.5.0, then followed with [v0.5.3](https://github.com/0ceanSlim/grain/releases/tag/v0.5.3). The lockup caused connections to hang under some filter and WebSocket paths, so operators on v0.5.1 or v0.5.0 should upgrade. grain tracks all major Nostr event categories, exposes NIP-11 relay information, supports whitelist/blacklist access control, per-kind rate limits, a web dashboard, and a Go client library added in the v0.5.x line.

### Mostro Core v0.10.0 and Mostro Mobile v1.2.5 adopt NIP-59 dual-key gift wrap

[Mostro Core v0.10.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.10.0) adds the new [NIP-59](/en/topics/nip-59/) gift-wrap module with split identity and trade keys. Earlier transport code used a single identity key for both trade identity and gift wrapping. v0.10.0 separates the stable trade identity from the ephemeral wrapping key, so each trade can use a fresh transport key while preserving the identity needed for the trade protocol. Daemon integration lands through [Mostro PR #718](https://github.com/MostroP2P/mostro/pull/718), and [mostro-cli PR #165](https://github.com/MostroP2P/mostro-cli/pull/165) brings the same migration to the command-line client.

[Mostro Mobile v1.2.5](https://github.com/MostroP2P/mobile/releases/tag/v1.2.5) ships alongside the protocol work. [PR #581](https://github.com/MostroP2P/mobile/pull/581) lets takers filter offers by the maker's account age, giving users a way to avoid newly created maker accounts in the order book. [PR #580](https://github.com/MostroP2P/mobile/pull/580) fixes role labels on canceled order details, and [PR #576](https://github.com/MostroP2P/mobile/pull/576) cleans up cooperative-cancellation buttons.

### marmot-ts v0.5.0 ships addressable KeyPackages

[marmot-ts](https://github.com/marmot-protocol/marmot-ts) cut [@internet-privacy/marmot-ts@0.5.0](https://github.com/marmot-protocol/marmot-ts/releases/tag/%40internet-privacy%2Fmarmot-ts%400.5.0), the first planned breaking-change release for the TypeScript [Marmot](/en/topics/marmot/) client. [PR #68](https://github.com/marmot-protocol/marmot-ts/pull/68) adds addressable KeyPackage support: `KeyPackageManager` can now handle both legacy kind `443` and new kind `30443` KeyPackage events. The release removes `KeyPackageStore` and the group-state storage classes, replacing them with generic key-value stores passed into `KeyPackageManager` and `MarmotGroup`. It also moves invite and group management onto `MarmotClient.invites` and `MarmotClient.groups`, so direct embedders need constructor and storage changes before upgrading.

### CruxCoach v0.1.3 ships encrypted climbing data backup with Nostr and Blossom

[CruxCoach](https://codeberg.org/CruxCoach/CruxCoach) is a new open-source Android app for Kilter Board climbers. The Kilter Board is an interactive training wall whose holds light up over Bluetooth to display routes. The app launched April 14 and reached [v0.1.3](https://codeberg.org/CruxCoach/CruxCoach/releases/tag/v0.1.3) on April 26.

v0.1.3 adds opt-in encrypted cloud backup. A user's CruxCoach account is a Nostr keypair, and the private key doubles as the input to the local backup encryption key. The app encrypts climbing data on-device and mirrors the ciphertext to Blossom storage servers (`blossom.primal.net` and `nostr.download`). Delete-remote actions call the Blossom cleanup path. Beyond backup, CruxCoach uses [NIP-46](/en/topics/nip-46/) remote signing for Amber support, [NIP-17](/en/topics/nip-17/) private DMs for in-app developer contact, [NIP-65](/en/topics/nip-65/) relay lists for relay discovery, and Vitor Pamplona's [Quartz](https://github.com/vitorpamplona/quartz) library for Nostr plumbing. Users can install it through Zapstore or direct Codeberg APKs.

### Meiso v1.3.0 adds subtasks, Blossom attachments, and NIP-89 tagging

[Meiso](https://github.com/higedamc/meiso) is a minimalist Flutter task manager for Android that stores tasks as [NIP-44](/en/topics/nip-44/) encrypted kind `30078` application data on Nostr relays. [v1.3.0](https://github.com/higedamc/meiso/releases/tag/v1.3.0), released April 6, adds subtasks with parent/child relationships, task links for blocks/blocked-by/related-to/duplicate-of, image attachments through Blossom and [NIP-96](/en/topics/nip-96/) HTTP file upload endpoints, a [NIP-89](https://github.com/nostr-protocol/nips/blob/master/89.md) recommended-application `client` tag on published events, and a Go command-line sync tool. v1.3.0 also fixes cold-start relay behavior and Amber client reuse.

### NoorNote, Nostria, Nostr Calendar, nos2x-fox, and library releases

[NoorNote](https://github.com/77elements/noornote) published [v0.8.7](https://github.com/77elements/noornote/releases/tag/v0.8.7), [v0.8.8](https://github.com/77elements/noornote/releases/tag/v0.8.8), and [v0.8.9](https://github.com/77elements/noornote/releases/tag/v0.8.9). Those releases fix image and video click handling in quoted reposts, add lightbox support for long-form article images, and fix the blank desktop startup screen. [Nostria](https://github.com/nostria-app/nostria) cut [v3.1.29](https://github.com/nostria-app/nostria/releases/tag/v3.1.29), [v3.1.30](https://github.com/nostria-app/nostria/releases/tag/v3.1.30), and [v3.1.31](https://github.com/nostria-app/nostria/releases/tag/v3.1.31), adding article-editor image compression, a wallet USD toggle, promotional-card controls, PDF support, and mobile layout polish.

[Nostr Calendar v1.4.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.4.1) decouples calendar event publishing from calendar-list management and fixes invitation tracking. [nos2x-fox v1.19.0](https://github.com/diegogurpegui/nos2x-fox/releases/tag/v1.19.0) adds custom authorization timeframes for Firefox NIP-07 browser-signing grants. [nostr-double-ratchet v0.0.97](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.97) ships new binaries. [nostr-wot-sdk 0.9.0](https://github.com/nostr-wot/nostr-wot-sdk/releases/tag/nostr-wot-sdk%400.9.0) mounts `NostrSessionProvider` by default, and [nostr-tools PR #535](https://github.com/nbd-wtf/nostr-tools/pull/535) adds multi-relay parsing support for NIP-47 wallet-connect strings.

Late in the week, [Amber v6.1.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre1) shipped a pre-release with a better connect-new-app layout, signer-dialog fixes, improved notification permission handling, and refactored account selection. [nostr-vpn v0.3.14](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.14) cut a fresh build with macOS Apple Silicon, Linux, and Windows artifacts. [Bitcredit Core v0.5.7-hotfix-1 and v0.5.8](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.8) shipped back-to-back fixes for an orphaned-block validation issue. [Surveil v0.1.6](https://gitlab.com/chad.curtis/surveil/-/tags/v0.1.6) brought mobile UI polish and an overhauled About page; the project itself is introduced [below](#surveil-a-magic-the-gathering-deck-builder-on-nostr).

### applesauce 6.0.0 removes legacy event factories and adds Blossom URI parsing

[applesauce](https://github.com/hzrd149/applesauce), hzrd149's TypeScript Nostr toolkit, shipped a 6.0.0 release train across the monorepo. [applesauce-core@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%406.0.0) removes the legacy `EventFactory` class and old `buildEvent`, `modifyEvent`, and `createEvent` helpers, pushing callers to the newer factory classes in `applesauce-core/factories` and `applesauce-common`. It also adds IP address and localhost handling to link parsing, BUD-10 Blossom URI regular expressions, and new observable helpers such as `timeoutWithIgnore`, `combineLatestBy`, `combineLatestByIndex`, and `combineLatestByKey`.

Package-level releases fill out the Nostr-specific pieces. [applesauce-content@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-content%406.0.0) adds BUD-10 Blossom URI nodes for text and Markdown, giving renderers a first-class way to parse Blossom references in content. [applesauce-actions@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-actions%406.0.0) adds base factory classes for NIP-51 lists covering relays, users, and items, making list construction less ad hoc. [applesauce-wallet-connect@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-wallet-connect%406.0.0) exposes `WalletConnect.connectURI`, so apps can access an existing NIP-47 wallet-connect URI directly.

## Unreleased changes

### Amethyst advances Nests audio rooms with MoQ interop testing

[Amethyst](https://github.com/vitorpamplona/amethyst) merged several Nests-focused PRs this week, building on last week's [Media over QUIC](https://datatracker.ietf.org/group/moq/about/) audio-room stack. [PR #2622](https://github.com/vitorpamplona/amethyst/pull/2622) adds a cross-client interop harness that exercises the Amethyst MoQ client against the reference web implementation. The goal is to catch Android/browser wire-level divergence before users hit it. [PR #2625](https://github.com/vitorpamplona/amethyst/pull/2625) improves picture-in-picture speaker focus and connection status, while [PR #2620](https://github.com/vitorpamplona/amethyst/pull/2620) clarifies avatars, mute state, and speaking state in the participant grid. Late in the week, [PR #2634](https://github.com/vitorpamplona/amethyst/pull/2634) fixes IME padding and window insets in the full-screen Nest view and [PR #2635](https://github.com/vitorpamplona/amethyst/pull/2635) adds presence-based freshness filtering to the Nests feed. Separately, [PR #2627](https://github.com/vitorpamplona/amethyst/pull/2627) removes Amethyst's custom C secp256k1 implementation and migrates to `libschnorr256k1`.

### nostream adds NIP-65 relay list support and NWC payments

[nostream](https://github.com/Cameri/nostream) merged three notable PRs after last week's 53-PR relay sprint. [NIP-65](/en/topics/nip-65/) relay-list metadata support lands in [PR #585](https://github.com/Cameri/nostream/pull/585), so the relay can index and serve kind `10002` relay-list events. A Nostr Wallet Connect payments processor follows in [PR #539](https://github.com/Cameri/nostream/pull/539), adding a pay-to-relay path. Connection cleanup improves in [PR #438](https://github.com/Cameri/nostream/pull/438), which closes a dead-connection bug where sockets with active subscriptions were not being reaped, causing subscription counts to drift on long-running instances.

### FIPS adds Nostr-based udp:nat bootstrap

[FIPS](https://github.com/jmcorgan/fips), the Free Internetworking Peering System previously covered in [Newsletter #6](/en/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking) and [Newsletter #10](/en/newsletters/2026-03-25-newsletter/#fips-v020-ships-tor-transport-reproducible-builds-and-sidecar-examples), merged [PR #53](https://github.com/jmcorgan/fips/pull/53) with Nostr-based `udp:nat` bootstrap. The change lets nodes publish Nostr adverts, exchange encrypted offer/answer signaling, discover public addresses through STUN, perform UDP hole punching, and hand the punched socket into the normal FIPS transport stack. The implementation binds signal payload identities to the actual Nostr sender, queries configured DM and advert relays for inbox lookup, and rolls back failed adopted-traversal handoffs so orphaned UDP transports do not remain live. This is the Nostr announcement and NAT traversal work to track in the canonical repo, `jmcorgan/fips`.

### strfry adds per-connection observability

[strfry](https://github.com/hoytech/strfry) merged [PR #214](https://github.com/hoytech/strfry/pull/214), adding per-connection observability and connection-level metrics exportable through Prometheus. [PR #204](https://github.com/hoytech/strfry/pull/204) normalizes Prometheus labels, and [PR #215](https://github.com/hoytech/strfry/pull/215) adds a Community Integrations section to the docs covering Namecoin identity projects built on top of strfry.

### Sprout adds Owner Attestation and multi-workspace support

[Sprout](https://github.com/block/sprout), Block's Nostr client, merged [PR #406](https://github.com/block/sprout/pull/406) implementing NIP-OA (Owner Attestation). The feature gives an autonomous agent a cryptographic proof that a specific human pubkey authorized its actions. [PR #409](https://github.com/block/sprout/pull/409) adds multi-workspace support to the desktop app, [PR #411](https://github.com/block/sprout/pull/411) adds `#channel` autocomplete to mobile compose, and [PR #410](https://github.com/block/sprout/pull/410) closes a race window that could drop active channel messages. [PR #413](https://github.com/block/sprout/pull/413) introduces NIP-RS for cross-device read state sync, and follow-up [PR #420](https://github.com/block/sprout/pull/420) and [PR #422](https://github.com/block/sprout/pull/422) wire that read state into the mobile unread badges.

### Zap Cooking adds recipe packs, delete requests, and bunker login

[Zap Cooking](https://github.com/zapcooking/frontend) merged a productive week of recipe-publishing work. [NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md) deletion requests for a user's own Recipe Packs land in [PR #367](https://github.com/zapcooking/frontend/pull/367). Publication reliability improves through [PR #366](https://github.com/zapcooking/frontend/pull/366), which forces every new recipe onto the garden relay and adds a retry queue for the shared recipe set. One-click authored pack publishing lands in [PR #365](https://github.com/zapcooking/frontend/pull/365), and [PR #331](https://github.com/zapcooking/frontend/pull/331) adds [NIP-46](/en/topics/nip-46/) bunker login support.

### Whitenoise-rs encrypts its local database

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) merged [PR #758](https://github.com/marmot-protocol/whitenoise-rs/pull/758), adding SQLCipher encryption for the on-disk Whitenoise database. That closes a long-standing at-rest security gap for the Marmot daemon stack. [PR #775](https://github.com/marmot-protocol/whitenoise-rs/pull/775) exposes group required capabilities, [PR #772](https://github.com/marmot-protocol/whitenoise-rs/pull/772) migrates group media operations to session-owned `MediaOps`, and [PR #773](https://github.com/marmot-protocol/whitenoise-rs/pull/773) extracts a `SharedServices` holder as part of the session-ops refactor. On the mobile side, [whitenoise PR #577](https://github.com/marmot-protocol/whitenoise/pull/577) enables boot auto-restart for the Android foreground service, fixing the case where the daemon would not come back after a device reboot.

## Newly tracked and discovered

### Nostrord: a NIP-29 client built with Kotlin Multiplatform and WASM

[Nostrord](https://github.com/nostrord/nostrord) is a new [NIP-29](/en/topics/nip-29/) group-chat client targeting the Discord-replacement use case. Groups live on Nostr relays with relay-enforced membership, roles, moderation, and access control, so group state is hosted by the selected NIP-29 relay. The client developer does not control a separate application database for those groups. The web app runs at [web.nostrord.com](https://web.nostrord.com) and is built with Kotlin Multiplatform compiling to WebAssembly, with native Android, iOS, and desktop builds in development. Nostrord is an [OpenSats](https://opensats.org) grant recipient and interoperates with the same NIP-29 relays used by Flotilla, Chachi, and 0xChat.

### Clave brings NIP-46 remote signing to iOS via APNs

[Clave](https://github.com/DocNR/clave) is an iOS remote signer in beta that signs Nostr events when the app is not open. The private key stays in the iPhone Keychain. When a client sends a [NIP-46](/en/topics/nip-46/) remote-signing request, a server-side proxy delivers an Apple Push Notification, waking a Notification Service Extension for up to 30 seconds. That extension decrypts the request with [NIP-44](/en/topics/nip-44/) encryption, signs with the Keychain key, and publishes the response. Device token registration uses [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) HTTP Auth to prevent token hijacking. Clave supports `bunker://` and `nostrconnect://` pairing, per-client trust levels, per-kind overrides, and has been tested with Nostur and noStrudel.

### Treasures: decentralized geocaching on Nostr

[Treasures](https://gitlab.com/chad.curtis/treasures) is a geocaching platform where caches and finds are signed Nostr events. Cache creators publish kind `37516` addressable events with GPS coordinates. Finders log discovery by scanning a QR code attached to the physical cache; the code encodes the creator pubkey, the cache `d` tag, and a verification private key used as proof of the physical visit. [NIP-57](/en/topics/nip-57/) zaps can flow from finders to cache creators, and the live app is at [treasures.to](https://treasures.to).

### smesh v0.5.1: self-hosted Nostr relay, client, and signer in one stack

[smesh](https://git.smesh.lol/smesh/smesh) is a self-hosted Nostr stack written in Moxie, a custom language derived from Go and TinyGo by mleku. The stack ships a native relay binary with HTTP, WebSocket, AUTH, search, and Blossom support; `sm3sh`, a web client compiled to ES modules; and a browser signer extension with NIP-07 browser signing plus NIP-04 and NIP-44 encryption support. Recent work includes MLS (RFC 9420) group messaging in v0.5.0, negentropy set reconciliation for relay sync, and a Web of Trust graph engine. The code lives on mleku's self-hosted forge at `git.smesh.lol`, built with his own `git-web` tool. The related [gitea-nostr-auth](https://git.smesh.lol/smesh/gitea-nostr-auth) repo is an OAuth2/OIDC bridge for Gitea: users authenticate with a NIP-07 browser signer, the bridge discovers relays through NIP-65, and Gitea receives standard OIDC identity claims.

### Surveil: a Magic: The Gathering deck builder on Nostr

[Surveil](https://gitlab.com/chad.curtis/surveil) is a Nostr client for Magic: The Gathering players that lets users search cards, build decks, scan paper cards on Android with on-device ML Kit OCR, and share decks across the network. Decks are published as kind `37381` addressable events, and the deck event spec is documented in the project's `NIP.md`. The social layer is built from standard Nostr primitives: NIP-22 (kind `1111`) threaded comments scoped to each deck, NIP-25 (kind `7`) reactions, [NIP-78](https://github.com/nostr-protocol/nips/blob/master/78.md) (kind `30078`) profile data for player homes, kind `3` follow feeds, and forks that carry an `a` tag back to the original deck. [v0.1.6](https://gitlab.com/chad.curtis/surveil/-/tags/v0.1.6) shipped this week with mobile UI polish, life counter improvements, an overhauled About page, and a relay pill on the deck hero banner. The web app runs anywhere static HTML is served, the Android build ships through [Zapstore](https://zapstore.dev), and kind `37381` events are also indexed natively by [Ditto](https://about.ditto.pub/reference) as Magic decks. The repo is on GitLab at [chad.curtis/surveil](https://gitlab.com/chad.curtis/surveil).

### Smaller additions: Fundstr, Nod City, deploy-nsite-to-pages, and null--nostr

[Fundstr](https://github.com/ritty65/Fundstr) is a creator-funding platform on Nostr using Cashu ecash for one-time and recurring pledges, with creator tier definitions and Nostr DMs. [Nod City](https://nod.city) is a Bitcoin-service review site where reviews are signed Nostr events and reviewers can receive zaps; no public source repo was found. [deploy-nsite-to-pages](https://github.com/Origami74/deploy-nsite-to-pages) is a GitHub Action that mirrors an nsite to GitHub Pages by using `nsyte download`, supporting root kind `15128` and named kind `35128` nsites. [null--nostr](https://github.com/tami1A84/null--nostr), also discovered in this week's NIP-34 data, is the client covered in the recent OpenSats wave as Nurunuru; it supports MLS group messaging, Amber, NIP-50 search, NIP-70 protected posts, ProofMode badges, and Zapstore distribution.

FIPS is not a new project for Compass. It was covered in [Newsletter #6](/en/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking) and [Newsletter #10](/en/newsletters/2026-03-25-newsletter/#fips-v020-ships-tor-transport-reproducible-builds-and-sidecar-examples). The database now points at the correct canonical repo, [jmcorgan/fips](https://github.com/jmcorgan/fips), and this week's NIP-34 discovery also surfaced related git-over-Nostr mirrors such as `fips` and `awesome-fips`.

## Protocol work

### NIP updates

Recent proposals and discussions in the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged this week:**

- **NIP-34 git repositories: remove unused refs tag extension** ([PR #2325](https://github.com/nostr-protocol/nips/pull/2325)): Removes a `refs` tag extension from [NIP-34](/en/topics/nip-34/) that was defined but unused. The cleanup reduces implementation ambiguity for git-over-Nostr tools.

- **NIP-34 git repositories: remove incorrect NIP-09 claim** ([PR #2326](https://github.com/nostr-protocol/nips/pull/2326)): Removes an incorrect claim that [NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md) deletion events can reset repository state. NIP-09 deletion is a client-side event-deletion request, not a repository state machine. The correction prevents NIP-34 implementors from treating deletion hints as authoritative repo resets.

**Open and implementation-driven work:**

- **GitWorkshop kind `1111` inline review comments**: The inline code review comment kind is documented in GitWorkshop's `NIP.md` and is now in active use, but it has not yet been proposed as a formal NIP. Verdict events (kind `7321`) and `suggestion` blocks remain in draft and have not yet shipped. Implementation feedback from GitWorkshop and ngit will determine whether the shapes become a standalone git-review NIP or remain an application convention layered on NIP-34.

- **Nostr mail core and Nostrmon**: Two new custom-NIP drafts circulated this week. [Nostr mail core](https://njump.me/57d11cdf2f9ed73f7f39d6a7a6012ee3d642584ab11887f96a031f7d00fd9697) proposes kind `1301` for RFC 2822 email content, wrapped with NIP-59 for private delivery and bridged to legacy email through NIP-05-resolved bridge pubkeys. [Nostrmon](https://njump.me/5e9a8cee19d464f5f0322518ac9ccaf2399c69da6572346b4fb12d36acb17a27) sketches addressable event kinds for regions, maps, creatures, NPCs, player saves, and items. Both remain custom drafts, not merged NIPs.

- **NIP-67: EOSE Completeness Hint** ([PR #2317](https://github.com/nostr-protocol/nips/pull/2317)): The proposal continues to iterate on adding a positive completeness marker to `EOSE`, allowing relays to distinguish "stored events fully delivered" from legacy `EOSE` cases where the relay makes no completeness claim.

## Six Nostr aprils

April gives a clean cross-section of Nostr's development path: the protocol document in 2021, early client work in 2022, the post-Damus application wave in 2023, private messaging and git-over-Nostr work in 2024, Blossom and relay-list cleanup in 2025, and adoption-focused client grants in 2026.

### April 2021: the protocol document before the NIPs repo

Fiatjaf published the original Nostr article, ["Notes and Other Stuff Transmitted by Relays"](https://fiatjaf.com/nostr.html), on November 20, 2020. That first text already contained the core shape that still defines the protocol: users sign events with keys, publish them to relays, and read from relays they choose. The [`nostr-protocol/nostr` commit log](https://github.com/nostr-protocol/nostr/commits?since=2021-04-01&until=2021-04-30) shows no commits between April 1 and April 30. Activity sits on either side: March 2021 commits added early "nostwitter" links and a `kind` filter, while May 2021 repurposed NIP-02 and added NIP authorship.

In April 2021, there was no public client market, no visible relay network, and no NIPs repo. The protocol still lived as a small document and a few experiments. Nostr had not yet become a social network or a development platform. It was still a relay/key/event model waiting for its first sustained contributor wave.

### April 2022: NIPs still lived in the main repo

April 2022 was the last month before NIPs moved out of the main `nostr-protocol/nostr` repo. Because the split had not happened yet, the dedicated [`nostr-protocol/nips`](https://github.com/nostr-protocol/nips) repo had no April pull-request history. In the main repo, three April commits landed: ["Update readme to add nip12"](https://github.com/nostr-protocol/nostr/commit/bae286312a233b971bee5429adda7aff41747eb8) on April 8 by goswami1999, ["add kinds list"](https://github.com/nostr-protocol/nostr/commit/4b9e9d123273ba8a5c70d77df46922070c11c11d) on April 25 by jb55, and ["add js formatting to sample code"](https://github.com/nostr-protocol/nostr/commit/759997657f07e0344064228ffe5e93febe85d367) on April 28 by steliosrammos.

Client work was also beginning to take shape. Damus commits from April 2022 added early chatroom behavior, profile handling, and app icons, while nostr-tools was becoming the JavaScript library path for early clients and experiments. On the protocol side, NIP-12 generic tag queries gave tag search a documented place, the kinds list moved Nostr toward a registry model, and better JavaScript examples made the spec easier for client and library authors to implement. On May 1, fiatjaf moved NIPs into the dedicated repo. April 2022 was the last month of the original single-repo era.

### April 2023: post-Damus application expansion

April 2023 arrived three months after Damus launched on the iOS App Store on January 31, 2023, and after Jack Dorsey had posted his Nostr public key. The network had just absorbed its first major public growth wave. Clients such as Damus, Snort, Iris, Coracle, and Amethyst were active, while relay operators were learning what a larger social graph did to bandwidth, spam, search, and moderation assumptions.

April 2023 had one merged NIPs PR: [PR #456](https://github.com/nostr-protocol/nips/pull/456), merged April 17, adding NIP-19 bech32 entity links to NIP-21 URI handling. The surrounding commits show the application pressure behind the protocol work. April 2023 saw work on [NIP-45 COUNT](https://github.com/nostr-protocol/nips/commit/8b39976e78f90fe766ad7149e250777cddacbb5e), event-specific zap markers, [NIP-15 marketplace](https://github.com/nostr-protocol/nips/commit/bf0a0da6a48b96467172414d8e41dc72b0ca379c), NIP-26 delete delegation semantics, NIP-94 file metadata, NIP-47 wallet-connect error handling, and [NIP-30 custom emoji](https://github.com/nostr-protocol/nips/commit/e91ce3409e1ce8267fc07a21784d2538621267c3). The contributor list had widened to include fiatjaf, staab, pablof7z, Semisol, CodyTseng, sethforprivacy, mikedilger, AsaiToshiya, alexgleason, martindsq, frbittencourt, and arkin0x.

Damus, Snort, Iris, Coracle, and Amethyst were no longer demos around a spec; they were production clients dealing with onboarding, feeds, spam, zaps, media, and relay selection. April 2023's protocol work reads like the backlog those clients created: zaps, marketplaces, file metadata, counting, emoji, and identity links all pushed the spec beyond simple notes and follows.

### April 2024: private messaging, git-over-Nostr, and maintainer support

April 2024 had two NIP PR merges. [PR #1167](https://github.com/nostr-protocol/nips/pull/1167), merged April 10, fixed confusing terminology in [NIP-46](/en/topics/nip-46/) remote signing, where clients and signers need exact language for requested and authorized actions. [PR #1108](https://github.com/nostr-protocol/nips/pull/1108), merged April 17, expanded [NIP-34](/en/topics/nip-34/) git repositories with status events, clarifications, optional maintainers, repo identifiers, and discoverability tags. That step made git-over-Nostr more practical for ngit and later GitWorkshop.

[NIP-17](https://github.com/nostr-protocol/nips/commit/df30012430c88d49fb5b124992b04d5c61b6338b), formerly NIP-24, landed on April 24 as sealed gift-wrapped messages for private DMs and small group chats. Client and library work ran alongside: Amethyst, Primal, Gossip, nostr-tools, NDK, and rust-nostr were all active in the same period.

OpenSats also announced long-term support for Nostr developers in April 2024: [PabloF7z](https://opensats.org/blog/pablofz7-receives-lts-grant) on April 9, [Stuart Bowman](https://opensats.org/blog/stuart-bowman-receives-lts-grant) on April 12, and [hzrd149](https://opensats.org/blog/hzrd149-receives-lts-grant) on April 15. Those grants moved funding from isolated project grants toward sustained maintenance of relays, libraries, and client infrastructure.

### April 2025: dense NIP cleanup and Blossom formalization

April 2025 was the densest protocol month in this retrospective, with sixteen merged NIPs PRs. The month began with [PR #1846](https://github.com/nostr-protocol/nips/pull/1846), adding blockchain transactions and addresses to NIP-73, and [PR #1865](https://github.com/nostr-protocol/nips/pull/1865), adding NIP-C0 tags to the standardized tags table. It continued with [PR #1801](https://github.com/nostr-protocol/nips/pull/1801) and [PR #1889](https://github.com/nostr-protocol/nips/pull/1889), both improving kind `10002` relay-list republication guidance, and [PR #1879](https://github.com/nostr-protocol/nips/pull/1879), which shrank and clarified [NIP-65](/en/topics/nip-65/).

[PR #1822](https://github.com/nostr-protocol/nips/pull/1822) added NIP-B7 for Blossom interaction, giving Nostr clients and Blossom servers a canonical coordination layer after more than a year of informal practice. [PR #1051](https://github.com/nostr-protocol/nips/pull/1051) deprecated [NIP-26](https://github.com/nostr-protocol/nips/blob/master/26.md), the delegated event signing spec. NIP-26 had been difficult to implement safely and had become less attractive as NIP-46 and other signer patterns matured.

The rest of the month combined cleanup with application expansion: [PR #1882](https://github.com/nostr-protocol/nips/pull/1882) added privacy policy and terms of service fields to [NIP-11](/en/topics/nip-11/), [PR #1849](https://github.com/nostr-protocol/nips/pull/1849) expanded kind `39701` web bookmarks under NIP-B0, [PR #1891](https://github.com/nostr-protocol/nips/pull/1891) added that bookmark kind to the README, and [PR #1895](https://github.com/nostr-protocol/nips/pull/1895) added NIP-B0 standardized tags. OpenSats announced its [Eleventh Wave of Nostr Grants](https://opensats.org/blog/eleventh-wave-of-nostr-grants) on April 16, funding Swae, HAMSTR, Vertex, Nostr Double Ratchet, and Nostr Game Engine. Primal, Coracle, noStrudel, nostr-tools, NDK, and rust-nostr were also shipping through this period, so the protocol cleanup sat next to active client and library work.

### April 2026: NIP-34 hardening, badges, and adoption-focused grants

April 2026, the month this issue closes, had four merged NIPs PRs. The first was [PR #2276](https://github.com/nostr-protocol/nips/pull/2276), merged April 1, which changed [NIP-58](https://github.com/nostr-protocol/nips/blob/master/58.md) profile badges to kind `10008` and added kind `30008` badge sets, making badge assignment and badge collections more composable. A second git-over-Nostr usability change arrived in [PR #2312](https://github.com/nostr-protocol/nips/pull/2312), merged April 10, adding `nostr://` clone URL semantics to [NIP-34](/en/topics/nip-34/). The April 25 cleanups, [PR #2325](https://github.com/nostr-protocol/nips/pull/2325) and [PR #2326](https://github.com/nostr-protocol/nips/pull/2326), removed unused and incorrect NIP-34 language.

Related commits sharpen the same surfaces. On April 22, fiatjaf added a Blossom server list to NIP-51 and adjusted NIP-29 metadata editing to match Flotilla's PUT-style behavior. On April 26, he renamed NIP-5A for clarity. April 2026 focused on making already-used protocol surfaces easier to implement and harder to misread.

OpenSats announced its [Sixteenth Wave of Nostr Grants](https://opensats.org/blog/sixteenth-wave-of-nostr-grants) on April 8, supporting Amethyst Desktop, Nostr Mail, Nostrord, Nurunuru (null--nostr), and a HAMSTR renewal: desktop clients, email-like messaging, group UX, Japanese onboarding, and off-grid connectivity.

---

*Thanks for reading Nostr Compass #20. [DM us on Nostr](https://nostr.com) with tips, corrections, or new projects to cover.*
