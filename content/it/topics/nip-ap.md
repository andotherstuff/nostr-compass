---
title: "Buzz NIP-AP: persona degli agenti"
date: 2026-10-21
translationOf: /en/topics/nip-ap.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

Buzz NIP-AP è una specifica in bozza del progetto Buzz, esterna alle NIP accettate in nostr-protocol/nips.

Definisce gli event persona di kind 30175, cioè definizioni indirizzabili per istanziare un agente AI, identificate da uno slug `d` in chiaro. Il kind 30178 contiene una proiezione del catalogo del team. I relay che implementano la specifica applicano un controllo d'accesso a entrambi i kind: gli autori leggono i propri event, mentre gli altri lettori vedono un event in query, consegna in tempo reale, ricerca, conteggi o ricerche per id solo se porta `["shared", "true"]`. Condividere un team espone la proiezione incorporata e le istruzioni di ogni membro, compresi i membri le cui persona non sono condivise. Il controllo regola l'accesso senza cifrare il contenuto; l'operatore del relay può comunque leggerlo.

Fonte primaria: la [specifica NIP-AP](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md) nel repository di Buzz.

## Fonti primarie

- [Buzz NIP-AP: persona degli agenti](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md)

## Citato in

- [Newsletter #46 (2026-10-28): buzz](/it/newsletters/2026-10-28-newsletter/#buzz)

- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#buzz)
