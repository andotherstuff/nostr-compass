---
title: "NIP-40 : Horodatage d'expiration"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-40 définit un tag d'expiration qui indique aux relais quand un événement doit être supprimé.

## Structure

Les événements incluent un tag `expiration` avec un horodatage Unix :

```json
["expiration", "1734567890"]
```

Après ce moment, les relais devraient supprimer l'événement et refuser de le servir.

## Cas d'utilisation

- Contenu éphémère qui devrait disparaître après un temps défini
- Offres ou annonces à durée limitée
- Expiration des annonces dans les places de marché (ex: Shopstr)
- Réduction des besoins de stockage des relais

## Considérations

- Les relais ne sont pas obligés d'honorer l'expiration (mais la plupart le font)
- Les clients ne devraient pas compter sur l'expiration pour la suppression de contenu critique en termes de sécurité
- Une fois le contenu récupéré par un autre client, il peut être mis en cache ou republié

---

**Sources principales :**
- [Spécification NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/fr/newsletters/2025-12-17-newsletter/#news)

