---
title: "NIP-35: Torrent"
date: 2026-10-21
translationOf: /en/topics/nip-35.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

NIP-35 è una NIP in bozza e opzionale per gli event di indicizzazione dei torrent. Un event di kind 2003 contiene un infohash BitTorrent v1 in un tag `x` insieme ai percorsi dei file, e può indicare dei tracker. Gli event contengono metadati di indicizzazione, mentre i peer recuperano il contenuto dei file tramite BitTorrent. I commenti a un torrent usano il kind 2004 e seguono il threading di NIP-10.

Il numero ha una storia precedente. NIP-35 era assegnato a Draft Wraps finché, nel 2024, una rinumerazione non ha spostato quella proposta a NIP-37. Un riferimento a NIP-35 anteriore a quel cambiamento potrebbe indicare Draft Wraps. Oggi il numero appartiene a Torrent.

Il formato degli event è definito nel [testo attuale di NIP-35](https://github.com/nostr-protocol/nips/blob/master/35.md). L'assegnazione precedente è documentata nel [commit di rinumerazione](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408).

## Fonti primarie

- [NIP-35: Torrent](https://github.com/nostr-protocol/nips/blob/master/35.md)
- [Commit 48674e5 di nostr-protocol/nips (rinumerazione del 2024)](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408)

## Citato in
- [Newsletter #46: Magnetar](/it/newsletters/2026-10-28-newsletter/#magnetar)

- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#short-history)
