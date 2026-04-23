---
title: "NIP-40 : Horodatage d'expiration"
date: 2025-12-17
translationOf: /en/topics/nip-40.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
---

NIP-40 définit un tag d'expiration qui indique aux relais quand un événement doit être supprimé.

## Fonctionnement

Les événements incluent un tag `expiration` avec un horodatage Unix :

```json
["expiration", "1734567890"]
```

Après ce moment, les relais devraient supprimer l'événement et refuser de le servir.

## Pourquoi c'est important

- Contenu éphémère qui devrait disparaître après un temps défini
- Offres ou annonces à durée limitée
- Expiration des annonces dans les places de marché (ex. Shopstr)
- Réduction des besoins de stockage des relais

L'expiration est une indication de rétention, pas un système de révocation. Elle aide à aligner le comportement des relais concernant le contenu obsolète, mais ne garantit pas l'effacement une fois qu'un autre relais, client ou archive a déjà copié l'événement.

## Notes de confiance et de sécurité

- Les relais ne sont pas obligés d'honorer l'expiration (mais la plupart le font)
- Les clients ne devraient pas compter sur l'expiration pour la suppression de contenu critique en termes de sécurité
- Une fois le contenu récupéré par un autre client, il peut être mis en cache ou republié
- L'expiration ne masque pas le fait qu'un événement a existé. Les identifiants d'événement, les citations ou les copies hors relais peuvent persister après le passage de l'horodatage

---

**Sources principales :**
- [Spécification NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/en/newsletters/2025-12-17-newsletter/)
- [Newsletter #3 : Changements de code notables](/en/newsletters/2025-12-31-newsletter/)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)
