---
title: "NIP-54 : Wiki"
date: 2025-12-31
translationOf: /en/topics/nip-54.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Content
---

NIP-54 définit le kind `30818` pour les articles de type wiki sur Nostr. Plusieurs auteurs peuvent publier des entrées pour le même sujet, les clients ont donc besoin d'heuristiques de classement et de confiance plutôt qu'une page canonique unique.

## Fonctionnement

Les articles wiki sont identifiés par un tag `d` normalisé qui représente le sujet. Plusieurs personnes peuvent publier des entrées avec le même sujet normalisé, créant un wiki ouvert sans éditeur central.

**Normalisation du tag D :**
- Mettre en minuscules les lettres qui ont des variantes de casse
- Convertir les espaces en tirets
- Supprimer la ponctuation et les symboles
- Réduire les tirets répétés et supprimer les tirets en début ou fin
- Préserver les lettres et chiffres non-ASCII

Cette règle de normalisation est importante pour l'interopérabilité. Si deux clients normalisent le même titre différemment, ils interrogeront des sujets différents et fragmenteront l'ensemble d'articles.

## Format du contenu

La spécification fusionnée utilise le balisage Asciidoc avec deux fonctionnalités supplémentaires :

- **Wikilinks** (`[[page cible]]`) - Liens vers d'autres articles wiki sur Nostr
- **Liens Nostr** - Références à des profils ou événements selon NIP-21

Un passage à Djot a été proposé, mais il n'a pas remplacé Asciidoc dans le NIP canonique en date de mars 2026.

## Sélection des articles

Lorsque plusieurs versions d'un article existent, les clients peuvent prioriser selon :

1. Les réactions (NIP-25) indiquant l'approbation de la communauté
2. Les listes de relais (NIP-51) pour le classement des sources
3. Les listes de contacts (NIP-02) formant des réseaux de recommandation

En pratique, NIP-54 n'est pas seulement un format de contenu. C'est aussi un problème de politique client. Deux clients peuvent montrer des articles "meilleurs" différents pour le même sujet tout en restant conformes à la spécification.

## Fonctionnalités collaboratives

- **Fork** - Créer des versions dérivées d'articles
- **Demandes de fusion** (kind 818) - Proposer des modifications aux articles existants
- **Redirections** (kind 30819) - Pointer les anciens sujets vers les nouveaux
- **Marqueurs de déférence** - Indiquer les versions d'articles préférées

Les forks et les marqueurs de déférence permettent aux auteurs de reconnaître de meilleures versions sans supprimer leur propre travail. Cela compte dans un réseau où les anciennes révisions peuvent rester disponibles à travers de nombreux relais.

---

**Sources principales :**
- [NIP-54 Specification](https://github.com/nostr-protocol/nips/blob/master/54.md)
- [PR #2177: Internationalized d-tag normalization](https://github.com/nostr-protocol/nips/pull/2177)

**Mentionné dans :**
- [Newsletter #3 : NIP Updates](/en/newsletters/2025-12-31-newsletter/#nip-updates)
- [Newsletter #15 : Open PRs](/en/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**Voir aussi :**
- [NIP-51 : Lists](/fr/topics/nip-51/)
- [NIP-02 : Follow List](/fr/topics/nip-02/)
