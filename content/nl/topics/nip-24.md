---
title: "NIP-24: Extra metadatavelden"
date: 2025-12-17
translationDate: 2026-03-07
translationOf: /en/topics/nip-24.md
draft: false
categories:
  - Protocol
  - Identiteit
---

NIP-24 definieert aanvullende optionele velden voor kind 0-gebruikersmetadata naast de basisvelden name, about en picture.

## Extra metadatavelden

- **display_name**: Een alternatieve, grotere naam met rijkere tekens dan `name`
- **website**: Een web-URL die verband houdt met de auteur van het event
- **banner**: URL naar een brede afbeelding (~1024x768) voor optionele achtergrondweergave
- **bot**: Boolean die aangeeft dat content geheel of gedeeltelijk geautomatiseerd is
- **birthday**: Object met optionele velden voor jaar, maand en dag

De specificatie markeert ook twee oudere velden als verouderd: `displayName` moet `display_name` worden, en `username` moet `name` worden. Clients zien deze nog steeds in het wild, dus een tolerante parser helpt met achterwaartse compatibiliteit, ook als een writer ze niet meer zou moeten uitsturen.

## Standaardtags

NIP-24 standaardiseert ook tags voor algemeen gebruik:
- `r`: Web-URL-verwijzing
- `i`: Externe identifier
- `title`: Naam voor verschillende eventtypes
- `t`: Hashtag (moet lowercase zijn)

## Waarom het belangrijk is

NIP-24 draait vooral om convergentie. Deze velden en tags verschenen al in verschillende clients, dus de specificatie geeft ze consistente namen en betekenissen. Dat verkleint kleine maar vervelende incompatibiliteiten, zoals clients die van mening verschillen over of een banner onder `banner` hoort of onder een app-specifieke sleutel.

Een praktisch punt voor implementers is dat kind 0 in de meeste clients een hot path blijft. Extra metadata moet licht blijven. Als een veld een eigen fetch-patroon of een onafhankelijke updatecyclus nodig heeft, hoort het waarschijnlijk thuis in een apart event kind in plaats van profielmetadata op te blazen.

---

**Primaire bronnen:**
- [NIP-24 Specification](https://github.com/nostr-protocol/nips/blob/master/24.md)

**Vermeld in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**Zie ook:**
- [NIP-01: Basic Protocol](/nl/topics/nip-01/)
