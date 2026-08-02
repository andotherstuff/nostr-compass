---
title: "NIP-68: Beeldgerichte feeds"
date: 2026-07-29
translationOf: /en/topics/nip-68.md
translationDate: 2026-08-02
draft: false
categories:
  - Media
  - Protocol
---

NIP-68 definieert adresseerbare afbeeldingsevents. Het biedt clients een verplaatsbare manier om afbeeldingsmetadata, bijschriften, labels en verwijzingen naar afbeeldingsbestanden te publiceren, terwijl het event zelf gescheiden blijft van blobopslag.

## Hoe het werkt

Een afbeelding gebruikt kind `20` en bevat een `title`-tag met een beschrijving in `content`. De `imeta`-tag beschrijft elke afbeelding met velden zoals `url`, `m` voor het MIME-type, `dim` voor de afmetingen, `alt`-tekst en een optionele SHA-256-hash. Met meerdere `imeta`-tags kan één event een reeks afbeeldingen vertegenwoordigen.

Het event kan `p`-tags bevatten voor afgebeelde of vermelde personen, `t`-tags voor onderwerpen en gewone Nostr-verwijzingen. Het kan ook tags voor mediatype, hash, locatie en inhoudswaarschuwingen bevatten, zodat clients afbeeldingsberichten consistent kunnen filteren en weergeven.

NIP-68 schrijft geen opslagbackend voor. Clients kunnen verwijzen naar gewone HTTPS-URL's of een inhoudgeadresseerd systeem zoals Blossom, zolang ze voldoende `imeta`-metadata publiceren om een andere client de afbeelding te laten weergeven en verifiëren.

## Implementaties

[NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0) voegde NIP-68-afbeeldingstags toe naast zijn beeldgerichte clientfuncties.

---

**Primaire bronnen:**
- [NIP-68-specificatie](https://github.com/nostr-protocol/nips/blob/master/68.md)
- [NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0)

**Vermeld in:**
- [Nieuwsbrief #33: Getagde releases](/nl/newsletters/2026-07-29-newsletter/#tagged-releases)

**Zie ook:**
- [Blossom-protocol](/nl/topics/blossom/)
- [NIP-94: Bestandsmetadata](/nl/topics/nip-94/)
