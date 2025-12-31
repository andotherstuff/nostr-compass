---
title: "NIP-94: Bestandsmetadata"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2025-12-31
draft: false
categories:
  - Media
  - Protocol
---

NIP-94 definieert een bestandsmetadata-event (kind 1063) voor het organiseren en classificeren van gedeelde bestanden op Nostr, waardoor relays content effectief kunnen filteren en organiseren.

## Hoe Het Werkt

1. Gebruiker uploadt een bestand naar een hostingdienst
2. Een kind 1063 event wordt gepubliceerd met metadata over het bestand
3. De eventinhoud bevat een voor mensen leesbare beschrijving
4. Gestructureerde tags bieden machineleesbare metadata
5. Gespecialiseerde clients kunnen bestanden systematisch organiseren en weergeven

## Vereiste en Optionele Tags

**Kerntags:**
- `url` - Downloadlink voor het bestand
- `m` - MIME type (kleine letters vereist)
- `x` - SHA-256 hash van het bestand

**Optionele tags:**
- `ox` - SHA-256 hash van het originele bestand vóór servertransformaties
- `size` - Bestandsgrootte in bytes
- `dim` - Afmetingen (breedte x hoogte) voor afbeeldingen/video
- `magnet` - Magnet URI voor torrent-distributie
- `i` - Torrent infohash
- `blurhash` - Placeholder-afbeelding voor voorvertoningen
- `thumb` - Thumbnail-URL
- `image` - Voorbeeldafbeelding-URL
- `summary` - Tekstuittreksel
- `alt` - Toegankelijkheidsbeschrijving
- `fallback` - Alternatieve downloadbronnen

## Gebruiksscenario's

NIP-94 is ontworpen voor bestandsdelingstoepassingen in plaats van sociale of langvorm-contentclients. Voorgestelde toepassingen zijn onder andere:

- Torrent-indexeringsrelays
- Portfolio-deelplatforms (vergelijkbaar met Pinterest)
- Software-configuratie- en updatedistributie
- Mediabibliotheken en archieven

---

**Primaire bronnen:**
- [NIP-94 Specificatie](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Genoemd in:**
- [Newsletter #3: December Terugblik](/nl/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Zie ook:**
- [NIP-92: Mediabijlagen](/nl/topics/nip-92/)
- [Blossom](/nl/topics/blossom/)
