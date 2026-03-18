---
title: "NIP-54: Wiki"
date: 2025-12-31
draft: false
categories:
  - Protocol
  - Content
---

NIP-54 defines kind `30818` for wiki-style articles on Nostr. Multiple authors can publish entries for the same topic, so clients need ranking and trust heuristics instead of a single canonical page.

## How It Works

Wiki articles are identified by a normalized `d` tag that represents the topic. Multiple people can publish entries with the same normalized topic, creating an open wiki without a central editor.

**D Tag Normalization:**
- Lowercase letters that have case variants
- Convert whitespace to hyphens
- Remove punctuation and symbols
- Collapse repeated hyphens and trim leading or trailing hyphens
- Preserve non-ASCII letters and numbers

That normalization rule matters for interoperability. If two clients normalize the same title differently, they will query different topics and fragment the article set.

## Content Format

The canonical spec now uses Djot markup with two extra behaviors:

- **Nostr links** - References to profiles or events per NIP-21
- **Wikilinks** - Reference-style links without explicit targets resolve to normalized wiki article names

That change landed in [PR #2242](https://github.com/nostr-protocol/nips/pull/2242), which replaced the older Asciidoc-based text. The merged update also adds clearer examples for merge requests, redirects, and non-Latin `d` tag normalization.

## Article Selection

When multiple versions of an article exist, clients can prioritize based on:

1. Reactions (NIP-25) indicating community approval
2. Relay lists (NIP-51) for source ranking
3. Contact lists (NIP-02) forming recommendation networks

In practice, this means NIP-54 is not only a content format. It is also a client policy problem. Two clients can show different "best" articles for the same topic while both remain spec-compliant.

## Collaborative Features

- **Forking** - Create derivative versions of articles
- **Merge requests** (kind 818) - Propose changes to existing articles
- **Redirects** (kind 30819) - Point old topics to new ones
- **Deference markers** - Indicate preferred article versions

Forks and deference markers let authors acknowledge better versions without deleting their own work. That matters in a network where old revisions can remain available across many relays.

---

**Primary sources:**
- [NIP-54 Specification](https://github.com/nostr-protocol/nips/blob/master/54.md)
- [PR #2177: Internationalized d-tag normalization](https://github.com/nostr-protocol/nips/pull/2177)
- [PR #2242: Switch from Asciidoc to Djot](https://github.com/nostr-protocol/nips/pull/2242)

**Mentioned in:**
- [Newsletter #3: NIP Updates](/en/newsletters/2025-12-31-newsletter/#nip-updates)
- [Newsletter #12: Open PRs](/en/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)
- [Newsletter #14: NIP Deep Dive](/en/newsletters/2026-03-18-newsletter/#nip-deep-dive-nip-54-wiki)

**See also:**
- [NIP-51: Lists](/en/topics/nip-51/)
- [NIP-02: Follow List](/en/topics/nip-02/)
