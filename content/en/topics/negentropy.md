---
title: "Negentropy: Set Reconciliation Protocol"
date: 2026-01-28
draft: false
categories:
  - Protocol
  - Sync
---

Negentropy is a set-reconciliation protocol for finding which events one side has and the other side lacks, without resending the full dataset.

## How It Works

Rather than requesting every event matching a filter, negentropy compares two sorted sets and narrows in on only the ranges that differ. The protocol exchanges compact range summaries and falls back to explicit ID lists only where needed.

1. **Ordering**: Both sides sort records by timestamp, then by ID
2. **Range comparison**: They exchange fingerprints for ranges of records
3. **Refinement**: Mismatched ranges get split until the actual missing IDs are clear

## Why It Matters

Traditional Nostr sync uses timestamp-based `since` filters, which can miss events due to:
- Clock drift between client and relay
- Multiple events with identical timestamps
- Events arriving out of order

Negentropy solves these problems by comparing actual event sets rather than relying on timestamps.

## Practical Use

- **DM Recovery**: Clients can detect and fetch missing direct messages even with old timestamps
- **Feed Sync**: Ensures complete timeline synchronization across relays
- **Offline Sync**: Efficiently catches up after periods of disconnection

The useful implementation detail is that many clients do not replace normal subscriptions with negentropy. They use it as a repair path. Damus, for example, kept ordinary DM loading and added negentropy on manual refresh to recover messages that the normal flow would miss.

## Tradeoffs

Negentropy requires support on both sides, and it adds protocol complexity beyond standard `REQ` usage. It is most helpful when correctness matters more than minimal implementation effort.

In mixed environments, clients still need graceful fallback behavior because not every relay supports the protocol.

---

**Primary sources:**
- [Negentropy Protocol Repository](https://github.com/hoytech/negentropy)
- [Damus PR #3536](https://github.com/damus-io/damus/pull/3536)
- [Damus PR #3547](https://github.com/damus-io/damus/pull/3547)

**Mentioned in:**
- [Newsletter #7: Damus ships negentropy for reliable DM syncing](/en/newsletters/2026-01-28-newsletter/#damus-ships-negentropy-for-reliable-dm-syncing)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**See also:**
- [NIP-01: Basic Protocol Flow](/en/topics/nip-01/)
