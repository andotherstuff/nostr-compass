---
title: "ContextVM"
date: 2026-02-25
translationOf: /en/topics/contextvm.md
translationDate: 2026-03-07
draft: false
categories:
  - Infrastructure
  - AI
  - Protocol
---
ContextVM è un protocollo e una toolchain per trasportare traffico MCP (Model Context Protocol) su Nostr. Permette a client e server MCP di trovarsi e scambiare messaggi firmati senza dipendere da un registro centrale, domini o OAuth.

## Come funziona

L'SDK di ContextVM fornisce transport client e server TypeScript per MCP su Nostr. I server MCP esistenti possono restare sui loro transport normali mentre un gateway li espone a Nostr, e i client senza supporto Nostr nativo possono connettersi tramite un livello proxy.

I relay agiscono come message bus. Instradano gli eventi, mentre firma e cifratura forniscono autenticazione degli endpoint e privacy di transport.

## Componenti

**SDK**: libreria TypeScript con transport client/server, supporto proxy e funzionalità gateway per collegare server MCP locali a Nostr.

**CVMI**: interfaccia a riga di comando per scoperta dei server e invocazione dei metodi.

**Relatr**: servizio di trust scoring che calcola punteggi personalizzati dalla distanza nel social graph e dalla validazione del profilo.

## Perché conta

ContextVM è un ponte di transport, non un sostituto di MCP stesso. Questo conta perché riduce il costo di adozione: un server MCP esistente può ottenere raggiungibilità via Nostr senza riscrivere il proprio schema degli strumenti o la propria business logic.

Il lavoro recente su ContextVM ha anche spinto la consegna effimera per il traffico gift-wrapped. Questo è utile per tool call e risposte intermedie in cui l'archiviazione durevole sui relay non è necessaria e può creare esposizione aggiuntiva della privacy.

## Note sull'interoperabilità

Tra febbraio e marzo 2026, il progetto è passato dall'implementazione alla standardizzazione. Il team ha aperto proposte NIP per MCP JSON-RPC su Nostr e per una variante effimera del gift wrap. Anche se queste proposte cambieranno, mostrano con più chiarezza il confine del protocollo: MCP resta il livello applicativo, Nostr gestisce scoperta e transport.

---

**Fonti primarie:**
- [ContextVM Website](https://contextvm.org)
- [ContextVM SDK](https://github.com/ContextVM/sdk)
- [CVMI CLI](https://github.com/ContextVM/cvmi)
- [Relatr](https://github.com/ContextVM/relatr)
- [NIP PR #2245: Ephemeral Gift Wrap](https://github.com/nostr-protocol/nips/pull/2245)
- [NIP PR #2246: MCP JSON-RPC over Nostr](https://github.com/nostr-protocol/nips/pull/2246)

**Citato in:**
- [Newsletter #11: ContextVM News](/en/newsletters/2026-02-25-newsletter/#contextvm-mcp-over-nostr)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**Vedi anche:**
- [NIP-90: Data Vending Machines](/it/topics/nip-90/)
