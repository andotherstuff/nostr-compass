---
title: "NIP-45: Conteggio degli eventi"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Protocol
---
NIP-45 definisce come i client chiedono ai relay di contare gli eventi che corrispondono a un filtro senza trasferire gli eventi corrispondenti. Riusa la sintassi dei filtri di NIP-01, quindi un client può spesso trasformare una `REQ` esistente in una richiesta `COUNT` con gli stessi filtri.

## Come funziona

Un client invia una richiesta `COUNT` con un ID di sottoscrizione e un filtro:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

Il relay risponde con un conteggio:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

Questo evita di scaricare centinaia o migliaia di eventi solo per mostrare un numero. Se un client invia più filtri in una richiesta `COUNT`, il relay li aggrega in un unico risultato, proprio come più filtri `REQ` vengono combinati con OR.

## Conteggio approssimato con HyperLogLog

A partire da febbraio 2026, NIP-45 supporta il conteggio approssimato con HyperLogLog (HLL) ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). I relay possono contrassegnare un risultato come approssimato e, per la deduplicazione tra relay, possono restituire 256 registri HLL insieme al conteggio:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<512-char hex string>"}]
```

HLL risolve un problema fondamentale: contare eventi distinti su più relay. Se il relay A segnala 50 reaction e il relay B ne segnala 40, il totale non è 90 perché molti eventi esistono su entrambi i relay. I client uniscono i valori HLL prendendo il valore massimo in ogni posizione del registro, ottenendo così una stima sull'intera rete senza scaricare gli eventi grezzi.

La specifica fissa il numero di registri a 256 per l'interoperabilità. Questo mantiene piccolo il payload e rende pratico il caching lato relay perché ogni relay calcola la stessa disposizione dei registri per lo stesso filtro idoneo.

## Note di interoperabilità

HLL è definito solo per filtri con un attributo tag, perché l'offset usato per costruire i registri deriva dal primo valore taggato nel filtro. La specifica indica anche un piccolo insieme di query canoniche, incluse reaction, repost, quote, reply, commenti e conteggi dei follower. Questi sono i conteggi più facili da precalcolare o mettere in cache per i relay.

## Perché è importante

Conteggi dei follower, delle reaction e delle reply sono i principali casi d'uso. Senza NIP-45, i client devono o fidarsi della vista locale di un singolo relay oppure scaricare tutti gli eventi corrispondenti e deduplicarli localmente. NIP-45 mantiene il conteggio dentro il relay, e HLL rende pratici i conteggi multi-relay senza trasformare un relay nell'autorità.

---

**Fonti primarie:**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)

**Citato in:**
- [Newsletter #9: NIP Deep Dive](/en/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-45-event-counting-and-hyperloglog)
- [Newsletter #9: NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12: Five Years of Nostr Februaries](/en/newsletters/2026-03-04-newsletter/)

**Vedi anche:**
- [NIP-11: Relay Information Document](/it/topics/nip-11/)
