---
title: "NIP-BE: Bluetooth Low Energy"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Connectivity
---

NIP-BE specifica come le applicazioni Nostr possono comunicare e sincronizzarsi tramite Bluetooth Low Energy, abilitando app capaci di funzionare offline per sincronizzare dati tra dispositivi vicini senza connettivita' internet.

## Struttura GATT

Usa un Nordic UART Service con due caratteristiche:
- **Caratteristica Write** - Il client invia dati al server
- **Caratteristica Read** - Il server invia dati al client (tramite notifiche)

## Framing dei Messaggi

BLE ha limiti di payload piccoli (20-256 byte a seconda della versione), quindi i messaggi sono:
- Compressi con DEFLATE
- Divisi in chunk con un indice a 2 byte e flag batch finale
- Limitati a 64KB di dimensione massima

## Negoziazione dei Ruoli

I dispositivi confrontano gli UUID pubblicizzati alla scoperta:
- UUID piu' alto diventa server GATT (ruolo relay)
- UUID piu' basso diventa client GATT
- Esistono UUID predeterminati per dispositivi a ruolo singolo

## Sincronizzazione

Usa comunicazione half-duplex con tipi di messaggio Nostr standard (`EVENT`, `EOSE`, `NEG-MSG`) per coordinare la sincronizzazione dati attraverso connessioni intermittenti.

## Casi d'Uso

- Sincronizzazione eventi offline tra dispositivi vicini
- Propagazione messaggi in stile mesh senza internet
- Connettivita' di backup quando la rete non e' disponibile

---

**Fonti primarie:**
- [Specifica NIP-BE](https://github.com/nostr-protocol/nips/blob/master/BE.md)

**Menzionato in:**
- [Newsletter #1: Notizie](/it/newsletters/2025-12-17-newsletter/#news)

