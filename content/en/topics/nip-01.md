---
title: "NIP-01: Basic Protocol"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-01 defines the base event model and relay protocol that the rest of Nostr builds on. If a client, relay, or library speaks Nostr at all, it starts here.

## How It Works

Events are the only object type in Nostr. Profiles, notes, reactions, relay lists, and many application-specific payloads all use the same seven-field envelope:

- **id**: SHA256 hash of the serialized event (unique identifier)
- **pubkey**: The creator's public key (32-byte hex, secp256k1)
- **created_at**: Unix timestamp
- **kind**: Integer categorizing the event type
- **tags**: Array of arrays for metadata
- **content**: The payload (interpretation depends on kind)
- **sig**: Schnorr signature proving authenticity

The event `id` is the SHA256 hash of the serialized event data, not an arbitrary identifier. That matters in practice: changing any field, including a tag order or timestamp, produces a different event and requires a new signature.

## Kinds

Kinds determine how relays store and handle events:

- **Regular events** (1, 2, 4-44, 1000-9999): Stored normally, all versions kept
- **Replaceable events** (0, 3, 10000-19999): Only the latest per pubkey is kept
- **Ephemeral events** (20000-29999): Not stored, just forwarded to subscribers
- **Addressable events** (30000-39999): Latest per pubkey + kind + `d` tag combination

Core kinds include: 0 (user metadata), 1 (text note), and 3 (follow list).

## Client-Relay Communication

Clients communicate with relays over WebSocket connections using JSON arrays:

**Client to relay:**
- `["EVENT", <event>]` - Publish an event
- `["REQ", <sub-id>, <filter>, ...]` - Subscribe to events
- `["CLOSE", <sub-id>]` - End a subscription

**Relay to client:**
- `["EVENT", <sub-id>, <event>]` - Deliver matching event
- `["EOSE", <sub-id>]` - End of stored events (now streaming live)
- `["OK", <event-id>, <true|false>, <message>]` - Accept/reject acknowledgment
- `["NOTICE", <message>]` - Human-readable message

In practice, most higher-level NIPs do not change the transport layer. They define new event kinds, tags, or interpretation rules while still using the same `EVENT`, `REQ`, and `CLOSE` messages from NIP-01.

## Filters

Filters specify which events to retrieve, with fields including `ids`, `authors`, `kinds`, `#e`/`#p`/`#t`, `since`, `until`, and `limit`. Conditions inside one filter use AND logic. Multiple filters inside one `REQ` use OR logic.

## Interop Notes

Two details cause many implementation bugs. First, clients should treat relay responses as eventually consistent, not globally ordered, because different relays can return different subsets of history. Second, replaceable and addressable events mean "latest" is part of the protocol model, so clients need deterministic rules for picking the newest valid event when several relays disagree.

---

**Primary sources:**
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Mentioned in:**
- [Newsletter #1: NIP Deep Dive](/en/newsletters/2025-12-17-newsletter/#nip-deep-dive-nip-01-and-nip-19)
- [Newsletter #19: NIP-67 EOSE completeness hint proposal](/en/newsletters/2026-04-22-newsletter/#nip-updates)

**See also:**
- [NIP-19: Bech32-Encoded Entities](/en/topics/nip-19/)
- [Kind Registry](/en/kind-registry/)
