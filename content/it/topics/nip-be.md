---
title: "NIP-BE: Bluetooth Low Energy"
date: 2025-12-17
translationOf: /en/topics/nip-be/
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Connectivity
---
NIP-BE specifica come le applicazioni Nostr possono comunicare e sincronizzarsi tramite Bluetooth Low Energy, permettendo ad app capaci di funzionare offline di sincronizzare dati tra dispositivi vicini senza connettività internet.

## Come funziona

NIP-BE riutilizza i normali message frame di Nostr su BLE invece di inventare un modello di eventi separato. I dispositivi annunciano un servizio BLE più un UUID del dispositivo, confrontano gli UUID quando si incontrano e decidono in modo deterministico quale lato diventa il server GATT e quale lato diventa il client GATT.

Il servizio GATT usa una struttura in stile Nordic UART con una characteristic di scrittura e una characteristic di lettura/notifica. Questo mantiene il trasporto abbastanza semplice per gli stack mobili con risorse limitate pur trasportando normali messaggi Nostr.

## Struttura dei messaggi

BLE ha limiti ridotti di payload, quindi NIP-BE comprime i messaggi con DEFLATE, li divide in chunk indicizzati e invia un solo messaggio alla volta. La specifica limita i messaggi a 64 KB, un promemoria utile del fatto che questo trasporto è pensato per la sincronizzazione e la propagazione locale, non per trasferimenti massivi.

## Modello di sincronizzazione

Dopo che una connessione è stata stabilita, i peer usano un flusso di sincronizzazione half-duplex basato sui messaggi di negentropy di [NIP-77](https://github.com/nostr-protocol/nips/blob/master/77.md) come `NEG-OPEN`, `NEG-MSG`, `EVENT` ed `EOSE`. Questa scelta conta perché permette alle implementazioni di riusare la logica di sync con i relay già esistente invece di costruire un algoritmo di replica solo per BLE.

La regola half-duplex riflette anche la realtà dei link BLE instabili. Le connessioni intermittenti a corto raggio funzionano meglio quando ogni lato sa con precisione a chi tocca parlare.

## Perché è importante

NIP-BE offre alle applicazioni Nostr una strada per il networking local-first. Due telefoni possono sincronizzare note o stato dei relay direttamente quando sono vicini, anche se nessuno dei due ha internet funzionante. Questo rende BLE utile per la resistenza alla censura, gli scenari di emergenza e le app social con bassa connettività.

I vincoli sono altrettanto importanti: la banda BLE è bassa, le connessioni durano poco e grandi cronologie non si adattano bene. In pratica, NIP-BE è più adatto alla sync incrementale e alla diffusione di messaggi tra dispositivi vicini, non alla replica archivistica completa.

---

**Fonti primarie:**
- [Specifica NIP-BE](https://github.com/nostr-protocol/nips/blob/master/BE.md)
- [PR #1979](https://github.com/nostr-protocol/nips/pull/1979)

**Citato in:**
- [Newsletter #1: Notizie](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3: Riepilogo di dicembre](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Vedi anche:**
- [NIP-01: Protocollo di base](/it/topics/nip-01/)
