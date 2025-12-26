---
title: "NIP-18 : Reposts"
date: 2025-12-17
draft: false
categories:
  - Social
  - Protocol
---

NIP-18 définit comment reposter des événements, similaire aux retweets sur d'autres plateformes.

## Structure

Un repost est un événement kind 6 (pour les notes kind 1) ou kind 16 (repost générique) contenant :
- Un tag `e` référençant l'événement reposté
- Un tag `p` référençant l'auteur original
- Optionnellement, l'événement original complet dans le champ `content`

## Changements récents

Support amélioré pour reposter les événements remplaçables avec le support du tag `a`. Cela permet aux reposts d'événements adressables (kinds 30000-39999) de les référencer par leur adresse plutôt que par un ID d'événement spécifique.

---

**Sources principales :**
- [Spécification NIP-18](https://github.com/nostr-protocol/nips/blob/master/18.md)

**Mentionné dans :**
- [Newsletter #1 : Mises à jour NIP](/fr/newsletters/2025-12-17-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)

