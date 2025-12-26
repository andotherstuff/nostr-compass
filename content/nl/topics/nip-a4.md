---
title: "NIP-A4: Openbare Berichten"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Sociaal
---

NIP-A4 definieert openbare berichten (kind 24) ontworpen voor notificatieschermen, met brede client-ondersteuning als doel.

## Hoe Het Werkt

In tegenstelling tot threaded gesprekken hebben deze berichten geen concept van chatgeschiedenis of berichtketens. Het zijn eenvoudige eenmalige berichten bedoeld om te verschijnen in de notificatiefeed van een ontvanger.

## Structuur

- Gebruikt `q` tags (citaten) in plaats van `e` tags om threading-complicaties te vermijden
- Geen gespreksstatus of geschiedenis
- Ontworpen voor eenvoudige openbare notificaties

## Gebruiksscenario's

- Openbare erkenningen of shoutouts
- Broadcast-berichten naar een gebruiker
- Notificaties die geen reply-threading nodig hebben

---

**Primaire bronnen:**
- [NIP-A4 PR](https://github.com/nostr-protocol/nips/pull/1988)

**Vermeld in:**
- [Nieuwsbrief #2: NIP Updates](/nl/newsletters/2025-12-24-newsletter/#nip-updates)

**Zie ook:**
- [NIP-01: Basisprotocol](/nl/topics/nip-01/)
- [NIP-10: Tekstnota Threading](/nl/topics/nip-10/)
