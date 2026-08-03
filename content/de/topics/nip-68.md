---
title: "NIP-68: Bildorientierte Feeds"
date: 2026-07-29
translationOf: /en/topics/nip-68.md
translationDate: 2026-07-29
draft: false
categories:
  - Media
  - Protocol
---

NIP-68 definiert adressierbare Bild-events. Es bietet Clients eine portable Möglichkeit, Bildmetadaten, Bildunterschriften, Kennzeichnungen und Verweise auf Bilddateien zu veröffentlichen, während das event selbst vom Blob-Speicher getrennt bleibt.

## Funktionsweise

Ein Bild verwendet kind `20` und enthält ein `title`-tag sowie eine Beschreibung in `content`. Das `imeta`-tag beschreibt jedes Bild mit Feldern wie `url`, `m` für den MIME-Typ, `dim` für die Abmessungen, `alt`-Text und einem optionalen SHA-256-Hash. Mehrere `imeta`-tags ermöglichen einem event, einen Bildsatz darzustellen.

Das event kann `p`-tags für abgebildete oder in den Credits genannte Personen, `t`-tags für Themen und gewöhnliche Nostr-Verweise enthalten. Es kann außerdem tags für Medientyp, Hash, Ort und Inhaltswarnung enthalten, damit Clients Bildbeiträge einheitlich filtern und darstellen können.

NIP-68 schreibt kein Speicher-Backend vor. Clients können gewöhnliche HTTPS-URLs oder ein inhaltsadressiertes System wie Blossom referenzieren, sofern sie genügend `imeta`-Metadaten veröffentlichen, damit ein anderer Client das Bild darstellen und verifizieren kann.

## Implementierungen

[NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0) ergänzte seine bildorientierten Client-Funktionen um die Bildkennzeichnung nach NIP-68.

---

**Primärquellen:**
- [NIP-68-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/68.md)
- [NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0)

**Erwähnt in:**
- [Newsletter #33: Releases mit Versions-Tag](/de/newsletters/2026-07-29-newsletter/#tagged-releases)

**Siehe auch:**
- [Blossom Protocol](/de/topics/blossom/)
- [NIP-94: Dateimetadaten](/de/topics/nip-94/)
