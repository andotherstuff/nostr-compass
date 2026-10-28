---
title: "NIP-35: Torrents"
date: 2026-10-21
translationOf: /en/topics/nip-35.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

A NIP-35 é uma NIP em rascunho e opcional para events de índice de torrents. Um event de kind 2003 carrega um infohash BitTorrent v1 em uma tag `x`, junto com caminhos de arquivos, e pode indicar trackers. Os events contêm metadados de índice, enquanto os peers buscam o conteúdo dos arquivos via BitTorrent. Comentários sobre um torrent usam kind 2004 e seguem o encadeamento da NIP-10.

Esse número já teve outro uso. O Draft Wraps ocupava a NIP-35 até 2024, quando uma renumeração transferiu essa proposta para a NIP-37. Uma referência à NIP-35 anterior a essa mudança pode significar Draft Wraps. Hoje, o número pertence a Torrents.

O [texto atual da NIP-35](https://github.com/nostr-protocol/nips/blob/master/35.md) define o formato do event. Já o [commit de renumeração](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408) registra a atribuição anterior.

## Fontes primárias

- [NIP-35: Torrents](https://github.com/nostr-protocol/nips/blob/master/35.md)
- [Commit 48674e5 de nostr-protocol/nips (renumeração de 2024)](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408)

## Mencionado em
- [Newsletter #46: Magnetar](/pt/newsletters/2026-10-28-newsletter/#magnetar)

- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#short-history)
