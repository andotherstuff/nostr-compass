---
title: "Nostr Compass #31"
date: 2026-07-15
publishDate: 2026-07-15
draft: false
type: newsletters
description: "Vector v0.4.0 retires Marmot for group chats in favor of the open Concord protocol and ships Concord v2 days later, Amethyst merges its own clean-room Concord implementation, Sonar splits off from Bitchat with a cross-platform alpha and a sticker-pack spec, Divine Mobile 1.0.16 ships at-rest encryption and ProofMode provenance, Bitchat 1.7.0 adds live push-to-talk voice, and MDK v0.9.4 bounds external-signer login."
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** [Vector v0.4.0](#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later) retires [Marmot](/en/topics/marmot/) as the default transport for Group Chats in favor of [Concord](/en/topics/concord-protocol/), an open, MIT-licensed community protocol also used by Soapbox's Armada, and ships Concord v2 four days later with a slash-command picker for bots, a self-destruct timer, and NIP-58 badges. [Amethyst merges its own clean-room, wire-compatible Concord implementation](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities) the same week. [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) splits off from Bitchat with a cross-platform alpha and is the cited spec source for this week's sticker-pack kinds proposal. [Divine Mobile 1.0.16](#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance) ships a deeper video editor, at-rest encryption, and ProofMode provenance that survives watermarked-clip downloads. [Bitchat v1.7.0](#bitchat-v170-adds-live-push-to-talk-voice-for-dms-and-the-public-mesh) adds live push-to-talk voice for DMs and signed push-to-talk on the public mesh. [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) bounds external-signer login and adds draft persistence, continuing its hardening pass the same week Vector steps away from the spec for group chat.

Tagged releases bring [n_cord v1.1](#n_cord-v11-adds-nsec-bunker-support) adding NSEC Bunker support, [cdk v0.17.3](#cdk-v0173-adds-nip-47-wallet-service-support-across-cdk-cdk-nwc-and-cdk-ffi) adding NIP-47 wallet-service support across cdk, cdk-nwc, and cdk-ffi, [Coop Mobile v0.2.4](#coop-mobile-v024-improves-nostr-connect-and-adds-ncryptsec1-import) improving Nostr Connect and adding ncryptsec1 import, [Nmail v0.14.0](#nmail-v0140-ships-on-macos-with-scheduled-send-and-push-notifications) landing on macOS with scheduled send, [Nostrord v2.2.0](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages) adding a DM master toggle, [Nostr WoT 0.3.86](#nostr-wot-0386-hardens-key-backups-and-signing-prompts) hardening key backups to NIP-49 format, [Keep Android v1.1.8](#keep-android-v118-adds-first-run-frost-onboarding) adding first-run FROST onboarding, [Noscall v0.6.0](#noscall-v060-adds-a-cashu-wallet-and-relay-based-push-notifications) adding a Cashu wallet and relay-based push notifications, [Kubo](#kubo-ships-tablet-mode-and-group-chat-photos) adding tablet mode and group-chat photos, and [Nostr Codex Phone v0.2.9](#nostr-codex-phone-v029-adds-gitdiffread-file-helper-requests) adding git, diff, and read-file helper requests.

On the unreleased side, [Amethyst](#amethyst-lets-accounts-nickname-contacts-with-encrypted-nip-85-cards) lets accounts nickname contacts with encrypted NIP-85 cards across 54 merged PRs, [Zap Cooking](#zap-cooking-ships-my-kitchen-phase-3-and-fixes-an-ndk-pool-quorum-bug) ships My Kitchen Phase 3 and fixes an NDK pool quorum bug, [Kehto](#kehto-streams-outbox-reads-before-relay-discovery) streams outbox reads before relay discovery finishes, [Wired and TAO](#wired-and-tao-add-nip-57-creator-revenue-sharing) add NIP-57 creator revenue sharing, [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) rebuilds its merchant orders inbox around ephemeral guest checkout, [Buzz](#buzz-hardens-channel-creator-provisioning-around-kind-39002) hardens channel-creator provisioning across 240 merged PRs, and [Nostr Docs](#nostr-docs-adopts-a-nip-49-signer-with-multi-account-and-qr-pairing) adopts a NIP-49 signer with multi-account and QR pairing. Newly tracked this week: [OpenDiscord v1.0.1](#opendiscord-v101-launches-as-a-discord-style-client-on-nostr), [Auditable Voting v0.1.140](#auditable-voting-v01140-aligns-organiser-voter-and-audit-proxy-roles), and Discovery pick [Cambium v0.3.2](#cambium-v032-pairs-with-heartwood-as-a-keyless-nip-55-signer), a keyless NIP-55 signer that proxies to a Heartwood hardware companion.

The NIPs repository merges nothing in the last week and opens six proposals: [kind:10011 favorite follow sets](#open-kind10011-favorite-follow-sets), a [private encrypted drive extending NIP-4E](#open-private-encrypted-drive-extends-nip-4e), [NIP-DA permissioned private data sharing](#open-nip-da-permissioned-private-data-sharing), [sticker pack kinds 10031 and 30031](#open-sticker-pack-kinds-10031-and-30031), [NIP-29 message pinning](#open-nip-29-message-pinning-with-kind9010-and-kind39005), and a [NIP-66 relay discovery restructure](#open-nip-66-relay-discovery-restructure). The Deep Dive covers [NIP-99 and the Gamma Markets commerce extension](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension).

---

## Lead stories

### Vector v0.4.0 moves Group Chats from Marmot to Concord, and Amethyst ships its own Concord client days later

[Vector](https://github.com/VectorPrivacy/Vector) is a Nostr messenger built around a single-binary, privacy-first client for DMs and group chats. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) rewrites the app's messaging engine into a shared `vector-core` library and, in the same release, retires [Marmot](/en/topics/marmot/) (MLS-over-Nostr) as the default transport for Group Chats in favor of [Concord](/en/topics/concord-protocol/), an end-to-end encrypted community protocol; existing Marmot group history does not carry over, and the release notes tell users to back up any Marmot group data before upgrading. Vector's own release notes describe Concord as "our custom messaging protocol," but the underlying [CORD-01 through CORD-07 specs](https://github.com/concord-protocol/concord) are published separately, MIT-licensed, and already implemented outside Vector: Soapbox's Discord-style client [Armada](https://gitlab.com/soapbox-pub/armada) builds its Communities feature on the same Concord spec, and one day later, [Amethyst merged its own clean-room, wire-compatible Concord implementation](https://github.com/vitorpamplona/amethyst/pull/3566), covered in full below. The same Vector release adds optional Tor routing for all traffic, [NIP-46](/en/topics/nip-46/) remote-signer login by QR or pasted bunker URI, multiple accounts with an in-app switcher, and custom emoji packs shared across clients. Message deletion removes a message for both sides in DMs and group chats, and Vector deliberately keeps the ephemeral signing key instead of following the standard [NIP-17](/en/topics/nip-17/) deletion flow, a privacy-motivated departure the project calls out explicitly in the release notes. Four days later, [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) ships **Concord v2**, described as bringing major privacy and stability improvements to Communities while keeping existing ones working, alongside a Discord-style slash-command picker for bots with typed parameters, a per-chat self-destruct timer, and a NIP-58 badge system for bug hunters. The move away from Marmot for group chat comes the same week [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) below continues investing in the spec.

### Amethyst ships a clean-room Concord implementation for end-to-end encrypted communities

[Amethyst](https://github.com/vitorpamplona/amethyst) is a feature-rich Android and multiplatform Nostr client. [PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566) adds a full implementation of [Concord](/en/topics/concord-protocol/) (CORD-01 through CORD-07) covering serverless, end-to-end encrypted communities: gift-wrapped control, chat, and guestbook planes over ordinary relays, owner-rooted role and ban enforcement that every client verifies locally instead of trusting a server, and rekeying to cut off removed members. Protocol and crypto code lives in `quartz/`, state and view models in `commons/`, and screens and navigation in `amethyst/` for Android, with thin CLI verbs under `cli/`; there is no desktop UI yet, since the shared logic sits in `quartz`/`commons` for Desktop to adopt later. The implementation is clean-room: built from the public CORD specs and observed wire constants, under Amethyst's own MIT license, distinct from Armada's AGPL-3.0 codebase. Armada's own test-vector values were ported into Quartz's unit tests to confirm the two clients actually interoperate on the wire, giving Concord three independent implementations within days of each other: Vector shipping first, Armada as Soapbox's reference client, and now Amethyst's from-spec build.

### Sonar splits off from Bitchat with a cross-platform alpha and a sticker-pack spec

[Sonar](https://sonarprivacy.xyz/) is a Bluetooth-mesh-plus-Nostr messenger and wallet grown out of Bitchat, with Marmot group DMs interoperable with White Noise. Code lives at [hedwig-corp/bitchat-to-sonar](https://github.com/hedwig-corp/bitchat-to-sonar). [v0.1-alpha.7](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.7) adds Signal-style bounded transcript windowing so open and scroll performance stays local-first, synchronizes nearby-discovery state across peers, and fixes Blossom media uploads that were failing on content-type and HTTP-status handling; the preceding [alpha.6](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.6) drained live Marmot events for faster chat refresh and closed Android-to-iOS feature parity gaps across calls, messaging, wallet, and push. Sonar is also the cited spec source for [PR #2410](#open-sticker-pack-kinds-10031-and-30031), which registers sticker-pack event kinds under the project's own "Sonar Stickers" specification, giving this launch a direct hub link into this week's protocol work.

### Divine Mobile 1.0.16 ships a deeper video editor, at-rest encryption, and ProofMode provenance

[Divine](https://github.com/divinevideo/divine-mobile) is a short-video client built on Nostr with Web-of-Trust feed curation. [v1.0.16](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.16), the first tagged release since #30, adds clip transitions, reverse playback, a voice-over recorder, and timeline beat markers to the video editor, alongside a feed-tuning control that lets a user swipe to adjust recommendations directly instead of leaving them to opaque engagement signals. The release also turns on at-rest encryption for local data, adds background uploads that survive the app being suspended, and carries [ProofMode](/en/topics/proofmode/) provenance data forward when a watermarked clip is downloaded so the human-made attestation is not stripped in transit. Divine also ships new protections for under-16 accounts and expands localization to 17 languages and 284 translated strings.

### Bitchat v1.7.0 adds live push-to-talk voice for DMs and the public mesh

[Bitchat](https://github.com/permissionlesstech/bitchat) is a Bluetooth-mesh chat app with an opt-in gateway onto Nostr relays. [v1.7.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.7.0), released the evening #30 published, adds live push-to-talk voice in [PR #1403](https://github.com/permissionlesstech/bitchat/pull/1403) that streams audio while the sender holds the button and falls back to a voice note if the stream drops, plus signed public-mesh push-to-talk in [PR #1406](https://github.com/permissionlesstech/bitchat/pull/1406) so live voice bursts on the shared mesh channel carry sender authentication. The release also heals peer-ID rotation by rebinding the link on a verified re-announce, recognizing the same peer under its new ID ([PR #1401](https://github.com/permissionlesstech/bitchat/pull/1401)), and direct messages to a currently unreachable peer now queue with store-and-forward delivery instead of failing outright ([PR #1415](https://github.com/permissionlesstech/bitchat/pull/1415)). This continues directly from #30's coverage of v1.6.0's [NIP-13](/en/topics/nip-13/) proof-of-work and mesh-to-Nostr gateway work.

### MDK v0.9.4 bounds external-signer login and adds draft persistence

[MDK](https://github.com/marmot-protocol/mdk) is the reference SDK for the [Marmot](/en/topics/marmot/) protocol, the MLS-over-Nostr messaging layer that #30 covered marking its spec adopted. [v0.9.4](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.4) bounds the advisory-directory steps a client walks through during external-signer login in [PR #793](https://github.com/marmot-protocol/mdk/pull/793), preventing an unbounded retry loop when a remote signer is slow or unresponsive. The same release adds draft-message persistence and profile-website bindings in [PR #812](https://github.com/marmot-protocol/mdk/pull/812), continuing the incremental hardening pass MDK has run since cutting v0.9.0.

---

## Tagged releases

### n_cord v1.1 adds NSEC Bunker support

[n_cord](https://github.com/0n4t3/n_cord) is a Nostr-powered chat client inspired by Discord and IRC. [v1.1](https://github.com/0n4t3/n_cord/releases/tag/v1.1) adds [NIP-46](/en/topics/nip-46/) NSEC Bunker support alongside a reply-handling bug fix.

### cdk v0.17.3 adds NIP-47 wallet-service support across cdk, cdk-nwc, and cdk-ffi

[cdk](https://github.com/cashubtc/cdk) is a Cashu development kit; this release is Bitcoin/Lightning-only in most respects, but [v0.17.3](https://github.com/cashubtc/cdk/releases/tag/v0.17.3) adds [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect) service support with a dedicated NWC service crate, wallet integration, FFI bindings for `cdk-ffi`, and end-to-end test coverage, giving Cashu wallets built on cdk a standard Nostr Wallet Connect surface.

### Coop Mobile v0.2.4 improves Nostr Connect and adds ncryptsec1 import

[Coop Mobile](https://git.reya.su/reya/coop-mobile) is a [NIP-17](/en/topics/nip-17/) private-messaging client for mobile platforms. [v0.2.4](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.4) improves its [NIP-46](/en/topics/nip-46/) Nostr Connect flow, fixes a loading indicator that stuck permanently on some connections, and adds import support for the [NIP-49](/en/topics/nip-49/) `ncryptsec1` encrypted key format alongside a redesigned identity-import screen.

### Nmail v0.14.0 ships on macOS with scheduled send and push notifications

[Nmail](https://github.com/nogringo/nostr-mail-client) is a mail client built on Nostr; [v0.14.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.14.0) brings the app to macOS, adds scheduled send with a dedicated Scheduled mailbox for queued messages, and adds push notifications. The release also switches address-book Nostr identifier resolution to NDK's [NIP-05](/en/topics/nip-05/) resolver in place of a bespoke implementation.

### Nostrord v2.2.0 adds a DM master toggle and richer direct messages

[Nostrord](https://github.com/nostrord/nostrord) is a [NIP-29](/en/topics/nip-29/) relay-based group-chat client for Android, iOS, web, and desktop. [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) adds a master toggle to disable all direct-message features at once ([PR #175](https://github.com/nostrord/nostrord/pull/175)) and ships "richer direct messages" ([PR #186](https://github.com/nostrord/nostrord/pull/186)), continuing from #30's coverage of the release folding the relay pool and detecting zombie WebSockets.

### Nostr WoT 0.3.86 hardens key backups and signing prompts

[Nostr WoT](https://github.com/nostr-wot/nostr-wot-extension) is a browser extension pairing a Nostr identity with a Lightning wallet. [v0.3.86](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.3.86) moves encrypted-key backups to the standard [NIP-49](/en/topics/nip-49/) format, makes signing prompts show the full event and all tags instead of a summary, verifies relay data against its signature, and stops exposing the active identity when switching accounts. The extension also drops the unused `scripting` browser permission.

### Keep Android v1.1.8 adds first-run FROST onboarding

[Keep](https://github.com/privkeyio/keep-android) is an Android signer built on threshold FROST key shares. [v1.1.8](https://github.com/privkeyio/keep-android/releases/tag/v1.1.8) adds a first-run flow that explains FROST key shares and lets a new user pick a signing policy of Manual, Basic, or Auto before the first signature request arrives, the first Android-side onboarding for the underlying keep-mobile crate's threshold-signing model.

### Noscall v0.6.0 adds a Cashu wallet and relay-based push notifications

[Noscall](https://github.com/sanah9/noscall) is a secure audio- and video-calling app built on Nostr. [v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release) adds an account-scoped Cashu wallet with multi-mint balances, ecash send and receive, and Lightning pay and receive with quote persistence. The release also migrates Android push notifications off Firebase Cloud Messaging to a Nostr-relay-based delivery path through UnifiedPush, and improves iOS VoIP and APNs push reliability during login retries.

### Kubo ships tablet mode and group-chat photos

[Kubo](https://github.com/JeroenOnNostr/kubo) is a child-safe Nostr video platform with Web-of-Trust feed curation. [kubo-v2026.07.05](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v2026.07.05) adds an opt-in tablet grid layout for the child feed and support for attaching photos to group-chat messages, plus fixes for the sign-up button hiding behind the on-screen keyboard on Android.

### Nostr Codex Phone v0.2.9 adds git/diff/read-file helper requests

[Nostr Codex Phone](https://github.com/tidley/nostr-codex-phone) is a mobile control surface for a local coding-assistant worker communicating over encrypted Nostr DMs. [v0.2.9](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.9) adds mobile OpenCode tool actions including git, diff, read-file, status, and history helper requests, session pin and search improvements, and a task-stop control, alongside an encrypted [Blossom](/en/topics/blossom/) upload wrapper that shipped in the preceding v0.2.8.

### GitWorkshop v3.0.3 fixes newly announced refs in the repo explorer, and ships its first Android build

[GitWorkshop](https://github.com/DanConwayDev/gitworkshop) is a git-over-Nostr web UI for browsing and reviewing NIP-34 repositories. [v3.0.3](https://github.com/DanConwayDev/gitworkshop/releases/tag/v3.0.3) fixes the branches, tags, commits, and code-browsing views failing to resolve a ref that a repo announces after the explorer has already loaded it, alongside CI workflow-timing cleanup, confirmed directly against the tag and commit history. The same week, GitWorkshop published its first native Android build to [Zapstore](https://zapstore.dev), starting at v3.0.0 and reaching v3.0.3 within hours; the web UI stays the primary interface, and the Android package brings the same NIP-34 repository browsing to a phone for the first time.

### Bitcoin-Safe reaches Flathub, spotlighting its Nostr Sync & Chat plugin

[Bitcoin-Safe](https://bitcoin-safe.org) is a self-custody Bitcoin wallet built around hardware-signer workflows. The project [shipped a Flathub package](https://flathub.org/apps/org.bitcoin_safe.BitcoinSafe) this week, its first listing in a mainstream Linux app store. The Flathub release puts Bitcoin-Safe's Sync & Chat plugin in front of a wider audience: the plugin uses [NIP-17](/en/topics/nip-17/) direct messages, via the project's own [bitcoin-nostr-chat](https://github.com/andreasgriffin/bitcoin-nostr-chat) library, to synchronize wallet labels between a user's devices and to send and receive PSBTs for remote multisig co-signing between trusted participants. The Nostr layer itself shipped earlier, in [2.0.0](https://github.com/andreasgriffin/bitcoin-safe/releases/tag/2.0.0) (2026-06-29), which redesigned transaction signing around a "Share via Chat & Sync" connection type alongside QR, USB, and Bluetooth. This week's news is the Flathub packaging putting that existing feature in front of a mainstream Linux audience for the first time.

---

## Unreleased changes

### Amethyst lets accounts nickname contacts with encrypted NIP-85 cards

Beyond the [Concord implementation](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities) covered above, Amethyst merged 54 other PRs in the last week. The headline among them is [PR #3548](https://github.com/vitorpamplona/amethyst/pull/3548), which lets an account nickname any other user by publishing its own kind 30382 [NIP-85](/en/topics/nip-85/) contact card about them. The petname, a private note, and any custom [NIP-30](/en/topics/nip-30/) emoji-shortcode mappings live inside the card's [NIP-44](/en/topics/nip-44/)-encrypted content, so only the signing account can read them, and cards sync through the account's extended outbox relay set on login and incrementally afterward. Feeds, chats, and mentions render the petname in place of the public display name, with a tappable nickname card on the profile page above the user's real name.

### Zap Cooking ships My Kitchen Phase 3 and fixes an NDK pool quorum bug

[Zap Cooking](https://github.com/zapcooking/frontend) is a recipe-sharing and cooking-community app built on Nostr. It merged 43 PRs continuing its "My Kitchen" meal-planning feature, landing grocery-list generation, a recipe picker, and a planner week grid in this phase. The same set of changes fixes an [NDK](https://github.com/nostr-dev-kit/ndk) (Nostr Development Kit) connection-pool quorum-readiness bug that could leave relay reads waiting past the point a quorum of relays had already answered.

### Kehto streams outbox reads before relay discovery

[Kehto](https://github.com/kehto/web) is an early web-based runtime for [NIP-5D](/en/topics/nip-5d/) Nostr applets, or "napplets." It merged 26 PRs. [PR #193](https://github.com/kehto/web/pull/193) fixes outbox reads that previously waited on [NIP-65](/en/topics/nip-65/) relay-list loading to finish before opening any relay at all, so a relay-list load that never settled could block both event delivery and query timeouts; the fix opens validated relay hints immediately and streams results as write relays are discovered. A second change ([PR #196](https://github.com/kehto/web/pull/196)) aligns the project's identity-audit page with NAP-SHELL, the Napplet platform's lifecycle contract, part of the same protocol-alignment work visible elsewhere in this week's `napplet/web` release.

### Wired and TAO add NIP-57 creator revenue sharing

[Wired](https://github.com/smolgrrr/Wired) and [TAO](https://github.com/smolgrrr/TAO) are twin free-speech-focused social clients built on Nostr, sharing the same PR list; both merged [PR #121](https://github.com/smolgrrr/Wired/pull/121), which implements [NIP-57](/en/topics/nip-57/) creator revenue sharing so zaps sent to a post can split automatically to contributors beyond the original poster. This continues #30's coverage of the pair raising their proof-of-work signal to 21 bits as unreleased work.

### Conduit Mono rebuilds the merchant orders inbox around ephemeral guest checkout

[Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) is a marketplace protocol adjacent to [NIP-99](/en/topics/nip-99/) classified listings. [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) adds guest checkout using a browser-generated ephemeral key: the guest sends an encrypted order and a payment report to the merchant using that one-time key, and the merchant follows up out of band by phone or email, so the buyer never needs a durable inbox identity. [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) rebuilds the merchant orders inbox around a single shared order-state model, separating buyer and merchant roles and requiring a tracking code and carrier before a physical or mixed order can move to shipped. The project's checkout flow builds on [NIP-17](/en/topics/nip-17/) private messages, [NIP-44](/en/topics/nip-44/) encryption, and [NIP-59](/en/topics/nip-59/) gift wrap. This week's [NIP Deep Dive](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension) covers the [Gamma Markets](/en/topics/gamma-markets/) conventions this same order-state problem builds toward.

### Buzz hardens channel-creator provisioning around kind 39002

[Buzz](https://github.com/block/buzz) is a hive-mind communication platform connecting AI agents and humans over Nostr. It merged 240 PRs in the last week, continuing its relay-layer hardening arc from #30's coverage of kind 44200 agent-turn metrics. This week's fix ([PR #1830](https://github.com/block/buzz/pull/1830)) treats a channel's creator as a member before kind 39002 channel-provisioning logic runs, closing a race where the creator's own channel could reject them during setup.

### Nostr Docs adopts a NIP-49 signer with multi-account and QR pairing

[Nostr Docs](https://github.com/formstr-hq/nostr-docs) is a Nostr-native collaborative docs application. It merged 5 PRs, the notable one ([PR #50](https://github.com/formstr-hq/nostr-docs/pull/50)) adopting the `@formstr/signer` package for full [NIP-49](/en/topics/nip-49/) authentication with multi-account switching and QR pairing, replacing an earlier bespoke signing path.

### Also shipped

Smaller signer-interop and reliability fixes landed across several tracked projects in the last week without enough new surface for their own paragraphs: [ngit-cli](https://github.com/DanConwayDev/ngit-cli), a command-line client for a Nostr-based GitHub alternative, ships [v2.6.3](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.6.3) making `ngit init` give actionable setup guidance instead of repeatedly prompting for an nsec; [Manent](https://github.com/dtonon/manent), a private encrypted notes-and-files app built on Nostr, ships [v1.4.1](https://github.com/dtonon/manent/releases/tag/v1.4.1) fixing Android signer login broken when Amber returns a hex pubkey and improving bunker-login scrolling; [NoorNote](https://github.com/77elements/noornote), a slim, Google-service-free Nostr client, ships [v1.2.8](https://github.com/77elements/noornote/releases/tag/v1.2.8) fixing missed Nostrord-group notifications and adding a self-post alert toggle; [Bray](https://github.com/forgesworn/bray), a trust-aware Nostr MCP server for AI agents and humans, ships [v1.34.0](https://github.com/forgesworn/bray/releases/tag/v1.34.0) sending client-name metadata on [NIP-46](/en/topics/nip-46/) bunker connect; [Lumilumi](https://github.com/TsukemonoGit/lumilumi), a Nostr web client, caches [NIP-65](/en/topics/nip-65/) relay lists in local storage for offline fallback; [Earthly](https://github.com/moogmodular/earthly), a Nostr-based local city and community app, adds [NIP-50](/en/topics/nip-50/) geo search; and [lnbits](https://github.com/lnbits/lnbits), a free and open-source Lightning wallet and accounts system, ships [PR #3925](https://github.com/lnbits/lnbits/pull/3925) making `send_nostr_dm` publish non-blocking inside an otherwise Lightning-focused release.

---

## Newly tracked and discovered

### OpenDiscord v1.0.1 launches as a Discord-style client on Nostr

[OpenDiscord](https://github.com/sofia-gros/open-discord) is a Discord-style server-and-channel client built on Nostr with role-based permissions and WebRTC/SFU voice lobbies. [v1.0.1](https://github.com/sofia-gros/open-discord/releases/tag/v1.0.1) is the project's first tagged installer release.

### Auditable Voting v0.1.140 aligns organiser, voter, and audit-proxy roles

[Auditable Voting](https://github.com/tidley/auditable-voting) is a client-only Nostr voting shell. [v0.1.140](https://github.com/tidley/auditable-voting/releases/tag/v0.1.140) aligns the organiser, voter, and audit-proxy roles with the exact organiser-signed public questionnaire-definition event, closing a gap where an audit proxy could act on stale generated accounts or state persisted from a different worker or organiser.

### Cambium v0.3.2 pairs with Heartwood as a keyless NIP-55 signer

[Cambium](https://github.com/forgesworn/cambium) is this issue's Discovery pick: an Android [NIP-55](/en/topics/nip-55/) signer that holds no private key material of its own, proxying every signing request over [NIP-46](/en/topics/nip-46/) to a companion Heartwood hardware signer. The project shares the `forgesworn` GitHub org with tracked project Bray, and Heartwood itself was covered in #30 shipping the relay-to-serial signing bridge that Cambium's Android side now talks to. [v0.3.2](https://github.com/forgesworn/cambium) polishes the approval sheet to warn live when the selected identity differs from the app's existing binding and moves activity-log writes to a single non-blocking queue.

### Also launching this week: echoes, Dispatch, and Linky

Three more launches are worth a mention this week. [echoes](https://github.com/Lwb89dev/echoes) is an offline-first, end-to-end encrypted notes app that syncs privately over Nostr. [Dispatch](https://github.com/freecritter/dispatch) is a local-first travel organizer where every save is [NIP-44](/en/topics/nip-44/)-encrypted and backed up over Nostr under a dedicated, unlinkable key, and its [v0.3.0](https://github.com/freecritter/dispatch) release adds Amber [NIP-55](/en/topics/nip-55/) login so the app never touches the user's private key directly. [Linky](https://github.com/hynek-jina/linky) combines Nostr contacts and DMs with Lightning and Cashu payments in a single progressive web app.

---

## Protocol work and NIP updates

No PRs merged into the [NIPs repository](https://github.com/nostr-protocol/nips) in the last week. Six proposals opened.

### Open: kind:10011 favorite follow sets

[PR #2413](https://github.com/nostr-protocol/nips/pull/2413), from fiatjaf, adds kind:10011 favorite follow sets. It mirrors the existing pattern where kind:10012 (favorite relay sets) holds `a` tags pointing at kind:30002 relay sets, extending the same favoriting mechanism to kind:30000 follow sets so a client can bookmark a curated follow list without replacing its own contact list.

### Open: private encrypted drive extends NIP-4E

[PR #2412](https://github.com/nostr-protocol/nips/pull/2412), from the Form* team, proposes a generic Metadata event, kind 34578, distinguished by a `d` identifier tag and a `t` sub-type tag, along with a private encrypted file system built on top of it that is already implemented in Form*'s own, still-experimental Form* Drive client. A file record is a Metadata event with `t=files`: file blobs live on [Blossom](/en/topics/blossom/) servers while only an encrypted index sits on relays, and each file chunk gets its own ephemeral keypair with [NIP-44](/en/topics/nip-44/) v2 HKDF-derived encryption. A companion Decoupled Encryption Key event holds one drive-wide symmetric key that every file's metadata decrypts against, and it explicitly builds on [NIP-4E](/en/topics/nip-4e/), fiatjaf's still-open storage-abstraction draft ([PR #1647](https://github.com/nostr-protocol/nips/pull/1647), open since December 2024).

That single drive-wide key means a leaked key exposes every file's metadata in the drive, not just one file, since the per-file ephemeral keypairs only vary the chunk-encryption key, not the metadata-decryption key; no rotation or revocation path exists yet beyond publishing a new Metadata event warning that older events may be lost. A second, narrower proposal reaches for the same underlying NIP-4E idea from a different angle: [PR #2361](https://github.com/nostr-protocol/nips/pull/2361), from fiatjaf, decouples identity and encryption keys inside [NIP-17](/en/topics/nip-17/) messaging specifically, open since June 1. Both PRs are unmerged, leaving this an active, contested corner of the design space. Form* says the Drive client is experimental with an update coming soon.

### Open: NIP-DA permissioned private data sharing

[PR #2411](https://github.com/nostr-protocol/nips/pull/2411), from JAFairweather, is a new NIP-DA draft for permissioned private data sharing through scoped data grants. Each user keeps one encrypted, authoritative record per scope on relays, and access is granted by privately delivering that scope's symmetric key inside a [NIP-59](/en/topics/nip-59/) gift wrap, so relays store only ciphertext and never learn who granted access to whom; a revocation is just a key rotation, with no need to rewrite every consumer's copy. The author positions it as distinct from [NIP-17](/en/topics/nip-17/) DMs (which can carry a data snapshot but not live updates or revocation) and from NIP-51 private lists (which carry no key material), and cites two independent implementations, a JavaScript reference library and a Go CLI on go-nostr, cross-tested against relay.damus.io, nos.lol, and relay.primal.net.

### Open: sticker pack kinds 10031 and 30031

[PR #2410](https://github.com/nostr-protocol/nips/pull/2410), from vincenzopalazzo, registers kind 30031 (addressable sticker packs) and kind 10031 (a user's sticker pack list) in the Event Kinds table, specified by the "Sonar Stickers" format that [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) ships this week. The kinds sit deliberately one slot above the [NIP-30](/en/topics/nip-30/) custom-emoji kinds 30030 and 10030 so a client cannot mistake a sticker pack for an emoji set; sticker image bytes live on HTTPS [Blossom](/en/topics/blossom/)-compatible servers, and sent-sticker references carry a plaintext hash so an edited addressable pack cannot silently change the appearance of stickers already sent in old messages. A companion PR registers the same kinds in the separate `registry-of-kinds` project.

### Open: NIP-29 message pinning with kind:9010 and kind:39005

[PR #2379](https://github.com/nostr-protocol/nips/pull/2379), from Anderson-Juhasc, adds message pinning to [NIP-29](/en/topics/nip-29/) relay-based groups: kind:9010 `update-pin-list` is a moderation event carrying the full pinned-event list as `e` tags in display order, so a single event can pin, unpin, reorder, or clear the pinned set, and kind:39005 is a relay-generated mirror exposing the latest accepted list. The design supersedes an earlier add/remove-pair approach from [PR #1163](https://github.com/nostr-protocol/nips/pull/1163) after review feedback, and picks kind numbers 9010/39005 because 9009 and 39003 have since been claimed by `create-invite` and group roles. Anderson-Juhasc also maintains [Nostrord](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages), whose [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) ships this same week.

### Open: NIP-66 relay discovery restructure

[PR #2241](https://github.com/nostr-protocol/nips/pull/2241), from VincenzoImp, is a substantial restructure of [NIP-66](/en/topics/nip-66/) relay discovery. It replaces the loose "Other tags include" prose with a structured Indexed Tags section, adds a `W` tag mirroring NIP-11's `attributes` field for relay-discovery filtering, adds an `l` label tag using standardized namespaces (`ISO-639-1`, `ISO-3166-1`, `IANA-asn`, `IANA-tz`, `nip66.label.city`), and organizes RTT, SSL/TLS, network, geographic, DNS, and HTTP tags into dedicated sections alongside a new Check Types table. It also fixes broken example events that had wrong field names, a missing `kind`, and invalid check-type names, and closes out [issue #2171](https://github.com/nostr-protocol/nips/issues/2171). All changes stay backward compatible since every added tag is optional.

---

## NIP Deep Dive: NIP-99 and the Gamma Markets commerce extension

[NIP-15](/en/topics/nip-15/), the original Nostr Marketplace spec, is legacy at this point: it modeled a merchant stall (kind 30017) with products (kind 30018) filed underneath it, and the clients that once ran on it, Shopstr among them, have since moved to [NIP-99](/en/topics/nip-99/) classified listings as the active spec. NIP-99 itself is a single addressable event, kind 30402 for an active listing or kind 30403 for a draft, with no stall to create first. It leaves everything past the listing undefined: shipping cost, order status, receipts, reviews, and a way to group several listings under one storefront, exactly the parts of NIP-15 that never carried over. [Gamma Markets](/en/topics/gamma-markets/) fills that gap, and is the modern commerce layer worth understanding today.

### The gap NIP-99 leaves open

A NIP-99 listing's `content` field carries a Markdown description, `price` and `location` sit directly on the event, and `t` tags make it searchable as ordinary hashtag content. Because it is addressable on the pubkey, kind, and `d` tag tuple, a seller edits a listing in place by publishing a new version with the same `d` tag:

```json
{
  "kind": 30402,
  "content": "Vintage mechanical keyboard, Cherry MX Blue switches, barely used.",
  "tags": [
    ["d", "keyboard-mx-blue-01"],
    ["title", "Vintage Mechanical Keyboard"],
    ["summary", "Cherry MX Blue, barely used"],
    ["published_at", "1752537600"],
    ["location", "NYC"],
    ["price", "100", "USD"],
    ["t", "electronics"]
  ]
}
```

That is the entire spec: a signed, updatable classified ad. Every client implementing NIP-99 for real e-commerce, beyond a one-off classified, ended up inventing its own private conventions for shipping, order messages, and reviews. Two NIP-99 clients could each render a listing correctly and still have no shared way to complete a checkout between them.

### Gamma Markets: standardizing what NIP-99 left out

Gamma Markets is the name a working group of Nostr marketplace developers, the teams behind Shopstr, Cypher, Plebeian Market, and Conduit Market, gave to a shared set of e-commerce conventions built on top of NIP-99's existing kind 30402 event. The spec is linked from the canonical NIP-99 document via [PR #1784](https://github.com/nostr-protocol/nips/pull/1784) and maintained in its own repository, [GammaMarkets/market-spec](https://github.com/GammaMarkets/market-spec).

Gamma Markets adds two standalone listing-adjacent kinds. Kind 30405 groups multiple listings into a product collection, referencing each one by an explicit `a` tag:

```json
{
  "kind": 30405,
  "content": "Summer sale picks",
  "tags": [
    ["d", "summer-picks"],
    ["title", "Summer Sale"],
    ["a", "30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["shipping_option", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

Kind 30406 defines a shipping option with per-country pricing and optional weight- or distance-based cost rules:

```json
{
  "kind": 30406,
  "content": "Standard Regional Shipping",
  "tags": [
    ["d", "standard-regional"],
    ["title", "Standard Shipping"],
    ["price", "5.99", "USD"],
    ["country", "US"],
    ["service", "standard"],
    ["duration", "24", "72", "H"],
    ["weight-max", "30", "kg"]
  ]
}
```

Order creation, payment requests, status and shipping updates, and payment receipts all move as ordinary [NIP-17](/en/topics/nip-17/) gift-wrapped private messages, split across three kinds by role, not by rewrapping the transport: kind 14 carries free-form buyer/merchant communication, kind 16 carries every order-state transition (a `type` tag of 1 through 4 marks order creation, payment request, status update, or shipping update), and kind 17 carries the buyer's payment receipt. An order creation message looks like this before gift-wrapping:

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

Rating a completed purchase is a separate addressable kind, 31555, pointing back at the listing it reviews:

```json
{
  "kind": 31555,
  "content": "Arrived fast, exactly as described.",
  "tags": [
    ["d", "a:30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["rating", "1", "thumb"],
    ["rating", "1.0", "quality"],
    ["rating", "0.9", "delivery"]
  ]
}
```

Riding order messages on NIP-17 means a Gamma Markets checkout uses the same private-message transport clients already ship for DMs, instead of a bespoke order-message kind.

The spec's core design choice is that nothing cascades. A listing that belongs to a collection references it explicitly with an `a` tag instead of inheriting the collection's shipping options or description automatically, and a shipping option a listing uses is referenced the same explicit way. That is a deliberate reversal of NIP-15's stall model, where a product silently inherited whatever currency and shipping table its parent stall defined. The tradeoff is more explicit tagging on every listing, in exchange for a listing's full configuration always being readable from the event itself, with no parent object to resolve first.

### Where this shows up in practice

This week's [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) work sits in the same order-message territory Gamma Markets standardizes: [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174)'s ephemeral-key guest checkout and [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175)'s merchant-orders-inbox rebuild both solve the buyer/merchant order-state problem that Gamma Markets' kind 14, 16, and 17 messages formalize; Conduit Mono runs its own order-state model alongside those kinds, without adopting them directly. Shopstr, one of the four projects that authored the spec, kept its own commerce plumbing moving in the last week too: [PR #568](https://github.com/shopstr-eng/shopstr/pull/568) extracts duplicated NIP-17 gift-wrap logic into a shared module, and [PR #567](https://github.com/shopstr-eng/shopstr/pull/567) brings its [NIP-98](/en/topics/nip-98/) HTTP-auth parser to full test coverage, maintenance on exactly the messaging and auth layers a Gamma Markets order flow depends on to reach a buyer and merchant safely.

NIP-15 lost the storefront role by standardizing a stall and a product, then leaving payments, shipping, reviews, and order status as an application problem. Gamma Markets fills most of that missing surface without touching NIP-99's single-listing shape, building on Nostr's existing DM stack, NIP-17, instead of inventing a new messaging layer.

---

That's it for this week. Building something or have news to share? Reach out via NIP-17 DM or find us on Nostr.
