---
title: "NIP-77: Riconciliazione Negentropy"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-77.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Sync
---

NIP-77 definisce come i relay e i client Nostr utilizzano il protocollo di riconciliazione degli insiemi [Negentropy](/it/topics/negentropy/) per sincronizzare efficientemente gli insiemi di eventi, trovando quali eventi mancano da ciascun lato senza ritrasmettere l'intero dataset.

## Come funziona

La riconciliazione Negentropy viene eseguita su una connessione WebSocket utilizzando un tipo di messaggio dedicato. Il client e il relay si scambiano impronte digitali di intervallo compatte sui loro insiemi di eventi ordinati, convergendo solo sugli intervalli che differiscono. Una volta identificate le differenze, vengono trasferiti solo gli ID degli eventi mancanti (e poi gli eventi mancanti stessi).

NIP-77 standardizza il framing dei messaggi affinché qualsiasi client e relay che implementa la specifica possa negoziare una sessione di sincronizzazione efficiente. Il protocollo utilizza i tipi di messaggio `NEG-OPEN`, `NEG-MSG` e `NEG-CLOSE` sulla connessione WebSocket Nostr esistente.

## Perché è importante

La sincronizzazione Nostr tradizionale utilizza filtri `since` basati sui timestamp, che possono perdere eventi a causa della deriva dell'orologio, eventi con timestamp identici o eventi che arrivano fuori ordine. Negentropy confronta insiemi di eventi reali invece di affidarsi ai timestamp, fornendo una sincronizzazione completa e dimostrabile in molti meno round trip rispetto al polling ingenuo.

Questo è particolarmente utile per:
- Client mobili che si aggiornano dopo essere stati offline
- Replicazione da relay a relay
- Sincronizzazione relay locale (come nell'aggregatore relay di Citrine)

## Implementazioni

- [Citrine](https://github.com/greenart7c3/Citrine) — [PR #139](https://github.com/greenart7c3/Citrine/pull/139) ha aggiunto il supporto NIP-77 per la sincronizzazione efficiente tramite riconciliazione degli insiemi nel nodo relay Android
- [strfry](https://github.com/hoytech/strfry) — supporto Negentropy lato relay
- [nostr-tools](https://github.com/nbd-wtf/nostr-tools) — implementazione Negentropy lato client

---

**Fonti primarie:**
- [Specifica NIP-77](https://github.com/nostr-protocol/nips/blob/master/77.md)
- [Protocollo Negentropy](https://github.com/hoytech/negentropy)

**Menzionato in:**
- [Newsletter #22: Citrine v3.0.0-pre1](/it/newsletters/2026-05-14-newsletter/#citrine-v300-pre1-lands-built-in-tor-and-relay-aggregation)

**Vedi anche:**
- [Negentropy](/it/topics/negentropy/)
