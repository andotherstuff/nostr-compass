---
title: "NIP-11: Relay Information"
date: 2025-12-17
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11 defines how relays expose metadata about themselves, including supported NIPs, limitations, and contact information.

## How It Works

Clients fetch relay information by making an HTTP GET request to the relay's WebSocket URL with an `Accept: application/nostr+json` header. The relay returns a JSON document describing its capabilities.

## Key Fields

- **name** - Human-readable relay name
- **description** - What the relay is for
- **supported_nips** - List of implemented NIPs
- **limitation** - Restrictions like max message size, required auth, etc.
- **self** - The relay's own public key (new field for relay identity)

## Use Cases

- Clients can check if a relay supports required features before connecting
- Discovery services can index relay capabilities
- Users can see relay policies before publishing

---

**Primary sources:**
- [NIP-11 Specification](https://github.com/nostr-protocol/nips/blob/master/11.md)

**Mentioned in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
