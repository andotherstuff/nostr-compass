---
title: "NIP-94: File Metadata"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2026-04-22
draft: false
categories:
  - Media
  - Protocol
---

NIP-94 definiert ein File-Metadata-Event, kind 1063, um geteilte Dateien auf Nostr zu organisieren und zu klassifizieren. Dadurch können Relays Inhalte wirksam filtern und ordnen.

## Funktionsweise

NIP-94 verwendet kind `1063` als eigenständiges Metadata-Event für eine Datei. Das Event-`content` enthält eine menschenlesbare Beschreibung, während Tags maschinenlesbare Felder wie Download-URL, MIME type, Hashes, Abmessungen und Preview-Hints tragen.

Diese Trennung ist wichtig, weil das Metadata-Event unabhängig von jeder Note, die auf die Datei verweist, indexiert, gefiltert und wiederverwendet werden kann. Ein Client kann ein kind-`1063`-Event als kanonische Beschreibung eines Assets behandeln, statt Metadaten aus freiformuliertem Post-Text zu scrapen.

## Erforderliche und optionale Tags

**Core tags:**
- `url` - Download-Link zur Datei
- `m` - MIME type, das Format muss kleingeschrieben sein
- `x` - SHA-256-Hash der Datei

**Optionale Tags:**
- `ox` - SHA-256-Hash der Originaldatei vor Server-Transformationen
- `size` - Dateigröße in Bytes
- `dim` - Abmessungen, width x height, für Bilder oder Video
- `magnet` - Magnet-URI für Torrent-Verteilung
- `i` - Torrent-Infohash
- `blurhash` - Platzhalterbild für Previews
- `thumb` - Thumbnail-URL
- `image` - Preview-Bild-URL
- `summary` - Textauszug
- `alt` - Barrierefreiheitsbeschreibung
- `fallback` - Alternative Download-Quellen
- `service` - Speicherprotokoll oder Diensttyp, etwa NIP-96

Die Tags `ox` und `x` werden leicht übersehen, sind in der Praxis aber sehr nützlich. `ox` identifiziert die ursprünglich hochgeladene Datei, während `x` die transformierte Version bezeichnen kann, die ein Server tatsächlich ausliefert. Wenn ein Medienhost Uploads komprimiert oder verkleinert, können Clients die Identität der Originaldatei trotzdem erhalten, ohne zu behaupten, dass das ausgelieferte Blob bytegenau identisch ist.

## Wann man es verwenden sollte

NIP-94 ist für File-Sharing-Anwendungen gedacht, nicht für Social- oder Longform-Clients. Vorgeschlagene Anwendungen sind unter anderem:

- Torrent-Indexierungs-Relays
- Plattformen zum Teilen von Portfolios, ähnlich wie Pinterest
- Verteilung von Software-Konfigurationen und Updates
- Medienbibliotheken und Archive

Wenn File-Metadata nur eine in ein anderes Event eingebettete URL ergänzen soll, ist [NIP-92: Media Attachments](/de/topics/nip-92/) leichter. NIP-94 ist die bessere Wahl, wenn die Datei selbst als eigenständiges, abfragbares Objekt behandelt werden soll.

## Interop-Hinweise

NIP-94 funktioniert über verschiedene Storage-Backends hinweg. Eine Datei kann über [NIP-96: HTTP File Storage](/de/topics/nip-96/) hochgeladen werden, über Blossom oder über einen anderen Dienst, und trotzdem mit derselben kind-`1063`-Event-Form beschrieben werden. Genau deshalb überlebt das Metadata-Format jedes einzelne Upload-Protokoll.

---

**Primärquellen:**
- [NIP-94 Specification](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Erwähnt in:**
- [Newsletter #3: December Recap](/de/newsletters/2025-12-31-newsletter/)
- [Newsletter #14: NIP Deep Dive](/de/newsletters/2026-03-18-newsletter/)

**Siehe auch:**
- [NIP-92: Media Attachments](/de/topics/nip-92/)
- [Blossom](/de/topics/blossom/)
