---
title: "NIP-54: Wiki"
date: 2025-12-31
translationOf: /en/topics/nip-54.md
translationDate: 2025-12-31
draft: false
categories:
  - Protocolo
  - Contenido
---

NIP-54 define kind 30818 como un tipo de evento direccionable para crear artículos wiki y entradas de enciclopedia en Nostr. Permite la creación de contenido colaborativo y descentralizado donde múltiples autores pueden escribir sobre los mismos temas.

## Cómo Funciona

Los artículos wiki se identifican mediante un `d` tag normalizado (el tema del artículo). Múltiples personas pueden escribir artículos sobre el mismo tema, creando una base de conocimientos descentralizada sin autoridad central.

**Normalización del D Tag:**
- Convertir todas las letras a minúsculas
- Convertir espacios en guiones
- Eliminar puntuación y símbolos
- Preservar caracteres no ASCII y números

## Formato del Contenido

Los artículos utilizan el marcado Asciidoc con dos características especiales:

- **Wikilinks** (`[[página destino]]`) - Enlaces a otros artículos wiki en Nostr
- **Enlaces Nostr** - Referencias a perfiles o eventos según NIP-21

## Selección de Artículos

Cuando existen múltiples versiones de un artículo, los clientes priorizan basándose en:

1. Reacciones (NIP-25) indicando aprobación de la comunidad
2. Listas de relays (NIP-51) para clasificación de fuentes
3. Listas de contactos (NIP-02) formando redes de recomendación

## Características Colaborativas

- **Bifurcación** - Crear versiones derivadas de artículos
- **Solicitudes de fusión** (kind 818) - Proponer cambios a artículos existentes
- **Redirecciones** (kind 30819) - Apuntar temas antiguos a nuevos
- **Marcadores de deferencia** - Indicar versiones preferidas de artículos

---

**Fuentes primarias:**
- [Especificación NIP-54](https://github.com/nostr-protocol/nips/blob/master/54.md)

**Mencionado en:**
- [Boletín #3: Actualizaciones de NIP](/es/newsletters/2025-12-31-newsletter/#nip-updates)

**Ver también:**
- [NIP-51: Listas](/es/topics/nip-51/)
- [NIP-02: Lista de Seguidos](/es/topics/nip-02/)
