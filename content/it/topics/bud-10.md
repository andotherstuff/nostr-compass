---
title: "BUD-10: Schema URI Blossom"
date: 2025-12-17
translationOf: /en/topics/bud-10/
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---
BUD-10 definisce lo schema URI `blossom:`, un riferimento portabile a un blob che può includere hint sul server, hint sull'autore e dimensione attesa insieme all'hash del file.

## Formato URI

```
blossom:<sha256>.<ext>?xs=<server>&as=<pubkey>&sz=<bytes>
```

La specifica richiede un hash SHA-256 minuscolo di 64 caratteri e un'estensione di file. Se l'estensione è sconosciuta, i client dovrebbero ripiegare su `.bin`.

## Come funziona la risoluzione

I client dovrebbero risolvere un URI `blossom:` per fasi:

1. Provare eventuali hint server `xs` nell'ordine in cui compaiono
2. Se sono presenti pubkey autore `as`, recuperare l'elenco server [BUD-03](/it/topics/bud-03/) di ciascun autore e provare quei server
3. Ripiegare su server noti o cache locale se necessario

Questo ordine è utile perché permette a un mittente di allegare hint immediati per un recupero rapido, lasciando comunque ai destinatari un percorso di recupero se quegli hint diventano obsoleti.

## Perché conta

Gli URI `blossom:` funzionano più come magnet link che come normali URL media. Descrivono quale blob recuperare e includono indizi su dove trovarlo, invece di presumere che un host resterà disponibile per sempre.

Il campo facoltativo `sz` aggiunge un controllo concreto di integrità oltre all'hash. I client possono verificare la dimensione attesa prima o dopo il download, cosa che aiuta a rilevare trasferimenti incompleti e migliora la UX per i media di grandi dimensioni.

---

**Fonti primarie:**
- [BUD-10 Specification](https://github.com/hzrd149/blossom/blob/master/buds/10.md)
- [Blossom Repository](https://github.com/hzrd149/blossom)

**Citato in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)

**Vedi anche:**
- [Blossom Protocol](/it/topics/blossom/)
- [BUD-03: User Server List](/it/topics/bud-03/)
