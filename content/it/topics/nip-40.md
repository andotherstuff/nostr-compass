---
title: "NIP-40: Timestamp di scadenza"
date: 2025-12-17
translationOf: /en/topics/nip-40/
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
---
NIP-40 definisce un tag di scadenza che indica ai relay quando un evento dovrebbe essere eliminato.

## Come funziona

Gli eventi includono un tag `expiration` con un timestamp Unix:

```json
["expiration", "1734567890"]
```

Dopo questo momento, i relay dovrebbero eliminare l'evento e rifiutarsi di servirlo.

## Perché è importante

- Contenuto effimero che dovrebbe scomparire dopo un tempo stabilito
- Offerte o annunci a tempo limitato
- Scadenza degli annunci nei marketplace (ad esempio Shopstr)
- Riduzione dei requisiti di storage dei relay

La scadenza è un suggerimento di retention, non un sistema di revoca. Aiuta ad allineare il comportamento dei relay rispetto ai contenuti obsoleti, ma non garantisce la cancellazione una volta che un altro relay, client o archivio ha già copiato l'evento.

## Note su fiducia e sicurezza

- I relay non sono obbligati a rispettare la scadenza, anche se la maggior parte lo fa
- I client non dovrebbero fare affidamento sulla scadenza per la cancellazione di contenuti critici per la sicurezza
- Una volta che il contenuto viene recuperato da un altro client, può essere messo in cache o ripubblicato
- La scadenza non nasconde che un evento sia esistito. Event id, citazioni o copie fuori relay possono ancora sopravvivere dopo il passaggio del timestamp

---

**Fonti primarie:**
- [NIP-40 Specification](https://github.com/nostr-protocol/nips/blob/master/40.md)

**Citato in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#rust-nostr-library)

**Vedi anche:**
- [NIP-01: Basic Protocol](/it/topics/nip-01/)
