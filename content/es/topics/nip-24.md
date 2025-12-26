---
title: "NIP-24: Campos de Metadatos Extra"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
---

NIP-24 define campos opcionales adicionales para metadatos de usuario kind 0 más allá del nombre básico, descripción e imagen.

## Campos de Metadatos Extra

- **display_name**: Un nombre alternativo, más grande con caracteres más ricos que `name`
- **website**: Una URL web relacionada con el autor del evento
- **banner**: URL a una imagen ancha (~1024x768) para visualización de fondo opcional
- **bot**: Booleano que indica que el contenido es total o parcialmente automatizado
- **birthday**: Objeto con campos opcionales de año, mes y día

## Etiquetas Estándar

NIP-24 también estandariza etiquetas de propósito general:
- `r`: Referencia a URL web
- `i`: Identificador externo
- `title`: Nombre para varios tipos de eventos
- `t`: Hashtag (debe estar en minúsculas)

---

**Fuentes primarias:**
- [Especificación NIP-24](https://github.com/nostr-protocol/nips/blob/master/24.md)

**Mencionado en:**
- [Boletín #1: Actualizaciones de NIP](/es/newsletters/2025-12-17-newsletter/#nip-updates)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
