---
title: "NIP-AC: WebRTC Signaling"
date: 2026-04-08
description: "An open proposal for WebRTC signaling over Nostr relays."
---

NIP-AC is an open proposal for exchanging WebRTC signaling over Nostr. Relays carry the connection setup events; media travels directly between peers once WebRTC connects.

## How It Works

A peer publishes provisional ephemeral events for pings, connection requests, offers, answers, and ICE candidates. A `p` tag addresses the other peer, while an `e` tag groups messages into a session. A replaceable kind `30600` event advertises discoverable WebRTC endpoints.

Relays SHOULD broadcast the ephemeral signaling events and MUST NOT store them. Applications needing confidentiality SHOULD encrypt offer, answer, and candidate content with [NIP-44](/en/topics/nip-44/). Encryption does not hide all relay-visible metadata, including event authors and recipients.

The proposal remains open, and its event numbers are provisional.

---

**Primary sources:**
- [NIP-AC PR #2461](https://github.com/nostr-protocol/nips/pull/2461) - Current open WebRTC-signaling proposal

**Mentioned in:**
- [Newsletter #39: Nostr Implementation Possibilities](/en/newsletters/2026-09-09-newsletter/#nostr-implementation-possibilities)
- [Nostr Compass #17 (2026-04-08)](/en/newsletters/2026-04-08-newsletter/)

**See also:**
- [NIP-44 (Encrypted Payloads)](/en/topics/nip-44/)
