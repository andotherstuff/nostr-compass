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

Quartz es una biblioteca Kotlin Multiplatform para Nostr desarrollada por Vitor Pamplona. Es la capa de protocolo y datos compartida detrás del impulso de Amethyst hacia Android, escritorio y eventualmente iOS desde una sola base de código.

## Cómo funciona

Quartz proporciona funcionalidad central de Nostr como una biblioteca compartida:

- **Manejo de eventos**: Análisis, validación y creación de eventos Nostr
- **Criptografía**: Firma Secp256k1, cifrado NIP-44, gestión de claves
- **Comunicación con relays**: Gestión de conexiones, ordenamiento de mensajes, manejo de suscripciones
- **Soporte de NIPs**: Implementación de NIPs comunes incluyendo NIP-06, NIP-19, NIP-44 y más

## Por qué importa

Quartz mueve la lógica pesada de protocolo fuera de una sola aplicación y la coloca en una biblioteca reutilizable. Eso importa porque el manejo de relays, análisis de eventos, cifrado y reglas de almacenamiento se vuelven más fáciles de compartir entre clientes en lugar de reimplementarse por plataforma.

El resultado concreto ya se mostró en el trabajo de escritorio de Amethyst. La refactorización respaldada por la subvención movió código compartido a módulos Kotlin Multiplatform como `commonMain`, `jvmAndroid` y `jvmMain`, haciendo del soporte de escritorio un problema de biblioteca y módulos en lugar de una reescritura completa.

## Arquitectura

La biblioteca usa una estructura modular de conjuntos de fuentes:
- `commonMain`: Código compartido para todas las plataformas
- `jvmAndroid`: Código compartido entre JVM y Android
- `androidMain`: Implementaciones específicas de Android
- `jvmMain`: Implementaciones JVM de escritorio
- `iosMain`: Implementaciones específicas de iOS

## Estado actual

En diciembre de 2025, OpenSats anunció financiación para Quartz en su decimocuarta ola de subvenciones Nostr. El repositorio existe como una biblioteca independiente, pero gran parte del progreso visible hasta ahora ha llegado a través de PRs de Amethyst que convierten módulos de la aplicación en código multiplataforma y rastrean la paridad de características entre objetivos.

---

**Fuentes primarias:**
- [Repositorio de Quartz](https://github.com/vitorpamplona/quartz)
- [Quartz en Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Repositorio de Amethyst](https://github.com/vitorpamplona/amethyst)
- [Decimocuarta ola de subvenciones Nostr de OpenSats](https://opensats.org/blog/fourteenth-wave-of-nostr-grants)

**Mencionado en:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3: News](/en/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3: Amethyst Notable Changes](/en/newsletters/2025-12-31-newsletter/#amethyst-android)

**Ver también:**
- [Blossom Protocol](/es/topics/blossom/)
