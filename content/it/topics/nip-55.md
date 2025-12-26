---
title: "NIP-55: Applicazione Signer Android"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55 definisce come le applicazioni Android possono richiedere operazioni di firma da un'app signer dedicata, permettendo agli utenti di mantenere le proprie chiavi private in un'unica posizione sicura mentre usano piu' client Nostr.

## Come Funziona

NIP-55 usa l'interfaccia content provider di Android per esporre le operazioni di firma. Un'app signer si registra come content provider, e altre app Nostr possono richiedere firme senza mai accedere direttamente alla chiave privata.

Il flusso:
1. L'app client chiama il content provider del signer
2. Il signer mostra l'UI di approvazione all'utente
3. L'utente approva o nega la richiesta
4. Il signer restituisce la firma (o il rifiuto) al client

## Operazioni Principali

- **get_public_key** - Recupera la chiave pubblica dell'utente (chiamare una volta durante la connessione iniziale)
- **sign_event** - Firma un evento Nostr
- **nip04_encrypt/decrypt** - Cifra o decifra messaggi NIP-04
- **nip44_encrypt/decrypt** - Cifra o decifra messaggi NIP-44

## Avvio della Connessione

Un errore di implementazione comune e' chiamare `get_public_key` ripetutamente da processi in background. La specifica raccomanda di chiamarlo solo una volta durante la configurazione della connessione iniziale, poi memorizzare in cache il risultato.

---

**Fonti primarie:**
- [Specifica NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Menzionato in:**
- [Newsletter #1: Rilasci](/it/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2: Notizie](/it/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #2: Aggiornamenti NIP](/it/newsletters/2025-12-24-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-46: Nostr Connect](/it/topics/nip-46/)

