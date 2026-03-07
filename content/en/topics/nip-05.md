---
title: "NIP-05: Domain Verification"
date: 2026-02-04
draft: false
description: "NIP-05 enables human-readable identifiers for Nostr pubkeys through domain verification."
categories:
  - Identity
  - Discovery
---

NIP-05 maps Nostr public keys to human-readable internet identifiers like `user@example.com`. It gives users a DNS-backed identity hint that clients can verify over HTTPS.

## How It Works

A user claims an identifier by adding a `nip05` field to their profile metadata. The identifier follows the format `name@domain`. Clients verify the claim by fetching `https://domain/.well-known/nostr.json` and checking that the name maps to the user's pubkey.

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

NIP-05 is not a global username registry. It proves control of a domain name and web server path, not legal identity or long-term account continuity. If a domain owner changes the mapping later, clients will verify the new mapping unless they keep prior state.

That makes NIP-05 useful for discoverability and reputation, but weaker than users often assume. A good client should treat it as verified domain control, not proof that a person or organization is who they claim to be.

## Relay Hints

The `nostr.json` file can optionally include a `relays` object mapping pubkeys to arrays of relay URLs. This helps clients discover where to find events from a particular user.

## Interop Notes

The lowercase requirement matters more than it looks. Mixed-case names or pubkeys can work in one implementation and fail in another, so current clients should expect lowercase names and lowercase hex keys in `nostr.json`.

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

**Mentioned in:**
- [Newsletter #8: NIP Updates](/en/newsletters/2026-02-04-newsletter/#nip-updates)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
- [NIP-65: Relay List Metadata](/en/topics/nip-65/)
