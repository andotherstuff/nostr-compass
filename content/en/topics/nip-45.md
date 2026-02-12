---
title: "NIP-45: Event Counting"
date: 2026-02-11
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45 defines how clients ask relays to count events matching a filter without transferring the events themselves. Clients send a COUNT message with the same filter syntax as REQ, and relays respond with a count.

## How It Works

A client sends a COUNT request with a subscription ID and filter:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

The relay responds with the count:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

This avoids downloading hundreds or thousands of events just to display a number.

## HyperLogLog Approximate Counting

As of February 2026, NIP-45 supports HyperLogLog (HLL) approximate counting ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). Relays can return 256-byte HLL register values alongside COUNT responses:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

HLL solves a fundamental problem: counting distinct events across multiple relays. If relay A reports 50 reactions and relay B reports 40, the total is not 90 because many events exist on both relays. HLL registers from multiple relays can be merged by taking the maximum value at each register position, automatically deduplicating across the network.

With 256 registers, the standard error is approximately 5.2%. HyperLogLog++ corrections improve accuracy for small cardinalities under ~200 events. Even two reaction events consume more bandwidth than the 256-byte HLL payload, making this efficient for any count above trivial numbers.

The spec fixes the register count at 256 for interoperability across all relay implementations.

## Use Cases

Social metrics (follower counts, reaction counts, repost counts) are the primary application. Without HLL, clients must either query a single "trusted" relay for counts (centralizing the data) or download all events from all relays to deduplicate locally (wasting bandwidth). HLL provides approximate cross-relay counts with 256 bytes of overhead per relay.

---

**Primary sources:**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)

**Mentioned in:**
- [Newsletter #9: NIP Deep Dive](/en/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-45-event-counting-and-hyperloglog)
- [Newsletter #9: NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)

**See also:**
- [NIP-11: Relay Information Document](/en/topics/nip-11/)
