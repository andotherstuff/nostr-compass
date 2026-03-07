---
title: "NIP-84: Highlights"
date: 2026-02-18
translationOf: /en/topics/nip-84.md
translationDate: 2026-03-07
draft: false
categories:
  - Content
  - Protocol
---

NIP-84 definiert kind-9802-"highlight"-Events, mit denen Nutzer Passagen aus Longform-Inhalten auf Nostr markieren und teilen können, die sie wertvoll finden.

## Funktionsweise

Das `.content`-Feld enthält den hervorgehobenen Text. Events referenzieren ihr Quellmaterial über `a`- oder `e`-Tags für Nostr-native Inhalte oder über `r`-Tags für externe URLs. Clients sollten dabei Tracking-Parameter entfernen. Optionale `p`-Tags nennen die ursprünglichen Autoren, und ein optionales `context`-Tag liefert umgebenden Text, wenn das Highlight nur ein Ausschnitt aus einer größeren Passage ist.

Bei nicht textbasierten Medien kann der Highlight-Inhalt leer sein. So können Clients trotzdem auf ein Audio- oder Video-Highlight verweisen, während die Quelle in den Tags erhalten bleibt.

## Quote-Highlights

Nutzer können ein `comment`-Tag hinzufügen, um Quote-Highlights zu erstellen, die als quoted reposts gerendert werden. Dadurch entstehen in Microblogging-Clients keine doppelten Einträge. Innerhalb von Kommentaren brauchen `p`-Tag-Erwähnungen ein Attribut `mention`, damit sie von Zuschreibungen als Autor oder Editor unterscheidbar bleiben, und `r`-Tag-URLs verwenden ein Attribut `source` für Ursprungsreferenzen.

## Warum das wichtig ist

NIP-84 trennt die hervorgehobene Passage von der umgebenden Diskussion. Ein Client kann den ausgewählten Text als primäres Objekt darstellen und Kommentare nur als optionale Metadaten behandeln, statt beides in einer gewöhnlichen Note zu vermischen.

Das ist besonders nützlich für Lese- und Recherchewerkzeuge, weil der exakte Auszug erhalten bleibt. Zwei Leser können denselben Artikel kommentieren und trotzdem portable Highlight-Events erzeugen, die andere Clients verstehen.

## Interop-Hinweise

Attribution-Tags sind wichtiger, als es auf den ersten Blick scheint. Ein `p`-Tag mit der Rolle `author` oder `editor` sagt Clients, wer das Quellmaterial erstellt hat, während eine Rolle `mention` innerhalb eines Quote-Kommentars etwas anderes bedeutet. Wenn Clients diese Fälle zusammenwerfen, können sie die Quelle falsch beschriften oder Personen fälschlich benachrichtigen.

---

**Primärquellen:**
- [NIP-84 Specification](https://github.com/nostr-protocol/nips/blob/master/84.md)

**Erwähnt in:**
- [Newsletter #10: Releases](/de/newsletters/2026-02-18-newsletter/#prism-share-anything-to-nostr-from-android)

**Siehe auch:**
- [NIP-94: File Metadata](/de/topics/nip-94/)
