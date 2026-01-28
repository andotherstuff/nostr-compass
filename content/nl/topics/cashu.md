---
title: "Cashu: Ecash Protocol"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-01-28
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu is een Chaumian ecash protocol gebouwd op Bitcoin en Lightning Network, dat private, directe en goedkope betalingen mogelijk maakt via cryptografische tokens.

## Hoe Het Werkt

Cashu gebruikt blinde handtekeningen om ontraceerbare ecash tokens te creëren:

1. **Minting**: Gebruikers storten Bitcoin/Lightning bij een mint en ontvangen geblindeerde tokens
2. **Uitgeven**: Tokens kunnen peer-to-peer worden overgedragen zonder betrokkenheid van de mint
3. **Inwisseling**: Ontvangers wisselen tokens in bij de mint voor Bitcoin/Lightning

De mint kan stortingen niet koppelen aan inwisselingen vanwege het blinderingsproces, wat sterke privacygaranties biedt.

## Belangrijke Eigenschappen

- **Privacy**: Mint kan tokenoverdrachten tussen gebruikers niet volgen
- **Direct**: Overdrachten gebeuren offline, geen blockchain-bevestiging nodig
- **Lage kosten**: Geen on-chain kosten voor tokenoverdrachten
- **Custodial**: Gebruikers vertrouwen de mint om inwisselingen te honoreren

## Nostr-Integratie

Cashu integreert op verschillende manieren met Nostr:

- **Nutzaps**: Ecash tokens verzonden als zaps met verbeterde privacy
- **Escrow**: HTLC-gebaseerde betalingsescrow voor diensten zoals ridesharing
- **Wallets**: Nostr-native wallets slaan versleutelde Cashu tokens op relays op
- **[NIP-87](/nl/topics/nip-87/)**: Mint-ontdekking en reviews via Nostr

## Vertrouwensmodel

In tegenstelling tot zelf-custodial Bitcoin vereist Cashu het vertrouwen van mint-operators. Gebruikers moeten:
- Reputabele, goed-beoordeelde mints gebruiken
- Kleine saldi aanhouden passend bij het vertrouwensniveau
- Begrijpen dat mints kunnen exit-scammen of offline gaan, waarbij ze fondsen meenemen

## Gerelateerd

- [NIP-87](/nl/topics/nip-87/) - Cashu Mint-Aanbevelingen
- [NIP-60](/nl/topics/nip-60/) - Nostr Wallet
