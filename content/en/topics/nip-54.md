---
title: "NIP-54: Wiki"
date: 2025-12-31
draft: false
categories:
  - Protocol
  - Content
---

NIP-54 defines kind 30818 as an addressable event type for creating wiki articles and encyclopedia entries on Nostr. It enables decentralized, collaborative content creation where multiple authors can write about the same topics.

## How It Works

Wiki articles are identified by a normalized `d` tag (the article topic). Multiple people can write articles about the same subject, creating a decentralized knowledge base without central authority.

**D Tag Normalization:**
- Lowercase all letters
- Convert spaces to hyphens
- Remove punctuation and symbols
- Preserve non-ASCII characters and numbers

## Content Format

Articles use Asciidoc markup with two special features:

- **Wikilinks** (`[[target page]]`) - Links to other wiki articles across Nostr
- **Nostr links** - References to profiles or events per NIP-21

## Article Selection

When multiple versions of an article exist, clients prioritize based on:

1. Reactions (NIP-25) indicating community approval
2. Relay lists (NIP-51) for source ranking
3. Contact lists (NIP-02) forming recommendation networks

## Collaborative Features

- **Forking** - Create derivative versions of articles
- **Merge requests** (kind 818) - Propose changes to existing articles
- **Redirects** (kind 30819) - Point old topics to new ones
- **Deference markers** - Indicate preferred article versions

---

**Primary sources:**
- [NIP-54 Specification](https://github.com/nostr-protocol/nips/blob/master/54.md)

**Mentioned in:**
- [Newsletter #3: NIP Updates](/en/newsletters/2025-12-31-newsletter/#nip-updates)

**See also:**
- [NIP-51: Lists](/en/topics/nip-51/)
- [NIP-02: Follow List](/en/topics/nip-02/)
