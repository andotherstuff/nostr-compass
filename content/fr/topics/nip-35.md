---
title: "NIP-35 : torrents"
date: 2026-10-21
translationOf: /en/topics/nip-35.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

NIP-35 est une NIP optionnelle, à l’état de brouillon, consacrée aux events d’index de torrents. Un event de kind 2003 contient un infohash BitTorrent v1 dans un tag `x` ainsi que des chemins de fichiers, et il peut désigner des trackers. Ces events renferment des métadonnées d’index, tandis que les pairs récupèrent le contenu des fichiers via BitTorrent. Les commentaires sur un torrent utilisent le kind 2004 et suivent le modèle de fils de discussion de NIP-10.

Ce numéro a une histoire plus ancienne. Draft Wraps occupait NIP-35 jusqu’à ce qu’une renumérotation, en 2024, déplace cette proposition vers NIP-37. Une référence à NIP-35 antérieure à ce changement peut donc désigner Draft Wraps. Aujourd’hui, le numéro est attribué à Torrents.

Le [texte actuel de NIP-35](https://github.com/nostr-protocol/nips/blob/master/35.md) définit le format des events. L’attribution antérieure est consignée dans le [commit de renumérotation](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408).

## Sources primaires

- [NIP-35 : Torrents](https://github.com/nostr-protocol/nips/blob/master/35.md)
- [Commit 48674e5 de nostr-protocol/nips (renumérotation de 2024)](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408)

## Mentionné dans
- [Newsletter #46 : Magnetar](/fr/newsletters/2026-10-28-newsletter/#magnetar)

- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#short-history)
