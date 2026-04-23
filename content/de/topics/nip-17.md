---
title: "NIP-17: Private Direct Messages"
date: 2025-12-17
translationOf: /en/topics/nip-17.md
translationDate: 2026-04-22
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17 definiert private Direct Messages, die NIP-59-Gift-Wrapping für Sender-Privatsphäre nutzen. Anders als NIP-04-DMs, die den Sender im äußeren Event offenlegen, verbirgt NIP-17 den Sender vor Relays und beiläufigen Beobachtern.

## Funktionsweise

Nachrichten sind in mehrere Verschlüsselungsschichten eingepackt:
1. Der eigentliche Nachrichteninhalt lebt in einem Rumor-Event vom kind 14.
2. Ein Seal verschlüsselt diesen Inhalt für den Empfänger.
3. Ein Gift Wrap verschlüsselt den Seal erneut und veröffentlicht ihn von einem Wegwerf-Keypair aus.

Der äußere Gift Wrap nutzt ein zufälliges, Wegwerf-Keypair, sodass Relays und Beobachter nicht feststellen können, wer die Nachricht gesendet hat.

## Nachrichtenstruktur

- **Kind 14** - Der eigentliche DM-Inhalt innerhalb der eingepackten Schichten
- **Kind 1059** - Das äußere Gift-Wrap-Event, das an Relays publiziert wird
- Verwendet NIP-44-Verschlüsselung für die Payloads innerhalb des Wrapping-Flows
- Die Spezifikation wurde verfeinert, um interaktive DM-Features wie Reaktionen besser zu unterstützen

## Sicherheits- und Vertrauensmodell

- Relays können den Sender nicht sehen, weil das Wegwerf-Keypair des Gift Wraps ihn verbirgt
- Der Empfänger bleibt sichtbar, im `p`-Tag des Gift Wraps
- Nachrichtentimestamps werden innerhalb eines Fensters randomisiert
- Es gibt kein sichtbares Threading oder Conversation Grouping auf Relay-Ebene

Der Empfänger erfährt nach dem Entpacken trotzdem, wer die Nachricht gesendet hat. NIP-17 verbirgt die Senderidentität vor dem Netzwerk, nicht vor dem anderen Teilnehmer. Diese Unterscheidung ist wichtig, wenn von "privaten DMs" gesprochen wird.

## Warum das wichtig ist

NIP-04-DMs verschlüsseln Inhalte, lassen aber Metadaten sichtbar:
- Der pubkey des Senders ist öffentlich
- Der pubkey des Empfängers steht im `p`-Tag
- Timestamps sind exakt

NIP-17 verbirgt den Sender, erkauft sich das aber mit höherer Implementierungskomplexität.

Diese Komplexität bringt einen echten Privatsphäregewinn. Ein Relay kann weiterhin sehen, dass eine verpackte Nachricht an einen Empfänger adressiert ist, aber es kann aus den äußeren Event-Metadaten nicht direkt einen Sender-Empfänger-Graphen ableiten wie bei kind-4-Nachrichten.

## Interop-Hinweise

NIP-17 definiert außerdem Inbox-Relay-Listen für private Nachrichten. Clients können ein kind-10050-Event veröffentlichen, damit Sender wissen, welche Relays sie für die DM-Zustellung nutzen sollen. Private Relay-Routing-Daten getrennt von öffentlichem Content-Routing zu halten, hilft dabei, private Kommunikation nicht an die falschen Orte zu veröffentlichen.

---

**Primärquellen:**
- [NIP-17 Specification](https://github.com/nostr-protocol/nips/blob/master/17.md)
- [PR #2098](https://github.com/nostr-protocol/nips/pull/2098) - wording cleanup and reaction support update

**Erwähnt in:**
- [Newsletter #1: NIP Updates](/de/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: News](/de/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/de/newsletters/2025-12-31-newsletter/)
- [Newsletter #3: Notable Code Changes](/de/newsletters/2025-12-31-newsletter/)
- [Newsletter #5: News](/de/newsletters/2026-01-13-newsletter/)
- [Newsletter #13: Vector](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: NipLock password manager](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-04: Encrypted Direct Messages (Deprecated)](/de/topics/nip-04/)
- [NIP-44: Encrypted Payloads](/de/topics/nip-44/)
- [NIP-59: Gift Wrap](/de/topics/nip-59/)
