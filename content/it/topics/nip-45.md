---
title: "NIP-45: Event Counting"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45 definisce come i client possono chiedere ai relay di contare eventi corrispondenti a un filtro evitando di trasferire gli eventi stessi. I client inviano un messaggio COUNT con la stessa sintassi filtro di REQ, e i relay rispondono con un conteggio.

## Come Funziona

Un client invia una richiesta COUNT con un subscription ID e un filtro:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

Il relay risponde con il conteggio:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

Questo evita di scaricare centinaia o migliaia di eventi solo per visualizzare un numero.

## Conteggio Approssimativo HyperLogLog

A febbraio 2026, NIP-45 supporta il conteggio approssimativo HyperLogLog (HLL) ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). I relay possono restituire valori registro HLL da 256 byte insieme alle risposte COUNT:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

HLL risolve un problema fondamentale, il conteggio di eventi distinti attraverso più relay. Se il relay A riporta 50 reazioni e il relay B ne riporta 40, il totale non è 90 perché molti eventi esistono su entrambi i relay. I registri HLL provenienti da più relay possono essere uniti prendendo il valore massimo a ciascuna posizione registro, deduplicando automaticamente attraverso la rete.

Con 256 registri, l'errore standard è di circa il 5,2%. Le correzioni HyperLogLog++ migliorano l'accuratezza per cardinalità ridotte sotto i ~200 eventi. Anche solo due eventi reazione consumano più banda del payload HLL da 256 byte, rendendo il meccanismo efficiente per qualsiasi conteggio non banale.

La spec fissa il numero di registri a 256 per l'interoperabilità tra tutte le implementazioni relay.

## Casi d'Uso

Le metriche social (conteggi follower, conteggi reazioni, conteggi repost) sono l'applicazione principale. In assenza di HLL, i client devono interrogare un singolo relay "fidato" per i conteggi (centralizzando il dato) o scaricare tutti gli eventi da tutti i relay per deduplicare localmente (sprecando banda). HLL fornisce conteggi approssimativi cross-relay con 256 byte di overhead per relay.

---

**Fonti primarie**
- [NIP-45, Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561, HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)

**Menzionato in**
- [Newsletter #9, NIP Deep Dive](/it/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-45-event-counting-e-hyperloglog)
- [Newsletter #9, Aggiornamenti NIP](/it/newsletters/2026-02-11-newsletter/#aggiornamenti-nip)

**Vedi anche**
- [NIP-11, Relay Information Document](/it/topics/nip-11/)
