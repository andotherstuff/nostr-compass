---
title: "NIP-65: Relay Lijst Metadata"
date: 2026-01-13
draft: false
categories:
  - Protocol
  - Discovery
---

NIP-65 definieert kind 10002 events die adverteren welke relays een gebruiker prefereert voor lezen en schrijven. Deze metadata helpt andere gebruikers en clients je content te lokaliseren over het gedistribueerde relay netwerk, wat het "outbox model" mogelijk maakt dat de belasting verdeelt en censuurbestendigheid verbetert.

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

Elke `r`-tag bevat een relay-WebSocket-URL en een optionele marker die aangeeft hoe de gebruiker met die relay interacteert. De `read`-marker betekent dat de gebruiker events van deze relay consumeert, dus anderen moeten daar publiceren om de gebruiker te bereiken. De `write`-marker betekent dat de gebruiker naar deze relay publiceert, dus anderen moeten zich daar abonneren om de content van de gebruiker te zien. Het weglaten van de marker betekent zowel lezen als schrijven.

Het `content`-veld is leeg voor relaylijst-events.

## Het Outbox Model

NIP-65 maakt een gedecentraliseerd contentdistributiepatroon mogelijk genaamd het "outbox-model." In plaats van dat iedereen publiceert naar en leest van dezelfde centrale relays, publiceren gebruikers naar hun eigen geprefereerde relays en ontdekken clients dynamisch waar ze de content van elke gebruiker kunnen vinden.

Wanneer Alice Bob's berichten wil vinden, haalt haar client eerst Bob's kind 10002 event op van elke relay die het heeft. Ze extraheert dan de relays die Bob heeft gemarkeerd voor `write` aangezien dat is waar hij publiceert. Haar client abonneert zich op die relays voor Bob's events. Wanneer Alice Bob een direct bericht wil sturen, zoekt haar client in plaats daarvan naar zijn `read` relays en publiceert het bericht daar.

Clients die het outbox-model volgen onderhouden verbindingen met relays vermeld in de NIP-65-events van hun gevolgde gebruikers. Naarmate ze nieuwe accounts ontdekken, verbinden ze dynamisch met nieuwe relays. Relays die in meerdere lijsten van gevolgde gebruikers voorkomen krijgen prioriteit aangezien verbinden met hen meer van de sociale grafiek van de gebruiker bedient.

Deze architectuur verbetert censuurbestendigheid omdat geen enkele relay ieders content hoeft op te slaan of te serveren. Als één relay offline gaat of een gebruiker blokkeert, blijft hun content beschikbaar op hun andere vermelde relays.

## Relatie met Relay Hints

NIP-65 complementeert de relay-hints die door andere NIP's heen te vinden zijn. Wanneer je iemand tagt met `["p", "pubkey", "wss://hint.relay"]`, vertelt de hint clients waar ze moeten zoeken naar die specifieke verwijzing. NIP-65 biedt de gezaghebbende, door de gebruiker beheerde lijst van geprefereerde relays, terwijl hints snelkoppelingen bieden ingebed in individuele events voor snellere ontdekking.

## Best Practices

Houd je relaylijst actueel aangezien verouderde vermeldingen die naar niet-functionerende relays wijzen je moeilijker vindbaar maken. Neem ten minste twee of drie relays op voor redundantie zodat als een relay offline gaat, je content toegankelijk blijft via de anderen.

Vermijd het vermelden van te veel relays. Wanneer je tien of vijftien relays vermeldt, moet elke client die je content wil ophalen met allemaal verbinden, wat hun ervaring vertraagt en de belasting over het netwerk verhoogt. Een gefocuste lijst van drie tot vijf goed gekozen relays dient je beter dan een uitputtende lijst die iedereen die je volgt belast.

Meng algemene relays met gespecialiseerde relays die je gebruikt. Bijvoorbeeld, je zou een populaire algemene relay kunnen vermelden zoals `wss://relay.damus.io`, een relay gericht op je geografische regio, en een relay voor een specifieke gemeenschap waar je aan deelneemt.

---

**Primaire bronnen:**
- [NIP-65 Specificatie](https://github.com/nostr-protocol/nips/blob/master/65.md)

**Vermeld in:**
- [Nieuwsbrief #5: NIP Diepgaand](/nl/newsletters/2026-01-13-newsletter/#nip-65-relay-list-metadata)

**Zie ook:**
- [NIP-11: Relay-informatie](/nl/topics/nip-11/)
