---
title: "NIP-65: Metadati Lista Relay"
date: 2026-01-13
draft: false
categories:
  - Protocol
  - Discovery
---

NIP-65 definisce event di kind 10002 che pubblicizzano quali relay un utente preferisce per leggere e scrivere. Questi metadati aiutano altri utenti e client a localizzare i vostri contenuti attraverso la rete distribuita di relay, abilitando il "modello outbox" che distribuisce il carico e migliora la resistenza alla censura.

## Struttura

Una lista di relay è un event sostituibile (kind 10002) contenente tag `r` per ogni relay che l'utente vuole pubblicizzare. L'event sostituisce qualsiasi lista di relay precedente della stessa pubkey.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "sig1234..."
}
```

Ogni tag `r` contiene un URL WebSocket del relay e un marcatore opzionale che indica come l'utente interagisce con quel relay. Il marcatore `read` significa che l'utente consuma event da questo relay, quindi altri dovrebbero pubblicare lì per raggiungere l'utente. Il marcatore `write` significa che l'utente pubblica su questo relay, quindi altri dovrebbero iscriversi lì per vedere i contenuti dell'utente. Omettere il marcatore indica sia lettura che scrittura.

Il campo `content` è vuoto per gli event di lista relay.

## Il Modello Outbox

NIP-65 abilita un pattern di distribuzione dei contenuti decentralizzato chiamato "modello outbox". Invece di avere tutti che pubblicano e leggono dagli stessi relay centrali, gli utenti pubblicano sui loro relay preferiti e i client scoprono dinamicamente dove trovare i contenuti di ogni utente.

Quando Alice vuole trovare i post di Bob, il suo client prima recupera l'event kind 10002 di Bob da qualsiasi relay che lo abbia. Poi estrae i relay che Bob ha marcato per `write` poiché sono quelli dove lui pubblica. Il suo client si iscrive a quei relay per gli event di Bob. Quando Alice vuole inviare a Bob un messaggio diretto, il suo client cerca invece i suoi relay `read` e pubblica il messaggio lì.

I client che seguono il modello outbox mantengono connessioni ai relay elencati negli event NIP-65 degli utenti seguiti. Man mano che scoprono nuovi account, si connettono dinamicamente a nuovi relay. I relay che appaiono nelle liste di più utenti seguiti vengono prioritizzati poiché connettersi ad essi serve più del grafo sociale dell'utente.

Questa architettura migliora la resistenza alla censura perché nessun singolo relay deve memorizzare o servire i contenuti di tutti. Se un relay va offline o blocca un utente, i loro contenuti rimangono disponibili sugli altri relay elencati.

## Relazione con gli Hint dei Relay

NIP-65 complementa gli hint dei relay trovati in altre NIP. Quando taggate qualcuno con `["p", "pubkey", "wss://hint.relay"]`, l'hint dice ai client dove cercare quel riferimento specifico. NIP-65 fornisce la lista autorevole e controllata dall'utente dei relay preferiti, mentre gli hint offrono scorciatoie incorporate nei singoli event per una scoperta più rapida.

## Best Practice

Mantenete aggiornata la vostra lista di relay poiché voci obsolete che puntano a relay defunti vi rendono più difficili da trovare. Includete almeno due o tre relay per ridondanza così che se un relay va offline, i vostri contenuti rimangono accessibili attraverso gli altri.

Evitate di elencare troppi relay. Quando elencate dieci o quindici relay, ogni client che vuole recuperare i vostri contenuti deve connettersi a tutti, rallentando la loro esperienza e aumentando il carico attraverso la rete. Una lista mirata di tre-cinque relay ben scelti vi serve meglio di una lista esaustiva che grava su tutti quelli che vi seguono.

Mescolate relay generici con eventuali relay specializzati che usate. Per esempio, potreste elencare un relay generale popolare come `wss://relay.damus.io`, un relay focalizzato sulla vostra regione geografica, e un relay per una comunità specifica a cui partecipate.

---

**Fonti principali:**
- [Specifica NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md)

**Menzionato in:**
- [Newsletter #5: Approfondimento NIP](/it/newsletters/2026-01-13-newsletter/#nip-65-metadati-lista-relay)

**Vedi anche:**
- [NIP-11: Informazioni Relay](/it/topics/nip-11/)
