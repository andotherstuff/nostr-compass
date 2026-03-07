---
title: "Asserzioni affidabili sui relay"
date: 2026-01-21
translationOf: /en/topics/trusted-relay-assertions.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Relays
---
Trusted Relay Assertions è l'idea di pubblicare su Nostr valutazioni firmate di relay da parte di terzi, così i client possono scegliere i relay con più contesto rispetto ai soli metadati auto-dichiarati. Il building block standardizzato attuale è [NIP-85: Trusted Assertions](/it/topics/nip-85/), che definisce come gli utenti si fidano dei provider e come i provider pubblicano risultati calcolati e firmati.

## Come funziona

La selezione dei relay ha tre livelli. [NIP-11: Relay Information Document](/it/topics/nip-11/) copre ciò che un relay dice di sé stesso. [NIP-66: Relay Discovery and Liveness Monitoring](/it/topics/nip-66/) copre ciò che gli osservatori possono misurare, come disponibilità e latenza. Trusted relay assertions cercano di colmare il divario restante: cosa conclude una terza parte a partire da quei dati, e se un client decide di fidarsi di quella conclusione.

Nel modello più ampio di NIP-85, gli utenti indicano provider fidati con eventi di kind `10040`, e i provider pubblicano eventi addressable di asserzione firmati. Un'applicazione di relay scoring avrebbe poi bisogno di altri due elementi su cui i client concordano: come un relay viene identificato come soggetto, e quali result tag rappresentano il punteggio e le prove che lo supportano.

Questa distinzione è importante perché il trasporto e la delega di fiducia sono standardizzati, ma il modello di scoring specifico per i relay è ancora un pattern applicativo. Provider diversi possono legittimamente non essere d'accordo su cosa renda un relay affidabile.

## Modello di fiducia

I punteggi di fiducia dei relay non sono fatti oggettivi. Un provider può dare priorità all'uptime e al write throughput, un altro può dare priorità alla giurisdizione legale, alla politica di moderazione o all'identità dell'operatore, e un terzo può preoccuparsi soprattutto della resistenza alla sorveglianza. Un client utile dovrebbe mostrare chi ha prodotto il punteggio, non solo il punteggio stesso.

È qui che entra in gioco anche il [Web of Trust](/it/topics/web-of-trust/). Se un client si fida già di certe persone o servizi, può preferire valutazioni dei relay che provengono da quello stesso vicinato sociale invece di fingere che esista una singola classifica globale.

## Perché è importante

Per i remote signer di [NIP-46](/it/topics/nip-46/), le connessioni wallet o qualsiasi app che suggerisca relay poco familiari, le valutazioni di relay da parte di terzi possono ridurre la fiducia cieca nei default. Insieme alle relay list di [NIP-65](/it/topics/nip-65/), i client possono separare "quali relay uso" da "di quali relay mi fido per questo compito".

La principale riserva sulla correttezza riguarda l'ambito. La copertura della newsletter di gennaio 2026 descriveva il relay trust scoring come una proposta dedicata, ma lo standard fuso nel repository dei NIP è il formato più ampio di [NIP-85: Trusted Assertions](/it/topics/nip-85/). Il relay scoring resta un caso d'uso costruito sopra quel modello, non un wire format separato e definitivo per la fiducia nei relay.

---

**Fonti primarie:**
- [Specifica NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #1534: Trusted Assertions](https://github.com/nostr-protocol/nips/pull/1534)

**Citato in:**
- [Newsletter #6: Notizie](/en/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [Newsletter #6: Aggiornamenti NIP](/en/newsletters/2026-01-21-newsletter/#nip-updates)
- [Newsletter #7: Aggiornamenti NIP](/en/newsletters/2026-01-28-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-11: Relay Information Document](/it/topics/nip-11/)
- [NIP-66: Relay Discovery and Liveness Monitoring](/it/topics/nip-66/)
- [NIP-85: Trusted Assertions](/it/topics/nip-85/)
- [Web of Trust](/it/topics/web-of-trust/)
