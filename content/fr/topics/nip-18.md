---
title: "NIP-18 : Reposts"
date: 2025-12-17
translationOf: /en/topics/nip-18.md
translationDate: 2026-03-07
draft: false
categories:
  - Social
  - Protocol
---

NIP-18 définit comment reposter des événements, similaire aux retweets sur d'autres plateformes.

## Fonctionnement

Un repost est un événement kind 6 (pour les notes kind 1) ou kind 16 (repost générique) contenant :
- Un tag `e` référençant l'événement reposté
- Un tag `p` référençant l'auteur original
- Optionnellement, l'événement original complet dans le champ `content`

Kind 6 est spécifique aux notes textuelles. Kind 16 existe pour que les clients puissent reposter d'autres types d'événements sans prétendre que tout est une note kind 1.

## Notes d'interopérabilité

Support amélioré pour reposter les événements remplaçables avec le support du tag `a`. Cela permet aux reposts d'événements adressables (kinds 30000-39999) de les référencer par leur adresse plutôt que par un ID d'événement spécifique.

Cette distinction est importante car les événements adressables peuvent être mis à jour au fil du temps. Reposter par coordonnée `a` permet aux clients de pointer vers la version actuelle d'un événement adressable, tandis que reposter par ID d'événement fige une instance historique spécifique.

## Pourquoi c'est important

Les reposts sont plus qu'un bouton de partage dans l'interface. Ils font partie de la manière dont le contenu circule à travers les graphes sociaux, dont les clients comptent l'engagement, et dont les données d'indices de relais se propagent à travers le réseau. Si un client gère mal les tags de repost, la reconstruction des fils et la récupération des événements peuvent se casser de manière subtile.

---

**Sources principales :**
- [Spécification NIP-18](https://github.com/nostr-protocol/nips/blob/master/18.md)
- [PR #2132](https://github.com/nostr-protocol/nips/pull/2132) - support du tag `a` pour les reposts génériques

**Mentionné dans :**
- [Newsletter #1 : NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #8 : News](/en/newsletters/2026-02-04-newsletter/#news)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)
- [NIP-10 : Threading des notes textuelles](/fr/topics/nip-10/)
