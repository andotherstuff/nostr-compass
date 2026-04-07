---
title: "NIP-23: Long-form Content"
date: 2026-04-08
description: "Defines kind 30023 for long-form text content on Nostr, supporting Markdown articles with metadata tags."
---

NIP-23 defines kind `30023` for long-form text content on Nostr. Unlike kind `1` short notes, long-form events are parameterized replaceable events (keyed by a `d` tag), support Markdown formatting, and include metadata tags for titles, summaries, images, and publication dates.

## How It Works

A long-form event uses kind `30023` with a `d` tag as a unique identifier, allowing the author to update the content by publishing a new event with the same `d` tag. The `content` field contains Markdown text. Standard tags include `title`, `summary`, `image` (header image URL), `published_at` (original publication timestamp), and `t` (hashtags). Because the event is parameterized replaceable, relays store only the latest version per `d` tag per author.

## Key Tags

- `d` - unique article identifier (slug)
- `title` - article title
- `summary` - short description
- `image` - header image URL
- `published_at` - original publication unix timestamp (distinct from `created_at` which updates on each edit)
- `t` - hashtag/topic tags

## Implementations

- [Habla](https://habla.news) - Long-form content reader and publisher
- [YakiHonne](https://yakihonne.com) - Long-form content platform
- [Highlighter](https://highlighter.com) - Reading and annotation tool

---

**Primary sources:**
- [NIP-23 specification](https://github.com/nostr-protocol/nips/blob/master/23.md)

**See also:**
- [NIP-01 (Basic Protocol)](/en/topics/nip-01/)
