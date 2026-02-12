---
title: "NIP-39: External Identities in Profiles"
date: 2026-02-11
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 defines how users attach external identity claims to their Nostr profiles using `i` tags. These tags link a Nostr pubkey to accounts on external platforms like GitHub, Twitter, or DNS domains.

## How It Works

Users publish identity claims as `i` tags. Each tag contains a platform identifier and a proof URL where the external account links back to the Nostr pubkey, establishing bidirectional verification:

```json
{
  "tags": [
    ["i", "github:username", "https://gist.github.com/username/proof"],
    ["i", "twitter:handle", "https://twitter.com/handle/status/proof_tweet_id"]
  ]
}
```

Clients verify claims by fetching the proof URL and checking that it contains the user's Nostr pubkey. This creates a web of identity connections without requiring centralized verification services.

## Recent Changes

As of February 2026, [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) extracted identity tags from kind 0 (user metadata) events to a dedicated kind 10011. The move was part of vitorpamplona's kind 0 slimming campaign, motivated by low adoption: almost no clients implemented `i` tag verification, yet every kind 0 fetch carried the overhead. The new kind 10011 lets interested clients fetch identity claims separately.

---

**Primary sources:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)

**Mentioned in:**
- [Newsletter #9: NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)

**See also:**
- [NIP-05: DNS-Based Verification](/en/topics/nip-05/)
