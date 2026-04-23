---
title: "NIP-57 : Zaps"
date: 2025-12-17
translationOf: /en/topics/nip-57.md
translationDate: 2026-04-22
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

Un client valideur devrait vérifier quatre choses avant d'afficher un reçu comme zap : la signature du reçu doit correspondre au `nostrPubkey` annoncé dans la réponse LNURL du destinataire, le montant de la facture `bolt11` doit correspondre au tag `amount` de la demande embarquée, le hash de description de la facture doit s'engager sur la demande de zap stringifiée, et le `preimage` doit hacher vers le `payment_hash` de la facture. Les clients qui affichent des totaux de zaps sans effectuer ces vérifications sont trivialement falsifiables.

## Zaps privés et anonymes

Les zaps privés ajoutent une couche de confidentialité. L'expéditeur peut chiffrer le `content` de la demande de zap pour le destinataire et inclure un tag `anon` sur la requête externe. Un zap anonyme va plus loin encore : le client génère une nouvelle paire de clés éphémère pour la demande elle-même, de sorte que le reçu prouve qu'un paiement a eu lieu sans relier ce zap à la pubkey longue durée de l'expéditeur.

## Objectifs de zap et splits

NIP-57 sous-tend le système d'objectifs de zap défini dans [NIP-75](/fr/topics/nip-75/). Un objectif est un événement kind `9041` qui déclare une cible de financement et une liste de relays, et les clients calculent sa progression en sommant les montants `bolt11` validés des événements kind `9735` correspondants.

Les zap splits, définis dans une annexe du NIP, permettent à un destinataire de publier un profil kind `0` avec plusieurs tags `zap` pondérés afin qu'un seul zap soit réparti atomiquement entre plusieurs pubkeys. [Amethyst](https://github.com/vitorpamplona/amethyst), [Damus](https://github.com/damus-io/damus) et [noStrudel](https://github.com/hzrd149/nostrudel) implémentent ce paiement réparti de bout en bout.

---

**Sources principales :**
- [Spécification NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/fr/newsletters/2025-12-17-newsletter/)
- [Newsletter #2 : Actualités](/fr/newsletters/2025-12-24-newsletter/)
- [Newsletter #3 : Changements notables de code](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #9 : Mises à jour NIP](/fr/newsletters/2026-02-11-newsletter/)
- [Newsletter #19 : deep dive NIP](/en/newsletters/2026-04-22-newsletter/)

**Voir aussi :**
- [NIP-47 : Nostr Wallet Connect](/fr/topics/nip-47/)
- [NIP-75 : Objectifs de zap](/fr/topics/nip-75/)
- [NIP-53 : Activités en direct](/fr/topics/nip-53/)
