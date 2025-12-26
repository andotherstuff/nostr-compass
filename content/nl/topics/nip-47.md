---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47 definieert een protocol voor het verbinden van Nostr-applicaties met Lightning-wallets, waardoor betalingen mogelijk zijn zonder wallet-credentials bloot te stellen aan elke app.

## Hoe Het Werkt

Een wallet (zoals Zeus) draait een NWC-service die luistert naar betalingsverzoeken op specifieke Nostr-relays. Apps verbinden met een verbindingsstring die de pubkey van de wallet en relay-informatie bevat. Betalingsverzoeken en antwoorden worden versleuteld tussen de app en wallet.

## Gebruiksscenario's

- **Zappen** - Stuur sats naar posts, profielen of content creators
- **Betalingen** - Betaal Lightning-facturen vanuit elke Nostr-app
- **Abonnementen** - Terugkerende betalingen voor premium content

## Belangrijke Kenmerken

- **Budgetcontroles** - Stel uitgavenlimieten in per verbinding
- **Aangepaste relays** - Gebruik je eigen relay voor wallet-communicatie
- **Parallelle betalingen** - Verwerk meerdere zaps tegelijk voor batch-bewerkingen

---

**Primaire bronnen:**
- [NIP-47 Specificatie](https://github.com/nostr-protocol/nips/blob/master/47.md)

**Vermeld in:**
- [Nieuwsbrief #1: Nieuws](/nl/newsletters/2025-12-17-newsletter/#news)
- [Nieuwsbrief #2: Releases](/nl/newsletters/2025-12-24-newsletter/#releases)

**Zie ook:**
- [NIP-57: Zaps](/nl/topics/nip-57/)
