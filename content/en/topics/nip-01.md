---
title: "NIP-01: Basic Protocol"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-01 defines the foundational protocol for Nostr, establishing the data structures and communication patterns that all other NIPs build upon.

## Events

Events are the only object type in Nostr. Every piece of data, from a profile update to a text post to a reaction, is represented as an event with this structure:

- **id**: SHA256 hash of the serialized event (unique identifier)
- **pubkey**: The creator's public key (32-byte hex, secp256k1)
- **created_at**: Unix timestamp
- **kind**: Integer categorizing the event type
- **tags**: Array of arrays for metadata
- **content**: The payload (interpretation depends on kind)
- **sig**: Schnorr signature proving authenticity

## Kinds

Kinds determine how relays store and handle events:

- **Regular events** (1, 2, 4-44, 1000-9999): Stored normally, all versions kept
- **Replaceable events** (0, 3, 10000-19999): Only the latest per pubkey is kept
- **Ephemeral events** (20000-29999): Not stored, just forwarded to subscribers
- **Addressable events** (30000-39999): Latest per pubkey + kind + `d` tag combination

Core kinds include: 0 (user metadata), 1 (text note), 3 (follow list).

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

## Filters

Filters specify which events to retrieve, with fields including: `ids`, `authors`, `kinds`, `#e`/`#p`/`#t` (tag values), `since`/`until`, and `limit`. Conditions within a filter use AND logic; multiple filters in a `REQ` combine with OR logic.

---

**Primary sources:**
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Mentioned in:**
- [Newsletter #1: NIP Deep Dive](/en/newsletters/2025-12-17-newsletter/#nip-deep-dive-nip-01-and-nip-19)

**See also:**
- [NIP-19: Bech32-Encoded Entities](/en/topics/nip-19/)
- [Kind Registry](/en/kind-registry/)
