---
title: "NIP-CD: slash-commando's"
date: 2026-10-28
translationOf: /en/topics/nip-cd.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-CD definieert slash-commando's. Een dienst publiceert een commando, en iedereen kan het als platte tekst aanroepen in de content van elk willekeurig Nostr-event. NIP-CD is een optionele conceptspecificatie. Na een eerder voorstel werd NIP-CD op 21 oktober 2026 samengevoegd onder de titel Commands, en de titel werd gewijzigd in Slash Commands toen op 27 oktober 2026 optionele lijsten met geïnstalleerde commando's werden samengevoegd.

## Hoe het werkt

Een event van kind 31992 definieert een commando. Verplichte tags geven het triggerwoord zonder slash, een titel en een beschrijving van het gebruik. Geordende `arg` tags declareren positionele argumenten, met types zoals pubkey, event, relay, number, enum of text. Met `s` tags wordt beperkt welke events het commando activeren, op basis van kind, relay, auteur of tag. Deze scopes werken als een filter: waarden van hetzelfde type zijn alternatieven, en elk type dat aanwezig is, moet overeenkomen.

Een aanroep is tekst die begint op index 0 van de content van een event, zoals `/ban` gevolgd door argumenten, en bevat geen tags. Door een kwalificatie van de vorm `@nostr:npub1...` toe te voegen, richt je de aanroep op één enkele executor. Zonder kwalificatie kan elk commando reageren waarvan de trigger overeenkomt en waarvan de scope het event omvat, zodat één bericht meerdere diensten kan activeren.

Ondersteuning door clients is optioneel. Clients mogen autocomplete, argumentkiezers en gerenderde chips aanbieden. Hun eigen ondersteuning mogen ze niet als voorwaarde stellen voordat ze een aanroep versturen, en tekst die niet geparsed kan worden, moeten ze als gewone content versturen.

Voor relaygebaseerde groepen gaan definities en aanroepen naar de grouprelay. Bij broadcastgebruik gaan definities naar de outboxes van executors en aanroepen naar de inboxes van executors.

## Lijsten met geïnstalleerde commando's

Een gebruiker kan een optionele lijst van kind 10992 bijhouden, volgens NIP-51, met `a` tags die via de pubkey van de executor en de `d` waarde verwijzen naar commandodefinities van kind 31992, met een optionele relayhint. Clients zouden de lijst moeten gebruiken voor autocomplete en gerenderde chips. Wat de lijst vastlegt, is de voorkeur van een gebruiker voor weergave en ontdekking. Ze machtigt geen executor, en aanroepen in platte tekst werken ook zonder de lijst. Dit deel van de specificatie werd op 27 oktober 2026 samengevoegd via PR #2525. Uit de merge blijkt niet welke clients de lijst hebben geïmplementeerd.

## Primaire bronnen

- [NIP-CD-specificatie](https://github.com/nostr-protocol/nips/blob/master/CD.md)
- [Merge van NIP-CD op 21 oktober 2026](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4)
- [PR #2525 voor lijsten met geïnstalleerde commando's, samengevoegd op 27 oktober 2026](https://github.com/nostr-protocol/nips/pull/2525)
- [Commit van 26 oktober 2026 uit PR #2525, vóór de merge gemaakt op de branch van die PR](https://github.com/nostr-protocol/nips/commit/0142de0384210d69074c089448ef5bc303faef37)
- [Merge van lijsten met geïnstalleerde commando's in NIP-CD op 27 oktober 2026](https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157)

## Vermeld in
- [Nieuwsbrief #46: NIP-CD definieert commando's die als platte tekst worden aangeroepen](/nl/newsletters/2026-10-28-newsletter/#nip-cd-defines-commands-invoked-as-plain-text) Nieuwsbrieven

- [Nieuwsbrief #46: NIP-CD voegt optionele lijsten met geïnstalleerde commando's toe](/nl/newsletters/2026-10-28-newsletter/#nip-cd-adds-optional-installed-command-lists) Nieuwsbrieven

- [Nieuwsbrief #46 (2026-10-28): oktober 2026, gedeelde betekenissen van queries en diensten die door tekst worden geactiveerd](/nl/newsletters/2026-10-28-newsletter/#october-2026-shared-query-meanings-and-text-triggered-services)

## Zie ook

- [NIP-01: basisprotocol](/nl/topics/nip-01/)
