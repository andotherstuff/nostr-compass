---
title: "NIP-23: Long-form Content"
date: 2026-04-08
translationOf: /en/topics/nip-23.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Content
---

NIP-23 definieert kind `30023` voor long-form content op Nostr. Anders dan korte notities van kind `1` zijn long-form events parameterized replaceable events (gesleuteld op een `d`-tag), ondersteunen ze Markdown-opmaak en bevatten ze metadata-tags voor titels, samenvattingen, afbeeldingen en publicatiedata.

## Hoe Het Werkt

Een long-form event gebruikt kind `30023` met een `d`-tag als unieke identifier, zodat de auteur de inhoud kan bijwerken door een nieuw event met dezelfde `d`-tag te publiceren. Het veld `content` bevat Markdown-tekst. Standaardtags zijn onder meer `title`, `summary`, `image` (header image URL), `published_at` (oorspronkelijke publicatietimestamp) en `t` (hashtags). Omdat dit een parameterized replaceable event is, slaan relays alleen de nieuwste versie per `d`-tag per auteur op.

## Belangrijke Tags

- `d` - unieke artikelidentifier (slug)
- `title` - artikeltitel
- `summary` - korte beschrijving
- `image` - header image URL
- `published_at` - oorspronkelijke publicatie-unix-timestamp (anders dan `created_at`, dat bij elke bewerking wordt bijgewerkt)
- `t` - hashtag-/onderwerptags

## Implementaties

- [Habla](https://habla.news) - Long-form content reader en publisher
- [YakiHonne](https://yakihonne.com) - Long-form contentplatform
- [Highlighter](https://highlighter.com) - Lees- en annotatietool

---

**Primaire bronnen:**
- [NIP-23 specification](https://github.com/nostr-protocol/nips/blob/master/23.md)

**Zie ook:**
- [NIP-01 (Basic Protocol)](/nl/topics/nip-01/)
