---
title: "Quartz"
date: 2025-12-31
translationOf: /en/topics/quartz.md
translationDate: 2025-12-31
draft: false
categories:
  - Bibliothek
  - Entwicklung
---

Quartz ist eine Kotlin Multiplatform Bibliothek für Nostr, entwickelt von Vitor Pamplona. Ursprünglich aus dem Amethyst Android-Client extrahiert, bietet Quartz wiederverwendbare Nostr-Protokoll-Implementierungen für JVM-, Android-, iOS- und Linux-Plattformen.

## So Funktioniert Es

Quartz stellt Nostr-Kernfunktionalität als gemeinsam genutzte Bibliothek bereit:

- **Event-Verarbeitung**: Parsing, Validierung und Erstellung von Nostr-Events
- **Kryptographie**: Secp256k1-Signierung, NIP-44-Verschlüsselung, Schlüsselverwaltung
- **Relay-Kommunikation**: Verbindungsverwaltung, Nachrichtenordnung, Abonnement-Handling
- **NIP-Unterstützung**: Implementierung gängiger NIPs einschließlich NIP-06, NIP-19, NIP-44 und mehr

## Hauptmerkmale

- **Kotlin Multiplatform**: Eine einzige Codebasis kompiliert für mehrere Ziele
- **Zielplattformen**: Android, JVM, iOS (ARM64, Simulator), Linux
- **Performance-Optimiert**: Effiziente Event-Verarbeitung und kryptographische Operationen
- **Blossom-Integration**: Unterstützung für Medien-Uploads über das Blossom-Protokoll
- **OpenTimestamp**: Vollständiger Kotlin-Port für Zeitstempelverifizierung

## Architektur

Die Bibliothek verwendet eine modulare Source-Set-Struktur:
- `commonMain`: Gemeinsamer Code für alle Plattformen
- `jvmAndroid`: Code, der zwischen JVM und Android geteilt wird
- `androidMain`: Android-spezifische Implementierungen
- `jvmMain`: Desktop-JVM-Implementierungen
- `iosMain`: iOS-spezifische Implementierungen

## OpenSats-Förderung

Im Dezember 2025 kündigte OpenSats die Finanzierung von Quartz als Teil ihrer vierzehnten Welle von Nostr-Förderungen an. Die Förderung unterstützt die fortlaufende Entwicklung zur Ermöglichung von Amethyst auf iOS durch denselben Kotlin Multiplatform-Ansatz, der bereits die Android- und Desktop-Versionen antreibt.

---

**Primäre Quellen:**
- [Quartz auf Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Amethyst Repository](https://github.com/vitorpamplona/amethyst)

**Erwähnt in:**
- [Newsletter #3: Dezember-Rückblick](/de/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3: Neuigkeiten](/de/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3: Wichtige Amethyst-Änderungen](/de/newsletters/2025-12-31-newsletter/#amethyst-android)

**Siehe auch:**
- [Blossom-Protokoll](/de/topics/blossom/)
