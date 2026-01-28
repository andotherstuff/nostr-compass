---
title: "Negentropy: Set Reconciliation Protocol"
date: 2026-01-28
draft: false
categories:
  - Protocol
  - Sync
---

Negentropy is a set reconciliation protocol that enables efficient synchronization between Nostr clients and relays by identifying missing events without transferring the full dataset.

## How It Works

Rather than requesting all events matching a filter, negentropy allows clients to compare their local event set against a relay's set and identify only the differences. This is accomplished through a multi-round protocol:

1. **Fingerprinting**: Client and relay each compute a fingerprint of their event sets
2. **Comparison**: Fingerprints are exchanged and compared
3. **Reconciliation**: Only missing event IDs are identified and transferred

## Why It Matters

Traditional Nostr sync uses timestamp-based `since` filters, which can miss events due to:
- Clock drift between client and relay
- Multiple events with identical timestamps
- Events arriving out of order

Negentropy solves these problems by comparing actual event sets rather than relying on timestamps.

## Use Cases

- **DM Recovery**: Clients can detect and fetch missing direct messages even with old timestamps
- **Feed Sync**: Ensures complete timeline synchronization across relays
- **Offline Sync**: Efficiently catches up after periods of disconnection

## Implementation

Negentropy requires relay support. Clients typically implement it as a fallback recovery mechanism rather than replacing standard REQ subscriptions, gracefully degrading when relays don't support the protocol.

## Related

- [NIP-01](/en/topics/nip-01/) - Basic Protocol
