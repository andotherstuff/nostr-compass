---
title: "Buzz NIP-FA: adattatore di identità federata"
date: 2026-10-21
draft: false
categories: ["NIPs"]
translationOf: /en/topics/nip-fa.md
translationDate: 2026-11-05
---

Buzz NIP-FA è una specifica in bozza e opzionale del progetto Buzz. Si colloca al di fuori dei NIP accettati del repository ufficiale nostr-protocol/nips.

Definisce un contratto HTTP neutrale rispetto al provider tra un client Nostr e un adattatore di identità aziendale. Dopo un login tramite browser, l'adattatore mantiene una sessione per l'utente. Emette asserzioni Buzz NIP-FI locali al progetto che associano l'utente a una chiave Nostr, di cui il client dimostra il controllo con [NIP-98](/it/topics/nip-98/). [L'operatore sceglie la durata di ciascuna asserzione](https://github.com/block/buzz/pull/8934), che deve rispettare il maximum_assertion_age dell'emittente accettato dal relay, ed exp non può superare la scadenza della sessione dell'adattatore. La durata scelta limita per quanto tempo una chiave revocata potrebbe ancora riconnettersi dopo un riavvio del relay, e i client non devono rifiutare un'asserzione solo a causa della sua durata. NIP-FI e i NIP ufficiali restano invariati. Il login usa una challenge di handoff S256 e una callback di loopback su `127.0.0.1` o `[::1]` che riceve un codice monouso. I sistemi upstream come OIDC o SAML restano dietro l'adattatore. L'individuazione dei relay che richiedono un'identità aziendale è demandata ad altre specifiche.

Fonte primaria: la [specifica NIP-FA](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md) nel repository Buzz.

## Credenziali per agenti {#agent-credentials}

Buzz ha integrato una [bozza NIP-FA per credenziali di agenti autorizzate dal proprietario](https://github.com/block/buzz/pull/9015), che definisce route di concessione, asserzione e revoca per gli agenti che un proprietario ha autorizzato tramite NIP-OA. Una concessione deriva da uno scambio di token RFC 8693 che abbina la sessione del proprietario a una prova [NIP-98](/it/topics/nip-98/) dell'agente. Per ottenere un'asserzione, l'agente presenta la concessione come token Bearer insieme alla propria prova, e i client verificano l'`iss` dell'asserzione rispetto all'emittente della concessione. Le prove degli agenti sono monouso e appartengono solo alle route di concessione e di asserzione. La revoca avviene sulla sessione del proprietario senza alcuna prova dell'agente; revoca la chiave dell'agente e le sue concessioni e disconnette l'agente. La policy dell'adattatore decide la durata della concessione. Le condizioni di autorizzazione non supportate vengono rifiutate, e una chiave revocata non può registrarsi di nuovo. NIP-FA è una specifica di Buzz, non un NIP accettato. L'integrazione riguarda solo il codice sorgente, senza alcuna dichiarazione di attivazione in produzione, di una build rilasciata o di interoperabilità.

## Fonti primarie {#primary-sources}

- [Buzz NIP-FA: adattatore di identità federata](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md)

- [Route per le credenziali di agenti autorizzate dal proprietario](https://github.com/block/buzz/pull/9015)

## Citato in {#mentioned-in}

- [Newsletter #47: credenziali per agenti di Buzz](/it/newsletters/2026-11-04-newsletter/#buzz-defines-owner-authorized-agent-credential-routes)


- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#buzz)
