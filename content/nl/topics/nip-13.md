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

NIP-13 definieert een proof-of-work-systeem voor Nostr events, waarbij rekenwerk nodig is om events te maken als mechanisme voor spampreventie.

## Hoe Het Werkt

Proof of work wordt aangetoond door een event ID (SHA256-hash) te vinden met een opgegeven aantal voorloopnulbits:

1. **Moeilijkheidsgraad**: Gemeten in voorloopnulbits (bijv. 20 bits = gemiddeld 2^20 pogingen)
2. **Nonce Tag**: Events bevatten een `nonce` tag met de nonce-waarde en de doelmoeilijkheid
3. **Verificatie**: Relays en clients kunnen snel controleren dat het werk is gedaan

```json
{
  "tags": [["nonce", "12345", "20"]],
  ...
}
```

## Moeilijkheidsniveaus

| Bits | Gemiddelde pogingen | Typisch gebruik |
|------|---------------------|-----------------|
| 8 | 256 | Minimale afschrikking tegen spam |
| 16 | 65.536 | Lichte filtering |
| 20 | 1.048.576 | Gematigde bescherming |
| 24 | 16.777.216 | Sterke weerstand tegen spam |

## Waarom Het Belangrijk Is

- **Relay-toelating**: Relays kunnen een minimale PoW eisen voordat ze een event accepteren
- **Rate limiting**: Hogere moeilijkheid voor acties zoals accountregistratie
- **Spamfiltering**: Clients kunnen events met hoge PoW voorrang geven in feeds
- **Reputatiebootstrap**: Nieuwe accounts kunnen via PoW laten zien dat ze moeite willen doen

De nuttige eigenschap is asymmetrische kost. Veel acceptabele events maken wordt duur voor de verzender, terwijl het controleren van het bewijs goedkoop blijft voor relays en clients.

## Afwegingen

- Bevoordeelt gebruikers met krachtige hardware
- Zorgt voor vragen over energieverbruik
- Voorkomt niet alle spam, maar verhoogt alleen de kost ervan

PoW verschuift spamweerstand ook van accountidentiteit naar beschikbaarheid van rekenkracht. Dat kan helpen in permissionless omgevingen, maar het onderscheidt een legitieme nieuwe gebruiker niet van een goed gefinancierde spammer.

---

**Primaire bronnen:**
- [NIP-13 Specification](https://github.com/nostr-protocol/nips/blob/master/13.md)

**Vermeld in:**
- [Newsletter #7: News](/en/newsletters/2026-01-28-newsletter/#news)
- [Newsletter #12: News](/en/newsletters/2026-03-04-newsletter/#news)

**Zie ook:**
- [NIP-01: Basic Protocol](/nl/topics/nip-01/)
