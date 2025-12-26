---
title: "NIP-51 : Listes"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Social
---

NIP-51 définit différents types de listes pour organiser les références aux événements, utilisateurs et contenus dans Nostr.

## Types de listes

- **Kind 10000** : Liste de mutes (utilisateurs, fils ou mots à masquer)
- **Kind 10001** : Liste d'épingles (événements à mettre en avant sur le profil)
- **Kind 30000** : Ensembles d'abonnements (listes d'abonnements catégorisées)
- **Kind 30003** : Ensembles de signets
- **Kind 30004** : Ensembles de curation (articles)
- **Kind 30005** : Ensembles vidéo
- **Kind 30006** : Ensembles d'images
- **Kind 30015** : Ensembles d'intérêts (hashtags)
- **Kind 30030** : Ensembles d'emojis

## Structure

Les listes utilisent des tags pour référencer le contenu :
- Tags `p` pour les clés publiques
- Tags `e` pour les événements
- Tags `a` pour les événements adressables
- Tags `t` pour les hashtags
- Tags `word` pour les mots mutés

## Public vs Privé

Les listes peuvent avoir des tags publics (visibles par tous) et un contenu chiffré (privé). Les éléments privés sont chiffrés en utilisant NIP-44 et stockés dans le champ `content` de l'événement. Le chiffrement utilise les propres clés de l'auteur (chiffrement vers soi-même).

Cela permet des fonctionnalités comme des signets publics avec des notes privées, ou une liste de mutes où les éléments mutés sont cachés aux autres.

## Changements récents

- Tags hashtag et URL supprimés des signets génériques ; les hashtags utilisent maintenant le kind 30015
- Kind 30006 ajouté pour les ensembles d'images curées

---

**Sources principales :**
- [Spécification NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md)

**Mentionné dans :**
- [Newsletter #1 : Mises à jour NIP](/fr/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2 : Mises à jour NIP](/fr/newsletters/2025-12-24-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-02 : Liste d'abonnements](/fr/topics/nip-02/)

