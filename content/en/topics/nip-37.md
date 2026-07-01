---
title: "NIP-37: Draft Wraps"
date: 2026-07-01
draft: false
categories:
  - NIP
  - Drafts
  - Privacy
---

NIP-37 defines an encrypted storage event for unsigned draft events of any kind. A user composing a long-form article, an upcoming calendar event, or a message they may want to send later can store the draft on relays under a kind `31234` event, encrypted to their own key with [NIP-44](/en/topics/nip-44/). The draft is recoverable from any client that holds the user's key, and the same NIP defines a separate `kind:10013` list event that names the relays the user wants their private drafts stored on.

## How It Works

A draft wrap is a parameterised replaceable event of kind `31234`. The unsigned draft event is JSON-stringified, NIP-44 encrypted to the signer's own public key, and placed in `.content`. A `k` tag declares the kind of the draft so a client can group drafts by event type. A `d` tag carries the draft identifier so the wrap can be replaced as the draft evolves, and a NIP-40 `expiration` tag is recommended so old drafts age out automatically.

```json
{
  "kind": 31234,
  "tags": [
    ["d", "<identifier>"],
    ["k", "<kind of the draft event>"],
    ["expiration", "<unix-timestamp>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

A blanked `.content` field signals the draft has been deleted.

## Checkpoints

Kind `1234` defines checkpoints belonging to a parent `kind:31234` event. Checkpoints carry an `a` tag pointing back at the parent draft and let a client store revision history alongside the latest draft.

```json
{
  "kind": 1234,
  "tags": [
    ["a", "31234:<pubkey>:<identifier>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

## Relay List for Private Content (kind 10013)

Kind `10013` is a replaceable event whose tags list the relays the user wants to store private content on, including draft wraps. Clients publishing kind `31234` SHOULD publish to relays listed on the user's kind `10013` event. This separates the relay set used for public posting (NIP-65) from the relay set used for private content storage, so a user can pin private drafts to a small set of trusted relays without exposing that set in their public outbox.

## Implementations

- [Notedeck](https://github.com/damus-io/notedeck) - stores private-sync relays as a kind-10013 list (added 2026-06)

---

**Primary sources:**
- [NIP-37 Specification](https://github.com/nostr-protocol/nips/blob/master/37.md)
- [Notedeck commit storing private-sync relays as kind-10013](https://github.com/damus-io/notedeck) - Damus team adopts the spec for desktop sync relay management

**Mentioned in:**
- [Newsletter #29: Notedeck](/en/newsletters/2026-07-01-newsletter/#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments)

**See also:**
- [NIP-44: Versioned Encryption](/en/topics/nip-44/)
- [NIP-65: Relay List Metadata](/en/topics/nip-65/)
