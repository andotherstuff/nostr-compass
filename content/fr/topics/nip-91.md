---
title: "NIP-91 : Opérateur AND pour les filtres"
date: 2026-03-04
translationOf: /en/topics/nip-91.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Protocol
---

NIP-91 ajoute une sémantique de filtre AND pour les tableaux de tags dans les abonnements aux relais Nostr. Il a été fusionné le 2026-03-03 après que des implémentations sont apparues dans plusieurs relais.

## Le problème

Le système de filtres de Nostr ([NIP-01](/fr/topics/nip-01/)) combine plusieurs valeurs au sein d'un même filtre de tag en utilisant une logique OR. Si un client spécifie deux valeurs de tag `p` dans un filtre, le relais renvoie les événements correspondant à l'une ou l'autre des pubkeys. Il n'existait aucun moyen de demander des événements référençant les deux pubkeys simultanément.

Cela obligeait les clients à récupérer trop d'événements auprès des relais et à filtrer localement, augmentant l'utilisation de la bande passante et le temps de traitement.

## Fonctionnement

NIP-91 introduit une sémantique AND pour les tableaux de tags. Lorsqu'un client a besoin d'événements correspondant à toutes les valeurs de tags spécifiées, il peut opter pour un matching par intersection au lieu du comportement d'union par défaut.

C'est pertinent pour des requêtes comme "événements qui taguent les deux participants d'une conversation" ou "événements portant deux labels requis à la fois". Avant ce changement, les relais ne pouvaient répondre qu'avec l'ensemble plus large et laisser l'intersection précise au client.

## Pourquoi c'est important

Les filtres AND rendent les index côté relais plus utiles. Les clients peuvent demander au relais un ensemble de résultats plus petit et déjà pertinent, ce qui réduit la bande passante et le post-traitement local. Le gain est le plus visible sur les clients mobiles et sur les requêtes portant sur de grands ensembles de données riches en tags.

## Notes d'interopérabilité

Au moment de la fusion, des implémentations fonctionnelles existaient dans nostr-rs-relay, satellite-node, worker-relay et applesauce. La proposition portait initialement le numéro NIP-119 avant sa renumérotation.

Les clients doivent s'attendre à un support inégal pendant que l'adoption par les relais progresse. Une solution de repli pratique consiste à conserver l'ancien chemin d'intersection côté client pour les relais qui n'ont pas encore implémenté la nouvelle sémantique.

---

**Sources primaires :**
- [PR #1365](https://github.com/nostr-protocol/nips/pull/1365)

**Mentionné dans :**
- [Newsletter #12 : NIP Updates](/en/newsletters/2026-03-04-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-01 : Basic Protocol](/fr/topics/nip-01/)
