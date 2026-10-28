---
title: 'Buzz-concept NIP-RS: synchronisatie van leesstatus tussen apparaten'
date: 2026-10-28
translationOf: /en/topics/nip-rs.md
translationDate: 2026-10-28
draft: false
---

**Status:** Dit is een conceptvoorstel dat specifiek is voor het Buzz-project. NIP-RS is geen geaccepteerde officiële NIP. Het label komt uit de projectdocumentatie van Buzz, en de officiële NIPs-repository heeft het niet toegekend of goedgekeurd.

## Doel

Met NIP-RS kunnen de apparaten van één gebruiker met elkaar delen tot waar die gebruiker heeft gelezen. Elke installatie publiceert een adresseerbaar event `kind:30078`. De tag `d` daarvan bestaat uit `read-state:` gevolgd door een willekeurige slot-ID, en de inhoud is met NIP-44 versleuteld naar de eigen sleutel van de gebruiker. In de plaintext worden context-ID's gekoppeld aan tijdstempelgrenzen (frontiers), die elk betekenen dat alles op of vóór dat tijdstip gelezen is. Het concept publiceert geen leesbevestigingen en onthult niet wat andere mensen hebben gelezen.

## Beperkingen

Frontiers zijn hints naar beste vermogen over recente activiteit. Een volledige geschiedenis van gelezen berichten vormen ze niet. Overrides voor handmatig als ongelezen markeren, inclusief tombstone-ondergrenzen, volgen een apart duurzaam contract. Het laden van de volledige override-status hangt af van het gedrag van relays op het gebied van volgorde en capaciteit, en dat kan een client niet volledig verifiëren; een willekeurige relay geeft dus mogelijk geen volledige ongelezen-status terug. Context-ID's hebben grotendeels alleen betekenis binnen één familie van clients.

Een openstaande pull request, #8639, stelt voor om Buzz-clients over te zetten op een NIP-11-capability `buzz_v1`, ondersteund door een private, geauthenticeerde HTTP-API die standaard uitgeschakeld is. Relays zonder die capability zouden bij NIP-RS blijven.

## Primaire bronnen

- [Buzz NIP-RS-concept: synchronisatie van leesstatus tussen apparaten (vastgepinde revisie)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-RS.md)
- [Buzz pull request #8639: leesstatus via een relay-capability (open)](https://github.com/block/buzz/pull/8639)

## Zie ook

- [NIP-44](/nl/topics/nip-44/)
- [NIP-78](/nl/topics/nip-78/)

**Vermeld in:**

- [Nieuwsbrief #46: Buzz](/nl/newsletters/2026-10-28-newsletter/#buzz)
