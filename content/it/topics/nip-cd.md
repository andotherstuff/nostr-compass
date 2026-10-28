---
title: "NIP-CD: comandi slash"
date: 2026-10-28
translationOf: /en/topics/nip-cd.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-CD definisce i comandi slash. Un servizio pubblica un comando e chiunque può invocarlo come testo semplice nel contenuto di qualsiasi event Nostr. NIP-CD è una specifica opzionale in bozza. È stata integrata (merge) il 21 ottobre 2026 con il titolo Commands, dopo una proposta precedente, e ha preso il nuovo titolo Slash Commands quando, il 27 ottobre 2026, sono state integrate le liste opzionali di comandi installati.

## Come funziona

Un event di kind 31992 definisce un comando. I tag obbligatori indicano la parola di attivazione senza barra, un titolo e una descrizione d'uso. Attraverso tag `arg` ordinati si dichiarano gli argomenti posizionali, con tipi come pubkey, event, relay, number, enum o text. I tag `s` limitano quali event attivano il comando in base a kind, relay, autore o tag. Questi ambiti funzionano come un filtro: i valori dello stesso tipo sono alternative, e ogni tipo presente deve corrispondere.

Un'invocazione è un testo che inizia all'indice 0 del contenuto di un event, come `/ban` seguito da argomenti, e non porta alcun tag. Aggiungendo un qualificatore della forma `@nostr:npub1...` ci si rivolge a un singolo esecutore. In assenza di qualificatore può agire ogni comando la cui parola di attivazione corrisponde e il cui ambito include l'event, per cui un solo messaggio può attivare più servizi.

Il supporto da parte dei client è opzionale. I client possono offrire completamento automatico, selettori di argomenti e chip renderizzati. Non devono subordinare l'invio di un'invocazione al proprio supporto, e devono inviare come contenuto ordinario il testo che non supera il parsing.

Nei gruppi basati su relay, definizioni e invocazioni vanno al relay del gruppo. Per l'uso in broadcast, le definizioni vanno agli outbox degli esecutori e le invocazioni ai loro inbox.

## Liste di comandi installati

Un utente può mantenere una lista opzionale di kind 10992, conforme a NIP-51, contenente tag `a` che puntano a definizioni di comandi di kind 31992 tramite la pubkey dell'esecutore e il valore `d`, con un suggerimento di relay facoltativo. I client dovrebbero usare la lista per il completamento automatico e per i chip renderizzati. Ciò che la lista registra è una preferenza dell'utente in materia di visualizzazione e scoperta. Non autorizza un esecutore, e l'invocazione in testo semplice funziona anche senza di essa. Questa parte della specifica è stata integrata il 27 ottobre 2026 tramite la PR #2525. Dal merge non risulta quali client abbiano implementato la lista.

## Fonti primarie

- [Specifica NIP-CD](https://github.com/nostr-protocol/nips/blob/master/CD.md)
- [Merge di NIP-CD del 21 ottobre 2026](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4)
- [PR #2525 per le liste di comandi installati, integrata il 27 ottobre 2026](https://github.com/nostr-protocol/nips/pull/2525)
- [Commit del 26 ottobre 2026 dalla PR #2525, effettuato sul suo branch prima del merge](https://github.com/nostr-protocol/nips/commit/0142de0384210d69074c089448ef5bc303faef37)
- [Merge del 27 ottobre 2026 delle liste di comandi installati in NIP-CD](https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157)

## Citato in
- [Newsletter #46: NIP-CD definisce comandi invocati come testo semplice](/it/newsletters/2026-10-28-newsletter/#nip-cd-defines-commands-invoked-as-plain-text) Newsletter

- [Newsletter #46: NIP-CD aggiunge liste opzionali di comandi installati](/it/newsletters/2026-10-28-newsletter/#nip-cd-adds-optional-installed-command-lists) Newsletter

- [Newsletter #46 (2026-10-28): ottobre 2026, significati condivisi delle query e servizi attivati da testo](/it/newsletters/2026-10-28-newsletter/#october-2026-shared-query-meanings-and-text-triggered-services)

## Vedi anche

- [NIP-01: protocollo di base](/it/topics/nip-01/)
