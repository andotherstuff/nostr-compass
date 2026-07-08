---
title: "NIP-B0 : Signets web"
date: 2026-05-28
draft: false
translationOf: /en/topics/nip-b0.md
translationDate: 2026-07-01
categories:
  - Protocol
  - Social
---

NIP-B0 définit un événement remplaçable paramétré (kind 39701) qui publie des signets web en tant qu'événements Nostr de première classe. La proposition permet aux utilisateurs de bâtir des collections de signets soignées qui peuvent être découvertes, zappées et republiées entre clients sans dépendre d'un service central de signets.

## Comment ça marche

Un signet est un événement de kind 39701 dont le tag `d` est l'URL canonique de la page mise en signet. La sémantique remplaçable permet à l'auteur de mettre à jour son propre signet pour cette URL (retaguer, mettre à jour le titre, marquer comme périmé) sans produire d'événements en double. Le champ content porte la note de l'auteur sur le signet ; les tags portent le titre, la description, l'image et des tags de sujet `t` pour la découverte.

```json
{
  "kind": 39701,
  "tags": [
    ["d", "https://example.com/an-article-worth-saving"],
    ["title", "Article Title"],
    ["t", "nostr"],
    ["t", "protocol"],
    ["published_at", "1717000000"]
  ],
  "content": "Useful primer on the topic.",
  "pubkey": "...",
  "sig": "..."
}
```

Le tag `d` identifie le signet de manière unique par auteur, donc deux utilisateurs peuvent tous deux mettre en signet la même URL avec leurs propres annotations et ensembles de tags.

## Découverte et curation

Parce que chaque signet est un événement de première classe, tout client Nostr peut afficher un flux de signets en s'abonnant aux événements kind 39701 filtrés par tags ou auteurs. Les workflows pilotés par les curateurs deviennent naturels : un curateur publie une liste de signets, les lecteurs suivent le pubkey du curateur, et les signets circulent à travers n'importe quel relais qui les transporte. Il n'y a pas d'annuaire central.

## Implémentations

- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) — Client web de référence avec une architecture à trois boîtes (curateur, indexeur, visualiseur) et un système de paliers financé par des zaps NIP-57 directs vers le curateur. Implémente NIP-B0 aux côtés de NIP-07, NIP-46, NIP-57, NIP-44, NIP-98, NIP-65 et Blossom BUD-01/BUD-04 pour le stockage de fichiers.

## Notes de confiance et de sécurité

- Les signets sont publics par défaut ; ne publiez pas de listes de lecture privées de cette façon
- La republication dépend des relais qui continuent à transporter les événements ; les relais éphémères abandonneront les signets
- Le tag `published_at` est déclaré par l'éditeur, non vérifiable

---

**Sources primaires :**
- [Spécification NIP-B0 proposée](https://github.com/nostr-protocol/nips/pull/2089) — Suit l'événement de signet web kind 39701 proposé
- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) — Implémentation de référence avec système de paliers pour curateurs

**Mentionné dans :**
- [Newsletter #24 : signets NIP-B0 deepmarks avec publication monétisée par le curateur](/fr/newsletters/2026-05-28-newsletter/#deepmarks-nip-b0-bookmarks-with-curator-monetized-publishing)
- [Newsletter #27 : Également livré](/fr/newsletters/2026-06-17-newsletter/#also-shipped)

**Voir aussi :**
- [NIP-57 : Zaps Lightning](/fr/topics/nip-57/)
- [NIP-65 : Métadonnées de liste de relais](/fr/topics/nip-65/)
