---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2025-12-31
draft: false
categories:
  - Portafoglio
  - Ecash
---

NIP-60 definisce come i portafogli ecash basati su Cashu operano all'interno di Nostr. Le informazioni del portafoglio sono memorizzate sui relay, consentendo portafogli portatili che funzionano attraverso diverse applicazioni senza richiedere account separati.

## Come Funziona

NIP-60 utilizza tre tipi di eventi memorizzati sui relay:

**Evento Portafoglio (kind 17375):** Un evento sostituibile contenente la configurazione crittografata del portafoglio, inclusi gli URL di mint e una chiave privata per ricevere pagamenti. Questa chiave è separata dalla chiave di identità Nostr dell'utente.

**Eventi Token (kind 7375):** Memorizzano prove Cashu non spese e crittografate. Quando le prove vengono spese, il client elimina il vecchio evento e ne crea uno nuovo con le prove rimanenti.

**Cronologia Spese (kind 7376):** Registrazioni opzionali delle transazioni che mostrano i movimenti di fondi, con contenuto crittografato e riferimenti agli eventi token creati/distrutti.

## Caratteristiche Principali

- **Facilità d'uso** - I nuovi utenti possono ricevere ecash immediatamente senza configurazione di account esterni
- **Interoperabilità** - I dati del portafoglio seguono gli utenti attraverso diverse applicazioni Nostr
- **Privacy** - Tutti i dati del portafoglio sono crittografati con le chiavi dell'utente
- **Gestione delle prove** - Traccia quali eventi token sono stati spesi per prevenire la doppia spesa

## Flusso di Lavoro

1. Il client recupera la configurazione del portafoglio dai relay
2. Gli eventi token vengono caricati e decrittografati per ottenere i fondi disponibili
3. Spendere crea nuovi eventi token ed elimina quelli vecchi
4. Gli eventi cronologia opzionali registrano le transazioni come riferimento per l'utente

---

**Fonti primarie:**
- [Specifica NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Menzionato in:**
- [Newsletter #3: Riepilogo di Dicembre](/it/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Vedi anche:**
- [NIP-57: Zaps](/it/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/it/topics/nip-47/)
