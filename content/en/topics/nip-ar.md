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

Each artifact is an editable record with a stable `d` identity and one channel home in an `h` tag. Its revisions are full snapshots linked by `prev`. A relay accepts an edit only if `prev` names the current head. Two competing revisions therefore cannot both become the next head. Buzz's implementation uses kind `45010` for artifacts and a relay-signed kind `45011` marker when an artifact moves out of a channel. The source channel sees the removal without learning the destination from that marker.

The [Buzz specification merge](https://github.com/block/buzz/pull/7791) describes the model, and the [relay implementation merge](https://github.com/block/buzz/pull/7919) reports tests for conflict handling, history queries, moves, and channel permissions. Those merges establish project source behavior, not a general Nostr standard or a public deployment guarantee.

## Sync and recovery

On October 30 Buzz merged two NIP-AR extensions into its main branch. Both remain project-local and describe different consistency guarantees.

The [complete WebSocket snapshot merge](https://github.com/block/buzz/commit/a56966b777278f703040b4686820a201bc278c57) gives a REQ for current artifacts in the selected `#h` channels a consistent database snapshot that is complete at EOSE, followed by live current heads. The relay registers live interest before the snapshot read and holds changes until EOSE, and a client replaces its local set only at EOSE. Access changes, pubsub loss, lag, redactions, and queue drops end the subscription with an explicit resync `CLOSED`. One window remains: a node that crashes after a database commit and before publishing can miss a live change, so clients that need a bound must resync on their own schedule.

The [incremental HTTP recovery merge](https://github.com/block/buzz/commit/a57349b237c67c3983dd7a09af378977ccd1e3f9) provides eventual consistency and does not produce a complete cut. Signed HTTP queries with checkpoints and cursors replay current upserts and explicit removals after a disconnect, and a known-ID read confirms whether a write was accepted and is still accessible. Absence from a page never proves deletion. Modified timestamps come from the database clock with a 120-second overlap, which assumes each commit lands within 120 seconds of its timestamp. Access-policy changes reset and revalidate known IDs. The feature is off by default behind `BUZZ_ARTIFACT_INCREMENTAL_ENABLED`, and operators must apply migrations 0076 to 0078 and upgrade every writer before enabling it.

---

**Primary sources:**
- [Buzz channel-artifact specification merge](https://github.com/block/buzz/pull/7791)
- [Buzz channel-artifact implementation merge](https://github.com/block/buzz/pull/7919)
- [Buzz complete WebSocket artifact snapshot merge](https://github.com/block/buzz/commit/a56966b777278f703040b4686820a201bc278c57)
- [Buzz incremental HTTP artifact recovery merge](https://github.com/block/buzz/commit/a57349b237c67c3983dd7a09af378977ccd1e3f9)

**Mentioned in:**
- [Newsletter #47: Buzz adopts complete artifact snapshots over WebSocket](/en/newsletters/2026-11-04-newsletter/#buzz-adopts-complete-artifact-snapshots-over-websocket)
- [Newsletter #47: Buzz merges incremental recovery for saved artifact stores](/en/newsletters/2026-11-04-newsletter/#buzz-merges-incremental-recovery-for-saved-artifact-stores)
- [Newsletter #46: Buzz NIP-AR sync subscriptions send a complete snapshot before live heads](/en/newsletters/2026-10-28-newsletter/#buzz-nip-ar-sync-subscriptions-send-a-complete-snapshot-before-live-heads)
- [Newsletter #45](/en/newsletters/2026-10-21-newsletter/#buzz)
- [Newsletter #42: Buzz channel artifacts](/en/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
