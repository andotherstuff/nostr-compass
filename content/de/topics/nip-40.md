---
title: "NIP-40: Ablaufzeitstempel"
date: 2025-12-17
translationOf: /en/topics/nip-40.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
---

NIP-40 definiert ein Ablauf-Tag, das Relays mitteilt, wann ein Event gelöscht werden soll.

## Wie es funktioniert

Events enthalten ein `expiration`-Tag mit einem Unix-Zeitstempel:

```json
["expiration", "1734567890"]
```

Nach dieser Zeit sollten Relays das Event löschen und die Auslieferung verweigern.

## Warum es wichtig ist

- Ephemerer Inhalt, der nach einer festgelegten Zeit verschwinden soll
- Zeitlich begrenzte Angebote oder Ankündigungen
- Ablauf von Angeboten in Marktplätzen, etwa bei Shopstr
- Reduzierung der Relay-Speicheranforderungen

Expiration ist ein Hinweis zur Aufbewahrung und kein Widerrufssystem. Es hilft dabei, das Verhalten von Relays bei veralteten Inhalten anzugleichen, garantiert aber keine Löschung, sobald ein anderes Relay, ein Client oder ein Archiv das Event bereits kopiert hat.

## Vertrauens- und Sicherheitshinweise

- Relays sind nicht verpflichtet, den Ablauf zu berücksichtigen, auch wenn es die meisten tun
- Clients sollten sich nicht auf den Ablauf für sicherheitskritische Inhaltslöschung verlassen
- Sobald Inhalt von einem anderen Client abgerufen wurde, kann er zwischengespeichert oder erneut veröffentlicht werden
- Expiration verbirgt nicht, dass ein Event existiert hat. Event-IDs, Zitate oder Kopien außerhalb des Relays können nach Ablauf des Zeitstempels weiter bestehen

---

**Primärquellen:**
- [NIP-40 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/40.md)

**Erwähnt in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/)

**Siehe auch:**
- [NIP-01: Basic Protocol](/de/topics/nip-01/)
