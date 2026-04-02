---
title: "NIP-86: Relay Management API"
date: 2026-04-01
translationOf: /en/topics/nip-86.md
translationDate: 2026-04-01
draft: false
categories:
  - Relays
  - Protocol
---

NIP-86 definieert een JSON-RPC-interface voor relaybeheer, waarmee geautoriseerde clients administratieve commando's naar relays kunnen sturen via een gestandaardiseerde API. Relayoperators kunnen pubkeys bannen of toestaan, toegangslijsten beheren en relaystatus opvragen zonder relay-specifieke tooling.

## Hoe Het Werkt

De beheer-API gebruikt JSON-RPC-achtige verzoeken over HTTP op dezelfde URI als het relay WebSocket-eindpunt. Verzoeken gebruiken het `application/nostr+json+rpc` contenttype en authenticeren met een [NIP-98](/nl/topics/nip-98/) (HTTP Auth) ondertekend event in de `Authorization` header. De relay verifieert de verzoekende pubkey tegen zijn adminlijst voordat commando's worden uitgevoerd.

Beschikbare methoden omvatten het bannen en toestaan van pubkeys, het opvragen van gebande gebruikers en het bevragen van relayconfiguratie. De gestandaardiseerde interface betekent dat één enkele clientimplementatie elke NIP-86-compatibele relay kan beheren.

## Implementaties

- [Amethyst](https://github.com/vitorpamplona/amethyst) - Android-client met NIP-86 relaybeheer-UI (v1.07.0+)

---

**Primaire bronnen:**
- [NIP-86 Specificatie](https://github.com/nostr-protocol/nips/blob/master/86.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - Client-side NIP-86 ondersteuning
- [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) - Relaybeheer gebruikerzoekdialoog

**Vermeld in:**
- [Newsletter #16: Amethyst levert relaybeheer](/nl/newsletters/2026-04-01-newsletter/#amethyst-ships-pinned-notes-relay-management-and-request-to-vanish)

**Zie ook:**
- [NIP-11: Relay Information Document](/nl/topics/nip-11/)
- [NIP-98: HTTP Auth](/nl/topics/nip-98/)
- [NIP-42: Authentication of Clients to Relays](/nl/topics/nip-42/)
