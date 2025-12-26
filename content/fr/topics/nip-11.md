---
title: "NIP-11 : Informations du relais"
date: 2025-12-17
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11 définit comment les relais exposent des métadonnées sur eux-mêmes, incluant les NIPs supportés, les limitations et les informations de contact.

## Fonctionnement

Les clients récupèrent les informations du relais en faisant une requête HTTP GET à l'URL WebSocket du relais avec un en-tête `Accept: application/nostr+json`. Le relais renvoie un document JSON décrivant ses capacités.

## Champs clés

- **name** - Nom du relais lisible par l'humain
- **description** - À quoi sert le relais
- **supported_nips** - Liste des NIPs implémentés
- **limitation** - Restrictions comme la taille max des messages, l'authentification requise, etc.
- **self** - La clé publique propre du relais (nouveau champ pour l'identité du relais)

## Cas d'utilisation

- Les clients peuvent vérifier si un relais supporte les fonctionnalités requises avant de se connecter
- Les services de découverte peuvent indexer les capacités des relais
- Les utilisateurs peuvent voir les politiques du relais avant de publier

---

**Sources principales :**
- [Spécification NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md)

**Mentionné dans :**
- [Newsletter #1 : Mises à jour NIP](/fr/newsletters/2025-12-17-newsletter/#nip-updates)

