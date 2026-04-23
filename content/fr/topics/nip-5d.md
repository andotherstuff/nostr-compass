---
title: "NIP-5D : Nostr Web Applets"
date: 2026-04-08
translationOf: /en/topics/nip-5d.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Hosting
---

NIP-5D définit un protocole `postMessage` pour des applications web sandboxées (« napplets ») exécutées dans des iframes afin de communiquer avec une application hôte (« shell »). Il étend [NIP-5A](/fr/topics/nip-5a/) (sites web statiques) avec une couche de communication runtime qui donne aux web apps accès aux fonctionnalités Nostr sans exposer la clé privée de l'utilisateur.

## Fonctionnement

Une application shell charge une napplet dans une iframe sandboxée. La napplet communique avec le shell via l'API `postMessage` du navigateur en utilisant un protocole de messages structurés. Le shell fournit à la napplet la signature Nostr, l'accès relay et le contexte utilisateur à travers ce canal de messages. La sandbox de l'iframe empêche la napplet d'accéder directement à la clé privée de l'utilisateur, de sorte que le shell agit comme gardien pour toutes les opérations Nostr.

## Cas d'usage

- **Applications Nostr interactives** : construire des apps qui lisent et écrivent des événements Nostr sans demander aux utilisateurs de coller leur nsec
- **Marketplace d'apps** : distribuer des applications web interactives via des événements Nostr
- **Extensions sandboxées** : ajouter des fonctionnalités aux clients Nostr via des napplets tierces

---

**Sources principales :**
- [NIP-5D PR #2303](https://github.com/nostr-protocol/nips/pull/2303) - Proposition Nostr Web Applets

**Mentionné dans :**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)

**Voir aussi :**
- [NIP-5A (sites web statiques)](/fr/topics/nip-5a/)
- [NIP-5C (Scrolls)](/fr/topics/nip-5c/)
