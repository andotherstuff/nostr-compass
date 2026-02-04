---
title: "NIP-34 (Collaboration Git)"
date: 2026-02-04
description: "NIP-34 permet l'hébergement décentralisé de dépôts git et la collaboration via les événements Nostr."
---

NIP-34 définit les types d'événements pour héberger des dépôts git, des patches et des issues sur les relais Nostr. Cela permet une collaboration de code entièrement décentralisée sans dépendance aux plateformes d'hébergement centralisées comme GitHub ou GitLab.

## Fonctionnement

Les dépôts sont représentés comme des événements adressables (kind 30617) contenant des métadonnées comme le nom, la description et les URLs de clonage. Le propriétaire du dépôt publie cet événement pour établir le projet sur Nostr.

Les patches (kind 1617) contiennent du contenu de patch git qui peut être appliqué à un dépôt. Les contributeurs soumettent des patches comme événements référençant le dépôt cible. Cela reflète le flux de travail par patch basé sur email utilisé par des projets comme le noyau Linux.

Les issues (kind 1621) fonctionnent comme les systèmes de suivi d'issues traditionnels. Elles référencent un dépôt et contiennent un titre et une description. Les commentaires sur les issues et patches utilisent des événements de réponse standard.

## Types d'événements

- **30617** - Annonce de dépôt (adressable)
- **1617** - Soumission de patch
- **1621** - Issue
- **1622** - Statut d'issue (ouverte/fermée)

## Implémentations

- **ngit** - Outil en ligne de commande pour publier des dépôts et patches sur Nostr
- **gitworkshop.dev** - Interface web pour parcourir les dépôts hébergés sur Nostr
- **Notedeck** - Client de bureau avec [support brouillon pour la visualisation NIP-34](https://github.com/damus-io/notedeck/pull/1279)

## Sources principales

- [Spécification NIP-34](https://github.com/nostr-protocol/nips/blob/master/34.md)

## Mentionné dans

- [Newsletter #8 (2026-02-04)](/fr/newsletters/2026-02-04-newsletter/) - Notedeck ajoutant le visualiseur NIP-34
