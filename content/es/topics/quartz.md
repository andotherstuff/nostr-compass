---
title: "Quartz"
date: 2025-12-31
translationOf: /en/topics/quartz.md
translationDate: 2025-12-31
draft: false
categories:
  - Biblioteca
  - Desarrollo
---

Quartz es una biblioteca Kotlin Multiplatform para Nostr desarrollada por Vitor Pamplona. Originalmente extraída del cliente Android Amethyst, Quartz proporciona implementaciones reutilizables del protocolo Nostr para plataformas JVM, Android, iOS y Linux.

## Cómo Funciona

Quartz proporciona funcionalidad central de Nostr como una biblioteca compartida:

- **Manejo de Eventos**: Análisis, validación y creación de eventos Nostr
- **Criptografía**: Firma Secp256k1, cifrado NIP-44, gestión de claves
- **Comunicación con Relays**: Gestión de conexiones, ordenamiento de mensajes, manejo de suscripciones
- **Soporte de NIPs**: Implementación de NIPs comunes incluyendo NIP-06, NIP-19, NIP-44, y más

## Características Principales

- **Kotlin Multiplatform**: Una única base de código compila para múltiples objetivos
- **Plataformas Objetivo**: Android, JVM, iOS (ARM64, Simulador), Linux
- **Optimizado para Rendimiento**: Procesamiento eficiente de eventos y operaciones criptográficas
- **Integración con Blossom**: Soporte para subida de medios mediante el protocolo Blossom
- **OpenTimestamp**: Port completo en Kotlin para verificación de marcas de tiempo

## Arquitectura

La biblioteca usa una estructura modular de conjuntos de fuentes:
- `commonMain`: Código compartido para todas las plataformas
- `jvmAndroid`: Código compartido entre JVM y Android
- `androidMain`: Implementaciones específicas de Android
- `jvmMain`: Implementaciones JVM de escritorio
- `iosMain`: Implementaciones específicas de iOS

## Subvención de OpenSats

En diciembre de 2025, OpenSats anunció financiación para Quartz como parte de su decimocuarta ola de subvenciones Nostr. La subvención apoya el desarrollo continuo para habilitar Amethyst en iOS mediante el mismo enfoque Kotlin Multiplatform que ya impulsa las versiones de Android y escritorio.

---

**Fuentes principales:**
- [Quartz en Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Repositorio de Amethyst](https://github.com/vitorpamplona/amethyst)

**Mencionado en:**
- [Newsletter #3: Resumen de Diciembre](/es/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3: Noticias](/es/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3: Cambios Notables de Amethyst](/es/newsletters/2025-12-31-newsletter/#amethyst-android)

**Ver también:**
- [Protocolo Blossom](/es/topics/blossom/)
