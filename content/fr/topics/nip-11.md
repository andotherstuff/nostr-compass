---
title: "NIP-11 : Document d'information du relais"
date: 2025-12-17
translationOf: /en/topics/nip-11.md
translationDate: 2026-03-11
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11 définit comment les relais publient une description lisible par les machines, incluant le support de fonctionnalités revendiqué, les limites et les métadonnées de l'opérateur.

## Fonctionnement

Les clients récupèrent les informations du relais en effectuant une requête HTTP GET vers l'URL WebSocket du relais avec un en-tête `Accept: application/nostr+json`. Le relais renvoie un document JSON décrivant ses capacités.

## Champs utiles

- **name** : nom lisible du relais
- **description** : à quoi sert le relais
- **supported_nips** : liste des NIPs revendiqués comme supportés
- **limitation** : restrictions comme la taille maximale de message, l'authentification requise, etc.
- **pubkey** : clé publique de l'opérateur du relais, lorsqu'elle est fournie
- **contact** : adresse de contact de l'opérateur

## Modèle de confiance

NIP-11 est constitué de métadonnées auto-déclarées. Il indique ce qu'un relais dit de lui-même, pas ce qu'il a prouvé en conditions réelles. C'est malgré tout utile pour la découverte et l'expérience utilisateur, mais les clients ne devraient pas traiter `supported_nips` comme une vérité établie sans tester le comportement.

Cette distinction compte pour la sélection de relais. Un relais peut annoncer la recherche NIP-50, des exigences d'authentification ou une limite de message élevée, mais la vraie réponse n'apparaît qu'une fois que le client se connecte réellement et exerce ces chemins de code.

## Pourquoi c'est important

- Les clients peuvent vérifier si un relais supporte les fonctionnalités requises avant de se connecter
- Les services de découverte peuvent indexer les capacités des relais
- Les utilisateurs peuvent consulter les politiques du relais avant de publier

## Évolution récente de la spécification

La spécification a été réduite au fil du temps. Les anciens champs optionnels comme `software`, `version`, les détails de politique de confidentialité et les métadonnées de rétention ont été supprimés après des années de faible adoption. Les documents NIP-11 actuels sont donc plus compacts et réalistes, mais les clients ne devraient pas s'attendre à des métadonnées de politique riches de la part des relais.

---

**Sources principales :**
- [Spécification NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [PR #1764](https://github.com/nostr-protocol/nips/pull/1764) - mise à jour du champ d'identité du relais
- [PR #1946](https://github.com/nostr-protocol/nips/pull/1946) - nettoyage des champs peu utilisés
- [PR #2231](https://github.com/nostr-protocol/nips/pull/2231) - suppression des champs obsolètes

**Mentionné dans :**
- [Newsletter #1 : NIP Updates](/fr/newsletters/2025-12-17-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-66 : Découverte de relais et surveillance de disponibilité](/fr/topics/nip-66/)
