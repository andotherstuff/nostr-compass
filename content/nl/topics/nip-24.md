---
title: "NIP-24: Extra Metadatavelden"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identiteit
---

NIP-24 definieert aanvullende optionele velden voor kind 0 gebruikersmetadata naast de basis naam, over en foto.

## Extra Metadatavelden

- **display_name**: Een alternatieve, grotere naam met rijkere tekens dan `name`
- **website**: Een web-URL gerelateerd aan de event-auteur
- **banner**: URL naar een brede (~1024x768) afbeelding voor optionele achtergrondweergave
- **bot**: Boolean die aangeeft dat content geheel of gedeeltelijk geautomatiseerd is
- **birthday**: Object met optionele jaar, maand en dag velden

## Standaard Tags

NIP-24 standaardiseert ook algemene tags:
- `r`: Web URL-referentie
- `i`: Externe identifier
- `title`: Naam voor verschillende eventtypes
- `t`: Hashtag (moet in kleine letters zijn)

---

**Primaire bronnen:**
- [NIP-24 Specificatie](https://github.com/nostr-protocol/nips/blob/master/24.md)

**Vermeld in:**
- [Nieuwsbrief #1: NIP Updates](/nl/newsletters/2025-12-17-newsletter/#nip-updates)

**Zie ook:**
- [NIP-01: Basisprotocol](/nl/topics/nip-01/)
