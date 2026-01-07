---
title: "NIP-89: Recommended Application Handlers"
date: 2026-01-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

NIP-89 defines how applications can announce their capabilities and how users can recommend apps that handle specific event kinds.

## Event Kinds

- **kind 31990** - Application handler (published by app developers)
- **kind 31989** - App recommendation (published by users)

## How It Works

1. **Applications** publish handler events describing which event kinds they support and how to open content
2. **Users** recommend apps they use for specific event kinds
3. **Clients** query recommendations to offer "open in..." functionality for unknown event types

## Application Handler

```json
{
  "id": "<event-id>",
  "pubkey": "<app-developer-pubkey>",
  "created_at": 1736200000,
  "kind": 31990,
  "tags": [
    ["d", "<app-identifier>"],
    ["k", "30023"],
    ["web", "https://app.example.com/a/<bech32>", "naddr"],
    ["ios", "appname://open/<bech32>"]
  ],
  "content": "{\"name\": \"My App\", \"picture\": \"...\"}",
  "sig": "<signature>"
}
```

The `k` tags specify supported event kinds. URL templates use `<bech32>` as a placeholder for NIP-19 encoded entities.

## User Recommendation

```json
{
  "id": "<event-id>",
  "pubkey": "<user-pubkey>",
  "created_at": 1736200000,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:app-pubkey:identifier", "wss://relay", "web"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

The `d` tag is the event kind being recommended. Multiple `a` tags can recommend different apps for different platforms.

## Use Cases

- Discovering apps that can display longform articles (kind 30023)
- Finding clients that support specific event types
- Cross-client "open in..." functionality
- Detecting client capabilities for encryption support

---

**Primary sources:**
- [NIP-89 Specification](https://github.com/nostr-protocol/nips/blob/master/89.md)

**Mentioned in:**
- [Newsletter #4: NIP Deep Dive](/en/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)

**See also:**
- [NIP-19: Bech32-Encoded Entities](/en/topics/nip-19/)
