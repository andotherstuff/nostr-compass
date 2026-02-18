---
title: "NIP-84: Highlights"
date: 2026-02-18
translationOf: /en/topics/nip-84.md
translationDate: 2026-02-18
draft: false
categories:
  - Content
  - Protocol
---

NIP-84 definiert kind-9802-„Highlight"-Events, mit denen Nutzer Passagen aus Langform-Inhalten auf Nostr markieren und teilen können, die sie als wertvoll erachten.

## Funktionsweise

Das `.content`-Feld enthält den hervorgehobenen Text. Events referenzieren ihr Quellmaterial über `a`- oder `e`-Tags für Nostr-native Inhalte oder `r`-Tags für externe URLs (Clients sollten Tracking-Parameter entfernen). Optionale `p`-Tags benennen Originalautoren, und ein optionaler `context`-Tag liefert umgebenden Text, wenn der Highlight ein Ausschnitt einer größeren Passage ist.

## Zitat-Highlights

Nutzer können einen `comment`-Tag hinzufügen, um Zitat-Highlights zu erstellen, die als zitierte Reposts dargestellt werden. Dies verhindert doppelte Einträge in Microblogging-Clients. Innerhalb von Kommentaren benötigen `p`-Tag-Erwähnungen ein „mention"-Attribut, um sie von Autoren-/Editor-Zuschreibungen zu unterscheiden, und `r`-Tag-URLs verwenden ein „source"-Attribut für Ursprungsreferenzen.

---

**Primärquellen:**
- [NIP-84-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/84.md)

**Erwähnt in:**
- [Newsletter #10: Releases](/de/newsletters/2026-02-18-newsletter/#prism-alles-von-android-aus-auf-nostr-teilen)

**Siehe auch:**
- [NIP-94: Datei-Metadaten](/de/topics/nip-94/)
