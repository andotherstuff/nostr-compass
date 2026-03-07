---
title: "Protocole Marmot"
date: 2025-12-17
translationOf: /en/topics/marmot.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot est un protocole de messagerie de groupe chiffrée de bout en bout sur Nostr. Il combine l'identité et le réseau de relais de Nostr avec MLS pour la gestion des clés de groupe, la confidentialité persistante et la sécurité post-compromission.

## Fonctionnement

Marmot utilise Nostr pour l'identité, le transport par relais et la distribution d'événements, puis ajoute MLS par-dessus pour les changements de membres et le chiffrement des messages. Contrairement à [NIP-17](/fr/topics/nip-17/), qui se concentre sur la messagerie un-à-un, Marmot est conçu pour les groupes où les membres rejoignent, quittent ou font tourner leurs clés au fil du temps.

## Pourquoi c'est important

MLS donne à Marmot des propriétés que les schémas de messages directs de Nostr ne fournissent pas seuls : évolution de l'état du groupe, sémantique de retrait des membres et récupération après compromission grâce aux mises à jour ultérieures des clés.

Cette répartition des responsabilités est l'idée utile. Nostr résout l'identité et le transport dans un réseau ouvert. MLS résout l'accord de clés de groupe authentifié. Marmot est la couche de liaison entre les deux.

## État de l'implémentation

Le protocole reste expérimental, mais il dispose maintenant de plusieurs implémentations et d'une utilisation active dans des applications. MDK est la pile de référence principale en Rust, `marmot-ts` apporte le modèle en TypeScript, et des applications comme White Noise, Pika et Vector utilisent des composants compatibles Marmot.

Les travaux récents se sont concentrés sur le renforcement et l'interopérabilité. Des correctifs issus d'audit ont été intégrés début 2026, et MIP-03 a introduit la résolution déterministe des commits pour que les clients puissent converger lorsque des changements d'état de groupe concurrents se croisent sur les relais.

---

**Sources principales :**
- [Dépôt du protocole Marmot](https://github.com/marmot-protocol/marmot)
- [NIP-104 : Messagerie de groupe chiffrée basée sur MLS](/fr/topics/nip-104/)
- [Marmot Development Kit](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/fr/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1 : Sorties](/fr/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #4](/fr/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/fr/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/fr/newsletters/2026-03-04-newsletter/)

**Voir aussi :**
- [MLS (Message Layer Security)](/fr/topics/mls/)
- [MIP-05 : Notifications push préservant la vie privée](/fr/topics/mip-05/)
- [NIP-17 : Messages directs privés](/fr/topics/nip-17/)
- [NIP-59 : Gift Wrap](/fr/topics/nip-59/)
