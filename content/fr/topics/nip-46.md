---
title: "NIP-46 : Nostr Connect"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46 définit la signature distante, permettant à une application de signature de détenir les clés tandis que les clients demandent des signatures via les relais Nostr.

## Fonctionnement

1. Le signer génère un URI de connexion (`bunker://` ou `nostrconnect://`)
2. L'utilisateur colle l'URI dans un client
3. Le client envoie des demandes de signature comme événements chiffrés au relais du signer
4. Le signer demande l'approbation de l'utilisateur, renvoie les événements signés

## Méthodes de connexion

- **bunker://** - Connexion initiée par le signer
- **nostrconnect://** - Connexion initiée par le client via code QR ou deep link

## Opérations supportées

- `sign_event` - Signer un événement arbitraire
- `get_public_key` - Récupérer la clé publique du signer
- `nip04_encrypt/decrypt` - Opérations de chiffrement NIP-04
- `nip44_encrypt/decrypt` - Opérations de chiffrement NIP-44

---

**Sources principales :**
- [Spécification NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Mentionné dans :**
- [Newsletter #1 : Changements notables de code](/fr/newsletters/2025-12-17-newsletter/#amethyst-android)

**Voir aussi :**
- [NIP-55 : Android Signer](/fr/topics/nip-55/)

