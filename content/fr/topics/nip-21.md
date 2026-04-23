---
title: "NIP-21 : Schéma d'URI nostr:"
date: 2026-04-22
translationOf: /en/topics/nip-21.md
translationDate: 2026-04-23
draft: false
categories:
  - Protocol
  - Interoperability
---

NIP-21 définit le schéma d'URI `nostr:`, une manière standard pour les applications, les sites web et les systèmes d'exploitation d'ouvrir des identifiants Nostr comme `npub`, `nprofile`, `nevent` et `naddr` via le client Nostr que l'utilisateur a enregistré comme gestionnaire.

## Fonctionnement

Une URI `nostr:` se compose du préfixe de schéma suivi de n'importe lequel des identifiants bech32 de [NIP-19](/fr/topics/nip-19/), à l'exception de `nsec`. Les clients et les systèmes d'exploitation traitent ce schéma comme `mailto:` ou `tel:` : s'enregistrer comme gestionnaire permet à l'utilisateur de cliquer sur un lien `nostr:` n'importe où dans le système et de l'ouvrir dans le client Nostr de son choix.

Exemples tirés de la spécification :

- `nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9` pointe vers un profil utilisateur
- `nostr:nprofile1...` pointe vers un profil utilisateur avec des indices de relais intégrés
- `nostr:nevent1...` pointe vers un événement précis avec des indices de relais
- `nostr:naddr1...` pointe vers un événement remplaçable paramétré, comme un article long format

## Lier des pages HTML à des entités Nostr

NIP-21 spécifie aussi deux conventions `<link>` utiles pour les pages web qui correspondent à des entités Nostr. Une page qui sert le même contenu qu'un événement Nostr, par exemple un billet de blog rendu depuis un article `kind:30023` de [NIP-23](/fr/topics/nip-23/), peut inclure un `<link rel="alternate">` pointant vers l'URI Nostr. Une page de profil peut inclure un `<link rel="me">` ou `<link rel="author">` pointant vers un `nprofile` pour affirmer une paternité fondée sur Nostr.

## Pourquoi c'est important

Ce schéma constitue la couche d'interopérabilité qui permet à n'importe quel identifiant Nostr de devenir un lien fonctionnel en dehors de l'interface d'un client unique. Les extensions de navigateur, les gestionnaires d'OS mobiles et les environnements desktop peuvent tous router les URI `nostr:` vers le client installé par l'utilisateur, ce qui permet de partager un profil ou un événement en collant une URI n'importe où sans perdre la possibilité de l'ouvrir de façon native dans Nostr.

## Implémentations

Le support des URI `nostr:` est largement répandu dans l'écosystème des clients, y compris parmi les principaux clients web, mobiles et desktop. Des extensions de navigateur comme [nos2x](https://github.com/fiatjaf/nos2x) et [Alby](https://github.com/getAlby/lightning-browser-extension) gèrent l'enregistrement de l'URI dans les navigateurs desktop.

---

**Sources principales :**

- [Spécification NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md)

**Mentionné dans :**

- [Newsletter #19 : Nostrability migre vers NIP-34](/en/newsletters/2026-04-22-newsletter/#nostrability-migrates-to-nip-34-and-opens-19-per-nip-interop-trackers)

**Voir aussi :**

- [NIP-19 : Entités encodées en bech32](/fr/topics/nip-19/)
- [NIP-23 : Contenu long format](/fr/topics/nip-23/)
