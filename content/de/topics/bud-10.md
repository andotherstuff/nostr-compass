---
title: "BUD-10: Blossom-URI-Schema"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-10 definiert ein benutzerdefiniertes URI-Schema für Blossom, das alle Informationen einbettet, die zum Abrufen einer Datei von einem beliebigen verfügbaren Server benötigt werden.

## URI-Format

```
blossom:<sha256>.<ext>?size=<bytes>&server=<url>&server=<url>&pubkey=<hex>
```

Komponenten:
- **sha256**: Datei-Hash (erforderlich)
- **ext**: Dateierweiterung
- **size**: Dateigröße in Bytes
- **server**: Ein oder mehrere Server-Hinweise
- **pubkey**: Autoren-Pubkeys für BUD-03-Server-Erkennung

## Vorteile

- Widerstandsfähiger als statische HTTP-URLs
- Automatischer Fallback über mehrere Server
- Autorenbasierte Erkennung über Pubkey-Hinweise
- Selbstverifizierend (Hash stellt Integrität sicher)

---

**Primärquellen:**
- [BUD-10 PR](https://github.com/hzrd149/blossom/pull/84)

**Erwähnt in:**
- [Newsletter #1: Neuigkeiten](/de/newsletters/2025-12-17-newsletter/#news)

**Siehe auch:**
- [Blossom-Protokoll](/de/topics/blossom/)
- [BUD-03: Benutzer-Serverliste](/de/topics/bud-03/)
