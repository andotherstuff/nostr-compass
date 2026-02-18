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

## Quote Highlights

Users can add a `comment` tag to create quote highlights, which render as quoted reposts. This prevents duplicate entries in microblogging clients. Within comments, `p`-tag mentions require a "mention" attribute to distinguish them from author/editor attributions, and `r`-tag URLs use a "source" attribute for origin references.

---

**Primary sources:**
- [NIP-84 Specification](https://github.com/nostr-protocol/nips/blob/master/84.md)

**Mentioned in:**
- [Newsletter #10: Releases](/en/newsletters/2026-02-18-newsletter/#prism-share-anything-to-nostr-from-android)

**See also:**
- [NIP-94: File Metadata](/en/topics/nip-94/)
