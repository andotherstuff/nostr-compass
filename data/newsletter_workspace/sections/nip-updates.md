## NIP Deep Dive

### Search Capability (NIP-50)

[NIP-50](/en/topics/nip-50/), defined in the [primary specification](https://github.com/nostr-protocol/nips/blob/master/50.md), adds an optional search filter for relays. Ordinary Nostr filters work when a client already knows an author, event kind, identifier, or tag; NIP-50 addresses discovery when the input is a human query such as `best nostr apps`.

The [NIP-50 wire format](https://github.com/nostr-protocol/nips/blob/master/50.md#search-filter-field) adds a `search` string to a normal filter inside a `REQ` message. A request can combine that field with `kinds`, `authors`, `ids`, tag filters, and `limit`, and one REQ can carry several independent filters. A supporting relay should match primarily against event `content`, may use other fields when the event kind makes that useful, and should sort by its own relevance score before applying `limit`. That order differs from the usual newest-first event stream.

The query string can include the specification's [`key:value` extensions](https://github.com/nostr-protocol/nips/blob/master/50.md#extensions). It names `include:spam`, `domain:`, `language:`, `sentiment:`, and `nsfw:`; a relay should ignore extensions it does not implement. Clients discover declared support through the relay's [NIP-11](/en/topics/nip-11/) `supported_nips` field, but they may still send the filter elsewhere if they are prepared to reject unrelated responses.

The [NIP-50 specification](https://github.com/nostr-protocol/nips/blob/master/50.md) deliberately does not standardize tokenization, stemming, ranking, language detection, sentiment analysis, or spam classification. Two compliant relays can return different events and different ordering for the same query. That makes the relay an index and ranking provider, not a source of truth. The specification recommends querying several supporting relays, checking whether returned events satisfy the client's use case, and dropping relays whose results have poor precision.

This differs from exact [NIP-01 filtering](https://github.com/nostr-protocol/nips/blob/master/01.md). An `authors` or `#t` filter has deterministic matching semantics that a client can verify directly, while a search match may depend on an index and an opaque score. NIP-50 retains NIP-01's signed event envelope and relay transport, but accepts variation in recall and ordering to make open-ended retrieval possible.

The event below is an illustrative search result using the [seven NIP-01 event fields](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures). The repeated hexadecimal values are placeholders rather than a valid signature.

```json
{
  "id": "0000000000000000000000000000000000000000000000000000000000000000",
  "pubkey": "1111111111111111111111111111111111111111111111111111111111111111",
  "created_at": 1785888000,
  "kind": 1,
  "tags": [["t", "nostr"]],
  "content": "A comparison of Nostr search relays and their indexes.",
  "sig": "22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
}
```

Current clients use the same filter in different discovery surfaces. [Nostria](https://github.com/nostria-app/nostria/blob/d291c2ab091c60c36f99c90241e2fd9da1b0c4bc/src/app/services/relays/search-relay.ts) sends NIP-50 searches to dedicated search relays, [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useSearchEvents.ts) searches events through its relay pool, and [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/services/orchestration/SearchOrchestrator.ts) coordinates relay-backed searches for long-form reading. Their different result handling reflects the latitude NIP-50 leaves to relays and clients.

### Highlights (NIP-84)

[NIP-84](/en/topics/nip-84/), defined by its [primary specification](https://github.com/nostr-protocol/nips/blob/master/84.md), assigns kind `9802` to a highlight. It turns a selected passage, or a reference to non-text media, into a signed event that can move between reading, social, and annotation clients.

The [event's `content`](https://github.com/nostr-protocol/nips/blob/master/84.md#format) contains the selected text and may be empty when the source is audio, video, or another non-text medium. A highlight points to a Nostr source with an `a` tag for an addressable event or an `e` tag for an ordinary event; an `r` tag identifies a web URL. URL-producing clients should remove tracking and other non-useful query parameters before publishing so cosmetic URL variants do not fragment references to the same source.

Optional [`p` tags](https://github.com/nostr-protocol/nips/blob/master/84.md#attribution) attribute the source to one or more Nostr pubkeys. Their fourth value may identify a role such as `author` or `editor`, and a `context` tag can preserve surrounding text when the selection alone would be unclear. A quote highlight adds a `comment` tag instead of publishing a second kind `1` note: the source `r` tag receives the `source` marker, while pubkeys or URLs mentioned in the comment carry `mention`, letting renderers distinguish attribution from the user's response.

The [kind `9802` definition](https://github.com/nostr-protocol/nips/blob/master/84.md) makes a highlight a regular event rather than a replaceable one. Repeating or correcting a selection creates another signed event, and removing one relies on the normal deletion-request flow and relay retention policy. The specification does not define byte offsets, selectors, or a canonical document snapshot, so a client may be unable to relocate a passage after its web source changes. Public highlights also reveal reading interests; private annotation requires a separate encryption and sharing design.

NIP-84 differs from a [NIP-23 long-form event](https://github.com/nostr-protocol/nips/blob/master/23.md), which publishes an entire article as kind `30023`; a highlight quotes or points into material that may remain elsewhere. It also differs from a [NIP-51 bookmark set](https://github.com/nostr-protocol/nips/blob/master/51.md), which stores a replaceable collection of references. NIP-84 makes each selection independently signed, attributable, discoverable, and discussable.

This illustrative highlight contains the [seven NIP-01 event fields](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures). Its identifier and signature are placeholders.

```json
{
  "id": "3333333333333333333333333333333333333333333333333333333333333333",
  "pubkey": "4444444444444444444444444444444444444444444444444444444444444444",
  "created_at": 1785888000,
  "kind": 9802,
  "tags": [
    ["a", "30023:6666666666666666666666666666666666666666666666666666666666666666:relay-search", "wss://relay.example"],
    ["p", "6666666666666666666666666666666666666666666666666666666666666666", "wss://relay.example", "author"],
    ["context", "Search relays are indexes whose ranking policies can differ."]
  ],
  "content": "ranking policies can differ",
  "sig": "55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555"
}
```

The format already crosses client boundaries. [nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) added NIP-84 rendering this week, [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/components/ui/note-rendering/HighlightRenderer.ts) renders highlight events in its long-form client, and [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useCreateHighlight.ts) publishes them from selected content. Those implementations cover reading, creation, and social rendering without requiring one service to own the annotation.

---

Send a NIP-17 DM to share a project or news item through the [Nostr Compass project](https://github.com/andotherstuff/nostr-compass).

GATE: PASS
