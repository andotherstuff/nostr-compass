---
title: "NIP-06: derivazione delle chiavi da mnemonico"
date: 2026-10-28
translationOf: /en/topics/nip-06.md
translationDate: 2026-10-28
draft: false
categories: ["Identity", "Keys"]
---

NIP-06 descrive come derivare una coppia di chiavi Nostr da una seed phrase mnemonica. L'[attuale testo ufficiale di NIP-06](https://github.com/nostr-protocol/nips/blob/master/06.md) è contrassegnato come bozza e opzionale, e riporta questo avviso:

> __Avviso__ `unrecommended`: preferite un singolo nsec

Questa pagina tratta NIP-06 per ragioni di compatibilità storica. Non raccomanda di adottare la derivazione da seed.

## Come funziona

Secondo la [specifica attuale](https://github.com/nostr-protocol/nips/blob/master/06.md), BIP39 serve a generare le parole mnemoniche e a ricavarne un seed binario. Successivamente BIP32 deriva le chiavi lungo il percorso `m/44'/1237'/<account>'/0/0`, dove 1237 è la voce di Nostr in SLIP44. Un client di base può usare l'account 0. Incrementando il valore dell'account si ottengono altre chiavi dallo stesso seed. Due implementazioni riproducono la stessa identità solo se concordano sui passaggi di derivazione e usano le codifiche corrette per il risultato.

## Vettori di test

Un [commit del 12 ottobre 2023](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b) ha aggiunto due vettori di test, uno costruito a partire da un mnemonico di 12 parole e l'altro da un mnemonico di 24 parole. Per ciascuno sono elencate la chiave privata e la chiave pubblica attese in esadecimale, insieme alle corrispondenti codifiche nsec e npub. Gli sviluppatori possono servirsi dei vettori per verificare le implementazioni in modo incrociato. I vettori non dicono nulla sulla custodia delle chiavi, non certificano la sicurezza e non garantiscono un'interoperabilità universale.

## Vedi anche

- [NIP-01](/it/topics/nip-01/)

**Fonti primarie:**

- [NIP-06 (attuale)](https://github.com/nostr-protocol/nips/blob/master/06.md)
- [Commit che aggiunge i vettori di test di NIP-06 (12 ottobre 2023)](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b)

**Citato in:**

- [Newsletter #46](/it/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)
