---
title: "NIP-39: External Identities in Profiles"
date: 2026-02-11
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 defines how users attach external identity claims to their Nostr profiles using `i` tags. These tags link a Nostr pubkey to accounts on external platforms such as GitHub, Twitter, Mastodon, or Telegram.

## How It Works

Users publish identity claims in kind 10011 events as `i` tags. Each tag contains a `platform:identity` value plus a proof pointer that lets a client verify the claim:

```json
{
  "id": "5f1c7b7e2c6f3d4a9b0e6a2d8c1f7e3b4a6d9c0e1f2a3b4c5d6e7f8091a2b3c4",
  "pubkey": "3bf0c63fcb8d0d8b6a8fcb3c7f5cb2a972f8a0b5a3d6d8790bb2d4e4f0d6b1c2",
  "created_at": 1741699200,
  "kind": 10011,
  "tags": [
    ["i", "github:alice", "9f5df4e2a8b14c1f9e6d2b7c4a1e8f90"],
    ["i", "twitter:alice_dev", "1898123456789012345"]
  ],
  "content": "",
  "sig": "8f4c62d8a7e9b1c3d5f7091a2b4c6d8e0f1234567890abcdeffedcba09876543211223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

Clients reconstruct the proof URL from the platform and proof value, then check that the external post contains the user's `npub`. That keeps the claim portable across clients without requiring a central verifier.

## Proof Model

The important detail is that NIP-39 proves control of two identities at once: the Nostr key and the external account. If either side of that proof disappears, verification becomes weaker. A deleted gist or tweet does not invalidate the historical event, but it does remove the live proof most clients depend on.

Another useful implementation point is fetch strategy. Since claims now live outside kind 0, clients can decide whether to request them only on profile detail views, only for followed users, or not at all. That avoids adding more weight to the already hot kind 0 path.

## Implementations

- [Amethyst PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747) - Publishes external identities as dedicated kind 10011 events
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - Adds explicit kind 10011 registry reference to the NIP set

## Current Status

As of the current spec, identity claims live in dedicated kind 10011 events instead of kind 0 metadata. That separation came from the broader effort to slim down kind 0 profile fetches.

---

**Primary sources:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - Moved identity claims out of kind 0
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - Added explicit kind 10011 reference

**Mentioned in:**
- [Newsletter #9: NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12: Amethyst](/en/newsletters/2026-03-04-newsletter/#amethyst-nip-39-nip-c0-nip-66)
- [Newsletter #13: NIP Updates](/en/newsletters/2026-03-11-newsletter/#nip-updates)

**See also:**
- [NIP-05: DNS-Based Verification](/en/topics/nip-05/)
