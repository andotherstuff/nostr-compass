---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2025-12-31
draft: false
categories:
  - Portemonnee
  - Ecash
---

NIP-60 definieert hoe Cashu-gebaseerde ecash-wallets werken binnen Nostr. Wallet-informatie wordt opgeslagen op relays, waardoor draagbare wallets mogelijk zijn die werken in verschillende applicaties zonder aparte accounts te vereisen.

## Hoe Het Werkt

NIP-60 gebruikt drie soorten events die op relays worden opgeslagen:

**Wallet-Event (kind 17375):** Een vervangbaar event met versleutelde wallet-configuratie, inclusief mint-URLs en een privésleutel voor het ontvangen van betalingen. Deze sleutel is gescheiden van de Nostr-identiteitssleutel van de gebruiker.

**Token-Events (kind 7375):** Slaan versleutelde, niet-uitgegeven Cashu-proofs op. Wanneer proofs worden uitgegeven, verwijdert de client het oude event en maakt een nieuw event met de resterende proofs.

**Uitgavegeschiedenis (kind 7376):** Optionele transactierecords die geldbewegingen tonen, met versleutelde inhoud en verwijzingen naar aangemaakte/vernietigde token-events.

## Belangrijkste Kenmerken

- **Gebruiksgemak** - Nieuwe gebruikers kunnen direct ecash ontvangen zonder externe accountconfiguratie
- **Interoperabiliteit** - Wallet-gegevens volgen gebruikers over verschillende Nostr-applicaties
- **Privacy** - Alle wallet-gegevens zijn versleuteld met de sleutels van de gebruiker
- **Proof-beheer** - Houdt bij welke token-events zijn uitgegeven om dubbele uitgaven te voorkomen

## Werkstroom

1. Client haalt wallet-configuratie op van relays
2. Token-events worden geladen en ontsleuteld om beschikbare fondsen te verkrijgen
3. Uitgeven creëert nieuwe token-events en verwijdert oude
4. Optionele geschiedenisevents registreren transacties ter referentie voor de gebruiker

---

**Primaire bronnen:**
- [NIP-60 Specificatie](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Vermeld in:**
- [Nieuwsbrief #3: December Terugblik](/nl/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Zie ook:**
- [NIP-57: Zaps](/nl/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/nl/topics/nip-47/)
