---
title: "NIP-73: External Content IDs"
date: 2026-02-04
draft: false
categories:
  - Protocol
  - Discovery
  - Metadata
---

NIP-73 defines a standard way to reference external content inside Nostr events. It uses `i` tags for the identifier itself and `k` tags for the identifier type, so clients can group discussion around the same book, website, podcast episode, location, hashtag, or blockchain object.

## How It Works

An event using NIP-73 includes an `i` tag containing a normalized external identifier and a `k` tag describing what kind of identifier it is. Clients can then query for all events that reference the same subject.

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

The spec covers several identifier families, including:

- normalized web URLs with no fragment
- ISBNs for books
- ISANs for films
- geohashes and ISO 3166 country or subdivision codes
- podcast feed, episode, and publisher GUIDs
- hashtags
- blockchain transaction and address identifiers

## Normalization Rules

The main reader-facing detail in NIP-73 is normalization. The same subject should map to one canonical string, otherwise clients split discussion across multiple identifiers that mean the same thing.

Examples from the spec:

- geohashes use `geo:<value>` and must be lowercase
- country and subdivision codes use `iso3166:<code>` and must be uppercase
- ISBNs omit hyphens
- web URLs drop fragments
- blockchain transaction hashes use lowercase hex

That sounds small, but it is the difference between one shared conversation and several incompatible indexes.

## Useful Patterns

NIP-73 is a general reference layer, not a content format. A long-form note can point to a book ISBN, a review can point to a film ISAN, and a local post can point to a geohash or country code without inventing a custom tag each time.

The spec also allows an optional URL hint as the second value of an `i` tag. That gives clients a fallback link when they do not have a custom renderer for the identifier type.

## Why It Matters

Nostr already has strong internal references for events and profiles. NIP-73 extends that idea to things outside Nostr. Once identifiers are normalized, comments, ratings, highlights, and trusted assertions can all attach to the same external subject across different clients.

This is also why NIP-85 builds on NIP-73. Trusted Assertions can rate not only users and events, but also NIP-73 identifiers such as books, websites, hashtags, and locations.

---

**Primary sources:**
- [NIP-73 Specification](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Adds ISO 3166 country and subdivision codes

**Mentioned in:**
- [Newsletter #8: NIP Updates](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [Newsletter #10: NIP-85 Deep Dive](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)

**See also:**
- [NIP-85: Trusted Assertions](/en/topics/nip-85/)
