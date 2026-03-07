---
title: "NIP-24 : Champs de métadonnées supplémentaires"
date: 2025-12-17
translationOf: /en/topics/nip-24.md
translationDate: 2026-03-07
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

La spécification marque aussi deux anciens champs comme obsolètes : `displayName` doit devenir `display_name`, et `username` doit devenir `name`. Les clients les voient encore sur le terrain, donc un analyseur tolérant aide la rétrocompatibilité même si un rédacteur ne devrait pas les émettre.

## Tags standards

NIP-24 standardise également des tags à usage général :
- `r` : Référence URL web
- `i` : Identifiant externe
- `title` : Nom pour divers types d'événements
- `t` : Hashtag (doit être en minuscules)

## Pourquoi c'est important

NIP-24 est principalement une question de convergence. Ces champs et tags apparaissaient déjà dans différents clients, et la spécification leur donne des noms et significations cohérents. Cela réduit les petites mais agaçantes incompatibilités comme des clients en désaccord sur le fait qu'une bannière se trouve sous `banner` ou sous une clé spécifique à l'application.

Un point pratique pour les implémenteurs est que kind 0 reste un chemin critique dans la plupart des clients. Les métadonnées supplémentaires doivent rester légères. Si un champ nécessite son propre schéma de récupération ou un cycle de mise à jour indépendant, il appartient probablement à un kind d'événement séparé plutôt que de gonfler les métadonnées de profil.

---

**Sources principales :**
- [Spécification NIP-24](https://github.com/nostr-protocol/nips/blob/master/24.md)

**Mentionné dans :**
- [Newsletter #1 : NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)
