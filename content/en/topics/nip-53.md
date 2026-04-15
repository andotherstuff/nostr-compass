---
title: "NIP-53: Live Activities"
date: 2026-04-15
draft: false
categories:
  - Protocol
  - Live Streaming
description: "NIP-53 defines how live stream metadata is published on Nostr using kind 30311 addressable events."
---

NIP-53 defines the standard event format for live streaming metadata on Nostr. A stream is announced as a kind `30311` addressable event, so clients can discover it, show its current state, and link chat back to the stream context.

## How It Works

Each stream uses a kind `30311` event with a `d` tag as its stable identifier. The event typically includes title and summary text, a `streaming` tag with the playback URL, and a `status` tag (`planned`, `live`, or `ended`). Because this is an addressable event, updates replace prior metadata for the same `d` value instead of creating an unbounded event trail.

The event can include topic tags (`t`), participant references (`p`), and optional participant count fields. Live chat is carried by kind `1311` events that reference the stream with an `a` tag, which keeps chat messages tied to one specific live activity record.

## Implementations

- [Shosho](https://github.com/r0d8lsh0p/shosho-releases) publishes live stream metadata and chat around Nostr-native live broadcasts.
- [Zap.stream](https://zap.stream/) uses Nostr events for stream discovery and interaction.
- [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) uses kind `1311` live chat events in its internet radio context.

---

**Primary sources:**
- [NIP-53 Specification](https://github.com/nostr-protocol/nips/blob/master/53.md)

**Mentioned in:**
- [Newsletter #18: WaveFunc launch](/en/newsletters/2026-04-15-newsletter/#wavefunc-v010-and-v011-launch-nostr-internet-radio)

**See also:**
- [NIP-29: Relay-based Groups](/en/topics/nip-29/)
- [NIP-C7: Chat Messages](/en/topics/nip-c7/)
