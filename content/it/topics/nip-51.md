---
title: "NIP-51: Liste"
date: 2025-12-17
translationOf: /en/topics/nip-51/
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---
NIP-51 definisce eventi lista per organizzare utenti, eventi, relay, hashtag e altri riferimenti. È il protocollo principale per segnalibri, liste di mute, insiemi di follow, insiemi di relay e diverse altre raccolte curate dagli utenti.

## Liste e insiemi standard

- **Le liste standard** usano kind di eventi sostituibili come la kind `10000` per le liste di mute, la kind `10003` per i segnalibri e la kind `10007` per i relay di ricerca.
- **Gli insiemi** usano kind indirizzabili con tag `d`, come la kind `30000` per gli insiemi di follow, la kind `30003` per gli insiemi di segnalibri e la kind `30030` per gli insiemi di emoji.

La distinzione conta per il comportamento dei client. Le liste standard implicano una singola lista canonica per utente e kind. Gli insiemi implicano molte raccolte con nome, quindi i client devono preservare il tag `d` di ogni lista.

## Struttura

Le liste usano tag per fare riferimento al contenuto:

- tag `p` per le pubkey
- tag `e` per gli eventi
- tag `a` per gli eventi indirizzabili
- tag `t` per gli hashtag
- tag `word` per le parole silenziate
- tag `relay` per gli URL dei relay nei tipi di lista orientati ai relay

Alcuni tipi di lista hanno forme di tag consentite più ristrette di altri. Per esempio, le liste orientate ai relay usano tag `relay`, mentre i segnalibri devono puntare a note o eventi indirizzabili. I client che trattano ogni lista NIP-51 come tag arbitrari in formato libero perderanno interoperabilità.

## Pubblico vs privato

Le liste possono avere tag pubblici ed elementi privati. Gli elementi privati vengono serializzati come un array JSON che rispecchia la struttura di `tags`, cifrati e memorizzati nel `content` dell'evento. La specifica attuale usa NIP-44 per questo modello di self-encryption, con NIP-04 mantenuto solo per compatibilità legacy.

Questa divisione permette agli utenti di pubblicare un contenitore di lista visibile nascondendo alcune voci. Una lista di segnalibri può restare pubblica mentre note private o segnalibri privati rimangono nel contenuto cifrato.

## Kind utili

- **Kind 10000**: lista di mute per pubkey, thread, hashtag e parole silenziate
- **Kind 10003**: segnalibri per note e contenuti indirizzabili
- **Kind 10007**: relay di ricerca preferiti
- **Kind 30002**: insiemi di relay per gruppi di relay con nome
- **Kind 30006**: insiemi di curatela di immagini
- **Kind 39089**: starter pack per bundle di follow condivisibili

Le modifiche recenti alla specifica hanno spostato gli hashtag fuori dai segnalibri generici e dentro gli insiemi di interessi, e hanno aggiunto la kind `30006` per la curatela di immagini. Entrambe le modifiche riducono l'ambiguità nel modo in cui i client interpretano il contenuto delle liste.

---

**Fonti principali:**
- [Specifica NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md)

**Citato in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #4: NIP Deep Dive](/en/newsletters/2026-01-13-newsletter/#nip-deep-dive-nip-51-and-nip-65)
- [Newsletter #8: njump Adds NIP-51 Support](/en/newsletters/2026-02-04-newsletter/#njump)

**Vedi anche:**
- [NIP-02: Follow List](/it/topics/nip-02/)
