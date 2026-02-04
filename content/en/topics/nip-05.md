---
title: "NIP-05 (Domain Verification)"
date: 2026-02-04
description: "NIP-05 enables human-readable identifiers for Nostr pubkeys through domain verification."
---

NIP-05 maps Nostr public keys to human-readable internet identifiers like `user@example.com`. This provides a way to verify identity through domain ownership without requiring trust in a central authority.

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

When verification succeeds, clients can display the identifier instead of or alongside the npub. Some clients show a checkmark or other indicator for verified identifiers.

## Relay Hints

The `nostr.json` file can optionally include a `relays` object mapping pubkeys to arrays of relay URLs. This helps clients discover where to find events from a particular user.

## Implementations

Most major clients support NIP-05 verification:
- Damus, Amethyst, Primal display verified identifiers
- Many relay services offer NIP-05 identifiers as a feature
- Numerous free and paid NIP-05 providers exist

## Primary Sources

- [NIP-05 Specification](https://github.com/nostr-protocol/nips/blob/master/05.md)

## Mentioned In

- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - PR requiring lowercase for hex keys and names
