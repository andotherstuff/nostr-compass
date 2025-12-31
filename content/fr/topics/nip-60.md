---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2025-12-31
draft: false
categories:
  - Portefeuille
  - Ecash
---

NIP-60 définit comment les portefeuilles ecash basés sur Cashu fonctionnent au sein de Nostr. Les informations du portefeuille sont stockées sur les relays, permettant des portefeuilles portables qui fonctionnent à travers différentes applications sans nécessiter de comptes séparés.

## Fonctionnement

NIP-60 utilise trois types d'événements stockés sur les relays :

**Événement de Portefeuille (kind 17375) :** Un événement remplaçable contenant la configuration chiffrée du portefeuille, incluant les URLs de mint et une clé privée pour recevoir des paiements. Cette clé est séparée de la clé d'identité Nostr de l'utilisateur.

**Événements de Token (kind 7375) :** Stockent les preuves Cashu non dépensées et chiffrées. Lorsque les preuves sont dépensées, le client supprime l'ancien événement et en crée un nouveau avec les preuves restantes.

**Historique des Dépenses (kind 7376) :** Enregistrements optionnels de transactions montrant les mouvements de fonds, avec un contenu chiffré et des références aux événements de tokens créés/détruits.

## Caractéristiques Principales

- **Facilité d'utilisation** - Les nouveaux utilisateurs peuvent recevoir des ecash immédiatement sans configuration de compte externe
- **Interopérabilité** - Les données du portefeuille suivent les utilisateurs à travers différentes applications Nostr
- **Confidentialité** - Toutes les données du portefeuille sont chiffrées avec les clés de l'utilisateur
- **Gestion des preuves** - Suit quels événements de token ont été dépensés pour éviter la double dépense

## Flux de Travail

1. Le client récupère la configuration du portefeuille depuis les relays
2. Les événements de token sont chargés et déchiffrés pour obtenir les fonds disponibles
3. Dépenser crée de nouveaux événements de token et supprime les anciens
4. Les événements d'historique optionnels enregistrent les transactions pour référence de l'utilisateur

---

**Sources primaires :**
- [Spécification NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Mentionné dans :**
- [Newsletter #3 : Récapitulatif de Décembre](/fr/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Voir aussi :**
- [NIP-57 : Zaps](/fr/topics/nip-57/)
- [NIP-47 : Nostr Wallet Connect](/fr/topics/nip-47/)
