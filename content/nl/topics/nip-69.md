---
title: "NIP-69: Peer-to-Peer Handel"
date: 2025-12-17
draft: false
categories:
  - Handel
  - Protocol
---

NIP-69 definieert een protocol voor peer-to-peer handel via Nostr, wat een uniforme orderboek creëert over meerdere platforms in plaats van gefragmenteerde liquiditeitspools.

## Event Kind

- **Kind 38383** - P2P order events

## Orderstructuur

Orders gebruiken tags om handelsparameters te specificeren:

- `d` - Order-ID
- `k` - Ordertype (koop/verkoop)
- `f` - Fiat-valuta (ISO 4217 code)
- `amt` - Bitcoin-bedrag in satoshis
- `fa` - Fiat-bedrag
- `pm` - Geaccepteerde betaalmethoden
- `premium` - Prijspremie/korting percentage
- `network` - Afwikkelingslaag (onchain, lightning, liquid)
- `expiration` - Wanneer de order verloopt

## Orderlevenscyclus

Orders doorlopen statussen:
- `pending` - Open en beschikbaar voor matching
- `in-progress` - Handel gestart met tegenpartij
- `success` - Handel voltooid
- `canceled` - Ingetrokken door maker
- `expired` - Voorbij verloopdatum

## Beveiliging

De `bond` tag specificeert een waarborgsom die beide partijen moeten betalen, wat bescherming biedt tegen verlating of fraude.

---

**Primaire bronnen:**
- [NIP-69 Specificatie](https://github.com/nostr-protocol/nips/blob/master/69.md)

**Vermeld in:**
- [Nieuwsbrief #1: NIP Updates](/nl/newsletters/2025-12-17-newsletter/#nip-updates)
- [Nieuwsbrief #1: Releases](/nl/newsletters/2025-12-17-newsletter/#releases)
- [Nieuwsbrief #2: Nieuws](/nl/newsletters/2025-12-24-newsletter/#news)
