---
title: "NIP-43: Metadatos de Acceso a Relays y Solicitudes"
date: 2026-03-18
translationOf: /en/topics/nip-43.md
translationDate: 2026-04-01
draft: false
categories:
  - Protocol
  - Relay
  - Access Control
---

NIP-43 define cómo los relays publican información de membresía y cómo los usuarios solicitan admisión, invitaciones o eliminación de relays restringidos. Le da al control de acceso de relays una superficie de eventos estándar en lugar de obligar a cada relay privado o semi-privado a inventar su propio protocolo de unión.

## Cómo Funciona

La especificación combina varios kinds de evento:

- kind `13534` publica una lista de membresía del relay
- kind `8000` anuncia que un miembro fue añadido
- kind `8001` anuncia que un miembro fue eliminado
- kind `28934` permite a un usuario enviar una solicitud de unión con un código de reclamo
- kind `28935` permite a un relay devolver un código de invitación bajo demanda
- kind `28936` permite a un usuario solicitar que su propio acceso sea revocado

El estado de membresía intencionalmente no se deriva de un solo evento. Un cliente puede necesitar consultar tanto los eventos de membresía firmados por el relay como los propios eventos del miembro antes de decidir si el acceso es vigente.

## Por Qué Importa

NIP-43 le da a los relays restringidos una forma estándar de expresar el estado de admisión y membresía. Esto importa para sistemas de grupos, comunidades solo por invitación, y relays que necesitan incorporación legible por máquinas sin recurrir a formularios web fuera de banda o flujos de trabajo manuales del operador.

La aclaración abierta en [PR #2267](https://github.com/nostr-protocol/nips/pull/2267) ajusta un punto práctico: los relays deberían mantener un estado de membresía autoritativo por pubkey. Esto ayuda a los clientes a evitar historiales de reproducción ambiguos donde un evento antiguo de adición o eliminación puede ser malinterpretado como estado actual.

## Notas de Interoperabilidad

NIP-43 depende de que el relay anuncie soporte a través de su documento [NIP-11](/es/topics/nip-11/). Las solicitudes de unión, invitación y salida solo deberían enviarse a relays que explícitamente digan que soportan este NIP.

Dado que los eventos se encuentran en espacios controlados por el relay y por el usuario al mismo tiempo, las implementaciones necesitan reglas claras de conflicto. Por eso la aclaración del estado de membresía importa más de lo que aparenta a primera vista.

---

**Fuentes primarias:**
- [Especificación NIP-43](https://github.com/nostr-protocol/nips/blob/master/43.md)
- [PR #2267](https://github.com/nostr-protocol/nips/pull/2267) - Aclarar el manejo del estado de membresía

**Mencionado en:**
- [Newsletter #14: Actualizaciones de NIPs](/es/newsletters/2026-03-18-newsletter/#actualizaciones-de-nips)

**Ver también:**
- [NIP-11: Documento de Información del Relay](/es/topics/nip-11/)
- [NIP-42: Autenticación de Clientes ante Relays](/es/topics/nip-42/)
