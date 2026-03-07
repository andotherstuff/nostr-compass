---
title: "MIP-05 : Notifications push préservant la vie privée"
date: 2025-12-17
translationOf: /en/topics/mip-05.md
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---

MIP-05 définit un protocole de notifications push pour les clients Marmot qui tente de préserver la vie privée dans un contexte où les systèmes push mobiles classiques exposent généralement les jetons d'appareil et les relations entre comptes.

## Fonctionnement

- Les jetons d'appareil sont chiffrés avec ECDH+HKDF et ChaCha20-Poly1305
- Les clés éphémères empêchent la corrélation entre les notifications
- Un protocole de propagation à trois événements (kinds 447-449) synchronise les jetons chiffrés entre les membres du groupe
- Les jetons leurres via l'emballage NIP-59 gift wrap cachent la taille des groupes

## Modèle de confidentialité

- Les serveurs de notifications push ne peuvent pas identifier les utilisateurs
- L'appartenance au groupe n'est pas révélée par les schémas de notification
- Les jetons d'appareil ne peuvent pas être corrélés entre les messages

L'amélioration concrète est que le fournisseur push voit des jetons de livraison opaques, pas une correspondance directe entre membre du groupe et appareil. Cela ne rend pas les notifications anonymes au sens absolu, mais réduit ce que la couche push apprend par défaut.

## Kinds d'événements

- **Kind 447** : publication de jeton d'appareil chiffré
- **Kind 448** : demande de synchronisation de jeton
- **Kind 449** : réponse de synchronisation de jeton

## Compromis

MIP-05 ajoute de la confidentialité en ajoutant du travail de coordination. Les clients doivent synchroniser l'état des jetons chiffrés entre les membres du groupe, et les jetons leurres augmentent intentionnellement la surcharge de messages.

Cela signifie que les implémenteurs doivent trouver un équilibre entre la fiabilité de la livraison et la protection des métadonnées. Le protocole est utile précisément parce qu'il traite le push comme un problème de vie privée, pas simplement comme une commodité de transport.

---

**Sources principales :**
- [Spécification MIP-05](https://github.com/marmot-protocol/marmot/blob/master/05.md)
- [MIP-05 PR](https://github.com/marmot-protocol/marmot/pull/18)
- [White Noise v0.2.1 release](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/fr/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3 : Rétrospective de décembre](/fr/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Voir aussi :**
- [Protocole Marmot](/fr/topics/marmot/)
- [NIP-59 : Gift Wrap](/fr/topics/nip-59/)
