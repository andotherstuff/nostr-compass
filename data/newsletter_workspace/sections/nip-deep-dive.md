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

writer_model: claude-opus-5 (bounded first-party fallback candidate; wrapper run `7dee2ec3-0440-4980-a0a5-9dd9ce854a4c`)

GATE: PENDING REVIEW
