---
title: "NIP-30: Custom Emoji"
date: 2026-03-04
draft: false
categories:
  - NIP
  - Social
---

NIP-30 defines how clients display custom emoji in Nostr events. Custom emoji are referenced in event content using shortcodes (`:shortcode:`) and resolved through `emoji` tags mapping each shortcode to an image URL.

## How It Works

An event using custom emoji includes `emoji` tags alongside the shortcode references in content:

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

Clients replace `:gleam:` and `:nostrich:` in the rendered content with inline images from the specified URLs. Shortcodes must be alphanumeric (with underscore separators allowed), and the image URLs should point to small, square images suitable for inline display.

## Emoji Sets

Custom emoji can be organized into named sets published as kind 30030 parameterized replaceable events. Each set groups related emoji under a `d` tag identifier:

```json
{
  "kind": 30030,
  "tags": [
    ["d", "nostr-animals"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"],
    ["emoji", "nostrcat", "https://example.com/nostrcat.png"]
  ]
}
```

A March 2026 update ([PR #2247](https://github.com/nostr-protocol/nips/pull/2247)) added optional emoji set address references in emoji tags, letting clients open the originating set for browsing or bookmarking when a user clicks an emoji.

## Interop Notes

Custom emoji are a presentation feature, not a transport guarantee. If a client does not understand NIP-30 or cannot fetch the image URL, it should still show the raw `:shortcode:` text. That fallback is why readable shortcodes matter.

The tag is event-local unless it references a set. Reusing `:fire:` in two different events does not imply a shared global meaning unless both point at the same image or set. Clients should resolve the emoji definition from the current event first.

## Reactions

NIP-30 custom emoji also work in kind 7 reaction events. A reaction with `content` set to a shortcode and a matching `emoji` tag renders as a custom emoji reaction on the referenced event:

```json
{
  "kind": 7,
  "content": ":fire:",
  "tags": [
    ["emoji", "fire", "https://example.com/fire.gif"],
    ["e", "<event-id>"]
  ]
}
```

---

**Primary sources:**
- [NIP-30 Specification](https://github.com/nostr-protocol/nips/blob/master/30.md)
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - Emoji set address in tags

**Mentioned in:**
- [Newsletter #12: NoorNote v0.5.x](/en/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [Newsletter #12: NIP Updates](/en/newsletters/2026-03-04-newsletter/#nip-updates)
