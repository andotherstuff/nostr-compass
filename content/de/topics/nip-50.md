---
title: "NIP-50: Suche"
date: 2025-12-31
translationOf: /en/topics/nip-50.md
translationDate: 2026-03-07
draft: false
categories:
  - Protokoll
  - Relay
---

NIP-50 definiert eine allgemeine Suchfunktion fur Nostr-Relays. Sie fugt zu den exakten Filtern aus NIP-01 eine Suchmoglichkeit im Stil einer Volltextsuche hinzu.

## Wie es funktioniert

Das Protokoll fugt ein `search`-Feld zu Filterobjekten in `REQ`-Nachrichten hinzu:

1. Clients senden eine menschenlesbare Suchanfrage wie `best nostr apps`.
2. Relays interpretieren diese Anfrage gegen Event-Daten, in erster Linie gegen das Feld `content`.
3. Die Ergebnisse werden nach Trefferqualitat sortiert, nicht nach `created_at`.
4. `limit` wird erst nach der Relevanzsortierung angewendet.

Suchfilter lassen sich mit `kinds`, `ids`, Autoren und anderen normalen Filterfeldern kombinieren, um Anfragen genauer zu machen.

## Sucherweiterungen

Relays konnen optional diese Erweiterungsparameter unterstutzen:

- `include:spam` - Deaktiviert die standardmaBige Spam-Filterung
- `domain:<domain>` - Filtert nach verifizierter NIP-05-Domain
- `language:<code>` - Filtert nach ISO-Sprachcode
- `sentiment:<value>` - Filtert nach negativer, neutraler oder positiver Stimmung
- `nsfw:<true/false>` - SchlieBt NSFW-Inhalte ein oder aus

Relays sollten Erweiterungen ignorieren, die sie nicht unterstutzen. Clients mussen sie deshalb als Hinweise behandeln, nicht als Garantien.

## Interop-Hinweise

- Clients sollten Relay-Fahigkeiten uber das Feld `supported_nips` prufen
- Client-seitige Verifizierung der Ergebnisse ist empfehlenswert
- Nicht alle Relays implementieren Suche, sie bleibt eine optionale Funktion

Weil das Ranking von der jeweiligen Implementierung abhangt, kann dieselbe Anfrage auf unterschiedlichen Relays verschiedene Ergebnismengen liefern. Clients, denen Vollstandigkeit wichtig ist, sollten mehr als ein Such-Relay abfragen und die Ergebnisse zusammenfuhren.

## Warum es wichtig ist

Strukturierte Filter funktionieren gut, wenn man den gesuchten Autor, Kind oder Tag schon kennt. Suche ist fur den gegenteiligen Fall gedacht: Entdeckung. Das macht NIP-50 fur App-Verzeichnisse, lange Archive und die Suche in offentlichen Notizen nutzlich, bedeutet aber auch, dass die Suchqualitat stark von den Indexierungs- und Spam-Filter-Entscheidungen jedes Relays abhangt.

---

**Primarquellen:**
- [NIP-50 Specification](https://github.com/nostr-protocol/nips/blob/master/50.md)

**Erwahnt in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #7: NIP Updates](/en/newsletters/2026-01-07-newsletter/)

**Siehe auch:**
- [NIP-11: Relay Information](/de/topics/nip-11/)
