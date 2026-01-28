---
title: "NIP-13: Proof of Work"
date: 2026-01-28
translationOf: /en/topics/nip-13.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Spam Prevention
---

NIP-13 definiert ein Proof-of-Work-System für Nostr-Events, das Rechenaufwand zur Erstellung von Events als Spam-Präventionsmechanismus erfordert.

## Funktionsweise

Proof of Work wird nachgewiesen, indem eine Event-ID (SHA256-Hash) mit einer bestimmten Anzahl führender Null-Bits gefunden wird:

1. **Schwierigkeit**: Gemessen in führenden Null-Bits (z.B. 20 Bits = durchschnittlich 2^20 Versuche)
2. **Nonce-Tag**: Events enthalten ein `nonce`-Tag mit dem Nonce-Wert und der Zielschwierigkeit
3. **Verifizierung**: Relays und Clients können schnell überprüfen, dass die Arbeit geleistet wurde

```json
{
  "tags": [["nonce", "12345", "20"]],
  ...
}
```

## Schwierigkeitsstufen

| Bits | Durchschnittliche Versuche | Typische Verwendung |
|------|------------------|-------------|
| 8 | 256 | Minimale Spam-Abschreckung |
| 16 | 65.536 | Leichte Filterung |
| 20 | 1.048.576 | Moderater Schutz |
| 24 | 16.777.216 | Starke Spam-Resistenz |

## Anwendungsfälle

- **Relay-Zulassung**: Relays können Mindest-PoW für Event-Akzeptanz verlangen
- **Rate-Limiting**: Höhere Schwierigkeit für Aktionen wie Kontoregistrierung
- **Spam-Filterung**: Clients können Events mit hohem PoW in Feeds priorisieren
- **Reputations-Bootstrap**: Neue Konten können Engagement durch PoW demonstrieren

## Einschränkungen

- Bevorzugt Benutzer mit leistungsstarker Hardware
- Bedenken bezüglich Energieverbrauch
- Verhindert nicht allen Spam, erhöht nur die Kosten

## Verwandt

- [NIP-01](/de/topics/nip-01/) - Grundprotokoll
