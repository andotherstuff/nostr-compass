---
title: "NIP-58: Badges"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58 definieert een badge-systeem voor Nostr, waarmee uitgevers badges kunnen creëren en toekennen aan gebruikers die ze vervolgens op hun profiel kunnen tonen.

## Hoe Het Werkt

### Badge-Definitie (Kind 30009)

Uitgevers creëren badge-definities als adresseerbare events:

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Early Adopter"],
    ["description", "Geregistreerd voor 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### Badge-Toekenning (Kind 8)

Uitgevers kennen badges toe aan gebruikers:

```json
{
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ]
}
```

### Badge-Weergave (Kind 30008)

Gebruikers kiezen welke badges ze op hun profiel tonen:

```json
{
  "kind": 30008,
  "tags": [
    ["d", "profile_badges"],
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["e", "award-event-id"]
  ]
}
```

## Toepassingen

- **Community-Lidmaatschap**: Bewijs lidmaatschap van groepen of communities
- **Prestaties**: Erkenning van bijdragen of mijlpalen
- **Verificatie**: Attestaties van derden (werknemer, creator, etc.)
- **Toegangscontrole**: Content of functies beperken op basis van badge-eigendom

## Vertrouwensmodel

De waarde van een badge hangt volledig af van de reputatie van de uitgever. Iedereen kan badges creëren, dus clients moeten:
- Uitgeversinformatie prominent tonen
- Gebruikers laten filteren op vertrouwde uitgevers
- Badges niet als gezaghebbend behandelen zonder context

## Gerelateerd

- [NIP-51](/nl/topics/nip-51/) - Lijsten
- [Web of Trust](/nl/topics/web-of-trust/)
