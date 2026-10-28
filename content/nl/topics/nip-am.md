---
title: 'Buzz-concept NIP-AM: metrics per agentbeurt'
date: 2026-10-28
translationOf: /en/topics/nip-am.md
translationDate: 2026-10-28
draft: false
---

**Status:** Dit is een conceptvoorstel dat specifiek voor het Buzz-project geldt. NIP-AM is geen geaccepteerde officiële NIP. Het label komt uit de projectdocumentatie van Buzz, en de officiële NIPs-repository heeft het niet toegekend of goedgekeurd.

## Doel

NIP-AM legt het gebruik vast van elke voltooide beurt van een AI-agent. Per beurt publiceert de agent één `kind:44200` event, dat volgens de Buzz-conventie als een regulier append-only event geldt. De content is met NIP-44 versleuteld van agent naar eigenaar. Daarin staan cijfers over tokengebruik samen met correlatie-ID's, en eventuele kostenwaarden zijn schattingen. Een transcript van het gesprek bevat het niet.

## Beperkingen

Publieke tags identificeren de eigenaar en de agent, en relays kunnen nog steeds zien wanneer events worden gepubliceerd. Het formaat verbergt dus niet dat er activiteit heeft plaatsgevonden. Ontbreekt een gebruikswaarde, dan betekent dat onbekend, en zo'n waarde mag nooit als nul worden geteld.

## Voorstel voor gedelegeerde lezers

Een openstaande documentatie-pull request, #8582, stelt een least-privilege-machtiging voor die door de eigenaar is ondertekend. Daarbij zou de agent voor elke actieve lezer een afzonderlijke versleutelde kopie publiceren, elk gekoppeld aan het exacte event-ID van de machtiging. Aan de autorisatie tijdens runtime verandert de pull request niets. De voorgestelde kind `30180` voor de machtiging en het maximumaantal lezers zijn nog open vragen, en ook het intrekkingsbeleid ligt nog niet vast. Intrekking zou de relaygeschiedenis en toekomstige leesacties kunnen beperken. Kopieën die een lezer al heeft ontvangen, kan ze niet wissen.

## Primaire bronnen

- [Buzz NIP-AM-concept: Agent Turn Metrics (vastgepinde revisie)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-AM.md)
- [Buzz-pull request #8582: gedelegeerde lezers van metrics (open concept)](https://github.com/block/buzz/pull/8582)

## Zie ook

- [NIP-44](/nl/topics/nip-44/)

**Vermeld in:**

- [Nieuwsbrief #46: concepttekst van NIP-AM voor gedelegeerde lezers van metrics](/nl/newsletters/2026-10-28-newsletter/#draft-nip-am-text-for-delegated-metric-readers)
- [Nieuwsbrief #46: Buzz](/nl/newsletters/2026-10-28-newsletter/#buzz)
