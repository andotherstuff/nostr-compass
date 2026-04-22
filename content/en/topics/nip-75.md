---
title: "NIP-75: Zap Goals"
date: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-75 defines a fundraising goal event that users can zap toward. A goal declares a target amount in millisatoshis and a list of relays where zap receipts for the goal are tallied. Any [NIP-57](/en/topics/nip-57/) zap that references the goal event counts toward its progress.

## How It Works

A zap goal is a `kind:9041` event. The `.content` is a human-readable description. The required tags are `amount` (target in millisats) and `relays` (the relay list used for tallying zap receipts). Optional tags include `closed_at` to cut off the tally at a given timestamp, `image`, and `summary`. The goal may also include an `r` or `a` tag linking to an external URL or an addressable event, and it may carry multiple beneficiary pubkeys via zap-split tags borrowed from NIP-57 appendix G.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1776500000,
  "kind": 9041,
  "tags": [
    ["relays", "wss://alicerelay.example.com", "wss://bobrelay.example.com"],
    ["amount", "210000"],
    ["image", "<image url>"],
    ["summary", "Nostrasia travel expenses"]
  ],
  "content": "Nostrasia travel expenses",
  "sig": "<128-char hex>"
}
```

Clients attach a zap to a goal by including an `e` tag pointing at the goal event inside the zap request. Goal progress is the sum of matched zap receipt amounts on the relays the goal specified. When `closed_at` is set, zap receipts published after that timestamp do not count.

## Implementations

- [Amethyst](https://github.com/vitorpamplona/amethyst) now renders goal progress bars and one-tap zap buttons inside live-stream headers via [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469), which wires NIP-75 into the NIP-53 Live Activities screen.

---

**Primary sources:**
- [NIP-75 Specification](https://github.com/nostr-protocol/nips/blob/master/75.md)
- [Amethyst PR #2469: live stream top zappers and goal header](https://github.com/vitorpamplona/amethyst/pull/2469)

**Mentioned in:**
- [Newsletter #19: Amethyst live stream zap goals](/en/newsletters/2026-04-22-newsletter/#amethyst-ships-marmot-mip-compliance-nip-72-communities-and-live-stream-zap-goals)
- [Newsletter #19: NIP Deep Dive on NIP-57](/en/newsletters/2026-04-22-newsletter/#nip-deep-dive-nip-57-zaps)

**See also:**
- [NIP-57: Lightning Zaps](/en/topics/nip-57/)
- [NIP-53: Live Activities](/en/topics/nip-53/)
