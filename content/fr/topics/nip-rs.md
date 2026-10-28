---
title: "Brouillon Buzz NIP-RS : synchronisation de l’état de lecture entre appareils"
date: 2026-10-28
translationOf: /en/topics/nip-rs.md
translationDate: 2026-10-28
draft: false
---

**Statut :** il s’agit d’une proposition à l’état de brouillon, propre au projet Buzz. NIP-RS n’est pas un NIP officiel accepté. Ce label provient de la documentation du projet Buzz, et le dépôt officiel des NIPs ne l’a ni attribué ni approuvé.

## Objectif

NIP-RS permet aux appareils d’un même utilisateur de partager le point jusqu’où cet utilisateur a lu. Chaque installation publie un event adressable `kind:30078`. Son tag `d` se compose de `read-state:` suivi d’un identifiant d’emplacement aléatoire, et son contenu est chiffré selon NIP-44 à destination de la propre clé de l’utilisateur. En clair, ce contenu associe des identifiants de contexte à des frontières d’horodatage, chacune signifiant que tout ce qui date de ce moment ou d’avant a été lu. Le brouillon ne publie pas d’accusés de lecture et ne révèle pas ce que d’autres personnes ont lu.

## Limites

Les frontières sont des indications fournies au mieux sur l’activité récente. Elles ne constituent pas un historique complet des messages lus. Les forçages manuels en non-lu, y compris les planchers de tombstone, relèvent d’un contrat durable distinct. Charger l’intégralité de l’état des forçages dépend du comportement des relays en matière d’ordonnancement et de capacité, qu’un client ne peut pas vérifier entièrement ; un relay quelconque risque donc de ne pas renvoyer un état non lu complet. Pour la plupart, les identifiants de contexte n’ont de sens qu’au sein d’une même famille de clients.

Une pull request ouverte, #8639, propose de faire passer les clients Buzz à une capacité NIP-11 `buzz_v1`, adossée à une API HTTP privée et authentifiée, désactivée par défaut. Les relays dépourvus de cette capacité conserveraient NIP-RS.

## Sources primaires

- [Brouillon Buzz NIP-RS : synchronisation de l’état de lecture entre appareils (révision épinglée)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-RS.md)
- [Pull request Buzz #8639 : état de lecture via une capacité de relay (ouverte)](https://github.com/block/buzz/pull/8639)

## Voir aussi

- [NIP-44](/fr/topics/nip-44/)
- [NIP-78](/fr/topics/nip-78/)

**Mentionné dans :**

- [Newsletter n° 46 : Buzz](/fr/newsletters/2026-10-28-newsletter/#buzz)
