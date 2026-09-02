## NIP Deep Dive: Reposts and Reactions

A contact can put an existing note back in front of their followers, and they can attach a compact like, dislike, or emoji without writing a reply. [NIP-18](/en/topics/nip-18/) (reposts) publishes that redistribution as its own signed event. [NIP-25](/en/topics/nip-25/) (reactions) publishes the compact response as a separate signed event. Both remain `draft` `optional` files on the [canonical repost specification](https://github.com/nostr-protocol/nips/blob/master/18.md) and the [canonical reaction specification](https://github.com/nostr-protocol/nips/blob/master/25.md): they are present in the NIPs repository and implemented by clients, while still labeled non-final.

### Reposts (NIP-18)

Followers receive a signed pointer to a kind 1 text note someone already published when a client writes a kind 6 event. [The repost specification](https://github.com/nostr-protocol/nips/blob/master/18.md) sets `kind` to 6, puts the stringified JSON of that note in `content` (empty `content` is allowed and not recommended), requires an `e` tag whose value is the note's `id` and whose third entry is a relay URL where the note can be fetched, and says the event SHOULD also carry a `p` tag with the original author's `pubkey`. A repost of a [NIP-70](/en/topics/nip-70/) (protected events) event SHOULD keep `content` empty so the protected payload is not copied into the new event.

A quote is a citation inside some other event, not a kind 6 wrapper. When a client mentions a [NIP-21](/en/topics/nip-21/) (`nostr:` URI) `nevent`, `note`, or `naddr`, it must convert that mention into a `q` tag of the form `["q", "<event-id> or <event-address>", "<relay-url>", "<pubkey-if-a-regular-event>"]`. [Quote-repost tags](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts) keep those citations out of reply threads and let clients pull and count the quotes on a post.

Kind 6 is reserved for kind 1 notes. A kind 16 generic repost can wrap any event kind other than kind 1. It SHOULD include a `k` tag whose value is the stringified kind of the inner event. When that inner event is replaceable, the generic repost SHOULD add an `a` tag with the `kind:pubkey:d-tag` coordinate; if that `a` tag is absent, the repost targets one specific version and `content` must hold the full JSON string of that version. [The generic-repost rules](https://github.com/nostr-protocol/nips/blob/master/18.md#generic-reposts) keep long-form, addressable, and other non-note events from being published as if they were kind 1.

The following kind 6 event is a live repost recovered from `wss://relay.damus.io` at assembly time ([open the event](https://njump.me/nevent1qqs88k8xgv2d3d3yymawaa24f22a0kqqvknpur0p05vq9e5r4y74xjspz3mhxue69uhhyetvv9ujuerpd46hxtnfdu7elvca)):

```json
{
  "kind": 6,
  "id": "73d8e64314d8b62426faeef5554a95d7d80065a61e0de17d1802e683a93d534a",
  "pubkey": "a60e79e0edad5100d7543b669e513dbc1c2170e8e9b74fdb8e971afd1e0e6813",
  "created_at": 1787768621,
  "tags": [
    [
      "e",
      "38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976"
    ],
    [
      "p",
      "34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095"
    ],
    [
      "client",
      "Primal iOS"
    ]
  ],
  "content": "{\"pubkey\":\"34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095\",\"sig\":\"8c0271f7b438083ce491c391335598e0cbceee0758177cf98f7894531033cb5153704b01009590f3d4e9cdfadd5bbf73fc5eea54186fcbac6d30744e0e6c1cd6\",\"id\":\"38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976\",\"tags\":[[\"r\",\"https:\/\/stacker.news\/items\/1555439\"],[\"client\",\"Damus\"]],\"created_at\":1787766056,\"content\":\"🚨 Attention CLN (Core Lightning) node runners 🚨\n\nhttps:\/\/stacker.news\/items\/1555439\",\"kind\":1}",
  "sig": "b6b97fa377cfdb651e2850f65f2ccb12ca0724c0de0fc0e39e9721f850abdfd31f5d5567517a51d988145c2a2de9ae9540b02eecf7352e554022870d5e8c64a5"
}
```

Its `kind` is 6, the `e` tag points to the reposted note, the `p` tag identifies that note's author, and `content` carries the original kind 1 event as stringified JSON. This relay-recovered event omits the relay hint that the [NIP-18 specification](https://github.com/nostr-protocol/nips/blob/master/18.md) marks as required, illustrating why readers and clients must validate real events and allow for producers that omit fields.

### Reactions (NIP-25)

A post can collect signed likes, dislikes, and emoji without those marks entering the reply thread. [The reaction specification](https://github.com/nostr-protocol/nips/blob/master/25.md) defines that mark as a kind 7 event whose `content` MUST carry the reaction value. `+` or an empty string MUST be read as a like or upvote. `-` MUST be read as a dislike or downvote. An emoji or a [NIP-30](/en/topics/nip-30/) (custom emoji) shortcode SHOULD NOT be read as a like or dislike, and a client MAY display that emoji on the post.

The target is in the tags, not inferred from `content`. There MUST be an `e` tag set to the target event `id`, and that tag SHOULD include a relay hint; extra `e` tags are not recommended, and if they appear the target `id` must be last. There SHOULD be a `p` tag for the target author, last if several `p` tags appear. An addressable target SHOULD also get an `a` tag with `kind:pubkey:d-tag` coordinates. The `e` and `a` tags SHOULD include relay and pubkey hints, the `p` tags SHOULD include relay hints, and a `k` tag MAY carry the stringified kind of the reacted event. [Those tag rules](https://github.com/nostr-protocol/nips/blob/master/25.md#tags) let a client fetch the target and notify its author from the reaction event alone.

A client MAY put a single `:shortcode:` in `content` and one `emoji` tag that maps that shortcode to an image URL, following the [custom-emoji reaction rules](https://github.com/nostr-protocol/nips/blob/master/25.md#custom-emoji-reaction). If the target is not a native Nostr event, the reaction MUST be kind 17 and MUST carry [NIP-73](/en/topics/nip-73/) (external content IDs) `k` and `i` tags, as in the [external-content reaction rules](https://github.com/nostr-protocol/nips/blob/master/25.md#external-content-reactions). Kind 17 is a reaction to a website, podcast episode, or other external object. It is not a kind 7 event-to-event reaction and it is not a repost.

The following kind 7 event is a live reaction recovered from `wss://relay.damus.io` at assembly time ([open the event](https://njump.me/nevent1qqsytac63l00k7kyaphkfwqqn94wglmx78v6zhqtytg65w5k957luccpz3mhxue69uhhyetvv9ujuerpd46hxtnfdus63jym)):

```json
{
  "kind": 7,
  "id": "45f71a8fdefb7ac4e86f64b800996ae47f66f1d9a15c0b22d1aa3a962d3dfe63",
  "pubkey": "0755cc2b972c3cbcae36913109c50b36b3fe110fa38a76dc37d1f01c5305496a",
  "created_at": 1787768605,
  "tags": [
    [
      "e",
      "519de32071d71bb2ab8b71a07e03eb9a256b6a59f9b08877b156c80966d5c320"
    ],
    [
      "a",
      "34236:5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb:2ddda68516f4729d3ef55a1eb01fe028253393212493a34816ad8eb79f97a3b7"
    ],
    [
      "p",
      "5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb"
    ],
    [
      "k",
      "34236"
    ],
    [
      "client",
      "Divine",
      "31990:d95aa8fc0eff8e488952495b8064991d27fb96ed8652f12cdedc5a4e8b5ae540:divine-mobile",
      "wss://relay.divine.video"
    ]
  ],
  "content": "+",
  "sig": "3c081756c7a73e2ee8aa10fadf3b5009390d5ac9a72078ba03701c42af91022ef275df7cb17724689a23dca4e29ff1a7cd5e3a24135d021983e2726a28b00b1e"
}
```

Its `content` is `+`, the conventional like from [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md). The `e` tag names the reacted-to event; the `a` tag adds its addressable coordinate; the `p` tag identifies its author; and the optional `k` tag records the target's kind as a string.

### Current client implementations

[Amethyst](https://github.com/vitorpamplona/amethyst), an Android Nostr client, defines the [repost event type](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip18Reposts/RepostEvent.kt) and the [reaction event type](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt) in its current protocol layer.

[Snort](https://github.com/v0l/snort), a web Nostr client, implements [NIP-18 helpers that include quote-link tag handling](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip18.ts) and [creates NIP-25 event-reaction tags](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip25.ts).

[Ditto](https://github.com/soapbox-pub/ditto), a combined Mastodon server and Nostr relay, [publishes kind 16 generic reposts with a `k` tag and an `a` coordinate on addressable targets](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/components/RepostMenu.tsx) and [applies kind 7 reaction semantics by treating the last `e` tag as the target event](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/lib/nostrEvents.ts).

### How They Work Together

A kind 6 or kind 16 event redistributes an existing event into the reposter's followers' feeds, either by embedding that event's JSON or by pointing at a replaceable coordinate. A `q` tag marks a quote inside some other event so thread reconstruction can count citations without treating the quoting event as a reply, which is the split drawn in the [quote-repost section](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts). A kind 7 event leaves the original event in place and attaches only the reaction value plus target tags, which is the contract in the [reaction specification](https://github.com/nostr-protocol/nips/blob/master/25.md). Clients that fetch one pubkey therefore see that pubkey's reposts as new kind 6 or 16 events and that pubkey's opinions as kind 7 events on other people's posts.

---

Send a NIP-17 DM to share a project or news item through the [Nostr Compass project](https://github.com/andotherstuff/nostr-compass).

GATE: PENDING REVIEW
