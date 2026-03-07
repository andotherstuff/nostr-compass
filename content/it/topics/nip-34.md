---
title: "NIP-34: Collaborazione Git"
date: 2026-02-04
translationOf: /en/topics/nip-34/
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Development
---
NIP-34 definisce tipi di evento per ospitare repository git, patch e issue sui relay Nostr. Questo consente una collaborazione sul codice pienamente decentralizzata senza dipendere da piattaforme di hosting centralizzate come GitHub o GitLab.

## Come funziona

I repository sono rappresentati come eventi addressable (kind 30617) che contengono metadati come nome, descrizione e URL di clone. Il proprietario del repository pubblica questo evento per stabilire il progetto su Nostr.

Le patch (kind 1617) contengono contenuto `git format-patch` che può essere applicato a un repository. I contributori inviano patch come eventi che referenziano il repository di destinazione. Questo rispecchia il workflow di patch basato su email usato da progetti come il kernel Linux.

Le issue (kind 1621) funzionano come i tradizionali issue tracker. Le pull request usano i kind 1618 e 1619, e gli aggiornamenti di stato usano da 1630 a 1633. Le risposte a issue, patch e pull request usano commenti [NIP-22](/it/topics/nip-22/).

## Tipi di evento

- **30617** - Annuncio del repository (addressable)
- **30618** - Annuncio dello stato del repository per branch e tag
- **1617** - Invio patch
- **1618** - Pull request
- **1619** - Aggiornamento pull request
- **1621** - Issue
- **1630-1633** - Eventi di stato open, merged/resolved, closed e draft

## Perché è importante

NIP-34 separa discovery e transport. Il repository vero e proprio può ancora vivere su normali server Git, ma gli eventi Nostr forniscono un livello distribuito via relay per discovery, discussione, scambio di patch e tracciamento dello stato. Questo significa che un progetto può continuare a usare strumenti git-native senza dipendere dal database o dall'API di una singola forge.

Il tag `r` con il commit univoco più antico è uno dei dettagli più importanti. Fornisce ai client un modo per raggruppare mirror e fork che rappresentano la stessa lineage del repository sottostante, cosa difficile da dedurre dai soli nomi.

## Stato di implementazione

- **ngit** - Strumento da riga di comando per pubblicare repository e patch su Nostr
- **gitworkshop.dev** - Interfaccia web per navigare repository ospitati su Nostr
- **Notedeck** - Client desktop con [supporto preliminare per la visualizzazione NIP-34](https://github.com/damus-io/notedeck/pull/1279)

---

**Fonti primarie:**

- [NIP-34 Specification](https://github.com/nostr-protocol/nips/blob/master/34.md)

**Citato in:**

- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - Notedeck aggiunge il viewer NIP-34
- [Newsletter #9: Notedeck](/en/newsletters/2026-02-11-newsletter/#notedeck)

**Vedi anche:**
- [NIP-22: Comments](/it/topics/nip-22/)
