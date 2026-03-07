---
title: "Marmot Protocol"
date: 2025-12-17
translationOf: /en/topics/marmot/
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---
Marmot è un protocollo per la messaggistica di gruppo end-to-end encrypted su Nostr. Combina il modello di identità e la rete di relay di Nostr con MLS per la gestione delle chiavi di gruppo, la forward secrecy e la post-compromise security.

## Come funziona

Marmot usa Nostr per identità, trasporto via relay e distribuzione degli eventi, poi aggiunge MLS sopra per i cambiamenti di appartenenza al gruppo e la cifratura dei messaggi. A differenza di [NIP-17](/it/topics/nip-17/), che si concentra sulla messaggistica uno-a-uno, Marmot è costruito per gruppi in cui i membri entrano, escono o ruotano le chiavi nel tempo.

## Perché conta

MLS dà a Marmot proprietà che gli schemi di direct message di Nostr non forniscono da soli: evoluzione dello stato del gruppo, semantica di rimozione dei membri e recupero dopo una compromissione tramite aggiornamenti successivi delle chiavi.

Questa divisione del lavoro è l'idea utile. Nostr risolve identità e trasporto in una rete aperta. MLS risolve l'accordo autenticato sulle chiavi di gruppo. Marmot è il livello di collegamento tra i due.

## Stato dell'implementazione

Il protocollo resta sperimentale, ma ora ha più implementazioni e un uso attivo nelle applicazioni. MDK è lo stack Rust di riferimento principale, `marmot-ts` porta il modello in TypeScript e applicazioni come White Noise, Pika e Vector hanno usato componenti compatibili con Marmot.

Il lavoro recente si è concentrato su hardening e interoperabilità. Correzioni guidate da audit sono arrivate all'inizio del 2026, e MIP-03 ha introdotto una risoluzione deterministica dei commit così che i client possano convergere quando cambiamenti concorrenti dello stato di gruppo corrono sui relay.

---

**Fonti primarie:**
- [Marmot Protocol Repository](https://github.com/marmot-protocol/marmot)
- [NIP-104: MLS-based Encrypted Group Chats](/it/topics/nip-104/)
- [Marmot Development Kit](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)

**Citato in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: Releases](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #4](/en/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**Vedi anche:**
- [MLS (Message Layer Security)](/it/topics/mls/)
- [MIP-05: Privacy-Preserving Push Notifications](/it/topics/mip-05/)
- [NIP-17: Private Direct Messages](/it/topics/nip-17/)
- [NIP-59: Gift Wrap](/it/topics/nip-59/)
