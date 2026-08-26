---
title: "NIP-25: Reaktionen"
date: 2026-07-29
translationOf: /en/topics/nip-25.md
translationDate: 2026-08-26
draft: false
categories:
  - Protocol
  - Social
---

NIP-25 definiert Reaktionen als Kind-`7`-Events. Es gibt Clients eine gemeinsame Event-Form, um ein Emoji oder eine andere kurze Reaktion an eine Notiz, einen Artikel, eine Kleinanzeige oder ein anderes referenziertes Event zu hängen.

## Wie es funktioniert

Ein Reaktions-Event trägt seinen Reaktionstext in `content` und referenziert das Ziel über den `e`-Tag des Ziel-Events. Ist das Ziel addressable, enthält die Reaktion zusätzlich seinen `a`-Tag. Sie enthält außerdem `p`-Tags für den Autor des referenzierten Events, wodurch relays und Clients Benachrichtigungen zustellen können, ohne die Empfänger aus dem Event-Content zu erschließen.

Die Standardreaktion ist `+`, sodass Clients einen leeren Reaktions-Content als positive Antwort behandeln können. Andere Emoji sind gültige Reaktionswerte. Die Spezifikation erlaubt zudem `-` für eine negative Reaktion, was der Nachtrag vom Juli 2022 nach der ursprünglichen Einführung ergänzte.

Clients sollten die Zielreferenz und die Autoren-Tags beim Erstellen einer Reaktion erhalten. Eine Reaktion ist ein gewöhnliches signiertes Event, kann also über normale relay-Subscriptions reisen und von jedem Client gerendert werden, der Kind `7` erkennt.

## Implementierungen

NIP-25 ist als Teil der gewöhnlichen Notiz-Interaktion in Nostr-Clients und -Bibliotheken breit implementiert. Sein einfaches Modell aus Kind und Tags erlaubt Clients, Zählungen, einzelne Reaktionen und Benachrichtigungen ohne separates Transportprotokoll anzuzeigen.

---

**Primärquellen:**
- [NIP-25 Specification](https://github.com/nostr-protocol/nips/blob/master/25.md)
- [Einführungs-Commit](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88)
- [Downvote-Nachtrag](https://github.com/nostr-protocol/nips/commit/89bb08ba8683)

**Erwähnt in:**
- [Newsletter #33: Sechs Jahre Nostr im Juli](/de/newsletters/2026-07-29-newsletter/#sechs-jahre-nostr-im-juli)
- [Newsletter #37: Marmot](/de/newsletters/2026-08-26-newsletter/#marmot)

**Siehe auch:**
- [NIP-01: Basic Protocol](/de/topics/nip-01/)
- [NIP-10: Text Note Threading](/de/topics/nip-10/)
