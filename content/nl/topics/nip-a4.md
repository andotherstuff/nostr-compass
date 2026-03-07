---
title: "NIP-A4: Openbare berichten"
date: 2025-12-24
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Sociaal
---

NIP-A4 definieert openbare berichten (kind 24) die bedoeld zijn voor notificatieschermen, met brede client-ondersteuning als doel.

## Hoe het werkt

Kind `24` is een ondertekend plaintext-bericht aan een of meer ontvangers. De berichtinhoud staat in `content`, en `p`-tags identificeren de beoogde ontvangers. De specificatie zegt dat clients deze events naar de inbox relays van de ontvangers uit [NIP-65](/nl/topics/nip-65/) en naar de outbox relay van de afzender moeten sturen.

Anders dan bij threaded gesprekken hebben deze berichten geen concept van chatgeschiedenis, room state of thread roots. Ze zijn bedoeld om in een notificatie-oppervlak te verschijnen en op zichzelf begrijpelijk te zijn.

## Protocolregels

- Gebruikt `p`-tags om ontvangers te identificeren
- Mag geen `e`-tags gebruiken voor threading
- Mag `q`-tags gebruiken om een ander event te citeren
- Werkt het best met expiration-tags uit [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md), zodat verouderde notificatieachtige berichten na verloop van tijd verdwijnen

## Waarom het bestaat

NIP-A4 geeft clients een eenvoudiger public-message-primitief dan een volledig threaded note. Dat is nuttig voor mention-achtige berichten, lichte shoutouts of eenmalige notificaties waarbij het opbouwen van een permanente conversatieboom meer complexiteit toevoegt dan waarde.

De afruil is dat deze berichten openbaar zijn. Ze zijn juist makkelijk in een notificatie-UI te tonen omdat ze geen private session state creëren. Iedereen kan ze lezen en beantwoorden als ze ze zien.

## Interop-opmerkingen

NIP-A4 is makkelijk te verwarren met direct-message-protocollen omdat het zich op specifieke ontvangers richt, maar het blijft een openbaar event kind. Clients moeten kind `24` niet presenteren als private messaging en ook geen vertrouwelijkheid aannemen die verder gaat dan relay placement.

---

**Primaire bronnen:**
- [NIP-A4 Specification](https://github.com/nostr-protocol/nips/blob/master/A4.md)
- [NIP-A4 PR](https://github.com/nostr-protocol/nips/pull/1988)

**Vermeld in:**
- [Nieuwsbrief #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Nieuwsbrief #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Zie ook:**
- [NIP-01: Basic Protocol](/nl/topics/nip-01/)
- [NIP-10: Text Note Threading](/nl/topics/nip-10/)
