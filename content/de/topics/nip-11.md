---
title: "NIP-11: Relay Information Document"
date: 2025-12-17
translationOf: /en/topics/nip-11.md
translationDate: 2026-04-22
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11 definiert, wie Relays eine maschinenlesbare Beschreibung ihrer selbst veröffentlichen, einschließlich behaupteter Feature-Unterstützung, Limits und Betreiber-Metadaten.

## Funktionsweise

Clients rufen Relay-Informationen ab, indem sie eine HTTP-GET-Anfrage an die WebSocket-URL des Relays mit dem Header `Accept: application/nostr+json` senden. Das Relay gibt ein JSON-Dokument zurück, das seine Fähigkeiten beschreibt.

## Nützliche Felder

- **name** - Menschenlesbarer Relay-Name
- **description** - Wofür das Relay gedacht ist
- **supported_nips** - Liste behaupteter NIP-Unterstützung
- **limitation** - Einschränkungen wie maximale Nachrichtengröße, erforderliche Authentifizierung und ähnliches
- **pubkey** - Öffentlicher Schlüssel des Relay-Betreibers, falls angegeben
- **contact** - Kontaktadresse des Betreibers

## Vertrauensmodell

NIP-11 ist selbstberichtete Metadaten. Es sagt, was ein Relay über sich selbst behauptet, nicht was es im Live-Traffic bewiesen hat. Für Discovery und UX ist das trotzdem nützlich, aber Clients sollten `supported_nips` nicht ohne Verhaltenstests als Ground Truth behandeln.

Gerade bei der Relay-Auswahl ist dieser Unterschied wichtig. Ein Relay kann NIP-50-Suche, Authentifizierungsanforderungen oder ein großes Message-Limit ankündigen, aber die echte Antwort zeigt sich erst, wenn ein Client tatsächlich verbindet und diese Pfade ausführt.

## Warum das wichtig ist

- Clients können vor dem Verbinden prüfen, ob ein Relay benötigte Features unterstützt
- Discovery-Dienste können Relay-Fähigkeiten indexieren
- Nutzer können Relay-Richtlinien vor dem Publizieren sehen

## Jüngste Spezifikationsrichtung

Die Spezifikation wurde im Lauf der Zeit reduziert. Ältere optionale Felder wie `software`, `version`, Details zur Privacy Policy und Retention-Metadaten wurden nach Jahren schwacher Akzeptanz entfernt. Das macht aktuelle NIP-11-Dokumente kleiner und realistischer, bedeutet aber auch, dass Clients keine reichen Richtlinien-Metadaten erwarten sollten.

[PR #2318](https://github.com/nostr-protocol/nips/pull/2318) schlägt ein optionales `access_control`-Objekt für das Relay Information Document vor. Es listet den Gating-Modus des Relays auf, etwa open, invite, payment oder allowlist, sowie gegebenenfalls einen Endpoint, über den ein Client Zugriff anfragen kann. Das Feld ist rein hinweisend und soll Clients und Verzeichnissen erlauben, geschützte Relays aus öffentlichen Discovery-Listen herauszufiltern und Nutzern früh zu zeigen, warum ein Relay Schreibzugriffe verweigert.

## Implementierungen

- [nostream PR #557](https://github.com/Cameri/nostream/pull/557) bringt nostream auf vollständige NIP-11-Relay-Info-Parität.

---

**Primärquellen:**
- [NIP-11 Specification](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [PR #1764](https://github.com/nostr-protocol/nips/pull/1764) - relay identity field update
- [PR #1946](https://github.com/nostr-protocol/nips/pull/1946) - cleanup of rarely used fields
- [PR #2231](https://github.com/nostr-protocol/nips/pull/2231) - removal of deprecated fields
- [PR #2318](https://github.com/nostr-protocol/nips/pull/2318) - `access_control` field for gated-relay discovery
- [nostream PR #557](https://github.com/Cameri/nostream/pull/557) - Complete NIP-11 relay info parity

**Erwähnt in:**
- [Newsletter #1: NIP Updates](/de/newsletters/2025-12-17-newsletter/)
- [Newsletter #13: NIP Updates](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: NIP Updates (`access_control` proposal)](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-66: Relay Discovery and Liveness Monitoring](/de/topics/nip-66/)
