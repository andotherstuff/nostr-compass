---
title: "NIP-02: Volglijst"
date: 2025-12-24
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Sociaal
---

NIP-02 definieert kind 3 events, die de volglijst van een gebruiker opslaan. Dit event is de basisinput voor home feeds, reply-meldingen en veel relay-selectiestrategieen.

## Hoe het werkt

Een kind 3 event bevat `p` tags die gevolgde pubkeys opsommen:

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Elke `p` tag heeft vier posities: de tagnaam, de gevolgde pubkey (hex), een optionele relay URL-hint en een optionele "petname" (een lokale bijnaam). De relay-hint vertelt andere clients waar ze de events van die gebruiker kunnen vinden. Met de petname kun je herkenbare namen toewijzen aan contacten zonder te vertrouwen op hun zelfgekozen display names.

## Vervangbaar gedrag

Kind 3 valt binnen het vervangbare bereik (0, 3, 10000-19999), dus relays bewaren alleen de nieuwste versie per pubkey. Wanneer je iemand nieuw volgt, publiceert je client een volledig nieuw kind 3 met al je follows plus de nieuwe. Dat betekent dat volglijsten elke keer volledig moeten zijn; je kunt geen incrementele updates publiceren.

## Waarom het belangrijk is

Om een home feed op te bouwen, haalt een client de kind 3 van de gebruiker op, extraheert alle pubkeys uit de `p` tags en abonneert zich daarna op kind 1 events van die auteurs:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

De relay retourneert overeenkomende notes, en de client rendert die. De relay-hints in kind 3 helpen clients bepalen welke relays ze voor elke gevolgde gebruiker moeten bevragen.

Dit event is ook de plek waar verouderde sociale staat het eerst zichtbaar wordt. Als de nieuwste kind 3 van een gebruiker ontbreekt op de relays die je bevraagt, kan hun feed leeg lijken ook al bestaan hun follows elders nog steeds. Clients die resultaten van meerdere relays samenvoegen herstellen meestal beter dan clients die op een enkele relay vertrouwen.

## Petnames en identiteit

Het petname-veld maakt een gedecentraliseerd naamgevingsschema mogelijk. In plaats van te vertrouwen op welke naam een gebruiker in het profiel claimt, kun je je eigen label toewijzen. Een client kan bijvoorbeeld "alice (Mijn zus)" tonen, waarbij "alice" uit haar kind 0-profiel komt en "Mijn zus" jouw petname is. Dat geeft context die globale gebruikersnamen niet kunnen bieden.

## Interop-opmerkingen

Omdat kind 3 events vervangbaar zijn en volledig moeten zijn, moeten clients onbekende tags behouden bij updates. Als een andere client tags heeft toegevoegd die jouw client niet begrijpt, gaat die data verloren als je blind overschrijft.

Dezelfde voorzichtigheid geldt voor relay-hints en petnames. Het zijn optionele velden, maar ze laten vallen bij het schrijven kan de ervaring in een andere client stilletjes slechter maken. Een veilige updateflow is: laad de nieuwste bekende kind 3, wijzig alleen de tags die je begrijpt, behoud de rest en publiceer daarna het volledige event opnieuw.

---

**Primaire bronnen:**
- [NIP-02-specificatie](https://github.com/nostr-protocol/nips/blob/master/02.md)

**Vermeld in:**
- [Nieuwsbrief #2: NIP Deep Dive](/en/newsletters/2025-12-24-newsletter/#nip-02-follow-list)

**Zie ook:**
- [NIP-01: Basic Protocol](/nl/topics/nip-01/)
- [NIP-10: Text Note Threading](/nl/topics/nip-10/)
- [NIP-65: Relay List Metadata](/nl/topics/nip-65/)
