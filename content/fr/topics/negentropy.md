---
title: "Negentropy : protocole de réconciliation d'ensembles"
date: 2026-01-28
translationOf: /en/topics/negentropy.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Sync
---

Negentropy est un protocole de réconciliation d'ensembles qui permet de déterminer quels événements un côté possède et l'autre non, sans renvoyer l'intégralité du jeu de données.

## Fonctionnement

Plutôt que de demander tous les événements correspondant à un filtre, negentropy compare deux ensembles triés et se concentre uniquement sur les plages qui diffèrent. Le protocole échange des résumés de plages compacts et ne recourt aux listes explicites d'identifiants que là où c'est nécessaire.

1. **Tri** : les deux côtés trient les enregistrements par horodatage, puis par identifiant
2. **Comparaison de plages** : ils échangent des empreintes pour des plages d'enregistrements
3. **Affinement** : les plages non concordantes sont subdivisées jusqu'à ce que les identifiants manquants soient clairement identifiés

## Pourquoi c'est important

La synchronisation Nostr traditionnelle utilise des filtres `since` basés sur l'horodatage, qui peuvent manquer des événements en raison de :
- la dérive d'horloge entre le client et le relais
- plusieurs événements avec des horodatages identiques
- des événements arrivant dans le désordre

Negentropy résout ces problèmes en comparant les ensembles d'événements réels plutôt qu'en se fiant aux horodatages.

## Utilisation pratique

- **Récupération de DM** : les clients peuvent détecter et récupérer les messages directs manquants même avec d'anciens horodatages
- **Synchronisation de fil** : assure une synchronisation complète de la timeline à travers les relais
- **Synchronisation hors ligne** : rattrapage efficace après des périodes de déconnexion

Le détail d'implémentation utile est que beaucoup de clients ne remplacent pas les abonnements normaux par negentropy. Ils l'utilisent comme chemin de réparation. Damus, par exemple, a conservé le chargement ordinaire des DM et ajouté negentropy lors du rafraîchissement manuel pour récupérer les messages que le flux normal aurait manqués.

## Compromis

Negentropy nécessite un support des deux côtés, et il ajoute de la complexité protocolaire au-delà de l'usage standard de `REQ`. Il est le plus utile lorsque l'exactitude compte davantage que la simplicité d'implémentation.

Dans les environnements mixtes, les clients ont encore besoin d'un comportement de repli gracieux car tous les relais ne supportent pas le protocole.

---

**Sources principales :**
- [Dépôt du protocole Negentropy](https://github.com/hoytech/negentropy)
- [Damus PR #3536](https://github.com/damus-io/damus/pull/3536)
- [Damus PR #3547](https://github.com/damus-io/damus/pull/3547)

**Mentionné dans :**
- [Newsletter #6 : Damus intègre negentropy pour une synchronisation fiable des DM](/fr/newsletters/2026-01-28-newsletter/#damus-ships-negentropy-for-reliable-dm-syncing)
- [Newsletter #12](/fr/newsletters/2026-03-04-newsletter/)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)
