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

---

**Primary sources:**
- [NIP-87 Specification](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Mentioned in:**
- [Newsletter #4: Releases](/en/newsletters/2026-01-07-newsletter/#releases)

**See also:**
- [NIP-60: Cashu Wallet](/en/topics/nip-60/)
