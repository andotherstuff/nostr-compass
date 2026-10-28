---
title: "NIP-03 : attestations OpenTimestamps pour les events"
date: 2026-10-28
translationOf: /en/topics/nip-03.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-03 décrit comment publier une preuve [OpenTimestamps](https://opentimestamps.org/) pour un event Nostr. Cette preuve établit que l’event existait déjà au moment d’un bloc Bitcoin précis.

**Avertissement :** la spécification actuelle porte les étiquettes `draft`, `optional` et `unrecommended`. D’après son en-tête, elle est vulnérable à une attaque bien précise et doit être mise à jour. Le texte ne décrit pas cette attaque. Considérez ce format comme une référence historique et ne l’adoptez pas pour de nouveaux travaux tant que la spécification n’aura pas été révisée.

## Fonctionnement

Chaque preuve est publiée sous la forme d’un event distinct de kind 1040. Son tag `e` désigne l’id de l’event cible, accompagné d’une URL de relay, tandis que son tag `k` consigne le kind de l’event cible. La preuve OpenTimestamps doit prouver l’id de l’event cible lui-même en tant que digest. Cet id n’est pas hashé une seconde fois.

Le `content` contient le fichier `.ots` complet, encodé en base64, avec au moins une attestation Bitcoin. La spécification recommande exactement une attestation et aucune attestation en attente, ces dernières ajoutant des octets sans faciliter la vérification.

Pour vérifier, on récupère l’event de kind 1040, on décode son contenu et on contrôle la preuve par rapport à Bitcoin. Une preuve valide montre que l’id de l’event était déjà engagé au moment du bloc attesté. On obtient ainsi une date de création au plus tard pour l’event, qui ne dépend pas de la valeur `created_at` fournie par l’auteur lui-même. En revanche, elle ne montre pas que le contenu de l’event est véridique.

## Historique

Un [commit du 11 octobre 2023](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e) a modifié l’emplacement des preuves. Auparavant, une preuve était un champ `ots` rattaché à l’event lui-même. Depuis, chaque preuve est un event distinct de kind 1040 qui pointe vers sa cible.

## Sources primaires

- [Spécification NIP-03 actuelle](https://github.com/nostr-protocol/nips/blob/master/03.md)
- [Commit du 11 octobre 2023 déplaçant les preuves vers des events de kind 1040](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e)

## Mentionné dans les newsletters

- [Newsletter #46 (2026-10-28) : octobre 2023, les events portent des preuves et des demandes de travail](/fr/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)

## Voir aussi

- [NIP-01 : protocole de base](/fr/topics/nip-01/)
