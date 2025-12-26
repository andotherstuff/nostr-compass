---
title: "NIP-BE: Bluetooth Low Energy"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Connectivity
---

NIP-BE spezifiziert, wie Nostr-Anwendungen über Bluetooth Low Energy kommunizieren und synchronisieren können, wodurch offline-fähige Apps Daten zwischen nahegelegenen Geräten ohne Internetverbindung synchronisieren können.

## GATT-Struktur

Verwendet einen Nordic UART Service mit zwei Charakteristiken:
- **Schreib-Charakteristik** - Client sendet Daten an Server
- **Lese-Charakteristik** - Server sendet Daten an Client (über Benachrichtigungen)

## Nachrichtenrahmen

BLE hat kleine Nutzlastgrenzen (20-256 Bytes je nach Version), daher werden Nachrichten:
- Mit DEFLATE komprimiert
- In Chunks mit einem 2-Byte-Index und Final-Batch-Flag aufgeteilt
- Auf maximal 64 KB begrenzt

## Rollenverhandlung

Geräte vergleichen angekündigte UUIDs bei der Erkennung:
- Höhere UUID wird zum GATT-Server (Relay-Rolle)
- Niedrigere UUID wird zum GATT-Client
- Vordefinierte UUIDs existieren für Einzelrollen-Geräte

## Synchronisation

Verwendet Halbduplex-Kommunikation mit Standard-Nostr-Nachrichtentypen (`EVENT`, `EOSE`, `NEG-MSG`) zur Koordination der Datensynchronisation über intermittierende Verbindungen.

## Anwendungsfälle

- Offline-Event-Synchronisation zwischen nahegelegenen Geräten
- Mesh-artige Nachrichtenweiterleitung ohne Internet
- Backup-Konnektivität, wenn das Netzwerk nicht verfügbar ist

---

**Primärquellen:**
- [NIP-BE Spezifikation](https://github.com/nostr-protocol/nips/blob/master/BE.md)

**Erwähnt in:**
- [Newsletter #1: Neuigkeiten](/de/newsletters/2025-12-17-newsletter/#news)
