---
title: "NIP-92: Media Attachments"
date: 2025-12-31
translationOf: /en/topics/nip-92.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

NIP-92 stelt gebruikers in staat mediabestanden aan Nostr-events toe te voegen door URLs op te nemen naast inline metadata-tags die die bronnen beschrijven.

## Hoe Het Werkt

Gebruikers plaatsen media-URLs direct in de event-content, bijvoorbeeld in een kind `1` text note. Een bijpassende `imeta`-tag voegt daarna machineleesbare details toe voor precies die URL. Clients kunnen die metadata gebruiken om previews te renderen, ruimte in de layout te reserveren en te voorkomen dat ze bestandseigenschappen moeten raden nadat de note al in beeld staat.

Elke `imeta`-tag moet overeenkomen met een URL in de event-content. Clients mogen tags negeren die niet overeenkomen, wat implementaties een simpele regel geeft om verouderde of onjuiste metadata af te wijzen.

## De imeta-tag

Elke `imeta`-tag moet een `url` en minstens een ander veld hebben. Ondersteunde velden zijn:

- `url` - De media-URL (verplicht)
- `m` - MIME-type van het bestand
- `dim` - Afmetingen van de afbeelding (breedte x hoogte)
- `blurhash` - Blurhash voor het genereren van previews
- `alt` - Alt-tekstbeschrijving voor toegankelijkheid
- `x` - SHA-256-hash (uit NIP-94)
- `fallback` - Alternatieve URLs als de primaire URL faalt

Omdat `imeta` velden uit [NIP-94: File Metadata](/nl/topics/nip-94/) kan meenemen, kunnen clients hetzelfde MIME-type, dezelfde afmetingen, hash en toegankelijkheidstekst hergebruiken die ze al begrijpen voor losse file metadata-events.

## Waarom Het Belangrijk Is

Het meest directe voordeel is betere rendering voordat een download start. Als `dim` aanwezig is, kunnen clients voor een afbeelding of video meteen de juiste ruimte reserveren in plaats van de timeline opnieuw te laten vloeien nadat het bestand is geladen. Als `blurhash` aanwezig is, kunnen ze eerst een goedkope preview tonen. Als `alt` aanwezig is, blijft de bijlage bruikbaar voor screenreader-gebruikers en mensen met beperkt zicht.

NIP-92 zorgt er ook voor dat de post zelf de bron van waarheid blijft. De URL blijft in `content`, zodat oudere clients nog steeds een gewone link tonen, terwijl nieuwere clients dezelfde note kunnen opwaarderen tot een rijkere mediakaart.

## Interop-opmerkingen

NIP-92 is inline metadata, geen apart media-objectformaat. Als een client een herbruikbaar filerecord nodig heeft met een eigen event, dan is [NIP-94: File Metadata](/nl/topics/nip-94/) geschikter.

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
- [NIP-92-specificatie](https://github.com/nostr-protocol/nips/blob/master/92.md)
- [Primal Android PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) - Een concrete client-implementatie voor afmetingen en aspect-ratio-afhandeling

**Vermeld in:**
- [Nieuwsbrief #3: December-terugblik](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Nieuwsbrief #6: Nieuws](/en/newsletters/2026-01-21-newsletter/#news)

**Zie ook:**
- [NIP-94: File Metadata](/nl/topics/nip-94/)
