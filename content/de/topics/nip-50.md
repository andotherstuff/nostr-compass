---
title: "NIP-50: Search"
date: 2025-12-31
translationOf: /en/topics/nip-50.md
translationDate: 2025-12-31
draft: false
categories:
  - Protokoll
  - Relay
---

NIP-50 definiert eine allgemeine Suchfunktion für Nostr-Relays, die es Clients ermöglicht, Volltextsuchen über strukturierte Abfragen nach Tags oder IDs hinaus durchzuführen.

## Wie Es Funktioniert

Das Protokoll fügt ein `search`-Feld zu Filterobjekten in REQ-Nachrichten hinzu:

1. Clients senden menschenlesbare Suchanfragen (z.B. "beste nostr apps")
2. Relays interpretieren und gleichen Anfragen mit Event-Daten ab, hauptsächlich das `content`-Feld
3. Ergebnisse werden nach Relevanz statt chronologischer Reihenfolge sortiert
4. Der `limit`-Filter wird nach der Relevanzsortierung angewendet

Suchfilter können mit anderen Einschränkungen wie `kinds` und `ids` für spezifischere Abfragen kombiniert werden.

## Sucherweiterungen

Relays können optional diese Erweiterungsparameter unterstützen:

- `include:spam` - Deaktiviert Standard-Spamfilterung
- `domain:<domain>` - Filtert nach verifizierter NIP-05-Domain
- `language:<code>` - Filtert nach ISO-Sprachcode
- `sentiment:<value>` - Filtert nach negativer/neutraler/positiver Stimmung
- `nsfw:<true/false>` - Schließt NSFW-Inhalte ein oder aus

## Client-Überlegungen

- Clients sollten Relay-Fähigkeiten über das Feld `supported_nips` prüfen
- Client-seitige Verifizierung der Ergebnisse wird empfohlen
- Nicht alle Relays implementieren Suche; es bleibt eine optionale Funktion

---

**Primäre Quellen:**
- [NIP-50 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/50.md)

**Erwähnt in:**
- [Newsletter #3: Dezember-Rückblick](/de/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Siehe auch:**
- [NIP-11: Relay-Informationen](/de/topics/nip-11/)
