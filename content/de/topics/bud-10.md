---
title: "BUD-10: Blossom-URI-Schema"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

BUD-10 definiert das `blossom:`-URI-Schema, eine portable Blob-Referenz, die Server-Hinweise, Autoren-Hinweise und die erwartete Dateigröße zusammen mit dem Datei-Hash übertragen kann.

## URI-Format

```
blossom:<sha256>.<ext>?xs=<server>&as=<pubkey>&sz=<bytes>
```

Die Spezifikation erfordert einen kleingeschriebenen 64-stelligen SHA-256-Hash und eine Dateiendung. Wenn die Endung unbekannt ist, sollten Clients auf `.bin` zurückgreifen.

## Wie die Auflösung funktioniert

Clients sollten ein `blossom:`-URI schrittweise auflösen:

1. Alle `xs`-Server-Hinweise in der angegebenen Reihenfolge versuchen
2. Falls `as`-Autoren-Pubkeys vorhanden sind, die [BUD-03](/de/topics/bud-03/)-Serverliste jedes Autors abrufen und diese Server versuchen
3. Bei Bedarf auf bekannte Server oder lokalen Cache zurückgreifen

Diese Reihenfolge ist nützlich, weil der Sender unmittelbare Hinweise für schnellen Abruf beifügen kann, während Empfänger einen Ausweichpfad haben, falls diese Hinweise veralten.

## Warum es wichtig ist

`blossom:`-URIs funktionieren eher wie Magnet-Links als wie gewöhnliche Medien-URLs. Sie beschreiben, welcher Blob abgerufen werden soll, und enthalten Hinweise darauf, wo er zu finden ist, anstatt davon auszugehen, dass ein Host dauerhaft verfügbar bleibt.

Das optionale `sz`-Feld fügt eine konkrete Integritätsprüfung über den Hash hinaus hinzu. Clients können die erwartete Größe vor oder nach dem Download prüfen, was hilft, unvollständige Übertragungen zu erkennen, und die Nutzererfahrung bei großen Mediendateien verbessert.

---

**Primärquellen:**
- [BUD-10-Spezifikation](https://github.com/hzrd149/blossom/blob/master/buds/10.md)
- [Blossom Repository](https://github.com/hzrd149/blossom)

**Erwähnt in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)

**Siehe auch:**
- [Blossom Protocol](/de/topics/blossom/)
- [BUD-03: User Server List](/de/topics/bud-03/)
