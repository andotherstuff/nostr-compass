---
title: "NIP-71: Video-Events"
date: 2026-01-13
draft: false
categories:
  - Media
  - Protocol
---

NIP-71 definiert Event-Kinds für Videoinhalte auf Nostr und ermöglicht das Teilen von Videos mit ordnungsgemäßer Metadaten-Unterstützung. Die Spezifikation umfasst sowohl reguläre Video-Events als auch adressierbare Video-Events, wobei letztere im Januar 2026 hinzugefügt wurden, um Erstellern zu ermöglichen, Video-Metadaten zu aktualisieren, ohne neu veröffentlichen zu müssen.

## Event-Kinds

NIP-71 definiert vier Event-Kinds, die in zwei Kategorien basierend auf Seitenverhältnis und Adressierbarkeit unterteilt sind.

Reguläre Video-Events verwenden kind 21 für horizontale (Querformat) Videos und kind 22 für vertikale (Hochformat/Shorts) Videos. Dies sind Standard-Nostr-Events mit unveränderlichem Inhalt nach der Veröffentlichung.

Adressierbare Video-Events verwenden kind 34235 für horizontale Videos und kind 34236 für vertikale Videos. Dies sind parametrisiert ersetzbare Events, die durch die Kombination aus pubkey, kind und `d`-Tag identifiziert werden. Das Veröffentlichen eines neuen Events mit denselben Identifikatoren ersetzt die vorherige Version und ermöglicht Metadaten-Updates.

## Struktur

Ein vollständiges adressierbares Video-Event enthält Identifikationsfelder, Metadaten-Tags und die Videoinhalts-Referenz.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 34235,
  "tags": [
    ["d", "my-video-2026-01"],
    ["title", "Introduction to Nostr Video"],
    ["summary", "A walkthrough of NIP-71 video events"],
    ["url", "https://example.com/video.mp4"],
    ["thumb", "https://example.com/thumbnail.jpg"],
    ["duration", "300"],
    ["dim", "1920x1080"],
    ["origin", "youtube:dQw4w9WgXcQ"]
  ],
  "content": "Extended description, transcript, or additional notes about the video.",
  "sig": "sig1234..."
}
```

Der `d`-Tag liefert einen eindeutigen Identifikator innerhalb deiner Videos dieses Kinds, sodass du mehrere adressierbare Videos haben kannst, indem du verschiedene `d`-Werte verwendest. Die `title`- und `summary`-Tags liefern den Videotitel und eine kurze Beschreibung zur Anzeige in Clients. Der `url`-Tag zeigt auf die eigentliche Videodatei, während `thumb` ein Vorschaubild liefert. Der `duration`-Tag gibt die Länge in Sekunden an, und `dim` gibt optional die Videodimensionen an.

Der `origin`-Tag verfolgt die Quellplattform beim Importieren von Inhalten von anderen Diensten. Dies bewahrt die Herkunft beim Migrieren von Videos von YouTube, Vimeo oder anderen Plattformen zum Nostr-Hosting.

Das `content`-Feld kann eine erweiterte Beschreibung, vollständige Transkription oder jeden zusätzlichen Text enthalten, der mit dem Video verbunden ist.

## Warum adressierbare Events wichtig sind

Reguläre Video-Events (kinds 21 und 22) sind nach der Veröffentlichung unveränderlich. Wenn du ein Video veröffentlichst und später einen Tippfehler im Titel bemerkst, das Thumbnail aktualisieren möchtest oder die Hosting-URL ändern musst, weil du zu einem anderen Videodienst gewechselt bist, kannst du das ursprüngliche Event nicht ändern. Deine einzige Option ist, ein neues Event mit einer neuen ID zu veröffentlichen, was alle bestehenden Referenzen bricht und Engagement-Metriken verliert.

Adressierbare Video-Events lösen dieses Problem, indem sie das Event ersetzbar machen. Die Kombination aus deinem pubkey, dem Event-Kind und dem `d`-Tag identifiziert dein Video eindeutig. Wenn du ein neues Event mit denselben Identifikatoren veröffentlichst, ersetzen Relays die alte Version durch die neue. Clients, die dein Video abrufen, erhalten immer die neuesten Metadaten.

Dies ist besonders wertvoll für das Beheben von Metadatenfehlern nach der Veröffentlichung, das Aktualisieren von Thumbnails, wenn du dein Branding verbesserst, das Migrieren von Video-Hosting-URLs beim Wechsel des Anbieters und das Importieren von Inhalten von eingestellten Plattformen wie Vine unter Bewahrung der Herkunft durch den `origin`-Tag.

## Implementierungen

Adressierbare Video-Events (kinds 34235 und 34236) sind derzeit in Amethyst und nostrvine implementiert. Beide Clients können adressierbare Video-Events erstellen, anzeigen und aktualisieren.

---

**Primärquellen:**
- [NIP-71 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - Update für adressierbare Video-Events

**Erwähnt in:**
- [Newsletter #5: NIP-Updates](/de/newsletters/2026-01-13-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-94: Datei-Metadaten](/de/topics/nip-94/)
