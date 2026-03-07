---
title: "NIP-58: Badges"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58 definieert een badgesysteem voor Nostr. Een event definieert de badge, een ander kent die toe, en een derde laat de ontvanger kiezen of die badge op het profiel wordt getoond.

## Hoe het werkt

### Badge-definitie (Kind 30009)

Uitgevers maken badge-definities als adresseerbare events:

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Early Adopter"],
    ["description", "Joined before 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### Badge-toekenning (Kind 8)

Uitgevers kennen badges toe aan een of meer gebruikers:

```json
{
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ]
}
```

### Badge-weergave (Kind 30008)

Gebruikers kiezen welke badges ze op hun profiel willen tonen:

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

In een profile badges-event moeten clients `a`- en `e`-tags als geordende paren lezen. Een `a`-tag zonder bijbehorend award event, of een `e`-tag zonder bijbehorende badge-definitie, moet worden genegeerd.

## Toepassingen

- **Communitylidmaatschap**: Toon lidmaatschap van groepen of communities
- **Prestaties**: Erken bijdragen of mijlpalen
- **Attestaties**: Laat een derde partij instaan voor een rol of status
- **Toegangscontrole**: Beperk functies of ruimtes met issuer-backed badges

## Vertrouwensmodel

De waarde van een badge hangt volledig af van de reputatie van de uitgever. Iedereen kan badges maken, dus clients moeten:

- Informatie over de uitgever duidelijk tonen
- Gebruikers laten filteren op vertrouwde uitgevers
- Badges niet zonder context als gezaghebbend behandelen

Badge-toekenningen zijn onveranderlijk en niet overdraagbaar. Daardoor zijn badges geschikt voor attestaties en erkenning, maar niet voor portable credentials in getokeniseerde zin.

## Implementatienotities

Badge-definities zijn adresseerbare events, dus uitgevers kunnen artwork of beschrijvingen van badges in de loop van de tijd bijwerken zonder de badge-identificatie te veranderen. Het award event is het blijvende record dat een ontvanger op een bepaald moment aan die definitie koppelt.

Clients hebben ook ruimte in de presentatie. De spec staat expliciet toe dat ze minder badges tonen dan een gebruiker vermeldt en zelf een thumbnailgrootte kiezen die past bij de beschikbare ruimte.

---

**Primaire bronnen:**
- [NIP-58 Specification](https://github.com/nostr-protocol/nips/blob/master/58.md)

**Vermeld in:**
- [Nieuwsbrief #7: Vijf jaar Nostr-januari's](/en/newsletters/2026-01-28-newsletter/)
- [Nieuwsbrief #15: Vijf jaar Nostr-februari's](/en/newsletters/2026-03-04-newsletter/)

**Zie ook:**
- [NIP-51: Lists](/nl/topics/nip-51/)
- [Web of Trust](/nl/topics/web-of-trust/)
