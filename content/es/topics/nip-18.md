---
title: "NIP-18: Reposts"
date: 2025-12-17
draft: false
categories:
  - Social
  - Protocol
---

NIP-18 define cómo repostear eventos, similar a los retweets en otras plataformas.

## Estructura

Un repost es un evento kind 6 (para notas kind 1) o kind 16 (repost genérico) que contiene:
- Etiqueta `e` referenciando el evento reposteado
- Etiqueta `p` referenciando al autor original
- Opcionalmente, el evento original completo en el campo `content`

## Cambios Recientes

Soporte mejorado para repostear eventos reemplazables con soporte de etiqueta `a`. Esto permite que los reposts de eventos direccionables (kinds 30000-39999) los referencien por su dirección en lugar de un ID de evento específico.

---

**Fuentes primarias:**
- [Especificación NIP-18](https://github.com/nostr-protocol/nips/blob/master/18.md)

**Mencionado en:**
- [Boletín #1: Actualizaciones de NIP](/es/newsletters/2025-12-17-newsletter/#nip-updates)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
