---
title: "NIP-73 (Geotags)"
date: 2026-02-04
description: "NIP-73 definieert locatietagging voor Nostr events met geografische coördinaten en identifiers."
---

NIP-73 specificeert hoe geografische locatiegegevens aan Nostr events worden toegevoegd. Dit maakt locatiegebaseerde ontdekking en filtering van content mogelijk.

## Hoe Het Werkt

Locatiegegevens worden toegevoegd aan events via `g` (geohash) tags. De geohash-codering representeert breedtegraad en lengtegraad als een enkele string, waarbij de precisie wordt bepaald door de stringlengte. Langere strings geven preciezere locaties aan.

Events kunnen meerdere geohash-tags bevatten op verschillende precisieniveaus, waardoor clients op verschillende granulariteiten kunnen zoeken. Een post getagd met een 6-karakter geohash bestrijkt ruwweg een huizenblok, terwijl een 4-karakter geohash een kleine stad bestrijkt.

## Tag Formaat

```json
{
  "tags": [
    ["g", "u4pruydqqvj", "geohash"],
    ["g", "u4pruyd", "geohash"],
    ["g", "u4pru", "geohash"]
  ]
}
```

## Landcodes

Recente updates aan NIP-73 ([PR #2205](https://github.com/nostr-protocol/nips/pull/2205)) voegden ondersteuning toe voor ISO 3166 landcodes, waardoor events getagd kunnen worden met locatie op landniveau zonder precieze coördinaten:

```json
{
  "tags": [
    ["g", "US", "countryCode"]
  ]
}
```

## Implementaties

- Locatiebewuste clients gebruiken NIP-73 voor check-ins en lokale ontdekking
- Relay-filters kunnen content beperken of prioriteren op geografie
- Mapping-applicaties tonen geogetagde notities

## Primaire Bronnen

- [NIP-73 Specificatie](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Voegt ISO 3166 landcodes toe

## Vermeld In

- [Nieuwsbrief #8 (2026-02-04)](/nl/newsletters/2026-02-04-newsletter/) - Landcode-ondersteuning gemerged
