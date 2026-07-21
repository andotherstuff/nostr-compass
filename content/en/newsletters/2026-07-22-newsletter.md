---
title: "Nostr Compass #32"
date: 2026-07-22
publishDate: 2026-07-22
draft: true
type: newsletters
description: "IndieSats drops its publisher role and relaunches as open Nostr music infrastructure, NIP-29 relay groups get five merged spec PRs with Nostrord v2.3.0 shipping the client side, Zapstore 1.1.0 makes the device key portable and the catalog relay-native, favorite follow sets merge and immediately renumber, and the Iris ecosystem ships a pubsub library, a browser FIPS runtime, and nostr-social-graph 2.0."
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** [IndieSats](#indiesats-drops-its-publisher-role-and-relaunches-as-open-nostr-music-infrastructure) retires key custody, its whitelist, and its mandatory revenue cut, relaunching as an open relay, player, and discovery layer where artists publish under their own keys. [NIP-29 relay groups](#nip-29-relay-groups-get-a-full-spec-week-with-a-shipping-client-landing-the-same-features) land five merged spec PRs covering subgroups, message pinning, banners, and invite codes, with [Nostrord v2.3.0](#nostrord-v230-ships-the-client-side-of-this-weeks-nip-29-spec-work) shipping the matching client features the same week. [Zapstore 1.1.0](#zapstore-110-makes-the-device-key-portable-and-the-app-catalog-relay-native) introduces a portable encrypted device key with Amber backup and moves the app catalog onto relays as kind:10067 events. The [favorite-follow-sets list kind](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house) merges and opens a renumbering PR within days. And the [Iris ecosystem](#the-iris-ecosystem-ships-a-pubsub-library-a-browser-fips-runtime-and-a-social-graph-20-in-one-week) ships nostr-pubsub, the fips-ts browser runtime, and nostr-social-graph 2.0.0 in a single week.

Tagged releases bring [Amber v6.3.0](#amber-v630-groups-bunker-signing-approvals-and-adds-expert-list-support) with grouped bunker-signing approvals, [Wisp v1.2.0](#wisp-v120-adds-a-multi-account-switcher-and-collapsible-reply-threads) with a multi-account switcher, [Sonar v0.1-alpha.11](#sonar-v01-alpha11-continues-the-alpha-line) continuing the alpha line, and new project [ClipRelay v0.1.2](#cliprelay-v012-new-project-syncs-clipboards-across-devices-over-nostr-relays) syncing clipboards over Nostr relays.

On the unreleased side, [nostream](#nostream-merges-nip-42-read-restriction-and-nip-43-membership-strategies) merges the NIP-42/NIP-43 access-control pair, and [Amethyst](#amethyst-lands-v1130-pre-release-qa-on-napplet-isolation-and-concord-authority) lands v1.13.0 pre-release QA across 81 merged PRs.

The NIPs repository merges five PRs this week, including the [NIP-29 cluster](#protocol-work-and-nip-updates) and [kind:10011 favorite follow sets](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house), and opens a [NIP-47 simplification debate](#open-nip-47-simplification-proposal). The Deep Dive covers [NIP-42 and NIP-43, the relay access-control pair](#nip-deep-dive).

---

## Lead stories

### IndieSats drops its publisher role and relaunches as open Nostr music infrastructure

[IndieSats](https://zapstore.dev) is a Nostr-based music platform that until this week acted as a publisher: it held keys for artists, ran a whitelist, and took a mandatory 2% cut of revenue. In a [pivot announcement published as a kind:1 note](https://njump.me/nevent1qqsr4awwnfndnnz77zanjxarw6nd0uld0ckayxp2navz0u9tzzwfweqpzamhxue69uhhyetvv9ujuurjd9kkzmpwdejhgtczyquwq70hxz22lzytw65rnnjewg0lj8a74khxa8h9j47q38pdnqy3kqcyqqqqqqgz8083u) on 2026-07-20, the project retired all three of those roles at once. The relaunched platform is three pieces of open infrastructure instead: an open relay, a player, and a discovery layer, with artists publishing music under their own Nostr profiles instead of a platform-custodied identity. Revenue splits become opt-in, no longer mandatory, and the platform now honors [NIP-09](/en/topics/nip-09/) kind:5 deletion requests so artists can remove their work. Corroborating Zapstore updates v1.1.1 through v1.1.3 shipped in the same week, so the pivot arrived with working client code behind it. For a space that usually talks about protocols replacing platforms, this is a live case of a platform voluntarily disassembling itself into protocol pieces.

### NIP-29 relay groups get a full spec week, with a shipping client landing the same features

Relay-based group chat had an unusually heavy spec week. Five [NIP-29](/en/topics/nip-29/) (relay-based groups) pull requests merged between July 15 and 17: [subgroups with parent/child tags and non-inherited membership](https://github.com/nostr-protocol/nips/pull/2319), [message pinning via a new kind:9010 pin-list moderation event and a kind:39005 pinned-events group event](https://github.com/nostr-protocol/nips/pull/2379), a [follow-up allowing `a`-tag addressable events in pin lists](https://github.com/nostr-protocol/nips/pull/2416), a [banner tag for group metadata](https://github.com/nostr-protocol/nips/pull/2383), and an [invite-code suffix for group join links](https://github.com/nostr-protocol/nips/pull/2380). The subgroups change is the largest: it lets a relay advertise support for nested groups under a parent group while keeping membership lists scoped per group, so a large community can split into channels without inheriting the parent's entire member set. The pinning pair gives group admins a spec-backed way to surface canonical posts, replacing the ad hoc client-side conventions groups had been using. Spec and implementation landed together this week: [Nostrord](https://github.com/nostrord/nostrord), a NIP-29 group-chat client for Android, iOS, web, and desktop, shipped [v2.3.0](https://github.com/nostrord/nostrord/releases/tag/v2.3.0) with wired-up NIP-29 moderation actions on all UIs, consent-gated group invites with cross-relay detection ([PR #195](https://github.com/nostrord/nostrord/pull/195)), cross-platform [NIP-51](/en/topics/nip-51/) mute lists ([PR #188](https://github.com/nostrord/nostrord/pull/188)), and Tor .onion relay support. Group chat on Nostr now has both a deeper spec and a client exercising most of it, which shortens the feedback loop for everyone else building on relay groups.

### Zapstore 1.1.0 makes the device key portable and the app catalog relay-native

[Zapstore](https://github.com/zapstore/zapstore) is a Nostr-native app store where releases are signed by developer keys and no central operator vouches for them. [Version 1.1.0](https://github.com/zapstore/zapstore/releases/tag/1.1.0), the first release covered here since early March, reworks how a device proves its identity: the device key is now portable, encrypted, and backable up through [Amber](https://github.com/greenart7c3/Amber), the Android [NIP-46](/en/topics/nip-46/) remote signer, so a user moving phones no longer starts over as an unknown device. The release also adds opt-in background auto-updates for installed apps, closing the gap with conventional app stores for users who want it. On the protocol side, the app catalog itself moves onto relays: catalog data is published as device-signed kind:10067 events, and the store gains [NIP-56](/en/topics/nip-56/) verified reporting so users can flag problematic apps in a way other clients can consume. Before any install proceeds, Zapstore now verifies the C1 proof attached to a release, tightening the link between what a developer signed and what a device runs.

### The favorite-follow-sets list kind merges and immediately moves house

A spec-coordination story played out inside a single week. [PR #2413](https://github.com/nostr-protocol/nips/pull/2413) merged on July 15, standardizing a replaceable list kind for favorite follow sets under [NIP-51](/en/topics/nip-51/) (lists): a dedicated kind where clients can publish a user's curated sets of followed accounts instead of overloading generic list kinds. Within days it turned out the assigned kind:10011 was already in use elsewhere, so a follow-up [PR #2417](https://github.com/nostr-protocol/nips/pull/2417) is now open to renumber the list to kind:10021. Nothing has shipped against the merged kind yet, which makes this the cheap moment to renumber; once clients start publishing kind:10011 events, the collision would get expensive to unwind. Developers building list-consuming features should track the renumbering PR, not the merged text, until it resolves.

### The Iris ecosystem ships a pubsub library, a browser FIPS runtime, and a social-graph 2.0 in one week

Three releases from the Iris orbit landed together, and they interlock. [nostr-pubsub](https://github.com/mmalmi/nostr-pubsub) is a transport-neutral publish/subscribe library for Nostr events; its [first tracked releases, v0.1.3 through v0.5.2](https://github.com/mmalmi/nostr-pubsub/releases), deliver a browser relay carrier built on nostr-tools' SimplePool, event verification at the transport boundary so invalid signatures never reach subscribers, and bounded historical queries. [fips-ts](https://github.com/mmalmi/fips-ts) brings [FIPS](/en/topics/fips/), the Noise-over-secp256k1 peer transport previously available as a Rust stack, into the browser as a TypeScript runtime: releases [0.0.24 through 0.0.30](https://github.com/mmalmi/fips-ts/releases) added a WebRTC datachannel carrier, Nostr-based signaling for peer discovery, a recent-peer cache, and an IndexedDB adapter for browser storage, and the runtime is wire-compatible with the reference Rust implementation. The third piece, [nostr-social-graph v2.0.0](https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.0), is a major version of the social-graph library: signed roster operations for Nostr identity graphs, device-approval flows bootstrapped from a canonical three-field URI, and FIPS transport identity facets with shared Rust and TypeScript test vectors. The connective framing is the [Iris Stack](https://stack.iris.to/), the project's integration lab tying these libraries together with Blossom, Hashtree, and encrypted messaging; the stack site shipped no release of its own, but the three components it assembles all shipped in the same week. Taken together, a web app can now discover peers over Nostr, open an encrypted FIPS channel to them, and maintain a signed social graph, all in TypeScript.

---

## Tagged releases

### Amber v6.3.0 groups bunker signing approvals and adds Expert List support

[Amber](https://github.com/greenart7c3/Amber) is an Android [NIP-46](/en/topics/nip-46/) remote signer. [v6.3.0](https://github.com/greenart7c3/Amber/releases/tag/v6.3.0) adds grouped multi-request approval for bunker signing so a batch of pending signature requests can be reviewed and approved together instead of one prompt at a time. The release also adds support for Expert List (kind 12022) and Expert Pack (kind 32022) events, a privacy mode that hides sensitive content on screen, and a change to fetch an account's [NIP-65](/en/topics/nip-65/) relay list before its profile metadata so signer flows start from the user's actual relay set. This follows the v6.2.x line covered in the 2026-07-08 issue.

### Nostrord v2.3.0 ships the client side of this week's NIP-29 spec work

[Nostrord v2.3.0](https://github.com/nostrord/nostrord/releases/tag/v2.3.0) is the shipped half of the NIP-29 cluster covered in this week's News section, and adds [PR #192](https://github.com/nostrord/nostrord/pull/192) (moderation wiring) beyond what the lead story lists. The release follows v2.2.0's DM controls covered in #31.

### Wisp v1.2.0 adds a multi-account switcher and collapsible reply threads

[Wisp](https://github.com/barrydeen/wisp) is a Nostr client. [v1.2.0](https://github.com/barrydeen/wisp/releases/tag/v1.2.0) adds a multi-account switcher, collapsible reply threads for long conversations, stripping of tracking parameters from note links, and a wallet transaction-history view. The release follows the Wisp update covered in the 2026-07-08 issue.

### ClipRelay v0.1.2 (new project) syncs clipboards across devices over Nostr relays

[ClipRelay](https://github.com/tajava2006/cliprelay) is a newly launched app, tracked for the first time this week via its [Zapstore](https://zapstore.dev) listing. [v0.1.2](https://github.com/tajava2006/cliprelay) syncs clipboard contents across a user's devices using Nostr relays as the transport, a simple and legible Nostr-native utility. This is ClipRelay's first appearance in the newsletter.

### Sonar v0.1-alpha.11 continues the alpha line

[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar), last week's lead story, cut [v0.1-alpha.11](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.11) with work on the Rust mesh link engine, BLE and mesh fixes, and relay diagnostics; an incremental follow-up to the alpha line covered in #31.

### nostr-social-graph 2.0.0 and the rest of the week's smaller launches

[nostr-social-graph 2.0.0](https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.0), the Iris-ecosystem social-graph library from this week's News section, is a major-version bump adding signed Nostr identity roster operations, device-approval flows with a canonical three-field bootstrap URI, and FIPS transport identity facets with shared Rust/TypeScript test vectors. Breaking changes for 1.x consumers. Beyond the cluster, three smaller launches deserve one line each: [noscall v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release), the Nostr calling app, migrated its push notifications to UnifiedPush, keeping call signaling off Google's push infrastructure; [nostr-vpn v4.1.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.1.1), a mesh VPN that uses Nostr for signaling, launched on Zapstore; and two new apps debuted there as well: StableKraft, a Nostr-plus-Lightning music and podcast aggregator, and Hakari, an encrypted Nostr backup for a weight logger.

### Amethyst lands v1.13.0 pre-release QA on napplet isolation and Concord authority

[Amethyst](https://github.com/vitorpamplona/amethyst) merged 81 PRs this week ahead of its v1.13.0 release. [PR #3650](https://github.com/vitorpamplona/amethyst/pull/3650) is a pre-release QA pass covering napplet account isolation, Concord authority fixes, and around 30 other fixes, with further v1.13.0 prep PRs landing through 07-21. This continues #31's coverage of Amethyst's clean-room Concord client implementation, tightening the authority and isolation behavior of that work before it ships tagged.

---

## Unreleased changes

### nostream merges NIP-42 read restriction and NIP-43 membership strategies

[nostream](https://github.com/Cameri/nostream), the TypeScript relay implementation, merged seven PRs this week without cutting a release. The headline pair is [PR #702](https://github.com/Cameri/nostream/pull/702), which restricts reads of encrypted event kinds to authenticated recipients under [NIP-42](/en/topics/nip-42/), and [PR #676](https://github.com/Cameri/nostream/pull/676), which adds join and leave request strategies under [NIP-43](/en/topics/nip-43/). Together they give relay operators a working authentication-plus-membership access-control stack; this week's NIP Deep Dive walks through exactly that handshake.

### Open: NIP-47 simplification proposal

[PR #2419](https://github.com/nostr-protocol/nips/pull/2419), opened by frnandu, proposes simplifying the [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect) core spec and moving functionality into extensions. NWC is implemented across a large share of Nostr wallets and apps, so a structural split of its core spec deserves attention even before any merge decision. Client and wallet authors that implement NIP-47 should weigh in while the proposal is young.

### FIPS v0.4.1 tightens the transport the Iris ecosystem builds on

[jmcorgan/fips](https://github.com/jmcorgan/fips) shipped [v0.4.1](https://github.com/jmcorgan/fips/releases/tag/v0.4.1), a maintenance release capping antipoison state, fixing convergence and MTU handling, and cutting CPU use. On its own this is plumbing, but this week it is connective tissue: the browser TypeScript runtime [fips-ts](https://github.com/mmalmi/fips-ts) from the Iris-ecosystem cluster in this issue's News section is wire-compatible with this Rust transport, so fixes here propagate directly to what the browser runtime interoperates with.

### Open: Trusted Relay Assertions draft

[PR #2418](https://github.com/nostr-protocol/nips/pull/2418), opened by Wisp contributor Letdown2491, is a new draft proposal for publishing [Trusted Relay Assertions](/en/topics/trusted-relay-assertions/): [NIP-66](/en/topics/nip-66/) metrics, operator reputation, and reports as relay-queryable data. No NIP number is assigned yet and the proposal is early, but it aims at a real gap, giving clients a standard way to reason about which relays to trust, replacing hardcoded operator lists.

---

## Protocol work and NIP updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-29](/en/topics/nip-29/) (Relay-based Groups): Subgroups** ([PR #2319](https://github.com/nostr-protocol/nips/pull/2319), merged 2026-07-16): NIP-29 defines relay-hosted groups where membership, roles, and chat history live on a single relay as addressable `kind:39000`-series events, with moderation actions carried by `kind:9000`-series admin events. This PR lets a group declare itself a subgroup by adding a `parent` tag to its metadata, pointing at the `d` identifier of another group on the same relay. Subgroups are ordinary groups in every other respect: membership does not cascade (joining a parent grants no membership in any child), admin roles do not inherit (each subgroup's `kind:39001` admins list is authoritative for its own scope), and each subgroup keeps its own independent `kind:9000`/`kind:9001` member events. Relays that support the hierarchy advertise it in their NIP-11 relay information document under a `nip29` object with `"subgroups": true`, so clients can discover the capability before attempting to create nested communities.

- **[NIP-29](/en/topics/nip-29/): Message pinning** ([PR #2379](https://github.com/nostr-protocol/nips/pull/2379), merged 2026-07-15; [PR #2416](https://github.com/nostr-protocol/nips/pull/2416), merged 2026-07-17): Group admins can now pin messages inside a relay-based group. The mechanism adds a new moderation event, `kind:9010` `update-pin-list`, which carries the full ordered pin list as `e` tags referencing regular event ids, and a new optional group-level event, `kind:39005` *group pinned events*, which the relay regenerates to mirror the most recent accepted pin list. Because each `kind:9010` replaces the whole list instead of toggling single entries, pinning, unpinning, reordering, and clearing pins are all expressed by submitting one new list. The follow-up PR #2416 extends the format so `a` tags are also accepted in the pin list, letting admins pin addressable events (long-form posts, wiki pages, and other parameterized replaceable content) alongside ordinary chat messages. Relays may cap the number of pins, and the merged spec text recommends displaying pins in the order the tags appear.

- **[NIP-29](/en/topics/nip-29/): Banner tag and invite-code suffix** ([PR #2383](https://github.com/nostr-protocol/nips/pull/2383), merged 2026-07-16; [PR #2380](https://github.com/nostr-protocol/nips/pull/2380), merged 2026-07-16): Two display-and-onboarding additions to group metadata. PR #2383 adds an optional `banner` tag to the `kind:39000` group metadata event, joining the existing `name`, `picture`, and `about` fields so clients can render a header image for a group page. PR #2380 defines an invite-code suffix for group share links: an invite code may be appended to the group's `naddr` identifier as `naddr1...?invite=<code>`. Because the bech32 character set does not include `?`, the portion before the suffix remains a valid naddr on its own, so clients that do not understand the extension can still resolve the group. Clients that do understand it pre-fill the `code` tag on the `kind:9021` join request, which pairs with the existing `kind:9009` `create-invite` moderation event to simplify admission to closed groups.

- **[NIP-51](/en/topics/nip-51/) (Lists): Favorite follow sets, kind:10011** ([PR #2413](https://github.com/nostr-protocol/nips/pull/2413), merged 2026-07-15): NIP-51 defines the standard list kinds, split between replaceable `kind:10000`-series lists (one per user) and addressable `kind:30000`-series sets (many per user, keyed by `d` tag). This PR adds `kind:10011`, *favorite follow sets*, a standard replaceable list whose `a` tags point at `kind:30000` follow sets. The mirror of `kind:10012` (relay feeds), which holds `a` tags referencing `kind:30002` relay sets, the new kind lets a user bookmark named follow sets, such as curated lists of pubkey collections published by themselves or others, and have clients surface them for one-tap following or feed switching. Note that this kind number is already contested: see the open renumbering PR below.

- **[NIP-46](/en/topics/nip-46/) (Nostr Connect): Silent-timeout guidance** ([PR #2375](https://github.com/nostr-protocol/nips/pull/2375), merged 2026-07-15): NIP-46 is the remote-signing protocol where a client sends encrypted JSON-RPC-style requests to a signer (bunker) over relays and waits for an encrypted response. The merged change is one sentence of wire behavior: requests made with unknown or unsupported methods MUST be replied to with an error. Previously a signer that received a method it did not implement could never respond, leaving the client hanging until its own timeout fired with no way to distinguish "unsupported method" from "signer offline." The mandated error reply lets clients fail fast and surface a meaningful message to the user instead of spinning indefinitely.

**Open PRs and Discussions:**

- **kind:10011 renumbering to kind:10021** ([PR #2417](https://github.com/nostr-protocol/nips/pull/2417)): Moves the newly merged favorite follow sets list from `kind:10011` to `kind:10021`, because `10011` is already in use elsewhere. The renumbering PR was open within days of the original merge, so clients implementing favorite follow sets should track this PR and target the final number, not `10011`.

- **[NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect): Core simplification** ([PR #2419](https://github.com/nostr-protocol/nips/pull/2419)): Proposes narrowing NIP-47, the wallet-connect protocol that lets apps request Lightning payments from a remote wallet over Nostr, into a smaller core spec. Optional and more specialized functionality would move out of `47.md` into a dedicated extensions repository, [nostr-wallet-connect/nwc](https://github.com/nostr-wallet-connect/nwc), where extension specs can evolve independently of the core. The stated goal is to keep the core small, stable, and easy to implement, following the direction agreed in earlier NWC calls of separating a minimal wallet-connect layer from richer optional behaviors. Given how widely NIP-47 is deployed across wallets and apps, anyone that speaks NWC should track the restructuring discussion.

- **Trusted Relay Assertions (draft, no number assigned)** ([PR #2418](https://github.com/nostr-protocol/nips/pull/2418)): Proposes a standard for publishing trust evaluations about Nostr relays, positioned as the "what we conclude" layer alongside [NIP-11](/en/topics/nip-11/) (what a relay claims about itself) and [NIP-66](/en/topics/nip-66/) (what monitors measured). Assertion providers would compute trust scores from observed metrics, operator reputation, and user reports; clients would query these assertions when choosing which relays to connect to. The draft introduces `kind:30385` (addressable Trusted Relay Assertion, carrying score, reliability, quality, accessibility, operator, policy, and jurisdiction tags), `kind:10385` (replaceable Trusted Provider List, the user's chosen assertion providers), and reuses [NIP-32](/en/topics/nip-32/) labels for relay and operator reports. No NIP number has been assigned yet; this is an early-stage draft.

- **AND operator for filters ("NIP-91", proposed, number not yet in the repo)** ([PR #2252](https://github.com/nostr-protocol/nips/pull/2252)): Under NIP-01, tag filters are OR-only: a filter `"#t": ["meme", "cat"]` matches events with either tag. This proposal adds an `&` modifier for indexable tags, so `"&t": ["meme", "cat"]` returns only events carrying both tags, letting relays do the intersection server-side instead of clients over-fetching and filtering locally. The rules specify that AND takes precedence over OR, that tag values used in AND should be ignored in OR by supporting relays, and that clients MUST also include the standard `#` OR tags for compatibility with relays that do not support the extension (those relays return the broader OR result, which the client intersects locally). The PR is a re-opened continuation of an earlier proposal and lists relay implementations including a nostr-rs-relay docker image, netstr, and a Snort worker relay. The NIP-91 number appears only in the PR branch; it is not yet in the repository README's NIP index, so treat the number as provisional.

- **Nostr web applets ("NIP-5D", proposed, number not yet in the repo)** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): Defines a `postMessage` protocol for sandboxed web applications ("napplets") running in iframes or webviews to communicate with a hosting application ("shell"). The spec is deliberately a thin core: it specifies the message envelope, sandbox rules (napplet iframes MUST use `sandbox="allow-scripts"` without `allow-same-origin`, and shells MUST NOT expose `window.nostr` NIP-07 inside the iframe), sender identification via the unforgeable `MessageEvent.source` window reference, not `event.origin`, and manifest-based capability negotiation. Actual protocol messages for signing, relay access, storage, and inter-napplet communication are delegated to NAP (Nostr Applet Protocol) extension specs, each owning a capability domain, with signing and encryption always mediated by the shell so keys never enter the sandbox. The proposal depends on the NIP-5A napplet manifest spec and is timely this week: Amethyst's v1.13.0 pre-release work includes napplet account isolation, making client-side napplet hosting an active implementation area. As with "NIP-91" above, the 5D number is provisional.

---

## NIP Deep Dive

This week nostream, the TypeScript relay implementation, merged two pull requests that implement the relay access-control stack end to end: [PR #702](https://github.com/Cameri/nostream/pull/702) restricts reads of encrypted kinds to authenticated recipients, and [PR #676](https://github.com/Cameri/nostream/pull/676) adds join and leave request strategies. Those two changes land on two different NIPs that are designed to work as a pair, so this issue's Deep Dive covers them together.

### NIP-42: Authentication of clients to relays

[NIP-42 (client authentication to relays)](/en/topics/nip-42/) answers one question: who is connected? A relay that wants to gate reads or writes sends an `AUTH` message containing a challenge string. The client signs an ephemeral kind 22242 event that binds its pubkey to that challenge and to the relay URL, and returns it inside an `AUTH` message of its own. The relay answers with an `OK`, exactly as if the auth event were a normal write. From that point on, the connection is treated as authenticated for the duration of the session.

The signed auth event looks like this:

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

Three details do the security work. The `challenge` tag binds the event to the specific challenge the relay issued, blocking replay of a captured auth. The `relay` tag binds the event to one relay URL, blocking reuse of the same signature elsewhere. The `created_at` timestamp must be within about ten minutes of now, so a stale auth event expires on its own. Relays must never broadcast kind 22242 to other clients; it exists only as a connection-level credential. The spec also defines two machine-readable prefixes that make gating visible to clients: `auth-required:` in an `OK` or `CLOSED` message means the client has not authenticated yet, and `restricted:` means it authenticated but still lacks permission for that action. That distinction is what [nostream's PR #702](https://github.com/Cameri/nostream/pull/702) builds on: reads of encrypted kinds can now be closed with `auth-required:` until the requesting pubkey proves it is the recipient.

### NIP-43: Relay Access Metadata and Requests

[NIP-43 (relay access metadata and requests)](/en/topics/nip-43/) answers the follow-up question: now that the relay knows who you are, what are you allowed to do? Where NIP-42 is a handshake on a live connection, NIP-43 is a set of published events that describe membership state and let users ask to change it. A relay publishes a kind 13534 membership list signed by the pubkey in its NIP-11 `self` field, with one `member` tag per pubkey. Kind 8000 announces a member being added, kind 8001 announces a removal. On the user side, kind 28934 is a join request carrying an invite code in a `claim` tag, kind 28935 is an ephemeral invite code a relay can hand out on demand, and kind 28936 is a leave request.

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

The relay answers the claim with an `OK` message, reusing the NIP-42 `restricted:` prefix for failures such as an expired or invalid code, and should then update its kind 13534 list and optionally publish a kind 8000 add-member event. Membership state is deliberately not derived from a single event: a client deciding whether someone is currently a member is expected to consult both the relay-signed list and the member's own events. Clients must only send join, invite, or leave requests to relays that advertise this NIP in the `supported_nips` section of their NIP-11 document, and [nostream's PR #676](https://github.com/Cameri/nostream/pull/676) is the relay-side machinery that turns those request kinds into actual membership changes.

### How They Work Together

The two NIPs split access control along a clean line. NIP-42 is proof of identity, scoped to one connection, one challenge, and a few minutes of validity. It says nothing about policy. NIP-43 is policy, expressed as regular relay events: who is a member, who was added, who was removed, and how a user requests any of those transitions. A private or paid relay uses them in sequence. The user obtains an invite code out of band, submits a kind 28934 join request, and the relay records membership with an updated kind 13534 and a kind 8000. On every subsequent connection, the relay challenges with `AUTH`, the client answers with kind 22242, and only then does the relay consult the NIP-43 membership state to decide what that authenticated pubkey may read or write. Reads of restricted kinds return `auth-required:` before the handshake and `restricted:` after it if the authenticated key is not on the list.

That two-layer shape is what nostream shipped this week, and it matches what relay groups and invite-only relays have been converging on: one NIP for the handshake, one NIP for the roster. It also leaves a real gap that implementers should keep in mind. NIP-43 membership events tell you the state; NIP-42 tells you the key on the wire; nothing yet standardizes the finer-grained roles and permissions that relays may attach to members, beyond the optional role metadata NIP-43 sketches. For now, any relay doing more than a binary member/non-member split is designing that layer on its own.

---

That's it for this week. Building something or have news to share? Reach out via NIP-17 DM or find us on Nostr.
