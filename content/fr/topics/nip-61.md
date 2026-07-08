---
title: "NIP-61 : Nutzaps"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-61.md
translationDate: 2026-07-01
categories:
  - Zaps
  - Ecash
---

NIP-61 définit les « nutzaps », des paiements ecash Cashu de pair à pair délivrés sous forme d'événements Nostr. Un expéditeur publie un jeton Cashu verrouillé P2PK adressé à la clé Nostr du destinataire, et le destinataire l'échange auprès de la mint à sa convenance. Les preuves elles-mêmes portent la valeur, donc un paiement NIP-61 arrive sous forme de jeton autonome que le destinataire peut échanger selon son propre calendrier, sans canal Lightning ni négociation interactive requise.

## Comment ça marche

NIP-61 s'appuie sur deux primitives existantes : les portefeuilles Cashu [NIP-60](/fr/topics/nip-60/) et les verrous P2PK de Cashu. Le flux utilise trois kinds d'événements.

**Recommandation de mint (kind 10019) :** un événement remplaçable que le destinataire publie pour annoncer de quelles mints il accepte des nutzaps et la clé publique Cashu utilisée pour verrouiller les preuves à son intention. Les expéditeurs lisent ceci avant d'envoyer afin que le jeton verrouillé soit un que le destinataire peut échanger.

**Événement nutzap (kind 9321) :** le paiement lui-même. Il porte les preuves Cashu (verrouillées P2PK vers le pubkey nutzap du destinataire issu de kind 10019), l'URL de la mint, des tags `e` et `a` optionnels identifiant la note zappée, et un tag `p` pour le destinataire. Le destinataire le reçoit via les abonnements Nostr normaux, déverrouille les preuves avec la clé privée correspondante, et soit les conserve dans son portefeuille NIP-60 soit les fond vers Lightning.

**Info nutzap (kind 7375) :** état mis en cache de la même forme que les événements de jetons NIP-60, enregistrant les preuves de nutzap échangées afin que le portefeuille ne les compte pas en double lors d'une resynchronisation.

## Compromis et modèle de confiance

Un nutzap est un jeton ecash autonome. Tant que le destinataire peut ultérieurement contacter la mint, il peut échanger le paiement. La mint elle-même est le dépositaire de confiance, le même modèle de confiance que NIP-60, et ce choix de garde est le prix explicite des micropaiements à finalité instantanée et capables de fonctionner hors ligne. Les zaps NIP-57 exigent que le récepteur exécute (ou soit hébergé sur) un nœud Lightning avec un point de terminaison LNURL qui accepte les HTLC entrants en temps réel. Les téléphones sans canal Lightning, les utilisateurs derrière des pare-feux et les destinataires qui se trouvent hors ligne sortent tous de ce modèle.

L'annonce kind 10019 est la porte de confiance de la couche sociale. L'expéditeur choisit l'une des mints acceptées par le destinataire, ce qui garde le chemin d'échange du destinataire prévisible. Un expéditeur qui choisit une mint en dehors de l'ensemble du destinataire risque un jeton non échangeable, donc les portefeuilles lisent d'abord kind 10019.

## Flux de travail

1. Le destinataire publie un kind 10019 annonçant les mints acceptées et un pubkey nutzap
2. L'expéditeur lit kind 10019, mint des preuves à l'une des mints listées, et les verrouille P2PK vers le pubkey nutzap du destinataire
3. L'expéditeur publie un kind 9321 avec les preuves verrouillées, l'URL de la mint et les tags cibles
4. Le destinataire reçoit le kind 9321 via son abonnement Nostr normal
5. Le destinataire déverrouille les preuves à l'aide de sa clé privée nutzap et soit les conserve dans son portefeuille NIP-60 soit les fond vers Lightning

## Exemple d'événement nutzap

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1750162800,
  "kind": 9321,
  "tags": [
    ["proof", "{\"amount\":21,\"secret\":\"...\",\"C\":\"...\",\"id\":\"...\"}"],
    ["u", "https://mint.example.com"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3"],
    ["p", "c5d8a4e3b2a1f0e9d8c7b6a5949382716050403020100ffeeddccbbaa99887766"]
  ],
  "content": "Great post!",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

## Implémentations

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) intègre le rendu des nutzaps avec des vues de solde par mint dans sa surface de portefeuille NIP-60/NIP-61 ([PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075))

---

**Sources primaires :**
- [Spécification NIP-61](https://github.com/nostr-protocol/nips/blob/master/61.md)
- [Amethyst PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075) - Prise en charge du portefeuille Cashu NIP-60 et des nutzaps NIP-61

**Mentionné dans :**
- [Newsletter #27 : Amethyst v1.12.0 intègre les portefeuilles Cashu, les nutzaps, un pilote CLINK et l'auto-réparation Tor](/fr/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Voir aussi :**
- [NIP-57 : Zaps](/fr/topics/nip-57/)
- [NIP-60 : Portefeuille Cashu](/fr/topics/nip-60/)
- [Cashu](/fr/topics/cashu/)
