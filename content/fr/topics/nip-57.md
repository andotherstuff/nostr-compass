---
title: "NIP-57 : Zaps"
date: 2025-12-17
translationOf: /en/topics/nip-57.md
translationDate: 2026-03-07
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57 définit les zaps, un moyen d'associer des paiements Lightning aux identités et au contenu Nostr. Il standardise à la fois la demande de facture compatible zap et l'événement de reçu que les portefeuilles publient après le paiement.

## Fonctionnement

1. Le client découvre le point de terminaison LNURL du destinataire depuis les métadonnées de profil ou un tag `zap` sur l'événement cible.
2. Le client envoie une demande de zap signée kind `9734` au callback LNURL du destinataire, pas aux relays.
3. L'utilisateur paie la facture.
4. Le serveur du portefeuille du destinataire publie un reçu de zap kind `9735` aux relays listés dans la demande de zap.
5. Les clients valident et affichent le zap.

## Demande de zap (kind 9734)

La demande de zap est un événement signé qui identifie le payeur et la cible prévue. Elle inclut généralement :

- Tag `p` avec la pubkey du destinataire
- Tag `e` avec l'événement zappé (optionnel)
- Tag `amount` en millisatoshis
- Tag `relays` listant où publier le reçu

Le contenu adressable peut utiliser un tag `a` au lieu de, ou en complément d'un tag `e`. Le tag optionnel `k` enregistre le kind cible.

## Reçu de zap (kind 9735)

Publié par le serveur du portefeuille du destinataire après confirmation du paiement. Il contient :

- La demande de zap originale dans un tag `description`
- Tag `bolt11` avec la facture payée
- Tag `preimage` prouvant le paiement

Les clients doivent valider le reçu par rapport au `nostrPubkey` LNURL du destinataire, au montant de la facture et à la demande de zap originale. Un reçu sans cette validation n'est qu'une affirmation.

## Confiance et compromis

Les zaps sont utiles parce qu'ils rendent les paiements visibles dans le graphe social, mais le reçu est toujours créé par l'infrastructure du portefeuille du destinataire. La spécification elle-même note qu'un reçu de zap n'est pas une preuve universelle de paiement. Il est préférable de le comprendre comme une déclaration signée par un portefeuille attestant qu'une facture liée à une demande de zap a été payée.

---

**Sources principales :**
- [Spécification NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2 : Actualités](/en/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #3 : Changements notables de code](/en/newsletters/2025-12-31-newsletter/#amethyst-android)
- [Newsletter #9 : Mises à jour NIP](/en/newsletters/2026-02-11-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-47 : Nostr Wallet Connect](/fr/topics/nip-47/)
