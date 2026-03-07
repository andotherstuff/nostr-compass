---
title: "NIP-24: Campos de Metadatos Extra"
date: 2025-12-17
translationOf: /en/topics/nip-24.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Identity
---

NIP-24 define campos opcionales adicionales para metadatos de usuario kind 0, más allá del nombre básico, descripción e imagen.

## Campos de Metadatos Extra

- **display_name**: Un nombre alternativo, más grande, con caracteres más ricos que `name`
- **website**: Una URL web relacionada con el autor del evento
- **banner**: URL de una imagen ancha (~1024x768) para visualización de fondo opcional
- **bot**: Booleano que indica que el contenido es total o parcialmente automatizado
- **birthday**: Objeto con campos opcionales de año, mes y día

La especificación también marca dos campos antiguos como obsoletos: `displayName` debería convertirse en `display_name`, y `username` en `name`. Los clientes aún ven estos en la práctica, así que un parser tolerante ayuda con la compatibilidad hacia atrás aunque un escritor no debería emitirlos.

## Tags Estándar

NIP-24 también estandariza tags de propósito general:
- `r`: Referencia a URL web
- `i`: Identificador externo
- `title`: Nombre para varios tipos de eventos
- `t`: Hashtag (debe estar en minúsculas)

## Por Qué Importa

NIP-24 trata sobre convergencia. Estos campos y tags ya aparecían en distintos clientes, así que la especificación les da nombres y significados consistentes. Eso reduce pequeñas pero molestas incompatibilidades, como clientes en desacuerdo sobre si un banner vive bajo `banner` o bajo alguna clave específica de la aplicación.

Un punto práctico para implementadores es que kind 0 sigue siendo una ruta caliente en la mayoría de los clientes. Los metadatos extra deben mantenerse ligeros. Si un campo necesita su propio patrón de obtención o ciclo de actualización independiente, probablemente pertenezca a un kind de evento separado en lugar de inflar los metadatos de perfil.

---

**Fuentes primarias:**
- [Especificación NIP-24](https://github.com/nostr-protocol/nips/blob/master/24.md)

**Mencionado en:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
