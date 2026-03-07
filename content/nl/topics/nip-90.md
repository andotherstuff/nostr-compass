---
title: "NIP-90: Data Vending Machines"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - DVM
---

NIP-90 definieert Data Vending Machines (DVMs), een protocol voor het aanvragen en leveren van betaald rekenwerk via Nostr.

## Hoe het werkt

Klanten publiceren job request-events in de `5000-5999`-reeks. Elke aanvraag kan een of meer `i`-tags voor input bevatten, `param`-tags voor jobspecifieke instellingen, een `output`-tag voor het verwachte formaat, een `bid`-plafond en relay-hints voor waar antwoorden moeten verschijnen. Serviceproviders antwoorden met een bijpassende result kind in de `6000-6999`-reeks, altijd `1000` hoger dan de request kind.

Resultaten bevatten de oorspronkelijke aanvraag, de pubkey van de klant en optioneel een `amount`-tag of invoice. Providers kunnen ook kind `7000` feedback-events sturen zoals `payment-required`, `processing`, `partial`, `error` of `success`, waardoor clients voortgang kunnen tonen voordat het definitieve resultaat arriveert.

## Betaling en privacy

Het protocol laat de businesslogica bewust open. Een provider kan om betaling vragen voordat het werk begint, nadat een sample is teruggestuurd of nadat het volledige resultaat is geleverd. Die flexibiliteit is nodig omdat DVM-jobs uiteenlopen van goedkope teksttransformaties tot dure GPU-taken, en providers niet allemaal hetzelfde betalingsrisico accepteren.

Als een klant private input wil gebruiken, kan de aanvraag `i`- en `param`-data naar versleutelde `content` verplaatsen en het event markeren met een `encrypted`-tag plus de `p`-tag van de provider. Dat beschermt prompts of bronmateriaal tegen relay-observers, maar het betekent ook dat de klant zich op een specifieke provider moet richten in plaats van een open marktaanvraag uit te zenden.

## Interop-notities

NIP-90 ondersteunt job chaining via `i`-tags met inputtype `job`, zodat een resultaat als input kan dienen voor een latere aanvraag. Daarmee worden meerstapsflows mogelijk zonder een aparte orchestration-laag te verzinnen.

Provider discovery valt buiten de request/response-lus zelf. De specificatie verwijst naar aankondigingen uit [NIP-89: Aanbevolen applicatiehandlers](/nl/topics/nip-89/) voor het adverteren van ondersteunde job kinds, zodat clients vendors kunnen vinden voordat ze een aanvraag publiceren.

---

**Primaire bronnen:**
- [NIP-90-specificatie](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Vermeld in:**
- [Newsletter #11: NIP-AC DVM Agent Coordination](/nl/newsletters/2026-02-25-newsletter/#nip-updates)

**Zie ook:**
- [NIP-89: Aanbevolen applicatiehandlers](/nl/topics/nip-89/)
