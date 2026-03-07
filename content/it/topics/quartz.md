---
title: "Quartz"
date: 2025-12-31
translationOf: /en/topics/quartz.md
translationDate: 2026-03-07
draft: false
categories:
  - Library
  - Development
---
Quartz è una libreria Nostr Kotlin Multiplatform sviluppata da Vitor Pamplona. È il livello condiviso di protocollo e dati dietro la spinta di Amethyst verso Android, desktop e in prospettiva iOS a partire da un'unica codebase.

## Come funziona

Quartz fornisce le funzionalità principali di Nostr come libreria condivisa:

- **Gestione degli eventi**: parsing, validazione e creazione di eventi Nostr
- **Crittografia**: firme Secp256k1, cifratura NIP-44, gestione delle chiavi
- **Comunicazione con i relay**: gestione delle connessioni, ordinamento dei messaggi, gestione delle subscription
- **Supporto ai NIP**: implementazione di NIP comuni tra cui NIP-06, NIP-19, NIP-44 e altri

## Perché è importante

Quartz sposta la logica pesante di protocollo fuori da una singola app e dentro una libreria riutilizzabile. Questo conta perché la gestione dei relay, il parsing degli eventi, la cifratura e le regole di storage diventano più facili da condividere tra i client invece di essere reimplementati per ogni piattaforma.

Il risultato concreto si è già visto nel lavoro desktop di Amethyst. Il refactor finanziato dal grant ha spostato il codice condiviso in moduli Kotlin Multiplatform come `commonMain`, `jvmAndroid` e `jvmMain`, trasformando il supporto desktop in un problema di libreria e moduli invece che in una riscrittura completa.

## Architettura

La libreria usa una struttura modulare di source set:
- `commonMain`: codice condiviso per tutte le piattaforme
- `jvmAndroid`: codice condiviso tra JVM e Android
- `androidMain`: implementazioni specifiche per Android
- `jvmMain`: implementazioni desktop JVM
- `iosMain`: implementazioni specifiche per iOS

## Stato attuale

Nel dicembre 2025, OpenSats ha annunciato il finanziamento di Quartz nella sua quattordicesima ondata di grant Nostr. Il repo esiste come libreria autonoma, ma gran parte dei progressi visibili finora è arrivata tramite PR di Amethyst che convertono i moduli dell'app in codice multipiattaforma e tracciano la parità di funzionalità tra i target.

---

**Fonti primarie:**
- [Repository di Quartz](https://github.com/vitorpamplona/quartz)
- [Quartz su Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Repository di Amethyst](https://github.com/vitorpamplona/amethyst)
- [Quattordicesima ondata di grant Nostr di OpenSats](https://opensats.org/blog/fourteenth-wave-of-nostr-grants)

**Citato in:**
- [Newsletter #3: Riepilogo di dicembre](/en/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3: Notizie](/en/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3: Cambiamenti rilevanti in Amethyst](/en/newsletters/2025-12-31-newsletter/#amethyst-android)

**Vedi anche:**
- [Protocollo Blossom](/it/topics/blossom/)
