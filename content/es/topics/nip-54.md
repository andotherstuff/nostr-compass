---
title: "NIP-54: Wiki"
date: 2025-12-31
translationOf: /en/topics/nip-54.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Content
---

NIP-54 define kind `30818` para artículos estilo wiki en Nostr. Múltiples autores pueden publicar entradas para el mismo tema, así que los clientes necesitan heurísticas de clasificación y confianza en lugar de una sola página canónica.

## Cómo funciona

Los artículos wiki se identifican por una etiqueta `d` normalizada que representa el tema. Múltiples personas pueden publicar entradas con el mismo tema normalizado, creando una wiki abierta sin un editor central.

**Normalización de la etiqueta D:**
- Convertir a minúsculas las letras que tienen variantes de caso
- Convertir espacios en blanco a guiones
- Eliminar puntuación y símbolos
- Colapsar guiones repetidos y recortar guiones iniciales o finales
- Preservar letras no ASCII y números

Esa regla de normalización importa para la interoperabilidad. Si dos clientes normalizan el mismo título de manera diferente, consultarán temas distintos y fragmentarán el conjunto de artículos.

## Formato del contenido

La especificación fusionada usa marcado Asciidoc con dos características extra:

- **Wikilinks** (`[[página destino]]`) - Enlaces a otros artículos wiki a través de Nostr
- **Enlaces Nostr** - Referencias a perfiles o eventos según NIP-21

Se ha propuesto un cambio a Djot, pero no ha reemplazado a Asciidoc en el NIP canónico a marzo de 2026.

## Selección de artículos

Cuando existen múltiples versiones de un artículo, los clientes pueden priorizar basándose en:

1. Reacciones (NIP-25) indicando aprobación de la comunidad
2. Listas de relays (NIP-51) para clasificación de fuentes
3. Listas de contactos (NIP-02) formando redes de recomendación

En la práctica, esto significa que NIP-54 no es solo un formato de contenido. También es un problema de política del cliente. Dos clientes pueden mostrar diferentes artículos "mejores" para el mismo tema mientras ambos permanecen conformes con la especificación.

## Características colaborativas

- **Bifurcación** - Crear versiones derivadas de artículos
- **Solicitudes de fusión** (kind 818) - Proponer cambios a artículos existentes
- **Redirecciones** (kind 30819) - Apuntar temas antiguos a nuevos
- **Marcadores de deferencia** - Indicar versiones preferidas de artículos

Las bifurcaciones y los marcadores de deferencia permiten a los autores reconocer mejores versiones sin eliminar su propio trabajo. Eso importa en una red donde las revisiones antiguas pueden permanecer disponibles a través de muchos relays.

---

**Fuentes primarias:**
- [Especificación NIP-54](https://github.com/nostr-protocol/nips/blob/master/54.md)
- [PR #2177: Normalización internacionalizada de d-tag](https://github.com/nostr-protocol/nips/pull/2177)

**Mencionado en:**
- [Boletín #3: Actualizaciones de NIP](/en/newsletters/2025-12-31-newsletter/#nip-updates)
- [Boletín #15: PRs abiertos](/en/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**Ver también:**
- [NIP-51: Listas](/es/topics/nip-51/)
- [NIP-02: Lista de seguidos](/es/topics/nip-02/)
