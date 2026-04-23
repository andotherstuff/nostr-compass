---
title: "NIP-23 : Contenu long-form"
date: 2026-04-08
translationOf: /en/topics/nip-23.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Content
---

NIP-23 définit le kind `30023` pour le contenu long-form sur Nostr. Contrairement aux notes courtes kind `1`, les événements long-form sont des événements remplaçables paramétrés (indexés par un tag `d`), supportent le formatage Markdown et incluent des tags de métadonnées pour les titres, résumés, images et dates de publication.

## Fonctionnement

Un événement long-form utilise le kind `30023` avec un tag `d` comme identifiant unique, ce qui permet à l'auteur de mettre à jour le contenu en publiant un nouvel événement avec le même tag `d`. Le champ `content` contient du texte Markdown. Les tags standards incluent `title`, `summary`, `image` (URL de l'image d'en-tête), `published_at` (horodatage Unix de publication d'origine) et `t` (hashtags). Comme il s'agit d'un événement remplaçable paramétré, les relays ne stockent que la dernière version par tag `d` et par auteur.

## Tags principaux

- `d` - identifiant unique de l'article (slug)
- `title` - titre de l'article
- `summary` - courte description
- `image` - URL de l'image d'en-tête
- `published_at` - horodatage Unix de publication d'origine (distinct de `created_at`, qui change à chaque modification)
- `t` - tags de hashtag/sujet

## Implémentations

- [Habla](https://habla.news) - Lecteur et éditeur de contenu long-form
- [YakiHonne](https://yakihonne.com) - Plateforme de contenu long-form
- [Highlighter](https://highlighter.com) - Outil de lecture et d'annotation

---

**Sources principales :**
- [Spécification NIP-23](https://github.com/nostr-protocol/nips/blob/master/23.md)

**Voir aussi :**
- [NIP-01 (Protocole de base)](/fr/topics/nip-01/)
