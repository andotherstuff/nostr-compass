---
title: "Nostr Compass #32"
date: 2026-07-22
publishDate: 2026-07-22
draft: false
type: newsletters
description: "IndieSats drops its publisher role and relaunches as open Nostr music infrastructure, Nostrord v2.3.0 ships the client side of a five-PR NIP-29 spec week, Zapstore 1.1.0 makes the device key portable and brings background auto-updates, favorite follow sets merge and immediately renumber, and the Iris projects ship a pubsub library, a browser FIPS runtime, and nostr-social-graph 2.0."
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** [IndieSats](#indiesats-drops-its-publisher-role-and-relaunches-as-open-nostr-music-infrastructure) retires key custody, its whitelist, and its mandatory revenue cut, relaunching as an open relay, player, and discovery layer where artists publish under their own keys. [Nostrord v2.3.0](#nostrord-v230-ships-group-moderation-mute-lists-and-onion-relays) lands group moderation, mute lists, and onion relays the same week five [NIP-29 spec PRs merge](#protocol-work-and-nip-updates). [Zapstore 1.1.0](#zapstore-110-makes-the-device-key-portable-and-adds-background-auto-updates) introduces a portable encrypted device key with Amber backup and opt-in background auto-updates. The [favorite-follow-sets list kind](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house) merges and opens a renumbering PR within days. And the [Iris projects](#the-iris-projects-ship-a-pubsub-library-a-browser-fips-runtime-and-a-social-graph-20-in-one-week) ship nostr-pubsub, the fips-ts browser runtime, and nostr-social-graph 2.0.0 in a single week.

Tagged releases bring [Amber v6.3.0](#amber-v630-groups-bunker-signing-approvals-and-adds-expert-list-support) with grouped bunker-signing approvals, [Armada v0.37.0](#armada-v0370-opens-buzz-workspaces-from-a-second-client) with a second client for Buzz workspaces, [Divine Mobile 1.0.17](#divine-mobile-1017-hardens-relay-security-and-dm-delivery) with durable NIP-17 delivery and strict TLS validation, and [nak v0.20.2](#nak-v0202-adds-nip-34-pull-request-workflows) with NIP-34 pull-request commands.

On the unreleased side, [Snort](#snort-rewrites-query-synchronization-around-eose-proven-coverage) records EOSE-proven cache coverage, [Shopstr](#shopstr-binds-payment-validation-to-signed-receipts-and-server-side-prices) closes two payment-integrity gaps, [Mostr](#mostr-bridges-activitypub-private-chats-and-nostr-dms) bridges ActivityPub private chats to Nostr DMs, [nostream](#nostream-merges-eight-prs-without-cutting-a-release) merges the access-control stack this week's Deep Dive covers, and [Amethyst](#amethyst-lands-v1130-pre-release-qa-on-napplet-isolation-and-concord-authority) reaches 88 merged PRs with full NIP-88 polls on Desktop.

The NIPs repository merges five PRs this week, including the [NIP-29 cluster](#protocol-work-and-nip-updates) and [kind:10011 favorite follow sets](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house), and opens debates on [NIP-47 simplification](#protocol-work-and-nip-updates) and [trusted relay assertions](#protocol-work-and-nip-updates). The Deep Dive covers [NIP-42 and NIP-43, the relay access-control pair](#nip-deep-dive-nip-42-and-nip-43).

---

## Lead stories

### IndieSats drops its publisher role and relaunches as open Nostr music infrastructure

[IndieSats](https://zapstore.dev) is a Nostr-based music platform that until this week acted as a publisher: it held keys for artists, ran a whitelist, and took a mandatory 2% cut of revenue. In a [pivot announcement published on July 20](https://njump.me/nevent1qqsr4awwnfndnnz77zanjxarw6nd0uld0ckayxp2navz0u9tzzwfweqpzamhxue69uhhyetvv9ujuurjd9kkzmpwdejhgtczyquwq70hxz22lzytw65rnnjewg0lj8a74khxa8h9j47q38pdnqy3kqcyqqqqqqgz8083u), the project retired all three of those roles at once. The relaunched platform is three pieces of open infrastructure: an open relay, a player, and a discovery layer. Artists now publish music under their own Nostr profiles. The 2% track-level platform share is optional but selected by default when an artist publishes, and artists can clear it to retain the full payment; the platform also honors [NIP-09](/en/topics/nip-09/) kind:5 deletion requests so artists can remove their work. A [v1.1.5 update published July 21](https://zapstore.dev/apps/com.indiesats.app) changed track publication to the event format expected by Amethyst and other Nostr music clients and made relay delivery explicit. For a space that usually talks about protocols replacing platforms, this is a live case of a platform voluntarily disassembling itself into protocol pieces.

### Nostrord v2.3.0 ships group moderation, mute lists, and onion relays

[Nostrord](https://github.com/nostrord/nostrord), the group-chat client for Android, iOS, web, and desktop, shipped [v2.3.0](https://github.com/nostrord/nostrord/releases/tag/v2.3.0) with wired-up group moderation actions on all UIs ([PR #192](https://github.com/nostrord/nostrord/pull/192)), consent-gated group invites with cross-relay detection ([PR #195](https://github.com/nostrord/nostrord/pull/195)), cross-platform [NIP-51](/en/topics/nip-51/) mute lists ([PR #188](https://github.com/nostrord/nostrord/pull/188)), and Tor .onion relay support. Its release lands the same week the underlying [NIP-29](/en/topics/nip-29/) spec merged five PRs covering subgroups, message pinning, banners, and invite codes (details in this week's [protocol section](#protocol-work-and-nip-updates)), so group chat on Nostr now has both a deeper spec and a client exercising most of it, which shortens the feedback loop for everyone else building on relay groups.

### Zapstore 1.1.0 makes the device key portable and adds background auto-updates

[Zapstore](https://github.com/zapstore/zapstore) is a Nostr-native app store where releases are signed by developer keys and no central operator vouches for them. [Version 1.1.0](https://github.com/zapstore/zapstore/releases/tag/1.1.0), the first release covered here since early March, closes the two biggest gaps with conventional app stores. For updates, opt-in background downloads now run over Wi-Fi and install silently or staged, so apps stay current without manual trips through the store. Identity continuity comes from a portable encrypted device key that users can back up through [Amber](https://github.com/greenart7c3/Amber) over [NIP-55](/en/topics/nip-55/), the Android signer interface, so a phone migration preserves the device identity. Version 1.1.0 also moves the app catalog onto relays as device-signed kind:10067 events, adds [NIP-56](/en/topics/nip-56/) verified reporting from the overflow menu so users can flag problematic apps in a way other clients can consume, and verifies the C1 proof attached to a release before any install proceeds, tightening the link between what a developer signed and what a device runs.

### The favorite-follow-sets list kind merges and immediately moves house

A spec-coordination story played out inside a single week. [PR #2413](https://github.com/nostr-protocol/nips/pull/2413) merged on July 15, standardizing a replaceable list kind for favorite follow sets under [NIP-51](/en/topics/nip-51/) (lists): a dedicated kind for a user's curated sets of followed accounts. Within days it turned out the assigned kind:10011 was already in use elsewhere, so a follow-up [PR #2417](https://github.com/nostr-protocol/nips/pull/2417) is now open to renumber the list to kind:10021. Nothing has shipped against the merged kind yet, which makes this the cheap moment to renumber; once clients start publishing kind:10011 events, the collision would get expensive to unwind. Developers building list-consuming features should track the renumbering PR, not the merged text, until it resolves.

### The Iris projects ship a pubsub library, a browser FIPS runtime, and a social-graph 2.0 in one week

Three releases from the Iris orbit landed together, and they interlock. [nostr-pubsub](https://github.com/mmalmi/nostr-pubsub) is a transport-neutral publish/subscribe library for Nostr events; its [first tracked releases, v0.1.3 through v0.5.2](https://github.com/mmalmi/nostr-pubsub/releases), deliver a browser relay carrier built on nostr-tools' SimplePool, event verification at the transport boundary so invalid signatures never reach subscribers, and bounded historical queries. [fips-ts](https://github.com/mmalmi/fips-ts) brings [FIPS](/en/topics/fips/), the Noise-over-secp256k1 peer transport previously available as a Rust stack, into the browser as a TypeScript runtime: releases [0.0.24 through 0.0.30](https://github.com/mmalmi/fips-ts/releases) added a WebRTC datachannel carrier, Nostr-based signaling for peer discovery, a recent-peer cache, and an IndexedDB adapter for browser storage, and the runtime is wire-compatible with the reference Rust implementation. The third piece, [nostr-social-graph v2.0.0](https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.0), is a major version of the social-graph library: signed roster operations for Nostr identity graphs, device-approval flows bootstrapped from a canonical three-field URI, and FIPS transport identity facets with shared Rust and TypeScript test vectors. The connective framing is the [Iris Stack](https://stack.iris.to/), the project's integration lab tying these libraries together with Blossom, Hashtree, and encrypted messaging. Taken together, a web app can now discover peers over Nostr, open an encrypted FIPS channel to them, and maintain a signed social graph, all in TypeScript.

---

## Tagged releases

### Amber v6.3.0 groups bunker signing approvals and adds Expert List support

[Amber](https://github.com/greenart7c3/Amber) is an Android [NIP-46](/en/topics/nip-46/) remote signer. [v6.3.0](https://github.com/greenart7c3/Amber/releases/tag/v6.3.0) adds grouped multi-request approval so users can review and approve a batch of bunker signatures at once. The release also adds support for Expert List (kind 12022) and Expert Pack (kind 32022) events, a privacy mode that hides sensitive content on screen, and a change to fetch an account's [NIP-65](/en/topics/nip-65/) relay list before its profile metadata so signer flows start from the user's actual relay set. This follows the v6.2.x line covered in the 2026-07-08 issue.

### Nostrord v2.2.0 follow-up

With [v2.3.0](#nostrord-v230-ships-group-moderation-mute-lists-and-onion-relays) leading this week's News section, the tagged-release slot notes only what the lead does not: v2.3.0 follows v2.2.0's DM controls covered in #31, making this the client's second consecutive weekly release.

### Armada v0.37.0 opens Buzz workspaces from a second client

[Armada](https://gitlab.com/soapbox-pub/armada), a Discord-style Nostr client, released [v0.37.0](https://gitlab.com/soapbox-pub/armada/-/commit/7a0d0ade51fb8a7bafa4513d2881d275bb2c7dde) with support for Buzz relays as an enhanced [NIP-29](/en/topics/nip-29/) workspace mode, detected through the relay's [NIP-11](/en/topics/nip-11/) metadata. The client renders Buzz forum posts and comments as kinds 45001 and 45003, folds edits and deletions into stream timelines, and adds presence, workflow, job, huddle, and shared-canvas surfaces. Its Projects workspace reads [NIP-34](/en/topics/nip-34/) repository announcements, patches, pull requests, issues, and status events directly from the relay ([implementation commit](https://gitlab.com/soapbox-pub/armada/-/commit/7d5603a3e21d564301d667113d28de4407d6f642)), giving Buzz workspaces a second client for both conversation and repository work.

### Wisp v1.2.0 adds a multi-account switcher and collapsible reply threads

[Wisp](https://github.com/barrydeen/wisp) is a privacy-oriented Nostr client with built-in wallet support. [v1.2.0](https://github.com/barrydeen/wisp/releases/tag/v1.2.0) adds a multi-account switcher for moving between profiles without re-login, collapsible reply threads for long conversations, stripping of tracking parameters from note links before they open, and a wallet transaction-history view. The release follows the Wisp update covered in the 2026-07-08 issue.

### Divine Mobile 1.0.17 hardens relay security and DM delivery

[Divine Mobile](https://github.com/divinevideo/divine-mobile), a Nostr short-video client, released [1.0.17](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.17) with a persistent stop-motion editor and tighter Nostr paths. Direct messages now wait for relay `OK` responses, retry through a durable queue, and route through recipients' kind 10050 inbox-relay lists ([PR #6046](https://github.com/divinevideo/divine-mobile/pull/6046)); NIP-46 pairing preserves `auth_url` challenges as recoverable signer steps ([PR #6151](https://github.com/divinevideo/divine-mobile/pull/6151)). [PR #6278](https://github.com/divinevideo/divine-mobile/pull/6278) removes permissive certificate acceptance from production relay WebSockets and HTTP requests used for NIP-96 uploads, LNURL, and zaps, restoring platform TLS validation outside debug loopback connections. Interrupted uploads can also resume from the server's last confirmed offset, so a backgrounded publish no longer restarts from zero.

### ClipRelay v0.1.2 (new project) syncs clipboards across devices over Nostr relays

[ClipRelay](https://github.com/tajava2006/cliprelay) is a newly launched cross-platform app (Android, macOS, Windows, Linux) that syncs your clipboard across your own devices: copy on one machine, paste on another. All traffic moves through Nostr relays as [NIP-44](/en/topics/nip-44/) encrypted events addressed to yourself, so there is no server to run and no account to create; the private key stays outside the app. [v0.1.2](https://github.com/tajava2006/cliprelay/releases) fixes a subtle sync failure where a machine waking from sleep kept publishing but silently stopped receiving, and tightens the relay-status indicators that previously reported dead subscriptions as healthy. This is ClipRelay's first appearance in the newsletter.

### Sonar v0.1-alpha.11 continues the alpha line

[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar), last week's lead story, cut [v0.1-alpha.11](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.11) with work on the Rust mesh link engine, BLE and mesh fixes, and relay diagnostics; an incremental follow-up to the alpha line covered in #31.

### nak v0.20.2 adds NIP-34 pull-request workflows

[nak](https://github.com/fiatjaf/nak), the Nostr command-line tool, released [v0.20.2](https://github.com/fiatjaf/nak/releases/tag/v0.20.2) with commands to create, pull, and merge [NIP-34](/en/topics/nip-34/) pull requests and to pull individual patches, and it allows pushes without rewriting a repository announcement. The [11-commit release range](https://github.com/fiatjaf/nak/compare/v0.20.1...v0.20.2) also adds parent-group handling for [NIP-29](/en/topics/nip-29/), queries more outbox relays, makes relay connection timeouts configurable, and fixes bunker selection when only the default `--sec` value exists.

### The week's smaller launches

Four smaller releases deserve one line each: [noscall v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release), the Nostr calling app, migrated its push notifications to UnifiedPush, keeping call signaling off Google's push infrastructure; [nostr-vpn v4.1.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.1.3), a mesh VPN that uses Nostr for signaling, unified its exit-DNS policy across platforms and now restores the original route and DNS state after WireGuard or private-exit sessions; [StableKraft v1.3.0](https://github.com/ChadFarrow/stablekraft-app/releases/tag/v1.3.0), the Nostr-plus-Lightning music and podcast aggregator covered in April, added native Android lock-screen and headset controls plus a playback-scoped wake lock so audio survives Doze; and new Zapstore app Hakari backs up a weight logger over encrypted Nostr events.

### Amethyst lands v1.13.0 pre-release QA on napplet isolation and Concord authority

[Amethyst](https://github.com/vitorpamplona/amethyst) merged 88 PRs this week ahead of its v1.13.0 release. [PR #3650](https://github.com/vitorpamplona/amethyst/pull/3650) is a pre-release QA pass covering napplet account isolation, Concord authority fixes, and around 30 other fixes. The late-window work adds full Desktop [NIP-88](https://github.com/nostr-protocol/nips/blob/master/88.md) poll rendering, creation, voting, declared-relay tallying, and kind 1068 search ([PR #3664](https://github.com/vitorpamplona/amethyst/pull/3664)); NIP-50 search now ranks results by BM25 relevance while large tag watchers use bounded merging ([PR #3663](https://github.com/vitorpamplona/amethyst/pull/3663)). A separate relay-store pass selects query indexes by measured cost, adds tag-author-kind indexes, and serializes each live event once per fanout ([PR #3660](https://github.com/vitorpamplona/amethyst/pull/3660)), with reported benchmark reductions from 149 to 4 milliseconds for one query shape and from 14.2 to 0.66 milliseconds for a common DM-room query.

---

## Unreleased changes

### Snort rewrites query synchronization around EOSE-proven coverage

[Snort](https://github.com/v0l/snort), a web Nostr client, rewrote its query and cache-synchronization path in [commit 8a62770](https://github.com/v0l/snort/commit/8a627700d8a5af9527cb68655d844dd14a3ac79d). The client now records which query windows reached EOSE, uses those watermarks to skip covered cache ranges, centralizes event dispatch behind one relay-pool listener, and sends search filters only to relays whose NIP-11 documents advertise [NIP-50](/en/topics/nip-50/). Follow-up fixes serialize concurrent watermark updates and correct inclusive timeline boundaries, while [commit 9d1721b](https://github.com/v0l/snort/commit/9d1721b8b5696a6f96f462170c469c232cabe672) restores a live subscription to the chunked follows feed so events arriving after page load do not freeze outside its cached windows.

### Shopstr binds payment validation to signed receipts and server-side prices

[Shopstr](https://github.com/shopstr-eng/shopstr), a Nostr marketplace client, closed two payment-integrity gaps. [PR #552](https://github.com/shopstr-eng/shopstr/pull/552) makes Zapsnag verify each kind 9735 receipt's signature, signer, embedded zap request, recipient and product tags, BOLT11 amount, and optional preimage against the invoice payment hash before treating it as a purchase. [PR #449](https://github.com/shopstr-eng/shopstr/pull/449) moves Cashu quote creation behind a Shopstr API route that resolves the listing and recomputes its price server-side, so a browser-modified amount cannot determine the mint invoice.

### Mostr bridges ActivityPub private chats and Nostr DMs

[Mostr](https://gitlab.com/soapbox-pub/mostr), an ActivityPub-to-Nostr bridge, now carries one-to-one Pleroma ChatMessage objects and encrypted Nostr DMs in both directions ([commit 36ee547](https://gitlab.com/soapbox-pub/mostr/-/commit/36ee547035f9287029f71656c472fe029a7ab31b)). ActivityPub private chats become kind 4 events addressed to the Nostr recipient, while kind 4 messages sent to bridged Fediverse users are decrypted and federated as ChatMessage objects. The bridge limits these events to configured DM relays gated by [NIP-42](/en/topics/nip-42/) and authenticates with a separate relay key. This interoperability path uses legacy [NIP-04](/en/topics/nip-04/) encryption. NIP-17 gift wrapping remains outside this implementation.

### nostream merges eight PRs without cutting a release

[nostream](https://github.com/Cameri/nostream), the TypeScript relay implementation, merged eight PRs this week without cutting a release. The headline pair is [PR #702](https://github.com/Cameri/nostream/pull/702) and [PR #676](https://github.com/Cameri/nostream/pull/676), which together give relay operators a working authentication-plus-membership access-control stack; this week's NIP Deep Dive walks through exactly that handshake. [PR #694](https://github.com/Cameri/nostream/pull/694) fixes generic `#e`, `#p`, `#g`, and similar tag filters that could return one copy of an event for every matching tag row, reducing duplicate protocol traffic within a subscription.

### FIPS v0.4.1 tightens the Iris transport layer

[jmcorgan/fips](https://github.com/jmcorgan/fips) shipped [v0.4.1](https://github.com/jmcorgan/fips/releases/tag/v0.4.1), a maintenance release capping antipoison state, fixing convergence and MTU handling, and cutting CPU use. The browser TypeScript runtime [fips-ts](https://github.com/mmalmi/fips-ts) from the Iris project cluster is wire-compatible with this Rust transport, so fixes here propagate directly to browser interoperability.

---

## Protocol work and NIP updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-29](/en/topics/nip-29/) (Relay-based Groups): Subgroups** ([PR #2319](https://github.com/nostr-protocol/nips/pull/2319), merged 2026-07-16): NIP-29 defines relay-hosted groups where membership, roles, and chat history live on a single relay as addressable `kind:39000`-series events, with moderation actions carried by `kind:9000`-series admin events. This PR lets a group declare itself a subgroup by adding a `parent` tag to its metadata, pointing at the `d` identifier of another group on the same relay. Subgroups are ordinary groups in every other respect: membership does not cascade (joining a parent grants no membership in any child), admin roles do not inherit (each subgroup's `kind:39001` admins list is authoritative for its own scope), and each subgroup keeps its own independent `kind:9000`/`kind:9001` member events. Relays that support the hierarchy advertise it in their NIP-11 relay information document under a `nip29` object with `"subgroups": true`, so clients can discover the capability before attempting to create nested communities.

- **[NIP-29](/en/topics/nip-29/): Message pinning** ([PR #2379](https://github.com/nostr-protocol/nips/pull/2379), merged 2026-07-15; [PR #2416](https://github.com/nostr-protocol/nips/pull/2416), merged 2026-07-17): Group admins can now pin messages inside a relay-based group. The mechanism adds a new moderation event, `kind:9010` `update-pin-list`, which carries the full ordered pin list as `e` tags referencing regular event ids, and a new optional group-level event, `kind:39005` *group pinned events*, which the relay regenerates to mirror the most recent accepted pin list. Each `kind:9010` replaces the whole list, so one new list expresses pinning, unpinning, reordering, or clearing. The follow-up PR #2416 extends the format so `a` tags are also accepted in the pin list, letting admins pin addressable events (long-form posts, wiki pages, and other parameterized replaceable content) alongside ordinary chat messages. Relays may cap the number of pins, and the merged spec text recommends displaying pins in the order the tags appear.

- **[NIP-29](/en/topics/nip-29/): Banner tag and invite-code suffix** ([PR #2383](https://github.com/nostr-protocol/nips/pull/2383), merged 2026-07-16; [PR #2380](https://github.com/nostr-protocol/nips/pull/2380), merged 2026-07-16): Two display-and-onboarding additions to group metadata. PR #2383 adds an optional `banner` tag to the `kind:39000` group metadata event, joining the existing `name`, `picture`, and `about` fields so clients can render a header image for a group page. PR #2380 defines an invite-code suffix for group share links: an invite code may be appended to the group's `naddr` identifier as `naddr1...?invite=<code>`. Because the bech32 character set does not include `?`, the portion before the suffix remains a valid naddr on its own, so clients that do not understand the extension can still resolve the group. Clients that do understand it pre-fill the `code` tag on the `kind:9021` join request, which pairs with the existing `kind:9009` `create-invite` moderation event to simplify admission to closed groups.

- **[NIP-51](/en/topics/nip-51/) (Lists): Favorite follow sets, kind:10011** ([PR #2413](https://github.com/nostr-protocol/nips/pull/2413), merged 2026-07-15): NIP-51 defines the standard list kinds, split between replaceable `kind:10000`-series lists (one per user) and addressable `kind:30000`-series sets (many per user, keyed by `d` tag). This PR adds `kind:10011`, *favorite follow sets*, a standard replaceable list whose `a` tags point at `kind:30000` follow sets. The mirror of `kind:10012` (relay feeds), which holds `a` tags referencing `kind:30002` relay sets, the new kind lets a user bookmark named follow sets, such as curated lists of pubkey collections published by themselves or others, and have clients surface them for one-tap following or feed switching. Note that this kind number is already contested: see the open renumbering PR below.

- **[NIP-46](/en/topics/nip-46/) (Nostr Connect): Silent-timeout guidance** ([PR #2375](https://github.com/nostr-protocol/nips/pull/2375), merged 2026-07-15): NIP-46 is the remote-signing protocol where a client sends encrypted JSON-RPC-style requests to a signer (bunker) over relays and waits for an encrypted response. The merged change is one sentence of wire behavior: requests made with unknown or unsupported methods MUST be replied to with an error. Previously a signer that received a method it did not implement could never respond, leaving the client hanging until its own timeout fired with no way to distinguish "unsupported method" from "signer offline." The mandated error reply lets clients fail fast and surface a meaningful error before the local timeout.

**Open PRs and Discussions:**

- **kind:10011 renumbering to kind:10021** ([PR #2417](https://github.com/nostr-protocol/nips/pull/2417)): Moves the newly merged favorite follow sets list from `kind:10011` to `kind:10021`, because `10011` is already in use elsewhere. The renumbering PR was open within days of the original merge, so clients implementing favorite follow sets should track this PR and target the final number, not `10011`.

- **[NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect): Core simplification** ([PR #2419](https://github.com/nostr-protocol/nips/pull/2419)): Proposes narrowing NIP-47, the wallet-connect protocol that lets apps request Lightning payments from a remote wallet over Nostr, into a smaller core spec. Optional and more specialized functionality would move out of `47.md` into a dedicated extensions repository, [nostr-wallet-connect/nwc](https://github.com/nostr-wallet-connect/nwc), where extension specs can evolve independently of the core. The stated goal is to keep the core small, stable, and easy to implement, following the direction agreed in earlier NWC calls of separating a minimal wallet-connect layer from richer optional behaviors. Given how widely NIP-47 is deployed across wallets and apps, anyone that speaks NWC should track the restructuring discussion.

- **Trusted Relay Assertions (draft, no number assigned)** ([PR #2418](https://github.com/nostr-protocol/nips/pull/2418)): Proposes a standard for publishing trust evaluations about Nostr relays, positioned as the "what we conclude" layer alongside [NIP-11](/en/topics/nip-11/) (what a relay claims about itself) and [NIP-66](/en/topics/nip-66/) (what monitors measured). Assertion providers would compute trust scores from observed metrics, operator reputation, and user reports; clients would query these assertions when choosing which relays to connect to. The draft introduces `kind:30385` (addressable Trusted Relay Assertion, carrying score, reliability, quality, accessibility, operator, policy, and jurisdiction tags), `kind:10385` (replaceable Trusted Provider List, the user's chosen assertion providers), and reuses [NIP-32](/en/topics/nip-32/) labels for relay and operator reports. No NIP number has been assigned yet; this is an early-stage draft.

- **AND operator for filters ("NIP-91", proposed, number not yet in the repo)** ([PR #2252](https://github.com/nostr-protocol/nips/pull/2252)): Under NIP-01, tag filters are OR-only: a filter `"#t": ["meme", "cat"]` matches events with either tag. This proposal adds an `&` modifier for indexable tags, so `"&t": ["meme", "cat"]` returns only events carrying both tags. Relays perform the intersection server-side and return a narrower result. Compatibility rules give AND precedence over OR, ignore AND values in OR on supporting relays, and require clients to include standard `#` OR tags for relays that lack the extension; clients intersect those broader results locally. This PR reopens an earlier proposal and lists relay implementations including a nostr-rs-relay docker image, netstr, and a Snort worker relay. NIP-91 appears only in the PR branch and remains absent from the repository README's NIP index, so the number is provisional.

- **Nostr web applets ("NIP-5D", proposed, number not yet in the repo)** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): Defines a `postMessage` protocol for sandboxed web applications ("napplets") running in iframes or webviews to communicate with a hosting application ("shell"). The spec is deliberately a thin core: it specifies the message envelope, sandbox rules (napplet iframes MUST use `sandbox="allow-scripts"` without `allow-same-origin`, and shells MUST NOT expose `window.nostr` NIP-07 inside the iframe), sender identification via the unforgeable `MessageEvent.source` window reference, not `event.origin`, and manifest-based capability negotiation. Actual protocol messages for signing, relay access, storage, and inter-napplet communication are delegated to NAP (Nostr Applet Protocol) extension specs, each owning a capability domain, with signing and encryption always mediated by the shell so keys never enter the sandbox. The proposal depends on the NIP-5A napplet manifest spec and is timely this week: Amethyst's v1.13.0 pre-release work includes napplet account isolation, making client-side napplet hosting an active implementation area. As with "NIP-91" above, the 5D number is provisional.

---

## NIP Deep Dive: NIP-42 and NIP-43

Running a relay that is not open to everyone used to mean inventing everything yourself. A paid or invite-only relay operator had to maintain a whitelist out of band, usually a text file of pubkeys collected over DMs, with no standard way to tell a connected client "prove who you are" and no standard way for a user to ask for admission or know whether they were a member. Every relay that wanted gated reads or gated writes built its own private mechanism, and clients could not interoperate with any of them. [NIP-42](/en/topics/nip-42/) standardizes the proof-of-identity half of that problem, and [NIP-43](/en/topics/nip-43/) standardizes the membership half. This week nostream, the TypeScript relay, merged the pair end to end: [PR #702](https://github.com/Cameri/nostream/pull/702) restricts reads of encrypted kinds to authenticated recipients, and [PR #676](https://github.com/Cameri/nostream/pull/676) adds join and leave request event strategies, both merged on July 20.

### NIP-42: Authentication of clients to relays

[NIP-42](/en/topics/nip-42/) answers one question: who is on this connection? A relay that wants to gate reads or writes sends an `AUTH` message carrying a challenge string, at connect time or on demand when a request needs authentication. A client replies with its own `AUTH` message containing a signed ephemeral event, kind 22242, and the relay answers with an `OK` message exactly as if the auth event were an ordinary write. Authentication then holds for the duration of the connection. A sequence of `AUTH` messages can authenticate several pubkeys on one connection.

Here is the signed auth event:

```json
{
  "id": "4ef6f2c0b1a84c9a3d0f9c58e2a1b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0",
  "pubkey": "c308e1f882c1f1dff2a43d4294239ddeec04e575f2d1aad1fa21ea7684e61fb5",
  "created_at": 1753195800,
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com/"],
    ["challenge", "challengestringhere"]
  ],
  "content": "",
  "sig": "8b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1"
}
```

The `pubkey` is the identity being proved, since the relay verifies the `sig` over the event `id` against it. Kind 22242 sits in the ephemeral range: the event is a connection-level credential, and relays must never store it or broadcast it to other clients. A `relay` tag binds the signature to one relay URL so a captured auth event cannot be replayed against a different relay, while the `challenge` tag binds it to the specific challenge string issued on this connection and blocks later replay. Its `created_at` must be close to the current time, within roughly a ten-minute window, so a stale auth event expires on its own. An empty `content` field confirms that nothing is being published.

The spec also defines two machine-readable prefixes that make gating visible to clients. A relay that rejects a subscription because the client has not authenticated yet answers with a `CLOSED` message starting with `auth-required:`, and a rejected write gets an `OK` with the same prefix. A client that authenticated but still lacks permission for the action gets `restricted:` instead. That distinction is what [nostream's PR #702](https://github.com/Cameri/nostream/pull/702) builds on: reads of encrypted kinds can now be closed with `auth-required:` until the requesting pubkey proves it is the recipient.

### NIP-43: Relay Access Metadata and Requests

[NIP-43](/en/topics/nip-43/) answers the follow-up question: now that the relay knows who you are, what are you allowed to do? Where NIP-42 is a handshake on a live connection, NIP-43 is a set of published events that describe membership state and let users ask to change it. On the relay side, a kind 13534 event, signed by the pubkey in the relay's [NIP-11](/en/topics/nip-11/) `self` field, lists one `member` tag per pubkey, with optional role arguments pointing at role definitions published as kind 33534. Kind 8000 announces a member being added and kind 8001 announces a removal, both signed by the same relay key with a `p` tag for the affected member. On the user side, kind 28934 is a join request carrying an invite code in a `claim` tag, kind 28935 is an ephemeral invite-code event the relay generates on the fly when a user requests a claim, and kind 28936 is a leave request.

A join request looks like this:

```json
{
  "id": "9f0e1d2c3b4a59687a6b5c4d3e2f1098a7b6c5d4e3f2019a8b7c6d5e4f3021a9b8",
  "pubkey": "ee1d336e13779e4d4c527b988429d96de16088f958cbf6c074676ac9cfd9c958",
  "created_at": 1753195900,
  "kind": 28934,
  "tags": [
    ["-"],
    ["claim", "invite-code-from-operator"]
  ],
  "content": "",
  "sig": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2"
}
```

The `pubkey` is the user asking for admission, and kind 28934 marks the event as a join request. Its `-` tag is the [NIP-70](/en/topics/nip-70/) protected-event marker, telling relays to accept the event only from its author. A `claim` tag carries the invite code obtained out of band, and `created_at` must be now, plus or minus a few minutes, so an old request cannot be replayed. Relays answer the claim with an `OK` message, reuse the NIP-42 `restricted:` prefix for failures such as an expired or invalid code, update the kind 13534 list, and may publish a kind 8000 add-member event. Membership is deliberately not derived from a single event: the spec treats the relay-signed list as one input, and a client deciding whether someone is currently a member should consult both the relay's kind 13534 and the member's own events. Clients must only send join, invite, or leave requests to relays that advertise this NIP in the `supported_nips` section of their NIP-11 document, and [nostream's PR #676](https://github.com/Cameri/nostream/pull/676) is the relay-side machinery that turns those request kinds into actual membership changes.

### History

NIP-42 is the older of the two by a wide margin. It entered the NIPs repository on January 2, 2023, in [commit c80be21c](https://github.com/nostr-protocol/nips/commit/c80be21c), where fiatjaf drastically simplified an earlier relay-auth NIP drafted by semisol, collapsing a more complex challenge scheme into the single signed ephemeral event the spec still uses today. NIP-43 arrived much later, on October 30, 2025, when hodlbod's [PR #1079](https://github.com/nostr-protocol/nips/pull/1079) merged, adding relay access metadata and requests built directly on top of NIP-42's `restricted:` prefix. The two-and-a-half-year gap reflects how long paid and private relay operators used ad-hoc whitelists before the membership layer got a standard.

### Implementations

On the relay side, [nostream](https://github.com/Cameri/nostream) now ships both halves after this week's merges. [strfry](https://github.com/hoytech/strfry) implements NIP-42, validating kind 22242 auth events in its ingester and issuing challenges from its config. [nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay) handles the AUTH handshake in its connection layer with tests covering the challenge and timestamp window. [khatru](https://github.com/fiatjaf/khatru), the Go relay framework, tracks the authenticated pubkey per connection so policies can gate reads and writes on it. On the client side, [Amethyst](https://github.com/vitorpamplona/amethyst) signs kind 22242 responses to relay challenges, including per-stream auth for its Concord encrypted communities. The two NIPs split access control along a clean line: NIP-42 is proof of identity, scoped to one connection, one challenge, and a few minutes of validity, and it says nothing about policy. NIP-43 is policy, expressed as ordinary relay events: who is a member, who was added or removed, and how a user requests those transitions. The gap implementers should keep in mind is that nothing yet standardizes finer-grained permissions beyond NIP-43's optional role metadata, so any relay doing more than a binary member/non-member split is designing that layer on its own.

---

That's it for this week. Building something or have news to share? Reach out via NIP-17 DM or find us on Nostr.
