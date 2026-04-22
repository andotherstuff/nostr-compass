---
title: "NIP-62: Vanish Requests"
date: 2026-01-13
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62 defines vanish requests, kind `62` events that ask specific relays to delete all events from the requesting pubkey. The request is relay-targeted by default, and it can also be broadcast as a global request using the special `ALL_RELAYS` tag value.

## How It Works

A vanish request is a kind `62` event signed by the pubkey that wants its history removed. The tag list must include at least one `relay` value naming the relay that should act on the request.

```json
{
  "id": "a7b8c9d0e1f23456789012345678901234567890abcdef1234567890abcdef12",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1743465600,
  "kind": 62,
  "tags": [
    ["relay", "wss://relay.example.com"]
  ],
  "content": "Requesting deletion of all events from this relay.",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

The `content` field may include a reason or legal notice to the relay operator. Clients should send the event directly to the target relays instead of posting it broadly unless the user intends a network-wide vanish request.

## Relay Behavior

Relays that see a vanish request and find their own service URL in a `relay` tag must fully delete any events from that pubkey up to the request's `created_at`. The spec also says relays should delete [NIP-59](/en/topics/nip-59/) (Gift Wrap) events that `p`-tagged the vanished pubkey, so incoming DMs get removed alongside the user's own events.

The relay must also ensure those deleted events cannot be re-broadcast into the relay. It may keep the signed vanish request itself for bookkeeping.

## Global Requests

To request deletion on every relay that sees the event, the tag value becomes `ALL_RELAYS` in uppercase:

```json
{
  "kind": 62,
  "pubkey": "<32-byte-hex-pubkey>",
  "tags": [
    ["relay", "ALL_RELAYS"]
  ],
  "content": "Global vanish request"
}
```

Clients should broadcast this form to as many relays as possible.

## Why It Matters

NIP-62 gives clients and relay operators a shared deletion signal that goes beyond ad hoc moderation APIs or relay-specific dashboards. A user can publish one signed request and let each relay process it with the same event format.

It also goes beyond [NIP-09](/en/topics/nip-09/). NIP-09 deletes individual events and relays may comply. NIP-62 asks tagged relays to delete everything from the pubkey and prevent those events from being re-imported.

## Implementations

- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - Client-side vanish request support
- [rust-nostr PR #1315](https://github.com/rust-nostr/nostr/pull/1315) - Memory backend support
- [rust-nostr PR #1316](https://github.com/rust-nostr/nostr/pull/1316) - LMDB backend support
- [rust-nostr PR #1317](https://github.com/rust-nostr/nostr/pull/1317) - SQLite backend support
- [rust-nostr PR #1318](https://github.com/rust-nostr/nostr/pull/1318) - Database test coverage for relay-specific vanish support
- [nostream PR #544](https://github.com/Cameri/nostream/pull/544) - Added NIP-62 right-to-vanish to the advertised feature list

---

**Primary sources:**
- [NIP-62 Specification](https://github.com/nostr-protocol/nips/blob/master/62.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - Client-side vanish support
- [rust-nostr PR #1315](https://github.com/rust-nostr/nostr/pull/1315)
- [rust-nostr PR #1316](https://github.com/rust-nostr/nostr/pull/1316)
- [rust-nostr PR #1317](https://github.com/rust-nostr/nostr/pull/1317)
- [rust-nostr PR #1318](https://github.com/rust-nostr/nostr/pull/1318)
- [nostream PR #544](https://github.com/Cameri/nostream/pull/544)

**Mentioned in:**
- [Newsletter #5: Notable Code Changes](/en/newsletters/2026-01-13-newsletter/#rust-nostr-library)
- [Newsletter #12: rust-nostr](/en/newsletters/2026-03-04-newsletter/#rust-nostr-nip-62-request-to-vanish)
- [Newsletter #16: Amethyst ships NIP-62 support](/en/newsletters/2026-04-01-newsletter/#amethyst-ships-pinned-notes-relay-management-and-request-to-vanish)
- [Newsletter #16: NIP Deep Dive](/en/newsletters/2026-04-01-newsletter/#nip-deep-dive-nip-62-request-to-vanish)
- [Newsletter #19: nostream NIP-62 support](/en/newsletters/2026-04-22-newsletter/#nostream-merges-53-prs-for-nip-45-nip-62-compression-and-query-hardening)

**See also:**
- [NIP-09: Event Deletion Request](/en/topics/nip-09/)
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
- [NIP-59: Gift Wrap](/en/topics/nip-59/)
