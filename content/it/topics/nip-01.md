---
title: "NIP-01: Protocollo Base"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-01 definisce il protocollo fondamentale per Nostr, stabilendo le strutture dati e i pattern di comunicazione su cui si basano tutti gli altri NIP.

## Eventi

Gli eventi sono l'unico tipo di oggetto in Nostr. Ogni dato, da un aggiornamento del profilo a un post di testo a una reazione, e' rappresentato come un evento con questa struttura:

- **id**: Hash SHA256 dell'evento serializzato (identificatore unico)
- **pubkey**: La chiave pubblica del creatore (32 byte esadecimali, secp256k1)
- **created_at**: Timestamp Unix
- **kind**: Intero che categorizza il tipo di evento
- **tags**: Array di array per i metadati
- **content**: Il payload (l'interpretazione dipende dal kind)
- **sig**: Firma Schnorr che prova l'autenticita'

## Kind

I kind determinano come i relay memorizzano e gestiscono gli eventi:

- **Eventi regolari** (1, 2, 4-44, 1000-9999): Memorizzati normalmente, tutte le versioni mantenute
- **Eventi sostituibili** (0, 3, 10000-19999): Solo l'ultimo per pubkey viene mantenuto
- **Eventi effimeri** (20000-29999): Non memorizzati, solo inoltrati ai sottoscrittori
- **Eventi indirizzabili** (30000-39999): Ultimo per combinazione pubkey + kind + tag `d`

I kind principali includono: 0 (metadati utente), 1 (nota di testo), 3 (lista follow).

## Comunicazione Client-Relay

I client comunicano con i relay tramite connessioni WebSocket usando array JSON:

**Da client a relay:**
- `["EVENT", <event>]` - Pubblica un evento
- `["REQ", <sub-id>, <filter>, ...]` - Sottoscrivi agli eventi
- `["CLOSE", <sub-id>]` - Termina una sottoscrizione

**Da relay a client:**
- `["EVENT", <sub-id>, <event>]` - Consegna evento corrispondente
- `["EOSE", <sub-id>]` - Fine degli eventi memorizzati (ora streaming live)
- `["OK", <event-id>, <true|false>, <message>]` - Conferma accettazione/rifiuto
- `["NOTICE", <message>]` - Messaggio leggibile

## Filtri

I filtri specificano quali eventi recuperare, con campi che includono: `ids`, `authors`, `kinds`, `#e`/`#p`/`#t` (valori tag), `since`/`until`, e `limit`. Le condizioni in un filtro usano logica AND; piu' filtri in una `REQ` si combinano con logica OR.

---

**Fonti primarie:**
- [Specifica NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Menzionato in:**
- [Newsletter #1: Approfondimento NIP](/it/newsletters/2025-12-17-newsletter/#nip-deep-dive-nip-01-and-nip-19)

**Vedi anche:**
- [NIP-19: Entita' Codificate Bech32](/it/topics/nip-19/)
- [Registro Kind](/it/kind-registry/)

