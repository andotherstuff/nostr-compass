---
title: "NIP-11: Relay-Informationen"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11 definiert, wie Relays eine maschinenlesbare Beschreibung von sich selbst veröffentlichen, einschließlich behaupteter Feature-Unterstützung, Limits und Metadaten des Betreibers.

## Wie es funktioniert

Clients rufen Relay-Informationen ab, indem sie eine HTTP-GET-Anfrage an die WebSocket-URL des Relays mit dem Header `Accept: application/nostr+json` senden. Das Relay liefert ein JSON-Dokument zurück, das seine Fähigkeiten beschreibt.

## Nützliche Felder

- **name** - Menschenlesbarer Name des Relays
- **description** - Wofür das Relay gedacht ist
- **supported_nips** - Liste der behaupteten NIP-Unterstützung
- **limitation** - Einschränkungen wie maximale Nachrichtengröße, erforderliche Auth usw.
- **pubkey** - Public Key des Relay-Betreibers, wenn vorhanden
- **contact** - Kontaktadresse des Betreibers

## Vertrauensmodell

NIP-11 ist selbst gemeldete Metadaten. Es sagt dir, was ein Relay über sich selbst behauptet, nicht was es im laufenden Betrieb bewiesen hat. Das ist trotzdem nützlich für Discovery und UX, aber Clients sollten `supported_nips` nicht ohne Verhaltenstests als Ground Truth behandeln.

Diese Unterscheidung ist für die Relay-Auswahl wichtig. Ein Relay kann NIP-50-Suche, Auth-Anforderungen oder ein hohes Nachrichtenlimit bewerben, aber die echte Antwort zeigt sich erst, wenn ein Client sich tatsächlich verbindet und diese Codepfade ausführt.

## Warum es wichtig ist

- Clients können vor dem Verbinden prüfen, ob ein Relay benötigte Features unterstützt
- Discovery-Dienste können Relay-Fähigkeiten indexieren
- Nutzer können Relay-Richtlinien sehen, bevor sie veröffentlichen

## Aktuelle Richtung der Spezifikation

Die Spezifikation wurde mit der Zeit verschlankt. Ältere optionale Felder wie `software`, `version`, Details zur Datenschutzerklärung und Metadaten zur Aufbewahrung wurden nach Jahren schwacher Adoption entfernt. Dadurch sind aktuelle NIP-11-Dokumente kleiner und realistischer, aber Clients sollten von Relays keine umfangreichen Policy-Metadaten erwarten.

---

**Primärquellen:**
- [NIP-11 Specification](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [PR #1764](https://github.com/nostr-protocol/nips/pull/1764) - relay identity field update
- [PR #1946](https://github.com/nostr-protocol/nips/pull/1946) - cleanup of rarely used fields
- [PR #2231](https://github.com/nostr-protocol/nips/pull/2231) - removal of deprecated fields

**Erwähnt in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-66: Relay Discovery and Liveness Monitoring](/de/topics/nip-66/)
