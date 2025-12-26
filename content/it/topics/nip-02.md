---
title: "NIP-02: Lista Follow"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-02 definisce gli eventi kind 3, che memorizzano la vostra lista follow. Questo semplice meccanismo alimenta il grafo sociale che rende possibili le timeline.

## Struttura

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

Ogni tag `p` ha quattro posizioni: il nome del tag, la pubkey seguita (esadecimale), un suggerimento URL relay opzionale, e un "petname" opzionale (un soprannome locale). Il suggerimento relay dice ad altri client dove trovare gli eventi di quell'utente. Il petname vi consente di assegnare nomi memorabili ai contatti senza affidarvi ai nomi visualizzati auto-dichiarati.

## Comportamento Sostituibile

Kind 3 rientra nell'intervallo sostituibile (0, 3, 10000-19999), quindi i relay mantengono solo l'ultima versione per pubkey. Quando seguite qualcuno di nuovo, il vostro client pubblica un nuovo kind 3 completo contenente tutti i vostri follow piu' quello nuovo. Questo significa che le liste follow devono essere complete ogni volta; non potete pubblicare aggiornamenti incrementali.

## Costruire Timeline

Per costruire un feed home, i client recuperano il kind 3 dell'utente, estraggono tutte le pubkey dai tag `p`, poi si iscrivono agli eventi kind 1 da quegli autori:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

Il relay restituisce le note corrispondenti, e il client le renderizza. I suggerimenti relay nel kind 3 aiutano i client a sapere quali relay interrogare per ogni utente seguito.

## Petname e Identita'

Il campo petname abilita uno schema di naming decentralizzato. Invece di fidarvi di qualsiasi nome un utente dichiara nel suo profilo, potete assegnare la vostra etichetta. Un client potrebbe visualizzare "alice (Mia Sorella)" dove "alice" viene dal suo profilo kind 0 e "Mia Sorella" e' il vostro petname. Questo fornisce contesto che i nomi utente globali non possono.

## Considerazioni Pratiche

Poiche' gli eventi kind 3 sono sostituibili e devono essere completi, i client dovrebbero preservare tag sconosciuti durante l'aggiornamento. Se un altro client ha aggiunto tag che il vostro client non capisce, sovrascrivere alla cieca perderebbe quei dati. Aggiungete nuovi follow invece di ricostruire da zero.

---

**Fonti primarie:**
- [Specifica NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md)

**Menzionato in:**
- [Newsletter #2: Approfondimento NIP](/it/newsletters/2025-12-24-newsletter/#nip-02-follow-list)

**Vedi anche:**
- [NIP-01: Protocollo Base](/it/topics/nip-01/)

