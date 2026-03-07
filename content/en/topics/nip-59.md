---
title: "NIP-59: Gift Wrap"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-59 defines gift wrap, a way to encapsulate an event so relays and outside observers do not learn the real sender from the outer event they receive.

## Structure

A gift-wrapped event has three layers:

1. **Rumor** - The target event without a signature.
2. **Seal** (kind `13`) - The rumor encrypted to the recipient and signed by the real sender.
3. **Gift Wrap** (kind `1059`) - The seal encrypted again and signed by a random one-time key.

The seal must have empty tags. The outer gift wrap usually carries the recipient `p` tag so relays can route it.

## What It Hides

Gift wrap hides the sender from relays and network observers because the outer event is signed by a disposable key. The recipient, however, can still decrypt the inner seal and learn which long-term key signed it. So the privacy gain is metadata protection on the transport layer, not anonymity from the recipient.

The spec also recommends randomizing wrapper timestamps and, when possible, using relays that require authentication and only serve wrapped events to the intended recipient. Without those relay behaviors, recipient metadata can still leak.

## Operational Notes

Gift wrap is not a messaging protocol by itself. Other protocols, such as private messaging systems, use it as a building block.

Relays may choose not to store wrapped events for long because they are not publicly useful. The spec also allows proof-of-work on the outer wrapper when implementations want extra spam resistance.

## Use Cases

- Private direct messages (NIP-17)
- Friends-only notes (NIP-FR proposal)
- Push notification payloads (NIP-9a proposal)
- Any scenario requiring sender privacy from the network

---

**Primary sources:**
- [NIP-59 Specification](https://github.com/nostr-protocol/nips/blob/master/59.md)

**Mentioned in:**
- [Newsletter #8: NIP Deep Dive](/en/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-59-gift-wrap)
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #12: Open PRs](/en/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**See also:**
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
