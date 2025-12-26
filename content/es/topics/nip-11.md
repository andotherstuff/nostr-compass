---
title: "NIP-11: Información del Relay"
date: 2025-12-17
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11 define cómo los relays exponen metadatos sobre sí mismos, incluyendo NIPs soportados, limitaciones e información de contacto.

## Cómo Funciona

Los clientes obtienen la información del relay haciendo una solicitud HTTP GET a la URL WebSocket del relay con un encabezado `Accept: application/nostr+json`. El relay devuelve un documento JSON describiendo sus capacidades.

## Campos Clave

- **name** - Nombre del relay legible para humanos
- **description** - Para qué es el relay
- **supported_nips** - Lista de NIPs implementados
- **limitation** - Restricciones como tamaño máximo de mensaje, autenticación requerida, etc.
- **self** - La clave pública propia del relay (nuevo campo para identidad del relay)

## Casos de Uso

- Los clientes pueden verificar si un relay soporta las características requeridas antes de conectarse
- Los servicios de descubrimiento pueden indexar las capacidades de los relays
- Los usuarios pueden ver las políticas del relay antes de publicar

---

**Fuentes primarias:**
- [Especificación NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md)

**Mencionado en:**
- [Boletín #1: Actualizaciones de NIP](/es/newsletters/2025-12-17-newsletter/#nip-updates)
