---
title: "NIP-5D: Nostr Web Applets"
date: 2026-04-08
translationOf: /en/topics/nip-5d.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Applications
---

NIP-5D definisce un protocollo `postMessage` per applicazioni web sandboxed ("napplets") in esecuzione in iframe che comunicano con un'applicazione host ("shell"). Estende [NIP-5A](/it/topics/nip-5a/) (siti web statici) con un livello di comunicazione runtime che offre alle web app accesso alle funzionalità Nostr senza esporre la chiave privata dell'utente.

## Come funziona

Un'applicazione shell carica una napplet in un iframe sandboxed. La napplet comunica con la shell tramite l'API `postMessage` del browser usando un protocollo di messaggi strutturato. La shell fornisce alla napplet firma Nostr, accesso ai relay e contesto utente attraverso questo canale. La sandbox dell'iframe impedisce alla napplet di accedere direttamente alla chiave privata dell'utente, quindi la shell agisce da gatekeeper per tutte le operazioni Nostr.

## Casi d'uso

- **App Nostr interattive**: creare app che leggono e scrivono eventi Nostr senza chiedere agli utenti di incollare il proprio nsec
- **Marketplace di app**: distribuire applicazioni web interattive attraverso eventi Nostr
- **Estensioni sandboxed**: aggiungere funzionalità ai client Nostr tramite napplet di terze parti

---

**Fonti primarie:**
- [NIP-5D PR #2303](https://github.com/nostr-protocol/nips/pull/2303) - proposta Nostr Web Applets

**Menzionato in:**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)

**Vedi anche:**
- [NIP-5A (Siti Web statici)](/it/topics/nip-5a/)
- [NIP-5C (Scrolls)](/it/topics/nip-5c/)
