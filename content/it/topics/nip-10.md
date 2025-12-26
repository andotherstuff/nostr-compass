---
title: "NIP-10: Threading Note di Testo"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-10 specifica come le note kind 1 si referenziano a vicenda per formare thread di risposte. Capire questo e' essenziale per costruire viste di conversazione.

## Il Problema

Quando qualcuno risponde a una nota, i client devono sapere: A cosa e' una risposta? Qual e' la radice della conversazione? Chi dovrebbe essere notificato? NIP-10 risponde a queste domande attraverso tag `e` (riferimenti eventi) e tag `p` (menzioni pubkey).

## Tag Marcati (Preferiti)

I client moderni usano marcatori espliciti nei tag `e`:

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
  "content": "Ottimo punto! Sono d'accordo.",
  "sig": "b7d3f..."
}
```

Il marcatore `root` punta alla nota originale che ha iniziato il thread. Il marcatore `reply` punta alla nota specifica a cui si sta rispondendo. Se rispondete direttamente alla root, usate solo `root` (nessun tag `reply` necessario). La distinzione conta per il rendering: il `reply` determina l'indentazione in una vista thread, mentre `root` raggruppa tutte le risposte insieme.

## Regole di Threading

- **Risposta diretta alla root:** Un tag `e` con marcatore `root`
- **Risposta a una risposta:** Due tag `e`, uno `root` e uno `reply`
- Il `root` rimane costante in tutto il thread; `reply` cambia in base a cosa state rispondendo

## Tag Pubkey per Notifiche

Includete tag `p` per tutti quelli che dovrebbero essere notificati. Come minimo, taggate l'autore della nota a cui state rispondendo. La convenzione e' anche includere tutti i tag `p` dall'evento parent (cosi' tutti nella conversazione rimangono nel loop), piu' qualsiasi utente che @menzionate nel vostro contenuto.

## Suggerimenti Relay

La terza posizione nei tag `e` e `p` puo' contenere un URL relay dove quell'evento o contenuto utente potrebbe essere trovato. Questo aiuta i client a recuperare il contenuto referenziato anche se non sono connessi al relay originale.

## Tag Posizionali Deprecati

Le prime implementazioni Nostr inferivano il significato dalla posizione del tag invece che dai marcatori: il primo tag `e` era root, l'ultimo era reply, quelli in mezzo erano menzioni. Questo approccio e' deprecato perche' crea ambiguita'. Se vedete tag `e` senza marcatori, sono probabilmente da client piu' vecchi. Le implementazioni moderne dovrebbero sempre usare marcatori espliciti.

## Costruire Viste Thread

Per visualizzare un thread, recuperate l'evento root, poi interrogate tutti gli eventi con un tag `e` che referenzia quella root:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Ordinate i risultati per `created_at` e usate i marcatori `reply` per costruire la struttura ad albero. Gli eventi il cui `reply` punta alla root sono risposte di primo livello; gli eventi il cui `reply` punta a un'altra risposta sono risposte annidate.

---

**Fonti primarie:**
- [Specifica NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md)

**Menzionato in:**
- [Newsletter #2: Approfondimento NIP](/it/newsletters/2025-12-24-newsletter/#nip-10-threading-note-di-testo)

**Vedi anche:**
- [NIP-01: Protocollo Base](/it/topics/nip-01/)

