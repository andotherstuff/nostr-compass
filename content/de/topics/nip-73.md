---
title: "NIP-73: External Content IDs"
date: 2026-02-04
translationOf: /en/topics/nip-73.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Discovery
  - Metadata
---

NIP-73 definiert einen Standard, um externe Inhalte innerhalb von Nostr-Events zu referenzieren. Es verwendet `i`-Tags für den Bezeichner selbst und `k`-Tags für dessen Typ, sodass Clients Diskussionen über dasselbe Buch, dieselbe Website, Podcast-Episode, denselben Ort, Hashtag oder Blockchain-Objekt bündeln können.

## Funktionsweise

Ein Event, das NIP-73 nutzt, enthält ein `i`-Tag mit einem normalisierten externen Bezeichner und ein `k`-Tag, das beschreibt, um welche Art von Bezeichner es sich handelt. Clients können dann alle Events abfragen, die auf dasselbe Thema verweisen.

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

Die Spezifikation deckt mehrere Familien von Bezeichnern ab, darunter:

- normalisierte Web-URLs ohne Fragment
- ISBNs für Bücher
- ISANs für Filme
- Geohashes sowie ISO-3166-Länder- und Verwaltungscodes
- Podcast-Feed-, Episode- und Publisher-GUIDs
- Hashtags
- Blockchain-Transaktions- und Adressbezeichner

## Normalisierungsregeln

Das wichtigste Detail auf Nutzerseite in NIP-73 ist die Normalisierung. Dasselbe Objekt sollte auf genau eine kanonische Zeichenkette abgebildet werden, sonst verteilen Clients eine Diskussion auf mehrere Bezeichner, die eigentlich dasselbe meinen.

Beispiele aus der Spezifikation:

- Geohashes verwenden `geo:<value>` und müssen kleingeschrieben sein
- Länder- und Verwaltungscodes verwenden `iso3166:<code>` und müssen großgeschrieben sein
- ISBNs werden ohne Bindestriche geschrieben
- Web-URLs lassen Fragmente weg
- Blockchain-Transaktions-Hashes verwenden Hex in Kleinbuchstaben

Das klingt klein, ist aber der Unterschied zwischen einem gemeinsamen Gespräch und mehreren inkompatiblen Indizes.

## Nützliche Muster

NIP-73 ist eine allgemeine Referenzschicht, kein Inhaltsformat. Eine Longform-Note kann auf eine ISBN verweisen, eine Rezension auf eine ISAN, und ein lokaler Post auf einen Geohash oder Ländercode, ohne dass jedes Mal ein eigenes Custom-Tag erfunden werden muss.

Die Spezifikation erlaubt außerdem optional einen URL-Hint als zweiten Wert eines `i`-Tags. Das gibt Clients einen Fallback-Link, wenn sie für diesen Bezeichnertyp keinen eigenen Renderer haben.

## Warum das wichtig ist

Nostr hat bereits starke interne Referenzen für Events und Profile. NIP-73 erweitert diese Idee auf Dinge außerhalb von Nostr. Sobald Bezeichner normalisiert sind, können Kommentare, Bewertungen, Highlights und Trusted Assertions alle am selben externen Objekt hängen, auch über verschiedene Clients hinweg.

Darauf baut auch [NIP-85](/de/topics/nip-85/) auf. Trusted Assertions können nicht nur Nutzer und Events bewerten, sondern auch NIP-73-Bezeichner wie Bücher, Websites, Hashtags und Orte.

---

**Primärquellen:**
- [NIP-73 Specification](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Adds ISO 3166 country and subdivision codes

**Erwähnt in:**
- [Newsletter #8: NIP Updates](/de/newsletters/2026-02-04-newsletter/#nip-updates)
- [Newsletter #10: NIP-85 Deep Dive](/de/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)

**Siehe auch:**
- [NIP-85: Trusted Assertions](/de/topics/nip-85/)
