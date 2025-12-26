---
title: "NIP-59: Gift Wrap"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-59 definieert gift wrapping, een techniek voor het verbergen van de afzender van een event door het te verpakken in lagen van encryptie met een wegwerp-identiteit.

## Structuur

Een gift-wrapped event heeft drie lagen:

1. **Rumor** - De originele niet-ondertekende event-inhoud
2. **Seal** (kind 13) - De rumor versleuteld naar de ontvanger, ondertekend door de echte afzender
3. **Gift Wrap** (kind 1059) - De seal versleuteld naar de ontvanger, ondertekend door een willekeurige wegwerpsleutel

De buitenste laag gebruikt een willekeurig sleutelpaar dat alleen voor dit bericht is gegenereerd, zodat waarnemers het niet kunnen koppelen aan de afzender.

## Waarom Drie Lagen?

- De **rumor** bevat de daadwerkelijke content
- De **seal** bewijst de echte afzender (alleen zichtbaar voor ontvanger)
- De **gift wrap** verbergt de afzender voor relays en waarnemers

## Verwijderingsondersteuning

Gift wrap events kunnen nu worden verwijderd via NIP-09/NIP-62 verwijderingsverzoeken. Dit is toegevoegd om gebruikers in staat te stellen verpakte berichten van relays te verwijderen.

## Gebruiksscenario's

- Privé directe berichten (NIP-17)
- Anonieme tips of klokkenluiden
- Elk scenario waar afzenderprivacy belangrijk is

---

**Primaire bronnen:**
- [NIP-59 Specificatie](https://github.com/nostr-protocol/nips/blob/master/59.md)

**Vermeld in:**
- [Nieuwsbrief #1: Nieuws](/nl/newsletters/2025-12-17-newsletter/#news)
- [Nieuwsbrief #1: NIP Updates](/nl/newsletters/2025-12-17-newsletter/#nip-updates)

**Zie ook:**
- [NIP-17: Privé Directe Berichten](/nl/topics/nip-17/)
