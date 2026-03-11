---
title: "NIP-17: Private Direktnachrichten"
date: 2025-12-17
translationOf: /en/topics/nip-17.md
translationDate: 2026-03-11
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17 definiert private Direktnachrichten mit NIP-59 Gift Wrapping für die Privatsphäre des Absenders. Im Gegensatz zu NIP-04 DMs, die den Absender im äußeren Event offenlegen, verbirgt NIP-17 den Absender vor Relays und beiläufigen Beobachtern.

## Wie es funktioniert

Nachrichten werden in mehrere Verschlüsselungsschichten eingehüllt:
1. Der eigentliche Nachrichteninhalt liegt in einem rumor Event vom Kind 14.
2. Ein seal verschlüsselt diesen Inhalt für den Empfänger.
3. Ein gift wrap verschlüsselt das seal erneut und veröffentlicht es von einem wegwerfbaren Keypair aus.

Das äußere gift wrap nutzt ein zufälliges, wegwerfbares Keypair, sodass Relays und Beobachter nicht feststellen können, wer die Nachricht gesendet hat.

## Nachrichtenstruktur

- **Kind 14** - Der eigentliche DM-Inhalt innerhalb der eingehüllten Schichten
- **Kind 1059** - Das äußere GiftWrap-Event, das an Relays veröffentlicht wird
- Verwendet NIP-44-Verschlüsselung für die Payloads innerhalb des Wrapping-Flows
- Die Spezifikation wurde verfeinert, um interaktive DM-Features wie Reaktionen besser zu unterstützen

## Sicherheits- und Vertrauensmodell

- Relays können den Absender nicht sehen, da er durch das wegwerfbare Keypair des gift wrap verborgen wird
- Der Empfänger bleibt sichtbar, im `p`-Tag des gift wrap
- Nachrichtentimestamps werden innerhalb eines Fensters randomisiert
- Auf dem Relay gibt es kein sichtbares Threading oder Gruppieren von Konversationen

Der Empfänger erfährt nach dem Auspacken trotzdem, wer die Nachricht gesendet hat. NIP-17 verbirgt die Absenderidentität vor dem Netzwerk, nicht vor dem anderen Teilnehmer. Diese Unterscheidung ist wichtig, wenn Leute von "privaten DMs" sprechen.

## Warum es wichtig ist

NIP-04 DMs verschlüsseln Inhalte, lassen Metadaten aber sichtbar:
- Der Pubkey des Absenders ist öffentlich
- Der Pubkey des Empfängers steht im `p`-Tag
- Timestamps sind exakt

NIP-17 verbirgt den Absender, kostet aber mehr Implementierungskomplexität.

Diese Komplexität bringt einen echten Gewinn an Privatsphäre. Ein Relay kann weiter sehen, dass eine eingehüllte Nachricht an einen Empfänger adressiert ist, aber es kann nicht direkt einen Absender-Empfänger-Graphen aus den Metadaten des äußeren Events bauen, wie es bei Kind-4-Nachrichten möglich ist.

## Interop-Hinweise

NIP-17 definiert auch Inbox-Relay-Listen für private Nachrichten. Clients können ein Kind-10050-Event veröffentlichen, damit Absender wissen, welche Relays sie für die DM-Zustellung ansprechen sollen. Die Trennung von DM-Relay-Routing und öffentlichem Content-Routing hilft dabei, privaten Verkehr nicht an die falschen Orte zu veröffentlichen.

---

**Primärquellen:**
- [NIP-17 Specification](https://github.com/nostr-protocol/nips/blob/master/17.md)
- [PR #2098](https://github.com/nostr-protocol/nips/pull/2098) - wording cleanup and reaction support update

**Erwähnt in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#shopstr-marketplace)
- [Newsletter #5: News](/en/newsletters/2026-01-13-newsletter/#news)

**Siehe auch:**
- [NIP-04: Encrypted Direct Messages (Deprecated)](/de/topics/nip-04/)
- [NIP-44: Encrypted Payloads](/de/topics/nip-44/)
- [NIP-59: Gift Wrap](/de/topics/nip-59/)
