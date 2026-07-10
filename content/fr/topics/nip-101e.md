---
title: "NIP-101e : Séances d'entraînement fitness"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-101e.md
translationDate: 2026-07-01
categories:
  - Fitness
  - Discovery
---

NIP-101e définit un format d'événement d'entraînement pour que les applications de suivi fitness puissent publier, partager et découvrir des séances d'entraînement sur Nostr. La spécification utilise des événements de kind 1301 qui transportent les métriques de séance (distance, durée, dénivelé, fréquence cardiaque, calories, cadence de cyclisme, application source) dans des tags structurés afin qu'un client puisse afficher l'entraînement sous forme de carte structurée avec les métriques présentées dans leurs unités appropriées.

## Comment ça marche

Un entraînement NIP-101e est un événement de kind 1301 avec des tags structurés pour chaque métrique capturée par l'application source. Les tags courants incluent :

- `type` pour la discipline d'entraînement (course, vélo, natation, musculation, etc.)
- `distance` avec valeur et unité
- `duration` en secondes
- `elevation_gain` avec valeur et unité
- Horodatages `start` et `end`
- `heart_rate` (moyenne et maximum)
- `calories` pour la dépense énergétique
- `source` nommant l'application publiante
- Tags de sujet `t` pour la découverte par hashtag

Le champ `content` transporte une note optionnelle rédigée par l'utilisateur (l'équivalent de la légende qu'un utilisateur attacherait à un téléversement Strava). Les clients qui reconnaissent kind 1301 affichent les métriques structurées comme une carte d'entraînement ; les clients qui ne le reconnaissent pas se rabattent sur l'affichage du champ `content` comme une note ordinaire.

## Sémantique de découverte et de flux

Les événements NIP-101e sont des événements de flux normaux, donc un entraînement publié par un utilisateur apparaît dans le fil de ses abonnés comme n'importe quelle autre publication. Les clients dotés de vues d'entraînement dédiées peuvent s'abonner à kind 1301 avec des filtres par auteur ou hashtag pour construire des surfaces de journal d'entraînement, des classements ou des flux de défis communautaires. Le pubkey de l'auteur est l'identité canonique de l'entraînement, donc une application tierce lisant les entraînements d'un autre utilisateur hérite des mêmes hypothèses de confiance que tout autre flux Nostr.

## Implémentations

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) intègre le rendu des entraînements kind 1301 avec une métrique vedette, une grille de statistiques, un affichage de vitesse spécifique au cyclisme et des badges de source ([PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184), refactorisé dans [PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226))

---

**Sources primaires :**
- [Spécification NIP-101e](https://github.com/nostr-protocol/nips/blob/master/101e.md)
- [Amethyst PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184) - Ajoute la prise en charge des entraînements fitness NIP-101e (Kind 1301)
- [Amethyst PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226) - Refonte de l'affichage d'entraînement avec métrique vedette et grille de statistiques

**Mentionné dans :**
- [Newsletter #27 : Amethyst v1.12.0 intègre les portefeuilles Cashu, les nutzaps, un pilote CLINK et l'auto-réparation Tor](/fr/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
