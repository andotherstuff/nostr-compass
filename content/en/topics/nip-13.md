---
title: "NIP-13: Proof of Work"
date: 2026-01-28
draft: false
categories:
  - NIP
  - Spam Prevention
---

NIP-13 defines a proof-of-work system for Nostr events, requiring computational effort to create events as a spam prevention mechanism.

## How It Works

Proof of work is demonstrated by finding an event ID (SHA256 hash) with a specified number of leading zero bits:

1. **Difficulty**: Measured in leading zero bits (e.g., 20 bits = 2^20 attempts on average)
2. **Nonce Tag**: Events include a `nonce` tag with the nonce value and target difficulty
3. **Verification**: Relays and clients can quickly verify the work was done

```json
{
  "tags": [["nonce", "12345", "20"]],
  ...
}
```

## Difficulty Levels

| Bits | Average Attempts | Typical Use |
|------|------------------|-------------|
| 8 | 256 | Minimal spam deterrent |
| 16 | 65,536 | Light filtering |
| 20 | 1,048,576 | Moderate protection |
| 24 | 16,777,216 | Strong spam resistance |

## Why It Matters

- **Relay Admission**: Relays can require minimum PoW for event acceptance
- **Rate Limiting**: Higher difficulty for actions like account registration
- **Spam Filtering**: Clients can prioritize high-PoW events in feeds
- **Reputation Bootstrap**: New accounts can demonstrate commitment via PoW

The useful property is asymmetric cost. Creating many acceptable events becomes expensive for the sender, while checking the proof remains cheap for relays and clients.

## Tradeoffs

- Favors users with powerful hardware
- Energy consumption concerns
- Doesn't prevent all spam, just raises the cost

PoW also shifts spam resistance from account identity to compute availability. That can help in permissionless environments, but it does not distinguish between a legitimate new user and a well-funded spammer.

---

**Primary sources:**
- [NIP-13 Specification](https://github.com/nostr-protocol/nips/blob/master/13.md)

**Mentioned in:**
- [Newsletter #7: News](/en/newsletters/2026-01-28-newsletter/#news)
- [Newsletter #12: News](/en/newsletters/2026-03-04-newsletter/#news)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
