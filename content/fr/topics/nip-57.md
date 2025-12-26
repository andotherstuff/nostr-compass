---
title: "NIP-57 : Zaps"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57 définit les zaps, une façon d'envoyer des paiements Lightning aux utilisateurs Nostr et au contenu avec une preuve cryptographique que le paiement a eu lieu.

## Fonctionnement

1. Le client récupère l'adresse Lightning du destinataire depuis son profil kind 0
2. Le client demande une facture au serveur LNURL du destinataire, incluant un événement de demande de zap
3. L'utilisateur paie la facture
4. Le serveur LNURL publie un reçu de zap kind 9735 aux relais Nostr
5. Les clients affichent le zap sur le contenu du destinataire

## Demande de zap (kind 9734)

La demande de zap est un événement signé qui prouve qui a envoyé le zap et vers quel contenu. Elle inclut :
- Tag `p` avec la clé publique du destinataire
- Tag `e` avec l'événement zappé (optionnel)
- Tag `amount` en millisatoshis
- Tag `relays` listant où publier le reçu

## Reçu de zap (kind 9735)

Publié par le serveur LNURL après confirmation du paiement. Contient :
- La demande de zap originale dans un tag `description`
- Tag `bolt11` avec la facture payée
- Tag `preimage` prouvant le paiement

---

**Sources principales :**
- [Spécification NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/fr/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2 : Actualités](/fr/newsletters/2025-12-24-newsletter/#news)

**Voir aussi :**
- [NIP-47 : Nostr Wallet Connect](/fr/topics/nip-47/)

