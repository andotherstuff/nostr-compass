---
title: "Quartz"
date: 2025-12-31
translationOf: /en/topics/quartz.md
translationDate: 2026-03-07
draft: false
categories:
  - Bibliothek
  - Entwicklung
---

Quartz ist eine Kotlin-Multiplatform-Bibliothek für Nostr, entwickelt von Vitor Pamplona. Sie ist die gemeinsame Protokoll- und Datenschicht hinter Amethysts Weg zu Android, Desktop und später iOS aus einer einzigen Codebasis.

## Funktionsweise

Quartz stellt zentrale Nostr-Funktionalität als gemeinsam genutzte Bibliothek bereit:

- **Event Handling**: Parsing, Validierung und Erstellung von Nostr-Events
- **Cryptography**: Secp256k1-Signierung, NIP-44-Verschlüsselung und Schlüsselverwaltung
- **Relay Communication**: Verbindungsverwaltung, Nachrichtenreihenfolge und Subscription-Handling
- **NIP Support**: Implementierung gängiger NIPs, darunter NIP-06, NIP-19, NIP-44 und weitere

## Warum das wichtig ist

Quartz verschiebt protokollschwere Logik aus einer einzelnen App in eine wiederverwendbare Bibliothek. Das ist wichtig, weil Relay-Handling, Event-Parsing, Verschlüsselung und Speicherregeln so leichter zwischen Clients geteilt werden können, statt auf jeder Plattform neu implementiert zu werden.

Das konkrete Ergebnis war bereits in Amethysts Desktop-Arbeit sichtbar. Der durch Grants finanzierte Refactor verlagerte gemeinsamen Code in Kotlin-Multiplatform-Module wie `commonMain`, `jvmAndroid` und `jvmMain`, sodass Desktop-Unterstützung eher ein Bibliotheks- und Modulproblem als ein kompletter Rewrite wurde.

## Architektur

Die Bibliothek nutzt eine modulare Source-Set-Struktur:
- `commonMain`: Gemeinsamer Code für alle Plattformen
- `jvmAndroid`: Code, der von JVM und Android geteilt wird
- `androidMain`: Android-spezifische Implementierungen
- `jvmMain`: JVM-Implementierungen für Desktop
- `iosMain`: iOS-spezifische Implementierungen

## Aktueller Stand

Im Dezember 2025 kündigte OpenSats die Finanzierung von Quartz in der vierzehnten Welle seiner Nostr-Grants an. Das Repo existiert als eigenständige Bibliothek, aber ein großer Teil des sichtbaren Fortschritts landete bisher über Amethyst-PRs, die App-Module in Multiplatform-Code umwandeln und Feature-Parität über mehrere Ziele hinweg verfolgen.

---

**Primärquellen:**
- [Quartz Repository](https://github.com/vitorpamplona/quartz)
- [Quartz on Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Amethyst Repository](https://github.com/vitorpamplona/amethyst)
- [OpenSats Fourteenth Wave of Nostr Grants](https://opensats.org/blog/fourteenth-wave-of-nostr-grants)

**Erwähnt in:**
- [Newsletter #3: December Recap](/de/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3: News](/de/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3: Amethyst Notable Changes](/de/newsletters/2025-12-31-newsletter/#amethyst-android)

**Siehe auch:**
- [Blossom Protocol](/de/topics/blossom/)
