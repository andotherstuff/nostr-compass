---
title: "NIP-94: File Metadata"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2025-12-31
draft: false
categories:
  - Media
  - Protocollo
---

NIP-94 definisce un evento di metadati file (kind 1063) per organizzare e classificare i file condivisi su Nostr, consentendo ai relay di filtrare e organizzare i contenuti in modo efficace.

## Come Funziona

1. L'utente carica un file su un servizio di hosting
2. Viene pubblicato un evento kind 1063 con i metadati del file
3. Il contenuto dell'evento contiene una descrizione leggibile dall'uomo
4. I tag strutturati forniscono metadati leggibili dalle macchine
5. Client specializzati possono organizzare e visualizzare i file sistematicamente

## Tag Obbligatori e Opzionali

**Tag principali:**
- `url` - Link di download del file
- `m` - MIME type (formato minuscolo richiesto)
- `x` - Hash SHA-256 del file

**Tag opzionali:**
- `ox` - Hash SHA-256 del file originale prima delle trasformazioni del server
- `size` - Dimensione del file in byte
- `dim` - Dimensioni (larghezza x altezza) per immagini/video
- `magnet` - Magnet URI per distribuzione torrent
- `i` - Infohash del torrent
- `blurhash` - Immagine segnaposto per anteprime
- `thumb` - URL miniatura
- `image` - URL immagine di anteprima
- `summary` - Estratto di testo
- `alt` - Descrizione di accessibilità
- `fallback` - Fonti di download alternative

## Casi d'Uso

NIP-94 è progettato per applicazioni di condivisione file piuttosto che per client di contenuti social o di formato lungo. Le applicazioni suggerite includono:

- Relay di indicizzazione torrent
- Piattaforme di condivisione portfolio (simile a Pinterest)
- Distribuzione di configurazioni e aggiornamenti software
- Librerie e archivi multimediali

---

**Fonti principali:**
- [Specifica NIP-94](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Menzionato in:**
- [Newsletter #3: Riepilogo di Dicembre](/it/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Vedi anche:**
- [NIP-92: Allegati Multimediali](/it/topics/nip-92/)
- [Blossom](/it/topics/blossom/)
