---
title: "Buzz NIP-FI: Asserzioni di identità federata"
date: 2026-09-30
translationOf: /en/topics/nip-fi.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Identity
  - Relays
---

NIP-FI è la specifica delle asserzioni di identità federata **specifica del progetto** Buzz. Il nome non implica l’adozione da parte del repository `nostr-protocol/nips` né l’interoperabilità con relay esterni a Buzz.

## Ingresso HTTP

Per le richieste HTTP protette in modalità di applicazione obbligatoria, Buzz associa un’asserzione di identità federata a un event di autorizzazione firmato NIP-98. La chiave pubblica Nostr dimostrata dalla firma HTTP deve corrispondere alla chiave indicata nell’asserzione. Le prove mancanti, non corrispondenti o non verificabili vengono rifiutate. Buzz usa questa associazione per collegare la decisione di autorizzazione di un emittente di identità esterno alla chiave Nostr che effettua la richiesta.

La [revisione della specifica del progetto](https://github.com/block/buzz/pull/7254) definisce il modello di applicazione. L’[implementazione integrata per l’ingresso HTTP](https://github.com/block/buzz/pull/7264) copre le superfici HTTP protette di Buzz, inclusi i percorsi del bridge del relay, dei contenuti multimediali, dei workflow e di Git. L’integrazione riporta test sul sorgente; non significa che un altro relay Nostr implementi la stessa politica.

---

**Fonti primarie:**
- [Revisione della specifica NIP-FI di Buzz](https://github.com/block/buzz/pull/7254)
- [Implementazione dell’ingresso HTTP di Buzz](https://github.com/block/buzz/pull/7264)

**Citato in:**
- [Newsletter #42: controlli di identità di Buzz](/it/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
