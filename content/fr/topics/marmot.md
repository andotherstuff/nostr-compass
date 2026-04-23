---
title: "Protocole Marmot"
date: 2025-12-17
translationOf: /en/topics/marmot.md
translationDate: 2026-04-22
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

Le protocole reste expérimental, mais il dispose maintenant de plusieurs implémentations et d'une utilisation active dans des applications. [MDK](https://github.com/marmot-protocol/mdk) est la pile de référence principale en Rust, [marmot-ts](https://github.com/marmot-protocol/marmot-ts) apporte le modèle en TypeScript, et des applications comme [White Noise](https://github.com/marmot-protocol/whitenoise), [Amethyst](https://github.com/vitorpamplona/amethyst), Pika et Vector utilisent des composants compatibles Marmot.

Les travaux récents se sont concentrés sur le durcissement et l'interopérabilité. Des correctifs issus d'audit ont atterri début 2026, et MIP-03 a introduit une résolution déterministe des commits pour que les clients puissent converger lorsque des changements d'état de groupe concurrents se croisent sur les relays.

En avril 2026, Amethyst a aligné son MDK embarqué sur les formats wire MIP-01 et MIP-05 : la [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) a ajouté l'encodage VarInt des préfixes de longueur de style TLS et la validation aller-retour contre les vecteurs de test MDK, la [PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) a ajouté le support de MIP-00 KeyPackage Relay List, et la [PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436) a comblé les dernières lacunes côté admin-gate et gestion des médias signalées par les tests inter-clients contre White Noise. La [PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466) a corrigé le framing des commits MLS afin que les bytes de welcome chiffrés correspondent à la sortie de mdk-core, et la [PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471) a corrigé un bug de déchiffrement de couche externe qui causait une divergence d'état entre co-admins. La [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493) ajoute ensuite une validation cryptographique complète des commits MLS, et la [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) livre `amy`, une interface CLI pour les opérations de groupe Marmot et MLS pilotée depuis l'implémentation d'Amethyst.

MDK a livré la [PR #261](https://github.com/marmot-protocol/mdk/pull/261) pour calculer `RequiredCapabilities` d'un groupe comme le LCD des capacités des invités, ce qui débloque les invitations entre versions mixtes entre Amethyst et White Noise, la [PR #262](https://github.com/marmot-protocol/mdk/pull/262) pour parser les KeyPackages des invités avant de persister le signer du créateur, la [PR #264](https://github.com/marmot-protocol/mdk/pull/264) pour faire converger le format wire de SelfUpdate entre implémentations, et la [PR #265](https://github.com/marmot-protocol/mdk/pull/265) pour exposer un accesseur `group_required_proposals`.

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) est au milieu d'un refactor multi-phase qui remplace les singletons globaux par des vues `AccountSession` par compte : la [PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743) a posé le squelette `AccountSession` et `AccountManager`, puis les phases suivantes ont migré les handles relay, les brouillons et paramètres, les opérations de message, la lecture et écriture de groupes, l'appartenance, les notifications push, les lectures de KeyPackage, la création de groupes et, depuis la [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770), le dispatch d'événements à portée de session. La [PR #68 de marmot-ts](https://github.com/marmot-protocol/marmot-ts/pull/68) migre quant à elle le client TypeScript vers les KeyPackages adressables kind `30443`.

---

**Sources principales :**
- [Dépôt du protocole Marmot](https://github.com/marmot-protocol/marmot)
- [Protocole MLS](https://messaginglayersecurity.rocks/)
- [Marmot Development Kit](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)
- [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)
- [Client White Noise](https://github.com/marmot-protocol/whitenoise)
- [Amethyst PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) - Alignement du format wire MIP-01/MIP-05
- [Amethyst PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) - MIP-00 KeyPackage Relay List
- [Amethyst PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) - CLI Amy

**Mentionné dans :**
- [Newsletter #1 : Actualités](/fr/newsletters/2025-12-17-newsletter/)
- [Newsletter #1 : Sorties](/fr/newsletters/2025-12-17-newsletter/)
- [Newsletter #4](/fr/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/fr/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/fr/newsletters/2026-03-04-newsletter/)
- [Newsletter #19 : conformité MIP d'Amethyst](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19 : travail d'interop MDK](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19 : refactor session de whitenoise-rs](/en/newsletters/2026-04-22-newsletter/)

**Voir aussi :**
- [MLS (Message Layer Security)](/fr/topics/mls/)
- [MIP-05 : Notifications push préservant la vie privée](/fr/topics/mip-05/)
- [NIP-17 : Messages directs privés](/fr/topics/nip-17/)
- [NIP-59 : Gift Wrap](/fr/topics/nip-59/)
