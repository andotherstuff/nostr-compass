---
title: "NIP-33 : Événements remplaçables paramétrés (événements adressables)"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-33 définissait à l'origine les événements remplaçables paramétrés, une classe d'événements où un seul événement par tuple `(pubkey, kind, d-tag)` est conservé par les relays. Le concept a depuis été renommé « événements adressables » et intégré dans [NIP-01](/fr/topics/nip-01/). Le document NIP-33 redirige désormais vers NIP-01, mais reste une référence courante dans les codebases et la documentation.

## Comment cela fonctionne

Un événement adressable utilise un kind dans la plage `30000-39999`. Chaque événement porte un tag `d` dont la valeur, avec la pubkey de l'auteur et le numéro de kind, forme une adresse unique. Lorsqu'un relay reçoit un nouvel événement correspondant à un tuple `(pubkey, kind, d-tag)` existant, il remplace l'ancien par le plus récent (selon `created_at`). Cela rend les événements adressables utiles pour l'état mutable : profils, paramètres, configurations d'application, annonces classées et autres structures où seule la dernière version compte.

Les clients référencent les événements adressables avec des tags `a` au format `<kind>:<pubkey>:<d-tag>`, éventuellement suivis d'un hint de relay.

## Usages courants

- Kind `30023` pour les articles long format
- Kind `30078` pour les données spécifiques à une application (utilisé par NIP-78)
- Kind `31923` pour les événements de calendrier (NIP-52)
- Kind `31990` pour les recommandations de handlers (NIP-89)
- Kind `30009` pour les définitions de badges (NIP-58)
- Kind `31991` pour les configurations d'exécution d'agents (Notedeck Agentium)

## Relation avec NIP-01

NIP-33 a été fusionné dans NIP-01 dans le cadre d'un effort de consolidation. La spécification NIP-01 définit maintenant trois catégories de rétention d'événements : événements réguliers (conservés tels quels), événements remplaçables (un par `(pubkey, kind)`) et événements adressables (un par `(pubkey, kind, d-tag)`). NIP-33 reste un raccourci valable pour le concept d'événement adressable.

---

**Sources principales :**
- [NIP-33 (redirect)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [Spécification NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) - section sur les événements adressables

**Mentionné dans :**
- [Newsletter #13 : Notedeck](/fr/newsletters/2026-03-11-newsletter/#notedeck-ajoute-les-limites-de-relay-de-nip-11-et-des-fonctionnalités-agentium)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)
