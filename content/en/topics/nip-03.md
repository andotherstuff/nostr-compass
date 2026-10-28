---
title: "NIP-03: OpenTimestamps Attestations for Events"
date: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-03 describes how to publish an [OpenTimestamps](https://opentimestamps.org/) proof for a Nostr event. The proof is evidence that the event existed by the time of a particular Bitcoin block.

**Warning:** the current specification is labelled `draft`, `optional` and `unrecommended`. Its header says it is vulnerable to one specific attack and needs an update. The text does not describe the attack. Treat the format as a historical reference and do not adopt it for new work until the specification is revised.

## How It Works

A proof is published as a separate kind 1040 event. Its `e` tag names the target event id, with a relay URL, and its `k` tag records the target event's kind. The OpenTimestamps proof must prove the target event id itself as its digest. The id is not hashed again.

The `content` holds the full `.ots` file, base64-encoded, with at least one Bitcoin attestation. The specification recommends exactly one attestation and no pending attestations, which add bytes without helping verification.

A verifier fetches the kind 1040 event, decodes its content and checks the proof against Bitcoin. A valid proof shows the event id was committed by the attested block. This sets a latest possible creation time for the event that does not depend on the author's own `created_at` value. It does not show that the event's content is true.

## History

An [October 11, 2023 commit](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e) changed where proofs live. Before it, a proof was an `ots` field attached to the event itself. After it, each proof is a separate kind 1040 event that points to its target.

## Primary Sources

- [Current NIP-03 specification](https://github.com/nostr-protocol/nips/blob/master/03.md)
- [October 11, 2023 commit moving proofs to kind 1040 events](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e)

## Mentioned in Newsletters

- [Newsletter #46 (2026-10-28): October 2023, events carry evidence and requests for work](/en/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)

## See Also

- [NIP-01: Basic Protocol](/en/topics/nip-01/)
