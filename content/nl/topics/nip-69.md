---
title: "NIP-69: Peer-to-Peer Handel"
date: 2025-12-17
translationDate: 2026-03-07
translationOf: /en/topics/nip-69.md
draft: false
categories:
  - Handel
  - Protocol
---

NIP-69 definieert een protocol voor peer-to-peer handel via Nostr, waarmee een uniform orderboek over meerdere platforms ontstaat in plaats van gefragmenteerde liquiditeitspools.

## Hoe het werkt

NIP-69 gebruikt adresseerbare kind 38383-events voor koop- en verkooporders. Het adresseerbare formaat is belangrijk omdat een order in de loop van de tijd meerdere statussen kan doorlopen terwijl het via de `d`-tag dezelfde logische identiteit behoudt.

## Orderstructuur

Orders gebruiken tags om handelsparameters op te geven:

- `d` - Order-ID
- `k` - Ordertype (koop/verkoop)
- `f` - Fiatvaluta (ISO 4217-code)
- `amt` - Bitcoin-bedrag in satoshis
- `fa` - Fiatbedrag
- `pm` - Geaccepteerde betaalmethoden
- `premium` - Prijspremie- of kortingspercentage
- `network` - Bitcoin-netwerk (mainnet, testnet, signet, regtest)
- `layer` - Afwikkellaag (onchain, lightning, liquid)
- `expiration` - Wanneer de order verloopt

## Orderlevenscyclus

Orders doorlopen deze statussen:
- `pending` - Open en beschikbaar voor matching
- `in-progress` - Handel gestart met een tegenpartij
- `success` - Handel voltooid
- `canceled` - Ingetrokken door de maker
- `expired` - Voorbij de vervaltijd

De specificatie maakt onderscheid tussen twee tijdslimieten. `expires_at` markeert wanneer een pending-order niet langer als open moet worden beschouwd, terwijl `expiration` relays een timestamp geeft die zij met [NIP-40](/nl/topics/nip-40/) kunnen gebruiken om verouderde order-events volledig te verwijderen.

## Waarom dit belangrijk is

NIP-69 is een interoperabiliteitsspel. Mostro, lnp2pBot, RoboSats, Peach en andere P2P-handelsystemen kunnen orders in een gedeeld eventformaat publiceren in plaats van liquiditeit opgesloten te houden in losse apps.

De optionele `g`-tag maakt ook lokale, face-to-face handel mogelijk zonder de rest van het orderschema te veranderen. Dat is nuttig omdat lokale cash trades geografische filtering nodig hebben, terwijl online Lightning trades dat niet hebben.

## Beveiliging en vertrouwen

De `bond`-tag specificeert een waarborgsom die beide partijen moeten betalen, wat bescherming biedt tegen afhaken of fraude.

Dat neemt het tegenpartijrisico niet weg. Betalingsgeschillen, fiatfraude, reputatie en custodyregels blijven op applicatieniveau liggen. NIP-69 standaardiseert het publiceren van orders, niet de geschillenafhandeling.

---

**Primaire bronnen:**
- [NIP-69-specificatie](https://github.com/nostr-protocol/nips/blob/master/69.md)
- [Mostro Protocol Specification](https://mostro.network/protocol/)

**Vermeld in:**
- [Nieuwsbrief #1: NIP Updates](/nl/newsletters/2025-12-17-newsletter/#nip-updates)
- [Nieuwsbrief #1: Releases](/nl/newsletters/2025-12-17-newsletter/#releases)
- [Nieuwsbrief #2: Nieuws](/nl/newsletters/2025-12-24-newsletter/#news)

**Zie ook:**
- [NIP-40: Expiration Timestamp](/nl/topics/nip-40/)
