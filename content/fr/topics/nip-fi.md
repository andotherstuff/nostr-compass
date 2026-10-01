---
title: "Buzz NIP-FI : Assertions d’identité fédérée"
date: 2026-09-30
draft: false
categories:
  - Project Proposals
  - Identity
  - Relays
translationOf: /en/topics/nip-fi.md
translationDate: 2026-10-01
---

NIP-FI est la spécification d'assertion d'identité fédérée **propre au projet** Buzz. Ce nom n'implique ni son adoption par le dépôt `nostr-protocol/nips`, ni une interopérabilité avec des relays extérieurs à Buzz.

## Entrée HTTP

Pour les requêtes HTTP protégées en mode d'application des contrôles, Buzz associe une assertion d'identité fédérée à un event d'autorisation signé NIP-98. La clé publique Nostr dont la possession est prouvée par la signature HTTP doit correspondre à la clé désignée dans l'assertion. Toute preuve manquante, non concordante ou invérifiable est rejetée. Buzz utilise cette association pour relier la décision d'autorisation d'un émetteur d'identité externe à la clé Nostr à l'origine de la requête.

La [révision de la spécification du projet](https://github.com/block/buzz/pull/7254) définit le modèle d'application des contrôles. L'[implémentation fusionnée de l'entrée HTTP](https://github.com/block/buzz/pull/7264) couvre les interfaces HTTP protégées de Buzz, notamment le pont relay, les médias, les workflows et les chemins Git. La fusion fait état de tests du code source ; elle ne signifie pas qu'un autre relay Nostr implémente la même politique.

---

**Sources primaires :**
- [Révision de la spécification Buzz NIP-FI](https://github.com/block/buzz/pull/7254)
- [Implémentation de l'entrée HTTP de Buzz](https://github.com/block/buzz/pull/7264)

**Mentionné dans :**
- [Lettre d'information #42 : Contrôles d'identité de Buzz](/fr/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
