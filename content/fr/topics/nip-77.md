---
title: "NIP-77 : Réconciliation Negentropy"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-77.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Sync
---

NIP-77 définit comment les relais et les clients Nostr utilisent le protocole de réconciliation d'ensembles [Negentropy](/fr/topics/negentropy/) pour synchroniser efficacement les ensembles d'événements, en trouvant quels événements manquent de chaque côté sans renvoyer l'intégralité du jeu de données.

## Fonctionnement

La réconciliation Negentropy s'exécute sur une connexion WebSocket en utilisant un type de message dédié. Le client et le relais échangent des empreintes de plage compactes sur leurs ensembles d'événements triés, en se concentrant uniquement sur les plages qui diffèrent. Une fois les différences identifiées, seuls les identifiants d'événements manquants (puis les événements manquants eux-mêmes) sont transférés.

NIP-77 standardise le cadrage des messages afin que tout client et relais implémentant la spécification puisse négocier une session de synchronisation efficace. Le protocole utilise les types de messages `NEG-OPEN`, `NEG-MSG` et `NEG-CLOSE` sur la connexion WebSocket Nostr existante.

## Pourquoi c'est important

La synchronisation Nostr traditionnelle utilise des filtres `since` basés sur les horodatages, qui peuvent manquer des événements en raison de la dérive d'horloge, d'événements avec des horodatages identiques, ou d'événements arrivant dans le désordre. Negentropy compare les ensembles d'événements réels plutôt que de se fier aux horodatages, offrant une synchronisation complète et démontrable en beaucoup moins d'allers-retours que le sondage naïf.

Ceci est particulièrement utile pour :
- Les clients mobiles qui se mettent à jour après avoir été hors ligne
- La réplication de relais à relais
- La synchronisation de relais local (comme dans l'agrégateur de relais de Citrine)

## Implémentations

- [Citrine](https://github.com/greenart7c3/Citrine) — [PR #139](https://github.com/greenart7c3/Citrine/pull/139) a ajouté la prise en charge de NIP-77 pour la synchronisation efficace par réconciliation d'ensembles dans le nœud relais Android
- [strfry](https://github.com/hoytech/strfry) — prise en charge Negentropy côté relais
- [nostr-tools](https://github.com/nbd-wtf/nostr-tools) — implémentation Negentropy côté client

---

**Sources primaires :**
- [Spécification NIP-77](https://github.com/nostr-protocol/nips/blob/master/77.md)
- [Protocole Negentropy](https://github.com/hoytech/negentropy)

**Mentionné dans :**
- [Newsletter #22 : Citrine v3.0.0-pre1](/fr/newsletters/2026-05-14-newsletter/#citrine-v300-pre1-lands-built-in-tor-and-relay-aggregation)

**Voir aussi :**
- [Negentropy](/fr/topics/negentropy/)
