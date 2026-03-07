---
title: "NIP-92: Media Attachments"
date: 2025-12-31
translationOf: /en/topics/nip-92.md
translationDate: 2026-03-07
draft: false
categories:
  - Medien
  - Protokoll
---

NIP-92 ermöglicht es Nutzern, Mediendateien an Nostr-Events anzuhängen, indem URLs zusammen mit Inline-Metadaten-Tags eingefügt werden, die diese Ressourcen beschreiben.

## Funktionsweise

Nutzer platzieren Medien-URLs direkt im Inhalt eines Events, zum Beispiel in einer kind-`1`-Textnote. Ein passendes `imeta`-Tag ergänzt dann maschinenlesbare Details genau für diese URL. Clients können diese Metadaten nutzen, um Vorschauen zu rendern, Platz im Layout zu reservieren und Dateieigenschaften nicht erst erraten zu müssen, nachdem die Note schon sichtbar ist.

Jedes `imeta`-Tag sollte genau zu einer URL im Event-Inhalt passen. Clients können Tags ignorieren, die nicht dazu passen. Das gibt Implementierungen eine einfache Regel, um veraltete oder fehlerhafte Metadaten zu verwerfen.

## Das imeta-Tag

Jedes `imeta`-Tag muss eine `url` und mindestens ein weiteres Feld haben. Unterstützte Felder sind unter anderem:

- `url` - Die Medien-URL, erforderlich
- `m` - MIME type der Datei
- `dim` - Bildabmessungen, Breite x Höhe
- `blurhash` - Blurhash für Vorschaugenerierung
- `alt` - Alt-Text für Barrierefreiheit
- `x` - SHA-256-Hash aus NIP-94
- `fallback` - Alternative URLs, falls die primäre fehlschlägt

Da `imeta` Felder aus [NIP-94: File Metadata](/de/topics/nip-94/) enthalten kann, können Clients denselben MIME type, dieselben Abmessungen, denselben Hash und denselben Accessibility-Text wiederverwenden, die sie bereits aus eigenständigen Datei-Metadaten-Events kennen.

## Warum das wichtig ist

Der direkteste Vorteil ist besseres Rendering vor dem Download. Wenn `dim` vorhanden ist, können Clients für ein Bild oder Video den passenden Platz reservieren, statt die Timeline nach dem Laden neu anzuordnen. Wenn `blurhash` vorhanden ist, können sie zuerst eine günstige Vorschau anzeigen. Wenn `alt` vorhanden ist, bleibt der Anhang für Screenreader-Nutzer und Menschen mit Sehbeeinträchtigung nutzbar.

NIP-92 erlaubt Clients außerdem, den Post selbst als Source of Truth zu behalten. Die URL bleibt in `content`, daher zeigen ältere Clients weiterhin einfach einen Link, während neuere Clients dieselbe Note zu einer reicheren Medienkarte aufwerten können.

## Interop-Hinweise

NIP-92 ist Inline-Metadaten, kein eigenes Format für Medienobjekte. Wenn ein Client einen wiederverwendbaren Dateieintrag mit eigenem Event braucht, ist [NIP-94: File Metadata](/de/topics/nip-94/) die bessere Wahl.

## Beispiel

```json
["imeta",
  "url https://example.com/image.jpg",
  "m image/jpeg",
  "dim 1920x1080",
  "blurhash LKO2?U%2Tw=w]~RBVZRi}^Xu%LRj"
]
```

---

**Primärquellen:**
- [NIP-92 Specification](https://github.com/nostr-protocol/nips/blob/master/92.md)
- [Primal Android PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) - A concrete client implementation for dimensions and aspect-ratio handling

**Erwähnt in:**
- [Newsletter #3: December Recap](/de/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #6: News](/de/newsletters/2026-01-21-newsletter/#news)

**Siehe auch:**
- [NIP-94: File Metadata](/de/topics/nip-94/)
