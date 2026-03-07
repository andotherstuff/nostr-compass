---
title: "NIP-63: Paywall / Contenuti Premium"
date: 2025-12-17
translationOf: /en/topics/nip-63/
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Monetization
---
NIP-63 è una proposta di standard per gestire contenuti con accesso limitato all'interno del protocollo Nostr, permettendo ai creatori di richiedere un pagamento prima di rivelare il contenuto.

## Come Funziona

I creatori di contenuti possono pubblicare eventi in cui il contenuto completo è cifrato oppure nascosto dietro un paywall. Dopo la verifica del pagamento, il contenuto viene sbloccato per l'utente pagante.

La proposta riguarda intenzionalmente la superficie di protocollo per i contenuti premium, non l'imposizione di un singolo rail di pagamento o di un unico modello di business. Questo la mantiene flessibile, ma significa anche che wallet, client ed editori devono ancora concordare in pratica il flusso di sblocco.

## Perché Conta

Senza un formato condiviso, ogni sistema di paywall su Nostr diventa un silo separato. Un NIP comune permetterebbe a un client di pubblicare contenuti premium e a un altro client di capire che il contenuto è protetto, cosa deve essere pagato e quando deve essere rivelato.

Questo però non garantisce ancora la portabilità. NIP-63 è ancora una proposta nella [PR #2156](https://github.com/nostr-protocol/nips/pull/2156), quindi le implementazioni possono ancora divergere mentre il design è in discussione.

## Casi d'Uso

- Articoli riservati agli abbonati
- Contenuti multimediali premium
- Eventi pay-per-view
- Accesso esclusivo ai creatori

## Compromessi

I metadati del paywall possono essere pubblici anche quando il payload premium non lo è. Questo dà ai client abbastanza informazioni per presentare un'offerta, ma significa anche che l'esistenza di contenuti a pagamento è visibile a chiunque possa leggere l'evento.

I creatori devono anche pensare a cosa succede dopo lo sblocco. Una volta che il testo in chiaro viene mostrato a un utente pagante, il protocollo non può impedire a quell'utente di copiarlo altrove.

---

**Fonti primarie:**
- [Proposta NIP-63 (PR #2156)](https://github.com/nostr-protocol/nips/pull/2156)

**Menzionato in:**
- [Newsletter #1: Aggiornamenti NIP](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-57: Zaps](/it/topics/nip-57/)
