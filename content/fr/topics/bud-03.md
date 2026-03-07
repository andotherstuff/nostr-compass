---
title: "BUD-03 : Liste de serveurs utilisateur"
date: 2025-12-17
translationOf: /en/topics/bud-03.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

BUD-03 définit comment un utilisateur publie ses serveurs Blossom préférés, afin que les clients sachent où téléverser les blobs et où chercher quand une URL média cesse de fonctionner.

## Fonctionnement

Les utilisateurs publient un événement remplaçable de kind `10063` contenant un ou plusieurs tags `server`. Chaque tag contient une URL complète de serveur Blossom.

Les clients peuvent alors :
- téléverser des blobs vers les serveurs préférés de l'utilisateur
- découvrir les emplacements probables des blobs à partir de la clé publique de l'auteur
- réessayer la récupération depuis les serveurs listés quand une URL plus ancienne ne fonctionne plus

## Détails utiles pour le lecteur

L'ordre des tags `server` compte. La spécification indique que les utilisateurs doivent lister leurs serveurs les plus fiables en premier, et les clients doivent au minimum essayer le premier serveur pour les téléversements. BUD-03 n'est donc pas seulement un annuaire, c'est aussi un signal de préférence faible.

La recommandation pour la récupération est aussi pratique : quand un client extrait un hash de blob d'une URL, il doit utiliser la dernière chaîne hexadécimale de 64 caractères dans le chemin. Cela aide les clients à récupérer des blobs à la fois depuis des URL Blossom standard et des URL de type CDN non standard qui intègrent tout de même le hash.

---

**Sources principales :**
- [Spécification BUD-03](https://github.com/hzrd149/blossom/blob/master/buds/03.md)
- [Dépôt Blossom](https://github.com/hzrd149/blossom)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/en/newsletters/2025-12-17-newsletter/#news)

**Voir aussi :**
- [Protocole Blossom](/fr/topics/blossom/)
- [NIP-51 : Listes](/fr/topics/nip-51/)
