---
title: "NIP-24 : Champs de métadonnées supplémentaires"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
---

NIP-24 définit des champs optionnels supplémentaires pour les métadonnées utilisateur kind 0 au-delà du nom, about et picture de base.

## Champs de métadonnées supplémentaires

- **display_name** : Un nom alternatif, plus grand avec des caractères plus riches que `name`
- **website** : Une URL web liée à l'auteur de l'événement
- **banner** : URL vers une image large (~1024x768) pour un affichage de fond optionnel
- **bot** : Booléen indiquant que le contenu est entièrement ou partiellement automatisé
- **birthday** : Objet avec des champs optionnels année, mois et jour

## Tags standards

NIP-24 standardise également des tags à usage général :
- `r` : Référence URL web
- `i` : Identifiant externe
- `title` : Nom pour divers types d'événements
- `t` : Hashtag (doit être en minuscules)

---

**Sources principales :**
- [Spécification NIP-24](https://github.com/nostr-protocol/nips/blob/master/24.md)

**Mentionné dans :**
- [Newsletter #1 : Mises à jour NIP](/fr/newsletters/2025-12-17-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)

