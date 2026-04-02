---
title: "NIP-70: Protected Events"
date: 2026-03-11
translationOf: /en/topics/nip-70.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Relay
  - Access Control
---

NIP-70 definieert een manier voor auteurs om een event als beschermd te markeren met de simpele tag `[["-"]]`. Een beschermd event kan alleen worden geaccepteerd wanneer een relay ervoor kiest dit gedrag te ondersteunen en verifieert dat de geauthenticeerde publisher dezelfde pubkey is als de eventauteur.

## Hoe Het Werkt

De kernregel is kort. Als een event de `[["-"]]` tag bevat, moet een relay het standaard weigeren. Een relay die beschermde events wil ondersteunen, moet eerst de [NIP-42](/nl/topics/nip-42/) `AUTH`-flow uitvoeren en bevestigen dat de client die zich heeft geauthenticeerd zijn eigen event publiceert.

Dat maakt NIP-70 een publicatieautoriteitsregel, geen versleutelingsregel. De inhoud kan nog steeds leesbaar zijn. Wat verandert is wie dat event op een relay mag plaatsen die de tag respecteert. Dit stelt relays in staat semi-gesloten feeds en andere contexten te ondersteunen waarin auteurs willen dat een relay herpublicatie door derden weigert.

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

## AUTH-flowimplicaties

Beschermde events zijn alleen nuttig wanneer relays daadwerkelijk auteuridentiteit afdwingen bij publicatie. Daarom is NIP-70 zo direct afhankelijk van [NIP-42](/nl/topics/nip-42/). Een relay die `[["-"]]` events accepteert zonder een overeenkomende auth-controle behandelt de tag als decoratie, niet als beleid.

## Relaygedrag en Beperkingen

NIP-70 belooft niet dat inhoud voor altijd ingesloten blijft. Elke ontvanger kan nog steeds kopiëren wat hij ziet en een nieuw event elders publiceren. De specificatie geeft relays alleen een standaardmanier om de intentie van de auteur te respecteren en directe herpublicatie van beschermde events te weigeren.

Daarom is vervolgwerk belangrijk. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) breidt de regel uit naar reposts die beschermde events insluiten, waarmee een eenvoudige omzeiling wordt gesloten waarbij het oorspronkelijke event beschermd bleef maar het wrapper-event niet.

## Implementaties

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - NIP-42 auth-ondersteuning voor beschermde events toegevoegd
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - Weigert reposts die beschermde events insluiten
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - Helperondersteuning gekoppeld aan beschermde-eventafhandeling

---

**Primaire bronnen:**
- [NIP-70 Specificatie](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - NIP-70 toegevoegd aan het NIPs-repository
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - Reposts die beschermde events insluiten weigeren
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Relay-implementatie voor NIP-42 auth en beschermde events

**Vermeld in:**
- [Newsletter #13: NIP Updates](/en/newsletters/2026-03-11-newsletter/#nip-updates)
- [Newsletter #13: NIP Deep Dive](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-70-protected-events)

**Zie ook:**
- [NIP-42: Client Authentication](/nl/topics/nip-42/)
- [NIP-11: Relay Information Document](/nl/topics/nip-11/)
