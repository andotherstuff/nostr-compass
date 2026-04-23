---
title: "Protocollo Blossom"
date: 2025-12-17
translationOf: /en/topics/blossom/
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---
Blossom è un protocollo di hosting media per Nostr che archivia blob su normali server HTTP e li identifica tramite hash SHA-256 invece che con ID assegnati dal server.

## Come funziona

I server Blossom espongono una piccola interfaccia HTTP per recupero, upload e gestione dei blob. L'identificatore canonico è l'hash del file, quindi lo stesso blob mantiene lo stesso indirizzo su ogni server conforme.

- `GET /<sha256>` recupera un blob tramite hash
- `PUT /upload` carica un blob
- gli eventi Nostr kind `24242` autorizzano upload e azioni di gestione
- gli eventi kind `10063`, definiti in [BUD-03](/it/topics/bud-03/), permettono agli utenti di pubblicare i propri server preferiti

Poiché l'hash è l'identificatore, i client possono verificare localmente l'integrità dopo il download e possono provare un altro server senza cambiare il riferimento sottostante.

## Perché conta

Blossom separa l'archiviazione dei blob dagli eventi sociali. Una nota o un profilo può puntare a un media senza legare quel media al design degli URL di un singolo host.

Questo cambia anche la gestione dei guasti. Se un server scompare, i client possono recuperare lo stesso hash da un mirror, una cache o un server scoperto tramite la lista [BUD-03](/it/topics/bud-03/) dell'autore. È un miglioramento pratico rispetto ai sistemi media in cui l'URL dell'host originale è l'unico identificatore.

## Note sull'interoperabilità

Blossom è modulare. Il comportamento di base per recupero e upload vive in BUD-01 e BUD-02, mentre mirroring, ottimizzazione dei media, autorizzazione e condivisione URI sono separati in BUD distinti.

Questa divisione permette ai client di implementare il minimo necessario per un'interoperabilità di base, poi aggiungere parti opzionali come gli hint URI di [BUD-10](/it/topics/bud-10/) o la cache locale man mano che il supporto matura.

---

**Fonti primarie:**
- [Blossom Repository](https://github.com/hzrd149/blossom)
- [BUD-01: Server requirements and blob retrieval](https://github.com/hzrd149/blossom/blob/master/buds/01.md)
- [BUD-02: Blob upload and management](https://github.com/hzrd149/blossom/blob/master/buds/02.md)
- [Local Blossom Cache guide](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md)

**Citato in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: Notable Code Changes](/en/newsletters/2025-12-24-newsletter/)
- [Newsletter #10: Blossom local cache layer emerges](/en/newsletters/2026-02-18-newsletter/)

**Vedi anche:**
- [BUD-03: User Server List](/it/topics/bud-03/)
- [BUD-10: Blossom URI Scheme](/it/topics/bud-10/)
