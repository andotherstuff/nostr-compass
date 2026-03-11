---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
translationOf: /en/topics/nip-47.md
translationDate: 2026-03-11
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47 definieert Nostr Wallet Connect, een protocol waarmee een Nostr-app met een externe Lightning-walletservice kan praten zonder de hoofdcredentials van de wallet bloot te stellen aan elke client.

## Hoe het werkt

Een walletservice publiceert een vervangbaar kind `13194` info-event dat beschrijft welke methoden en encryptiemodi worden ondersteund. Een client maakt verbinding via een `nostr+walletconnect://`-URI die de pubkey van de walletservice, een of meer relays en een speciaal secret voor die verbinding bevat. Verzoeken worden verzonden als kind `23194` events en responses komen terug als kind `23195` events.

## Opdrachten en meldingen

Veelgebruikte methoden zijn `pay_invoice`, `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance` en `get_info`. Walletservices kunnen ook meldingen pushen zoals `payment_received`, `payment_sent` en `hold_invoice_accepted`.

De spec kreeg in de loop van de tijd verschillende optionele methoden erbij, maar recente opschoning heeft de `multi_`-betaalmethoden verwijderd. In de praktijk is interoperabiliteit beter wanneer clients zich houden aan de opdrachten die in het info-event van de wallet worden geadverteerd, in plaats van uit te gaan van een brede methodenset.

## Toepassingen

- **Zaps** - Verstuur sats naar posts, profielen of makers van content
- **Betalingen** - Betaal Lightning-facturen vanuit elke Nostr-app
- **Scheiding van wallet-UX** - Gebruik een walletservice in meerdere Nostr-clients

## Beveiligings- en interoperabiliteitsnotities

De verbindings-URI bevat een speciaal secret dat de client gebruikt voor signing en encryptie. Daardoor krijgt elke app een eigen walletidentiteit, wat helpt bij zowel intrekking als privacy. Een wallet kan bestedingslimieten instellen, methoden uitschakelen of een enkele verbinding intrekken zonder andere verbindingen te raken.

NIP-44 heeft nu de voorkeur als encryptiemodus. De spec documenteert nog steeds NIP-04-fallback voor oudere implementaties, dus clients moeten de geadverteerde `encryption`-tag van de wallet inspecteren in plaats van ervan uit te gaan dat elke wallet al is gemigreerd.

---

**Primaire bronnen:**
- [NIP-47-specificatie](https://github.com/nostr-protocol/nips/blob/master/47.md)
- [PR #1913: Hold Invoice-ondersteuning](https://github.com/nostr-protocol/nips/pull/1913)
- [PR #2210: Vereenvoudiging](https://github.com/nostr-protocol/nips/pull/2210)

**Vermeld in:**
- [Nieuwsbrief #1: News](/nl/newsletters/2025-12-17-newsletter/#news)
- [Nieuwsbrief #2: Releases](/nl/newsletters/2025-12-24-newsletter/#releases)
- [Nieuwsbrief #3: December Recap](/nl/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Nieuwsbrief #8: NIP Deep Dive](/nl/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-47-nostr-wallet-connect)
- [Nieuwsbrief #10: NIP Updates](/nl/newsletters/2026-02-18-newsletter/#nip-updates)

**Zie ook:**
- [NIP-57: Zaps](/nl/topics/nip-57/)
