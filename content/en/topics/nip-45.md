---
title: "NIP-45: Event Counting"
date: 2026-02-11
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45 defines how clients ask relays to count events matching a filter without transferring the matching events themselves. It reuses NIP-01 filter syntax, so a client can often turn an existing `REQ` into a `COUNT` request with the same filters.

## How It Works

A client sends a `COUNT` request with a subscription ID and filter:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

The relay responds with a count:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

This avoids downloading hundreds or thousands of events just to display a number. If a client sends multiple filters in one `COUNT` request, the relay aggregates them into a single result, just as multiple `REQ` filters are ORed together.

## HyperLogLog Approximate Counting

As of February 2026, NIP-45 supports HyperLogLog (HLL) approximate counting ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). Relays can mark a result as approximate, and for cross-relay deduplication they can return 256 HLL registers alongside the count:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<512-char hex string>"}]
```

HLL solves a fundamental problem: counting distinct events across multiple relays. If relay A reports 50 reactions and relay B reports 40, the total is not 90 because many events exist on both relays. Clients merge HLL values by taking the maximum value at each register position, which gives a network-wide estimate without downloading the raw events.

The spec fixes the register count at 256 for interoperability. That keeps the payload small and makes relay-side caching practical because every relay computes the same register layout for the same eligible filter.

## Interop Notes

HLL is only defined for filters with a tag attribute, because the offset used to build the registers is derived from the first tagged value in the filter. The spec also calls out a small set of canonical queries, including reactions, reposts, quotes, replies, comments, and follower counts. Those are the easiest counts for relays to precompute or cache.

## Why It Matters

Follower counts, reaction counts, and reply counts are the main use cases. Without NIP-45, clients must either trust a single relay's local view or download all matching events and deduplicate them locally. NIP-45 keeps counting inside the relay, and HLL makes multi-relay counts practical without turning one relay into the authority.

---

## Implementations

- [nostream](https://github.com/Cameri/nostream) added `COUNT` support in [PR #522](https://github.com/Cameri/nostream/pull/522), letting clients ask how many events match a filter without fetching them.

---

**Primary sources:**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)
- [nostream PR #522](https://github.com/Cameri/nostream/pull/522) - NIP-45 COUNT support

**Mentioned in:**
- [Newsletter #9: NIP Deep Dive](/en/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-45-event-counting-and-hyperloglog)
- [Newsletter #9: NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12: Five Years of Nostr Februaries](/en/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: nostream NIP-45 support](/en/newsletters/2026-04-22-newsletter/#nostream-merges-53-prs-for-nip-45-nip-62-compression-and-query-hardening)

**See also:**
- [NIP-11: Relay Information Document](/en/topics/nip-11/)
