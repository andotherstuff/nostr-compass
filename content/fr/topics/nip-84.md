---
title: "NIP-84 : Highlights"
date: 2026-02-18
translationOf: /en/topics/nip-84.md
translationDate: 2026-02-18
draft: false
categories:
  - Content
  - Protocol
---

NIP-84 définit les événements « highlight » de kind 9802 qui permettent aux utilisateurs de marquer et de partager des passages qu'ils trouvent intéressants dans des contenus longs sur Nostr.

## Fonctionnement

Le champ `.content` contient le texte mis en évidence. Les événements référencent leur contenu source en utilisant des tags `a` ou `e` pour le contenu natif Nostr, ou des tags `r` pour les URLs externes (les clients doivent supprimer les paramètres de suivi). Les tags `p` optionnels attribuent les auteurs originaux, et un tag `context` optionnel fournit le texte environnant lorsque le highlight est une portion d'un passage plus large.

## Highlights avec citation

Les utilisateurs peuvent ajouter un tag `comment` pour créer des highlights avec citation, qui se rendent comme des reposts cités. Cela évite les entrées en double dans les clients de microblogging. Dans les commentaires, les mentions avec tag `p` nécessitent un attribut « mention » pour les distinguer des attributions d'auteur/éditeur, et les URLs avec tag `r` utilisent un attribut « source » pour les références d'origine.

---

**Sources principales :**
- [Spécification NIP-84](https://github.com/nostr-protocol/nips/blob/master/84.md)

**Mentionné dans :**
- [Compass #10 : Versions](/fr/newsletters/2026-02-18-newsletter/#prism--partager-nimporte-quoi-vers-nostr-depuis-android)

**Voir aussi :**
- [NIP-94 : Métadonnées de fichier](/fr/topics/nip-94/)
