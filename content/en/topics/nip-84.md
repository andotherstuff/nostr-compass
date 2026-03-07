---
title: "NIP-84: Highlights"
date: 2026-02-18
draft: false
categories:
  - Content
  - Protocol
---

NIP-84 defines kind 9802 "highlight" events that let users mark and share passages they find valuable from long-form content on Nostr.

## How It Works

The `.content` field contains the highlighted text. Events reference their source material using `a` or `e` tags for Nostr-native content, or `r` tags for external URLs (clients should strip tracking parameters). Optional `p` tags attribute original authors, and an optional `context` tag provides surrounding text when the highlight is a portion of a larger passage.

For non-text media, the highlight content can be empty. That gives clients a way to point at an audio or video highlight while keeping the source reference in tags.

## Quote Highlights

Users can add a `comment` tag to create quote highlights, which render as quoted reposts. This prevents duplicate entries in microblogging clients. Within comments, `p`-tag mentions require a "mention" attribute to distinguish them from author/editor attributions, and `r`-tag URLs use a "source" attribute for origin references.

## Why It Matters

NIP-84 separates the highlighted passage from the surrounding discussion. A client can render the selected text as the primary object, then treat commentary as optional metadata instead of mixing both into a regular note.

That is useful for reading and research tools because it preserves the exact excerpt. Two readers can comment on the same article and still produce portable highlight events that other clients understand.

## Interop Notes

Attribution tags are more important than they look. A `p` tag with an `author` or `editor` role tells clients who created the source material, while a `mention` role inside a quote comment means something different. If clients collapse those cases together, they can mislabel the highlighted source or incorrectly notify people.

---

**Primary sources:**
- [NIP-84 Specification](https://github.com/nostr-protocol/nips/blob/master/84.md)

**Mentioned in:**
- [Newsletter #10: Releases](/en/newsletters/2026-02-18-newsletter/#prism-share-anything-to-nostr-from-android)

**See also:**
- [NIP-94: File Metadata](/en/topics/nip-94/)
