---
title: "Buzz NIP-AP : personas d'agent"
date: 2026-10-21
translationOf: /en/topics/nip-ap.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

Buzz NIP-AP est une spécification à l'état de brouillon du projet Buzz, qui ne fait pas partie des NIPs acceptés dans nostr-protocol/nips.

Elle définit des events de persona de kind 30175, c'est-à-dire des définitions adressables servant à instancier un agent IA, indexées par un slug `d` en clair. Le kind 30178 contient une projection du catalogue d'équipe. Les relays qui l'implémentent restreignent l'accès à ces deux kinds : les auteurs lisent leurs propres events, tandis que les autres lecteurs ne voient un event dans les requêtes, la livraison en direct, la recherche, les comptages ou les recherches par id que s'il porte `["shared", "true"]`. Partager une équipe expose la projection et les instructions intégrées de chacun de ses membres, y compris ceux dont les personas ne sont pas partagées. Ce filtrage contrôle l'accès sans chiffrer le contenu ; l'opérateur du relay peut toujours le lire.

Source primaire : la [spécification NIP-AP](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md) dans le dépôt Buzz.

## Sources primaires

- [Buzz NIP-AP : personas d'agent](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md)

## Mentionné dans

- [Newsletter #46 (2026-10-28) : buzz](/fr/newsletters/2026-10-28-newsletter/#buzz)

- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#buzz)
