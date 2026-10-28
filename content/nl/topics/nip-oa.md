---
title: 'Buzz-concept NIP-OA: eigenaarsattestatie'
date: 2026-10-28
translationOf: /en/topics/nip-oa.md
translationDate: 2026-10-28
draft: false
---

**Status:** Dit is een conceptvoorstel dat specifiek is voor het Buzz-project. NIP-OA is geen geaccepteerde officiële NIP. Het label komt uit de projectdocumentatie van Buzz, en de officiële NIPs-repository heeft het niet toegekend of goedgekeurd.

## Doel

NIP-OA definieert een optionele tag `auth` waarmee een eigenaarssleutel een agentsleutel kan machtigen om events te publiceren. De auteur van het event blijft de agentsleutel. Een geldige tag geldt uitsluitend als bewijs van machtiging en stelt de agent niet in staat zich als de eigenaar voor te doen.

## Mechanisme

Met een Schnorr-handtekening ondertekent de eigenaar een domeingescheiden hash die de agent-pubkey koppelt aan een exacte conditiestring. Condities kunnen een bepaalde event-kind vereisen en grenzen stellen aan de zelf opgegeven `created_at`. Zolang elk event aan de condities voldoet, kan de agent de tag op zijn events hergebruiken. Verifiers valideren eerst het kernevent en controleren daarna de handtekening van de eigenaar en elke conditie.

## Beperkingen

Een lege conditiestring voegt geen beperkingen toe. Tijdstempelclausules beperken een veld dat de agent zelf beheert, dus leveren ze geen verloop op basis van de werkelijke kloktijd. Wie versheid nodig heeft, moet die afzonderlijk controleren. Wordt de tag openbaar gepubliceerd, dan zijn de eigenaars- en agentsleutel aan elkaar gekoppeld.

## Primaire bronnen

- [Buzz NIP-OA-concept: eigenaarsattestatie (vastgepinde revisie)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-OA.md)

## Zie ook

- [NIP-01](/nl/topics/nip-01/)

**Vermeld in:**

- [Nieuwsbrief #46: Buzz](/nl/newsletters/2026-10-28-newsletter/#buzz)
