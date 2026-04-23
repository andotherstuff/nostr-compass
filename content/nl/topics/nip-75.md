---
title: "NIP-75: Zap Goals"
date: 2026-04-22
translationOf: /en/topics/nip-75.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-75 definieert een fondsenwervingsdoel-event waar gebruikers naartoe kunnen zappen. Een doel verklaart een target amount in millisatoshis en een lijst van relays waar zap receipts voor dat doel worden opgeteld. Elke [NIP-57](/nl/topics/nip-57/) zap die naar het goal-event verwijst telt mee voor de voortgang.

## Hoe Het Werkt

Een zap goal is een `kind:9041`-event. De `.content` is een mensleesbare beschrijving. De verplichte tags zijn `amount` (target in millisats) en `relays` (de relaylijst die wordt gebruikt om zap receipts op te tellen). Optionele tags zijn onder meer `closed_at` om het tellen op een bepaalde timestamp te stoppen, `image` en `summary`. Het doel kan ook een `r`- of `a`-tag bevatten die naar een externe URL of een addressable event verwijst, en het kan meerdere beneficiary pubkeys dragen via zap-split-tags uit appendix G van NIP-57.

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

Clients koppelen een zap aan een doel door een `e`-tag op te nemen die naar het goal-event wijst binnen het zap request. Goal progress is de som van gematchte zap receipt-bedragen op de relays die het doel heeft opgegeven. Wanneer `closed_at` is ingesteld, tellen zap receipts die na die timestamp zijn gepubliceerd niet mee.

## Implementaties

- [Amethyst](https://github.com/vitorpamplona/amethyst) rendert nu goal progress bars en one-tap zap buttons in live-stream headers via [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469), die NIP-75 in het NIP-53 Live Activities-scherm integreert.

---

**Primaire bronnen:**
- [NIP-75 Specification](https://github.com/nostr-protocol/nips/blob/master/75.md)
- [Amethyst PR #2469: live stream top zappers and goal header](https://github.com/vitorpamplona/amethyst/pull/2469)

**Vermeld in:**
- [Newsletter #19: Amethyst live stream zap goals](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NIP Deep Dive on NIP-57](/en/newsletters/2026-04-22-newsletter/)

**Zie ook:**
- [NIP-57: Lightning Zaps](/nl/topics/nip-57/)
- [NIP-53: Live Activities](/nl/topics/nip-53/)
