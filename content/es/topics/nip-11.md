---
title: "NIP-11: Documento de Información del Relay"
date: 2025-12-17
translationOf: /en/topics/nip-11.md
translationDate: 2026-04-22
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11 define cómo los relays publican una descripción legible por máquina de sí mismos, incluyendo el soporte de funcionalidades declarado, límites y metadatos del operador.

## Cómo funciona

Los clientes obtienen la información del relay haciendo una solicitud HTTP GET a la URL WebSocket del relay con un encabezado `Accept: application/nostr+json`. El relay devuelve un documento JSON describiendo sus capacidades.

## Campos útiles

- **name** - Nombre del relay legible para humanos
- **description** - Para qué es el relay
- **supported_nips** - Lista de soporte de NIPs declarado
- **limitation** - Restricciones como tamaño máximo de mensaje, autenticación requerida, etc.
- **pubkey** - Clave pública del operador del relay cuando se proporciona
- **contact** - Dirección de contacto del operador

## Modelo de confianza

NIP-11 es metadatos auto-reportados. Indica lo que un relay dice sobre sí mismo, no lo que ha demostrado en tráfico real. Eso sigue siendo útil para descubrimiento y UX, pero los clientes no deben tratar `supported_nips` como verdad absoluta sin probar el comportamiento.

Esta distinción importa para la selección de relays. Un relay puede anunciar búsqueda NIP-50, requisitos de autenticación, o un límite de mensaje grande, pero la respuesta real solo aparece una vez que un cliente se conecta y ejercita esas rutas de código.

## Por qué importa

- Los clientes pueden verificar si un relay soporta las funcionalidades requeridas antes de conectarse
- Los servicios de descubrimiento pueden indexar las capacidades de los relays
- Los usuarios pueden ver las políticas del relay antes de publicar

## Dirección reciente de la especificación

La especificación se ha recortado con el tiempo. Campos opcionales más antiguos como `software`, `version`, detalles de política de privacidad y metadatos de retención fueron eliminados después de años de adopción débil. Eso hace que los documentos NIP-11 actuales sean más pequeños y realistas, pero también significa que los clientes no deben esperar metadatos de políticas detallados de los relays.

[PR #2318](https://github.com/nostr-protocol/nips/pull/2318) propone añadir un objeto opcional `access_control` al documento de información del relay, listando el modo de acceso restringido del relay (open, invite, payment, allowlist) y cualquier endpoint que un cliente pueda usar para solicitar acceso. El campo es solo orientativo, pensado para que clientes y directorios puedan filtrar relays restringidos de las listas públicas de descubrimiento y mostrar al usuario por adelantado por qué un relay rechaza escrituras.

## Implementaciones

- [nostream PR #557](https://github.com/Cameri/nostream/pull/557) lleva a nostream a paridad completa con la información de relay de NIP-11.

---

**Fuentes primarias:**
- [Especificación NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [PR #1764](https://github.com/nostr-protocol/nips/pull/1764) - actualización del campo de identidad del relay
- [PR #1946](https://github.com/nostr-protocol/nips/pull/1946) - limpieza de campos poco usados
- [PR #2231](https://github.com/nostr-protocol/nips/pull/2231) - eliminación de campos obsoletos
- [PR #2318](https://github.com/nostr-protocol/nips/pull/2318) - campo `access_control` para descubrimiento de relays restringidos
- [nostream PR #557](https://github.com/Cameri/nostream/pull/557) - paridad completa con la información de relay de NIP-11

**Mencionado en:**
- [Boletín #1: Actualizaciones de NIP](/es/newsletters/2025-12-17-newsletter/)
- [Boletín #13: Actualizaciones de NIP](/en/newsletters/2026-03-11-newsletter/)
- [Boletín #19: Actualizaciones de NIP (propuesta `access_control`)](/en/newsletters/2026-04-22-newsletter/)

**Ver también:**
- [NIP-66: Descubrimiento de Relays y Monitoreo de Disponibilidad](/es/topics/nip-66/)
