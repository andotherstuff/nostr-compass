---
title: "NIP-87: Ecash Mint Vindbaarheid"
date: 2026-01-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---

NIP-87 definieert hoe ecash mints (Cashu en Fedimint) zichzelf kunnen aankondigen op Nostr, en hoe gebruikers mints kunnen aanbevelen aan anderen.

## Event Kinds

- **kind 38172** - Cashu mint-aankondiging (gepubliceerd door mint-operators)
- **kind 38173** - Fedimint-aankondiging (gepubliceerd door mint-operators)
- **kind 38000** - Mint-aanbeveling (gepubliceerd door gebruikers)

## Hoe Het Werkt

1. **Mint-operators** publiceren de URL van hun mint, ondersteunde functies en netwerk (mainnet/testnet)
2. **Gebruikers** die een mint vertrouwen publiceren aanbevelingen met optionele reviews
3. **Andere gebruikers** zoeken naar aanbevelingen van mensen die ze volgen om vertrouwde mints te ontdekken

## Cashu Mint-aankondiging

```json
{
  "id": "<event-id>",
  "pubkey": "<mint-operator-pubkey>",
  "created_at": 1736200000,
  "kind": 38172,
  "tags": [
    ["d", "<mint-pubkey>"],
    ["u", "https://mint.example.com"],
    ["nuts", "1,2,3,4,5,6,7"],
    ["n", "mainnet"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

De `nuts` tag lijst ondersteunde NUTs (Notation, Usage, and Terminology specs voor Cashu).

## Gebruikersaanbevelingen

```json
{
  "id": "<event-id>",
  "pubkey": "<recommender-pubkey>",
  "created_at": 1736200000,
  "kind": 38000,
  "tags": [
    ["k", "38172"],
    ["d", "<mint-identifier>"],
    ["a", "38172:mint-pubkey:<d-tag>", "wss://relay"]
  ],
  "content": "Ik gebruik deze mint al maanden, zeer betrouwbaar",
  "sig": "<signature>"
}
```

Gebruikers kunnen reviews opnemen in het `content` veld en verwijzen naar specifieke mint-aankondigings-events.

---

**Primaire bronnen:**
- [NIP-87 Specificatie](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Genoemd in:**
- [Nieuwsbrief #4: Releases](/nl/newsletters/2026-01-07-newsletter/#releases)

**Zie ook:**
- [NIP-60: Cashu Wallet](/nl/topics/nip-60/)
