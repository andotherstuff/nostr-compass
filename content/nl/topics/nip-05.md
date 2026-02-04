---
title: "NIP-05 (Domeinverificatie)"
date: 2026-02-04
description: "NIP-05 maakt menselijk leesbare identifiers mogelijk voor Nostr pubkeys via domeinverificatie."
---

NIP-05 koppelt Nostr publieke sleutels aan menselijk leesbare internet-identifiers zoals `user@example.com`. Dit biedt een manier om identiteit te verifieren via domeineigendom zonder vertrouwen in een centrale autoriteit.

## Hoe Het Werkt

Een gebruiker claimt een identifier door een `nip05` veld toe te voegen aan zijn profielmetadata. De identifier volgt het formaat `naam@domein`. Clients verifieren de claim door `https://domein/.well-known/nostr.json` op te halen en te controleren of de naam is gekoppeld aan de pubkey van de gebruiker.

Het JSON-bestand op het well-known pad bevat een `names` object dat lokale namen koppelt aan hex pubkeys:

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

Wanneer verificatie slaagt, kunnen clients de identifier tonen in plaats van of naast de npub. Sommige clients tonen een vinkje of andere indicator voor geverifieerde identifiers.

## Relay Hints

Het `nostr.json` bestand kan optioneel een `relays` object bevatten dat pubkeys koppelt aan arrays van relay-URL's. Dit helpt clients te ontdekken waar events van een bepaalde gebruiker te vinden zijn.

## Implementaties

De meeste grote clients ondersteunen NIP-05 verificatie:
- Damus, Amethyst, Primal tonen geverifieerde identifiers
- Veel relay-diensten bieden NIP-05 identifiers als feature
- Er bestaan talrijke gratis en betaalde NIP-05 providers

## Primaire Bronnen

- [NIP-05 Specificatie](https://github.com/nostr-protocol/nips/blob/master/05.md)

## Vermeld In

- [Nieuwsbrief #8 (2026-02-04)](/nl/newsletters/2026-02-04-newsletter/) - PR die lowercase vereist voor hex keys en namen
