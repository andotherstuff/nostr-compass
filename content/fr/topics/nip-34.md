---
title: "NIP-34 : Collaboration Git"
date: 2026-02-04
description: "NIP-34 permet l'hébergement décentralisé de dépôts git et la collaboration via les événements Nostr."
translationOf: /en/topics/nip-34.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Development
---

NIP-34 définit les types d'événements pour héberger des dépôts git, des patches et des issues sur les relais Nostr. Cela permet une collaboration de code entièrement décentralisée sans dépendance aux plateformes d'hébergement centralisées comme GitHub ou GitLab.

## Fonctionnement

Les dépôts sont représentés comme des événements adressables (kind 30617) contenant des métadonnées comme le nom, la description et les URLs de clonage. Le propriétaire du dépôt publie cet événement pour établir le projet sur Nostr.

Les patches (kind 1617) contiennent du contenu `git format-patch` qui peut être appliqué à un dépôt. Les contributeurs soumettent des patches comme événements référençant le dépôt cible. Cela reproduit le flux de travail par patch basé sur email utilisé par des projets comme le noyau Linux.

Les issues (kind 1621) fonctionnent comme les systèmes de suivi d'issues traditionnels. Les pull requests utilisent les kinds 1618 et 1619, et les mises à jour de statut utilisent les kinds 1630 à 1633. Les réponses aux issues, patches et pull requests utilisent les commentaires [NIP-22](/fr/topics/nip-22/).

## Types d'événements

- **30617** - Annonce de dépôt (adressable)
- **30618** - Annonce d'état du dépôt pour les branches et les tags
- **1617** - Soumission de patch
- **1618** - Pull request
- **1619** - Mise à jour de pull request
- **1621** - Issue
- **1630-1633** - Événements de statut : ouvert, fusionné/résolu, fermé et brouillon

## Pourquoi c'est important

NIP-34 sépare la découverte du transport. Le dépôt réel peut rester sur des serveurs Git ordinaires, mais les événements Nostr fournissent une couche distribuée par les relais pour la découverte, la discussion, l'échange de patches et le suivi de statut. Un projet peut ainsi conserver ses outils git natifs sans dépendre de la base de données ou de l'API d'une seule forge.

Le tag `r` avec le commit unique le plus ancien est l'un des détails les plus importants. Il donne aux clients un moyen de regrouper les miroirs et les forks qui représentent la même lignée de dépôt sous-jacente, ce qui est difficile à déduire des noms seuls.

## État des implémentations

- **ngit** - Outil en ligne de commande pour publier des dépôts et des patches sur Nostr
- **gitworkshop.dev** - Interface web pour parcourir les dépôts hébergés sur Nostr
- **Notedeck** - Client de bureau avec [support brouillon pour la visualisation NIP-34](https://github.com/damus-io/notedeck/pull/1279)

---

**Sources principales :**
- [Spécification NIP-34](https://github.com/nostr-protocol/nips/blob/master/34.md)

**Mentionné dans :**
- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - Notedeck ajoutant le visualiseur NIP-34
- [Newsletter #9 : Notedeck](/en/newsletters/2026-02-11-newsletter/#notedeck)

**Voir aussi :**
- [NIP-22 : Commentaires](/fr/topics/nip-22/)
