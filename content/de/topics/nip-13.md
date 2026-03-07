---
title: "NIP-13: Proof of Work"
date: 2026-01-28
translationOf: /en/topics/nip-13.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Spam Prevention
---

NIP-13 definiert ein Proof-of-Work-System für Nostr-Events. Es verlangt Rechenaufwand bei der Erstellung von Events und dient damit als Mechanismus zur Spam-Abwehr.

## Wie es funktioniert

Proof of Work wird nachgewiesen, indem eine Event-ID, also ein SHA256-Hash, mit einer bestimmten Anzahl führender Null-Bits gefunden wird:

1. **Schwierigkeit**: Gemessen in führenden Null-Bits, zum Beispiel 20 Bits = durchschnittlich 2^20 Versuche
2. **Nonce-Tag**: Events enthalten ein `nonce`-Tag mit dem Nonce-Wert und der Zielschwierigkeit
3. **Verifikation**: Relays und Clients können schnell prüfen, dass die Arbeit geleistet wurde

```json
{
  "tags": [["nonce", "12345", "20"]],
  ...
}
```

## Schwierigkeitsstufen

| Bits | Durchschnittliche Versuche | Typische Verwendung |
|------|----------------------------|---------------------|
| 8 | 256 | Minimale Spam-Abschreckung |
| 16 | 65,536 | Leichte Filterung |
| 20 | 1,048,576 | Moderater Schutz |
| 24 | 16,777,216 | Starke Spam-Resistenz |

## Warum es wichtig ist

- **Relay-Zulassung**: Relays können ein Mindest-PoW für die Annahme von Events verlangen
- **Rate Limiting**: Höhere Schwierigkeit für Aktionen wie Account-Registrierung
- **Spam-Filterung**: Clients können Events mit hohem PoW in Feeds priorisieren
- **Reputations-Bootstrap**: Neue Accounts können durch PoW Commitment zeigen

Die nützliche Eigenschaft ist die asymmetrische Kostenverteilung. Viele akzeptable Events zu erzeugen wird für den Sender teuer, während die Prüfung für Relays und Clients billig bleibt.

## Tradeoffs

- Bevorzugt Nutzer mit leistungsfähiger Hardware
- Wirft Fragen zum Energieverbrauch auf
- Verhindert nicht jeden Spam, sondern erhöht nur die Kosten

PoW verlagert Spam-Resistenz außerdem von Account-Identität hin zur Verfügbarkeit von Rechenleistung. Das kann in permissionless Umgebungen helfen, unterscheidet aber nicht zwischen einem legitimen neuen Nutzer und einem gut finanzierten Spammer.

---

**Primärquellen:**
- [NIP-13 Specification](https://github.com/nostr-protocol/nips/blob/master/13.md)

**Erwähnt in:**
- [Newsletter #7: News](/en/newsletters/2026-01-28-newsletter/#news)
- [Newsletter #12: News](/en/newsletters/2026-03-04-newsletter/#news)

**Siehe auch:**
- [NIP-01: Basic Protocol](/de/topics/nip-01/)
