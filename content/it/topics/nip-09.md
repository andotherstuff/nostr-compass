---
title: "NIP-09: Richiesta di eliminazione evento"
date: 2026-02-25
translationOf: /en/topics/nip-09.md
translationDate: 2026-03-07
draft: false
categories:
  - Moderation
  - Protocol
---
NIP-09 definisce un modo con cui gli autori possono richiedere l'eliminazione di eventi pubblicati in precedenza. È un segnale di eliminazione lato relay, non una funzione di cancellazione valida per tutta la rete.

## Come funziona

Gli utenti pubblicano eventi kind 5 che contengono riferimenti agli eventi che vogliono eliminare. I relay che supportano NIP-09 dovrebbero smettere di servire gli eventi corrispondenti dello stesso autore e possono rimuoverli dallo storage.

L'eliminazione è una richiesta, non una garanzia. I relay possono ignorare le richieste di eliminazione e gli eventi potrebbero essersi già propagati verso relay che non supportano l'eliminazione. Gli utenti non dovrebbero fare affidamento su NIP-09 per rimuovere contenuti sensibili dal punto di vista della privacy.

## Perché conta

NIP-09 offre a client e relay un modo comune per esprimere "questo evento non dovrebbe più apparire", utile per post accidentali, rollover dello stato del wallet e flussi di moderazione. Ma l'autore può richiedere l'eliminazione solo dei propri eventi. Non è un meccanismo generale di rimozione per contenuti di terze parti.

## Compromessi

Il punto debole è la propagazione. Una volta che un evento è stato replicato su più relay, l'eliminazione diventa best-effort. Alcuni relay lo elimineranno, alcuni lasceranno una tombstone e alcuni continueranno a servirlo a tempo indeterminato. I client che presentano l'eliminazione come definitiva stanno promettendo più di quanto il protocollo garantisca davvero.

Un altro problema pratico riguarda i riferimenti. Utenti e app possono comunque conservare localmente l'evento eliminato o citarlo altrove, anche dopo che un relay conforme ha smesso di servirlo.

---

**Fonti primarie:**
- [NIP-09 Specification](https://github.com/nostr-protocol/nips/blob/master/09.md)

**Citato in:**
- [Newsletter #11: NIP-60 Deep Dive](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)
- [Newsletter #12: News](/en/newsletters/2026-03-04-newsletter/#news)

**Vedi anche:**
- [NIP-01: Protocollo di base](/it/topics/nip-01/)
- [NIP-60: Cashu Wallet](/it/topics/nip-60/)
