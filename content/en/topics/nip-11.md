---
title: "NIP-11: Relay Information Document"
date: 2025-12-17
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11 defines how relays publish a machine-readable description of themselves, including claimed feature support, limits, and operator metadata.

## How It Works

Clients fetch relay information by making an HTTP GET request to the relay's WebSocket URL with an `Accept: application/nostr+json` header. The relay returns a JSON document describing its capabilities.

## Useful Fields

- **name** - Human-readable relay name
- **description** - What the relay is for
- **supported_nips** - List of claimed NIP support
- **limitation** - Restrictions like max message size, required auth, etc.
- **pubkey** - Relay operator public key when provided
- **contact** - Operator contact address

## Trust Model

NIP-11 is self-reported metadata. It tells you what a relay says about itself, not what it has proven in live traffic. That is still useful for discovery and UX, but clients should not treat `supported_nips` as ground truth without testing behavior.

This distinction matters for relay selection. A relay may advertise NIP-50 search, authentication requirements, or a large message limit, but the real answer only appears once a client actually connects and exercises those code paths.

## Why It Matters

- Clients can check if a relay supports required features before connecting
- Discovery services can index relay capabilities
- Users can see relay policies before publishing

## Recent Spec Direction

The specification has been trimmed over time. Older optional fields such as `software`, `version`, privacy policy details, and retention metadata were removed after years of weak adoption. That makes current NIP-11 documents smaller and more realistic, but it also means clients should not expect rich policy metadata from relays.

---

**Primary sources:**
- [NIP-11 Specification](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [PR #1764](https://github.com/nostr-protocol/nips/pull/1764) - relay identity field update
- [PR #1946](https://github.com/nostr-protocol/nips/pull/1946) - cleanup of rarely used fields
- [PR #2231](https://github.com/nostr-protocol/nips/pull/2231) - removal of deprecated fields

**Mentioned in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**See also:**
- [NIP-66: Relay Discovery and Liveness Monitoring](/en/topics/nip-66/)
