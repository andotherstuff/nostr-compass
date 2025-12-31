---
title: "Quartz"
date: 2025-12-31
translationOf: /en/topics/quartz.md
translationDate: 2025-12-31
draft: false
categories:
  - Bibliotheek
  - Ontwikkeling
---

Quartz is een Kotlin Multiplatform bibliotheek voor Nostr, ontwikkeld door Vitor Pamplona. Oorspronkelijk geëxtraheerd uit de Amethyst Android-client, biedt Quartz herbruikbare Nostr-protocolimplementaties voor JVM-, Android-, iOS- en Linux-platformen.

## Hoe Het Werkt

Quartz biedt Nostr-kernfunctionaliteit als een gedeelde bibliotheek:

- **Event-afhandeling**: Parsing, validatie en creatie van Nostr-events
- **Cryptografie**: Secp256k1-ondertekening, NIP-44-encryptie, sleutelbeheer
- **Relay-communicatie**: Verbindingsbeheer, berichtvolgorde, abonnementafhandeling
- **NIP-ondersteuning**: Implementatie van gangbare NIPs inclusief NIP-06, NIP-19, NIP-44 en meer

## Belangrijkste Kenmerken

- **Kotlin Multiplatform**: Eén codebase compileert naar meerdere doelen
- **Doelplatformen**: Android, JVM, iOS (ARM64, Simulator), Linux
- **Prestatie-geoptimaliseerd**: Efficiënte eventverwerking en cryptografische operaties
- **Blossom-integratie**: Ondersteuning voor media-uploads via het Blossom-protocol
- **OpenTimestamp**: Volledige Kotlin-port voor tijdstempelverificatie

## Architectuur

De bibliotheek gebruikt een modulaire source set-structuur:
- `commonMain`: Gedeelde code voor alle platformen
- `jvmAndroid`: Code gedeeld tussen JVM en Android
- `androidMain`: Android-specifieke implementaties
- `jvmMain`: Desktop JVM-implementaties
- `iosMain`: iOS-specifieke implementaties

## OpenSats-subsidie

In december 2025 kondigde OpenSats financiering aan voor Quartz als onderdeel van hun veertiende golf van Nostr-subsidies. De subsidie ondersteunt voortgezette ontwikkeling om Amethyst op iOS mogelijk te maken via dezelfde Kotlin Multiplatform-aanpak die al de Android- en desktopversies aandrijft.

---

**Primaire bronnen:**
- [Quartz op Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Amethyst Repository](https://github.com/vitorpamplona/amethyst)

**Genoemd in:**
- [Newsletter #3: December Terugblik](/nl/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3: Nieuws](/nl/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3: Belangrijke Amethyst-wijzigingen](/nl/newsletters/2025-12-31-newsletter/#amethyst-android)

**Zie ook:**
- [Blossom Protocol](/nl/topics/blossom/)
