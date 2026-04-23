---
title: "NIP-65: Relay List Metadata"
date: 2026-01-13
translationOf: /en/topics/nip-65.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Discovery
---

NIP-65 definieert kind 10002-events die aangeven welke relays een gebruiker prefereert voor lezen en schrijven. Deze metadata helpt andere gebruikers en clients je content te vinden over het gedistribueerde relaynetwerk, en maakt het "outbox model" mogelijk dat belasting verdeelt en censuurbestendigheid verbetert.

## Structuur

Een relaylijst is een vervangbaar event (kind 10002) dat `r`-tags bevat voor elke relay die de gebruiker wil adverteren. Het event vervangt elke eerdere relaylijst van dezelfde pubkey.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "sig1234..."
}
```

Elke `r`-tag bevat een relay-WebSocket-URL en een optionele marker die aangeeft hoe de gebruiker met die relay omgaat. De `read`-marker betekent dat de gebruiker events van deze relay leest, dus anderen moeten daar publiceren om de gebruiker te bereiken. De `write`-marker betekent dat de gebruiker naar deze relay publiceert, dus anderen moeten zich daarop abonneren om de content van de gebruiker te zien. Als de marker ontbreekt, betekent dat zowel lezen als schrijven.

Het `content`-veld is leeg voor relaylijstevents.

## Het Outbox Model

NIP-65 maakt een gedecentraliseerd contentdistributiepatroon mogelijk dat het "outbox model" heet. In plaats van dat iedereen publiceert naar en leest van dezelfde centrale relays, publiceren gebruikers naar hun eigen voorkeursrelays en ontdekken clients dynamisch waar ze de content van elke gebruiker kunnen vinden.

Wanneer Alice de posts van Bob wil vinden, haalt haar client eerst Bobs kind 10002-event op van een relay die het heeft. Daarna haalt ze de relays eruit die Bob heeft gemarkeerd voor `write`, omdat hij daar publiceert. Haar client abonneert zich op die relays voor Bobs events. Wanneer Alice Bob een direct message wil sturen, zoekt haar client in plaats daarvan naar zijn `read`-relays en publiceert het bericht daar.

Clients die het outbox model volgen onderhouden verbindingen met relays die staan vermeld in de NIP-65-events van de gebruikers die zij volgen. Naarmate ze nieuwe accounts ontdekken, maken ze dynamisch verbinding met nieuwe relays. Relays die in de lijsten van meerdere gevolgde gebruikers voorkomen krijgen prioriteit, omdat een verbinding daarmee een groter deel van de social graph van de gebruiker bedient.

Deze architectuur verbetert de censuurbestendigheid omdat geen enkele relay ieders content hoeft op te slaan of te serveren. Als een relay offline gaat of een gebruiker blokkeert, blijft diens content beschikbaar op de andere vermelde relays.

## Waarom Het Belangrijk Is

NIP-65 verandert relayselectie van een hardcoded clientdefault in door gebruikers gepubliceerde routingmetadata. Daardoor kunnen clients zich aanpassen aan de werkelijke publicatie- en leesgewoonten van elk account, in plaats van ervan uit te gaan dat iedereen dezelfde set relays gebruikt.

Het verplaatst ook complexiteit naar clients. Om het outbox model goed te gebruiken heeft een client relay-caching, retry-logica en fallbackgedrag nodig wanneer een relaylijst ontbreekt of verouderd is. De spec verbetert discoverability, maar neemt de noodzaak van goede relayselectieheuristieken niet weg.

## Relatie Met Relay Hints

NIP-65 vult de relay hints aan die in andere NIPs voorkomen. Wanneer je iemand tagt met `["p", "pubkey", "wss://hint.relay"]`, vertelt die hint clients waar ze voor die specifieke verwijzing moeten zoeken. NIP-65 biedt de gezaghebbende, door de gebruiker gecontroleerde lijst met voorkeursrelays, terwijl hints snelkoppelingen bieden die in individuele events zijn ingebed voor snellere discovery.

Voor private messaging is NIP-65 niet het hele verhaal. Routing voor publieke content gebruikt kind 10002, maar moderne private messaging-stacks vertrouwen vaak op aparte inboxmetadata zoals relaylijsten uit [NIP-17](/nl/topics/nip-17/), zodat gebruikers DM-routing gescheiden kunnen houden van relays voor publieke posts.

## Best Practices

Houd je relaylijst actueel, want verouderde vermeldingen die naar niet-werkende relays wijzen maken je moeilijker vindbaar. Neem minstens twee of drie relays op voor redundantie, zodat je content via andere relays beschikbaar blijft als er een offline gaat.

Vermijd het opnemen van te veel relays. Wanneer je tien of vijftien relays vermeldt, moet elke client die je content wil ophalen met al die relays verbinden, wat hun ervaring vertraagt en de belasting over het netwerk verhoogt. Een gerichte lijst van drie tot vijf goed gekozen relays werkt beter dan een uitputtende lijst die iedereen die je volgt belast.

Combineer algemene relays met gespecialiseerde relays die je gebruikt. Je kunt bijvoorbeeld een populaire algemene relay opnemen zoals `wss://relay.damus.io`, een relay gericht op je geografische regio, en een relay voor een specifieke community waaraan je deelneemt.

---

**Primaire bronnen:**
- [NIP-65 Specification](https://github.com/nostr-protocol/nips/blob/master/65.md)

**Vermeld in:**
- [Newsletter #5: NIP Deep Dive](/nl/newsletters/2026-01-13-newsletter/)
- [Newsletter #12: Outbox Model Benchmarks](/nl/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: Wisp inbox-relay broadcasting](/en/newsletters/2026-04-22-newsletter/)

**Zie ook:**
- [NIP-11: Relay Information](/nl/topics/nip-11/)
- [NIP-17: Private Direct Messages](/nl/topics/nip-17/)
