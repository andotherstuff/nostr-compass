---
title: "NIP-57: Zaps"
date: 2025-12-17
translationOf: /en/topics/nip-57.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57 definieert zaps, een manier om Lightning-betalingen te koppelen aan Nostr-identiteiten en content. De NIP standaardiseert zowel het verzoek om een zap-enabled invoice als het ontvangstbewijs-event dat wallets na betaling publiceren.

## Hoe Het Werkt

1. De client ontdekt het LNURL-endpoint van de ontvanger via profielmetadata of een `zap` tag op het doel-event.
2. De client stuurt een ondertekend kind `9734` zap request naar de LNURL-callback van de ontvanger, niet naar relays.
3. De gebruiker betaalt de invoice.
4. De wallet server van de ontvanger publiceert een kind `9735` zap receipt naar de relays die in het zap request staan.
5. Clients valideren en tonen de zap.

## Zap Request (kind 9734)

Het zap request is een ondertekend event dat de betaler en het beoogde doel identificeert. Het bevat meestal:

- `p` tag met de pubkey van de ontvanger
- `e` tag met het event dat wordt gezapt (optioneel)
- `amount` tag in millisatoshis
- `relays` tag met de lijst van relays waar het receipt moet worden gepubliceerd

Addressable content kan een `a` tag gebruiken in plaats van, of naast, een `e` tag. De optionele `k` tag legt het doel-kind vast.

## Zap Receipt (kind 9735)

Gepubliceerd door de wallet server van de ontvanger na betalingsbevestiging. Het bevat:

- Het oorspronkelijke zap request in een `description` tag
- `bolt11` tag met de betaalde invoice
- `preimage` tag die de betaling bewijst

Clients moeten het receipt valideren tegen de LNURL `nostrPubkey` van de ontvanger, het invoicebedrag en het oorspronkelijke zap request. Een receipt zonder die validatie is alleen een claim.

## Trust and Tradeoffs

## Private en Anonieme Zaps

Private zaps voegen daarbovenop een vertrouwelijkheidslaag toe. Een afzender kan de `content` van het zap request voor de ontvanger encrypten en een `anon`-tag op het outer request opnemen, zodat het relaynetwerk het betalingsdoel ziet maar de meegestuurde notitie niet kan lezen. Een anonieme zap gaat nog een stap verder: de client genereert voor het zap request zelf een nieuw ephemeral keypair, zodat het receipt nog steeds bewijst dat een betaling heeft plaatsgevonden, maar de ontvanger de zap niet aan de langlevende pubkey van de afzender kan koppelen.

## Zap Goals en Splits

NIP-57 vormt de basis voor het zap-goalsysteem uit [NIP-75](/nl/topics/nip-75/). Een goal is een kind `9041`-event dat een target amount en een relayset opgeeft waar receipts meetellen, en clients tellen de goal progress op door de gevalideerde `bolt11`-bedragen van gematchte kind `9735`-events te sommeren.

Zap splits, gedefinieerd in een appendix van de NIP, laten een ontvanger een kind `0`-profiel publiceren met meerdere gewogen `zap`-tags zodat een enkele zap-betaling atomair over meerdere pubkeys wordt verdeeld. [Amethyst](https://github.com/vitorpamplona/amethyst), [Damus](https://github.com/damus-io/damus) en [noStrudel](https://github.com/hzrd149/nostrudel) implementeren split-paying end-to-end.

Zaps zijn nuttig omdat ze betalingen zichtbaar maken binnen de sociale graph, maar het receipt wordt nog steeds gemaakt door de wallet-infrastructuur van de ontvanger. De specificatie zelf merkt op dat een zap receipt geen universeel betalingsbewijs is. Je kunt het het best begrijpen als een door de wallet ondertekende verklaring dat een invoice die aan een zap request was gekoppeld, is betaald.

---

**Primaire bronnen:**
- [NIP-57 Specification](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Vermeld in:**
- [Newsletter #1: News](/nl/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: News](/nl/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #9: NIP Updates](/nl/newsletters/2026-02-11-newsletter/)
- [Newsletter #19: NIP Deep Dive](/en/newsletters/2026-04-22-newsletter/)

**Zie ook:**
- [NIP-47: Nostr Wallet Connect](/nl/topics/nip-47/)
- [NIP-75: Zap Goals](/nl/topics/nip-75/)
- [NIP-53: Live Activities](/nl/topics/nip-53/)
