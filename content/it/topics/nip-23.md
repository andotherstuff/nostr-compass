---
title: "NIP-23: Contenuti Long-form"
date: 2026-04-08
translationOf: /en/topics/nip-23.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Publishing
---

NIP-23 definisce il kind `30023` per i contenuti testuali long-form su Nostr. A differenza delle note brevi kind `1`, gli eventi long-form sono eventi parameterized replaceable (identificati da un tag `d`), supportano la formattazione Markdown e includono tag di metadati per titolo, riassunto, immagini e date di pubblicazione.

## Come funziona

Un evento long-form usa il kind `30023` con un tag `d` come identificatore univoco, così l'autore può aggiornare il contenuto pubblicando un nuovo evento con lo stesso tag `d`. Il campo `content` contiene testo Markdown. I tag standard includono `title`, `summary`, `image` (URL dell'immagine di copertina), `published_at` (timestamp Unix della pubblicazione originale) e `t` (hashtag). Poiché l'evento è parameterized replaceable, i relay conservano solo la versione piu recente per ogni tag `d` per autore.

## Tag principali

- `d` - identificatore univoco dell'articolo (slug)
- `title` - titolo dell'articolo
- `summary` - descrizione breve
- `image` - URL dell'immagine di copertina
- `published_at` - timestamp Unix della pubblicazione originale (distinto da `created_at`, che si aggiorna a ogni modifica)
- `t` - hashtag e tag tematici

## Implementazioni

- [Habla](https://habla.news) - lettore e publisher di contenuti long-form
- [YakiHonne](https://yakihonne.com) - piattaforma di contenuti long-form
- [Highlighter](https://highlighter.com) - strumento di lettura e annotazione

---

**Fonti primarie:**
- [Specifica NIP-23](https://github.com/nostr-protocol/nips/blob/master/23.md)

**Vedi anche:**
- [NIP-01 (Protocollo di base)](/it/topics/nip-01/)
