---
title: "NIP-09"
date: 2026-02-25
translationOf: /en/topics/nip-09.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Protocol
---

NIP-09 definisce la Cancellazione degli Event, un meccanismo con cui gli utenti possono richiedere ai relay di rimuovere event precedentemente pubblicati.

## Come Funziona

Gli utenti pubblicano event di kind 5 contenenti tag `e` che referenziano gli ID degli event da eliminare. I relay che supportano NIP-09 dovrebbero smettere di servire gli event referenziati e possono cancellarli dallo storage.

La cancellazione è una richiesta, non una garanzia. I relay possono ignorare le richieste di cancellazione, e gli event potrebbero essersi già propagati a relay che non supportano la cancellazione. Gli utenti non dovrebbero fare affidamento su NIP-09 per la rimozione di contenuti sensibili alla privacy.

## Caratteristiche Principali

- Event di richiesta di cancellazione kind 5
- Riferimento agli event eliminati tramite ID con tag e
- Campo motivo opzionale per il contesto della cancellazione
- La conformità del relay è volontaria

---

**Fonti principali:**
- [Specifica NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md)

**Citato in:**
- [Newsletter #11: Approfondimento NIP-60](/it/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-wallet-cashu)

**Vedi anche:**
- [NIP-60: Wallet Cashu](/it/topics/nip-60/)
