---
title: "NIP-10: Threading delle text note"
date: 2025-12-24
translationOf: /en/topics/nip-10/
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---
NIP-10 specifica come le note kind 1 si riferiscono tra loro per formare thread di risposta. Capirlo è essenziale per costruire viste delle conversazioni.

## Come funziona

Quando qualcuno risponde a una nota, i client devono sapere: a cosa sta rispondendo? Qual è la radice della conversazione? Chi dovrebbe essere notificato? NIP-10 risponde a queste domande tramite tag `e` (riferimenti a eventi) e tag `p` (menzioni di pubkey).

## Tag marcati (preferiti)

I client moderni usano marker espliciti nei tag `e`:

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "Great point! I agree.",
  "sig": "b7d3f..."
}
```

Il marker `root` punta alla nota originale che ha avviato il thread. Il marker `reply` punta alla nota specifica a cui si sta rispondendo. Se si risponde direttamente alla root, si usa solo `root` e non serve alcun tag `reply`. La distinzione conta per il rendering: `reply` determina il livello di rientro in una vista a thread, mentre `root` raggruppa insieme tutte le risposte.

## Regole del threading

- **Risposta diretta alla root:** Un tag `e` con marker `root`
- **Risposta a una risposta:** Due tag `e`, uno `root` e uno `reply`
- `root` resta costante per tutto il thread; `reply` cambia in base a ciò a cui si sta rispondendo

## Notifiche e menzioni

Includi tag `p` per chiunque debba ricevere una notifica. Come minimo, tagga l'autore della nota a cui stai rispondendo. La convenzione è includere anche tutti i tag `p` dell'evento genitore, così tutte le persone nella conversazione restano aggiornate, oltre a tutti gli utenti che @menzioni nel contenuto.

## Relay hint

La terza posizione nei tag `e` e `p` può contenere un URL di relay dove quell'evento o il contenuto di quell'utente potrebbero essere trovati. Questo aiuta i client a recuperare il contenuto referenziato anche se non sono connessi al relay originale.

## Note sull'interoperabilità

Le prime implementazioni di Nostr deducevano il significato dalla posizione del tag invece che dai marker: il primo tag `e` era la root, l'ultimo era la reply, quelli in mezzo erano menzioni. Questo approccio è deprecato perché crea ambiguità. Se vedi tag `e` senza marker, probabilmente provengono da client più vecchi. Le implementazioni moderne dovrebbero usare sempre marker espliciti.

I client devono comunque analizzare entrambi i formati se vogliono renderizzare correttamente i thread più vecchi. In pratica, l'interoperabilità di NIP-10 è in parte un problema di migrazione: i producer dovrebbero emettere tag marcati, ma i reader dovrebbero restare tolleranti verso le forme posizionali più vecchie.

## Costruire viste a thread

Per visualizzare un thread, recupera l'evento root e poi interroga tutti gli eventi con un tag `e` che fa riferimento a quella root:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Ordina i risultati per `created_at` e usa i marker `reply` per costruire la struttura ad albero. Gli eventi il cui `reply` punta alla root sono risposte di primo livello; gli eventi il cui `reply` punta a un'altra reply sono risposte annidate.

---

**Fonti primarie:**
- [NIP-10 Specification](https://github.com/nostr-protocol/nips/blob/master/10.md)

**Citato in:**
- [Newsletter #2: NIP Deep Dive](/en/newsletters/2025-12-24-newsletter/#nip-10-text-note-threading)

**Vedi anche:**
- [NIP-01: Protocollo di base](/it/topics/nip-01/)
- [NIP-18: Repost](/it/topics/nip-18/)
