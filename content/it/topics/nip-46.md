---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46 definisce la firma remota, permettendo a un'applicazione signer di mantenere le chiavi mentre i client richiedono firme tramite relay Nostr.

## Come Funziona

1. Il signer genera un URI di connessione (`bunker://` o `nostrconnect://`)
2. L'utente incolla l'URI in un client
3. Il client invia richieste di firma come eventi cifrati al relay del signer
4. Il signer richiede l'approvazione dell'utente, restituisce gli eventi firmati

## Metodi di Connessione

- **bunker://** - Connessione iniziata dal signer
- **nostrconnect://** - Connessione iniziata dal client tramite codice QR o deep link

## Operazioni Supportate

- `sign_event` - Firma un evento arbitrario
- `get_public_key` - Recupera la chiave pubblica del signer
- `nip04_encrypt/decrypt` - Operazioni di cifratura NIP-04
- `nip44_encrypt/decrypt` - Operazioni di cifratura NIP-44

---

**Fonti primarie:**
- [Specifica NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Menzionato in:**
- [Newsletter #1: Modifiche Notevoli al Codice](/it/newsletters/2025-12-17-newsletter/#amethyst-android)

**Vedi anche:**
- [NIP-55: Signer Android](/it/topics/nip-55/)

