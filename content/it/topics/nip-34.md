---
title: "NIP-34 (Collaborazione Git)"
date: 2026-02-04
description: "NIP-34 abilita l'hosting decentralizzato di repository git e la collaborazione attraverso eventi Nostr."
---

NIP-34 definisce i tipi di evento per ospitare repository git, patch e issue sui relay Nostr. Questo abilita la collaborazione sul codice completamente decentralizzata senza dipendenza da piattaforme di hosting centralizzate come GitHub o GitLab.

## Come Funziona

I repository sono rappresentati come eventi addressable (kind 30617) contenenti metadati come nome, descrizione e URL per il clone. Il proprietario del repository pubblica questo evento per stabilire il progetto su Nostr.

Le patch (kind 1617) contengono contenuto git patch che può essere applicato a un repository. I contributori inviano patch come eventi che fanno riferimento al repository target. Questo rispecchia il flusso di lavoro basato su email usato da progetti come il kernel Linux.

Le issue (kind 1621) funzionano come i tradizionali issue tracker. Fanno riferimento a un repository e contengono un titolo e una descrizione. I commenti su issue e patch usano eventi di risposta standard.

## Tipi di Evento

- **30617** - Annuncio repository (addressable)
- **1617** - Invio patch
- **1621** - Issue
- **1622** - Stato issue (aperto/chiuso)

## Implementazioni

- **ngit** - Strumento da riga di comando per pubblicare repo e patch su Nostr
- **gitworkshop.dev** - Interfaccia web per sfogliare repository ospitati su Nostr
- **Notedeck** - Client desktop con [supporto bozza per visualizzazione NIP-34](https://github.com/damus-io/notedeck/pull/1279)

## Fonti Primarie

- [Specifica NIP-34](https://github.com/nostr-protocol/nips/blob/master/34.md)

## Menzionato In

- [Newsletter #8 (2026-02-04)](/it/newsletters/2026-02-04-newsletter/) - Notedeck aggiunge visualizzatore NIP-34
