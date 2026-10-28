---
title: "NIP-06 : dérivation de clés à partir d’un mnémonique"
date: 2026-10-28
translationOf: /en/topics/nip-06.md
translationDate: 2026-10-28
draft: false
categories: ["Identity", "Keys"]
---

NIP-06 décrit comment dériver une paire de clés Nostr à partir d’une phrase mnémonique (seed phrase). Le [texte officiel actuel de NIP-06](https://github.com/nostr-protocol/nips/blob/master/06.md) est marqué comme brouillon et optionnel, et il comporte l’avertissement suivant :

> __Avertissement__ `unrecommended` : préférez une seule nsec

Cette page présente NIP-06 pour des raisons de compatibilité historique. Elle ne recommande pas d’adopter la dérivation à partir d’une seed.

## Fonctionnement

Selon la [spécification actuelle](https://github.com/nostr-protocol/nips/blob/master/06.md), BIP39 sert à générer les mots mnémoniques et à en dériver une seed binaire. BIP32 dérive ensuite les clés le long du chemin `m/44'/1237'/<account>'/0/0`, où 1237 correspond à l’entrée de Nostr dans SLIP44. Un client basique peut utiliser le compte 0. En incrémentant la valeur du compte, on obtient d’autres clés issues de la même seed. Deux implémentations ne reproduisent la même identité que si elles s’accordent sur les étapes de dérivation et utilisent les bons encodages pour le résultat.

## Vecteurs de test

Un [commit du 12 octobre 2023](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b) a ajouté deux vecteurs de test, l’un construit à partir d’un mnémonique de 12 mots, l’autre à partir d’un mnémonique de 24 mots. Chacun indique la clé privée et la clé publique attendues en hexadécimal, ainsi que les encodages nsec et npub correspondants. Les développeurs peuvent s’en servir pour comparer leurs implémentations entre elles. Ces vecteurs ne disent rien de la garde des clés, ne certifient pas la sécurité et ne garantissent pas une interopérabilité universelle.

## Voir aussi

- [NIP-01](/fr/topics/nip-01/)

**Sources primaires :**

- [NIP-06 (version actuelle)](https://github.com/nostr-protocol/nips/blob/master/06.md)
- [Commit ajoutant les vecteurs de test de NIP-06 (12 octobre 2023)](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b)

**Mentionné dans :**

- [Newsletter #46](/fr/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)
