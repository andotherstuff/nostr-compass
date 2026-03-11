---
title: "NIP-91: AND Operator for Filters"
date: 2026-03-04
draft: false
categories:
  - NIP
  - Protocol
---

NIP-91 adds AND filter semantics for tag arrays in Nostr relay subscriptions. It merged on 2026-03-03 after implementations appeared in multiple relays.

## The Problem

Nostr's filter system ([NIP-01](/en/topics/nip-01/)) combines multiple values within a single tag filter using OR logic. If a client specifies two `p` tag values in a filter, the relay returns events matching either pubkey. There was no way to request events that reference both pubkeys simultaneously.

This forced clients to over-fetch events from relays and filter locally, increasing bandwidth use and processing time.

## How It Works

NIP-91 introduces AND semantics for tag arrays. When a client needs events matching all specified tag values, it can opt into intersection matching instead of the default union behavior.

That matters for queries such as "events that tag both participants in a conversation" or "events carrying two required labels at once." Before this change, relays could only answer the broader superset and leave the precise intersection to the client.

## Why It Matters

AND filters make relay-side indexes more useful. Clients can ask a relay for a smaller, already-relevant result set, which cuts down bandwidth and local post-processing. The gain is most noticeable on mobile clients and on queries over large tag-heavy datasets.

## Interop Notes

At the time of merge, working implementations existed in nostr-rs-relay, satellite-node, worker-relay, and applesauce. The proposal was formerly numbered NIP-119 before renumbering.

Clients should still expect mixed support while relay adoption catches up. A practical fallback is to keep the old client-side intersection path for relays that have not implemented the new semantics yet.

---

**Primary sources:**
- [PR #1365](https://github.com/nostr-protocol/nips/pull/1365)

**Mentioned in:**
- [Newsletter #12: NIP Updates](/en/newsletters/2026-03-04-newsletter/#nip-updates)
- [Newsletter #13: NIP Updates](/en/newsletters/2026-03-11-newsletter/#nip-updates)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
