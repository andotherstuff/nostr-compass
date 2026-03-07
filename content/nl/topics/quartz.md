---
title: "Quartz"
date: 2025-12-31
translationOf: /en/topics/quartz.md
translationDate: 2026-03-07
draft: false
categories:
  - Bibliotheek
  - Ontwikkeling
---

Quartz is een Kotlin Multiplatform Nostr-bibliotheek, ontwikkeld door Vitor Pamplona. Het is de gedeelde protocol- en datalaag achter Amethysts beweging naar Android, desktop en uiteindelijk iOS vanuit één codebase.

## Hoe het werkt

Quartz biedt Nostr-kernfunctionaliteit als een gedeelde bibliotheek:

- **Event-afhandeling**: Parsing, validatie en creatie van Nostr-events
- **Cryptografie**: Secp256k1-signing, NIP-44-encryptie, sleutelbeheer
- **Relay-communicatie**: Verbindingsbeheer, berichtvolgorde, afhandeling van subscriptions
- **NIP-ondersteuning**: Implementatie van gangbare NIPs, waaronder NIP-06, NIP-19, NIP-44 en meer

## Waarom het belangrijk is

Quartz verplaatst protocolzware logica uit één app naar een herbruikbare bibliotheek. Dat is belangrijk omdat relay-afhandeling, event-parsing, encryptie en opslagregels dan eenvoudiger gedeeld kunnen worden tussen clients, in plaats van per platform opnieuw te worden gebouwd.

Het concrete resultaat was al zichtbaar in Amethysts desktopwerk. De door een subsidie ondersteunde refactor verplaatste gedeelde code naar Kotlin Multiplatform-modules zoals `commonMain`, `jvmAndroid` en `jvmMain`, waardoor desktopondersteuning een bibliotheek- en modulevraagstuk werd in plaats van een volledige herschrijving.

## Architectuur

De bibliotheek gebruikt een modulaire source set-structuur:

- `commonMain`: Gedeelde code voor alle platformen
- `jvmAndroid`: Code gedeeld tussen JVM en Android
- `androidMain`: Android-specifieke implementaties
- `jvmMain`: Desktop JVM-implementaties
- `iosMain`: iOS-specifieke implementaties

## Huidige status

In december 2025 kondigde OpenSats financiering aan voor Quartz in zijn veertiende lichting Nostr-subsidies. De repo bestaat als een zelfstandige bibliotheek, maar veel van de zichtbare voortgang tot nu toe is terechtgekomen in Amethyst-PR's die app-modules omzetten naar multiplatform-code en feature parity tussen targets volgen.

---

**Primaire bronnen:**
- [Quartz Repository](https://github.com/vitorpamplona/quartz)
- [Quartz op Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Amethyst Repository](https://github.com/vitorpamplona/amethyst)
- [OpenSats veertiende lichting Nostr-subsidies](https://opensats.org/blog/fourteenth-wave-of-nostr-grants)

**Genoemd in:**
- [Nieuwsbrief #3: Decemberterugblik](/en/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Nieuwsbrief #3: Nieuws](/en/newsletters/2025-12-31-newsletter/#news)
- [Nieuwsbrief #3: Opmerkelijke wijzigingen in Amethyst](/en/newsletters/2025-12-31-newsletter/#amethyst-android)

**Zie ook:**
- [Blossom Protocol](/nl/topics/blossom/)
