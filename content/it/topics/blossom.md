---
title: "Protocollo Blossom"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

Blossom e' un protocollo di hosting media per Nostr che fornisce archiviazione file decentralizzata con URL content-addressable.

## Come Funziona

I file sono memorizzati sui server Blossom e indirizzati tramite il loro hash SHA256. Questo significa:
- Lo stesso file ha sempre lo stesso URL su tutti i server
- I file possono essere recuperati da qualsiasi server che li possiede
- I client possono verificare l'integrita' del file controllando l'hash

## Funzionalita'

- Archiviazione content-addressable
- Ridondanza su piu' server
- Scoperta autore tramite BUD-03
- Schema URI personalizzato tramite BUD-10
- Paginazione basata su cursore sull'endpoint `/list`

---

**Fonti primarie:**
- [Repository Blossom](https://github.com/hzrd149/blossom)

**Menzionato in:**
- [Newsletter #1: Notizie](/it/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Modifiche Notevoli al Codice](/it/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)

**Vedi anche:**
- [BUD-03: Lista Server Utente](/it/topics/bud-03/)
- [BUD-10: Schema URI Blossom](/it/topics/bud-10/)

