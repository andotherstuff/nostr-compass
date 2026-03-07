---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2026-03-07
draft: false
categories:
  - Wallet
  - Ecash
---
NIP-60 definisce come i wallet ecash basati su Cashu operano all'interno di Nostr. Le informazioni del wallet sono memorizzate sui relay, rendendo possibili wallet portabili che funzionano tra applicazioni diverse senza richiedere account separati.

## Come funziona

NIP-60 usa tre tipi di evento principali memorizzati sui relay, più un evento helper opzionale per i quote in sospeso:

**Evento wallet (kind 17375):** Un evento replaceable che contiene la configurazione cifrata del wallet, inclusi gli URL delle mint e una chiave privata per ricevere pagamenti. Questa chiave è separata dalla chiave di identità Nostr dell'utente.

**Eventi token (kind 7375):** Memorizzano prove Cashu non spese cifrate. Quando le prove vengono spese, il client elimina il vecchio evento e ne crea uno nuovo con le eventuali prove rimanenti.

**Storico di spesa (kind 7376):** Record opzionali delle transazioni che mostrano i movimenti dei fondi, con contenuto cifrato e riferimenti agli eventi token creati o distrutti.

**Eventi quote (kind 7374):** Stato cifrato opzionale per i quote di mint in sospeso. La specifica raccomanda eventi di breve durata con tag di scadenza, soprattutto nei casi in cui lo stato locale non basta.

## Modello di stato

NIP-60 riguarda la sincronizzazione dello stato del wallet, non l'atto di ricevere denaro. L'evento wallet dice a un client quali mint e quale chiave wallet usare, mentre gli eventi token sono lo stato reale del saldo perché contengono le prove non spese.

Questa distinzione conta per l'interoperabilità. Due client possono mostrare lo stesso wallet solo se interpretano allo stesso modo il rollover dei token: spendere le prove, pubblicare prove sostitutive ed eliminare l'evento token speso tramite [NIP-09](/it/topics/nip-09/) così che altri client non continuino a conteggiare le prove spese nel saldo.

## Perché è importante

- **Facilità d'uso** - I nuovi utenti possono ricevere ecash subito senza configurare account esterni
- **Interoperabilità** - I dati del wallet seguono gli utenti tra diverse applicazioni Nostr
- **Privacy** - Tutti i dati del wallet sono cifrati con le chiavi dell'utente
- **Gestione delle prove** - Tiene traccia delle transizioni di stato del wallet così che i client possano convergere sullo stesso saldo

## Note di interoperabilità

I client cercano prima le informazioni sui relay del wallet tramite kind 10019 e ricadono sulla lista relay dell'utente di [NIP-65](/it/topics/nip-65/) se non è presente una lista relay dedicata al wallet. Questo fallback è utile, ma significa anche che la portabilità del wallet dipende comunque dal fatto che i relay memorizzino e servano davvero gli eventi wallet cifrati.

La specifica richiede anche che la chiave privata del wallet resti separata dalla chiave di identità Nostr dell'utente. Questo mantiene isolata la gestione delle ricevute del wallet dalla chiave di firma principale e riduce la probabilità che una chiave venga riutilizzata per due scopi diversi.

## Flusso di lavoro

1. Il client recupera la configurazione del wallet dai relay del wallet o dalla lista relay dell'utente
2. Gli eventi token vengono caricati e decifrati per ottenere i fondi disponibili
3. La spesa crea nuovi eventi token ed elimina quelli vecchi
4. Eventi storici opzionali registrano le transazioni come riferimento per l'utente

---

**Fonti primarie:**
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Citato in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #9: NIP Deep Dive](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)

**Vedi anche:**
- [NIP-57: Zaps](/it/topics/nip-57/)
- [NIP-09: Event Deletion Request](/it/topics/nip-09/)
- [NIP-47: Nostr Wallet Connect](/it/topics/nip-47/)
