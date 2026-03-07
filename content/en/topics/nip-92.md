---
title: "NIP-92: Media Attachments"
date: 2025-12-31
draft: false
categories:
  - Media
  - Protocol
---

NIP-92 enables users to attach media files to Nostr events by including URLs alongside inline metadata tags that describe those resources.

## How It Works

Users place media URLs directly in event content, for example in a kind `1` text note. A matching `imeta` tag then adds machine-readable details for that exact URL. Clients can use the metadata to render previews, reserve layout space, and avoid guessing file properties after the note is already on screen.

Each `imeta` tag should match one URL in the event content. Clients may ignore tags that do not match, which gives implementations a simple rule for rejecting stale or malformed metadata.

## The imeta Tag

Each `imeta` tag must have a `url` and at least one other field. Supported fields include:

- `url` - The media URL (required)
- `m` - MIME type of the file
- `dim` - Image dimensions (width x height)
- `blurhash` - Blurhash for preview generation
- `alt` - Alt text description for accessibility
- `x` - SHA-256 hash (from NIP-94)
- `fallback` - Alternative URLs if primary fails

Because `imeta` may carry fields from [NIP-94: File Metadata](/en/topics/nip-94/), clients can reuse the same MIME type, dimensions, hash, and accessibility text they would already understand for standalone file metadata events.

## Why It Matters

The most immediate benefit is better rendering before download. If `dim` is present, clients can reserve the right amount of space for an image or video instead of reflowing the timeline after the file loads. If `blurhash` is present, they can show a low-cost preview first. If `alt` is present, the attachment stays usable for screen-reader and low-vision users.

NIP-92 also lets clients keep the post itself as the source of truth. The URL remains in `content`, so older clients still show a plain link, while newer clients can upgrade the same note into a richer media card.

## Interop Notes

NIP-92 is inline metadata, not a separate media object format. If a client needs a reusable file record with its own event, [NIP-94: File Metadata](/en/topics/nip-94/) is the better fit.

## Example

```json
["imeta",
  "url https://example.com/image.jpg",
  "m image/jpeg",
  "dim 1920x1080",
  "blurhash LKO2?U%2Tw=w]~RBVZRi}^Xu%LRj"
]
```

---

**Primary sources:**
- [NIP-92 Specification](https://github.com/nostr-protocol/nips/blob/master/92.md)
- [Primal Android PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) - A concrete client implementation for dimensions and aspect-ratio handling

**Mentioned in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #6: News](/en/newsletters/2026-01-21-newsletter/#news)

**See also:**
- [NIP-94: File Metadata](/en/topics/nip-94/)
