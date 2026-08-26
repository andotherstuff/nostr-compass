---
title: "NIP-38 : Statuts d'utilisateur"
date: 2026-08-26
translationOf: /en/topics/nip-38.md
translationDate: 2026-08-26
draft: false
description: "Définit des événements de statut d'utilisateur de courte durée, y compris les catégories de statut général et musical."
---

NIP-38 définit des événements adressables kind 30315 pour de courts statuts d'utilisateur. Un tag `d` identifie la catégorie du statut, comme `general` ou `music`, tandis que des tags `r` et `p` optionnels peuvent renvoyer à une URL ou identifier un artiste. Les clients peuvent utiliser le tag `expiration` de l'événement pour cesser d'afficher les statuts périmés.

## Comment ça fonctionne

Un utilisateur publie un événement kind 30315 avec le texte du statut dans `content`. L'événement est adressable par pubkey, kind et tag `d`, de sorte qu'un événement plus récent de la même catégorie remplace le précédent. Un champ de contenu vide efface ce statut.

---

**Sources primaires :**
- [Spécification NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) - Statuts d'utilisateur

**Mentionné dans :**
- [Newsletter #37 : NoorNote v1.3.6 : statuts de profil et annonces classées](/fr/newsletters/2026-08-26-newsletter/#noornote-v136--statuts-de-profil-et-annonces-classées)
