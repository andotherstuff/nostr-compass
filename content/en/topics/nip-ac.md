---
title: "NIP-AC: P2P Voice and Video Calls"
date: 2026-04-08
description: "Defines a protocol for peer-to-peer voice and video calls using Nostr for signaling and WebRTC for media transport."
---

NIP-AC proposes a protocol for peer-to-peer voice and video calls over Nostr. The spec uses Nostr events for call signaling (offers, answers, ICE candidates) and WebRTC for the actual media transport, keeping the call setup decentralized while using standard browser APIs for audio and video.

## How It Works

A caller publishes a call offer event containing a WebRTC Session Description Protocol (SDP) offer, tagged with the callee's pubkey. The callee responds with an SDP answer event. Both parties exchange ICE candidate events to negotiate the network path. Once the WebRTC connection is established, media flows directly between peers without relay involvement.

The signaling events are encrypted so relays cannot observe who is calling whom. The call state machine handles offer, answer, reject, busy, and hangup transitions.

## Implementations

- [Amethyst](https://github.com/vitorpamplona/amethyst) is building NIP-AC support with a call state machine test suite and stale call offer handling.

---

**Primary sources:**
- [NIP-AC PR #2301](https://github.com/nostr-protocol/nips/pull/2301) - P2P Voice and Video Calls over WebRTC

**Mentioned in:**
- [Nostr Compass #17 (2026-04-08)](/en/newsletters/2026-04-08-newsletter/)

**See also:**
- [NIP-44 (Encrypted Payloads)](/en/topics/nip-44/)
