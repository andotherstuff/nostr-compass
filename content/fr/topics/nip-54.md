---
title: "NIP-54: Wiki"
date: 2025-12-31
translationOf: /en/topics/nip-54.md
translationDate: 2025-12-31
draft: false
categories:
  - Protocole
  - Contenu
---

NIP-54 définit kind 30818 comme un type d'événement adressable pour créer des articles wiki et des entrées d'encyclopédie sur Nostr. Il permet la création de contenu collaboratif et décentralisé où plusieurs auteurs peuvent écrire sur les mêmes sujets.

## Fonctionnement

Les articles wiki sont identifiés par un `d` tag normalisé (le sujet de l'article). Plusieurs personnes peuvent écrire des articles sur le même sujet, créant une base de connaissances décentralisée sans autorité centrale.

**Normalisation du D Tag :**
- Convertir toutes les lettres en minuscules
- Convertir les espaces en tirets
- Supprimer la ponctuation et les symboles
- Préserver les caractères non-ASCII et les chiffres

## Format du Contenu

Les articles utilisent le balisage Asciidoc avec deux fonctionnalités spéciales :

- **Wikilinks** (`[[page cible]]`) - Liens vers d'autres articles wiki sur Nostr
- **Liens Nostr** - Références à des profils ou événements selon NIP-21

## Sélection des Articles

Lorsque plusieurs versions d'un article existent, les clients priorisent selon :

1. Les réactions (NIP-25) indiquant l'approbation de la communauté
2. Les listes de relays (NIP-51) pour le classement des sources
3. Les listes de contacts (NIP-02) formant des réseaux de recommandation

## Fonctionnalités Collaboratives

- **Fork** - Créer des versions dérivées d'articles
- **Demandes de fusion** (kind 818) - Proposer des modifications aux articles existants
- **Redirections** (kind 30819) - Pointer les anciens sujets vers les nouveaux
- **Marqueurs de déférence** - Indiquer les versions d'articles préférées

---

**Sources primaires :**
- [Spécification NIP-54](https://github.com/nostr-protocol/nips/blob/master/54.md)

**Mentionné dans :**
- [Newsletter #3 : Mises à jour NIP](/fr/newsletters/2025-12-31-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-51 : Listes](/fr/topics/nip-51/)
- [NIP-02 : Liste de Suivi](/fr/topics/nip-02/)
