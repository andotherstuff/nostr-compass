---
title: "NIP-5C : Scrolls (programmes WASM)"
date: 2026-04-08
translationOf: /en/topics/nip-5c.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Programs
---

NIP-5C (anciennement NIP-A5) définit des conventions pour publier, découvrir et exécuter des programmes WebAssembly (« scrolls ») sur Nostr. Les binaires WASM sont stockés comme événements Nostr, ce qui permet à n'importe quel client de les récupérer et de les exécuter dans un runtime sandboxé.

## Fonctionnement

Les développeurs publient des programmes WASM comme événements Nostr contenant le binaire compilé. Les clients découvrent ces programmes via des requêtes Nostr standards, téléchargent le binaire WASM depuis l'événement, puis l'exécutent dans un runtime WebAssembly sandboxé. La sandbox empêche les scrolls d'accéder directement au système hôte et les limite aux capacités que le runtime fournit explicitement.

## Cas d'usage

- **Calcul portable** : exécuter des programmes sur n'importe quel client qui supporte l'exécution WASM
- **Distribution décentralisée d'applications** : publier et découvrir des applications sans app stores
- **Outils composables** : chaîner des scrolls ensemble pour des workflows complexes

## Démo

Une [demo app](https://nprogram.netlify.app/) montre des scrolls s'exécutant dans le navigateur, avec des programmes exemples publiés comme événements Nostr.

---

**Sources principales :**
- [NIP-5C PR #2281](https://github.com/nostr-protocol/nips/pull/2281) - Proposition Scrolls (programmes WASM)

**Mentionné dans :**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)
- [Newsletter #19 : proposition NIP-5D applets](/en/newsletters/2026-04-22-newsletter/)

**Voir aussi :**
- [NIP-5D (Web Applets)](/fr/topics/nip-5d/)
- [NIP-5A (sites web statiques)](/fr/topics/nip-5a/)
