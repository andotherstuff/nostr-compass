---
title: "NIP-40: Timestamp di Scadenza"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-40 definisce un tag di scadenza che dice ai relay quando un evento dovrebbe essere eliminato.

## Struttura

Gli eventi includono un tag `expiration` con un timestamp Unix:

```json
["expiration", "1734567890"]
```

Dopo questo momento, i relay dovrebbero eliminare l'evento e rifiutarsi di servirlo.

## Casi d'Uso

- Contenuto effimero che dovrebbe scomparire dopo un tempo stabilito
- Offerte o annunci a tempo limitato
- Scadenza inserzioni nei marketplace (es. Shopstr)
- Riduzione dei requisiti di storage dei relay

## Considerazioni

- I relay non sono obbligati a onorare la scadenza (ma la maggior parte lo fa)
- I client non dovrebbero fare affidamento sulla scadenza per l'eliminazione di contenuti critici per la sicurezza
- Una volta che il contenuto e' stato recuperato da un altro client, potrebbe essere memorizzato in cache o ri-pubblicato

---

**Fonti primarie:**
- [Specifica NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md)

**Menzionato in:**
- [Newsletter #1: Notizie](/it/newsletters/2025-12-17-newsletter/#news)

