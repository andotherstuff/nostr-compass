---
title: "NIP-11: Relay-informatie"
date: 2025-12-17
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11 definieert hoe relays metadata over zichzelf blootstellen, inclusief ondersteunde NIPs, beperkingen en contactinformatie.

## Hoe Het Werkt

Clients halen relay-informatie op door een HTTP GET-verzoek te doen naar de WebSocket URL van de relay met een `Accept: application/nostr+json` header. De relay retourneert een JSON-document dat zijn mogelijkheden beschrijft.

## Belangrijke Velden

- **name** - Leesbare relay-naam
- **description** - Waar de relay voor is
- **supported_nips** - Lijst van geïmplementeerde NIPs
- **limitation** - Restricties zoals maximale berichtgrootte, vereiste authenticatie, etc.
- **self** - De eigen publieke sleutel van de relay (nieuw veld voor relay-identiteit)

## Gebruiksscenario's

- Clients kunnen controleren of een relay vereiste functies ondersteunt voordat ze verbinden
- Discovery-diensten kunnen relay-mogelijkheden indexeren
- Gebruikers kunnen relay-beleid bekijken voordat ze publiceren

---

**Primaire bronnen:**
- [NIP-11 Specificatie](https://github.com/nostr-protocol/nips/blob/master/11.md)

**Vermeld in:**
- [Nieuwsbrief #1: NIP Updates](/nl/newsletters/2025-12-17-newsletter/#nip-updates)
