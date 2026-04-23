---
title: "NIP-75: Zap Goals"
date: 2026-04-22
translationOf: /en/topics/nip-75.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-75 definisce un evento di obiettivo di raccolta fondi verso cui gli utenti possono inviare zap. Un obiettivo dichiara un importo target in millisatoshi e una lista di relay sui quali vengono conteggiate le ricevute zap relative all'obiettivo. Qualunque zap [NIP-57](/it/topics/nip-57/) che faccia riferimento all'evento dell'obiettivo contribuisce al suo avanzamento.

## Come funziona

Uno zap goal è un evento `kind:9041`. Il `.content` è una descrizione leggibile da esseri umani. I tag richiesti sono `amount` (target in millisats) e `relays` (lista di relay usata per contare le ricevute zap). I tag facoltativi includono `closed_at` per chiudere il conteggio a un dato timestamp, `image` e `summary`. L'obiettivo puo anche includere un tag `r` o `a` che punta a un URL esterno o a un evento addressable e puo portare più pubkey beneficiarie tramite gli zap-split tag presi dall'appendice G di NIP-57.

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

I client collegano uno zap a un obiettivo includendo un tag `e` che punta all'evento dell'obiettivo dentro la zap request. L'avanzamento dell'obiettivo è la somma degli importi delle ricevute zap corrispondenti sui relay specificati dall'obiettivo. Quando è impostato `closed_at`, le ricevute zap pubblicate dopo quel timestamp non vengono conteggiate.

## Implementazioni

- [Amethyst](https://github.com/vitorpamplona/amethyst) ora mostra barre di avanzamento dell'obiettivo e pulsanti zap con un tocco nelle intestazioni dei live stream tramite [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469), che collega NIP-75 alla schermata Live Activities di NIP-53.

---

**Fonti primarie:**
- [Specifica NIP-75](https://github.com/nostr-protocol/nips/blob/master/75.md)
- [Amethyst PR #2469: live stream top zappers and goal header](https://github.com/vitorpamplona/amethyst/pull/2469)

**Menzionato in:**
- [Newsletter #19: obiettivi zap nei live stream di Amethyst](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: approfondimento NIP-57](/en/newsletters/2026-04-22-newsletter/)

**Vedi anche:**
- [NIP-57: Lightning Zaps](/it/topics/nip-57/)
- [NIP-53: Live Activities](/it/topics/nip-53/)
