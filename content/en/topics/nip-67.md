---
title: "NIP-67: EOSE Completeness Hint"
date: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-67 is an open proposal that extends the existing `EOSE` message in [NIP-01](/en/topics/nip-01/) with an optional third element indicating whether the relay has delivered every stored event matching the filter. It is intended to replace the unreliable heuristic clients use today to decide whether a subscription is exhausted or cut short by a relay-side cap.

## The Problem

`EOSE` marks the boundary between stored and real-time events, but it carries no information about completeness. In practice, relays enforce a per-subscription cap, commonly between 300 and 1000 events, that is independent of the client's `limit`. A client that asks for the last 500 notes from a relay capped at 300 receives 300 events and an `EOSE`, with no way to distinguish "this is all of it" from "we stopped partway through." The current workaround is to compare the event count to the client's `limit` and paginate defensively, which both misses events when the cap is below the requested limit and wastes a round trip when the cap is a multiple of the actual match count.

Boundary ties make this worse. Paginating with `until = oldest_created_at` risks either missing or double-fetching events that share the oldest timestamp in the batch, depending on how the relay compares timestamps.

## The Change

NIP-67 adds an optional third element to `EOSE`:

```
["EOSE", "<subscription_id>", "finish"]   // all matching stored events delivered
["EOSE", "<subscription_id>"]             // no claim of completeness (legacy)
```

Only the positive signal is specified. A relay that advertises NIP-67 support but omits the hint is saying there is more. A relay that does not advertise support falls through to the existing heuristic, so the change is backward compatible with every current client and relay.

Clients that know their relay supports NIP-67 can stop paginating as soon as they see `"finish"`, avoid the mandatory extra round trip when the cap exactly matches the result set, and surface accurate completeness to the user.

## Status

The proposal is [open as PR #2317](https://github.com/nostr-protocol/nips/pull/2317) against the NIPs repository.

---

**Primary sources:**
- [PR #2317: NIP-67 EOSE Completeness Hint](https://github.com/nostr-protocol/nips/pull/2317)
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Mentioned in:**
- [Newsletter #19: NIP Updates](/en/newsletters/2026-04-22-newsletter/#nip-updates)

**See also:**
- [NIP-01: Basic protocol flow](/en/topics/nip-01/)
- [NIP-11: Relay Information Document](/en/topics/nip-11/)
