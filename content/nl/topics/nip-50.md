---
title: "NIP-50: Search"
date: 2025-12-31
translationOf: /en/topics/nip-50.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Relay
---

NIP-50 definieert een algemene zoekmogelijkheid voor Nostr relays. Het voegt full-text-achtige query's toe boven op de exact-match filters van NIP-01.

## Hoe Het Werkt

Het protocol voegt een `search`-veld toe aan filterobjecten in `REQ`-berichten:

1. Clients sturen een menselijk leesbare querystring in, zoals `best nostr apps`.
2. Relays interpreteren die query tegen eventdata, vooral het veld `content`.
3. Resultaten worden gesorteerd op matchkwaliteit, niet op `created_at`.
4. `limit` wordt toegepast na sortering op relevantie.

Zoekfilters kunnen worden gecombineerd met `kinds`, `ids`, authors en andere normale filtervelden voor specifiekere query's.

## Zoekextensies

Relays kunnen optioneel deze extensieparameters ondersteunen:

- `include:spam` - Schakelt standaard spamfiltering uit
- `domain:<domain>` - Filtert op geverifieerd NIP-05-domein
- `language:<code>` - Filtert op ISO-taalcode
- `sentiment:<value>` - Filtert op negatief, neutraal of positief sentiment
- `nsfw:<true/false>` - Neemt NSFW-inhoud op of sluit die uit

Relays horen extensies die ze niet ondersteunen te negeren, dus clients moeten ze behandelen als hints, niet als garanties.

## Interop-notities

- Clients moeten relay-mogelijkheden controleren via het veld `supported_nips`
- Client-side verificatie van resultaten wordt aanbevolen
- Niet alle relays implementeren search; het blijft een optionele functie

Omdat ranking implementatie-afhankelijk is, kan dezelfde query verschillende resultaatsets teruggeven op verschillende relays. Clients die om recall geven, horen meer dan een search relay te bevragen en de resultaten samen te voegen.

## Waarom Het Belangrijk Is

Gestructureerde filters werken goed wanneer je al weet welke auteur, kind of tag je zoekt. Search is voor het omgekeerde geval: ontdekking. Dat maakt NIP-50 nuttig voor app-directory's, lange archieven en het doorzoeken van publieke notes, maar het betekent ook dat de zoekkwaliteit sterk afhangt van de indexering en spamfiltering van elke relay.

---

**Primaire bronnen:**
- [NIP-50 Specificatie](https://github.com/nostr-protocol/nips/blob/master/50.md)

**Vermeld in:**
- [Nieuwsbrief #3: Decemberoverzicht](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Nieuwsbrief #7: NIP-updates](/en/newsletters/2026-01-07-newsletter/#nip-updates)

**Zie ook:**
- [NIP-11: Relay Information](/nl/topics/nip-11/)
