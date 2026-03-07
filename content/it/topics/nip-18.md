---
title: "NIP-18: Repost"
date: 2025-12-17
translationOf: /en/topics/nip-18/
translationDate: 2026-03-07
draft: false
categories:
  - Social
  - Protocol
---
NIP-18 definisce come ripubblicare eventi, in modo simile ai retweet su altre piattaforme.

## Come funziona

Un repost è un evento kind 6 (per note kind 1) o kind 16 (repost generico) che contiene:
- tag `e` che fa riferimento all'evento ripubblicato
- tag `p` che fa riferimento all'autore originale
- facoltativamente, l'intero evento originale nel campo `content`

Kind 6 è specifico per le text note. Kind 16 esiste così i client possono ripubblicare altri tipi di evento senza fingere che tutto sia una note kind 1.

## Note di interoperabilità

È stato migliorato il supporto per il repost di eventi replaceable con supporto per il tag `a`. Questo consente ai repost di eventi addressable (kind 30000-39999) di farvi riferimento tramite il loro indirizzo invece che tramite uno specifico ID evento.

Questa distinzione conta perché gli eventi addressable possono essere aggiornati nel tempo. Ripubblicare tramite coordinata `a` permette ai client di puntare alla versione corrente di un evento addressable, mentre ripubblicare tramite ID evento congela una specifica istanza storica.

## Perché è importante

I repost sono più di un pulsante di condivisione nell'interfaccia. Fanno parte del modo in cui il contenuto si muove attraverso i grafi sociali, di come i client contano l'engagement e di come i dati di relay hint si propagano nella rete. Se un client gestisce male i tag di repost, la ricostruzione dei thread e il recupero degli eventi possono rompersi in modi sottili.

---

**Fonti principali:**
- [Specifica NIP-18](https://github.com/nostr-protocol/nips/blob/master/18.md)
- [PR #2132](https://github.com/nostr-protocol/nips/pull/2132) - supporto del tag `a` per i repost generici

**Menzionato in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #8: News](/en/newsletters/2026-02-04-newsletter/#news)

**Vedi anche:**
- [NIP-01: Basic Protocol](/it/topics/nip-01/)
- [NIP-10: Text Note Threading](/it/topics/nip-10/)
