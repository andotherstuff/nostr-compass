---
title: 'Bozza NIP-OA di Buzz: attestazione del proprietario'
date: 2026-10-28
translationOf: /en/topics/nip-oa.md
translationDate: 2026-10-28
draft: false
---

**Stato:** Si tratta di una bozza di proposta specifica del progetto Buzz. NIP-OA non è un NIP ufficiale accettato. L'etichetta proviene dalla documentazione del progetto Buzz, e il repository ufficiale dei NIP non l'ha né assegnata né approvata.

## Scopo

NIP-OA definisce un tag facoltativo `auth` che consente a una chiave del proprietario di autorizzare una chiave agente a pubblicare event. L'autore dell'event resta la chiave dell'agente. Un tag valido vale solo come prova di autorizzazione e non permette all'agente di impersonare il proprietario.

## Meccanismo

Con una firma Schnorr, il proprietario firma un hash con separazione di dominio che vincola la pubkey dell'agente a una stringa di condizioni esatta. Le condizioni possono richiedere un determinato kind di event e fissare limiti sul `created_at` autodichiarato. L'agente può riutilizzare il tag sui propri event, purché ciascun event soddisfi le condizioni. I verificatori convalidano prima l'event di base, poi controllano la firma del proprietario e ogni singola condizione.

## Limiti

Una stringa di condizioni vuota non aggiunge alcun vincolo. Le clausole sui timestamp vincolano un campo controllato dall'agente, perciò non forniscono una scadenza basata sull'ora reale. Chi ha bisogno di garantire la freschezza deve verificarla separatamente. La pubblicazione del tag in forma pubblica collega tra loro le chiavi del proprietario e dell'agente.

## Fonti primarie

- [Bozza NIP-OA di Buzz: attestazione del proprietario (revisione fissata)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-OA.md)

## Vedi anche

- [NIP-01](/it/topics/nip-01/)

**Citato in:**

- [Newsletter #46: Buzz](/it/newsletters/2026-10-28-newsletter/#buzz)
