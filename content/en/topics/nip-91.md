---
title: "NIP-91: AND Operator for Filters"
date: 2026-03-04
draft: false
categories:
  - NIP
  - Protocol
---

NIP-91 adds AND filter semantics for tag arrays in Nostr relay subscriptions. It merged on March 3, 2026 after implementation across multiple relays.

## The Problem

Nostr's filter system ([NIP-01](/en/topics/nip-01/)) combines multiple values within a single tag filter using OR logic. If a client specifies two `p` tag values in a filter, the relay returns events matching either pubkey. There was no way to request events that reference both pubkeys simultaneously.

This forced clients to over-fetch events from relays and filter locally, increasing bandwidth use and processing time.

## How It Works

NIP-91 introduces AND semantics for tag arrays. When a client needs events matching all specified tag values, it can use the AND operator to require that every value in the array is present in the event's tags.

The specification defines the convention for relay implementations to support this, while maintaining backward compatibility with existing OR behavior for clients that do not opt in.

## Relay Implementations

At the time of merge, working implementations existed in nostr-rs-relay, satellite-node, worker-relay, and applesauce. The proposal was formerly numbered NIP-119 before renumbering.

---

**Primary sources:**
- [NIP-91 Specification](https://github.com/nostr-protocol/nips/blob/master/91.md)
- [PR #1365](https://github.com/nostr-protocol/nips/pull/1365)

**Mentioned in:**
- [Newsletter #12: NIP Updates](/en/newsletters/2026-03-04-newsletter/#nip-updates)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
