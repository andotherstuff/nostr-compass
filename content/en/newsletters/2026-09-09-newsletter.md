---
title: "Nostr Compass #39"
date: 2026-09-09
publishDate: 2026-09-09
draft: false
type: newsletters
description: "Nostr Compass #39 follows signed git workflows, browser publishing, self-hosted live streams, community relay consent, private events, focused releases, and the NIP-21/NIP-27 link contract."
---

Welcome back to [Nostr Compass](https://nostrcompass.org), your weekly guide to Nostr.

**This week:** [ngit and GitWorkshop](https://ngit.dev/v3) move signed git workflows onto Nostr and [Blossom](/en/topics/blossom/), [nsite-clay](https://github.com/jooray/nsite-clay) makes browser publishing recoverable, and [Wingman App](https://github.com/OtherStuffAI/wm-app) joins browsing, local signing, authentication, and files. [Shosho and Livelier](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) connect self-hosted streams to Nostr, [Communitator](https://github.com/dyne/communitator) makes relay templates inspectable before signing, [cal.emre.xyz](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) publishes appointment slots, and [Plektos](https://github.com/derekross/plektos/pull/16) encrypts private events. Tagged releases add recovery and privacy work in [Vector](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4), [Primal Android](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27), [LibreNostr](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0), and [SkateSpots](https://zapstore.dev/apps/org.skatespots.app). Development work spans [NIP-27](/en/topics/nip-27/) rendering, signed relay preferences in [Conduit](https://github.com/Conduit-BTC/conduit-mono/pull/397), [NIP-A3](/en/topics/nip-a3/) payment targets, and Blossom mirrors. Merged changes in the [NIPs repository](https://github.com/nostr-protocol/nips) clarify live-only subscriptions and authenticated application data. Our deep dive explains how [NIP-21](/en/topics/nip-21/) links and NIP-27 references carry Nostr profiles and events across applications.

## Top Stories

### Signed git workflows move CI, private repositories, and releases onto Nostr

The [September 8 v3 launch](https://ngit.dev/v3) brings ngit, GitWorkshop, ngit-grasp, and ngit-ci into one signed workflow. [ngit](https://ngit.dev/ngit.git) carries branches, patches, and pull requests as [NIP-34](/en/topics/nip-34/) events, while [GitWorkshop](https://ngit.dev/gitworkshop.git) provides the review interface. The launch adds ngit-ci 0.1, a self-hosted continuous-integration service whose instructions and results travel as signed Nostr events, so checks can run on maintainer-controlled hardware alongside code review.

The same release gives [ngit-grasp v3](https://ngit.dev/ngit-grasp.git) private repositories through the GRASP-08 private-repository extension and makes maintainer authority explicit. Signed release records can point to assets in [Blossom](/en/topics/blossom/), keeping both release metadata and content-addressed files outside a hosted forge. The [new documentation site](https://ngit.dev/v3) gathers the client, private-repository, CI, and web components.

### nsite-clay makes browser publishing recoverable

An [August 31 signer-prompt fix](https://github.com/jooray/nsite-clay/commit/064a0c5350f1e2b107f7d8f1de00ad75ef2e69d8), [publication recovery](https://github.com/jooray/nsite-clay/commit/d1ad514f8068eec2e007059dc62a5b6f1d240ae0), and [September 2 editing controls](https://github.com/jooray/nsite-clay/commit/8f9d7d140dd3cd3e1db8726781fcd852041713f7) make [nsite-clay](https://github.com/jooray/nsite-clay) a browser publishing tool for a single-page site. A user edits the document object model in place, serializes the result, uploads it as a content-addressed [Blossom](/en/topics/blossom/) blob, and republishes the site's [NIP-5A](/en/topics/nip-5a/) manifest. No local build or server is required.

The [browser publisher](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/deploy.html) now makes failed publication recoverable and reduces repeated signer prompts, while the [editing guide](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/guide.html) documents the loop. The result remains an ordinary NIP-5A site for existing gateways.

### Wingman App joins browsing, signing, and files

The September work adds [file pickers](https://github.com/OtherStuffAI/wm-app/commit/b0c9c03d317573adeafa92b1a56d696ad399e3ec), [profile publication](https://github.com/OtherStuffAI/wm-app/commit/f2343add8493625d62a1eb7fb76002ceab73f704), [safe signer and session restore](https://github.com/OtherStuffAI/wm-app/commit/4e278d96eb9258b89dc8b9639eac7bde3ac475c6), and [tested mobile builds](https://github.com/OtherStuffAI/wm-app/commit/60456ec0a8b4ed26ecde53812a61f95dc0bd22ac) to [Wingman App](https://github.com/OtherStuffAI/wm-app). Its Flutter shell injects a [NIP-07](/en/topics/nip-07/) provider into pages opened inside the app, while Flight Deck and Tower-backed Drive provide a work surface and file workspace beside the browser.

Wingman signs authenticated HTTP requests using [NIP-98](/en/topics/nip-98/). The [request implementation](https://github.com/OtherStuffAI/wm-app/blob/67ed27d216e528da5bb431322bd10ac15553796f/crates/wmapp-core/src/auth/nip98.rs) builds the event a server verifies before answering, giving one installed identity a consistent approval path for relay actions, web-app signing, and files.

### Shosho ships Livelier's self-hosted streams

[Shosho 1.1.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) shipped September 1 with support for [Livelier](https://github.com/r0d8lsh0p/livelier), whose [August 31 attribution update](https://github.com/r0d8lsh0p/livelier/commit/7d8abb875770289502b55c3d947987db08e206dc) identifies the bridge and Owncast source in bridged profiles. Livelier watches Owncast's public directory, checks whether a video stream is live, and then publishes an addressable `kind:30311` [NIP-53](/en/topics/nip-53/) event. Discovery travels over Nostr while video remains on the streamer's server.

Chat crosses the bridge as `kind:1311` events. The [bridge design](https://github.com/r0d8lsh0p/livelier) opens a source-side connection only while a Nostr reader is subscribed, labels derived identities, and sends transient chat to a relay that deletes it after three hours. The discovery relay accepts live-event writes only from the bridge key; the chat relay uses [NIP-42 authentication](/en/topics/nip-42/) and [NIP-70 protected-event flags](/en/topics/nip-70/).

### Communitator makes relay templates inspectable before signing

The [August 31 launch series](https://github.com/dyne/communitator/commit/520edd33a253ca3249993172fd1003c80bfd9b7c) gives [Communitator](https://github.com/dyne/communitator) canonical templates for kind `10002` relay lists, kind `10063` Blossom servers, and kind `10050` private-message inboxes. Before a signer connects, the application shows normalized endpoints, read/write permissions, event kinds, fixed publication relays, and destinations.

The [bounded signing and publication flow](https://github.com/dyne/communitator/commit/2bd04c8fab292e73fe9a4ada250c64358aee8501) separates connecting from applying. Each event is signed separately, one run uses at most four WebSocket connections, and a destination counts only after a positive [NIP-01](/en/topics/nip-01/) `OK`. Results distinguish complete, partial, failed, and cancelled delivery. Shared templates remain untrusted recommendations; the [consent surface](https://github.com/dyne/communitator#security-and-consent) explains relay and network observability.

### cal.emre.xyz publishes NIP-52 appointment availability

The public repository opened in an [initial September 2 commit](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743), followed by a signed [September 3 handler announcement](https://njump.me/6fead386f0f401c2d8641ef842ccc2ade5abb4e45d61bfd7f3872b43db04cdac) for [cal.emre.xyz](https://cal.emre.xyz). A host publishes availability as a `kind:31923` [NIP-52](/en/topics/nip-52/) event; a guest publishes a `kind:31925` RSVP.

It reads host events and accepted busy RSVPs from relays, excludes overlapping timespans, and keeps Nostr events as the scheduling record without copying them into a separate database. Hosts can sign with [NIP-07](/en/topics/nip-07/), [NIP-46](/en/topics/nip-46/), or a local key; guests can generate a separate key. Its [repository](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) also exposes the resulting `naddr` and calendar links, with email disabled by default.

### Plektos makes private events one encrypted channel

The [September 2 private-event implementation](https://github.com/derekross/plektos/pull/12) makes each [Plektos](https://github.com/derekross/plektos) gathering a private channel inside a [Concord](/en/topics/concord-protocol/) encrypted community. The guest list, RSVP roster, sign-up board, thread, contributions, cover images, edits, and deletions are encrypted together; an invitation carries only that event's key and no plaintext calendar event is published.

The [September 6 lifecycle audit](https://github.com/derekross/plektos/pull/14) anchors the event-definition id for direct lookup when more than 500 wraps exist, while retaining a paginated fallback. Invitation bundles expire 30 days after an event ends and can be disabled, but someone who already obtained a channel key can retain it. A separate [parser-security repair](https://github.com/derekross/plektos/pull/16) makes malformed type-length-value (TLV) [NIP-19](/en/topics/nip-19/) identifiers fail instead of trapping the parser.

## Tagged Releases

### Vector 0.4.4 makes encrypted-community recovery safer

[Vector 0.4.4](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) shipped August 31 with community recovery, key-rotation, moderation, and reply-routing fixes. Refounding closes a raided community to the invitation path used by attackers; replacement membership supersedes stale local state; and one unreachable member no longer freezes the roster. Empty rotations are rejected, promotions preserve online members, and operations refuse to run when required members cannot be reached.

The [release](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) also persists moderator deletions and bans, re-encrypts the guest book after a password change, binds notification replies to their conversation after restart, and uses only verified multiplayer paths. These are recovery controls, not revocation of keys already obtained.

### Primal Android 3.5.27 checks signer and wallet identity

[Primal Android 3.5.27](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27) shipped September 3 after [the signer identity check](https://github.com/PrimalHQ/primal-android-app/pull/1108) and [wallet-request authentication](https://github.com/PrimalHQ/primal-android-app/pull/1105) merged August 31. Local signing rejects a request whose identity does not match the held account, and incoming [NIP-47](/en/topics/nip-47/) requests are authenticated before processing. Zap-poll routing also sends votes to the poll author when the poll appears in a reply.

### GRAIN 0.8.0-rc2 closes an acknowledged-but-not-stored path

[GRAIN 0.8.0-rc2](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) shipped September 7 after a storage failure allowed `OK` before its asynchronous LMDB database writer noticed full storage capacity. The relay now warns at 80 and 95 percent, refuses new events at 97 percent while leaving deletion room, and reports post-acceptance writer failures. Retention walks oldest-first, teardown handles late messages, and invalid filters no longer discard valid siblings.

The [release](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) also corroborates kind `10166` monitor announcements and kind `30166` relay reports, evicts stale reports, keeps configured relays as fallback, and reports live limits and authentication in [NIP-11](/en/topics/nip-11/) instead of static zeros.

### LibreNostr 0.5.0–0.5.2 makes Tor routing fail closed

[LibreNostr 0.5.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) shipped September 7 with an Orbot mode routing relays, zaps, uploads, media, playback, and previews through one SOCKS port, plus a repair for a zap-sheet crash. If Orbot or the proxy is unavailable, connections stop instead of leaking onto a direct route. [Version 0.5.1](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.1) stops slow [NIP-50](/en/topics/nip-50/) searches delaying local results; [0.5.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.2) replaces recursive thread layout and repairs thread ordering.

The [fail-closed behavior](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) applies to every network surface listed by the release, and a restart is required because those clients are long lived. The patch releases preserve that choice while limiting unrelated search, stack-depth, and layout failures.

### SkateSpots adds an on-device relay path

The signed [September 8 Zapstore release](https://zapstore.dev/apps/org.skatespots.app) adds an optional Citrine relay to SkateSpots. Spots, crews, messages, and map data can load locally; posts queue offline; and the phone keeps a local copy. Existing stash and message content stays end-to-end encrypted. Payment checks require invoice amounts and provider-issued zap receipts before granting access or counting contributions.

The [local relay](https://zapstore.dev/apps/org.skatespots.app) is a storage and continuity option, not a replacement for every remote relay. It lets a skater keep working through a disconnected stretch and then reconcile signed activity later, while the payment changes stop a self-authored receipt from becoming proof of settlement.

### Whistle 1.8.15 repairs encrypted-group lifecycle recovery

[Whistle 1.8.15](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) shipped September 3 after an Android lifecycle repair stopped route-level state holders from destroying application-wide relay subscriptions and location updates. Its release notes also describe refreshed connection state after lock or doze and a recovered 501-event backlog in the observed case.

The [bug](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) tied ownership of a long-lived service to a short-lived screen. Keeping the activity-scoped instance alive and checking the socket before a one-shot read makes ordinary Android navigation and background suspension less likely to look like an empty group.

### TWENTY ONE Companion 1.12.0 separates encrypted DMs from legacy chat

[TWENTY ONE Companion 1.12.0](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) shipped September 5 with [NIP-17](/en/topics/nip-17/) gift-wrapped DMs. The encrypted inbox is separate from older space chat, which remains distinct because those messages were never encrypted and cannot be migrated. PDFs and videos are supported subject to relay policy, and personal hides sync without becoming moderator bans.

The [visible separation](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) is part of the security model. Calling the old history a secure inbox would misrepresent its provenance, while silently migrating it would suggest encryption that did not exist when it was written.

### ZapStore 1.1.2 validates event ids and certificate rotation

[ZapStore 1.1.2](https://github.com/zapstore/zapstore/releases/tag/1.1.2) shipped September 4 with NIP-01 event-id validation: the client recomputes an incoming event's id and rejects mismatches before using it. The release also identifies packages installed outside ZapStore. On the server, [certificate-hash retention](https://github.com/zapstore/relay/pull/8) preserves repeated `apk_certificate_hash` tags so Android signing-key rotation can retain an approved lineage.

The [event-id check](https://github.com/zapstore/zapstore/releases/tag/1.1.2) prevents a relay or cache from changing tags or content while keeping the old id. The installer-source indicator supplies separate provenance when an Android package with the same application id came from another channel.

### Amber 6.6.1 keeps signer responses attributable

[Amber 6.6.1](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) shipped September 4 after permission parsing was fixed to tolerate a missing optional `kind`, and rejected signing requests began returning their original request id. Calling applications can match a rejection to the submitted operation. The release also updates remote-signer defaults and adds an indexer relay.

Together these [fixes](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) preserve attribution in both directions: a permission record remains usable when an optional field is absent, and a refusal remains tied to the request that caused it. The relay-default changes affect discovery, but they do not replace the signer's local authorization decision.

## In Development

### Zap Cooking renders NIP-27 references with relay hints

[The September 4 merge](https://github.com/zapcooking/frontend/pull/665) makes [Zap Cooking](https://github.com/zapcooking/frontend) render `nostr:npub` and `nostr:nprofile` references in articles, recipes, editor previews, and print views. Invalid identifiers remain text, resolution is non-blocking, and the editor previews the Markdown that will be signed. When relay information exists, a bare `npub` becomes an `nprofile` with outbox relays and a matching `p` tag.

The same week fixed [author-scoped kind `30023` reads](https://github.com/zapcooking/frontend/commit/6a379c680727bb49074a4ff85f070b404dba97a7), added [verified NIP-50 search relays](https://github.com/zapcooking/frontend/commit/1802e8d7e95ed482209d09e03c834c2d9adfc1ea) with deduplication and stale-query guards, and repaired [NIP-47 wallet calls](https://github.com/zapcooking/frontend/pull/705) after dependency changes broke balances and history.

### Conduit reconciles signed relay and Blossom preferences

[Conduit](https://github.com/Conduit-BTC/conduit-mono) merged [Blossom preference editing](https://github.com/Conduit-BTC/conduit-mono/pull/374) on September 2 and [signed preference reconciliation](https://github.com/Conduit-BTC/conduit-mono/pull/397) on September 7. Market and Merchant retain the latest valid kind `10002` relay list and kind `10050` inbox declaration, preserve a usable signed list when a newer event is malformed, distinguish an explicit empty list from an unavailable lookup, and do not replace failed declared relays with code defaults.

The [kind `10063` editor](https://github.com/Conduit-BTC/conduit-mono/pull/374) lets a user load, reorder, review, externally sign, publish, and read back an ordered HTTPS media-server list without contacting those servers or inserting an undeclared default.

### NIP-A3 payment targets reach three clients

From September 1–3, [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041), [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851), and [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) implemented NIP-A3 kind `10133` payment targets. Amethyst offers an opt-in handoff only when a compatible target exists and does not turn it into a zap; Grimoire uses a fixed registry before building wallet URIs; Pollerama validates Monero addresses and fetches the author's relay list before querying targets. Each client still needs an allowed payment method, a relay route, and an accurate display.

### Ditto expands Blossom fallback and live embeds

[Ditto](https://github.com/soapbox-pub/ditto) merged [broad Blossom fallback and mirroring](https://github.com/soapbox-pub/ditto/commit/1e35a0705c28f706eb40d1f99aedef3105cf6f07) on September 6. Avatars, badges, banners, community images, custom emoji, and application icons now try declared servers with the same blob hash; mirror uploads use a standard BUD-11 authorization token. A [September 4 change](https://github.com/soapbox-pub/ditto/commit/e2a29004a65122470179c83d6ded8336a5c10dfa) added compact `kind:30311` live-stream embeds.

## Protocol and Spec Work

### Nostr Implementation Possibilities

[NIP-01](/en/topics/nip-01/) now clarifies [the `limit: 0` filter](https://github.com/nostr-protocol/nips/pull/2460), merged September 4. A relay MUST return no stored events, MUST send `EOSE` when initial queries complete, and MUST keep the subscription active for new matching events. Clients can open a live-only subscription with one filter field while retaining local history. The clarification records compatible behavior across several relay implementations and public relays.

[NIP-78](/en/topics/nip-78/) gained an [authenticated app-data requirement](https://github.com/nostr-protocol/nips/pull/2458), merged September 3. Relays SHOULD require [NIP-42](/en/topics/nip-42/) authentication for kinds `78` and `30078` and SHOULD serve them only to the authenticated event author. That is a SHOULD, not a confidentiality guarantee: clients cannot treat arbitrary relays as private storage. The merge also discourages custom app-data kinds as generic public interchange.

[NIP-AC](/en/topics/nip-ac/) opened September 4 as an explicitly open [WebRTC-signaling proposal](https://github.com/nostr-protocol/nips/pull/2461). It uses provisional ephemeral kinds for ping, connect requests, offers, answers, and ICE candidates, addressed with `p` and grouped by a session `e` tag; kind `30600` supports discovery. Relays SHOULD broadcast and MUST NOT store those signaling events while peers connect directly. The numbers remain provisional, clients SHOULD use [NIP-65 relay lists](/en/topics/nip-65/), and applications needing confidentiality SHOULD encrypt offer, answer, and candidate content with [NIP-44](/en/topics/nip-44/).

## NIP Deep Dive: URI Links and References in Event Text

A Nostr identifier needs a transportable meaning before another application can open it. [NIP-21](/en/topics/nip-21/) puts a [NIP-19](/en/topics/nip-19/) identifier after the `nostr:` URI scheme, giving browsers, operating systems, and applications one dispatchable form. [NIP-27](/en/topics/nip-27/) defines what that same URI means inside readable event `content`. NIP-21 crosses an application boundary; NIP-27 keeps a profile or event reference in signed prose. Neither creates an event kind or changes relay messages; the [two specifications](https://github.com/nostr-protocol/nips/tree/master) define only linking and rendering behavior.

### URI dispatch and NIP-19 semantics

[NIP-21's grammar](https://github.com/nostr-protocol/nips/blob/master/21.md) is `nostr:` followed by one NIP-19 bech32 entity. `nsec` is excluded because it encodes a private key. There is no authority, path, or query component, so a conforming link is `nostr:npub1...`, not `nostr://npub1...`. A platform or client may register as the handler; the specification does not choose the installed application or define a web fallback.

The prefix tells a client what to decode. `npub` carries a public key and `note` an event id. `nprofile` adds optional relay hints to a profile; `nevent` adds relays, author, and kind to an event id; and `naddr` carries the author, kind, and `d` identifier of an addressable event, with optional relays. These forms use [NIP-19 type-length-value fields](https://github.com/nostr-protocol/nips/blob/master/19.md). Hints narrow discovery but prove neither relay possession nor author control. Every fetched event still needs an id recomputation and signature check.

The profile form in the [NIP-21 specification](https://github.com/nostr-protocol/nips/blob/master/21.md) is:

```
nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9
```

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) also defines HTML bridges: a page serving a Nostr event can put its `naddr` in `<link rel="alternate">`, and a profile can put an `nprofile` in `<link rel="me">` or `<link rel="author">`.

### NIP-27 rendering and optional tags

[NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) applies to readable event content such as kind `1` notes and kind `30023` articles. A composer may display `@name`, but publishes `nostr:nprofile1...` in the signed string. A reader scans the URI, decodes its NIP-19 entity, fetches the target, and may render a name, card, preview, or local link. If decoding fails, the URI remains ordinary text. The raw content must not be rewritten: changing it changes the NIP-01 serialization, id, and signature.

Content references and tags have related but distinct jobs. [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) describes optional `p` and `e` tags and the [NIP-18](/en/topics/nip-18/) `q` tag. A client may show a reference without creating a notification or thread relationship; quote discovery should write both the URI and a `q` tag. [Zap Cooking's September 4 implementation](https://github.com/zapcooking/frontend/pull/665) follows that split by retaining the URI while adding relay hints and a matching `p` tag. Adding `p` or `q` does not make the URI private, and NIP-27 has no hidden-mention mode.

The following [kind `1` event](https://njump.me/note1e0my422kylehy2g4ax4d98vsthdvnvy702yq3f6eguedjr0256as200k6a) was recovered from `wss://nos.lol` and verified before inclusion as a concrete NIP-27 reference. Its `content` contains an `naddr` for a version-independent addressable event. Decoding yields kind `30402`, author `91036d...310a`, the workbook's `d` identifier, and a `wss://nos.lol/` hint. The `q`, `p`, `t`, `zap`, and `client` tags are application choices, not NIP-27 requirements.

```json
{
  "id": "cbf64aa95627f3722915e9aad29d905ddac9b09e7a8808a7594732d90deaa6bb",
  "pubkey": "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
  "created_at": 1788953511,
  "kind": 1,
  "tags": [
    [
      "p",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/"
    ],
    [
      "t",
      "archetype"
    ],
    [
      "q",
      "30402:91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a:Archetype-Workbook-Companion-Meet-your-King-Warrioir-Magician-Lover-today-oejbwe",
      "wss://nos.lol/"
    ],
    [
      "zap",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/",
      "0.9"
    ],
    [
      "zap",
      "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
      "wss://relay.nostr.band/",
      "0.1"
    ],
    [
      "client",
      "Amethyst"
    ]
  ],
  "content": "You can check, read and use this Workbook already! You can also support and get it for few sats and support us in this project.\n\nI hope it'll help you in your Archetype Journey :)\n\n#archetype\n\nnostr:naddr1qpgyzunrdpjhg7tsv5k4wmmjdd3x7mmt94pk7mtsv9hxjmmw94xk2et594uk7atj949kjmn894tkzunjd9hkju3df4skw6trd9skut2vdamx2u3dw3hkgcte94hk26nzwajszrnhwden5te0dehhxtnvdakz7q3qjypkmmqcaetrcpld4m27la946cch2hrk7qr8xjehsu5j5h3uxy9qxpqqqpmvyqnrm7n",
  "sig": "aa9592e7c773271b9e9f980c8a7e17fda2ffd5a4483a1789e5dd4c4a83018ac576c5202b21b33b08770dcabe023f93998a41f1a0be4bf00e36cdde611d07915e"
}
```

### Trust, failure behavior, and client implementations

A safe reader finds a complete `nostr:` token, validates bech32, decodes NIP-19, rejects `nsec`, ignores unknown TLV types, and leaves malformed or oversized text alone. `npub` and `nprofile` lead to profile queries; `note` and `nevent` identify immutable events; `naddr` selects the latest valid addressable event for its kind, author, and `d` tag. Relay hints reduce search but do not extend trust. Under the [NIP-01 event rules](https://github.com/nostr-protocol/nips/blob/master/01.md), the client verifies a fetched `nevent` id and checks every `naddr` candidate signature before applying addressable-event replacement rules.

Inline previews are a client choice with privacy and resource costs. Fetching every reference reveals the reader's interests and can create a lookup storm, so clients can use a cache, defer fetches until visible, cap concurrency, and require a click for unfamiliar media. Under [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md), a preview must remain distinct from the current author's signed text. Failure should be visible as unresolved text or an unavailable card, not silently treated as verified content.

Trust also changes by identifier type. A `nevent` names immutable bytes, so a client can reject a fetched event whose serialized id differs from the requested id. An `naddr` names a replaceable coordinate, so a client must verify each candidate and apply the addressable-event rules before deciding which version to display. A relay hint is useful for the first query in either case, but it is not an endorsement of the relay or of the returned content. [NIP-19's TLV definition](https://github.com/nostr-protocol/nips/blob/master/19.md) supplies the data needed to make those checks explicit.

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) defines a portable link that can be opened from outside Nostr, while NIP-27 makes the same link durable inside signed text. A client that implements only NIP-21 can open a pasted URI but not render embedded references. Full NIP-27 support adds scanning, safe decoding, fetch policy, local rendering, and an explicit choice about notification and quote tags. The shared URI keeps those layers interoperable without forcing clients to present them identically.

[Damus](https://github.com/damus-io/damus) models inline references as typed mentions. Its [mention code](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/Mentions.swift) maps `npub` and `nprofile` to profile references, `note` and `nevent` to event references, and `naddr` to address references; [NostrLink](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/NostrLink.swift) routes them to the appropriate destination. [Primal Android](https://github.com/PrimalHQ/primal-android-app) [parses the scheme and pasted forms](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/domain/nostr/src/commonMain/kotlin/net/primal/domain/nostr/utils/NostrUriUtils.kt), validates bech32 and extracts relay hints, then [maps references into note-content models](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/app/src/main/kotlin/net/primal/android/notes/feed/model/NoteNostrUriUi.kt). [Zap Cooking](https://github.com/zapcooking/frontend/pull/665) renders the same references in articles, recipes, editor previews, and print views.

---

Send a NIP-17 DM to share a project or news item through the [Nostr Compass project](https://github.com/andotherstuff/nostr-compass).
