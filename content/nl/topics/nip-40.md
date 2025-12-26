---
title: "NIP-40: Verloopdatum Tijdstempel"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-40 definieert een verloopdatum-tag die relays vertelt wanneer een event verwijderd moet worden.

## Structuur

Events bevatten een `expiration` tag met een Unix-tijdstempel:

```json
["expiration", "1734567890"]
```

Na deze tijd moeten relays het event verwijderen en weigeren het te serveren.

## Gebruiksscenario's

- Vluchtige content die na een bepaalde tijd moet verdwijnen
- Tijdgelimiteerde aanbiedingen of aankondigingen
- Verloopdatum van vermeldingen in marktplaatsen (bijv. Shopstr)
- Verminderen van relay-opslagvereisten

## Overwegingen

- Relays zijn niet verplicht om verloopdatum te honoreren (maar de meeste doen dat)
- Clients moeten niet vertrouwen op verloopdatum voor beveiligingskritieke contentverwijdering
- Zodra content is opgehaald door een andere client, kan deze worden gecachet of opnieuw gepubliceerd

---

**Primaire bronnen:**
- [NIP-40 Specificatie](https://github.com/nostr-protocol/nips/blob/master/40.md)

**Vermeld in:**
- [Nieuwsbrief #1: Nieuws](/nl/newsletters/2025-12-17-newsletter/#news)
