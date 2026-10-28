---
title: "NIP-35: torrents"
date: 2026-10-21
translationOf: /en/topics/nip-35.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

NIP-35 es un NIP en borrador y opcional para events de índice de torrents. Un event de kind 2003 lleva un infohash de BitTorrent v1 en un tag `x` junto con rutas de archivos, y puede indicar trackers. Los events contienen metadatos de índice, mientras que los pares obtienen el contenido de los archivos a través de BitTorrent. Los comentarios sobre un torrent usan kind 2004 y siguen el sistema de hilos de NIP-10.

El número tiene una historia anterior. Draft Wraps ocupaba NIP-35 hasta que una renumeración de 2024 trasladó esa propuesta a NIP-37. Por eso, una referencia a NIP-35 anterior a ese cambio puede referirse a Draft Wraps. Hoy el número corresponde a Torrents.

El [texto actual de NIP-35](https://github.com/nostr-protocol/nips/blob/master/35.md) define el formato del event. En el [commit de renumeración](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408) queda constancia de la asignación anterior.

## Fuentes primarias

- [NIP-35: torrents](https://github.com/nostr-protocol/nips/blob/master/35.md)
- [Commit 48674e5 de nostr-protocol/nips (renumeración de 2024)](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408)

## Mencionado en
- [Boletín n.º 46: Magnetar](/es/newsletters/2026-10-28-newsletter/#magnetar)

- [Boletín 45](/en/newsletters/2026-10-21-newsletter/#short-history)
