---
title: "NIP-47 : Nostr Wallet Connect"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47 définit un protocole pour connecter les applications Nostr aux portefeuilles Lightning, permettant les paiements sans exposer les identifiants du portefeuille à chaque application.

## Fonctionnement

Un portefeuille (comme Zeus) exécute un service NWC qui écoute les demandes de paiement sur des relais Nostr spécifiques. Les applications se connectent en utilisant une chaîne de connexion qui inclut la clé publique du portefeuille et les informations de relais. Les demandes et réponses de paiement sont chiffrées entre l'application et le portefeuille.

## Cas d'utilisation

- **Zapping** - Envoyer des sats aux posts, profils ou créateurs de contenu
- **Paiements** - Payer des factures Lightning depuis n'importe quelle application Nostr
- **Abonnements** - Paiements récurrents pour du contenu premium

## Fonctionnalités clés

- **Contrôles de budget** - Définir des limites de dépenses par connexion
- **Relais personnalisés** - Utiliser votre propre relais pour la communication du portefeuille
- **Paiements parallèles** - Traiter plusieurs zaps simultanément pour les opérations en lot

---

**Sources principales :**
- [Spécification NIP-47](https://github.com/nostr-protocol/nips/blob/master/47.md)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/fr/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2 : Sorties](/fr/newsletters/2025-12-24-newsletter/#releases)

**Voir aussi :**
- [NIP-57 : Zaps](/fr/topics/nip-57/)

