---
title: "NIP-94: File Metadata"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2026-04-22
draft: false
categories:
  - Media
  - Protocol
---
NIP-94 definisce un evento di metadati dei file (kind 1063) per organizzare e classificare i file condivisi su Nostr, permettendo ai relay di filtrare e organizzare il contenuto in modo efficace.

## Come funziona

NIP-94 usa il kind `1063` come evento autonomo di metadati per un file. Il `content` dell'evento contiene una descrizione leggibile dagli esseri umani, mentre i tag trasportano campi leggibili dalle macchine come URL di download, MIME type, hash, dimensioni e indizi per l'anteprima.

Questa separazione conta perché l'evento di metadati può essere indicizzato, filtrato e riusato indipendentemente da qualsiasi nota che rimandi al file. Un client può trattare un evento kind `1063` come descrizione canonica di una risorsa invece di estrarre i metadati da testo libero in un post.

## Tag obbligatori e facoltativi

**Tag principali:**
- `url` - Link di download del file
- `m` - MIME type (formato minuscolo obbligatorio)
- `x` - Hash SHA-256 del file

**Tag facoltativi:**
- `ox` - Hash SHA-256 del file originale prima delle trasformazioni del server
- `size` - Dimensione del file in byte
- `dim` - Dimensioni (larghezza x altezza) per immagini e video
- `magnet` - URI magnet per la distribuzione torrent
- `i` - Torrent infohash
- `blurhash` - Immagine segnaposto per le anteprime
- `thumb` - URL della thumbnail
- `image` - URL dell'immagine di anteprima
- `summary` - Estratto di testo
- `alt` - Descrizione per l'accessibilità
- `fallback` - Sorgenti di download alternative
- `service` - Protocollo di storage o tipo di servizio, come NIP-96

I tag `ox` e `x` sono facili da trascurare ma utili nella pratica. `ox` identifica il file originale caricato, mentre `x` può identificare la versione trasformata che un server serve davvero. Quando un host multimediale comprime o ridimensiona gli upload, i client possono comunque conservare l'identità del file originale senza fingere che il blob trasformato sia identico byte per byte.

## Quando usarlo

NIP-94 è progettato per applicazioni di file sharing invece che per client social o longform. Le applicazioni suggerite includono:

- Relay di indicizzazione torrent
- Piattaforme per condividere portfolio, simili a Pinterest
- Distribuzione di configurazioni software e aggiornamenti
- Librerie e archivi multimediali

Se i metadati del file devono solo arricchire un URL incorporato dentro un altro evento, [NIP-92: Media Attachments](/it/topics/nip-92/) è più leggero. NIP-94 è la scelta migliore quando il file stesso deve essere interrogabile come oggetto di prima classe.

## Note di interoperabilità

NIP-94 funziona attraverso backend di storage diversi. Un file può essere caricato tramite [NIP-96: HTTP File Storage](/it/topics/nip-96/), Blossom o un altro servizio, e poi essere comunque descritto con la stessa forma di evento kind `1063`. Per questo il formato dei metadati continua a vivere oltre qualunque singolo protocollo di upload.

---

**Fonti primarie:**
- [NIP-94 Specification](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Menzionato in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)

**Vedi anche:**
- [NIP-92: Media Attachments](/it/topics/nip-92/)
- [Blossom](/it/topics/blossom/)
