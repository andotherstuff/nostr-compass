---
title: "Protocollo Marmot"
date: 2025-12-17
translationOf: /en/topics/marmot.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot è un protocollo per la messaggistica di gruppo end-to-end encrypted su Nostr. Combina l'identità e la rete relay di Nostr con MLS per la gestione delle chiavi di gruppo, forward secrecy e post-compromise security.

## Come funziona

Marmot usa Nostr per identità, trasporto relay e distribuzione degli eventi, poi stratifica MLS sopra per i cambiamenti di membership e la cifratura dei messaggi. A differenza di [NIP-17](/it/topics/nip-17/), che si concentra sulla messaggistica uno-a-uno, Marmot è pensato per gruppi in cui i membri entrano, escono o ruotano le chiavi nel tempo.

## Perché conta

MLS offre a Marmot proprietà che gli schemi di direct message di Nostr non forniscono da soli: evoluzione dello stato del gruppo, semantica di rimozione dei membri e recupero dopo una compromissione tramite aggiornamenti successivi delle chiavi.

Questa divisione del lavoro è l'intuizione utile. Nostr risolve identità e trasporto in una rete aperta. MLS risolve l'accordo autenticato sulle chiavi di gruppo. Marmot è il livello di collegamento tra i due.

## Stato delle implementazioni

Il protocollo resta sperimentale, ma oggi ha più implementazioni e uso attivo in applicazioni. [MDK](https://github.com/marmot-protocol/mdk) è lo stack Rust di riferimento, [marmot-ts](https://github.com/marmot-protocol/marmot-ts) porta il modello in TypeScript e applicazioni come [White Noise](https://github.com/marmot-protocol/whitenoise), [Amethyst](https://github.com/vitorpamplona/amethyst), Pika e Vector hanno già usato componenti compatibili con Marmot.

Il lavoro recente si è concentrato su hardening e interoperabilità. Fix guidati da audit sono arrivati all'inizio del 2026, e MIP-03 ha introdotto una risoluzione deterministica dei commit per permettere ai client di convergere quando cambiamenti concorrenti di stato del gruppo corrono su relay diversi.

Nell'aprile 2026, Amethyst ha allineato il proprio MDK embedded ai formati wire MIP-01 e MIP-05: [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) ha aggiunto codifica VarInt e validazione round-trip, [PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) ha aggiunto il supporto MIP-00 KeyPackage Relay List, [PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436) ha chiuso i gap residui emersi dai test con White Noise, [PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466) ha corretto il framing dei commit MLS, [PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471) ha corretto un bug di decrittazione nel layer esterno e [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493) ha aggiunto validazione crittografica completa dei commit. [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) pubblica inoltre `amy`, una CLI per operazioni di gruppo Marmot e MLS.

MDK ha pubblicato [PR #261](https://github.com/marmot-protocol/mdk/pull/261) per calcolare le `RequiredCapabilities` del gruppo come LCD delle capability degli invitati, sbloccando inviti tra versioni diverse di Amethyst e White Noise. [PR #262](https://github.com/marmot-protocol/mdk/pull/262) valida i key package degli invitati prima di persistere il signer del creatore, [PR #264](https://github.com/marmot-protocol/mdk/pull/264) converge il formato wire di SelfUpdate tra implementazioni e [PR #265](https://github.com/marmot-protocol/mdk/pull/265) espone un accessor `group_required_proposals`.

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) è nel mezzo di una refactor multi-fase dai singleton globali a viste per-account `AccountSession`: [PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743) ha impostato la scaffolding di `AccountSession` e `AccountManager`, le fasi successive hanno migrato relay handles, draft, settings, operazioni messaggi, lettura e scrittura dei gruppi, membership, notifiche push, letture dei key package e creazione dei gruppi, e [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770) porta ora il dispatch degli eventi a livello di sessione. Sul lato TypeScript, [marmot-ts PR #68](https://github.com/marmot-protocol/marmot-ts/pull/68) migra i key package all'evento addressable kind `30443`.

---

**Fonti primarie:**
- [Marmot Protocol Repository](https://github.com/marmot-protocol/marmot)
- [MLS Protocol](https://messaginglayersecurity.rocks/)
- [Marmot Development Kit (MDK)](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)
- [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)
- [White Noise client](https://github.com/marmot-protocol/whitenoise)
- [Amethyst PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) - allineamento wire format MIP-01/MIP-05
- [Amethyst PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) - MIP-00 KeyPackage Relay List
- [Amethyst PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) - Amy CLI

**Menzionato in:**
- [Newsletter #1: News](/it/newsletters/2025-12-17-newsletter/)
- [Newsletter #1: Releases](/it/newsletters/2025-12-17-newsletter/)
- [Newsletter #4](/it/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/it/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/it/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: Amethyst MIP compliance](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: MDK interop work](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: whitenoise-rs session refactor](/en/newsletters/2026-04-22-newsletter/)

**Vedi anche:**
- [MLS (Message Layer Security)](/it/topics/mls/)
- [MIP-05: Privacy-Preserving Push Notifications](/it/topics/mip-05/)
- [NIP-17: Messaggi diretti privati](/it/topics/nip-17/)
- [NIP-59: Gift Wrap](/it/topics/nip-59/)
