---
title: "NIP-71: Video Events"
date: 2026-01-13
draft: false
categories:
  - Media
  - Protocol
---

NIP-71 defines Nostr events for landscape and short-form video, including the playback metadata clients need to choose media, display previews, load captions, and preserve imported-source provenance. It covers immutable video posts and addressable videos whose metadata can be updated under a stable coordinate.

## Event Kinds

NIP-71 defines four event kinds divided into two categories based on aspect ratio and addressability.

Regular video events use kind 21 for horizontal (landscape) videos and kind 22 for vertical (portrait/shorts) videos. These are standard Nostr events with immutable content once published.

Addressable video events use kind 34235 for horizontal videos and kind 34236 for vertical videos. These are parameterized replaceable events identified by the combination of pubkey, kind, and `d` tag. Publishing a new event with the same identifiers replaces the previous version, allowing metadata updates.

## Structure

A complete addressable video event includes an identifier, descriptive tags, and one or more `imeta` tags describing playable media variants.

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
    ["imeta", "url https://example.com/video.mp4", "m video/mp4", "dim 1920x1080", "image https://example.com/thumbnail.jpg", "duration 300"],
    ["duration", "300"],
    ["origin", "youtube:dQw4w9WgXcQ"]
  ],
  "content": "Extended description, transcript, or additional notes about the video.",
  "sig": "sig1234..."
}
```

The `d` tag provides a unique identifier within a publisher's videos of that kind. The `title` and `summary` tags provide descriptive text. Each `imeta` tag begins with a media URL and MIME type and can include dimensions, a SHA-256 hash, preview images, fallbacks, a media service, bitrate, and duration. Multiple `imeta` tags let a client select among files with different formats, resolutions, or hosts.

NIP-71 can also attach text tracks for captions, timed segments for chapters, `p` tags for participants, content warnings, hashtags, references, and imported-source metadata. A client should validate hashes when present, bound media downloads, and disclose external-host requests because a video server can observe playback traffic.

The `origin` tag tracks the source platform when importing content from other services. This preserves provenance when migrating videos from YouTube, Vimeo, or other platforms to Nostr hosting.

The `content` field can hold an extended description, full transcript, or any additional text associated with the video.

## Why Addressable Events Matter

Regular video events (kinds 21 and 22) are immutable once published. If you publish a video and later notice a typo in the title, want to update the thumbnail, or need to change the hosting URL because you migrated to a different video service, you cannot modify the original event. Your only option is to publish a new event with a new ID, which breaks any existing references and loses engagement metrics.

Addressable video events solve this problem by making the event replaceable. The combination of your pubkey, the event kind, and the `d` tag uniquely identifies your video. When you publish a new event with the same identifiers, relays replace the old version with the new one. Clients fetching your video always get the latest metadata.

This is particularly valuable for fixing metadata errors after publishing, updating thumbnails as you improve your branding, migrating video hosting URLs when changing providers, and importing content from discontinued platforms like Vine while preserving provenance through the `origin` tag.

An additional benefit is stable linking. Other events can keep referring to the same addressable video while the creator updates presentation details around it, which is cleaner than fragmenting comments and references across multiple immutable reposts.

## Tradeoffs

Replaceability helps metadata maintenance, but it also means clients need to decide how much historical state to preserve. If a creator changes the title or summary after publication, the newest event becomes canonical even though older clients may have indexed the previous version.

Kinds 21 and 22 still matter for applications that want an immutable publication record. NIP-71 does not force every video workflow into the replaceable model.

## Implementations

[Amethyst](https://github.com/vitorpamplona/amethyst/blob/96bec0cc7c1df4c05d4208fb1cfd6aac06fe97e7/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip71Video/VideoEvent.kt) parses video metadata, separates video and audio tracks, and chooses a playable variant. [Wisp](https://github.com/barrydeen/wisp/blob/b48be58271131c6062be2cc5449777cdd4fe6d31/app/src/main/kotlin/com/wisp/app/nostr/Nip71.kt) parses and builds regular landscape and short-video events with structured `imeta` fields. [Resonote](https://github.com/ikuradon/Resonote/blob/4ac14e1206608315d6507da405d4c5df3312d4d0/packages/core/src/nip71-video.ts) builds and parses all four video kinds along with variants, captions, chapters, participants, and origin metadata.

---

**Primary sources:**
- [NIP-71 Specification](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - Addressable video events update

**Mentioned in:**
- [Newsletter #41: NIP Deep Dive](/en/newsletters/2026-09-23-newsletter/#nip-deep-dive-custom-emoji-and-video-events)
- [Newsletter #5: NIP Updates](/en/newsletters/2026-01-13-newsletter/#nip-updates)
- [Newsletter #12: NoorNote](/en/newsletters/2026-03-04-newsletter/)
- [Newsletter #13: NIP Updates](/en/newsletters/2026-03-11-newsletter/#nip-updates)

**See also:**
- [NIP-94: File Metadata](/en/topics/nip-94/)
