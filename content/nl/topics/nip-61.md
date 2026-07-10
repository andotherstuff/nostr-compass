---
title: "NIP-61: Nutzaps"
date: 2026-06-17
draft: false
categories:
  - Zaps
  - Ecash
translationOf: /en/topics/nip-61.md
translationDate: 2026-07-01
---

NIP-61 definieert "nutzaps": peer-to-peer Cashu ecash-betalingen die worden afgeleverd als Nostr-events. Een verzender publiceert een P2PK-vergrendelde Cashu-token gericht aan de Nostr-sleutel van de ontvanger, en de ontvanger int deze bij de mint op een geschikt moment. De proofs zelf dragen de waarde, dus een NIP-61-betaling komt aan als een op zichzelf staande token die de ontvanger op eigen tempo kan innen, zonder Lightning-kanaal of interactieve handshake.

## Hoe het werkt

NIP-61 bouwt voort op twee bestaande primitieven: [NIP-60](/nl/topics/nip-60/) Cashu-wallets en de P2PK-vergrendelingen van Cashu. De flow gebruikt drie event-kinds.

**Mint-aanbeveling (kind 10019):** een vervangbaar event dat de ontvanger publiceert om aan te kondigen van welke mints zij nutzaps accepteert en welke Cashu-publieke sleutel wordt gebruikt om proofs voor haar te vergrendelen. Verzenders lezen dit vóór het verzenden, zodat de vergrendelde token er een is die de ontvanger kan innen.

**Nutzap-event (kind 9321):** de betaling zelf. Het bevat de Cashu-proofs (P2PK-vergrendeld op de nutzap-pubkey van de ontvanger uit kind 10019), de mint-URL, optionele `e`- en `a`-tags die de gezapte note identificeren, en een `p`-tag voor de ontvanger. De ontvanger krijgt het via normale Nostr-abonnementen binnen, ontgrendelt de proofs met de bijbehorende private key en houdt ze ofwel in haar NIP-60-wallet ofwel smelt ze om tot Lightning.

**Nutzap-info (kind 7375):** gecachte state met dezelfde vorm als NIP-60-tokenevents, die geïnde nutzap-proofs registreert zodat de wallet ze niet dubbel telt bij een resync.

## Afwegingen en vertrouwensmodel

Een nutzap is een op zichzelf staande ecash-token. Zolang de ontvanger later contact kan opnemen met de mint, kan zij de betaling innen. De mint zelf is de vertrouwde bewaarder, hetzelfde vertrouwensmodel als NIP-60, en die keuze voor custodie is de expliciete prijs voor offline-capabele micropayments met directe finaliteit. NIP-57-zaps vereisen dat de ontvanger een Lightning-node draait (of gehost wordt op een node) met een LNURL-eindpunt dat inkomende HTLC's in realtime accepteert. Telefoons zonder Lightning-kanaal, gebruikers achter firewalls en ontvangers die toevallig offline zijn, vallen allemaal buiten dat model.

De kind 10019-aankondiging is de vertrouwenspoort op sociaal niveau. De verzender kiest een van de door de ontvanger geaccepteerde mints, wat het inningspad van de ontvanger voorspelbaar houdt. Een verzender die een mint buiten de set van de ontvanger kiest, riskeert een niet-inbare token, dus wallets lezen eerst kind 10019.

## Workflow

1. De ontvanger publiceert een kind 10019 die geaccepteerde mints en een nutzap-pubkey aankondigt
2. De verzender leest kind 10019, mint proofs bij een van de vermelde mints en vergrendelt ze P2PK op de nutzap-pubkey van de ontvanger
3. De verzender publiceert een kind 9321 met de vergrendelde proofs, de mint-URL en de doel-tags
4. De ontvanger krijgt de kind 9321 binnen via haar normale Nostr-abonnement
5. De ontvanger ontgrendelt de proofs met haar nutzap-private-key en houdt ze in haar NIP-60-wallet of smelt ze om tot Lightning

## Voorbeeld van een nutzap-event

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1750162800,
  "kind": 9321,
  "tags": [
    ["proof", "{\"amount\":21,\"secret\":\"...\",\"C\":\"...\",\"id\":\"...\"}"],
    ["u", "https://mint.example.com"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3"],
    ["p", "c5d8a4e3b2a1f0e9d8c7b6a5949382716050403020100ffeeddccbbaa99887766"]
  ],
  "content": "Great post!",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

## Implementaties

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) levert nutzap-weergave met balansweergaves per mint als onderdeel van het NIP-60/NIP-61 wallet-oppervlak ([PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075))

---

**Primaire bronnen:**
- [NIP-61 Specificatie](https://github.com/nostr-protocol/nips/blob/master/61.md)
- [Amethyst PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075) - NIP-60 Cashu-wallet en NIP-61 nutzap-ondersteuning

**Genoemd in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/nl/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Zie ook:**
- [NIP-57: Zaps](/nl/topics/nip-57/)
- [NIP-60: Cashu Wallet](/nl/topics/nip-60/)
- [Cashu](/nl/topics/cashu/)
