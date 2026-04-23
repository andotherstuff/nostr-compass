---
title: "NIP-65: Metadati della Lista Relay"
date: 2026-01-13
translationOf: /en/topics/nip-65.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Discovery
---
NIP-65 definisce gli eventi kind 10002 che pubblicizzano quali relay un utente preferisce per leggere e scrivere. Questi metadati aiutano altri utenti e i client a individuare i tuoi contenuti nella rete distribuita di relay, abilitando il "modello outbox" che distribuisce il carico e migliora la resistenza alla censura.

## Struttura

Una relay list è un evento sostituibile (kind 10002) che contiene tag `r` per ogni relay che l'utente vuole pubblicizzare. L'evento sostituisce ogni relay list precedente dello stesso pubkey.

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

Ogni tag `r` contiene un URL WebSocket del relay e un marker opzionale che indica come l'utente interagisce con quel relay. Il marker `read` significa che l'utente consuma eventi da quel relay, quindi gli altri dovrebbero pubblicare lì per raggiungere l'utente. Il marker `write` significa che l'utente pubblica su quel relay, quindi gli altri dovrebbero iscriversi lì per vedere i contenuti dell'utente. Omettere il marker indica sia read sia write.

Il campo `content` è vuoto per gli eventi relay list.

## Il Modello Outbox

NIP-65 abilita un modello decentralizzato di distribuzione dei contenuti chiamato "modello outbox". Invece di far pubblicare e leggere tutti dagli stessi relay centrali, gli utenti pubblicano sui relay che preferiscono e i client scoprono dinamicamente dove trovare i contenuti di ciascun utente.

Quando Alice vuole trovare i post di Bob, il suo client recupera prima l'evento kind 10002 di Bob da qualunque relay lo abbia. Poi estrae i relay che Bob ha marcato come `write`, perché sono quelli su cui pubblica. Il suo client si iscrive a quei relay per gli eventi di Bob. Quando Alice vuole inviare a Bob un messaggio diretto, il suo client cerca invece i suoi relay `read` e pubblica lì il messaggio.

I client che seguono il modello outbox mantengono connessioni ai relay elencati negli eventi NIP-65 degli utenti seguiti. Man mano che scoprono nuovi account, si connettono dinamicamente a nuovi relay. I relay che compaiono nelle liste di più utenti seguiti ricevono priorità, perché connettersi a essi serve una parte più ampia del grafo sociale dell'utente.

Questa architettura migliora la resistenza alla censura perché nessun relay singolo deve archiviare o servire i contenuti di tutti. Se un relay va offline o blocca un utente, i suoi contenuti restano disponibili sugli altri relay elencati.

## Perché Conta

NIP-65 trasforma la selezione dei relay da un'impostazione predefinita hardcoded del client in metadati di instradamento pubblicati dall'utente. Questo permette ai client di adattarsi alle reali abitudini di pubblicazione e lettura di ciascun account invece di presumere che tutti usino lo stesso insieme di relay.

Sposta anche complessità sui client. Per usare bene il modello outbox, un client ha bisogno di caching dei relay, logica di retry e comportamento di fallback quando una relay list manca oppure è stale. La specifica migliora la discoverability, ma non elimina la necessità di buone euristiche per la selezione dei relay.

## Relazione con i Relay Hint

NIP-65 integra i relay hint presenti in altri NIP. Quando tagghi qualcuno con `["p", "pubkey", "wss://hint.relay"]`, l'hint dice ai client dove cercare quel riferimento specifico. NIP-65 fornisce la lista autorevole, controllata dall'utente, dei relay preferiti, mentre gli hint offrono scorciatoie incorporate nei singoli eventi per una discovery più rapida.

Per la messaggistica privata, NIP-65 non basta da solo. L'instradamento dei contenuti pubblici usa il kind 10002, ma gli stack moderni di messaggistica privata spesso si basano su metadati inbox separati, come le relay list di [NIP-17](/it/topics/nip-17/), così gli utenti possono mantenere separato l'instradamento dei DM dai relay usati per i post pubblici.

## Best Practice

Mantieni aggiornata la tua relay list, perché voci stale che puntano a relay non più attivi rendono più difficile trovarti. Includi almeno due o tre relay per ridondanza, così se un relay va offline i tuoi contenuti restano accessibili tramite gli altri.

Evita di elencare troppi relay. Se ne elenchi dieci o quindici, ogni client che vuole recuperare i tuoi contenuti deve connettersi a tutti, rallentando l'esperienza e aumentando il carico sulla rete. Una lista mirata di tre o cinque relay scelti bene ti serve meglio di una lista esaustiva che pesa su chiunque ti segua.

Mescola relay generalisti con eventuali relay specializzati che usi. Per esempio, potresti elencare un relay generalista diffuso come `wss://relay.damus.io`, un relay focalizzato sulla tua area geografica e un relay per una comunità specifica a cui partecipi.

---

**Fonti primarie:**
- [Specifica NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md)

**Menzionato in:**
- [Newsletter #5: Approfondimento NIP](/it/newsletters/2026-01-13-newsletter/)
- [Newsletter #10: Benchmark del Modello Outbox](/it/newsletters/2026-03-04-newsletter/)

**Vedi anche:**
- [NIP-11: Informazioni sul Relay](/it/topics/nip-11/)
- [NIP-17: Messaggi Diretti Privati](/it/topics/nip-17/)
