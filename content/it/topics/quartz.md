---
title: "Quartz"
date: 2025-12-31
translationOf: /en/topics/quartz.md
translationDate: 2025-12-31
draft: false
categories:
  - Libreria
  - Sviluppo
---

Quartz è una libreria Kotlin Multiplatform per Nostr sviluppata da Vitor Pamplona. Originariamente estratta dal client Android Amethyst, Quartz fornisce implementazioni riutilizzabili del protocollo Nostr per piattaforme JVM, Android, iOS e Linux.

## Come Funziona

Quartz fornisce funzionalità core di Nostr come libreria condivisa:

- **Gestione Eventi**: Parsing, validazione e creazione di eventi Nostr
- **Crittografia**: Firma Secp256k1, crittografia NIP-44, gestione delle chiavi
- **Comunicazione con i Relay**: Gestione delle connessioni, ordinamento dei messaggi, gestione delle sottoscrizioni
- **Supporto NIP**: Implementazione di NIP comuni inclusi NIP-06, NIP-19, NIP-44 e altri

## Caratteristiche Principali

- **Kotlin Multiplatform**: Un'unica base di codice compila per più target
- **Piattaforme Target**: Android, JVM, iOS (ARM64, Simulatore), Linux
- **Ottimizzato per le Prestazioni**: Elaborazione efficiente degli eventi e operazioni crittografiche
- **Integrazione Blossom**: Supporto per upload di media tramite il protocollo Blossom
- **OpenTimestamp**: Port Kotlin completo per la verifica dei timestamp

## Architettura

La libreria utilizza una struttura modulare di source set:
- `commonMain`: Codice condiviso per tutte le piattaforme
- `jvmAndroid`: Codice condiviso tra JVM e Android
- `androidMain`: Implementazioni specifiche per Android
- `jvmMain`: Implementazioni JVM desktop
- `iosMain`: Implementazioni specifiche per iOS

## Sovvenzione OpenSats

A dicembre 2025, OpenSats ha annunciato il finanziamento per Quartz come parte della sua quattordicesima ondata di sovvenzioni Nostr. La sovvenzione supporta lo sviluppo continuo per abilitare Amethyst su iOS attraverso lo stesso approccio Kotlin Multiplatform che già alimenta le versioni Android e desktop.

---

**Fonti principali:**
- [Quartz su Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Repository Amethyst](https://github.com/vitorpamplona/amethyst)

**Menzionato in:**
- [Newsletter #3: Riepilogo di Dicembre](/it/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3: Notizie](/it/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3: Modifiche Rilevanti di Amethyst](/it/newsletters/2025-12-31-newsletter/#amethyst-android)

**Vedi anche:**
- [Protocollo Blossom](/it/topics/blossom/)
