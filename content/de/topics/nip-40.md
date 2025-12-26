---
title: "NIP-40: Ablaufzeitstempel"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-40 definiert ein Ablauf-Tag, das Relays mitteilt, wann ein Event gelöscht werden soll.

## Struktur

Events enthalten ein `expiration`-Tag mit einem Unix-Zeitstempel:

```json
["expiration", "1734567890"]
```

Nach dieser Zeit sollten Relays das Event löschen und die Auslieferung verweigern.

## Anwendungsfälle

- Ephemerer Inhalt, der nach einer festgelegten Zeit verschwinden soll
- Zeitlich begrenzte Angebote oder Ankündigungen
- Ablauf von Angeboten in Marktplätzen (z.B. Shopstr)
- Reduzierung der Relay-Speicheranforderungen

## Überlegungen

- Relays sind nicht verpflichtet, den Ablauf zu berücksichtigen (aber die meisten tun es)
- Clients sollten sich nicht auf den Ablauf für sicherheitskritische Inhaltslöschung verlassen
- Sobald Inhalt von einem anderen Client abgerufen wurde, kann er zwischengespeichert oder erneut veröffentlicht werden

---

**Primärquellen:**
- [NIP-40 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/40.md)

**Erwähnt in:**
- [Newsletter #1: Neuigkeiten](/de/newsletters/2025-12-17-newsletter/#news)
