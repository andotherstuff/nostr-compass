---
title: "NIP-24: Zusätzliche Metadatenfelder"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
---

NIP-24 definiert zusätzliche optionale Felder für Kind-0-Benutzer-Metadaten über die grundlegenden Name-, About- und Picture-Felder hinaus.

## Zusätzliche Metadatenfelder

- **display_name**: Ein alternativer, größerer Name mit reichhaltigeren Zeichen als `name`
- **website**: Eine Web-URL bezogen auf den Event-Autor
- **banner**: URL zu einem breiten (~1024x768) Bild zur optionalen Hintergrundanzeige
- **bot**: Boolean, der angibt, dass der Inhalt vollständig oder teilweise automatisiert ist
- **birthday**: Objekt mit optionalen Jahr-, Monat- und Tag-Feldern

## Standard-Tags

NIP-24 standardisiert auch allgemeine Tags:
- `r`: Web-URL-Referenz
- `i`: Externer Identifikator
- `title`: Name für verschiedene Event-Typen
- `t`: Hashtag (muss kleingeschrieben sein)

---

**Primärquellen:**
- [NIP-24 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/24.md)

**Erwähnt in:**
- [Newsletter #1: NIP-Updates](/de/newsletters/2025-12-17-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-01: Basisprotokoll](/de/topics/nip-01/)
