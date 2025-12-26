---
title: "NIP-01: Basisprotokoll"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-01 definiert das grundlegende Protokoll für Nostr und legt die Datenstrukturen und Kommunikationsmuster fest, auf denen alle anderen NIPs aufbauen.

## Events

Events sind der einzige Objekttyp in Nostr. Jedes Datenstück, von einer Profilaktualisierung über einen Textbeitrag bis hin zu einer Reaktion, wird als Event mit dieser Struktur dargestellt:

- **id**: SHA256-Hash des serialisierten Events (eindeutiger Bezeichner)
- **pubkey**: Der öffentliche Schlüssel des Erstellers (32-Byte Hex, secp256k1)
- **created_at**: Unix-Zeitstempel
- **kind**: Ganzzahl zur Kategorisierung des Event-Typs
- **tags**: Array von Arrays für Metadaten
- **content**: Die Nutzlast (Interpretation hängt vom Kind ab)
- **sig**: Schnorr-Signatur zum Nachweis der Authentizität

## Kinds

Kinds bestimmen, wie Relays Events speichern und verarbeiten:

- **Reguläre Events** (1, 2, 4-44, 1000-9999): Normal gespeichert, alle Versionen werden aufbewahrt
- **Ersetzbare Events** (0, 3, 10000-19999): Nur die neueste Version pro Pubkey wird aufbewahrt
- **Ephemere Events** (20000-29999): Nicht gespeichert, nur an Abonnenten weitergeleitet
- **Adressierbare Events** (30000-39999): Neueste pro Pubkey + Kind + `d`-Tag-Kombination

Kern-Kinds umfassen: 0 (Benutzer-Metadaten), 1 (Textnotiz), 3 (Folgeliste).

## Client-Relay-Kommunikation

Clients kommunizieren mit Relays über WebSocket-Verbindungen mittels JSON-Arrays:

**Client an Relay:**
- `["EVENT", <event>]` - Ein Event veröffentlichen
- `["REQ", <sub-id>, <filter>, ...]` - Events abonnieren
- `["CLOSE", <sub-id>]` - Ein Abonnement beenden

**Relay an Client:**
- `["EVENT", <sub-id>, <event>]` - Passendes Event ausliefern
- `["EOSE", <sub-id>]` - Ende der gespeicherten Events (jetzt Live-Streaming)
- `["OK", <event-id>, <true|false>, <message>]` - Annahme-/Ablehnungsbestätigung
- `["NOTICE", <message>]` - Menschenlesbare Nachricht

## Filter

Filter spezifizieren, welche Events abgerufen werden sollen, mit Feldern wie: `ids`, `authors`, `kinds`, `#e`/`#p`/`#t` (Tag-Werte), `since`/`until` und `limit`. Bedingungen innerhalb eines Filters verwenden UND-Logik; mehrere Filter in einer `REQ` werden mit ODER-Logik kombiniert.

---

**Primärquellen:**
- [NIP-01 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Erwähnt in:**
- [Newsletter #1: NIP Deep Dive](/de/newsletters/2025-12-17-newsletter/#nip-deep-dive-nip-01-und-nip-19)

**Siehe auch:**
- [NIP-19: Bech32-kodierte Entitäten](/de/topics/nip-19/)
- [Kind-Verzeichnis](/de/kind-registry/)
