---
title: "NIP-24: Zusätzliche Metadatenfelder"
date: 2025-12-17
translationOf: /en/topics/nip-24.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Identity
---

NIP-24 definiert zusätzliche optionale Felder für Kind-0-User-Metadaten, über die grundlegenden Felder `name`, `about` und `picture` hinaus.

## Zusätzliche Metadatenfelder

- **display_name**: Ein alternativer, größerer Name mit reichhaltigeren Zeichen als `name`
- **website**: Eine Web-URL, die mit dem Autor des Events verknüpft ist
- **banner**: URL zu einem breiten Bild, etwa 1024x768, für eine optionale Hintergrunddarstellung
- **bot**: Boolean, der angibt, dass der Inhalt ganz oder teilweise automatisiert ist
- **birthday**: Objekt mit optionalen Feldern für Jahr, Monat und Tag

Die Spezifikation markiert außerdem zwei ältere Felder als deprecated: `displayName` soll zu `display_name` werden und `username` soll zu `name` werden. Clients sehen diese Felder weiterhin in freier Wildbahn, daher hilft ein toleranter Parser bei der Rückwärtskompatibilität, auch wenn ein Writer sie nicht mehr erzeugen sollte.

## Standard-Tags

NIP-24 standardisiert auch Tags für allgemeine Zwecke:
- `r`: Web-URL-Referenz
- `i`: Externer Identifikator
- `title`: Name für verschiedene Event-Typen
- `t`: Hashtag, muss kleingeschrieben sein

## Warum es wichtig ist

NIP-24 geht vor allem um Konvergenz. Diese Felder und Tags tauchten bereits in verschiedenen Clients auf, und die Spezifikation gibt ihnen nun konsistente Namen und Bedeutungen. Das reduziert kleine, aber lästige Inkompatibilitäten, etwa wenn Clients sich nicht einig sind, ob ein Banner unter `banner` oder unter einem app-spezifischen Key liegt.

Ein praktischer Punkt für Implementierer ist, dass Kind 0 in den meisten Clients ein Hot Path bleibt. Zusätzliche Metadaten sollten leichtgewichtig bleiben. Wenn ein Feld ein eigenes Fetch-Muster oder einen unabhängigen Update-Zyklus braucht, gehört es wahrscheinlich in einen separaten Event-Kind statt in aufgeblähte Profilmetadaten.

---

**Primärquellen:**
- [NIP-24 Specification](https://github.com/nostr-protocol/nips/blob/master/24.md)

**Erwähnt in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-01: Basic Protocol](/de/topics/nip-01/)
