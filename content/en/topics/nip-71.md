---
title: "NIP-71: Video Events"
date: 2026-01-13
draft: false
categories:
  - Media
  - Protocol
---

NIP-71 defines event kinds for video content on Nostr, enabling video sharing with proper metadata support. The specification covers both regular video events and addressable video events, with the latter added in January 2026 to allow creators to update video metadata without republishing.

## Event Kinds

NIP-71 defines four event kinds divided into two categories based on aspect ratio and addressability.

Regular video events use kind 21 for horizontal (landscape) videos and kind 22 for vertical (portrait/shorts) videos. These are standard Nostr events with immutable content once published.

Addressable video events use kind 34235 for horizontal videos and kind 34236 for vertical videos. These are parameterized replaceable events identified by the combination of pubkey, kind, and `d` tag. Publishing a new event with the same identifiers replaces the previous version, allowing metadata updates.

## Structure

A complete addressable video event includes identification fields, metadata tags, and the video content reference.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 34235,
  "tags": [
    ["d", "my-video-2026-01"],
    ["title", "Introduction to Nostr Video"],
    ["summary", "A walkthrough of NIP-71 video events"],
    ["url", "https://example.com/video.mp4"],
    ["thumb", "https://example.com/thumbnail.jpg"],
    ["duration", "300"],
    ["dim", "1920x1080"],
    ["origin", "youtube:dQw4w9WgXcQ"]
  ],
  "content": "Extended description, transcript, or additional notes about the video.",
  "sig": "sig1234..."
}
```

The `d` tag provides a unique identifier within your videos of that kind, so you can have multiple addressable videos by using different `d` values. The `title` and `summary` tags provide the video title and a short description for display in clients. The `url` tag points to the actual video file, while `thumb` provides a preview image. The `duration` tag specifies the length in seconds, and `dim` optionally specifies the video dimensions.

The `origin` tag tracks the source platform when importing content from other services. This preserves provenance when migrating videos from YouTube, Vimeo, or other platforms to Nostr hosting.

The `content` field can hold an extended description, full transcript, or any additional text associated with the video.

## Why Addressable Events Matter

Regular video events (kinds 21 and 22) are immutable once published. If you publish a video and later notice a typo in the title, want to update the thumbnail, or need to change the hosting URL because you migrated to a different video service, you cannot modify the original event. Your only option is to publish a new event with a new ID, which breaks any existing references and loses engagement metrics.

Addressable video events solve this problem by making the event replaceable. The combination of your pubkey, the event kind, and the `d` tag uniquely identifies your video. When you publish a new event with the same identifiers, relays replace the old version with the new one. Clients fetching your video always get the latest metadata.

This is particularly valuable for fixing metadata errors after publishing, updating thumbnails as you improve your branding, migrating video hosting URLs when changing providers, and importing content from discontinued platforms like Vine while preserving provenance through the `origin` tag.

## Implementations

Addressable video events (kinds 34235 and 34236) are currently implemented in Amethyst and nostrvine. Both clients can create, display, and update addressable video events.

---

**Primary sources:**
- [NIP-71 Specification](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - Addressable video events update

**Mentioned in:**
- [Newsletter #5: NIP Updates](/en/newsletters/2026-01-13-newsletter/#nip-updates)

**See also:**
- [NIP-94: File Metadata](/en/topics/nip-94/)
