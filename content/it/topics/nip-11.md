---
title: "NIP-11: Informazioni Relay"
date: 2025-12-17
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11 definisce come i relay espongono metadati su se stessi, inclusi NIP supportati, limitazioni e informazioni di contatto.

## Come Funziona

I client recuperano le informazioni del relay facendo una richiesta HTTP GET all'URL WebSocket del relay con un header `Accept: application/nostr+json`. Il relay restituisce un documento JSON che descrive le sue capacita'.

## Campi Principali

- **name** - Nome leggibile del relay
- **description** - A cosa serve il relay
- **supported_nips** - Lista dei NIP implementati
- **limitation** - Restrizioni come dimensione massima messaggi, auth richiesta, ecc.
- **self** - La chiave pubblica del relay stesso (nuovo campo per l'identita' del relay)

## Casi d'Uso

- I client possono verificare se un relay supporta le funzionalita' richieste prima di connettersi
- I servizi di discovery possono indicizzare le capacita' dei relay
- Gli utenti possono vedere le policy del relay prima di pubblicare

---

**Fonti primarie:**
- [Specifica NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md)

**Menzionato in:**
- [Newsletter #1: Aggiornamenti NIP](/it/newsletters/2025-12-17-newsletter/#nip-updates)

