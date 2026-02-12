---
title: "NIP-96: HTTP File Storage"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Media
---

NIP-96 definiva come i client Nostr caricavano, scaricavano e gestivano file su server media HTTP. Ora contrassegnato come "non raccomandato" a favore di Blossom, NIP-96 resta rilevante mentre i progetti gestiscono la transizione tra i due standard media.

## Come Funziona

Un client scopre le capacità di un file server recuperando `/.well-known/nostr/nip96.json`, che restituisce l'URL API, i tipi di contenuto supportati, i limiti di dimensione e le trasformazioni media disponibili.

Per caricare, il client invia un POST `multipart/form-data` all'URL API con un header di autorizzazione NIP-98 (un evento Nostr firmato che prova l'identità di chi carica). Il server restituisce una struttura metadata file NIP-94 contenente l'URL del file, gli hash SHA-256, il tipo MIME e le dimensioni.

I download usano richieste GET a `<api_url>/<sha256-hash>`, con parametri query opzionali per trasformazioni server-side come il ridimensionamento immagini. La cancellazione usa DELETE con auth NIP-98. Chi pubblica eventi kind 10096 dichiara i propri server di upload preferiti.

## Perché È Stato Deprecato

NIP-96 legava gli URL dei file a server specifici. Se un server andava giù, ogni nota Nostr che referenziava quegli URL perdeva i suoi media. Blossom inverte il modello rendendo l'hash SHA-256 del contenuto del file l'identificatore canonico. Qualsiasi server Blossom che ospita lo stesso file lo serve allo stesso percorso hash, rendendo il contenuto portabile tra server di default.

Blossom semplifica anche l'API con semplice PUT per gli upload, GET per i download, ed eventi Nostr firmati (non header HTTP) per l'autorizzazione. La deprecazione è avvenuta a settembre 2025 tramite [PR #2047](https://github.com/nostr-protocol/nips/pull/2047).

## La Transizione

Server come nostr.build e void.cat supportavano NIP-96 e hanno aggiunto o migrato a endpoint Blossom. I client sono a vari stadi: Angor v0.2.5 ha aggiunto la configurazione server NIP-96 mentre ZSP v0.3.1 carica esclusivamente su server Blossom. La coesistenza continuerà fino a quando le rimanenti implementazioni NIP-96 completeranno la migrazione.

Gli eventi di preferenza server kind 10096 rimangono utili per la selezione server Blossom. I metadata file NIP-94 (eventi kind 1063) descrivono le proprietà dei file indipendentemente da quale protocollo di upload li ha creati.

---

**Fonti primarie**
- [NIP-96, HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047, Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**Menzionato in**
- [Newsletter #9, NIP Deep Dive](/it/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-96-http-file-storage-e-la-transizione-a-blossom)

**Vedi anche**
- [Blossom Protocol](/it/topics/blossom/)
- [NIP-94, File Metadata](/it/topics/nip-94/)
