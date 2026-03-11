---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
translationOf: /en/topics/nip-46.md
translationDate: 2026-03-11
draft: false
categories:
  - Signing
  - Protocol
---
NIP-46 definisce la firma remota tramite relay Nostr. Un client comunica con un firmatario separato, spesso chiamato bunker, così le chiavi di firma possono restare fuori dall'app che l'utente sta usando attivamente.

## Come funziona

1. Il client genera una coppia di chiavi locale usata solo per la sessione bunker.
2. La connessione viene stabilita con un URI `bunker://` oppure `nostrconnect://`.
3. Client e signer si scambiano eventi di richiesta e risposta crittografati di kind `24133` tramite relay.
4. Dopo la connessione, il client chiama `get_public_key` per conoscere la pubkey reale dell'utente per cui sta firmando.

## Metodi di connessione

- **bunker://** - Connessione avviata dal signer
- **nostrconnect://** - Connessione avviata dal client tramite QR code o deep link

I flussi `nostrconnect://` includono un segreto condiviso obbligatorio così il client può verificare che la prima risposta provenga davvero dal signer previsto. Questo impedisce semplici spoofing della connessione.

## Operazioni supportate

- `sign_event` - Firma un evento arbitrario
- `get_public_key` - Recupera la pubkey dell'utente dal signer
- `nip04_encrypt/decrypt` - Operazioni di crittografia NIP-04
- `nip44_encrypt/decrypt` - Operazioni di crittografia NIP-44
- `switch_relays` - Chiede al signer un insieme aggiornato di relay

Molte implementazioni usano anche stringhe di permesso come `sign_event:1` o `nip44_encrypt` durante la configurazione così il signer può approvare un ambito ristretto invece dell'accesso completo.

## Modello di relay e fiducia

NIP-46 sposta le chiavi private fuori dal client, ma non rimuove la fiducia dal signer. Il signer può approvare, negare o ritardare le richieste, e vede ogni operazione che il client gli chiede di eseguire. Anche la scelta dei relay conta perché il protocollo dipende dalla consegna di richieste e risposte tramite relay raggiungibili da entrambe le parti.

Il metodo `switch_relays` esiste così il signer può spostare la sessione su un insieme diverso di relay nel tempo. I client che lo ignorano funzioneranno in modo meno affidabile quando cambiano le preferenze del signer sui relay.

---

**Fonti primarie:**
- [NIP-46 Specification](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Citato in:**
- [Newsletter #1: Notable Code Changes](/it/newsletters/2025-12-17-newsletter/#amethyst-android)
- [Newsletter #3: December Recap](/it/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #7: Primal Android Becomes a Full Signing Hub](/it/newsletters/2026-01-07-newsletter/#primal-android-becomes-a-full-signing-hub)
- [Newsletter #15: NDK Collaborative Events and NIP-46 Timeout](/it/newsletters/2026-03-04-newsletter/#ndk-collaborative-events-and-nip-46-timeout)

**Vedi anche:**
- [NIP-55: Android Signer](/it/topics/nip-55/)
