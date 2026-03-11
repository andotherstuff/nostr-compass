---
title: "NIP-70: Beschermde events"
date: 2026-03-11
translationOf: /en/topics/nip-70.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Relay
  - Access Control
---

NIP-70 definieert een manier waarop auteurs een event als protected kunnen markeren met de eenvoudige tag `[["-"]]`. Een protected event kan alleen worden geaccepteerd wanneer een relay ervoor kiest dat gedrag te ondersteunen en controleert dat de geauthenticeerde publisher dezelfde pubkey heeft als de auteur van het event.

## Hoe het werkt

De kernregel is kort. Als een event de tag `[["-"]]` bevat, moet een relay het standaard weigeren. Een relay die protected events wil ondersteunen, moet eerst de [NIP-42](/nl/topics/nip-42/) `AUTH`-flow uitvoeren en bevestigen dat de client die zich heeft geauthenticeerd zijn eigen event publiceert.

Dat maakt NIP-70 een regel voor publicatie-autoriteit, niet voor encryptie. De inhoud kan nog steeds leesbaar zijn. Wat verandert, is wie dat event op een relay mag plaatsen die de tag respecteert. Daardoor kunnen relays semi-gesloten feeds en andere contexten ondersteunen waarin auteurs willen dat een relay republicatie door derden weigert.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

## Gevolgen van de AUTH-flow

Protected events zijn alleen nuttig wanneer relays de identiteit van de auteur echt afdwingen op het moment van publiceren. Daarom hangt NIP-70 zo direct af van [NIP-42](/nl/topics/nip-42/). Een relay die `[["-"]]`-events accepteert zonder een passende auth-check, behandelt de tag als decoratie en niet als beleid.

## Relaygedrag en grenzen

NIP-70 belooft niet dat inhoud voor altijd ingeperkt blijft. Elke ontvanger kan nog steeds kopieren wat hij ziet en elders als nieuw event publiceren. De specificatie geeft relays alleen een gestandaardiseerde manier om de intentie van de auteur te respecteren en directe republicatie van protected events te weigeren.

Daarom is vervolgwerk belangrijk. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) breidt de regel uit naar reposts die protected events insluiten, en sluit zo een eenvoudige omweg waarbij het oorspronkelijke event protected bleef maar het wrapper-event niet.

## Implementaties

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - voegt NIP-42-auth-ondersteuning toe voor protected events
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - weigert reposts die protected events insluiten
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - voegt helper-ondersteuning toe gekoppeld aan protected-event-afhandeling

---

**Primaire bronnen:**
- [NIP-70 Specification](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - voegde NIP-70 toe aan het NIPs-repository
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - weigert reposts die protected events insluiten
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - relay-implementatie voor NIP-42-auth en protected events

**Vermeld in:**
- [Nieuwsbrief #13: NIP Updates](/nl/newsletters/2026-03-11-newsletter/#nip-updates)
- [Nieuwsbrief #13: NIP Deep Dive](/nl/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-70-protected-events)

**Zie ook:**
- [NIP-42: Client Authentication](/nl/topics/nip-42/)
- [NIP-11: Relay Information Document](/nl/topics/nip-11/)
