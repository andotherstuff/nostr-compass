---
title: "NIP-F4: Podcasts"
date: 2026-06-03
draft: false
categories:
  - NIPs
  - Protocol
  - Media
---

NIP-F4 defines how Nostr clients reference, surface, and socially interact with podcast episodes. Merged on 2026-05-28 after two years and three months in draft, the spec uses kind 54 events for episodes and designs around the existing RSS podcasting stack as a complementary layer.

## How It Works

A kind 54 podcast episode event carries a `title` tag, an optional `image` tag, a `description` tag, one or more `imeta` tags for the audio file (URL, mime type, hash, duration, bitrate, language code, fallback URLs, NIP-96 service flag), `t` topic tags, and a NIP-31 `alt` tag for fallback display.

The load-bearing design choice is the `i` tag, which carries the episode's RSS GUID using `podcast:item:guid:<guid>` format. This lets:

- A Nostr client display a kind 54 event and link it back to the same episode in any RSS-aware podcast app
- An RSS-aware Nostr client surface an existing podcast's episodes as kind 54 events without forcing the podcaster to migrate hosting
- Cross-protocol comment threading via the Podcasting 2.0 `<podcast:socialInteract>` and `<podcast:chat>` tags

## Coexistence with RSS

The two-year debate on the PR thread (with Podcasting 2.0 co-author Dave Jones, Alex Gleason, fiatjaf, Mike Terenzio, Pablo F7z, and Jeff Gardner) settled on coexistence. Nostr provides the social and discovery layer while RSS keeps the source of truth for the audio file and feed metadata. Nostr does not duplicate the RSS distribution layer.

This contrasts with earlier attempts to replace RSS (JSONFeed, RSS 3.0, proprietary podcast APIs). The Podcasting 2.0 namespace already supports `<podcast:socialInteract>` referencing Nostr events by note ID, so an RSS feed can declare its companion Nostr discussion thread without requiring Nostr to mirror the feed itself.

## Example Event

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["imeta", "url https://podcast.example.com/audio/ep42.mp3", "m audio/mpeg", "x b2e0a7a82ac9f3f3a71f1d9a78c381d5be9d1cf19dce258765c17c8a76287c93", "duration 4523", "bitrate 192000", "l en ISO-639-1"],
    ["i", "podcast:item:guid:9b2a4c7d-1e3f-4a5b-8c9d-0e1f2a3b4c5d"],
    ["t", "podcasting"],
    ["alt", "Podcast episode: Why RSS Won (43 min)"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

## Implementations

- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - Dedicated podcast screen with episode list and inline player (first major client implementation, May 2026)
- [Wavlake](https://wavlake.com) - Largest Nostr-native music and podcasting platform, expected to align with kind 54 for podcast content
- [Fountain](https://fountain.fm) - Bitcoin podcast app, expected to bridge RSS and NIP-F4

## Open Questions

The merged spec keeps several design questions for implementations to converge on:

- Per-creator pubkeys are recommended but not required, so platforms like Wavlake that publish many creators under one pubkey remain valid
- Per-episode comments and discussion use NIP-22 generic threading and kind 1 timeline notes rather than a dedicated episode-comment kind
- Per-podcast metadata (host, network, language, license) lives either in the publisher's kind 0 metadata or in a separate kind 54 podcast-level record

---

**Primary sources:**
- [NIP-F4 Specification](https://github.com/nostr-protocol/nips/blob/master/F4.md)
- [PR #1093](https://github.com/nostr-protocol/nips/pull/1093) - Original proposal, merged 2026-05-28 after two-year discussion
- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - First major client implementation

**Mentioned in:**
- [Newsletter #25: NIP Updates and Deep Dive](/en/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-f4-podcasts)

**See also:**
- [NIP-22 (Comments)](https://github.com/nostr-protocol/nips/blob/master/22.md)
- [NIP-31 (Alt tags)](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [NIP-94 (File Metadata)](/en/topics/nip-94/)
- [NIP-96 (HTTP File Storage)](/en/topics/nip-96/)
- [Podcasting 2.0](https://podcasting2.org)
