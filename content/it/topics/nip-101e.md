---
title: "NIP-101e: allenamenti fitness"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-101e.md
translationDate: 2026-07-01
categories:
  - Fitness
  - Discovery
---

NIP-101e definisce un formato di evento per allenamenti in modo che le applicazioni di fitness tracking possano pubblicare, condividere e scoprire sessioni di allenamento su Nostr. La specifica utilizza eventi di kind 1301 che trasportano metriche di sessione (distanza, durata, dislivello, frequenza cardiaca, calorie, cadenza in bicicletta, app sorgente) in tag strutturati in modo che un client possa renderizzare l'allenamento come una scheda strutturata con le metriche mostrate nelle loro unità corrette.

## Come funziona

Un allenamento NIP-101e è un evento di kind 1301 con tag strutturati per ogni metrica catturata dall'applicazione sorgente. I tag comuni includono:

- `type` per la disciplina dell'allenamento (corsa, bici, nuoto, sollevamento pesi, ecc.)
- `distance` con valore e unità
- `duration` in secondi
- `elevation_gain` con valore e unità
- Timestamp `start` e `end`
- `heart_rate` (media e massima)
- `calories` per il dispendio energetico
- `source` che nomina l'applicazione che pubblica
- Tag argomento `t` per la scoperta tramite hashtag

Il campo `content` trasporta una nota opzionale scritta dall'utente (l'equivalente della didascalia che un utente allegherebbe a un caricamento Strava). I client che riconoscono il kind 1301 renderizzano le metriche strutturate come una scheda di allenamento; i client che non lo fanno ripiegano sulla visualizzazione del campo `content` come una nota normale.

## Semantica di discovery e feed

Gli eventi NIP-101e sono normali eventi di feed, quindi un allenamento pubblicato da un utente compare nelle timeline dei suoi follower come qualsiasi altro post. I client con visualizzazioni dedicate agli allenamenti possono sottoscrivere il kind 1301 con filtri per autore o hashtag per costruire superfici di training log, classifiche o feed di sfide comunitarie. Il pubkey dell'autore è l'identità canonica per l'allenamento, quindi un'applicazione di terze parti che legge gli allenamenti di un altro utente eredita le stesse assunzioni di fiducia di qualsiasi altro feed Nostr.

## Implementazioni

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) rilascia il rendering degli allenamenti di kind 1301 con una metrica in evidenza, una griglia di statistiche, una visualizzazione della velocità specifica per il ciclismo e badge di sorgente ([PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184), refattorizzato in [PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226))

---

**Fonti primarie:**
- [Specifica NIP-101e](https://github.com/nostr-protocol/nips/blob/master/101e.md)
- [Amethyst PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184) - Aggiunta del supporto per allenamenti fitness NIP-101e (Kind 1301)
- [Amethyst PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226) - Riprogettazione della visualizzazione degli allenamenti con metrica in evidenza e griglia di statistiche

**Menzionato in:**
- [Newsletter #27: Amethyst v1.12.0 rilascia wallet Cashu, nutzap, un driver CLINK e Tor self-heal](/it/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
