---
title: 'Bozza Buzz NIP-AM: metriche dei turni dell''agente'
date: 2026-10-28
translationOf: /en/topics/nip-am.md
translationDate: 2026-10-28
draft: false
---

**Stato:** questa è una proposta in bozza specifica del progetto Buzz. NIP-AM non è una NIP ufficiale accettata. L'etichetta proviene dalla documentazione del progetto Buzz, e il repository ufficiale delle NIP non l'ha né assegnata né approvata.

## Scopo

NIP-AM registra l'utilizzo per ogni turno completato di un agente AI. Per ciascun turno l'agente pubblica un event `kind:44200`, che la convenzione di Buzz tratta come un event regolare di sola aggiunta (append-only). Il contenuto è cifrato con NIP-44 dall'agente al proprietario. Al suo interno si trovano i dati sull'utilizzo dei token insieme agli ID di correlazione, e gli eventuali valori di costo sono stime. Non contiene alcuna trascrizione della conversazione.

## Limiti

I tag pubblici identificano il proprietario e l'agente, e i relay possono comunque vedere quando vengono pubblicati gli event. Il formato, quindi, non nasconde che un'attività sia avvenuta. Un valore di utilizzo mancante significa "sconosciuto" e non deve mai essere conteggiato come zero.

## Proposta sui lettori delegati

Una pull request di documentazione ancora aperta, la #8582, propone un'autorizzazione (grant) a privilegio minimo firmata dal proprietario. In base a questa, l'agente pubblicherebbe una copia cifrata separata per ogni lettore attivo, ciascuna legata all'ID esatto dell'event di grant. La pull request non modifica alcuna autorizzazione a runtime. Restano questioni aperte sia il kind di grant proposto `30180` sia il limite massimo di lettori, e nemmeno la politica di revoca è stata ancora definita. La revoca potrebbe limitare la cronologia sui relay e le letture future. Non può però cancellare le copie che un lettore ha già ricevuto.

## Fonti primarie

- [Bozza Buzz NIP-AM: metriche dei turni dell'agente (revisione fissata)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-AM.md)
- [Pull request Buzz #8582: lettori delegati delle metriche (bozza aperta)](https://github.com/block/buzz/pull/8582)

## Vedi anche

- [NIP-44](/it/topics/nip-44/)

**Citato in:**

- [Newsletter #46: testo della bozza NIP-AM per i lettori delegati delle metriche](/it/newsletters/2026-10-28-newsletter/#draft-nip-am-text-for-delegated-metric-readers)
- [Newsletter #46: Buzz](/it/newsletters/2026-10-28-newsletter/#buzz)
