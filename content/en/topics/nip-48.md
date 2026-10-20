---
title: "NIP-48: Bridged Events"
date: 2026-10-21
draft: false
categories:
  - NIP
---

[NIP-48](https://github.com/nostr-protocol/nips/blob/master/48.md) defines a `proxy` tag that marks a Nostr event as bridged from another protocol and links it to the source object. The spec is marked draft and optional.

## Purpose

Bridges republish posts from ActivityPub, AT Protocol, RSS feeds and websites as signed Nostr events. A `proxy` tag records the claimed origin of each event, so clients can link to the source and recognize copies of one object that arrive through different bridges ([NIP-48](https://github.com/nostr-protocol/nips/blob/master/48.md)).

## How it works

Any event kind may carry the tag:

```
["proxy", <id>, <protocol>]
```

The `<id>` identifies the source object and must be universally unique regardless of protocol. The spec lists four protocols and allows the list to grow:

| Protocol | ID format |
| -------- | --------- |
| `activitypub` | URL |
| `atproto` | AT URI |
| `rss` | Feed URL with a GUID fragment |
| `web` | URL |

Adding the tag indicates that the event did not originate on Nostr. Clients may use it to reconcile duplicated bridged content or to display a link to the source. The spec's example is a real kind 1 event from 2023 whose tag points to an ActivityPub object on gleasonator.com ([NIP-48](https://github.com/nostr-protocol/nips/blob/master/48.md)).

## Implementations

Amethyst's Quartz library, at commit 6ebf90c, includes a [proxy tag parser](https://github.com/vitorpamplona/amethyst/blob/6ebf90c95cd6dc960915618dc33f3bb799827a8e/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip48ProxyTags/ProxyTag.kt) and [tag helpers](https://github.com/vitorpamplona/amethyst/blob/6ebf90c95cd6dc960915618dc33f3bb799827a8e/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip48ProxyTags/TagArrayExt.kt) that parse and assemble proxy triples, define constants for the four listed protocol codes, enumerate every proxy tag or return the first, and detect whether an event carries a non-empty valid triple. This is library support; parsing does not verify the remote origin or define how a client displays or deduplicates bridged content.

The spec points to the [Mostr bridge](https://mostr.pub/) and to [FEP-fffd: Proxy Objects](https://codeberg.org/fediverse/fep/src/branch/main/fep/fffd/fep-fffd.md), a related Fediverse proposal.

## Trust and limits

The event signature authenticates the Nostr signer and its source claim. For bridged content, that signer is usually the bridge. The remote authorship and source-site authenticity remain unverified. Whether the source still serves the object, and whether the Nostr copy matches it exactly, also require separate checks. Clients choose which bridge keys to trust and whether to deduplicate events. NIP-48 leaves those policies and any bridge registry unspecified. The tag makes the claimed origin visible to anyone who reads the event ([NIP-48](https://github.com/nostr-protocol/nips/blob/master/48.md)).

### Mostr

In Mostr's [`transmute.ts`](https://gitlab.com/soapbox-pub/mostr/-/blob/99e94a76cc4e088a7cff95656b6b6b8f9c6d3065/src/nostr/transmute.ts#L229) (20 October commit), `toNoteEvent` appends `["proxy", note.id, "activitypub"]` before calling `signEvent(event, note.attributedTo)`. It emits kind 1111 for comments with a parent and reply, and kind 1 otherwise. `note.id` is the ID of the remote ActivityPub object. The tag labels where the event came from. The signature does not prove Fediverse authorship, account control or that the objects are the same.

## Primary sources

- [NIP-48 specification](https://github.com/nostr-protocol/nips/blob/master/48.md)
- [FEP-fffd: Proxy Objects](https://codeberg.org/fediverse/fep/src/branch/main/fep/fffd/fep-fffd.md)
- [Amethyst Quartz proxy tag parser at 6ebf90c](https://github.com/vitorpamplona/amethyst/blob/6ebf90c95cd6dc960915618dc33f3bb799827a8e/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip48ProxyTags/ProxyTag.kt)
- [Amethyst Quartz proxy tag helpers at 6ebf90c](https://github.com/vitorpamplona/amethyst/blob/6ebf90c95cd6dc960915618dc33f3bb799827a8e/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip48ProxyTags/TagArrayExt.kt)

## Mentioned in

- [Newsletter #45: NIP-37 and NIP-48](/en/newsletters/2026-10-21-newsletter/#nip-deep-dive-nip-37-and-nip-48)
