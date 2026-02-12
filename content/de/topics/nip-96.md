---
title: "NIP-96: HTTP-Dateispeicherung"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Media
---

NIP-96 definierte, wie Nostr-Clients Dateien auf HTTP-Medienservern hochladen, herunterladen und verwalten. Inzwischen als „nicht empfohlen" zugunsten von Blossom gekennzeichnet, bleibt NIP-96 relevant, während Projekte den Übergang zwischen den beiden Medienstandards bewältigen.

## Funktionsweise

Ein Client erkennt die Fähigkeiten eines Dateiservers durch Abruf von `/.well-known/nostr/nip96.json`, das die API-URL, unterstützte Inhaltstypen, Größenlimits und verfügbare Medientransformationen zurückgibt.

Zum Hochladen sendet der Client einen `multipart/form-data` POST an die API-URL mit einem NIP-98-Autorisierungs-Header (ein signiertes Nostr-Event, das die Identität des Uploaders beweist). Der Server gibt eine NIP-94-Dateimetadaten-Struktur zurück, die die Datei-URL, SHA-256-Hashes, MIME-Typ und Abmessungen enthält.

Downloads verwenden GET-Anfragen an `<api_url>/<sha256-hash>`, mit optionalen Abfrageparametern für serverseitige Transformationen wie Bildgrößenänderung. Löschung erfolgt per DELETE mit NIP-98-Auth. Benutzer veröffentlichen kind 10096 Events, um ihre bevorzugten Upload-Server zu deklarieren.

## Warum es als veraltet markiert wurde

NIP-96 band Datei-URLs an bestimmte Server. Wenn ein Server ausfiel, verlor jede Nostr-Notiz, die auf die URLs dieses Servers verwies, ihre Medien. Blossom kehrt dies um, indem der SHA-256-Hash des Dateiinhalts zur kanonischen Kennung wird. Jeder Blossom-Server, der dieselbe Datei hostet, liefert sie unter demselben Hash-Pfad, was Inhalte standardmäßig serverübergreifend portabel macht.

Blossom vereinfacht auch die API: einfacher PUT für Uploads, GET für Downloads, und signierte Nostr-Events (nicht HTTP-Header) für die Autorisierung. Die Markierung als veraltet erfolgte im September 2025 via [PR #2047](https://github.com/nostr-protocol/nips/pull/2047).

## Der Übergang

Server wie nostr.build und void.cat unterstützten NIP-96 und haben Blossom-Endpunkte hinzugefügt oder dorthin migriert. Clients befinden sich in verschiedenen Stadien: Angor v0.2.5 fügte NIP-96-Serverkonfiguration hinzu, während ZSP v0.3.1 ausschließlich auf Blossom-Server hochlädt. Die Koexistenz wird fortbestehen, bis die verbleibenden NIP-96-Implementierungen ihre Migration abschließen.

Kind 10096 Server-Präferenz-Events bleiben für die Blossom-Serverauswahl nützlich. NIP-94-Dateimetadaten (kind 1063 Events) beschreiben Dateieigenschaften unabhängig davon, welches Upload-Protokoll sie erstellt hat.

---

**Primärquellen:**
- [NIP-96: HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**Erwähnt in:**
- [Newsletter #9: NIP Deep Dive](/de/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-96-http-dateispeicherung-und-der-übergang-zu-blossom)

**Siehe auch:**
- [Blossom-Protokoll](/de/topics/blossom/)
- [NIP-94: Dateimetadaten](/de/topics/nip-94/)
