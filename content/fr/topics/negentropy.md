---
title: "Negentropy : Protocole de réconciliation d'ensembles"
date: 2026-01-28
translationOf: /en/topics/negentropy.md
translationDate: 2026-01-28
draft: false
categories:
  - Protocol
  - Sync
---

Negentropy est un protocole de réconciliation d'ensembles qui permet une synchronisation efficace entre les clients Nostr et les relais en identifiant les événements manquants sans transférer l'ensemble complet des données.

## Fonctionnement

Plutôt que de demander tous les événements correspondant à un filtre, negentropy permet aux clients de comparer leur ensemble d'événements local avec celui d'un relais et d'identifier uniquement les différences. Ceci est accompli via un protocole multi-tours :

1. **Empreinte** : Le client et le relais calculent chacun une empreinte de leurs ensembles d'événements
2. **Comparaison** : Les empreintes sont échangées et comparées
3. **Réconciliation** : Seuls les IDs d'événements manquants sont identifiés et transférés

## Pourquoi c'est important

La synchronisation Nostr traditionnelle utilise des filtres `since` basés sur l'horodatage, qui peuvent manquer des événements en raison de :
- La dérive d'horloge entre le client et le relais
- Plusieurs événements avec des horodatages identiques
- Des événements arrivant dans le désordre

Negentropy résout ces problèmes en comparant les ensembles d'événements réels plutôt que de se fier aux horodatages.

## Cas d'utilisation

- **Récupération de messages privés** : Les clients peuvent détecter et récupérer les messages directs manquants même avec d'anciens horodatages
- **Synchronisation du fil** : Assure une synchronisation complète de la timeline à travers les relais
- **Synchronisation hors ligne** : Rattrape efficacement après des périodes de déconnexion

## Implémentation

Negentropy nécessite le support des relais. Les clients l'implémentent généralement comme mécanisme de récupération de secours plutôt que de remplacer les abonnements REQ standard, se dégradant gracieusement lorsque les relais ne supportent pas le protocole.

## Voir aussi

- [NIP-01](/fr/topics/nip-01/) - Protocole de base
