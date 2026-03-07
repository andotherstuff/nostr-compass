---
title: "NIP-71: Video-Events"
date: 2026-01-13
translationOf: /en/topics/nip-71.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

NIP-71 definiert Event-Kinds für Videoinhalte auf Nostr und ermöglicht das Teilen von Videos mit passenden Metadaten. Die Spezifikation deckt sowohl normale Video-Events als auch addressable Video-Events ab. Letztere wurden im Januar 2026 ergänzt, damit Creators Video-Metadaten aktualisieren können, ohne neu veröffentlichen zu müssen.

## Event-Kinds

NIP-71 definiert vier Event-Kinds, aufgeteilt in zwei Kategorien nach Seitenverhältnis und Adressierbarkeit.

Normale Video-Events verwenden kind 21 für horizontale Videos im Querformat und kind 22 für vertikale Videos im Hochformat oder Shorts-Stil. Diese Events sind normale Nostr-Events mit unveränderlichem Inhalt nach der Veröffentlichung.

Addressable Video-Events verwenden kind 34235 für horizontale Videos und kind 34236 für vertikale Videos. Das sind parameterized replaceable events, die über die Kombination aus Pubkey, Kind und `d`-Tag identifiziert werden. Wenn ein neues Event mit denselben Kennungen veröffentlicht wird, ersetzt es die frühere Version und erlaubt so Metadaten-Updates.

## Struktur

Ein vollständiges addressable Video-Event enthält Identifikationsfelder, Metadaten-Tags und eine Referenz auf den Videoinhalt.

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

Das `d`-Tag liefert innerhalb deiner Videos dieses Kinds einen eindeutigen Bezeichner, sodass du mehrere addressable Videos mit unterschiedlichen `d`-Werten haben kannst. Die Tags `title` und `summary` liefern Videotitel und Kurzbeschreibung für die Anzeige im Client. Das `url`-Tag verweist auf die eigentliche Videodatei, `thumb` auf ein Vorschaubild. Das `duration`-Tag gibt die Länge in Sekunden an, und `dim` kann optional die Videoabmessungen angeben.

Das `origin`-Tag hält die Herkunft fest, wenn Inhalte von anderen Plattformen importiert werden. So bleibt Provenance erhalten, wenn Videos von YouTube, Vimeo oder anderen Diensten zu Nostr-Hosting migriert werden.

Das `content`-Feld kann eine längere Beschreibung, ein vollständiges Transkript oder beliebigen zusätzlichen Text zum Video enthalten.

## Warum addressable Events wichtig sind

Normale Video-Events der Kinds 21 und 22 sind nach der Veröffentlichung unveränderlich. Wenn du ein Video veröffentlichst und später einen Tippfehler im Titel findest, das Thumbnail ändern möchtest oder die Hosting-URL anpassen musst, weil du zu einem anderen Videodienst gewechselt bist, kannst du das ursprüngliche Event nicht ändern. Die einzige Möglichkeit ist ein neues Event mit neuer ID, wodurch bestehende Referenzen brechen und Engagement-Metriken verloren gehen.

Addressable Video-Events lösen dieses Problem, indem sie das Event ersetzbar machen. Die Kombination aus deinem Pubkey, dem Event-Kind und dem `d`-Tag identifiziert das Video eindeutig. Wenn du ein neues Event mit denselben Kennungen veröffentlichst, ersetzen Relays die alte Version durch die neue. Clients, die dein Video abrufen, erhalten dann immer die neuesten Metadaten.

Das ist besonders nützlich, um Metadatenfehler nach der Veröffentlichung zu korrigieren, Thumbnails beim Ausbau des Brandings zu aktualisieren, Hosting-URLs beim Anbieterwechsel zu migrieren oder Inhalte von eingestellten Plattformen wie Vine zu importieren und die Herkunft über das `origin`-Tag zu erhalten.

Ein weiterer Vorteil sind stabile Links. Andere Events können weiter auf dasselbe addressable Video verweisen, während der Creator Präsentationsdetails darum herum aktualisiert. Das ist sauberer, als Kommentare und Referenzen auf mehrere unveränderliche Reposts zu verteilen.

## Abwägungen

Die Ersetzbarkeit erleichtert die Pflege von Metadaten, bedeutet aber auch, dass Clients entscheiden müssen, wie viel historischen Zustand sie bewahren. Wenn ein Creator Titel oder Zusammenfassung nach der Veröffentlichung ändert, wird das neueste Event kanonisch, auch wenn ältere Clients die frühere Version bereits indiziert haben.

Kinds 21 und 22 bleiben trotzdem relevant für Anwendungen, die eine unveränderliche Veröffentlichungshistorie wollen. NIP-71 zwingt nicht jeden Video-Workflow in das replaceable Modell.

## Implementierungen

Addressable Video-Events der Kinds 34235 und 34236 sind derzeit in Amethyst und nostrvine implementiert. Beide Clients können solche Events erstellen, anzeigen und aktualisieren.

---

**Primärquellen:**
- [NIP-71 Specification](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - Addressable video events update

**Erwähnt in:**
- [Newsletter #5: NIP Updates](/de/newsletters/2026-01-13-newsletter/#nip-updates)
- [Newsletter #12: NoorNote](/de/newsletters/2026-03-04-newsletter/)

**Siehe auch:**
- [NIP-94: File Metadata](/de/topics/nip-94/)
