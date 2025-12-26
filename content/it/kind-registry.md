---
title: Registro dei Kind
url: /it/kind-registry/
translationOf: /en/kind-registry.md
translationDate: 2025-12-26
---

I kind degli eventi sono numeri interi che categorizzano gli eventi Nostr. Questo registro elenca tutti i kind standardizzati con le relative descrizioni e i NIP che li definiscono.

**Intervalli di kind** (da [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)):
- **0-999**: Eventi regolari (tutte le versioni vengono conservate)
- **1000-9999**: Eventi regolari (continua)
- **10000-19999**: Eventi sostituibili (viene conservato solo l'ultimo per pubkey)
- **20000-29999**: Eventi effimeri (non memorizzati, solo inoltrati)
- **30000-39999**: Eventi indirizzabili (l'ultimo per pubkey + kind + d-tag)

## Eventi Core (0-99)

| Kind | Descrizione | NIP |
|------|-------------|-----|
| 0 | Metadati Utente | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 1 | Nota di Testo Breve | [10](https://github.com/nostr-protocol/nips/blob/master/10.md) |
| 2 | Raccomanda Relay (deprecato) | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 3 | Seguiti | [02](https://github.com/nostr-protocol/nips/blob/master/02.md) |
| 4 | Messaggi Diretti Crittografati | [04](https://github.com/nostr-protocol/nips/blob/master/04.md) |
| 5 | Richiesta di Eliminazione Evento | [09](https://github.com/nostr-protocol/nips/blob/master/09.md) |
| 6 | Repost | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 7 | Reazione | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 8 | Assegnazione Badge | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 9 | Messaggio Chat | [C7](https://github.com/nostr-protocol/nips/blob/master/C7.md) |
| 10 | Risposta in Thread Chat di Gruppo (deprecato) | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 11 | Thread | [7D](https://github.com/nostr-protocol/nips/blob/master/7D.md) |
| 12 | Risposta Thread di Gruppo (deprecato) | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 13 | Seal | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 14 | Messaggio Diretto | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 15 | Messaggio File | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 16 | Repost Generico | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 17 | Reazione a un sito web | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 20 | Immagine | [68](https://github.com/nostr-protocol/nips/blob/master/68.md) |
| 21 | Evento Video | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 22 | Video Verticale Breve | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 40 | Creazione Canale | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 41 | Metadati Canale | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 42 | Messaggio Canale | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 43 | Nascondi Messaggio Canale | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 44 | Silenzia Utente Canale | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 62 | Richiesta di Scomparsa | [62](https://github.com/nostr-protocol/nips/blob/master/62.md) |
| 64 | Scacchi (PGN) | [64](https://github.com/nostr-protocol/nips/blob/master/64.md) |

## Crittografia MLS (443-445)

| Kind | Descrizione | NIP |
|------|-------------|-----|
| 443 | KeyPackage | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 444 | Messaggio di Benvenuto | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 445 | Evento di Gruppo | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |

## Eventi Regolari (1000-9999)

| Kind | Descrizione | NIP |
|------|-------------|-----|
| 1018 | Risposta Sondaggio | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1021 | Offerta | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1022 | Conferma offerta | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1040 | OpenTimestamps | [03](https://github.com/nostr-protocol/nips/blob/master/03.md) |
| 1059 | Gift Wrap | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 1063 | Metadati File | [94](https://github.com/nostr-protocol/nips/blob/master/94.md) |
| 1068 | Sondaggio | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1111 | Commento | [22](https://github.com/nostr-protocol/nips/blob/master/22.md) |
| 1222 | Messaggio Vocale | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1244 | Commento Messaggio Vocale | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1311 | Messaggio Chat dal Vivo | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 1337 | Frammento di Codice | [C0](https://github.com/nostr-protocol/nips/blob/master/C0.md) |
| 1617 | Patch | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1618 | Pull Request | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1619 | Aggiornamenti Pull Request | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1621 | Issue | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1984 | Segnalazione | [56](https://github.com/nostr-protocol/nips/blob/master/56.md) |
| 1985 | Etichetta | [32](https://github.com/nostr-protocol/nips/blob/master/32.md) |
| 2003 | Torrent | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 2004 | Commento Torrent | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 4550 | Approvazione Post Community | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 5000-5999 | Richiesta Lavoro | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 6000-6999 | Risultato Lavoro | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7000 | Feedback Lavoro | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7374 | Token Wallet Cashu Riservati | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7375 | Token Wallet Cashu | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7376 | Storico Wallet Cashu | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 8000 | Aggiungi Utente | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 8001 | Rimuovi Utente | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 9000-9030 | Eventi Controllo Gruppo | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 9041 | Obiettivo Zap | [75](https://github.com/nostr-protocol/nips/blob/master/75.md) |
| 9321 | Nutzap | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 9734 | Richiesta Zap | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9735 | Zap | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9802 | Highlights | [84](https://github.com/nostr-protocol/nips/blob/master/84.md) |

## Eventi Sostituibili (10000-19999)

| Kind | Descrizione | NIP |
|------|-------------|-----|
| 10000 | Lista silenziati | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10001 | Lista fissati | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10002 | Metadati Lista Relay | [65](https://github.com/nostr-protocol/nips/blob/master/65.md) |
| 10003 | Lista segnalibri | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10004 | Lista community | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10005 | Lista chat pubbliche | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10006 | Lista relay bloccati | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10007 | Lista relay di ricerca | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10009 | Gruppi utente | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10012 | Lista relay preferiti | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10013 | Lista relay eventi privati | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 10015 | Lista interessi | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10019 | Raccomandazione Mint Nutzap | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 10020 | Seguiti media | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10030 | Lista emoji utente | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10050 | Lista relay per ricevere DM | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 10051 | Lista Relay KeyPackage | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 10063 | Lista server utente | Blossom |
| 10166 | Annuncio Monitor Relay | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 10312 | Presenza Stanza | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 13194 | Info Wallet | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 13534 | Liste Membri | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 17375 | Evento Wallet Cashu | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |

## Autenticazione e Wallet (22000-27999)

| Kind | Descrizione | NIP |
|------|-------------|-----|
| 22242 | Autenticazione Client | [42](https://github.com/nostr-protocol/nips/blob/master/42.md) |
| 23194 | Richiesta Wallet | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 23195 | Risposta Wallet | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 24133 | Nostr Connect | [46](https://github.com/nostr-protocol/nips/blob/master/46.md) |
| 24242 | Blob memorizzati su mediaserver | Blossom |
| 27235 | HTTP Auth | [98](https://github.com/nostr-protocol/nips/blob/master/98.md) |

## Controllo Accessi (28000-29999)

| Kind | Descrizione | NIP |
|------|-------------|-----|
| 28934 | Richiesta di Adesione | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28935 | Richiesta di Invito | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28936 | Richiesta di Uscita | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |

## Eventi Indirizzabili (30000-39999)

| Kind | Descrizione | NIP |
|------|-------------|-----|
| 30000 | Set di seguiti | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30002 | Set di relay | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30003 | Set di segnalibri | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30004 | Set di curatela | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30005 | Set di video | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30007 | Set di kind silenziati | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30008 | Badge Profilo | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30009 | Definizione Badge | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30015 | Set di interessi | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30017 | Crea o aggiorna uno stand | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30018 | Crea o aggiorna un prodotto | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30019 | UI/UX Marketplace | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30020 | Prodotto venduto all'asta | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30023 | Contenuto Long-form | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30024 | Bozza Contenuto Long-form | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30030 | Set di emoji | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30063 | Set di artefatti di release | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30078 | Dati Specifici dell'Applicazione | [78](https://github.com/nostr-protocol/nips/blob/master/78.md) |
| 30166 | Scoperta Relay | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 30267 | Set di curatela app | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30311 | Evento dal Vivo | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30312 | Stanza Interattiva | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30313 | Evento Conferenza | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30315 | Stati Utente | [38](https://github.com/nostr-protocol/nips/blob/master/38.md) |
| 30402 | Annuncio Classificato | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30403 | Bozza Annuncio Classificato | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30617 | Annunci repository | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30618 | Annunci stato repository | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30818 | Articolo wiki | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 30819 | Redirect | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 31234 | Evento Bozza | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 31922 | Evento Calendario Basato su Data | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31923 | Evento Calendario Basato su Ora | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31924 | Calendario | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31925 | RSVP Evento Calendario | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31989 | Raccomandazione handler | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 31990 | Informazioni handler | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 34550 | Definizione Community | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 38172 | Annuncio Mint Cashu | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38173 | Annuncio Fedimint | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38383 | Eventi ordine peer-to-peer | [69](https://github.com/nostr-protocol/nips/blob/master/69.md) |
| 39000-39009 | Eventi metadati gruppo | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 39089 | Starter pack | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39092 | Starter pack media | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39701 | Segnalibri web | [B0](https://github.com/nostr-protocol/nips/blob/master/B0.md) |

*Ultimo aggiornamento: Dicembre 2025*

Consulta il [repository NIPs](https://github.com/nostr-protocol/nips) per la fonte ufficiale.
