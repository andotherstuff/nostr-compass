---
title: "NIP-33 : Événements remplaçables paramétrés (événements adressables)"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-33 définissait à l'origine les événements remplaçables paramétrés, une classe d'événements où un seul événement par tuple `(pubkey, kind, d-tag)` est conservé par les relays. Le concept a depuis été renommé « événements adressables » et intégré dans [NIP-01](/fr/topics/nip-01/). Le document NIP-33 redirige désormais vers NIP-01 mais reste une référence courante dans les bases de code et la documentation.

## Comment ça fonctionne

Un événement adressable utilise un kind dans la plage `30000-39999`. Chaque événement porte un tag `d` dont la valeur, combinée avec la pubkey de l'auteur et le numéro de kind, forme une adresse unique. Lorsqu'un relay reçoit un nouvel événement correspondant à un tuple `(pubkey, kind, d-tag)` existant, il remplace l'ancien événement par le nouveau (selon `created_at`). Cela rend les événements adressables utiles pour l'état mutable : profils, paramètres, configurations d'applications, annonces classifiées et structures similaires où seule la dernière version compte.

Les clients référencent les événements adressables avec des tags `a` au format `<kind>:<pubkey>:<d-tag>`, éventuellement suivis d'un indice de relay.

## Utilisations courantes

- Kind `30023` articles longs
- Kind `30078` données spécifiques à l'application (utilisé par NIP-78)
- Kind `31923` événements de calendrier (NIP-52)
- Kind `31990` recommandations de gestionnaires (NIP-89)
- Kind `30009` définitions de badges (NIP-58)
- Kind `31991` configurations d'exécution d'agents (Notedeck Agentium)

## Relation avec NIP-01

NIP-33 a été fusionné dans NIP-01 dans le cadre d'un effort de consolidation. La spécification NIP-01 définit désormais trois catégories de rétention d'événements : les événements réguliers (conservés tels quels), les événements remplaçables (un par `(pubkey, kind)`) et les événements adressables (un par `(pubkey, kind, d-tag)`). NIP-33 reste un raccourci valide pour le concept d'événement adressable.

---

**Sources principales :**
- [NIP-33 (redirection)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [Spécification NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) - Section événements adressables

**Mentionné dans :**
- [Newsletter #13 : Notedeck](/en/newsletters/2026-03-11-newsletter/#notedeck-adds-nip-11-relay-limits-and-agentium-features)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)
