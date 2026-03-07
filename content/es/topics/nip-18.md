---
title: "NIP-18: Reposts"
date: 2025-12-17
translationOf: /en/topics/nip-18.md
translationDate: 2026-03-07
draft: false
categories:
  - Social
  - Protocol
---

NIP-18 define cómo repostear eventos, similar a los retweets en otras plataformas.

## Cómo Funciona

Un repost es un evento kind 6 (para notas kind 1) o kind 16 (repost genérico) que contiene:
- Tag `e` referenciando el evento reposteado
- Tag `p` referenciando al autor original
- Opcionalmente, el evento original completo en el campo `content`

Kind 6 es específico para notas de texto. Kind 16 existe para que los clientes puedan repostear otros tipos de evento sin pretender que todo es una nota kind 1.

## Notas de Interoperabilidad

Soporte mejorado para repostear eventos reemplazables con soporte de tag `a`. Esto permite que los reposts de eventos direccionables (kinds 30000-39999) los referencien por su dirección en lugar de un ID de evento específico.

Esa distinción importa porque los eventos direccionables pueden actualizarse con el tiempo. Repostear por coordenada `a` permite a los clientes apuntar a la versión actual de un evento direccionable, mientras que repostear por ID de evento congela una instancia histórica específica.

## Por Qué Importa

Los reposts son más que un botón de compartir en la interfaz. Son parte de cómo el contenido se mueve a través de grafos sociales, cómo los clientes cuentan interacciones, y cómo los datos de pistas de relay se propagan por la red. Si un cliente maneja mal los tags de repost, la reconstrucción de hilos y la obtención de eventos pueden fallar de formas sutiles.

---

**Fuentes primarias:**
- [Especificación NIP-18](https://github.com/nostr-protocol/nips/blob/master/18.md)
- [PR #2132](https://github.com/nostr-protocol/nips/pull/2132) - Soporte de tag `a` para reposts genéricos

**Mencionado en:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #8: News](/en/newsletters/2026-02-04-newsletter/#news)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
- [NIP-10: Text Note Threading](/es/topics/nip-10/)
