---
title: "NIP-57: Zaps"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Wallet
  - Lightning
  - Sociaal
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

## Vertrouwen en Afwegingen

Zaps zijn nuttig omdat ze betalingen zichtbaar maken binnen de sociale graph, maar het receipt wordt nog steeds gemaakt door de wallet-infrastructuur van de ontvanger. De specificatie zelf merkt op dat een zap receipt geen universeel betalingsbewijs is. Je kunt het het best begrijpen als een door de wallet ondertekende verklaring dat een invoice die aan een zap request was gekoppeld, is betaald.

---

**Primaire bronnen:**
- [NIP-57-specificatie](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Vermeld in:**
- [Nieuwsbrief #1: Nieuws](/en/newsletters/2025-12-17-newsletter/#news)
- [Nieuwsbrief #2: Nieuws](/en/newsletters/2025-12-24-newsletter/#news)
- [Nieuwsbrief #3: Opmerkelijke codewijzigingen](/en/newsletters/2025-12-31-newsletter/#amethyst-android)
- [Nieuwsbrief #9: NIP-updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)

**Zie ook:**
- [NIP-47: Nostr Wallet Connect](/nl/topics/nip-47/)
