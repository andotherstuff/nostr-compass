---
title: "NIP-94: Bestandsmetadata"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

NIP-94 definieert een bestandsmetadata-event (kind 1063) voor het organiseren en classificeren van gedeelde bestanden op Nostr, zodat relays content effectief kunnen filteren en ordenen.

## Hoe Het Werkt

NIP-94 gebruikt kind `1063` als een zelfstandig metadata-event voor een bestand. De `content` van het event bevat een voor mensen leesbare beschrijving, terwijl tags machineleesbare velden dragen zoals download-URL, MIME type, hashes, afmetingen en preview-hints.

Die scheiding is belangrijk omdat het metadata-event onafhankelijk kan worden geïndexeerd, gefilterd en hergebruikt van elke note die naar het bestand linkt. Een client kan een kind `1063` event behandelen als de canonieke beschrijving van een asset in plaats van metadata uit vrije posttekst te moeten halen.

## Vereiste en Optionele Tags

**Kerntags:**
- `url` - Downloadlink voor het bestand
- `m` - MIME type (kleine letters vereist)
- `x` - SHA-256-hash van het bestand

**Optionele tags:**
- `ox` - SHA-256-hash van het originele bestand voor servertransformaties
- `size` - Bestandsgrootte in bytes
- `dim` - Afmetingen (breedte x hoogte) voor afbeeldingen/video
- `magnet` - Magnet-URI voor torrent-distributie
- `i` - Torrent-infohash
- `blurhash` - Placeholder-afbeelding voor previews
- `thumb` - Thumbnail-URL
- `image` - Previewafbeelding-URL
- `summary` - Tekstsamenvatting
- `alt` - Toegankelijkheidsbeschrijving
- `fallback` - Alternatieve downloadbronnen
- `service` - Storage protocol of servicetype, zoals NIP-96

De tags `ox` en `x` zijn makkelijk over het hoofd te zien, maar nuttig in de praktijk. `ox` identificeert het originele geuploade bestand, terwijl `x` de getransformeerde versie kan identificeren die een server daadwerkelijk aanbiedt. Wanneer een mediahost uploads comprimeert of schaalt, kunnen clients toch de identiteit van het originele bestand behouden zonder te doen alsof de getransformeerde blob byte voor byte identiek is.

## Wanneer Je Het Gebruikt

NIP-94 is bedoeld voor toepassingen voor bestandsdeling, niet voor social- of longform-contentclients. Voorgestelde toepassingen zijn onder meer:

- Torrent-indexeringsrelays
- Portfolio-platforms voor delen, vergelijkbaar met Pinterest
- Distributie van softwareconfiguratie en updates
- Medialibraries en archieven

Als de bestandsmetadata alleen een URL binnen een ander event hoeft aan te vullen, is [NIP-92: Mediabijlagen](/nl/topics/nip-92/) lichter. NIP-94 is de betere keuze wanneer het bestand zelf als first-class object doorzoekbaar moet zijn.

## Interop Notes

NIP-94 werkt over storage backends heen. Een bestand kan worden geüpload via [NIP-96: HTTP File Storage](/nl/topics/nip-96/), Blossom of een andere dienst, en daarna nog steeds met dezelfde kind `1063` eventvorm worden beschreven. Daarom blijft het metadataformaat bruikbaar, ook als een afzonderlijk uploadprotocol verandert.

---

**Primaire bronnen:**
- [NIP-94-specificatie](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Genoemd in:**
- [Newsletter #3: December-terugblik](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Zie ook:**
- [NIP-92: Mediabijlagen](/nl/topics/nip-92/)
- [Blossom](/nl/topics/blossom/)
