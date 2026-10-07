---
title: "NIP-05: Domain Verification"
date: 2026-02-04
draft: false
description: "NIP-05 enables human-readable identifiers for Nostr pubkeys through domain verification."
categories:
  - Identity
  - Discovery
---

NIP-05 associates Nostr public keys with human-readable internet identifiers like `user@example.com`. Clients compare a signed profile claim with an HTTPS name-to-key mapping hosted by the named domain.

## How It Works

A user claims an identifier by adding a `nip05` field to their profile metadata. The identifier follows the format `name@domain`. Clients verify the claim by fetching `https://domain/.well-known/nostr.json?name=user` and checking that the name maps to the signed profile author's lowercase hexadecimal key. The endpoint must not redirect; clients must ignore redirects.

The JSON file at the well-known path contains a `names` object mapping local names to hex pubkeys:

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

When verification succeeds, clients can display the identifier instead of or alongside the npub. Some clients show a verification indicator, while others show the identifier as plain text and leave trust decisions to the reader.

## Trust Model

NIP-05 is not a global username registry. A successful lookup establishes that the domain's mapping matches the profile author's claim at lookup time. It does not establish legal identity or permanent ownership of the identifier. A changed mapping must not replace a followed public key.

That makes NIP-05 useful for discoverability and reputation, but weaker than users often assume. Following an account stays anchored to its public key; the domain-backed name is a mutable association. The server can observe name lookups and their network origins.

## Relay Hints

The `nostr.json` file can optionally include a `relays` object mapping pubkeys to arrays of relay URLs. This helps clients discover where to find events from a particular user.

## Interop Notes

The lowercase requirement matters more than it looks. The identifier local part uses `a-z0-9-_.`, and returned public keys are lowercase hexadecimal. Client parser tolerance is separate from this specified format.

Another practical detail is the special `_` name, which lets a domain map the bare identifier form like `_@example.com` or just `example.com` in clients that support it. Not every client exposes that form the same way, so users still get the most consistent results with explicit `name@domain` identifiers.

## Implementation Status

Most major clients support NIP-05 verification:
- Damus, Amethyst, Primal display verified identifiers
- Many relay services offer NIP-05 identifiers as a feature
- Numerous free and paid NIP-05 providers exist

---

**Primary sources:**
- [NIP-05 Specification](https://github.com/nostr-protocol/nips/blob/master/05.md)
- [PR #2208](https://github.com/nostr-protocol/nips/pull/2208) - lowercase requirement for names and hex keys
- [nostr-tools NIP-05 commit](https://github.com/nbd-wtf/nostr-tools/commit/1ce00bd3b6909f78f212a7a172cf845b55280599)
- [Cordn repository](https://github.com/Cordn-msg/cordn-web) - Android onboarding and NIP-05 profile links

**Mentioned in:**
- [Newsletter #43: NIP-05 and NIP-24](/en/newsletters/2026-10-07-newsletter/#nip-deep-dive-nip-05-and-nip-24)
- [Newsletter #43](/en/newsletters/2026-10-07-newsletter/#new-projects)
- [Newsletter #8: NIP Updates](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [Newsletter #13: Amethyst](/en/newsletters/2026-03-11-newsletter/#amethyst)
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/en/newsletters/2026-06-17-newsletter/#amethyst-v1-12-0-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter #33: Lead stories](/en/newsletters/2026-07-29-newsletter/#top-stories)
- [Newsletter #33: Six Years of Nostr Julys](/en/newsletters/2026-07-29-newsletter/#six-years-of-nostr-julys)
- [Newsletter #36: Nostter adds bookmark lists, profile badges, and Blossom uploads](/en/newsletters/2026-08-19-newsletter/#nostter-adds-bookmark-lists-profile-badges-and-blossom-uploads)
- [Newsletter #37: NoorNote v1.3.6: profile statuses and classified listings](/en/newsletters/2026-08-26-newsletter/#noornote-v136-profile-statuses-and-classified-listings)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
- [NIP-65: Relay List Metadata](/en/topics/nip-65/)
