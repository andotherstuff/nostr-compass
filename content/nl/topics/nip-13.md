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

NIP-13 definieert een proof-of-work systeem voor Nostr events, waarbij computationele inspanning vereist is om events te creëren als spampreventie-mechanisme.

## Hoe Het Werkt

Proof of work wordt aangetoond door een event ID (SHA256 hash) te vinden met een bepaald aantal voorloopnulbits:

1. **Moeilijkheidsgraad**: Gemeten in voorloopnulbits (bijv. 20 bits = gemiddeld 2^20 pogingen)
2. **Nonce Tag**: Events bevatten een `nonce` tag met de nonce-waarde en doelmoeilijkheid
3. **Verificatie**: Relays en clients kunnen snel verifiëren dat het werk is gedaan

```json
{
  "tags": [["nonce", "12345", "20"]],
  ...
}
```

## Moeilijkheidsniveaus

| Bits | Gemiddelde Pogingen | Typisch Gebruik |
|------|---------------------|-----------------|
| 8 | 256 | Minimale spamafschrikking |
| 16 | 65.536 | Lichte filtering |
| 20 | 1.048.576 | Matige bescherming |
| 24 | 16.777.216 | Sterke spamresistentie |

## Toepassingen

- **Relay-Toegang**: Relays kunnen minimale PoW vereisen voor event-acceptatie
- **Rate Limiting**: Hogere moeilijkheid voor acties zoals accountregistratie
- **Spamfiltering**: Clients kunnen high-PoW events prioriteren in feeds
- **Reputatie-Bootstrap**: Nieuwe accounts kunnen toewijding demonstreren via PoW

## Beperkingen

- Bevoordeelt gebruikers met krachtige hardware
- Energieverbruik-zorgen
- Voorkomt niet alle spam, verhoogt alleen de kosten

## Gerelateerd

- [NIP-01](/nl/topics/nip-01/) - Basisprotocol
