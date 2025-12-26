---
title: "NIP-57: Zaps"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
  - Sociaal
---

NIP-57 definieert zaps, een manier om Lightning-betalingen te sturen naar Nostr-gebruikers en content met cryptografisch bewijs dat de betaling heeft plaatsgevonden.

## Hoe Het Werkt

1. Client haalt het Lightning-adres van de ontvanger op uit hun kind 0 profiel
2. Client vraagt een factuur aan bij de LNURL-server van de ontvanger, inclusief een zap request event
3. Gebruiker betaalt de factuur
4. LNURL-server publiceert een kind 9735 zap-ontvangst naar Nostr-relays
5. Clients tonen de zap op de content van de ontvanger

## Zap Request (kind 9734)

Het zap request is een ondertekend event dat bewijst wie de zap heeft gestuurd en naar welke content. Het bevat:
- `p` tag met de pubkey van de ontvanger
- `e` tag met het event dat wordt gezapt (optioneel)
- `amount` tag in millisatoshis
- `relays` tag die aangeeft waar de ontvangst gepubliceerd moet worden

## Zap-ontvangst (kind 9735)

Gepubliceerd door de LNURL-server na betalingsbevestiging. Bevat:
- Het originele zap request in een `description` tag
- `bolt11` tag met de betaalde factuur
- `preimage` tag als bewijs van betaling

---

**Primaire bronnen:**
- [NIP-57 Specificatie](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Vermeld in:**
- [Nieuwsbrief #1: Nieuws](/nl/newsletters/2025-12-17-newsletter/#news)
- [Nieuwsbrief #2: Nieuws](/nl/newsletters/2025-12-24-newsletter/#news)

**Zie ook:**
- [NIP-47: Nostr Wallet Connect](/nl/topics/nip-47/)
