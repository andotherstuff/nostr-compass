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
- [Amethyst](https://github.com/vitorpamplona/amethyst) wired [NIP-75](/en/topics/nip-75/) zap goals into the Live Activities screen via [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469): each live stream carries a fundraising goal header with a progress bar, a one-tap zap button, and a top-zappers leaderboard computed from kind `9735` zap receipts bound to the stream's kind `30311` event. Follow-up [PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) adds NIP-53 proof-of-agreement and event builders, and [PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486) ships a dedicated Live Streams feed screen with filtering and discovery.
- [NoorNote v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) adds one-tap zapping from live-stream cards where the sats appear in the stream's chat overlay via NIP-53.

---

**Primary sources:**
- [NIP-53 Specification](https://github.com/nostr-protocol/nips/blob/master/53.md)
- [Amethyst PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) - Live stream goal header and top-zappers leaderboard
- [Amethyst PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) - NIP-53 proof of agreement and event builders

**Mentioned in:**
- [Newsletter #18: WaveFunc launch](/en/newsletters/2026-04-15-newsletter/#wavefunc-v010-and-v011-launch-nostr-internet-radio)
- [Newsletter #19: Amethyst live stream zap goals](/en/newsletters/2026-04-22-newsletter/#amethyst-ships-marmot-mip-compliance-nip-72-communities-and-live-stream-zap-goals)
- [Newsletter #19: NoorNote v0.8.4](/en/newsletters/2026-04-22-newsletter/#noornote-v084-adds-scheduled-posts-and-live-stream-zapping)

**See also:**
- [NIP-29: Relay-based Groups](/en/topics/nip-29/)
- [NIP-75: Zap Goals](/en/topics/nip-75/)
- [NIP-57: Zaps](/en/topics/nip-57/)
- [NIP-C7: Chat Messages](/en/topics/nip-c7/)
