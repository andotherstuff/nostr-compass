---
title: "FIPS"
date: 2026-02-25
translationOf: /en/topics/fips.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Networking
  - Infrastructure
---
FIPS (Free Internetworking Peering System) è un protocollo di mesh networking auto-organizzato che usa coppie di chiavi secp256k1 in stile Nostr come identità dei nodi.

## Come funziona

FIPS punta a far funzionare il networking peer-to-peer senza server centrali o autorità di certificazione. I nodi scoprono i vicini, costruiscono lo stato di instradamento e inoltrano i pacchetti usando solo conoscenza locale.

Il design combina uno spanning tree con dati di raggiungibilità basati su bloom filter. Ogni nodo riceve coordinate relative all'albero, poi instrada in modo greedy verso la destinazione. Se il greedy routing fallisce, l'albero fornisce comunque un percorso di fallback.

Due livelli di cifratura proteggono il traffico. La cifratura del link layer (pattern Noise IK) protegge la comunicazione hop-by-hop tra nodi vicini. La cifratura del session layer (pattern Noise XK) fornisce protezione end-to-end contro i router intermedi.

## Perché conta

FIPS riusa lo stesso modello di chiavi che gli sviluppatori Nostr già conoscono, ma lo applica all'instradamento dei pacchetti invece che agli eventi sociali. Questo gli dà un modello di identità semplice: l'identità di rete è la chiave crittografica, non un'allocazione IP o una catena di certificati.

Anche il design indipendente dal trasporto conta. Lo stesso modello di instradamento e identità può, in linea di principio, funzionare su UDP, Ethernet, Bluetooth o LoRa, il che rende FIPS interessante per ambienti di rete ostili o inaffidabili.

## Stato dell'implementazione

Come coperto in Compass, l'implementazione Rust attuale include già un trasporto UDP funzionante e discovery basata su bloom filter. Il bootstrap basato su relay è ancora lavoro futuro, quindi oggi il protocollo è più un substrato di rete che un sostituto completo dei relay Nostr.

---

**Fonti primarie:**
- [FIPS Repository](https://github.com/jmcorgan/fips)
- [Design Documentation](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md)

**Citato in:**
- [Newsletter #11: FIPS News](/en/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**Vedi anche:**
- [Marmot Protocol](/it/topics/marmot/)
