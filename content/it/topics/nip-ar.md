---
title: "Buzz NIP-AR: Artefatti di canale"
date: 2026-09-30
translationOf: /en/topics/nip-ar.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Collaboration
---

NIP-AR è la specifica degli artefatti di canale **specifica del progetto** Buzz. L’etichetta qui non significa che sia stata adottata dal repository `nostr-protocol/nips` o da altri relay.

## Modello degli artefatti

Un artefatto è un record modificabile con un’identità `d` stabile, un unico canale di appartenenza indicato in un tag `h` e revisioni costituite da snapshot completi collegati tramite `prev`. Un relay accetta una modifica solo se `prev` indica la versione di testa attuale. Due revisioni in competizione non possono quindi diventare entrambe la successiva versione di testa. L’implementazione di Buzz usa il kind `45010` per gli artefatti e un marcatore di kind `45011` firmato dal relay quando un artefatto esce da un canale. Il canale di origine vede la rimozione senza apprendere la destinazione da quel marcatore.

L’[integrazione della specifica di Buzz](https://github.com/block/buzz/pull/7791) descrive il modello, e l’[integrazione dell’implementazione nel relay](https://github.com/block/buzz/pull/7919) riporta test per la gestione dei conflitti, le query sulla cronologia, gli spostamenti e i permessi dei canali. Queste integrazioni stabiliscono il comportamento del sorgente del progetto, non uno standard Nostr generale né una garanzia di distribuzione pubblica.

---

**Fonti primarie:**
- [Integrazione della specifica degli artefatti di canale di Buzz](https://github.com/block/buzz/pull/7791)
- [Integrazione dell’implementazione degli artefatti di canale di Buzz](https://github.com/block/buzz/pull/7919)

**Citato in:**
- [Newsletter #42: artefatti di canale di Buzz](/it/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
