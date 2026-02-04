---
title: "NIP-73 (Geotags)"
date: 2026-02-04
description: "NIP-73 defines location tagging for Nostr events using geographic coordinates and identifiers."
---

NIP-73 specifies how to attach geographic location data to Nostr events. This enables location-based discovery and filtering of content.

## How It Works

Location data is added to events via `g` (geohash) tags. The geohash encoding represents latitude and longitude as a single string, with precision determined by string length. Longer strings indicate more precise locations.

Events can include multiple geohash tags at different precision levels, allowing clients to query at various granularities. A post tagged with a 6-character geohash covers roughly a city block, while a 4-character geohash covers a small city.

## Tag Format

```json
{
  "tags": [
    ["g", "u4pruydqqvj", "geohash"],
    ["g", "u4pruyd", "geohash"],
    ["g", "u4pru", "geohash"]
  ]
}
```

## Country Codes

Recent updates to NIP-73 ([PR #2205](https://github.com/nostr-protocol/nips/pull/2205)) added support for ISO 3166 country codes, allowing events to be tagged with country-level location without requiring precise coordinates:

```json
{
  "tags": [
    ["g", "US", "countryCode"]
  ]
}
```

## Implementations

- Location-aware clients use NIP-73 for check-ins and local discovery
- Relay filters can restrict or prioritize content by geography
- Mapping applications display geotagged notes

## Primary Sources

- [NIP-73 Specification](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Adds ISO 3166 country codes

## Mentioned In

- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - Country code support merged
