---
title: "Buzz NIP-AR: Channel Artifacts"
date: 2026-09-30
draft: false
categories:
  - Project Proposals
  - Collaboration
---

NIP-AR is Buzz's **project-specific** channel-artifact specification. The label here does not mean it has been adopted by the `nostr-protocol/nips` repository or by other relays.

## Artifact model

An artifact is an editable record with a stable `d` identity, one channel home in an `h` tag, and full-snapshot revisions linked by `prev`. A relay accepts an edit only if `prev` names the current head. Two competing revisions therefore cannot both become the next head. Buzz's implementation uses kind `45010` for artifacts and a relay-signed kind `45011` marker when an artifact moves out of a channel. The source channel sees the removal without learning the destination from that marker.

The [Buzz specification merge](https://github.com/block/buzz/pull/7791) describes the model, and the [relay implementation merge](https://github.com/block/buzz/pull/7919) reports tests for conflict handling, history queries, moves, and channel permissions. Those merges establish project source behavior, not a general Nostr standard or a public deployment guarantee.

---

**Primary sources:**
- [Buzz channel-artifact specification merge](https://github.com/block/buzz/pull/7791)
- [Buzz channel-artifact implementation merge](https://github.com/block/buzz/pull/7919)

**Mentioned in:**
- [Newsletter #42: Buzz channel artifacts](/en/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
