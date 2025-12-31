---
title: "NIP-54: Wiki"
date: 2025-12-31
translationOf: /en/topics/nip-54.md
translationDate: 2025-12-31
draft: false
categories:
  - Protokoll
  - Inhalt
---

NIP-54 definiert kind 30818 als adressierbaren Event-Typ zur Erstellung von Wiki-Artikeln und Enzyklopädie-Einträgen auf Nostr. Es ermöglicht dezentralisierte, kollaborative Inhaltserstellung, bei der mehrere Autoren über dieselben Themen schreiben können.

## Funktionsweise

Wiki-Artikel werden durch einen normalisierten `d` tag (das Artikelthema) identifiziert. Mehrere Personen können Artikel zum selben Thema verfassen und so eine dezentralisierte Wissensbasis ohne zentrale Autorität schaffen.

**D Tag Normalisierung:**
- Alle Buchstaben in Kleinbuchstaben umwandeln
- Leerzeichen in Bindestriche umwandeln
- Satzzeichen und Symbole entfernen
- Nicht-ASCII-Zeichen und Zahlen beibehalten

## Inhaltsformat

Artikel verwenden Asciidoc-Markup mit zwei besonderen Funktionen:

- **Wikilinks** (`[[Zielseite]]`) - Links zu anderen Wiki-Artikeln auf Nostr
- **Nostr-Links** - Verweise auf Profile oder Events gemäß NIP-21

## Artikelauswahl

Wenn mehrere Versionen eines Artikels existieren, priorisieren Clients basierend auf:

1. Reaktionen (NIP-25), die Community-Zustimmung anzeigen
2. Relay-Listen (NIP-51) für Quellenrangfolge
3. Kontaktlisten (NIP-02), die Empfehlungsnetzwerke bilden

## Kollaborative Funktionen

- **Forking** - Abgeleitete Versionen von Artikeln erstellen
- **Merge-Anfragen** (kind 818) - Änderungen an bestehenden Artikeln vorschlagen
- **Weiterleitungen** (kind 30819) - Alte Themen auf neue verweisen
- **Deferenz-Markierungen** - Bevorzugte Artikelversionen angeben

---

**Primärquellen:**
- [NIP-54 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/54.md)

**Erwähnt in:**
- [Newsletter #3: NIP-Updates](/de/newsletters/2025-12-31-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-51: Listen](/de/topics/nip-51/)
- [NIP-02: Folge-Liste](/de/topics/nip-02/)
