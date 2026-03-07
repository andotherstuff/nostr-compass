---
title: "NIP-01: Basisprotokoll"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
---

NIP-01 definiert das grundlegende Event-Modell und das Relay-Protokoll, auf dem der Rest von Nostr aufbaut. Wenn ein Client, Relay oder eine Bibliothek überhaupt Nostr spricht, beginnt es hier.

## Wie es funktioniert

Events sind der einzige Objekttyp in Nostr. Profile, Notes, Reaktionen, Relay-Listen und viele anwendungsspezifische Payloads verwenden alle dieselbe Hülle mit sieben Feldern:

- **id**: SHA256-Hash der serialisierten Event-Daten (eindeutiger Bezeichner)
- **pubkey**: Der öffentliche Schlüssel des Erstellers (32-Byte-Hex, secp256k1)
- **created_at**: Unix-Zeitstempel
- **kind**: Ganzzahl zur Kategorisierung des Event-Typs
- **tags**: Array von Arrays für Metadaten
- **content**: Die Payload, deren Bedeutung vom Kind abhängt
- **sig**: Schnorr-Signatur zum Nachweis der Authentizität

Die Event-`id` ist der SHA256-Hash der serialisierten Event-Daten, kein beliebiger Bezeichner. Das ist praktisch wichtig: Schon eine Änderung an einem Feld, einschließlich der Reihenfolge von Tags oder des Zeitstempels, erzeugt ein anderes Event und erfordert eine neue Signatur.

## Kinds

Kinds bestimmen, wie Relays Events speichern und behandeln:

- **Reguläre Events** (1, 2, 4-44, 1000-9999): Werden normal gespeichert, alle Versionen bleiben erhalten
- **Ersetzbare Events** (0, 3, 10000-19999): Nur die neueste Version pro Pubkey bleibt erhalten
- **Ephemere Events** (20000-29999): Werden nicht gespeichert, sondern nur an Abonnenten weitergeleitet
- **Adressierbare Events** (30000-39999): Neueste Version pro Pubkey + Kind + `d`-Tag-Kombination

Zu den zentralen Kinds gehören 0 (Benutzermetadaten), 1 (Textnote) und 3 (Folgeliste).

## Client-Relay-Kommunikation

Clients kommunizieren mit Relays über WebSocket-Verbindungen mittels JSON-Arrays:

**Client an Relay:**
- `["EVENT", <event>]` - Ein Event veröffentlichen
- `["REQ", <sub-id>, <filter>, ...]` - Events abonnieren
- `["CLOSE", <sub-id>]` - Ein Abonnement beenden

**Relay an Client:**
- `["EVENT", <sub-id>, <event>]` - Ein passendes Event ausliefern
- `["EOSE", <sub-id>]` - Ende der gespeicherten Events, danach beginnt der Live-Stream
- `["OK", <event-id>, <true|false>, <message>]` - Bestätigung oder Ablehnung
- `["NOTICE", <message>]` - Menschenlesbare Nachricht

In der Praxis verändern die meisten höheren NIPs die Transportschicht nicht. Sie definieren neue Event-Kinds, Tags oder Interpretationsregeln und verwenden dennoch dieselben `EVENT`-, `REQ`- und `CLOSE`-Nachrichten aus NIP-01.

## Filter

Filter legen fest, welche Events abgerufen werden sollen, mit Feldern wie `ids`, `authors`, `kinds`, `#e`/`#p`/`#t`, `since`, `until` und `limit`. Bedingungen innerhalb eines Filters verwenden UND-Logik. Mehrere Filter innerhalb eines `REQ` verwenden ODER-Logik.

## Interop-Hinweise

Zwei Details verursachen viele Implementierungsfehler. Erstens sollten Clients Relay-Antworten als eventual consistent behandeln, nicht als global geordnet, weil unterschiedliche Relays unterschiedliche Ausschnitte der Historie zurückgeben können. Zweitens bedeuten ersetzbare und adressierbare Events, dass "neueste Version" Teil des Protokollmodells ist. Clients brauchen deshalb deterministische Regeln, um das neueste gültige Event zu wählen, wenn mehrere Relays widersprechen.

---

**Primärquellen:**
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Erwähnt in:**
- [Newsletter #1: NIP Deep Dive](/en/newsletters/2025-12-17-newsletter/#nip-deep-dive-nip-01-and-nip-19)

**Siehe auch:**
- [NIP-19: Bech32-Encoded Entities](/de/topics/nip-19/)
- [Kind Registry](/de/kind-registry/)
