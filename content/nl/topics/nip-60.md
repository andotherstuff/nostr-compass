---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Ecash
---

NIP-60 definieert hoe Cashu-gebaseerde ecash-wallets binnen Nostr werken. Wallet-informatie wordt op relays opgeslagen, waardoor draagbare wallets mogelijk zijn die in verschillende applicaties werken zonder aparte accounts nodig te hebben.

## Hoe Het Werkt

NIP-60 gebruikt drie kern-eventtypen die op relays worden opgeslagen, plus een optioneel hulpevent voor openstaande quotes:

**Wallet Event (kind 17375):** Een vervangbaar event met versleutelde wallet-configuratie, inclusief mint-URLs en een private key voor het ontvangen van betalingen. Deze key staat los van de Nostr identity key van de gebruiker.

**Token Events (kind 7375):** Slaan versleutelde, niet-uitgegeven Cashu proofs op. Wanneer proofs worden uitgegeven, verwijdert de client het oude event en maakt een nieuw event aan met eventuele overgebleven proofs.

**Spending History (kind 7376):** Optionele transactierecords die geldbewegingen tonen, met versleutelde inhoud en verwijzingen naar aangemaakte en vernietigde token events.

**Quote Events (kind 7374):** Optionele versleutelde state voor openstaande mint quotes. De specificatie raadt kortlevende events met expiration tags aan, vooral voor gevallen waarin lokale state niet genoeg is.

## Statusmodel

NIP-60 gaat over walletsynchronisatie, niet over de handeling van geld ontvangen. Het wallet event vertelt een client welke mints en welke wallet key moeten worden gebruikt, terwijl token events de feitelijke balansstatus vormen omdat ze de niet-uitgegeven proofs bevatten.

Dat onderscheid is belangrijk voor interoperabiliteit. Twee clients kunnen alleen dezelfde wallet tonen als ze token rollover op dezelfde manier interpreteren: proofs uitgeven, vervangende proofs publiceren en het uitgegeven token event verwijderen via [NIP-09](/nl/topics/nip-09/) zodat andere clients uitgegeven proofs niet in de balans blijven meetellen.

## Waarom Het Belangrijk Is

- **Gebruiksgemak** - Nieuwe gebruikers kunnen direct ecash ontvangen zonder externe accountconfiguratie
- **Interoperabiliteit** - Wallet-gegevens volgen gebruikers tussen verschillende Nostr-applicaties
- **Privacy** - Alle wallet-gegevens zijn versleuteld naar de sleutels van de gebruiker
- **Proof-beheer** - Houdt wallet-statusovergangen bij zodat clients op dezelfde balans kunnen uitkomen

## Interop Notes

Clients zoeken eerst naar wallet relay-informatie via kind 10019 en vallen terug op de relay-lijst van de gebruiker uit [NIP-65](/nl/topics/nip-65/) als er geen aparte wallet relay-lijst aanwezig is. Die fallback is nuttig, maar betekent ook dat wallet-portabiliteit nog steeds afhangt van relays die de versleutelde wallet events daadwerkelijk opslaan en serveren.

De specificatie vereist ook dat de private key van de wallet gescheiden blijft van de Nostr identity key van de gebruiker. Dat houdt de afhandeling van wallet-ontvangsten los van de hoofd-signing key en verkleint de kans dat een key voor twee verschillende doelen wordt hergebruikt.

## Workflow

1. De client haalt wallet-configuratie op van wallet-relays of de relay-lijst van de gebruiker
2. Token events worden geladen en ontsleuteld om beschikbare fondsen te bepalen
3. Uitgeven maakt nieuwe token events aan en verwijdert oude
4. Optionele history events leggen transacties vast als referentie voor de gebruiker

---

**Primaire bronnen:**
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Vermeld in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #11: NIP Deep Dive](/nl/newsletters/2026-02-25-newsletter/)
- [Newsletter #13: Shopstr and Milk Market Open MCP Commerce Surfaces](/en/newsletters/2026-03-11-newsletter/)

**Zie ook:**
- [NIP-57: Zaps](/nl/topics/nip-57/)
- [NIP-09: Event Deletion Request](/nl/topics/nip-09/)
- [NIP-47: Nostr Wallet Connect](/nl/topics/nip-47/)
