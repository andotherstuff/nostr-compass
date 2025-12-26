---
title: "BUD-03 : Liste de serveurs utilisateur"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-03 définit comment les utilisateurs publient leurs serveurs Blossom préférés, permettant aux clients de découvrir où télécharger et récupérer les fichiers média d'un utilisateur.

## Fonctionnement

Les utilisateurs publient un événement kind 10063 listant leurs serveurs Blossom. Les clients peuvent alors :
- Télécharger des médias vers les serveurs préférés de l'utilisateur
- Découvrir où trouver les blobs d'un utilisateur quand on leur donne leur clé publique

Cela permet la découverte basée sur l'auteur comme alternative à l'intégration directe des URLs de serveur dans le contenu.

---

**Sources principales :**
- [Spécification BUD-03](https://github.com/hzrd149/blossom/blob/master/buds/03.md)

**Voir aussi :**
- [Protocole Blossom](/fr/topics/blossom/)
- [NIP-51 : Listes](/fr/topics/nip-51/)

