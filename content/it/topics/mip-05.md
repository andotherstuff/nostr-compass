---
title: "MIP-05: Privacy-Preserving Push Notifications"
date: 2025-12-17
translationOf: /en/topics/mip-05/
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---
MIP-05 definisce un protocollo di push notification per i client Marmot che prova a preservare la privacy in un contesto in cui i normali sistemi push mobile di solito espongono token del dispositivo e relazioni tra account.

## Come funziona

- I token del dispositivo sono cifrati con ECDH+HKDF e ChaCha20-Poly1305
- Le chiavi effimere impediscono la correlazione tra notifiche
- Un protocollo gossip a tre eventi (kind 447-449) sincronizza i token cifrati tra i membri del gruppo
- I token esca tramite gift wrapping NIP-59 nascondono la dimensione dei gruppi

## Modello di privacy

- I server di push notification non possono identificare gli utenti
- L'appartenenza ai gruppi non viene rivelata dai pattern di notifica
- I token del dispositivo non possono essere correlati tra i messaggi

Il miglioramento concreto è che il provider push vede token di consegna opachi, non una mappa diretta tra membro del gruppo e dispositivo. Questo non rende le notifiche anonime in senso assoluto, ma riduce quanto il livello push apprende per impostazione predefinita.

## Kind degli eventi

- **Kind 447**: pubblicazione cifrata del token del dispositivo
- **Kind 448**: richiesta di sincronizzazione del token
- **Kind 449**: risposta di sincronizzazione del token

## Compromessi

MIP-05 aggiunge privacy aggiungendo lavoro di coordinamento. I client devono sincronizzare lo stato dei token cifrati tra i membri del gruppo, e i token esca aumentano volutamente l'overhead dei messaggi.

Questo significa che chi implementa il protocollo deve bilanciare affidabilità della consegna e protezione dei metadati. Il protocollo è utile proprio perché tratta il push come un problema di privacy, non solo come una comodità di trasporto.

---

**Fonti primarie:**
- [MIP-05 Specification](https://github.com/marmot-protocol/marmot/blob/master/05.md)
- [MIP-05 PR](https://github.com/marmot-protocol/marmot/pull/18)
- [White Noise v0.2.1 release](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Citato in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Vedi anche:**
- [Marmot Protocol](/it/topics/marmot/)
- [NIP-59: Gift Wrap](/it/topics/nip-59/)
