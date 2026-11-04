---
title: "NIP-73: External Content IDs"
date: 2026-02-04
draft: false
categories:
  - Protocol
  - Discovery
  - Metadata
---

NIP-73 defines a standard way to reference external content inside Nostr events. It uses `i` tags for the identifier itself and `k` tags for the identifier type, so clients can group discussion around the same book, website, podcast episode, location, hashtag, or blockchain object. The [current specification](https://github.com/nostr-protocol/nips/blob/master/73.md) is marked draft and optional.

## How It Works

An event using NIP-73 includes an `i` tag with a normalized external identifier and a `k` tag naming the identifier family. Clients can query relays for one exact subject through `i` or for a whole family through `k`. NIP-73 adds no event kind of its own. Comments, reviews and other events carry the tags.

Tag fragment, not a complete event:

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

A webpage puts its normalized URL in `i` and sets `k` to `web`. The spec covers several identifier families, including:

- normalized web URLs with no fragment
- ISBNs for books
- ISANs for films
- DOIs
- geohashes and ISO 3166 country or subdivision codes
- podcast feed, episode, and publisher GUIDs
- hashtags
- blockchain transaction and address identifiers

## Normalization Rules

Matching depends on identical strings, so the spec sets one written form for each family. Examples from the spec:

- geohashes use `geo:<value>` and must be lowercase
- country and subdivision codes use `iso3166:<code>` and must be uppercase
- ISBNs omit hyphens
- DOIs are lowercase
- web URLs drop fragments
- blockchain transaction hashes use lowercase hex

Normalization fixes how a single identifier is written. It does not merge aliases. Edition-specific ISBNs and URLs that normalize to different strings stay separate identifiers, so discussion of one book or article can still spread across several `i` values.

## URL Hints

An `i` tag may include an optional URL hint as its third array element, which is the second value after the tag name. A client with no custom renderer for that identifier type can use the hint as a fallback link.

Tag fragment: `["i", "isbn:9780765382030", "<url-hint>"]`

The author chooses the hint. It is not part of the identity, it proves no ownership, and it does not name a canonical site.

## Trust and Context

Two events with the same identifier end up in the same conversation, and the shared identifier establishes nothing more. A signed event identifies its author. It does not authenticate the book, site or podcast publisher it references, and it does not show who controls them.

What an `i` tag means depends on the event. In [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md) comments, uppercase `I`/`K` mark the root scope and lowercase `i`/`k` mark the parent. That thread structure comes from NIP-22, and NIP-73 defines no comment kind. [NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md) uses `i` for external identities in profiles, so not every `i` tag is a NIP-73 subject.

[NIP-85](/en/topics/nip-85/) Trusted Assertions can also target NIP-73 identifiers such as books, websites, hashtags, and locations.

## Implementations

rust-nostr's [nip73.rs at commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) parses known prefixes into a typed `ExternalContentId` and turns an optional hint into a typed URL. It writes the third tag element only when a hint exists. Its tests keep hyphenated ISBNs: the parser strips the prefix and stores the rest without applying spec normalization, so typed parsing does not guarantee canonical strings. It keeps chain IDs out of the family, mapping `ethereum:100:tx:<hash>` to `ethereum:tx`. That revision has no `iso3166` country variant.

Amethyst's [DisplayExternalId.kt at commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) sends geohash, hashtag and URL identifiers to dedicated displays and shows other supported types as a generic scope chip. A URL opens the app's own thread route for that page. With previews disabled, normal rendering shows a plain link chip and requests no preview. With previews enabled, fetching a missing preview can contact the target site. Neither file shows how a released version behaves.

---

**Primary sources:**
- [NIP-73 Specification](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Adds ISO 3166 country and subdivision codes
- [rust-nostr nip73.rs at commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs)
- [Amethyst DisplayExternalId.kt at commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt)

**Mentioned in:**
- [Newsletter #47: NIP Deep Dive](/en/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)
- [Newsletter #45](/en/newsletters/2026-10-21-newsletter/#feather)
- [Newsletter #43](/en/newsletters/2026-10-07-newsletter/#protocol-and-spec-work)
- [Newsletter #37: August 2025](/en/newsletters/2026-08-26-newsletter/#august-2025)
- [Newsletter #8: NIP Updates](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [Newsletter #10: NIP-85 Deep Dive](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #36: Comments (NIP-22)](/en/newsletters/2026-08-19-newsletter/#comments-nip-22)
- [Newsletter #38: NIP Deep Dive](/en/newsletters/2026-09-02-newsletter/#reactions-nip-25)
- [Newsletter #40: NIP-73 podcast-medium filters](/en/newsletters/2026-09-16-newsletter/#nip-73-proposes-podcast-medium-filters)
- [Newsletter #42: September 2024 external content](/en/newsletters/2026-09-30-newsletter/#september-2024-posts-acquire-richer-context)

**See also:**
- [NIP-31: Dealing with unknown event kinds](/en/topics/nip-31/)
- [NIP-22: Comment](/en/topics/nip-22/)
- [NIP-39: External Identities in Profiles](/en/topics/nip-39/)
- [NIP-85: Trusted Assertions](/en/topics/nip-85/)
