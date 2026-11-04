---
title: "NIP-87: Ecash Mint Discoverability"
date: 2026-01-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---

NIP-87 defines how ecash mints (Cashu and Fedimint) can announce themselves on Nostr, and how users can recommend mints to others.

## Event Kinds

- **kind 38172** - Cashu mint announcement (published by mint operators)
- **kind 38173** - Fedimint announcement (published by mint operators)
- **kind 38000** - Mint recommendation (published by users)

## How It Works

1. **Mint operators** publish their mint's URL, supported features, and network (mainnet/testnet)
2. **Users** who trust a mint publish recommendations with optional reviews
3. **Other users** query for recommendations from people they follow to discover trusted mints

## Cashu Mint Announcement

```json
{
  "id": "<event-id>",
  "pubkey": "<mint-operator-pubkey>",
  "created_at": 1736200000,
  "kind": 38172,
  "tags": [
    ["d", "<mint-pubkey>"],
    ["u", "https://mint.example.com"],
    ["nuts", "1,2,3,4,5,6,7"],
    ["n", "mainnet"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

The `nuts` tag lists supported NUTs (Notation, Usage, and Terminology specs for Cashu).

The `d` tag should be the mint's Cashu pubkey, which gives clients one stable identifier for discovery even if the mint later changes metadata or republishes its announcement.

## User Recommendations

```json
{
  "id": "<event-id>",
  "pubkey": "<recommender-pubkey>",
  "created_at": 1736200000,
  "kind": 38000,
  "tags": [
    ["k", "38172"],
    ["d", "<mint-identifier>"],
    ["a", "38172:mint-pubkey:<d-tag>", "wss://relay"]
  ],
  "content": "I've used this mint for months, very reliable",
  "sig": "<signature>"
}
```

Users can include reviews in the `content` field and point to specific mint announcement events.

Recommendation events are parameterized replaceable events. That is useful because a user can revise a recommendation, update their review text, or stop endorsing a mint without leaving several stale recommendation events behind.

## Trust Model

NIP-87 does not tell clients which mint is safe. It gives them a way to combine operator-published metadata with social recommendations from accounts the user already trusts.

That distinction matters because direct queries for mint announcement events can be noisy or malicious. The spec explicitly warns clients to use spam-prevention measures or high-quality relays when bypassing social recommendations and querying announcements directly.

## Interop Notes

Cashu and Fedimint use different announcement kinds because they expose different connection details. Cashu announcements publish mint URLs and supported NUTs, while Fedimint announcements publish invite codes and supported federation modules. A wallet that supports both needs to parse both formats.

---

**Primary sources:**
- [NIP-87 Specification](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Mentioned in:**
- [Newsletter #4: Releases](/en/newsletters/2026-01-07-newsletter/#releases)
- [Newsletter #7: Zeus](/en/newsletters/2026-01-28-newsletter/)

**See also:**
- [Cashu](/en/topics/cashu/)
- [NIP-60: Cashu Wallet](/en/topics/nip-60/)
