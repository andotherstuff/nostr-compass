---
title: "NIP-F4 : Podcasts"
date: 2026-06-03
draft: false
translationOf: /en/topics/nip-f4.md
translationDate: 2026-07-01
categories:
  - NIPs
  - Protocol
  - Media
---

NIP-F4 définit comment les clients Nostr référencent, font remonter et interagissent socialement avec les épisodes de podcast. Fusionné le 2026-05-28 après deux ans et trois mois en brouillon, la spécification utilise des événements de kind 54 pour les épisodes et est conçue autour de la pile RSS de podcasting existante comme couche complémentaire.

## Comment ça marche

Un événement d'épisode de podcast kind 54 porte un tag `title`, un tag `image` optionnel, un tag `description`, un ou plusieurs tags `imeta` pour le fichier audio (URL, type mime, hash, durée, débit binaire, code de langue, URL de repli, indicateur de service NIP-96), des tags de sujet `t` et un tag `alt` NIP-31 pour l'affichage de repli.

Le choix de conception structurant est le tag `i`, qui porte le GUID RSS de l'épisode au format `podcast:item:guid:<guid>`. Cela permet :

- À un client Nostr d'afficher un événement kind 54 et de le relier au même épisode dans n'importe quelle app podcast compatible RSS
- À un client Nostr compatible RSS de faire remonter les épisodes d'un podcast existant en tant qu'événements kind 54 sans forcer le podcasteur à migrer son hébergement
- L'enchaînement de commentaires inter-protocoles via les tags `<podcast:socialInteract>` et `<podcast:chat>` de Podcasting 2.0

## Coexistence avec RSS

Le débat de deux ans sur le fil de la PR (avec le co-auteur de Podcasting 2.0 Dave Jones, Alex Gleason, fiatjaf, Mike Terenzio, Pablo F7z et Jeff Gardner) s'est réglé sur la coexistence. Nostr fournit la couche sociale et de découverte tandis que RSS garde la source de vérité pour le fichier audio et les métadonnées du fil. Nostr ne duplique pas la couche de distribution RSS.

Cela contraste avec les tentatives antérieures de remplacer RSS (JSONFeed, RSS 3.0, API podcast propriétaires). L'espace de noms Podcasting 2.0 prend déjà en charge `<podcast:socialInteract>` référençant des événements Nostr par ID de note, donc un fil RSS peut déclarer son fil de discussion Nostr compagnon sans exiger que Nostr reflète le fil lui-même.

## Exemple d'événement

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["imeta", "url https://podcast.example.com/audio/ep42.mp3", "m audio/mpeg", "x b2e0a7a82ac9f3f3a71f1d9a78c381d5be9d1cf19dce258765c17c8a76287c93", "duration 4523", "bitrate 192000", "l en ISO-639-1"],
    ["i", "podcast:item:guid:9b2a4c7d-1e3f-4a5b-8c9d-0e1f2a3b4c5d"],
    ["t", "podcasting"],
    ["alt", "Podcast episode: Why RSS Won (43 min)"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

## Implémentations

- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - Écran podcast dédié avec liste d'épisodes et lecteur intégré (première implémentation majeure d'un client, mai 2026)
- [Wavlake](https://wavlake.com) - Plus grande plateforme musique et podcasting native Nostr, attendue pour s'aligner sur kind 54 pour le contenu podcast
- [Fountain](https://fountain.fm) - App podcast Bitcoin, attendue pour faire le pont entre RSS et NIP-F4

## Questions ouvertes

La spécification fusionnée conserve plusieurs questions de conception sur lesquelles les implémentations doivent converger :

- Les pubkeys par créateur sont recommandés mais non exigés, donc les plateformes comme Wavlake qui publient de nombreux créateurs sous un seul pubkey restent valides
- Les commentaires et discussions par épisode utilisent l'enchaînement générique NIP-22 et des notes de timeline kind 1 plutôt qu'un kind dédié aux commentaires d'épisode
- Les métadonnées par podcast (hôte, réseau, langue, licence) vivent soit dans les métadonnées kind 0 de l'éditeur, soit dans un enregistrement kind 54 séparé au niveau podcast

---

**Sources primaires :**
- [Spécification NIP-F4](https://github.com/nostr-protocol/nips/blob/master/F4.md)
- [PR #1093](https://github.com/nostr-protocol/nips/pull/1093) - Proposition originale, fusionnée le 2026-05-28 après deux ans de discussion
- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - Première implémentation majeure d'un client

**Mentionné dans :**
- [Newsletter #25 : Mises à jour NIP et deep dive](/fr/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-f4-podcasts)
- [Newsletter #27 : Amethyst v1.12.0 intègre les portefeuilles Cashu, les nutzaps, un pilote CLINK et l'auto-réparation Tor](/fr/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Voir aussi :**
- [NIP-22 (Commentaires)](https://github.com/nostr-protocol/nips/blob/master/22.md)
- [NIP-31 (Tags alt)](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [NIP-94 (Métadonnées de fichier)](/fr/topics/nip-94/)
- [NIP-96 (Stockage de fichiers HTTP)](/fr/topics/nip-96/)
- [Podcasting 2.0](https://podcasting2.org)
