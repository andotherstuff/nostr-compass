---
title: "NIP-FE-voorstel: Relay-opdrachten via HTTP"
date: 2026-09-30
translationOf: /en/topics/nip-fe.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Relays
---

Amethyst gebruikt het voorlopige label NIP-FE voor relay-opdrachten via HTTP in zijn werk aan de Geode-relay en de Quartz-client. Het label is geen toegewezen NIP en geen bewijs van adoptie door Nostr-relays in het algemeen.

## Transport {#transport}

In plaats van een WebSocket-verbinding te openen, stuurt een client één `REQ`-, `COUNT`- of `EVENT`-frame via een POST naar een HTTP-endpoint van een relay. Het antwoord streamt relay-frames als JSON gescheiden door regeleinden. Een client moet een volledig antwoord kunnen onderscheiden van een afgebroken stream, en een geauthenticeerd verzoek gebruikt nog steeds ondertekende Nostr-HTTP-autorisatie. Het transport verandert hoe opdrachten een relay bereiken; het verandert niets aan de onderliggende handtekening of inhoud van het event.

De [gemergede implementatie](https://github.com/vitorpamplona/amethyst/pull/4231) van Amethyst voegt de Geode-route, ondersteuning in de Quartz-client, limieten voor de body en gelijktijdigheid, en tests voor framing en autorisatie toe. Het is implementatiebewijs op broncodeniveau, geen bewijs dat onafhankelijke relays hetzelfde voorstel hebben geïmplementeerd.

## Naamconflict {#naming-collision}

Een ongerelateerde [concept-pull-request in de NIPs-repository](https://github.com/nostr-protocol/nips/pull/2488) gebruikt ook **NIP-FE**, dit keer voor privéfeeds die zijn gebouwd op een voorgestelde envelop voor meerdere ontvangers. Dat werk staat open en beschrijft een ander probleem dan het HTTP-transport van Amethyst. Geen van beide voorlopige toepassingen toont aan dat het label aan een geaccepteerde specificatie is toegewezen; lezers kunnen het voorstel het best aanduiden aan de hand van de bron en het onderwerp.

---

**Primaire bronnen:**
- [PR voor de Geode- en Quartz-implementatie van Amethyst](https://github.com/vitorpamplona/amethyst/pull/4231)
- [Amethyst-repository](https://github.com/vitorpamplona/amethyst)
- [Open concept voor privéfeeds dat ook NIP-FE gebruikt](https://github.com/nostr-protocol/nips/pull/2488)

**Genoemd in:**
- [Nieuwsbrief #42: relay-opdrachten van Amethyst](/nl/newsletters/2026-09-30-newsletter/#amethyst-repairs-encrypted-group-interoperability)
