---
title: "NIP-90"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - DVM
---

NIP-90 definisce le Data Vending Machine (DVM), un protocollo marketplace per richiedere e pagare lavoro computazionale su Nostr.

## Come Funziona

I client pubblicano event di richiesta lavoro (kind 5000-5999) specificando il lavoro necessario. I provider di servizi monitorano le richieste corrispondenti alle proprie capacità e pubblicano i risultati dopo aver completato il calcolo. Il pagamento avviene tramite Lightning o altri meccanismi negoziati nel flusso del job.

I kind di job definiscono diversi tipi di computazione: generazione di testo, generazione di immagini, traduzione, scoperta di contenuti e altro. Ogni kind specifica il formato di input e output atteso.

## Caratteristiche Principali

- Marketplace di calcolo decentralizzato
- Sistema di tipi di job basato sui kind
- Competizione tra provider su prezzo e qualità
- Estensibile per nuovi tipi di computazione

---

**Fonti principali:**
- [Specifica NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Citato in:**
- [Newsletter #11: NIP-AC Coordinamento Agenti DVM](/it/newsletters/2026-02-25-newsletter/#aggiornamenti-nip)

**Vedi anche:**
- [NIP-85: Trusted Assertions](/it/topics/nip-85/)
