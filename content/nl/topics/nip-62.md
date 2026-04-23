---
title: "NIP-62: Vanish Requests"
date: 2026-01-13
translationOf: /en/topics/nip-62.md
translationDate: 2026-04-22
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62 definieert vanish requests, kind `62`-events die specifieke relays vragen om alle events van de verzoekende pubkey te verwijderen. Het verzoek is standaard relay-targeted en kan ook als globaal verzoek worden uitgezonden met de speciale `ALL_RELAYS`-tagwaarde.

## Hoe Het Werkt

Een vanish request is een kind `62`-event dat is ondertekend door de pubkey die zijn geschiedenis verwijderd wil hebben. De taglijst moet minstens één `relay`-waarde bevatten die de relay benoemt die op het verzoek moet reageren.

```json
{
  "id": "a7b8c9d0e1f23456789012345678901234567890abcdef1234567890abcdef12",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1743465600,
  "kind": 62,
  "tags": [
    ["relay", "wss://relay.example.com"]
  ],
  "content": "Requesting deletion of all events from this relay.",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

Het veld `content` kan een reden of juridische kennisgeving aan de relay-operator bevatten. Clients moeten het event rechtstreeks naar de doelrelays sturen in plaats van het breed te publiceren, tenzij de gebruiker expliciet een netwerkbreed vanish request wil.

## Relaygedrag

Relays die een vanish request zien en hun eigen service-URL in een `relay`-tag terugvinden, moeten alle events van die pubkey tot en met de `created_at` van het verzoek volledig verwijderen. De specificatie zegt ook dat relays [NIP-59](/nl/topics/nip-59/) (Gift Wrap)-events moeten verwijderen die de verdwenen pubkey met een `p`-tag noemden, zodat inkomende DMs samen met de eigen events van de gebruiker verdwijnen.

De relay moet er ook voor zorgen dat die verwijderde events niet opnieuw in de relay kunnen worden gerebroadcast. Het ondertekende vanish request zelf mag voor bookkeeping bewaard blijven.

## Global Requests

Om verwijdering op elke relay aan te vragen die het event ziet, wordt de tagwaarde `ALL_RELAYS` in hoofdletters:

```json
{
  "kind": 62,
  "pubkey": "<32-byte-hex-pubkey>",
  "tags": [
    ["relay", "ALL_RELAYS"]
  ],
  "content": "Global vanish request"
}
```

Clients moeten deze vorm naar zo veel mogelijk relays uitzenden.

## Waarom Het Belangrijk Is

NIP-62 geeft clients en relay-operators een gedeeld verwijderingssignaal dat verder gaat dan ad-hoc moderatie-API's of relay-specifieke dashboards. Een gebruiker kan een enkel ondertekend verzoek publiceren en vervolgens elke relay zelf laten beslissen hoe die het verwerkt.

Het gaat ook verder dan [NIP-09](/nl/topics/nip-09/). NIP-09 verwijdert individuele events en relays kunnen daaraan voldoen. NIP-62 vraagt getagde relays om alles van de pubkey te verwijderen en te voorkomen dat die events opnieuw worden geïmporteerd.

## Implementaties

- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - Client-side vanish request support
- [rust-nostr PR #1315](https://github.com/rust-nostr/nostr/pull/1315) - Memory backend support
- [rust-nostr PR #1316](https://github.com/rust-nostr/nostr/pull/1316) - LMDB backend support
- [rust-nostr PR #1317](https://github.com/rust-nostr/nostr/pull/1317) - SQLite backend support
- [rust-nostr PR #1318](https://github.com/rust-nostr/nostr/pull/1318) - Database test coverage for relay-specific vanish support
- [nostream PR #544](https://github.com/Cameri/nostream/pull/544) - Added NIP-62 right-to-vanish to the advertised feature list

---

**Primaire bronnen:**
- [NIP-62 Specification](https://github.com/nostr-protocol/nips/blob/master/62.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - Client-side vanish support
- [rust-nostr PR #1315](https://github.com/rust-nostr/nostr/pull/1315)
- [rust-nostr PR #1316](https://github.com/rust-nostr/nostr/pull/1316)
- [rust-nostr PR #1317](https://github.com/rust-nostr/nostr/pull/1317)
- [rust-nostr PR #1318](https://github.com/rust-nostr/nostr/pull/1318)
- [nostream PR #544](https://github.com/Cameri/nostream/pull/544)

**Vermeld in:**
- [Newsletter #5: Notable Code Changes](/nl/newsletters/2026-01-13-newsletter/)
- [Newsletter #12: rust-nostr](/nl/newsletters/2026-03-04-newsletter/)
- [Newsletter #16: Amethyst ships NIP-62 support](/nl/newsletters/2026-04-01-newsletter/)
- [Newsletter #16: NIP Deep Dive](/nl/newsletters/2026-04-01-newsletter/)
- [Newsletter #19: nostream NIP-62 support](/en/newsletters/2026-04-22-newsletter/)

**Zie ook:**
- [NIP-09: Event Deletion Request](/nl/topics/nip-09/)
- [NIP-17: Private Direct Messages](/nl/topics/nip-17/)
- [NIP-59: Gift Wrap](/nl/topics/nip-59/)
