---
title: "Proposition NIP-FE : commandes relay via HTTP"
date: 2026-09-30
draft: false
categories:
  - Project Proposals
  - Relays
translationOf: /en/topics/nip-fe.md
translationDate: 2026-10-01
---

Amethyst utilise l'appellation provisoire NIP-FE pour les commandes relay via HTTP dans ses travaux sur le relay Geode et le client Quartz. Cette appellation ne correspond pas à un NIP attribué et ne constitue pas une preuve d'adoption par les relays Nostr.

## Transport

Au lieu d'ouvrir une connexion WebSocket, un client envoie par POST une seule trame `REQ`, `COUNT` ou `EVENT` à un point de terminaison HTTP du relay. La réponse transmet en flux des trames relay sous forme de JSON délimité par des sauts de ligne. Un client doit distinguer une réponse complète d'un flux interrompu, et une requête authentifiée utilise toujours une autorisation HTTP Nostr signée. Le transport modifie la manière dont les commandes parviennent à un relay ; il ne modifie ni la signature sous-jacente de l'event ni le contenu de l'event.

L'[implémentation fusionnée](https://github.com/vitorpamplona/amethyst/pull/4231) d'Amethyst ajoute la route Geode, la prise en charge dans le client Quartz, des limites sur le corps des requêtes et leur concurrence, ainsi que des tests du découpage en trames et de l'autorisation. Elle constitue une preuve d'implémentation au niveau du code source, et non la preuve que des relays indépendants ont implémenté la même proposition.

## Collision de noms

Une [pull request à l'état de brouillon dans le dépôt des NIPs](https://github.com/nostr-protocol/nips/pull/2488), sans lien avec ces travaux, utilise également **NIP-FE**, cette fois pour des flux privés reposant sur une proposition d'enveloppe à destinataires multiples. Ces travaux restent ouverts et décrivent un problème différent de celui du transport HTTP d'Amethyst. Aucun de ces usages provisoires n'établit que l'appellation a été attribuée à une spécification acceptée ; les lecteurs doivent identifier la proposition par sa source et son sujet.

---

**Sources primaires :**
- [PR d'implémentation de Geode et Quartz dans Amethyst](https://github.com/vitorpamplona/amethyst/pull/4231)
- [Dépôt d'Amethyst](https://github.com/vitorpamplona/amethyst)
- [Brouillon ouvert sur les flux privés utilisant également NIP-FE](https://github.com/nostr-protocol/nips/pull/2488)

**Mentionné dans :**
- [Lettre d'information #42 : commandes relay d'Amethyst](/fr/newsletters/2026-09-30-newsletter/#amethyst-repairs-encrypted-group-interoperability)
