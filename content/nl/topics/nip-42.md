---
title: "NIP-42: Authentication of clients to relays"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42 definieert hoe clients zich authenticeren bij relays. Relays kunnen authenticatie vereisen om toegangscontrole af te dwingen, misbruik te voorkomen of betaalde relay-diensten aan te bieden.

## Hoe Het Werkt

De authenticatiestroom begint wanneer een relay een `AUTH`-bericht naar de client stuurt. Dat bericht bevat een challenge-string die de client moet ondertekenen. De client maakt een kind 22242 authentication event aan met de challenge en ondertekent dat met zijn private key. De relay verifieert de handtekening en de challenge, en verleent daarna toegang.

```json
{
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com"],
    ["challenge", "random-challenge-string"]
  ],
  "content": "",
  "pubkey": "<client_pubkey>",
  "created_at": 1736784000,
  "sig": "<signature>"
}
```

De challenge voorkomt replay-aanvallen. De relay-URL in de tags voorkomt dat hetzelfde ondertekende event opnieuw kan worden gebruikt bij andere relays.

## Protocol Notes

Authenticatie is connection-scoped. Een challenge blijft geldig voor de duur van de verbinding, of totdat de relay een nieuwe stuurt. Het ondertekende event is ephemeral en mag niet als normaal event worden uitgezonden.

De specificatie definieert ook machine-readable foutprefixen. `auth-required:` betekent dat de client nog niet is geauthenticeerd. `restricted:` betekent dat de client zich wel heeft geauthenticeerd, maar dat die pubkey nog steeds geen toestemming heeft voor de gevraagde actie.

## Use Cases

Betaalde relays gebruiken NIP-42 om abonnees te verifiëren voordat ze toegang geven. Privé-relays gebruiken het om lees- of schrijfrechten te beperken tot goedgekeurde pubkeys. Het verbetert ook rate limiting, omdat relays gedrag per geauthenticeerde key kunnen volgen in plaats van per IP-adres.

Gecombineerd met [NIP-11](/nl/topics/nip-11/) metadata kunnen clients ontdekken of een relay NIP-42 ondersteunt voordat ze protected queries proberen. In de praktijk is ondersteuning nog ongelijk verdeeld, dus clients hebben een fallback-pad nodig wanneer een relay NIP-42 adverteert maar protected events verkeerd afhandelt.

---

**Primaire bronnen:**
- [NIP-42 Specification](https://github.com/nostr-protocol/nips/blob/master/42.md) - Authentication of clients to relays

**Vermeld in:**
- [Newsletter #6: Relay Information Documents](/nl/newsletters/2026-01-21-newsletter/)
- [Newsletter #9: Marmot Relay Status Testing](/nl/newsletters/2026-02-11-newsletter/)
- [Newsletter #10: Nostr MCP Server](/nl/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Relay AUTH Starts Reaching Real Apps](/en/newsletters/2026-03-11-newsletter/)

**Zie ook:**
- [NIP-11: Relay Information Document](/nl/topics/nip-11/)
- [NIP-50: Search Capability](/nl/topics/nip-50/)
