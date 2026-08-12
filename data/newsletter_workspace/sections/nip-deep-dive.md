## NIP Deep Dive

### Event Deletion Requests (NIP-09)

[NIP-09](/en/topics/nip-09/), defined by the [primary specification](https://github.com/nostr-protocol/nips/blob/master/09.md), gives an event author a signed way to ask relays and clients to stop serving one or more of that author's events. It does not erase every copy. It carries the author's intent through the same relay network that distributed the original event.

The request is an ordinary signed kind `5` event. Its tags contain one or more `e` references to specific event IDs or `a` references to addressable-event coordinates, and the [NIP-09 tag rules](https://github.com/nostr-protocol/nips/blob/master/09.md#event-deletion-request) say it should include a `k` tag for each referenced event kind. The optional `content` can explain the reason. For an `a` reference, a relay should remove every version at that coordinate whose timestamp is no later than the request's `created_at`, which prevents an old deletion request from suppressing a later replacement.

[Authorship is the security boundary](https://github.com/nostr-protocol/nips/blob/master/09.md#relay-behavior). A relay should stop publishing a referenced event only when its `pubkey` matches the deletion request's `pubkey`, and a client must perform that check before hiding an event. A relay may not possess the referenced event and therefore may be unable to validate the relationship when accepting the request, so clients cannot treat relay acceptance as proof that the deletion was authorized. The specification also asks relays to retain the kind `5` request because another client may already hold the original event and encounter the request later.

Here is a [signed kind `5` event](https://primal.net/e/6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943):

```json
{
  "id": "6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943",
  "pubkey": "5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743",
  "created_at": 1786465675,
  "kind": 5,
  "tags": [
    ["e", "f3d47f8b813928c5baf7ac993846be0220dc37a2e7c7b128fb49a4b92711f131"],
    ["k", "30091"],
    ["a", "30091:5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743:survey:0ad5cebc-608b-47d7-97fd-9e6c47787199"],
    ["t", "nostr-survey"]
  ],
  "content": "Public survey summary deleted during privacy refresh",
  "sig": "846be83b038dc5f91af0c9d03a4ac81aff9bc4cfde7d85c849fa2fdae890f75cc444a4072f45aa18883b0b3871e15381b220182d6e366892f0c9c6f9c0557244"
}
```

Deletion remains a cooperative policy, not revocation of a signed object. A relay, cache, screenshot, or offline client can preserve the original bytes, and deleting the kind `5` request itself does not undo it. Clients may hide the target, mark it as disowned, or display the request reason, but should tell users that universal deletion cannot be guaranteed. This differs from [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md), where an `expiration` tag asks relays to stop storing an event after a time chosen when the event is published. NIP-09 handles a later author decision and can point to already-distributed events.

Current implementations apply that policy at different layers. [Divine PR #6623](https://github.com/divinevideo/divine-mobile/pull/6623) removes deleted videos from the client's event store, [strfry PR #251](https://github.com/hoytech/strfry/pull/251) extends valid deletion requests to gift-wrap recipients, and [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md) declares NIP-09 support in its client. [nostrord's group client](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/network/NostrGroupClient.kt) supplies another current implementation path.

### Reporting (NIP-56)

[NIP-56](/en/topics/nip-56/), defined by the [primary specification](https://github.com/nostr-protocol/nips/blob/master/56.md), standardizes a signed report about an account, event, or referenced blob. It separates the report signal from the moderation decision, allowing each client or relay to choose which reporters it trusts and what response fits its policy.

A report uses kind `1984` and must identify the reported account in a `p` tag. Reporting a note also requires an `e` tag for the event ID. The third value of the tag carries one of the specified categories: `nudity`, `malware`, `profanity`, `illegal`, `spam`, `impersonation`, or `other`. A report about a blob can use its hash in an `x` tag, an `e` tag for the event that referenced the blob, and an optional `server` tag for a location. Optional `L` and `l` tags from [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) can add a namespaced label when the fixed category list is not precise enough.

[The event proves only that one key made an allegation](https://github.com/nostr-protocol/nips/blob/master/56.md#reporting). The reported content does not become false, illegal, or removable merely because a valid kind `1984` exists, and an open relay cannot safely count anonymous reports as votes. The specification advises against automatic relay moderation because reports are easy to game, while allowing relay administrators to act on reports from moderators they already trust. A client can instead weight reports through a user's social graph, for example by blurring content after several trusted contacts flag the same account.

Here is a [signed kind `1984` event](https://primal.net/e/17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2):

```json
{
  "id": "17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2",
  "pubkey": "1ff02fb5cdc633c1be55368ab655490ec25d2f5dc2e364d4703bc3196d99eab1",
  "created_at": 1786465319,
  "kind": 1984,
  "tags": [
    ["p", "3a72b02cc05ee07310dc580874b6a9ca8271c6518b90655bd2e98003c9601e68", "impersonation"]
  ],
  "content": "",
  "sig": "6362e415410feb19e0505654a4660e8456b6b2aec5ae39173a0429a6a8e5fa1381c9488198ca2982db43ee8198af056f2a25537705c763784062056d0ab2eb1a"
}
```

[NIP-56 and NIP-09 solve different problems](https://github.com/nostr-protocol/nips/tree/master). A kind `1984` report can target somebody else's account or event, but confers no deletion authority. A kind `5` request expresses the original author's intent and is valid only against that author's own events. Neither guarantees removal: NIP-56 deliberately delegates action to local moderation policy, while NIP-09 depends on relays and clients honoring an authenticated request.

Implementations expose those choices in different products. [Divine PR #6591](https://github.com/divinevideo/divine-mobile/pull/6591) corrects report delivery in a short-video client, [Conduit PR #250](https://github.com/Conduit-BTC/conduit-mono/pull/250) reads reports as bounded context for marketplace participants, and [nostrord's NIP-56 module](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/nostr/Nip56.kt) publishes and processes report events. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md#nip-support) also lists current NIP-56 support.


---

Send a NIP-17 DM to share a project or news item through the [Nostr Compass project](https://github.com/andotherstuff/nostr-compass).

GATE: PASS (final-delta claims, continuity, 73/73 live links, prose/style, topic-backlink, and production-build gates passed at 2026-08-12T15:45Z)
