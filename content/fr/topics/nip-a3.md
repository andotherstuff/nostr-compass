---
title: "NIP-A3: Cibles de paiement"
date: 2026-09-09
translationOf: /en/topics/nip-a3.md
translationDate: 2026-09-11
draft: false
categories:
  - Protocol
  - Payments
---

NIP-A3 définit un moyen portable permettant à un compte Nostr de publier des adresses de paiement pour plusieurs réseaux et services. Un événement remplaçable de kind `10133` contient une ou plusieurs balises `payto`.

## Fonctionnement

Chaque balise prend la forme `["payto", "<type>", "<address>"]`. Le type est en minuscules, par exemple `bitcoin`, `lightning` ou `monero`. Les clients peuvent valider les formats connus et générer un URI de paiement natif lorsqu’il en existe un. Pour les types inconnus, ils utilisent par défaut le schéma d’URI `payto:` défini par la RFC 8905.

L’événement déclare des destinations, et non un paiement effectué ou un zap Nostr. Les clients décident toujours des types de paiement qu’ils prennent en charge, de la manière de valider une adresse et de la clarté avec laquelle afficher la destination avant de la transmettre à un portefeuille.

## Implémentations

- [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041) propose un transfert facultatif vers le paiement lorsqu’il reconnaît une cible compatible.
- [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851) associe les types de cibles autorisés à des URI de paiement.
- [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) valide les cibles Monero et interroge les relais de l’auteur.

---

**Sources principales :**
- [Spécification NIP-A3](https://github.com/nostr-protocol/nips/blob/master/A3.md)
- [RFC 8905 : le schéma d’URI payto](https://www.rfc-editor.org/rfc/rfc8905.html)

**Mentionné dans :**
- [Newsletter nº 39 : les cibles de paiement NIP-A3 sont prises en charge par trois clients](/fr/newsletters/2026-09-09-newsletter/#nip-a3-payment-targets-reach-three-clients)

**Voir aussi :**
- [NIP-47 : Nostr Wallet Connect](/fr/topics/nip-47/)
