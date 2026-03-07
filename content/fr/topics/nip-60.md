---
title: "NIP-60 : Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2026-03-07
draft: false
categories:
  - Wallet
  - Ecash
---

NIP-60 définit comment les portefeuilles ecash basés sur Cashu fonctionnent au sein de Nostr. Les informations du portefeuille sont stockées sur les relays, permettant des portefeuilles portables qui fonctionnent à travers différentes applications sans nécessiter de comptes séparés.

## Fonctionnement

NIP-60 utilise trois types d'événements principaux stockés sur les relays, plus un événement auxiliaire optionnel pour les devis en attente :

**Événement de portefeuille (kind 17375) :** un événement remplaçable contenant la configuration chiffrée du portefeuille, incluant les URLs de mint et une clé privée pour recevoir des paiements. Cette clé est distincte de la clé d'identité Nostr de l'utilisateur.

**Événements de token (kind 7375) :** stockent les preuves Cashu non dépensées et chiffrées. Lorsque les preuves sont dépensées, le client supprime l'ancien événement et en crée un nouveau avec les preuves restantes.

**Historique des dépenses (kind 7376) :** enregistrements optionnels de transactions montrant les mouvements de fonds, avec un contenu chiffré et des références aux événements de tokens créés/détruits.

**Événements de devis (kind 7374) :** état chiffré optionnel pour les devis de mint en attente. La spécification recommande des événements de courte durée avec des tags d'expiration, principalement pour les cas où l'état local ne suffit pas.

## Modèle d'état

NIP-60 concerne la synchronisation de l'état du portefeuille, pas l'acte de recevoir de l'argent. L'événement de portefeuille indique à un client quels mints et quelle clé utiliser, tandis que les événements de token constituent l'état réel du solde car ils contiennent les preuves non dépensées.

Cette distinction est importante pour l'interopérabilité. Deux clients ne peuvent afficher le même portefeuille que s'ils interprètent le renouvellement des tokens de la même manière : dépenser les preuves, publier les preuves de remplacement, et supprimer l'événement de token dépensé via [NIP-09](/fr/topics/nip-09/) pour que les autres clients ne comptent pas les preuves dépensées comme solde.

## Pourquoi c'est important

- **Facilité d'utilisation** : les nouveaux utilisateurs peuvent recevoir des ecash immédiatement sans configuration de compte externe
- **Interopérabilité** : les données du portefeuille suivent les utilisateurs à travers différentes applications Nostr
- **Confidentialité** : toutes les données du portefeuille sont chiffrées avec les clés de l'utilisateur
- **Gestion des preuves** : suit les transitions d'état du portefeuille pour que les clients convergent vers le même solde

## Notes d'interopérabilité

Les clients cherchent d'abord les informations de relay du portefeuille via kind 10019 et se rabattent sur la liste de relays [NIP-65](/fr/topics/nip-65/) de l'utilisateur si aucune liste dédiée de relays de portefeuille n'est présente. Ce repli est utile, mais il signifie aussi que la portabilité du portefeuille dépend encore des relays qui stockent et servent effectivement les événements chiffrés du portefeuille.

La spécification exige aussi que la clé privée du portefeuille reste distincte de la clé d'identité Nostr de l'utilisateur. Cela isole la gestion de la réception du portefeuille de la clé de signature principale et réduit le risque qu'une clé soit réutilisée pour deux usages différents.

## Flux de travail

1. Le client récupère la configuration du portefeuille depuis les relays du portefeuille ou la liste de relays de l'utilisateur
2. Les événements de token sont chargés et déchiffrés pour obtenir les fonds disponibles
3. Dépenser crée de nouveaux événements de token et supprime les anciens
4. Les événements d'historique optionnels enregistrent les transactions pour référence de l'utilisateur

---

**Sources principales :**
- [Spécification NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Mentionné dans :**
- [Newsletter #3 : Récapitulatif de décembre](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #9 : Plongée approfondie NIP](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)

**Voir aussi :**
- [NIP-57 : Zaps](/fr/topics/nip-57/)
- [NIP-09 : Demande de suppression d'événement](/fr/topics/nip-09/)
- [NIP-47 : Nostr Wallet Connect](/fr/topics/nip-47/)
