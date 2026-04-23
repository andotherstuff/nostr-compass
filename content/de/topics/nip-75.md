---
title: "NIP-75: Zap Goals"
date: 2026-04-22
translationOf: /en/topics/nip-75.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-75 definiert ein Fundraising-Goal-Event, auf das Nutzer zappen können. Ein Goal deklariert einen Zielbetrag in millisatoshis und eine Liste von Relays, auf denen die Zap-Receipts für dieses Goal zusammengezählt werden. Jeder [NIP-57](/de/topics/nip-57/) zap, der das Goal-Event referenziert, zählt für seinen Fortschritt.

## Funktionsweise

Ein Zap Goal ist ein `kind:9041`-Event. Der Wert von `.content` ist eine menschenlesbare Beschreibung. Erforderliche Tags sind `amount` für das Ziel in millisats und `relays` für die Relay-Liste, die zum Zählen der Zap-Receipts verwendet wird. Optionale Tags sind `closed_at`, um das Tallying ab einem bestimmten Timestamp zu beenden, sowie `image` und `summary`. Das Goal kann außerdem ein `r`- oder `a`-Tag enthalten, das auf eine externe URL oder ein addressable Event verweist, und mehrere Begünstigten-pubkeys über Zap-Split-Tags tragen, die aus Appendix G von NIP-57 übernommen wurden.

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

Clients hängen einen zap an ein Goal, indem sie im Zap Request ein `e`-Tag mit Verweis auf das Goal-Event einfügen. Der Fortschritt des Goals ist die Summe der passenden Zap-Receipt-Beträge auf den Relays, die das Goal festgelegt hat. Wenn `closed_at` gesetzt ist, zählen Zap-Receipts, die nach diesem Timestamp veröffentlicht werden, nicht mehr.

## Implementierungen

- [Amethyst](https://github.com/vitorpamplona/amethyst) rendert jetzt Goal-Fortschrittsbalken und One-Tap-Zap-Buttons in Livestream-Headern über [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469), das NIP-75 in den NIP-53-Live-Activities-Screen integriert.

---

**Primärquellen:**
- [NIP-75 Specification](https://github.com/nostr-protocol/nips/blob/master/75.md)
- [Amethyst PR #2469: live stream top zappers and goal header](https://github.com/vitorpamplona/amethyst/pull/2469)

**Erwähnt in:**
- [Newsletter #19: Amethyst live stream zap goals](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NIP Deep Dive on NIP-57](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-57: Lightning Zaps](/de/topics/nip-57/)
- [NIP-53: Live Activities](/de/topics/nip-53/)
