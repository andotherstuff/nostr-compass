---
title: "NIP-53: Live Activities"
date: 2026-04-15
draft: false
categories:
  - Protocol
  - Live Streaming
description: "NIP-53 defines live streams, meeting spaces, conference events, presence, and live chat as Nostr addressable events."
---

NIP-53 defines the standard event surface for live activities on Nostr: live streams, persistent meeting spaces, scheduled conference events, listener presence, and the live chat channel that ties chat messages to a specific live activity record. Five event kinds work together to advertise what is happening live, who is participating, and where the audio or video is being served. Because every live activity is described as a Nostr event, any client can discover an activity, link to it from outside chat, and publish into its chat channel without a forge-specific API.

## How It Works

A live stream is announced as a kind `30311` addressable event. Its `d` tag is the stable identifier for the activity, the `streaming` tag points at the playback URL, and the `status` tag carries one of `planned`, `live`, or `ended`. Because the event is addressable, providers update it in place as participants join and leave. Each `p` tag carries a pubkey, a relay hint, a displayable role marker (`Host`, `Speaker`, `Participant`), and an optional proof of agreement field. The event also carries `title`, `summary`, `image`, `t` hashtags, optional `current_participants`/`total_participants` counts, and `starts`/`ends` timestamps. Hosts can pin one or more chat messages by listing their event IDs in `pinned` tags.

A representative Nests-style audio room announcement looks like this:

```json
{
  "id": "8c1e6d7b3f2e9a4d5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a",
  "pubkey": "82341f882b6eabcd2ba7f1ef90aad961cf074af15b9ef44a09f9d2a8fbfbe6a2",
  "created_at": 1746540000,
  "kind": 30311,
  "tags": [
    ["d", "nests-room-2026-05-05-protocol-discussion"],
    ["title", "Protocol discussion: NIP-34 git workflows"],
    ["summary", "Open call for ngit, GitWorkshop, and joinmarket-ng maintainers"],
    ["streaming", "https://moq.amethyst.social/rooms/protocol-discussion-2026-05-05"],
    ["starts", "1746543600"],
    ["status", "live"],
    ["current_participants", "12"],
    ["service", "wss://nests.amethyst.social/"],
    ["p", "a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd", "wss://relay.damus.io", "Host", "f1e0d7a8b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6"],
    ["p", "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5", "wss://nos.lol", "Speaker"],
    ["p", "0057059046164d2238bbdbdf45fa2e106f59188289f6842d6bf362218ef4a58c", "", "Participant"],
    ["relays", "wss://relay.damus.io", "wss://nos.lol"],
    ["t", "nostr"],
    ["t", "nip-34"]
  ],
  "content": "",
  "sig": "5a3e8b7c1d2f4a6b9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c8b7a6f5e4d3c2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c8b7a6f5e4d3"
}
```

Providers SHOULD keep the published participant list small (under 1000 users) and select which participants get named when limits are hit; clients should treat the list as a sample, not a full roster. Once an activity ends, providers can delete the event or update it to summarize the activity and add a `recording` URL for async playback. Clients MAY treat any `status=live` event without an update for one hour as `ended`, which gives clients a recovery path when a host abandons a stream without explicitly closing it.

The proof-of-agreement field is the fifth term in each `p` tag. It is the SHA-256 of the activity's full `a` tag (`30311:pubkey:dTag`) signed by the participant's private key, encoded as hex. Without it, clients MAY display the participant as "invited" only. The mechanism prevents malicious event owners from listing well-known accounts in their participant list to lure followers into a fake event. In practice, clients that surface speaker leaderboards, fundraising progress, or zap totals SHOULD gate display on the proof so a fake roster cannot inflate apparent attendance.

Live chat uses kind `1311` events. Each chat message MUST include an `a` tag pointing at the activity record (`30311:pubkey:dTag`) so chat is bound to one specific live activity, with an optional relay hint and `root` marker. An `e` tag indicates the parent message in a threaded reply, and `q` tags carry [NIP-21](/en/topics/nip-21/) `nostr:` URI quotes when chat content cites events. The `naddr` form ([NIP-19](/en/topics/nip-19/)) is the canonical way to link to a live activity from outside chat, so a long-form post or note can deep-link to a specific stream and bring readers directly into the right chat overlay.

## Meeting Spaces and Conference Events

NIP-53 separates the persistent room from the scheduled event held inside it. A kind `30312` "Meeting Space" event defines a room with a `d` identifier, human-readable `room` name, `summary`, optional `image`, a `status` of `open`/`private`/`closed`, a `service` URL clients use to join, an optional `endpoint` for status/info APIs, hashtag `t` tags, one or more `p` tags advertising providers and their roles (Host, Moderator, Speaker), and optional preferred `relays`. Rooms MAY persist when not in use, and private rooms MAY specify access control such as invite-only or payment-required policies in their service metadata. The split lets a provider stand up a permanent boardroom URL, an "office hours" room that is open every weekday at the same hour, or a private members area, and re-use that addressable record for many sequential events.

A kind `30313` "Conference Event" represents a scheduled or ongoing meeting inside a room. The event has its own `d` identifier and an `a` tag pointing back to the parent space (`30312:pubkey:room-id`) with an optional relay hint. It carries `title`, `summary`, `image`, `starts`, optional `ends`, a `status` of `planned`/`live`/`ended`, optional participant counts, and per-event `p` tags with roles distinct from the room's. Like live streams, status SHOULD be updated regularly while the meeting is live, and stale `live` events without updates for one hour MAY be treated as ended. The room/event split is what gives NIP-53 conference-grade scheduling: a single room hosts many `30313` events over time, each with its own start, end, and roster, while the room's hosts and providers stay stable.

Listener presence is a separate kind `10312` regular replaceable event. The presence event has an `a` tag pointing at the activity (a live stream, conference event, or meeting space) and an optional `hand` tag with value `1` to signal a raised hand. Replaceable means each user has exactly one current presence record, so a participant can signal presence in one room at a time, and clients SHOULD filter presence events older than a chosen window. The replaceable shape is intentional: presence is ephemeral, so the event is meant to be overwritten by a fresh presence record on each update.

## Event Kinds

- **30311** - Live Streaming Event (addressable)
- **30312** - Meeting Space (addressable; persistent room definition)
- **30313** - Conference Event (addressable; meeting held inside a meeting space)
- **1311** - Live Chat Message
- **10312** - Room Presence (replaceable; "I am here right now")

## Composing With Other NIPs

The Nostr live-activity surface is intentionally thin: NIP-53 advertises the activity, while other NIPs handle adjacent concerns. Zaps to live streams use [NIP-57](/en/topics/nip-57/) zap receipts (kind `9735`) bound to the stream's `30311` event, which is what Amethyst's top-zappers leaderboard reads. Fundraising goals attached to a stream use [NIP-75](/en/topics/nip-75/) zap goals, surfaced as a progress-bar header on the live activity card. Video content recorded after the activity ends can be republished as [NIP-71](/en/topics/nip-71/) video events. Threaded chat replies follow [NIP-22](/en/topics/nip-22/) comment conventions when needed beyond simple `e` tags. Verified profiles in chat ride on [NIP-05](/en/topics/nip-05/) DNS-based identifiers, and remote signing for live participation can use [NIP-46](/en/topics/nip-46/) Nostr Connect so a streamer never has to paste an nsec into a streaming client.

## Implementations

- [Amethyst](https://github.com/vitorpamplona/amethyst) wired [NIP-75](/en/topics/nip-75/) zap goals into the Live Activities screen via [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469): each live stream carries a fundraising goal header with a progress bar, a one-tap zap button, and a top-zappers leaderboard computed from kind `9735` zap receipts bound to the stream's kind `30311` event. Follow-up [PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) adds NIP-53 proof-of-agreement and event builders, and [PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486) ships a dedicated Live Streams feed screen with filtering and discovery. The Nests audio-room work shipping in [#19](/en/newsletters/2026-04-22-newsletter/#amethyst-ships-marmot-mip-compliance-nip-72-communities-zap-goals-and-moq-audio-rooms) and [#20](/en/newsletters/2026-04-29-newsletter/#amethyst-advances-nests-audio-rooms-with-moq-interop-testing) builds on the kind `30312`/`30313` meeting-space surface, with Media over QUIC handling the real-time audio transport while NIP-53 events handle the Nostr-side signaling.
- [Zap.stream](https://zap.stream/) is the longest-running NIP-53 client, built by Kieran. It uses kind `30311` for stream discovery and kind `1311` for the live chat overlay, with Lightning zaps wired into the chat as a first-class interaction. The earliest deployment shipped at 21 sats per minute streaming, which made Zap.stream one of the original demonstrations that micropayments could ride directly on a live activity record.
- [Shosho](https://github.com/r0d8lsh0p/shosho-releases) is a mobile live-streaming app for Nostr with a long shipping cadence covered across Compass. v0.11.1 added recording and VOD capabilities, room presence indicators, threaded chat conversations, and Nostr Connect signing on iOS via [NIP-46](/en/topics/nip-46/). v0.12.0 added video Clips with in-player replies, custom emoji integration, thread protection against indirect mention spam, and a horizontal Twitch-style playback mode. v0.13.0 added MP4 replay downloads from stream card menus and [NIP-05](/en/topics/nip-05/) profile verification. v0.15.0 launched Shows (custom live stream info connected to OBS or any external encoder) and a TikTok-style vertical video carousel.
- [HiveTalk](https://hivetalk.org) is an open-source real-time video conferencing platform with Nostr and Lightning integration, hosted on the [hivetalksfu](https://github.com/hivetalk/hivetalksfu) repository. It uses NIP-53 to advertise rooms and the active conference inside them, with zaps as a payment rail. The companion [Swarm](https://github.com/HiveTalk/swarm) project adds a team relay with Blossom media mirroring and per-kind controls, which is useful when a HiveTalk deployment wants to keep meeting-related events on a private team relay.
- [Corny Chat](https://cornychat.com) is an open-source audio rooms client (the source code lives at [vicariousdrama/cornychat](https://github.com/vicariousdrama/cornychat)) built on the Jam project with Nostr and Lightning integration. It publishes meeting space and conference events, and its [datatypes documentation](https://cornychat.com/datatypes) extends NIP-53 with custom kinds for sound-effect lists, slide sets, link sets, and high scores, all of which compose with the standard live activity record.
- [nostrnests](https://nostrnests.com) is the original Clubhouse-style audio spaces project on Nostr, hosted at [nostrnests/nests](https://github.com/nostrnests/nests). It pre-dates the Amethyst Nests audio-room work and continues to operate as a NIP-53 deployment. The naming overlap with Amethyst's "Nests" feature is incidental: nostrnests is the standalone web product, while Amethyst Nests is the in-app experience inside the Amethyst Android client.
- [Swae](https://github.com/suhailsaqan/swae) is a mobile-first live streaming app on Nostr with Lightning zaps and Cashu payments. The project is in beta and explores how a live activity card can hand off both Lightning and Cashu micropayments at the same time, where the chat overlay carries zap receipts and Cashu nutzaps as routine first-class events.
- [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) is a Nostr-based internet radio directory and player covered in newsletter [#18](/en/newsletters/2026-04-15-newsletter/#wavefunc-v010-and-v011-launch-nostr-internet-radio). It uses kind `1311` live chat events around station playback alongside custom kinds (`31237` for station listings, `30078` for favorites, `1111` for station comments), so a station's running chat shares the same kind that streamers and audio-room providers use. WaveFunc also ships with a [NIP-60](/en/topics/nip-60/) Cashu wallet and Lightning donation flow.
- [NoorNote v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) added one-tap zapping from live-stream cards, where the sats appear in the stream's chat overlay via NIP-53. Covered in newsletter [#19](/en/newsletters/2026-04-22-newsletter/#noornote-v084-adds-scheduled-posts-and-live-stream-zapping). NoorNote shows that a general-purpose Nostr client can integrate live activity zapping without operating its own streaming server.

---

**Primary sources:**

- [NIP-53 Specification](https://github.com/nostr-protocol/nips/blob/master/53.md)
- [Amethyst PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) - live stream goal header, top-zappers leaderboard, and one-tap zap
- [Amethyst PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486) - dedicated Live Streams feed screen
- [Amethyst PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) - NIP-53 proof of agreement and event builders

**Mentioned in:**

- [Newsletter #18 (2026-04-15): WaveFunc v0.1.0 and v0.1.1 launch Nostr internet radio](/en/newsletters/2026-04-15-newsletter/#wavefunc-v010-and-v011-launch-nostr-internet-radio)
- [Newsletter #18 (2026-04-15): NIP Updates (NIP-53 changes)](/en/newsletters/2026-04-15-newsletter/#nip-updates)
- [Newsletter #19 (2026-04-22): Amethyst ships Marmot MIP compliance, NIP-72 communities, zap goals, and MoQ audio rooms](/en/newsletters/2026-04-22-newsletter/#amethyst-ships-marmot-mip-compliance-nip-72-communities-zap-goals-and-moq-audio-rooms)
- [Newsletter #19 (2026-04-22): NoorNote v0.8.4 adds Scheduled Posts and live stream zapping](/en/newsletters/2026-04-22-newsletter/#noornote-v084-adds-scheduled-posts-and-live-stream-zapping)
- [Newsletter #20 (2026-04-29): Amethyst advances Nests audio rooms with MoQ interop testing](/en/newsletters/2026-04-29-newsletter/#amethyst-advances-nests-audio-rooms-with-moq-interop-testing)

**See also:**

- [NIP-05: DNS-based identifiers](/en/topics/nip-05/)
- [NIP-19: bech32-encoded entities](/en/topics/nip-19/)
- [NIP-21: `nostr:` URI scheme](/en/topics/nip-21/)
- [NIP-22: Comments](/en/topics/nip-22/)
- [NIP-29: Relay-based Groups](/en/topics/nip-29/)
- [NIP-46: Nostr Remote Signing](/en/topics/nip-46/)
- [NIP-57: Zaps](/en/topics/nip-57/)
- [NIP-71: Video Events](/en/topics/nip-71/)
- [NIP-75: Zap Goals](/en/topics/nip-75/)
- [NIP-c7: Chat Messages](/en/topics/nip-c7/)
