---
title: "NIP-85"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---

NIP-85 definisce le Trusted Assertions, un sistema per delegare calcoli costosi a provider di servizi fidati che pubblicano i risultati firmati come event Nostr.

## Come Funziona

I punteggi Web of Trust, le metriche di engagement e altri valori calcolati richiedono la scansione di molti relay e l'elaborazione di grandi volumi di event. Questo lavoro è impraticabile su dispositivi mobili. NIP-85 permette a provider specializzati di eseguire questi calcoli e pubblicare risultati che i client possono interrogare.

I provider di servizi pubblicizzano le proprie capacità tramite event kind 30085. I client scoprono i provider interrogando questi annunci da pubkey che l'utente già segue o di cui si fida. I risultati arrivano come event kind 30382 firmati dal provider.

## Caratteristiche Principali

- Calcolo delegato per metriche ad alto consumo di risorse
- Scoperta dei provider attraverso il grafo sociale
- Asserzioni firmate per risultati verificabili
- Decisioni di fiducia lato client

---

**Fonti principali:**
- [Specifica NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md)

**Citato in:**
- [Newsletter #10: Approfondimento NIP-85 Trusted Assertions](/it/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #11: Scoperta dei Provider di Servizi NIP-85](/it/newsletters/2026-02-25-newsletter/#aggiornamenti-nip)

**Vedi anche:**
- [Web of Trust](/it/topics/web-of-trust/)
