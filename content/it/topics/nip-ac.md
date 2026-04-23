---
title: "NIP-AC: Chiamate vocali e video P2P"
date: 2026-04-08
translationOf: /en/topics/nip-ac.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Messaging
---

NIP-AC propone un protocollo per chiamate vocali e video peer-to-peer su Nostr. La specifica usa eventi Nostr per il signaling della chiamata, come offer, answer e candidati ICE, e WebRTC per il trasporto effettivo dei media, mantenendo decentralizzata la fase di setup della chiamata e usando API browser standard per audio e video.

## Come funziona

Chi chiama pubblica un evento di offerta contenente un'offerta WebRTC Session Description Protocol (SDP), taggata con la pubkey del destinatario. Il destinatario risponde con un evento SDP answer. Entrambe le parti si scambiano eventi con candidati ICE per negoziare il percorso di rete. Una volta stabilita la connessione WebRTC, i media scorrono direttamente tra i peer senza coinvolgere i relay.

Gli eventi di signaling sono cifrati, quindi i relay non possono osservare chi sta chiamando chi. La macchina a stati della chiamata gestisce le transizioni di offer, answer, reject, busy e hangup.

## Implementazioni

- [Amethyst](https://github.com/vitorpamplona/amethyst) sta sviluppando il supporto a NIP-AC con una suite di test per la macchina a stati delle chiamate e gestione delle offerte di chiamata obsolete.

---

**Fonti primarie:**
- [NIP-AC PR #2301](https://github.com/nostr-protocol/nips/pull/2301) - chiamate vocali e video P2P su WebRTC

**Menzionato in:**
- [Nostr Compass #17 (2026-04-08)](/it/newsletters/2026-04-08-newsletter/)

**Vedi anche:**
- [NIP-44 (payload cifrati)](/it/topics/nip-44/)
