---
title: "NIP-01: Protocollo di base"
date: 2025-12-17
translationOf: /en/topics/nip-01.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
---
NIP-01 definisce il modello base degli eventi e il protocollo dei relay su cui si costruisce il resto di Nostr. Se un client, un relay o una libreria parla Nostr, parte da qui.

## Come funziona

Gli eventi sono l'unico tipo di oggetto in Nostr. Profili, note, reaction, relay list e molti payload specifici delle applicazioni usano tutti lo stesso involucro a sette campi:

- **id**: hash SHA256 dell'evento serializzato (identificatore univoco)
- **pubkey**: chiave pubblica del creatore (hex a 32 byte, secp256k1)
- **created_at**: timestamp Unix
- **kind**: intero che classifica il tipo di evento
- **tags**: array di array per i metadati
- **content**: il payload (l'interpretazione dipende dal kind)
- **sig**: firma Schnorr che prova l'autenticità

L'`id` dell'evento è l'hash SHA256 dei dati serializzati dell'evento, non un identificatore arbitrario. Questo conta nella pratica: cambiare qualunque campo, incluso l'ordine di un tag o il timestamp, produce un evento diverso e richiede una nuova firma.

## Kinds

I kind determinano come i relay archiviano e gestiscono gli eventi:

- **Regular events** (1, 2, 4-44, 1000-9999): archiviati normalmente, vengono mantenute tutte le versioni
- **Replaceable events** (0, 3, 10000-19999): viene mantenuta solo la versione più recente per pubkey
- **Ephemeral events** (20000-29999): non vengono archiviati, vengono solo inoltrati agli iscritti
- **Addressable events** (30000-39999): versione più recente per combinazione pubkey + kind + tag `d`

I kind fondamentali includono: 0 (metadati utente), 1 (text note) e 3 (follow list).

## Comunicazione client-relay

I client comunicano con i relay tramite connessioni WebSocket usando array JSON:

**Dal client al relay:**
- `["EVENT", <event>]` - Pubblica un evento
- `["REQ", <sub-id>, <filter>, ...]` - Si iscrive agli eventi
- `["CLOSE", <sub-id>]` - Termina una subscription

**Dal relay al client:**
- `["EVENT", <sub-id>, <event>]` - Consegna un evento corrispondente
- `["EOSE", <sub-id>]` - Fine degli eventi archiviati (ora in streaming live)
- `["OK", <event-id>, <true|false>, <message>]` - Conferma di accettazione/rifiuto
- `["NOTICE", <message>]` - Messaggio leggibile dagli esseri umani

Nella pratica, la maggior parte dei NIP di livello superiore non modifica il livello di trasporto. Definiscono nuovi event kind, tag o regole di interpretazione continuando però a usare gli stessi messaggi `EVENT`, `REQ` e `CLOSE` di NIP-01.

## Filtri

I filtri specificano quali eventi recuperare, con campi che includono `ids`, `authors`, `kinds`, `#e`/`#p`/`#t`, `since`, `until` e `limit`. Le condizioni all'interno di un singolo filtro usano logica AND. Più filtri nello stesso `REQ` usano logica OR.

## Note di interoperabilità

Due dettagli causano molti bug di implementazione. Primo, i client dovrebbero trattare le risposte dei relay come eventualmente consistenti, non globalmente ordinate, perché relay diversi possono restituire sottoinsiemi diversi della cronologia. Secondo, gli eventi replaceable e addressable significano che "latest" è parte del modello di protocollo, quindi i client hanno bisogno di regole deterministiche per scegliere l'evento valido più recente quando più relay non concordano.

---

**Fonti primarie:**
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Menzionato in:**
- [Newsletter #1: NIP Deep Dive](/it/newsletters/2025-12-17-newsletter/)
- [Newsletter #19: proposta NIP-67 per la completezza di EOSE](/en/newsletters/2026-04-22-newsletter/)

**Vedi anche:**
- [NIP-19: Entità codificate in Bech32](/it/topics/nip-19/)
- [Kind Registry](/en/kind-registry/)
