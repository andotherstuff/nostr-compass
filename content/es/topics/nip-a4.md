---
title: "NIP-A4: Mensajes Públicos"
date: 2025-12-24
translationOf: /en/topics/nip-a4.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---

NIP-A4 define mensajes públicos (kind 24) diseñados para pantallas de notificaciones, con amplio soporte de clientes como objetivo.

## Cómo funciona

Kind `24` es un mensaje de texto plano firmado dirigido a uno o más destinatarios. El cuerpo del mensaje vive en `content`, y las etiquetas `p` identifican a los receptores previstos. La especificación dice que los clientes deberían enviar estos eventos a los relays inbox de [NIP-65](/es/topics/nip-65/) de los destinatarios y al relay outbox del remitente.

A diferencia de las conversaciones hiladas, estos mensajes no tienen concepto de historial de chat, estado de sala ni raíces de hilo. Están destinados a aparecer en una superficie de notificación y ser comprensibles por sí mismos.

## Reglas del protocolo

- Usa etiquetas `p` para identificar destinatarios
- No debe usar etiquetas `e` para threading
- Puede usar etiquetas `q` para citar otro evento
- Funciona mejor con etiquetas de expiración [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md) para que los mensajes estilo notificación obsoletos desaparezcan con el tiempo

## Por qué existe

NIP-A4 da a los clientes una primitiva de mensaje público más simple que una nota hilada completa. Eso es útil para mensajes estilo mención, saludos ligeros, o notificaciones puntuales donde construir un árbol de conversación permanente añadiría más complejidad que valor.

La contrapartida es que estos mensajes son públicos. Son fáciles de mostrar en una interfaz de notificaciones precisamente porque no crean estado de sesión privado. Cualquiera puede leerlos y responderlos si los ve.

## Notas de interoperabilidad

NIP-A4 es fácil de confundir con protocolos de mensajes directos porque apunta a destinatarios nombrados, pero sigue siendo un kind de evento público. Los clientes no deberían presentar kind `24` como mensajería privada ni asumir ninguna confidencialidad más allá de la ubicación en el relay.

---

**Fuentes primarias:**
- [Especificación NIP-A4](https://github.com/nostr-protocol/nips/blob/master/A4.md)
- [PR de NIP-A4](https://github.com/nostr-protocol/nips/pull/1988)

**Mencionado en:**
- [Newsletter #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Ver también:**
- [NIP-01: Basic Protocol](/es/topics/nip-01/)
- [NIP-10: Text Note Threading](/es/topics/nip-10/)
