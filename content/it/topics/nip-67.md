---
title: "NIP-67: Indicatore di Completezza EOSE"
date: 2026-04-22
translationOf: /en/topics/nip-67.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-67 è una proposta aperta che estende il messaggio `EOSE` esistente in [NIP-01](/it/topics/nip-01/) con un terzo elemento facoltativo che indica se il relay ha consegnato tutti gli eventi memorizzati che corrispondono al filtro. L'obiettivo è sostituire l'euristica poco affidabile che i client usano oggi per capire se una subscription è davvero esaurita o è stata interrotta da un limite imposto dal relay.

## Il problema

`EOSE` segna il confine tra eventi memorizzati ed eventi in tempo reale, ma non dice nulla sulla completezza. In pratica i relay impongono un limite per subscription, spesso tra 300 e 1000 eventi, indipendente dal `limit` richiesto dal client. Un client che chiede le ultime 500 note a un relay limitato a 300 riceve 300 eventi e un `EOSE`, senza poter distinguere tra "questi sono tutti" e "ci siamo fermati a metà". Il workaround attuale consiste nel confrontare il numero di eventi con il `limit` del client e paginare in modo difensivo, ma questo può sia perdere eventi quando il limite del relay è più basso, sia sprecare un round trip quando il limite coincide con il numero reale dei risultati.

I pareggi sui boundary peggiorano la situazione. Paginare con `until = oldest_created_at` rischia di perdere o duplicare eventi che condividono il timestamp più vecchio del batch, a seconda di come il relay confronta i timestamp.

## Il cambiamento

NIP-67 aggiunge un terzo elemento facoltativo a `EOSE`:

```
["EOSE", "<subscription_id>", "finish"]   // tutti gli eventi memorizzati corrispondenti sono stati consegnati
["EOSE", "<subscription_id>"]             // nessuna affermazione di completezza (legacy)
```

Viene definito solo il segnale positivo. Un relay che dichiara il supporto a NIP-67 ma omette l'indicatore sta dicendo che c'è altro. Un relay che non dichiara il supporto continua a usare l'euristica esistente, quindi il cambiamento è retrocompatibile con tutti i client e relay attuali.

I client che sanno che il relay supporta NIP-67 possono smettere di paginare non appena vedono `"finish"`, evitare il round trip extra obbligatorio quando il limite coincide esattamente con il result set e mostrare all'utente un'informazione di completezza accurata.

## Stato

La proposta è [aperta come PR #2317](https://github.com/nostr-protocol/nips/pull/2317) nel repository dei NIP.

---

**Fonti primarie:**
- [PR #2317: NIP-67 EOSE Completeness Hint](https://github.com/nostr-protocol/nips/pull/2317)
- [Specifica NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Menzionato in:**
- [Newsletter #19: NIP Updates](/en/newsletters/2026-04-22-newsletter/)

**Vedi anche:**
- [NIP-01: Flusso del protocollo di base](/it/topics/nip-01/)
- [NIP-11: Relay Information Document](/it/topics/nip-11/)
