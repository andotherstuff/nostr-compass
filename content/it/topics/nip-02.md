---
title: "NIP-02: Lista dei follow"
date: 2025-12-24
translationOf: /en/topics/nip-02/
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---
NIP-02 definisce gli eventi kind 3, che memorizzano la follow list di un utente. Questo evento è l'input di base per i feed home, le notifiche di risposta e molte strategie di selezione dei relay.

## Come funziona

Un evento kind 3 contiene tag `p` che elencano le pubkey seguite:

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Ogni tag `p` ha quattro posizioni: il nome del tag, la pubkey seguita (hex), un relay URL hint opzionale e un "petname" opzionale (un soprannome locale). Il relay hint dice agli altri client dove trovare gli eventi di quell'utente. Il petname permette di assegnare nomi memorabili ai contatti senza dipendere dai display name dichiarati dall'utente stesso.

## Comportamento replaceable

Il kind 3 rientra nell'intervallo replaceable (0, 3, 10000-19999), quindi i relay mantengono solo la versione più recente per pubkey. Quando inizi a seguire una nuova persona, il tuo client pubblica un nuovo kind 3 completo che contiene tutti i follow esistenti più quello nuovo. Questo significa che le follow list devono essere complete ogni volta; non puoi pubblicare aggiornamenti incrementali.

## Perché conta

Per costruire un feed home, i client recuperano il kind 3 dell'utente, estraggono tutte le pubkey dai tag `p`, poi si iscrivono agli eventi kind 1 di quegli autori:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

Il relay restituisce le note corrispondenti e il client le mostra. I relay hint nel kind 3 aiutano i client a sapere quali relay interrogare per ogni utente seguito.

Questo evento è anche il punto in cui emerge per prima una condizione sociale obsoleta. Se il kind 3 più recente di un utente manca sui relay che interroghi, il suo feed può sembrare vuoto anche se i suoi follow esistono ancora altrove. I client che uniscono i risultati di più relay di solito recuperano meglio dei client che si fidano di un solo relay.

## Petname e identità

Il campo petname abilita uno schema di naming decentralizzato. Invece di fidarti del nome che un utente dichiara nel proprio profilo, puoi assegnargli la tua etichetta. Un client potrebbe mostrare "alice (Mia sorella)" dove "alice" proviene dal suo profilo kind 0 e "Mia sorella" è il tuo petname. Questo aggiunge contesto che gli username globali non possono fornire.

## Note di interoperabilità

Poiché gli eventi kind 3 sono replaceable e devono essere completi, i client dovrebbero preservare i tag sconosciuti durante un aggiornamento. Se un altro client ha aggiunto tag che il tuo client non comprende, sovrascriverli alla cieca farebbe perdere quei dati.

La stessa cautela vale per relay hint e petname. Sono campi opzionali, ma rimuoverli in scrittura può peggiorare in silenzio l'esperienza di un altro client. Un percorso di aggiornamento sicuro è: caricare l'ultimo kind 3 noto, modificare solo i tag che il client capisce, mantenere il resto, poi ripubblicare l'evento completo.

---

**Fonti primarie:**
- [NIP-02 Specification](https://github.com/nostr-protocol/nips/blob/master/02.md)

**Menzionato in:**
- [Newsletter #2: NIP Deep Dive](/en/newsletters/2025-12-24-newsletter/#nip-02-follow-list)

**Vedi anche:**
- [NIP-01: Protocollo di base](/it/topics/nip-01/)
- [NIP-10: Threading delle text note](/it/topics/nip-10/)
- [NIP-65: Relay List Metadata](/it/topics/nip-65/)
