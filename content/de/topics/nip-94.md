---
title: "NIP-94: File Metadata"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2025-12-31
draft: false
categories:
  - Medien
  - Protokoll
---

NIP-94 definiert ein Datei-Metadaten-Event (kind 1063) zur Organisation und Klassifizierung von geteilten Dateien auf Nostr, wodurch Relays Inhalte effektiv filtern und organisieren können.

## So Funktioniert Es

1. Der Benutzer lädt eine Datei zu einem Hosting-Dienst hoch
2. Ein kind 1063 Event wird mit Metadaten über die Datei veröffentlicht
3. Der Event-Inhalt enthält eine für Menschen lesbare Beschreibung
4. Strukturierte Tags liefern maschinenlesbare Metadaten
5. Spezialisierte Clients können Dateien systematisch organisieren und anzeigen

## Erforderliche und Optionale Tags

**Kern-Tags:**
- `url` - Download-Link für die Datei
- `m` - MIME type (Kleinschreibung erforderlich)
- `x` - SHA-256 Hash der Datei

**Optionale Tags:**
- `ox` - SHA-256 Hash der Originaldatei vor Server-Transformationen
- `size` - Dateigröße in Bytes
- `dim` - Abmessungen (Breite x Höhe) für Bilder/Video
- `magnet` - Magnet URI für Torrent-Verteilung
- `i` - Torrent Infohash
- `blurhash` - Platzhalter-Bild für Vorschauen
- `thumb` - Thumbnail-URL
- `image` - Vorschaubild-URL
- `summary` - Textauszug
- `alt` - Barrierefreiheits-Beschreibung
- `fallback` - Alternative Download-Quellen

## Anwendungsfälle

NIP-94 ist für Datei-Sharing-Anwendungen konzipiert, nicht für soziale oder Langform-Content-Clients. Vorgeschlagene Anwendungen umfassen:

- Torrent-Indexierungs-Relays
- Portfolio-Sharing-Plattformen (ähnlich wie Pinterest)
- Software-Konfigurations- und Update-Verteilung
- Medienbibliotheken und Archive

---

**Primäre Quellen:**
- [NIP-94 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Erwähnt in:**
- [Newsletter #3: Dezember-Rückblick](/de/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Siehe auch:**
- [NIP-92: Medienanhänge](/de/topics/nip-92/)
- [Blossom](/de/topics/blossom/)
