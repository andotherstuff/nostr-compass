---
title: "NIP-55 : Application de signature Android"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55 définit comment les applications Android peuvent demander des opérations de signature à une application de signature dédiée, permettant aux utilisateurs de garder leurs clés privées dans un seul emplacement sécurisé tout en utilisant plusieurs clients Nostr.

## Fonctionnement

NIP-55 utilise l'interface content provider d'Android pour exposer les opérations de signature. Une application de signature s'enregistre comme content provider, et d'autres applications Nostr peuvent demander des signatures sans jamais accéder directement à la clé privée.

Le flux :
1. L'application cliente appelle le content provider du signer
2. Le signer affiche l'interface d'approbation à l'utilisateur
3. L'utilisateur approuve ou refuse la demande
4. Le signer renvoie la signature (ou le rejet) au client

## Opérations clés

- **get_public_key** - Récupérer la clé publique de l'utilisateur (appeler une fois lors de la connexion initiale)
- **sign_event** - Signer un événement Nostr
- **nip04_encrypt/decrypt** - Chiffrer ou déchiffrer les messages NIP-04
- **nip44_encrypt/decrypt** - Chiffrer ou déchiffrer les messages NIP-44

## Initiation de connexion

Une erreur d'implémentation courante est d'appeler `get_public_key` répétitivement depuis des processus en arrière-plan. La spécification recommande de l'appeler seulement une fois lors de la configuration de connexion initiale, puis de mettre le résultat en cache.

---

**Sources principales :**
- [Spécification NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Mentionné dans :**
- [Newsletter #1 : Sorties](/fr/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2 : Actualités](/fr/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #2 : Mises à jour NIP](/fr/newsletters/2025-12-24-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-46 : Nostr Connect](/fr/topics/nip-46/)

