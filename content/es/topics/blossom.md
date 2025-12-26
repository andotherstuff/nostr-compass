---
title: "Protocolo Blossom"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

Blossom es un protocolo de alojamiento de medios para Nostr que proporciona almacenamiento de archivos descentralizado con URLs direccionables por contenido.

## Cómo Funciona

Los archivos se almacenan en servidores Blossom y se direccionan por su hash SHA256. Esto significa:
- El mismo archivo siempre tiene la misma URL en todos los servidores
- Los archivos pueden recuperarse de cualquier servidor que los tenga
- Los clientes pueden verificar la integridad del archivo comprobando el hash

## Características

- Almacenamiento direccionable por contenido
- Redundancia en múltiples servidores
- Descubrimiento de autor vía BUD-03
- Esquema URI personalizado vía BUD-10
- Paginación basada en cursor en el endpoint `/list`

---

**Fuentes primarias:**
- [Repositorio de Blossom](https://github.com/hzrd149/blossom)

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)
- [Boletín #2: Cambios Notables de Código](/es/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)

**Ver también:**
- [BUD-03: Lista de Servidores del Usuario](/es/topics/bud-03/)
- [BUD-10: Esquema URI de Blossom](/es/topics/bud-10/)
