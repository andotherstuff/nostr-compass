---
title: "NIP-11: Relay-informatiedocument"
date: 2025-12-17
translationOf: /en/topics/nip-11.md
translationDate: 2026-03-11
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11 definieert hoe relays een machineleesbare beschrijving van zichzelf publiceren, inclusief geclaimde feature support, limieten en metadata van de beheerder.

## Hoe Het Werkt

Clients halen relay-informatie op door een HTTP GET-request te doen naar de WebSocket-URL van de relay met een `Accept: application/nostr+json`-header. De relay retourneert dan een JSON-document dat zijn mogelijkheden beschrijft.

## Nuttige Velden

- **name** - Menselijk leesbare relay-naam
- **description** - Waar de relay voor bedoeld is
- **supported_nips** - Lijst met geclaimde NIP-support
- **limitation** - Beperkingen zoals maximale berichtgrootte, vereiste authenticatie, enzovoort
- **pubkey** - Public key van de relay-operator, als die is opgegeven
- **contact** - Contactadres van de operator

## Vertrouwensmodel

NIP-11 is zelfgerapporteerde metadata. Het vertelt je wat een relay over zichzelf zegt, niet wat die in live verkeer heeft bewezen. Dat is nog steeds nuttig voor discovery en UX, maar clients moeten `supported_nips` niet als grondwaarheid behandelen zonder gedrag te testen.

Dit onderscheid is belangrijk voor relayselectie. Een relay kan NIP-50 search, authentication requirements of een grote message limit adverteren, maar het echte antwoord zie je pas wanneer een client daadwerkelijk verbinding maakt en die codepaden gebruikt.

## Waarom Het Belangrijk Is

- Clients kunnen controleren of een relay vereiste features ondersteunt voordat ze verbinding maken
- Discovery-services kunnen relay-capaciteiten indexeren
- Gebruikers kunnen relay-beleid bekijken voordat ze publiceren

## Recente Richting van de Specificatie

De specificatie is in de loop van de tijd teruggesnoeid. Oudere optionele velden zoals `software`, `version`, privacybeleid-details en retention-metadata zijn verwijderd na jaren van zwakke adoptie. Daardoor zijn huidige NIP-11-documenten kleiner en realistischer, maar het betekent ook dat clients geen rijke beleidsmetadata van relays moeten verwachten.

---

**Primaire bronnen:**
- [NIP-11-specificatie](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [PR #1764](https://github.com/nostr-protocol/nips/pull/1764) - update van relay identity field
- [PR #1946](https://github.com/nostr-protocol/nips/pull/1946) - opschoning van zelden gebruikte velden
- [PR #2231](https://github.com/nostr-protocol/nips/pull/2231) - verwijdering van verouderde velden

**Vermeld in:**
- [Nieuwsbrief #1: NIP Updates](/nl/newsletters/2025-12-17-newsletter/#nip-updates)

**Zie ook:**
- [NIP-66: Relay Discovery and Liveness Monitoring](/nl/topics/nip-66/)
