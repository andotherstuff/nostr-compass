---
title: "BUD-03: Benutzer-Serverliste"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

BUD-03 definiert, wie ein Nutzer seine bevorzugten Blossom-Server veröffentlicht, damit Clients wissen, wohin Blobs hochgeladen werden sollen und wo sie suchen müssen, wenn eine Medien-URL nicht mehr funktioniert.

## Wie es funktioniert

Nutzer veröffentlichen ein ersetzbares kind `10063`-Event mit einem oder mehreren `server`-Tags. Jeder Tag enthält eine vollständige Blossom-Server-URL.

Clients können dann:
- Blobs auf die bevorzugten Server des Nutzers hochladen
- wahrscheinliche Blob-Speicherorte anhand des Pubkeys des Autors ermitteln
- den Abruf von den aufgelisteten Servern wiederholen, wenn eine ältere URL nicht mehr funktioniert

## Nützliche Details für Leser

Die Reihenfolge der `server`-Tags ist wichtig. Die Spezifikation besagt, dass Nutzer ihre vertrauenswürdigsten oder zuverlässigsten Server zuerst auflisten sollten, und Clients müssen zumindest den ersten Server für Uploads versuchen. Das bedeutet, BUD-03 ist nicht nur ein Verzeichnis, sondern auch ein schwaches Präferenzsignal.

Die Abrufanleitung ist ebenfalls praktisch: Wenn ein Client einen Blob-Hash aus einer URL extrahiert, sollte er den letzten 64-stelligen Hex-String im Pfad verwenden. Das hilft Clients, Blobs sowohl aus Standard-Blossom-URLs als auch aus nicht-standardmäßigen CDN-URLs abzurufen, die den Hash weiterhin einbetten.

---

**Primärquellen:**
- [BUD-03-Spezifikation](https://github.com/hzrd149/blossom/blob/master/buds/03.md)
- [Blossom Repository](https://github.com/hzrd149/blossom)

**Erwähnt in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)

**Siehe auch:**
- [Blossom Protocol](/de/topics/blossom/)
- [NIP-51: Lists](/de/topics/nip-51/)
