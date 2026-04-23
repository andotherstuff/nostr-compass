---
title: "NIP-23: Long-form Content"
date: 2026-04-08
translationOf: /en/topics/nip-23.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Content
description: "Definiert kind 30023 für Long-form-Textinhalte auf Nostr mit Markdown-Artikeln und Metadaten-Tags."
---

NIP-23 definiert kind `30023` für Long-form-Textinhalte auf Nostr. Anders als kurze Notizen mit kind `1` sind Long-form-Events parametrisierte ersetzbare Events, über ein `d`-Tag adressiert, unterstützen Markdown-Formatierung und enthalten Metadaten-Tags für Titel, Zusammenfassungen, Bilder und Veröffentlichungsdaten.

## Funktionsweise

Ein Long-form-Event nutzt kind `30023` mit einem `d`-Tag als eindeutiger Kennung. Dadurch kann der Autor den Inhalt aktualisieren, indem er ein neues Event mit demselben `d`-Tag veröffentlicht. Das Feld `content` enthält Markdown-Text. Zu den Standard-Tags gehören `title`, `summary`, `image` (Header-Bild-URL), `published_at` (ursprünglicher Veröffentlichungszeitstempel) und `t` (Hashtags). Weil das Event parametriert ersetzbar ist, speichern Relays pro `d`-Tag und Autor nur die neueste Version.

## Wichtige Tags

- `d` - eindeutige Artikelkennung (Slug)
- `title` - Artikeltitel
- `summary` - kurze Beschreibung
- `image` - Header-Bild-URL
- `published_at` - Unix-Zeitstempel der ursprünglichen Veröffentlichung, getrennt von `created_at`, das sich bei jeder Bearbeitung ändert
- `t` - Hashtag- oder Themen-Tags

## Implementierungen

- [Habla](https://habla.news) - Reader und Publisher für Long-form-Inhalte
- [YakiHonne](https://yakihonne.com) - Plattform für Long-form-Inhalte
- [Highlighter](https://highlighter.com) - Lese- und Annotationstool

---

**Primärquellen:**
- [NIP-23 specification](https://github.com/nostr-protocol/nips/blob/master/23.md)

**Siehe auch:**
- [NIP-01 (Basic Protocol)](/de/topics/nip-01/)
