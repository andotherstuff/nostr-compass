---
title: "Marmot Protocol"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot is a protocol for end-to-end encrypted group messaging on Nostr. It combines Nostr's identity and relay network with MLS for group key management, forward secrecy, and post-compromise security.

## How It Works

Marmot uses Nostr for identity, relay transport, and event distribution, then layers MLS on top for group membership changes and message encryption. Unlike [NIP-17](/en/topics/nip-17/), which focuses on one-to-one messaging, Marmot is built for groups where members join, leave, or rotate keys over time.

## Why It Matters

MLS gives Marmot properties that Nostr's direct-message schemes do not provide on their own: group state evolution, member removal semantics, and recovery after compromise through later key updates.

That division of labor is the useful insight. Nostr solves identity and transport in an open network. MLS solves authenticated group key agreement. Marmot is the glue layer between them.

## Implementation Status

The protocol remains experimental, but it now has multiple implementations and active application use. MDK is the main Rust reference stack, `marmot-ts` brings the model to TypeScript, and applications such as White Noise, Pika, and Vector have been using Marmot-compatible components.

Recent work has focused on hardening and interop. Audit-driven fixes landed in early 2026, and MIP-03 introduced deterministic commit resolution so clients can converge when concurrent group state changes race across relays.

---

**Primary sources:**
- [Marmot Protocol Repository](https://github.com/marmot-protocol/marmot)
- [MLS Protocol](https://messaginglayersecurity.rocks/)
- [Marmot Development Kit](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: Releases](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #4](/en/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**See also:**
- [MLS (Message Layer Security)](/en/topics/mls/)
- [MIP-05: Privacy-Preserving Push Notifications](/en/topics/mip-05/)
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
- [NIP-59: Gift Wrap](/en/topics/nip-59/)
