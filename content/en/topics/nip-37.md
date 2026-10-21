---
title: "NIP-37: Draft Wraps"
date: 2026-07-01
draft: false
categories:
  - NIP
  - Drafts
  - Privacy
---

[NIP-37](https://github.com/nostr-protocol/nips/blob/master/37.md) defines kind 31234 as encrypted storage for an unsigned draft of any other kind. The draft's JSON string is encrypted with NIP-44 to the signer's own public key. Its ciphertext goes in `content`. The `d` tag sets the addressable coordinate, so a later save under the same identifier replaces the earlier wrap. Its required `k` tag names the draft's kind, and a NIP-40 `expiration` tag is recommended. A blank `content` signals that the draft was deleted. Kind 1234 checkpoints hold the same kind of encrypted payload and point to their parent with an `a` tag of the form `31234:<pubkey>:<identifier>`, which gives a revision history.

Kind 10013 lists the relays where a user prefers to keep private events such as draft wraps. Its `relay` entries are private tags: JSON-stringified, NIP-44-encrypted to the signer and stored in `content`, with the public tag array left empty. Clients must publish kind 10013 to the author's NIP-65 write relays and should send kind 31234 events to the relays it lists. The spec recommends that these storage relays require NIP-42 authentication and serve events only to the authenticated signer ([NIP-37](https://github.com/nostr-protocol/nips/blob/master/37.md)).

The following [kind 31234 event](https://njump.me/nevent1qqsyvelwl4352zcrmvvuczujjlk0rl3tvh7fenw4dur9lwhp8xq7pqcpp4mhxue69uhkummn9ekx7mqxdzur3) was retrieved from nos.lol and is reproduced unchanged. Its plaintext is unknown.

```json
{
  "kind": 31234,
  "id": "4667eefd63450b03db19cc0b9297ecf1fe2b65fc9ccdd56f065fbae13981e083",
  "pubkey": "64acf4055fa826bcab8457e24ef8fba7490abb1e76dbab6aa8752a53a0eb4d4a",
  "created_at": 1792437134,
  "tags": [
    [
      "d",
      "bb0d7e8d-6ee6-407b-8426-85e43a0b954c"
    ],
    [
      "k",
      "1"
    ]
  ],
  "content": "AsSHMdC3Yuw9szbDej9OMmPUF5q37XUHBLnY2YaZ14zo/h3cwtZ7iZ30ONchDUrJmRSG4GZ7nbv0u6KMovyBZwNWJdwOlkjTjsoVCJ01RaQwt3fS74GU52xmYlDEYxMcLiVm6Qo/vukluILTqN9RBBYDcNap35v21ZzllMeGbqmPqfeq4DIihNjjALOPBgw0R42OCgY/o6pt/ZXPU1LUiiH+cJwKFlvhTRk4cAmb/y/uWNEghffUvNaAog0fLFdq6B5PBgTROcDG+O8o1URoZyYqj53/MEkOU/qbcnDML2cXW76A3Hz1jeqxvwmvpSHpXUwBak1QLsWL6wNWiSd833yK7Y0ge4noHLN1MbSLat0aQyClZHFPjJ6Yz7MbicnwumKH",
  "sig": "0bd82e078e215b5ac6071b5facfb1ddcfb1a2ca8d2f2cec06849f83e1cf69503724a0ba116389d642181e755b9ac6ada6733f3420a3ff1fc2143d2c6d13223e1"
}
```

The `k` tag declares a kind 1 draft and the `d` tag is a random UUID. The event has no `expiration` tag, so it skips the spec's recommendation and gives relays no NIP-40 signal for dropping it. Anyone who can fetch it reads the author pubkey, `created_at`, kind and both tags, and the ciphertext length gives an approximate size for the draft. Decrypting `content` requires the author's private key ([NIP-37](https://github.com/nostr-protocol/nips/blob/master/37.md)).

These properties set the privacy limits. NIP-44 hides the draft body, leaves the outer pubkey, timestamp, kind and tags readable, and a relay can still copy the event. Authenticated download is a recommendation for relay operators that a client cannot enforce. Expiration and replacement signal a change in the stored draft; blank content signals deletion. Earlier ciphertext can remain in relay storage or archived copies. A kind 10013 event on public write relays keeps its relay URLs encrypted but shows that the list exists and when it changed. Every draft and checkpoint is encrypted to the same key, so a compromised key exposes all of them ([NIP-37](https://github.com/nostr-protocol/nips/blob/master/37.md)).

## Implementations

- The [draft wrap model](https://github.com/vitorpamplona/amethyst/blob/6ebf90c95cd6dc960915618dc33f3bb799827a8e/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip37Drafts/DraftWrapEvent.kt) requires the signer's pubkey to equal the wrap's outer `pubkey` before NIP-44 decryption. It parses the inner JSON and recognizes blank content as a deleted draft. A draft can contain `e` and `a` tags that reference public events, and the model deliberately offers no relay hints for them, so private storage relay URLs do not leak into hints for those public events.
- The [kind 10013 relay list](https://github.com/vitorpamplona/amethyst/blob/6ebf90c95cd6dc960915618dc33f3bb799827a8e/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip37Drafts/privateOutbox/PrivateOutboxRelayListEvent.kt) writes new lists with `relay` tags in encrypted content and an empty public tag array. On update it moves public `relay` tags left by older clients into the encrypted content, and on read it accepts both locations for compatibility. The migration does not erase public copies that relays or archives already hold.

### Notedeck

At commit [`9395544`](https://github.com/damus-io/notedeck/blob/93955445ae1853924b17c0973e3c037015dd19b0/crates/notedeck/src/account/relay.rs#L346), Notedeck implements NIP-37's private relay list. Private relay URLs for kind 10013 are stored as JSON `relay` tags inside NIP-44 content that is encrypted to the account's own key. They are not published as public NIP-65 read/write flags. When parsing, Notedeck decrypts with the account secret and normalizes the URLs. Read-only pubkey accounts get an empty set, and malformed JSON is logged and ignored. [`private_sync.rs`](https://github.com/damus-io/notedeck/blob/93955445ae1853924b17c0973e3c037015dd19b0/crates/notedeck/src/private_sync.rs) passes these relays to a private client that handles local ingest, fan-out, NIP-77 history catch-up and live `REQ`. This covers the relay-list part only, not a full kind 31234 draft UI. No independent runtime or interop test was run.

## Primary sources

- [NIP-37 specification](https://github.com/nostr-protocol/nips/blob/master/37.md)

## Mentioned in

- [Newsletter #45: NIP-37 and NIP-48](/en/newsletters/2026-10-21-newsletter/#nip-deep-dive-nip-37-and-nip-48)
- [Newsletter #29: Notedeck](/en/newsletters/2026-07-01-newsletter/#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments)
