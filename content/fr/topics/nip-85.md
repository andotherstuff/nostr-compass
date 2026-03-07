---
title: "NIP-85 : Trusted Assertions"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---

NIP-85 définit les Trusted Assertions, un système pour déléguer des calculs coûteux à des fournisseurs de services de confiance qui publient les résultats signés sous forme d'événements Nostr.

## Fonctionnement

Les scores de Web of Trust, les métriques d'engagement et d'autres valeurs calculées nécessitent de parcourir de nombreux relays et de traiter de grands volumes d'événements. Ce travail est impraticable sur les appareils mobiles. NIP-85 permet à des fournisseurs spécialisés d'effectuer ces calculs et de publier des résultats que les clients peuvent interroger.

Les Trusted Assertions sont des événements adressables. Le tag `d` identifie le sujet évalué, et le kind de l'événement identifie le type de sujet : pubkeys (30382), événements classiques (30383), événements adressables (30384), et identifiants NIP-73 (30385).

Les utilisateurs déclarent les fournisseurs auxquels ils font confiance via kind 10040. Ces listes de fournisseurs peuvent être publiques dans les tags ou chiffrées dans le contenu de l'événement avec [NIP-44](/fr/topics/nip-44/), ce qui compte lorsqu'un utilisateur ne souhaite pas exposer publiquement ses choix de confiance.

## Pourquoi c'est important

L'apport de NIP-85 est qu'il standardise les sorties, pas les algorithmes. Deux fournisseurs peuvent tous deux publier un tag `rank` pour la même pubkey en utilisant des formules de Web of Trust différentes, des traitements de mute différents, des couvertures relay différentes ou des heuristiques anti-spam différentes. Les clients restent interopérables car le format de résultat correspond même quand le calcul diffère.

C'est une meilleure approche pour Nostr que de prétendre qu'il y aura un service de classement canonique unique. Les utilisateurs choisissent les assertions auxquelles ils font confiance.

## Modèle de confiance

Les fournisseurs de services doivent signer leurs propres événements d'assertion, et la spécification recommande des clés de service distinctes pour des algorithmes différents ou des points de vue spécifiques à un utilisateur. Cela empêche un fournisseur de fusionner des systèmes de classement non liés sous une seule identité opaque.

La confiance reste locale. Une sortie signée prouve quel fournisseur a publié un score, pas que le score est correct. Les clients ont besoin de politiques sur les clés de fournisseur à utiliser, les relays à interroger, et la façon de gérer les assertions contradictoires.

## Notes d'interopérabilité

NIP-85 va au-delà des personnes et des publications. Kind 30385 permet aux fournisseurs d'évaluer des identifiants externes NIP-73 tels que des livres, sites web, hashtags et lieux. Cela ouvre la voie à des données de réputation et d'engagement interopérables autour de sujets extérieurs à Nostr.

---

**Sources primaires :**
- [Spécification NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #2223](https://github.com/nostr-protocol/nips/pull/2223) - Orientations sur la découvrabilité des fournisseurs de services

**Mentionné dans :**
- [Newsletter #10 : NIP-85 Deep Dive](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #11 : NIP-85 Service Provider Discoverability](/en/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #12 : Protocol Recap](/en/newsletters/2026-03-04-newsletter/)

**Voir aussi :**
- [NIP-44 : Encrypted Payloads](/fr/topics/nip-44/)
- [NIP-73 : External Content IDs](/fr/topics/nip-73/)
- [Web of Trust](/fr/topics/web-of-trust/)
