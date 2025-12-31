---
title: "NIP-92: Media Attachments"
date: 2025-12-31
translationOf: /en/topics/nip-92.md
translationDate: 2025-12-31
draft: false
categories:
  - Media
  - Protocol
---

NIP-92 stelt gebruikers in staat om mediabestanden aan Nostr-events toe te voegen door URLs op te nemen samen met inline metadata-tags die deze bronnen beschrijven.

## Hoe Het Werkt

1. De gebruiker plaatst media-URLs direct in de event-inhoud (bijv. in een kind 1 tekstnotitie)
2. Een bijbehorende `imeta` (inline metadata) tag geeft details over elke URL
3. Clients kunnen imeta-URLs vervangen door rijke voorvertoningen op basis van de metadata
4. Metadata wordt doorgaans automatisch gegenereerd wanneer bestanden worden geüpload tijdens het opstellen

## De imeta Tag

Elke `imeta` tag moet een `url` en minimaal één ander veld hebben. Ondersteunde velden zijn:

- `url` - De media-URL (vereist)
- `m` - MIME-type van het bestand
- `dim` - Afbeeldingsafmetingen (breedte x hoogte)
- `blurhash` - Blurhash voor voorvertoningsgeneratie
- `alt` - Alternatieve tekst voor toegankelijkheid
- `x` - SHA-256-hash (van NIP-94)
- `fallback` - Alternatieve URLs als de primaire faalt

## Voorbeeld

```json
["imeta",
  "url https://example.com/image.jpg",
  "m image/jpeg",
  "dim 1920x1080",
  "blurhash LKO2?U%2Tw=w]~RBVZRi}^Xu%LRj"
]
```

---

**Primaire bronnen:**
- [NIP-92 Specificatie](https://github.com/nostr-protocol/nips/blob/master/92.md)

**Vermeld in:**
- [Nieuwsbrief #3: December Terugblik](/nl/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Zie ook:**
- [NIP-94: Bestandsmetadata](/nl/topics/nip-94/)
