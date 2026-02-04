---
title: "NIP-73 (Geotags)"
date: 2026-02-04
description: "NIP-73 definiert Standort-Tagging für Nostr-Events unter Verwendung von geografischen Koordinaten und Identifikatoren."
---

NIP-73 spezifiziert, wie geografische Standortdaten an Nostr-Events angehängt werden. Dies ermöglicht standortbasierte Entdeckung und Filterung von Inhalten.

## Funktionsweise

Standortdaten werden Events über `g` (Geohash)-Tags hinzugefügt. Die Geohash-Kodierung repräsentiert Breitengrad und Längengrad als einen einzelnen String, wobei die Präzision durch die String-Länge bestimmt wird. Längere Strings zeigen präzisere Standorte an.

Events können mehrere Geohash-Tags auf verschiedenen Präzisionsstufen enthalten, was es Clients ermöglicht, auf verschiedenen Granularitäten abzufragen. Ein Beitrag mit einem 6-Zeichen-Geohash deckt ungefähr einen Häuserblock ab, während ein 4-Zeichen-Geohash eine kleine Stadt abdeckt.

## Tag-Format

```json
{
  "tags": [
    ["g", "u4pruydqqvj", "geohash"],
    ["g", "u4pruyd", "geohash"],
    ["g", "u4pru", "geohash"]
  ]
}
```

## Ländercodes

Aktuelle Updates zu NIP-73 ([PR #2205](https://github.com/nostr-protocol/nips/pull/2205)) fügten Unterstützung für ISO 3166 Ländercodes hinzu, was es ermöglicht, Events mit Standort auf Länderebene zu taggen, ohne präzise Koordinaten zu benötigen:

```json
{
  "tags": [
    ["g", "US", "countryCode"]
  ]
}
```

## Implementierungen

- Standortbewusste Clients verwenden NIP-73 für Check-ins und lokale Entdeckung
- Relay-Filter können Inhalte nach Geografie einschränken oder priorisieren
- Kartenanwendungen zeigen geogetaggte Notizen an

## Primäre Quellen

- [NIP-73 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Fügt ISO 3166 Ländercodes hinzu

## Erwähnt in

- [Newsletter #8 (2026-02-04)](/de/newsletters/2026-02-04-newsletter/) - Ländercode-Unterstützung gemerged
