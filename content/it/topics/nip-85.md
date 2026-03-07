---
title: "NIP-85: Trusted Assertions"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---
NIP-85 definisce Trusted Assertions, un sistema per delegare calcoli costosi a service provider fidati che pubblicano risultati firmati come eventi Nostr.

## Come funziona

I punteggi del Web of Trust, le metriche di engagement e altri valori calcolati richiedono di scansionare molti relay e processare grandi volumi di eventi. Questo lavoro è poco pratico sui dispositivi mobili. NIP-85 consente a provider specializzati di eseguire questi calcoli e pubblicare risultati che i client possono interrogare.

Trusted Assertions sono eventi addressable. Il tag `d` identifica il soggetto valutato, e il kind dell'evento identifica che tipo di soggetto è: pubkey (30382), eventi regolari (30383), eventi addressable (30384) e identificatori NIP-73 (30385).

Gli utenti dichiarano di quali provider si fidano tramite kind 10040. Queste liste di provider possono essere pubbliche nei tag oppure cifrate nel contenuto dell'evento con [NIP-44](/it/topics/nip-44/), cosa che conta quando un utente non vuole pubblicare apertamente i propri input di fiducia.

## Perché è importante

L'idea utile in NIP-85 è che standardizza gli output, non gli algoritmi. Due provider possono entrambi pubblicare un tag `rank` per la stessa pubkey usando formule Web of Trust diverse, gestione dei mute diversa, copertura relay diversa o euristiche anti-spam diverse. I client restano interoperabili perché il formato del risultato coincide anche quando il calcolo non coincide.

Questo si adatta meglio a Nostr rispetto a fingere che esisterà un solo servizio di ranking canonico. Gli utenti scelgono di quali assertion fidarsi.

## Modello di trust

I service provider devono firmare i propri eventi di assertion, e la specifica raccomanda chiavi di servizio diverse per algoritmi diversi o per punti di vista specifici dell'utente. Questo evita che un provider faccia collassare sistemi di ranking non correlati in un'unica identità opaca.

Il trust resta comunque locale. Un output firmato dimostra quale provider ha pubblicato un punteggio, non che il punteggio sia corretto. I client hanno bisogno di una policy su quali chiavi provider usare, da quali relay recuperare i dati e come gestire assertion in conflitto.

## Note di interoperabilità

NIP-85 va oltre persone e post. Il kind 30385 consente ai provider di valutare identificatori esterni NIP-73 come libri, siti web, hashtag e luoghi. Questo crea un percorso per dati interoperabili di reputazione ed engagement attorno a soggetti esterni a Nostr stesso.

---

**Fonti principali:**
- [NIP-85 Specification](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #2223](https://github.com/nostr-protocol/nips/pull/2223) - Linee guida per la discoverability dei service provider

**Menzionato in:**
- [Newsletter #10: NIP-85 Deep Dive](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #11: NIP-85 Service Provider Discoverability](/en/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #12: Protocol Recap](/en/newsletters/2026-03-04-newsletter/)

**Vedi anche:**
- [NIP-44: Encrypted Payloads](/it/topics/nip-44/)
- [NIP-73: External Content IDs](/it/topics/nip-73/)
- [Web of Trust](/it/topics/web-of-trust/)
