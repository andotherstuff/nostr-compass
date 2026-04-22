---
title: "NIP-21: nostr: URI Scheme"
date: 2026-04-22
draft: false
categories:
  - Protocol
  - Interoperability
---

NIP-21 defines the `nostr:` URI scheme, a standard way for applications, websites, and operating systems to register interest in opening Nostr identifiers such as `npub`, `nprofile`, `nevent`, and `naddr` through whichever Nostr client the user has registered as a handler.

## How It Works

A `nostr:` URI is the scheme prefix followed by any of the [NIP-19](/en/topics/nip-19/) bech32 identifiers except `nsec`. Clients and operating systems treat the scheme the same way they treat `mailto:` or `tel:`: registering as a handler lets the user click a `nostr:` link anywhere in the system and have it open in their Nostr client of choice.

Examples from the specification:

- `nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9` points to a user profile
- `nostr:nprofile1...` points to a user profile with relay hints bundled in
- `nostr:nevent1...` points to a specific event with relay hints
- `nostr:naddr1...` points to a parameterised replaceable event (such as a long-form article)

## Linking HTML Pages to Nostr Entities

NIP-21 also specifies two useful `<link>` conventions for web pages that correspond to Nostr entities. A page that serves the same content as a Nostr event (for example a blog post rendered from a [NIP-23](/en/topics/nip-23/) `kind:30023` article) can include a `<link rel="alternate">` pointing at the Nostr URI. A profile page can include a `<link rel="me">` or `<link rel="author">` pointing at an `nprofile` to assert Nostr-based authorship.

## Why It Matters

The scheme is the interoperability layer that lets any Nostr identifier become a working link outside of a single client's UI. Browser extensions, mobile OS handlers, and desktop shells can all route `nostr:` URIs to whichever client the user has installed, which makes it possible to share a profile or event by pasting a URI anywhere without losing the ability to open it in a Nostr-native way.

## Implementations

Support for `nostr:` URIs is broad across the client ecosystem, including the major web, mobile, and desktop Nostr clients. Browser extensions such as [nos2x](https://github.com/fiatjaf/nos2x) and [Alby](https://github.com/getAlby/lightning-browser-extension) handle URI registration on desktop browsers.

---

**Primary sources:**

- [NIP-21 Specification](https://github.com/nostr-protocol/nips/blob/master/21.md)

**Mentioned in:**

- [Newsletter #19: Nostrability migrates to NIP-34](/en/newsletters/2026-04-22-newsletter/#nostrability-migrates-to-nip-34-and-opens-19-per-nip-interop-trackers)

**See also:**

- [NIP-19: bech32-encoded entities](/en/topics/nip-19/)
- [NIP-23: Long-form content](/en/topics/nip-23/)
