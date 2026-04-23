---
title: "NIP-63: Paywall / Premium Content"
date: 2025-12-17
translationDate: 2026-03-07
translationOf: /en/topics/nip-63.md
draft: false
categories:
  - Protocol
  - Monetisatie
---

NIP-63 is een voorgestelde standaard voor het afhandelen van afgesloten content binnen het Nostr-protocol, waardoor creators betaling kunnen vereisen voordat content wordt onthuld.

## Hoe Het Werkt

Content creators kunnen events publiceren waarbij de volledige content versleuteld is of verborgen blijft achter een paywall. Na betalingsverificatie wordt de content ontgrendeld voor de betalende gebruiker.

Het voorstel gaat bewust over het protocoloppervlak voor premium content, niet over het verplicht stellen van een enkel betaalspoor of businessmodel. Dat houdt het flexibel, maar het betekent ook dat wallets, clients en publishers in de praktijk nog steeds overeenstemming moeten bereiken over de unlock flow.

## Waarom Het Belangrijk Is

Zonder een gedeeld formaat wordt elk Nostr-paywallsysteem zijn eigen silo. Een gemeenschappelijke NIP zou het mogelijk maken dat de ene client premium content publiceert en een andere client begrijpt dat de content afgesloten is, wat er betaald moet worden en wanneer die zichtbaar moet worden.

Dat garandeert nog geen portabiliteit. NIP-63 is nog steeds een voorstel in [PR #2156](https://github.com/nostr-protocol/nips/pull/2156), dus implementaties kunnen nog uiteenlopen terwijl het ontwerp nog wordt besproken.

## Gebruiksscenario's

- Artikelen alleen voor abonnees
- Premium mediacontent
- Pay-per-view evenementen
- Exclusieve toegang tot creators

## Afwegingen

Paywall-metadata kan openbaar zijn, ook wanneer de premium payload dat niet is. Dat geeft clients genoeg informatie om een aanbod te tonen, maar het betekent ook dat het bestaan van betaalde content zichtbaar is voor iedereen die het event kan lezen.

Creators moeten ook nadenken over wat er na de unlock gebeurt. Zodra plaintext aan een betalende gebruiker wordt getoond, kan het protocol niet voorkomen dat die gebruiker het elders kopieert.

---

**Primaire bronnen:**
- [NIP-63-voorstel (PR #2156)](https://github.com/nostr-protocol/nips/pull/2156)

**Vermeld in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**Zie ook:**
- [NIP-57: Zaps](/nl/topics/nip-57/)
