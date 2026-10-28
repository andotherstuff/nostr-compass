---
title: 'Bozza NIP-RS di Buzz: sincronizzazione dello stato di lettura tra dispositivi'
date: 2026-10-28
translationOf: /en/topics/nip-rs.md
translationDate: 2026-10-28
draft: false
---

**Stato:** Si tratta di una bozza di proposta specifica del progetto Buzz. NIP-RS non è un NIP ufficiale accettato. L'etichetta proviene dalla documentazione del progetto Buzz, e il repository ufficiale dei NIP non l'ha né assegnata né approvata.

## Scopo

NIP-RS permette ai dispositivi di uno stesso utente di condividere il punto fino a cui quell'utente ha letto. Ogni installazione pubblica un event indirizzabile `kind:30078`. Il suo tag `d` è `read-state:` seguito da un ID di slot casuale, mentre il contenuto è cifrato con NIP-44 verso la chiave dell'utente stesso. Nel testo in chiaro, gli ID di contesto sono associati a frontiere temporali, ciascuna delle quali indica che tutto ciò che si colloca in quel momento o prima è stato letto. La bozza non pubblica conferme di lettura e non rivela che cosa abbiano letto altre persone.

## Limiti

Le frontiere sono indicazioni best-effort sull'attività recente. Non costituiscono una cronologia completa dei messaggi letti. Le sovrascritture manuali dello stato "non letto", comprese le soglie tombstone, seguono un contratto durevole separato. Il caricamento dello stato completo delle sovrascritture dipende dall'ordinamento dei relay e dal loro comportamento in termini di capacità, che un client non è in grado di verificare del tutto; di conseguenza, un relay arbitrario potrebbe non restituire uno stato completo dei messaggi non letti. Per lo più, gli ID di contesto hanno significato solo all'interno di una stessa famiglia di client.

Una pull request aperta, la #8639, propone di spostare i client Buzz su una capability NIP-11 `buzz_v1` supportata da un'API HTTP privata e autenticata, disattivata per impostazione predefinita. I relay privi di quella capability continuerebbero a usare NIP-RS.

## Fonti primarie

- [Bozza NIP-RS di Buzz: sincronizzazione dello stato di lettura tra dispositivi (revisione fissata)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-RS.md)
- [Pull request di Buzz #8639: stato di lettura tramite una capability del relay (aperta)](https://github.com/block/buzz/pull/8639)

## Vedi anche

- [NIP-44](/it/topics/nip-44/)
- [NIP-78](/it/topics/nip-78/)

**Citato in:**

- [Newsletter #46: Buzz](/it/newsletters/2026-10-28-newsletter/#buzz)
