---
title: "NIP-84 : Highlights"
date: 2026-02-18
translationOf: /en/topics/nip-84.md
translationDate: 2026-03-07
draft: false
categories:
  - Content
  - Protocol
---

NIP-84 définit les événements kind 9802 "highlight" qui permettent aux utilisateurs de marquer et partager des passages qu'ils trouvent intéressants dans du contenu long format sur Nostr.

## Fonctionnement

Le champ `.content` contient le texte mis en surbrillance. Les événements référencent leur source via des tags `a` ou `e` pour le contenu natif Nostr, ou des tags `r` pour les URL externes (les clients doivent supprimer les paramètres de tracking). Des tags `p` optionnels attribuent les auteurs originaux, et un tag `context` optionnel fournit le texte environnant lorsque le highlight ne couvre qu'une portion d'un passage plus large.

Pour les médias non textuels, le contenu du highlight peut être vide. Cela permet aux clients de pointer vers un highlight audio ou vidéo tout en conservant la référence source dans les tags.

## Quote Highlights

Les utilisateurs peuvent ajouter un tag `comment` pour créer des quote highlights, qui s'affichent comme des reposts avec citation. Cela évite les doublons dans les clients de microblogging. Dans les commentaires, les mentions via `p`-tag nécessitent un attribut "mention" pour les distinguer des attributions auteur/éditeur, et les URL via `r`-tag utilisent un attribut "source" pour les références d'origine.

## Pourquoi c'est important

NIP-84 sépare le passage mis en surbrillance de la discussion environnante. Un client peut afficher le texte sélectionné comme objet principal, puis traiter le commentaire comme métadonnée optionnelle au lieu de mélanger les deux dans une note classique.

C'est utile pour les outils de lecture et de recherche car cela préserve l'extrait exact. Deux lecteurs peuvent commenter le même article tout en produisant des événements highlight portables que d'autres clients comprennent.

## Notes d'interopérabilité

Les tags d'attribution sont plus importants qu'il n'y paraît. Un tag `p` avec un rôle `author` ou `editor` indique aux clients qui a créé le contenu source, tandis qu'un rôle `mention` dans un quote comment signifie autre chose. Si les clients confondent ces cas, ils peuvent mal identifier la source du highlight ou notifier des personnes par erreur.

---

**Sources primaires :**
- [Spécification NIP-84](https://github.com/nostr-protocol/nips/blob/master/84.md)

**Mentionné dans :**
- [Newsletter #10 : Releases](/en/newsletters/2026-02-18-newsletter/#prism-share-anything-to-nostr-from-android)

**Voir aussi :**
- [NIP-94 : File Metadata](/fr/topics/nip-94/)
