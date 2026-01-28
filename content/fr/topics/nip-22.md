---
title: "NIP-22 : Commentaires"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Social
---

NIP-22 définit un standard pour commenter n'importe quel contenu Nostr adressable, permettant des discussions en fil sur les articles, vidéos, événements de calendrier et autres événements adressables.

## Fonctionnement

Les commentaires utilisent des événements kind 1111 avec des tags référençant le contenu commenté :

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["E", "root-event-id", "wss://relay.example"],
    ["K", "30023"]
  ],
  "content": "Super article !"
}
```

## Structure des tags

- **Tag `A`** : Référence l'événement adressable commenté (format kind:pubkey:d-tag)
- **Tag `E`** : Référence l'ID de l'événement racine pour le fil
- **Tag `K`** : Indique le kind de l'événement racine
- **Tag `e`** : Référence le commentaire parent pour les réponses imbriquées

## Différence avec le Kind 1

Bien que les notes kind 1 puissent répondre à d'autres notes, les commentaires NIP-22 sont spécifiquement conçus pour :

- Le contenu adressable (articles, vidéos, événements de calendrier)
- Maintenir des relations parent-enfant claires
- Permettre la modération et le fil sur le contenu long format

## Cas d'utilisation

- Discussions d'articles
- Commentaires vidéo
- Discussions sur les événements de calendrier [NIP-52](/fr/topics/nip-52/)
- Pages de discussion des pages wiki
- N'importe quel type d'événement adressable

## Voir aussi

- [NIP-01](/fr/topics/nip-01/) - Protocole de base (notes kind 1)
- [NIP-52](/fr/topics/nip-52/) - Événements de calendrier
