---
title: "NIP-69 : Trading pair-à-pair"
date: 2025-12-17
translationOf: /en/topics/nip-69.md
translationDate: 2026-03-07
draft: false
categories:
  - Trading
  - Protocol
---

NIP-69 définit un protocole pour le trading pair-à-pair sur Nostr, créant un carnet d'ordres unifié à travers plusieurs plateformes plutôt que des pools de liquidité fragmentés.

## Fonctionnement

NIP-69 utilise des événements adressables kind 38383 pour les ordres d'achat et de vente. Le format adressable est important parce qu'un ordre peut traverser plusieurs états au fil du temps tout en conservant la même identité logique grâce à son tag `d`.

## Structure des ordres

Les ordres utilisent des tags pour spécifier les paramètres de trade :

- `d` - identifiant de l'ordre
- `k` - type d'ordre (achat/vente)
- `f` - devise fiat (code ISO 4217)
- `amt` - montant Bitcoin en satoshis
- `fa` - montant fiat
- `pm` - méthodes de paiement acceptées
- `premium` - pourcentage de prime/remise sur le prix
- `network` - réseau Bitcoin (mainnet, testnet, signet, regtest)
- `layer` - couche de règlement (onchain, lightning, liquid)
- `expiration` - date d'expiration de l'ordre

## Cycle de vie de l'ordre

Les ordres progressent à travers différents statuts :
- `pending` - ouvert et disponible pour correspondance
- `in-progress` - trade initié avec une contrepartie
- `success` - trade complété
- `canceled` - retiré par le maker
- `expired` - temps d'expiration dépassé

La spécification distingue deux limites de temps. `expires_at` indique quand un ordre en attente ne devrait plus être considéré comme ouvert, tandis que `expiration` donne aux relais un timestamp qu'ils peuvent utiliser avec [NIP-40](/fr/topics/nip-40/) pour supprimer entièrement les événements d'ordres périmés.

## Pourquoi c'est important

NIP-69 est un projet d'interopérabilité. Mostro, lnp2pBot, RoboSats, Peach et d'autres systèmes de trading P2P peuvent exposer leurs ordres dans un format d'événement partagé unique au lieu de garder la liquidité piégée dans des applications séparées.

Le tag optionnel `g` rend aussi possible le trading local en face-à-face sans modifier le reste du schéma d'ordre. C'est utile parce que les trades en espèces locaux nécessitent un filtrage géographique, alors que les trades Lightning en ligne n'en ont pas besoin.

## Sécurité et confiance

Le tag `bond` spécifie un dépôt de garantie que les deux parties doivent payer, fournissant une protection contre l'abandon ou la fraude.

Cela ne supprime pas le risque de contrepartie. Les litiges de paiement, la fraude fiat, la réputation et les règles de garde restent au niveau de la couche applicative. NIP-69 standardise la publication des ordres, pas la résolution des litiges.

---

**Sources primaires :**
- [Spécification NIP-69](https://github.com/nostr-protocol/nips/blob/master/69.md)
- [Spécification du protocole Mostro](https://mostro.network/protocol/)

**Mentionné dans :**
- [Newsletter #1 : NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #1 : Releases](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2 : News](/en/newsletters/2025-12-24-newsletter/#news)

**Voir aussi :**
- [NIP-40 : Expiration Timestamp](/fr/topics/nip-40/)
