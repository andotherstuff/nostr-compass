---
title: "NIP-69: Trading Peer-to-Peer"
date: 2025-12-17
translationOf: /en/topics/nip-69/
translationDate: 2026-03-07
draft: false
categories:
  - Trading
  - Protocol
---
NIP-69 definisce un protocollo per il trading peer-to-peer su Nostr, creando un order book unificato su più piattaforme invece di pool di liquidità frammentati.

## Come Funziona

NIP-69 usa eventi addressable kind 38383 per ordini di acquisto e vendita. Il formato addressable conta perché un ordine può attraversare diversi stati nel tempo mantenendo la stessa identità logica tramite il suo tag `d`.

## Struttura dell'Ordine

Gli ordini usano tag per specificare i parametri della transazione:

- `d` - ID dell'ordine
- `k` - Tipo di ordine (buy/sell)
- `f` - Valuta fiat (codice ISO 4217)
- `amt` - Quantità di Bitcoin in satoshi
- `fa` - Quantità fiat
- `pm` - Metodi di pagamento accettati
- `premium` - Percentuale di premio/sconto sul prezzo
- `network` - Rete Bitcoin (mainnet, testnet, signet, regtest)
- `layer` - Livello di regolamento (onchain, lightning, liquid)
- `expiration` - Quando l'ordine scade

## Ciclo di Vita dell'Ordine

Gli ordini passano attraverso questi stati:
- `pending` - Aperto e disponibile per il matching
- `in-progress` - Scambio avviato con la controparte
- `success` - Scambio completato
- `canceled` - Ritirato dal maker
- `expired` - Oltre il tempo di scadenza

La specifica distingue due limiti temporali. `expires_at` indica quando un ordine pending deve smettere di essere considerato aperto, mentre `expiration` fornisce ai relay un timestamp che possono usare con [NIP-40](/it/topics/nip-40/) per rimuovere del tutto gli eventi d'ordine stale.

## Perché Conta

NIP-69 è una mossa di interoperabilità. Mostro, lnp2pBot, RoboSats, Peach e altri sistemi di trading P2P possono esporre gli ordini in un formato di evento condiviso invece di tenere la liquidità intrappolata dentro app separate.

Il tag `g` opzionale rende possibile anche il trading locale, faccia a faccia, senza cambiare il resto dello schema dell'ordine. Questo è utile perché gli scambi in contanti locali hanno bisogno di filtri geografici, mentre gli scambi Lightning online no.

## Sicurezza e Fiducia

Il tag `bond` specifica un deposito di garanzia che entrambe le parti devono pagare, fornendo protezione contro abbandono o frode.

Questo però non elimina il rischio di controparte. Controversie sui pagamenti, frodi fiat, reputazione e regole di custodia restano al livello applicativo. NIP-69 standardizza la pubblicazione degli ordini, non la risoluzione delle controversie.

---

**Fonti primarie:**
- [Specifica NIP-69](https://github.com/nostr-protocol/nips/blob/master/69.md)
- [Specifica del Protocollo Mostro](https://mostro.network/protocol/)

**Menzionato in:**
- [Newsletter #1: Aggiornamenti NIP](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #1: Release](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2: Notizie](/en/newsletters/2025-12-24-newsletter/#news)

**Vedi anche:**
- [NIP-40: Timestamp di Scadenza](/it/topics/nip-40/)
