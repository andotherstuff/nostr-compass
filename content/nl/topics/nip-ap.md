---
title: "Buzz NIP-AP: agentpersona's"
date: 2026-10-21
translationOf: /en/topics/nip-ap.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

Buzz NIP-AP is een conceptspecificatie van het Buzz-project die buiten de geaccepteerde NIPs in nostr-protocol/nips valt.

Ze definieert persona-events van kind 30175: adresseerbare definities voor het instantiëren van een AI-agent, met een slug in platte tekst, `d`, als sleutel. Kind 30178 bevat een projectie van een teamcatalogus. Relays die dit implementeren, schermen beide kinds af: auteurs lezen hun eigen events, en andere lezers zien een event in queries, live levering, zoekopdrachten, tellingen of opzoekingen op id alleen als het `["shared", "true"]` bevat. Wie een team deelt, stelt de ingebedde projectie en instructies van elk lid bloot, ook van leden met niet-gedeelde persona's. De afscherming regelt de toegang zonder de content te versleutelen; de relay-operator kan die nog steeds lezen.

Primaire bron: de [NIP-AP-specificatie](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md) in de Buzz-repository.

## Primaire bronnen

- [Buzz NIP-AP: agentpersona's](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md)

## Vermeld in

- [Nieuwsbrief #46 (2026-10-28): buzz](/nl/newsletters/2026-10-28-newsletter/#buzz)

- [Nieuwsbrief 45](/en/newsletters/2026-10-21-newsletter/#buzz)
