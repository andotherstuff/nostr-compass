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
  "kind": 10011,
  "tags": [
    ["i", "github:username", "gist-id"],
    ["i", "twitter:handle", "tweet-id"]
  ]
}
```

Clients reconstruct the proof URL from the platform and proof value, then check that the external post contains the user's `npub`. That keeps the claim portable across clients without requiring a central verifier.

## Proof Model

The important detail is that NIP-39 proves control of two identities at once: the Nostr key and the external account. If either side of that proof disappears, verification becomes weaker. A deleted gist or tweet does not invalidate the historical event, but it does remove the live proof most clients depend on.

Another useful implementation point is fetch strategy. Since claims now live outside kind 0, clients can decide whether to request them only on profile detail views, only for followed users, or not at all. That avoids adding more weight to the already hot kind 0 path.

## Current Status

As of the current spec, identity claims live in dedicated kind 10011 events instead of kind 0 metadata. That separation came from the broader effort to slim down kind 0 profile fetches.

---

**Primary sources:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - Moved identity claims out of kind 0

**Mentioned in:**
- [Newsletter #9: NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12: Amethyst](/en/newsletters/2026-03-04-newsletter/#amethyst-nip-39-nip-c0-nip-66)

**See also:**
- [NIP-05: DNS-Based Verification](/en/topics/nip-05/)
