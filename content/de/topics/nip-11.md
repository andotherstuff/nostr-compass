---
title: "NIP-11: Relay-Informationen"
date: 2025-12-17
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11 definiert, wie Relays Metadaten über sich selbst bereitstellen, einschließlich unterstützter NIPs, Einschränkungen und Kontaktinformationen.

## Funktionsweise

Clients rufen Relay-Informationen ab, indem sie eine HTTP-GET-Anfrage an die WebSocket-URL des Relays mit einem `Accept: application/nostr+json`-Header senden. Das Relay gibt ein JSON-Dokument zurück, das seine Fähigkeiten beschreibt.

## Wichtige Felder

- **name** - Menschenlesbarer Relay-Name
- **description** - Wofür das Relay gedacht ist
- **supported_nips** - Liste der implementierten NIPs
- **limitation** - Einschränkungen wie maximale Nachrichtengröße, erforderliche Authentifizierung usw.
- **self** - Der eigene öffentliche Schlüssel des Relays (neues Feld für Relay-Identität)

## Anwendungsfälle

- Clients können prüfen, ob ein Relay erforderliche Funktionen unterstützt, bevor sie sich verbinden
- Discovery-Dienste können Relay-Fähigkeiten indexieren
- Benutzer können Relay-Richtlinien vor dem Veröffentlichen einsehen

---

**Primärquellen:**
- [NIP-11 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/11.md)

**Erwähnt in:**
- [Newsletter #1: NIP-Updates](/de/newsletters/2025-12-17-newsletter/#nip-updates)
