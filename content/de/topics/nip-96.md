---
title: "NIP-96: HTTP-Dateispeicherung"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Media
---

NIP-96 definiert, wie Nostr-Clients Dateien auf HTTP-Medienservern hochladen, herunterladen und verwalten. Es ist inzwischen als "unrecommended" zugunsten von Blossom markiert, bleibt aber wichtig, weil bestehende Server und Clients es während des Übergangs weiter unterstützen.

## Funktionsweise

Ein Client entdeckt die Fähigkeiten eines Dateiservers, indem er `/.well-known/nostr/nip96.json` abruft. Dieses Dokument kündigt die URL der Upload-API, eine optionale Download-URL, unterstützte Content-Types, Größenlimits und die Unterstützung für Media-Transformationen oder delegated hosting an.

Für Uploads sendet der Client ein `multipart/form-data`-POST an die API-URL mit einem [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md)-Authorization-Header. Der Server antwortet mit einem Metadatenobjekt im NIP-94-Format, das die Datei-URL sowie Tags wie `ox` für den Original-Hash und gegebenenfalls `x` für die transformierte Datei enthält, die tatsächlich ausgeliefert wird.

Downloads verwenden `GET <api_url>/<sha256-hash>` mit optionalen Query-Parametern wie Bildbreite. Löschungen verwenden `DELETE` mit NIP-98-Auth. Nutzer veröffentlichen kind-10096-Events, um ihre bevorzugten Upload-Server anzugeben.

## Details des Datenmodells

Ein nützliches Detail ist, dass NIP-96 Dateien über den Hash der Originaldatei identifiziert, selbst wenn der Server den Upload transformiert. So kann ein Client ein Objekt unter derselben stabilen Kennung löschen oder erneut herunterladen und trotzdem vom Server erzeugte Thumbnails oder komprimierte Varianten erhalten, wenn sie verfügbar sind.

Das well-known-Dokument unterstützt außerdem `delegated_to_url`. Damit kann ein Relay Clients auf einen separaten HTTP-Storage-Server verweisen. So musste Relay-Software nicht selbst die vollständige Media-API implementieren.

## Warum es abgewertet wurde

NIP-96 band Datei-URLs an bestimmte Server. Wenn ein Server ausfiel, verloren alle Nostr-Notizen, die auf diese URLs verwiesen, ihre Medien. Blossom kehrt das um, indem der SHA-256-Hash des Dateiinhalts zum kanonischen Bezeichner wird. Jeder Blossom-Server, der dieselbe Datei hostet, liefert sie unter demselben Hash-Pfad aus. Inhalte werden dadurch standardmäßig serverübergreifend portabel.

Blossom vereinfacht außerdem die API: schlichtes PUT für Uploads, GET für Downloads und signierte Nostr-Events statt HTTP-Headern für die Autorisierung. Die Abwertung erfolgte im September 2025 über [PR #2047](https://github.com/nostr-protocol/nips/pull/2047).

## Interop-Hinweise

Server wie nostr.build und void.cat unterstützten NIP-96 und haben Blossom-Endpunkte ergänzt oder sind dorthin migriert. Clients befinden sich in unterschiedlichen Phasen: Angor v0.2.5 ergänzte NIP-96-Serverkonfiguration, während ZSP v0.3.1 ausschließlich auf Blossom-Server hochlädt. Diese Koexistenz wird anhalten, bis die verbleibenden NIP-96-Implementierungen ihre Migration abgeschlossen haben.

Kind-10096-Events für Server-Präferenzen bleiben auch für die Auswahl von Blossom-Servern nützlich. NIP-94-Dateimetadaten, also kind-1063-Events, beschreiben Dateieigenschaften unabhängig davon, welches Upload-Protokoll sie erzeugt hat.

---

**Primärquellen:**
- [NIP-96: HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**Erwähnt in:**
- [Newsletter #9: NIP Deep Dive](/de/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-96-http-dateispeicherung-and-the-transition-to-blossom)

**Siehe auch:**
- [Blossom Protocol](/de/topics/blossom/)
- [NIP-94: File Metadata](/de/topics/nip-94/)
