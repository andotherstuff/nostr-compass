---
title: "NIP-54: Wiki"
date: 2025-12-31
translationOf: /en/topics/nip-54.md
translationDate: 2026-03-07
draft: false
categories:
  - Protokoll
  - Inhalt
---

NIP-54 definiert Kind `30818` fur Wiki-artige Artikel auf Nostr. Mehrere Autoren konnen Eintrage zum selben Thema veroffentlichen, deshalb brauchen Clients Ranking- und Vertrauensheuristiken statt einer einzelnen kanonischen Seite.

## Wie es funktioniert

Wiki-Artikel werden uber ein normalisiertes `d`-Tag identifiziert, das das Thema reprasentiert. Mehrere Personen konnen Eintrage fur dasselbe normalisierte Thema veroffentlichen und so ein offenes Wiki ohne zentrale Redaktion erzeugen.

**D-Tag-Normalisierung:**
- Buchstaben mit GroB-/Kleinschreibung in Kleinbuchstaben umwandeln
- Leerraum in Bindestriche umwandeln
- Satzzeichen und Symbole entfernen
- Wiederholte Bindestriche zusammenfassen und fuhrende oder abschlieBende Bindestriche entfernen
- Nicht-ASCII-Buchstaben und Zahlen beibehalten

Diese Normalisierungsregel ist fur Interoperabilitat wichtig. Wenn zwei Clients denselben Titel unterschiedlich normalisieren, fragen sie unterschiedliche Themen ab und splitten die Artikelmenge.

## Inhaltsformat

Die zusammengefuhrte Spezifikation verwendet Asciidoc-Markup mit zwei Zusatzfunktionen:

- **Wikilinks** (`[[target page]]`) - Links zu anderen Wiki-Artikeln auf Nostr
- **Nostr-Links** - Verweise auf Profile oder Events gemass NIP-21

Ein Wechsel zu Djot wurde vorgeschlagen, hat Asciidoc in der kanonischen NIP mit Stand Marz 2026 aber nicht ersetzt.

## Artikelauswahl

Wenn mehrere Versionen eines Artikels existieren, konnen Clients priorisieren anhand von:

1. Reaktionen (NIP-25), die Zustimmung aus der Community signalisieren
2. Relay-Listen (NIP-51) fur Quell-Ranking
3. Kontaktlisten (NIP-02), die Empfehlungsnetzwerke bilden

In der Praxis bedeutet das, dass NIP-54 nicht nur ein Inhaltsformat ist. Es ist auch ein Client-Policy-Problem. Zwei Clients konnen fur dasselbe Thema unterschiedliche "beste" Artikel anzeigen und trotzdem beide der Spezifikation entsprechen.

## Kollaborative Funktionen

- **Forking** - Abgeleitete Versionen von Artikeln erstellen
- **Merge requests** (kind 818) - Anderungen an bestehenden Artikeln vorschlagen
- **Redirects** (kind 30819) - Alte Themen auf neue verweisen
- **Deference markers** - Bevorzugte Artikelversionen markieren

Forks und Deference Markers erlauben Autoren, bessere Versionen anzuerkennen, ohne ihre eigene Arbeit zu loschen. Das ist in einem Netzwerk wichtig, in dem alte Revisionen auf vielen Relays weiter verfugbar bleiben konnen.

---

**Primarquellen:**
- [NIP-54 Specification](https://github.com/nostr-protocol/nips/blob/master/54.md)
- [PR #2177: Internationalized d-tag normalization](https://github.com/nostr-protocol/nips/pull/2177)

**Erwahnt in:**
- [Newsletter #3: NIP Updates](/en/newsletters/2025-12-31-newsletter/#nip-updates)
- [Newsletter #15: Open PRs](/en/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**Siehe auch:**
- [NIP-51: Lists](/de/topics/nip-51/)
- [NIP-02: Follow List](/de/topics/nip-02/)
