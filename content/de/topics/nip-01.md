---
title: "NIP-01: Basic Protocol"
date: 2025-12-17
translationOf: /en/topics/nip-01.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
---

NIP-01 definiert das grundlegende Event-Modell und Relay-Protokoll, auf dem der Rest von Nostr aufbaut. Wenn ein Client, Relay oder eine Library überhaupt Nostr spricht, beginnt es hier.

## Funktionsweise

Events sind der einzige Objekttyp in Nostr. Profile, Notizen, Reaktionen, Relay-Listen und viele anwendungsspezifische Payloads nutzen denselben Envelope mit sieben Feldern:

- **id**: SHA256-Hash des serialisierten Events, die eindeutige Kennung
- **pubkey**: Der öffentliche Schlüssel des Erstellers, 32-Byte-Hex auf secp256k1
- **created_at**: Unix-Timestamp
- **kind**: Integer zur Kategorisierung des Event-Typs
- **tags**: Array von Arrays für Metadaten
- **content**: Die Payload, deren Interpretation vom kind abhängt
- **sig**: Schnorr-Signatur als Echtheitsnachweis

Die Event-`id` ist der SHA256-Hash der serialisierten Event-Daten und keine beliebige Kennung. Das ist praktisch relevant: Jede Änderung, auch an Tag-Reihenfolge oder Timestamp, erzeugt ein anderes Event und verlangt eine neue Signatur.

## Kinds

Kinds bestimmen, wie Relays Events speichern und behandeln:

- **Regular events** (1, 2, 4-44, 1000-9999): normal gespeichert, alle Versionen bleiben erhalten
- **Replaceable events** (0, 3, 10000-19999): pro pubkey bleibt nur die neueste Version erhalten
- **Ephemeral events** (20000-29999): werden nicht gespeichert, nur an Subscriber weitergeleitet
- **Addressable events** (30000-39999): neueste Version pro pubkey + kind + `d`-Tag-Kombination

Zu den Kern-Kinds gehören 0 für User-Metadaten, 1 für Textnotizen und 3 für Follow-Listen.

## Client-Relay-Kommunikation

Clients kommunizieren mit Relays über WebSocket-Verbindungen mithilfe von JSON-Arrays:

**Client zu Relay:**
- `[`"EVENT"`, <event>]` - Ein Event veröffentlichen
- `[`"REQ"`, <sub-id>, <filter>, ...]` - Events abonnieren
- `[`"CLOSE"`, <sub-id>]` - Eine Subscription beenden

**Relay zu Client:**
- `[`"EVENT"`, <sub-id>, <event>]` - Passendes Event ausliefern
- `[`"EOSE"`, <sub-id>]` - Ende der gespeicherten Events, danach Echtzeit-Stream
- `[`"OK"`, <event-id>, <true|false>, <message>]` - Bestätigung oder Ablehnung
- `[`"NOTICE"`, <message>]` - Menschlich lesbare Nachricht

In der Praxis verändern die meisten höherstufigen NIPs nicht die Transportebene. Sie definieren neue Event-Kinds, Tags oder Interpretationsregeln, verwenden aber weiterhin dieselben `EVENT`-, `REQ`- und `CLOSE`-Nachrichten aus NIP-01.

## Filter

Filter legen fest, welche Events abgerufen werden sollen, mit Feldern wie `ids`, `authors`, `kinds`, `#e`, `#p`, `#t`, `since`, `until` und `limit`. Bedingungen innerhalb eines Filters werden mit AND verknüpft. Mehrere Filter innerhalb eines `REQ` werden mit OR verknüpft.

## Interop-Hinweise

Zwei Details verursachen viele Implementierungsfehler. Erstens sollten Clients Relay-Antworten als eventually consistent und nicht als global geordnet behandeln, weil verschiedene Relays unterschiedliche Teilmengen der Historie zurückgeben können. Zweitens bedeuten replaceable und addressable Events, dass "latest" Teil des Protokollmodells ist. Clients brauchen also deterministische Regeln, um das neueste gültige Event auszuwählen, wenn mehrere Relays widersprüchige Versionen liefern.

---

**Primärquellen:**
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Erwähnt in:**
- [Newsletter #1: NIP Deep Dive](/de/newsletters/2025-12-17-newsletter/)
- [Newsletter #19: NIP-67 EOSE completeness hint proposal](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-19: Bech32-Encoded Entities](/de/topics/nip-19/)
- [Kind Registry](/en/kind-registry/)
