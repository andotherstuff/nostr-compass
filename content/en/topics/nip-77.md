---
title: "NIP-77: Negentropy Reconciliation"
date: 2026-05-14
draft: false
categories:
  - NIPs
  - Sync
---

NIP-77 defines how Nostr relays and clients use the [Negentropy](/en/topics/negentropy/) set-reconciliation protocol to efficiently sync event sets, finding which events each side is missing without resending the full dataset.

## How It Works

Negentropy reconciliation runs over a WebSocket connection using a dedicated message type. The client and relay exchange compact range fingerprints over their sorted event sets, narrowing in on only the ranges that differ. Once the differences are identified, only the missing event IDs (and then the missing events themselves) are transferred.

NIP-77 standardizes the message framing so any client and relay that implement the spec can negotiate an efficient sync session. The protocol uses `NEG-OPEN`, `NEG-MSG`, and `NEG-CLOSE` message types over the existing Nostr WebSocket connection.

## Why It Matters

Traditional Nostr sync uses timestamp-based `since` filters, which can miss events due to clock drift, events with identical timestamps, or events arriving out of order. Negentropy compares actual event sets rather than relying on timestamps, giving a provably complete sync in significantly fewer round trips than naive polling.

This is especially useful for:
- Mobile clients catching up after going offline
- Relay-to-relay replication
- Local relay sync (as in Citrine's relay aggregator)

## Implementations

- [Citrine](https://github.com/greenart7c3/Citrine) — [PR #139](https://github.com/greenart7c3/Citrine/pull/139) added NIP-77 support for efficient set-reconciliation sync in the Android relay node
- [strfry](https://github.com/hoytech/strfry) — relay-side negentropy support
- [nostr-tools](https://github.com/nbd-wtf/nostr-tools) — client-side negentropy implementation

---

**Primary sources:**
- [NIP-77 Specification](https://github.com/nostr-protocol/nips/blob/master/77.md)
- [Negentropy protocol](https://github.com/hoytech/negentropy)

**Mentioned in:**
- [Newsletter #22: Citrine v3.0.0-pre1](/en/newsletters/2026-05-14-newsletter/#citrine-v300-pre1-lands-built-in-tor-and-relay-aggregation)

**See also:**
- [Negentropy](/en/topics/negentropy/)
