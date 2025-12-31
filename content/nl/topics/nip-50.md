---
title: "NIP-50: Search"
date: 2025-12-31
translationOf: /en/topics/nip-50.md
translationDate: 2025-12-31
draft: false
categories:
  - Protocol
  - Relay
---

NIP-50 definieert een algemene zoekmogelijkheid voor Nostr relays, waardoor clients full-text zoekopdrachten kunnen uitvoeren die verder gaan dan gestructureerde queries op tags of IDs.

## Hoe Het Werkt

Het protocol voegt een `search`-veld toe aan filterobjecten in REQ-berichten:

1. Clients dienen menselijk leesbare zoekopdrachten in (bijv. "beste nostr apps")
2. Relays interpreteren en matchen queries tegen eventdata, voornamelijk het `content`-veld
3. Resultaten worden gerangschikt op relevantie in plaats van chronologische volgorde
4. Het `limit`-filter wordt toegepast na relevantiesortering

Zoekfilters kunnen worden gecombineerd met andere beperkingen zoals `kinds` en `ids` voor meer specifieke queries.

## Zoekextensies

Relays kunnen optioneel deze extensieparameters ondersteunen:

- `include:spam` - Schakelt standaard spamfiltering uit
- `domain:<domain>` - Filtert op geverifieerd NIP-05 domein
- `language:<code>` - Filtert op ISO-taalcode
- `sentiment:<value>` - Filtert op negatief/neutraal/positief sentiment
- `nsfw:<true/false>` - Includeert of excludeert NSFW-inhoud

## Client-overwegingen

- Clients moeten relay-mogelijkheden controleren via het `supported_nips`-veld
- Client-side verificatie van resultaten wordt aanbevolen
- Niet alle relays implementeren zoeken; het blijft een optionele functie

---

**Primaire bronnen:**
- [NIP-50 Specificatie](https://github.com/nostr-protocol/nips/blob/master/50.md)

**Vermeld in:**
- [Nieuwsbrief #3: December Samenvatting](/nl/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Zie ook:**
- [NIP-11: Relay Informatie](/nl/topics/nip-11/)
