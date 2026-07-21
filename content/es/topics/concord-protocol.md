---
title: "Concord Protocol"
date: 2026-07-15
draft: false
translationOf: /en/topics/concord-protocol.md
translationDate: 2026-07-15
categories:
  - Protocol
  - Messaging
---

Concord es un protocolo abierto con licencia MIT para comunidades y canales cifrados de extremo a extremo sobre Nostr, definido por las [especificaciones CORD-01 a CORD-07](https://github.com/concord-protocol/concord). [Vector](https://github.com/VectorPrivacy/Vector) lo adoptó como transporte predeterminado para su función de Chats Grupales a partir de v0.4.0, llamándolo "nuestro protocolo de mensajería personalizado" en sus propias notas de lanzamiento, pero la especificación se publica por separado de Vector y ya tiene implementaciones independientes.

## Cómo funciona

Concord divide lo que un servidor de comunidad estilo Discord normalmente hace en piezas que no necesitan confiar en nadie: los relay solo almacenan blobs cifrados dirigidos a etiquetas rotativas, poseer la clave de una sala es lo que convierte a alguien en miembro, y la autoridad sobre roles, expulsiones y baneos es un registro firmado enraizado en la identidad del propietario que cada cliente verifica localmente en lugar de confiar en un servidor para aplicarlo. Cada evento durable viaja en el mismo sobre de tres capas: un envoltorio kind 1059 firmado por la clave de flujo derivada del plano, conteniendo un sello firmado por la clave real del autor, conteniendo un rumor sin firma que lleva el evento funcional. Un rumor de mensaje de chat es un evento kind 9 simple:

```json
{
  "kind": 9,
  "pubkey": "<author>",
  "content": "Hey chat!",
  "tags": [
    ["channel", "<channel_id>"],
    ["epoch", "0"]
  ]
}
```

El tráfico de control, chat e invitados cada uno obtiene su propio plano envuelto con gift-wrap [NIP-59](/es/topics/nip-59/), de modo que un relay que alberga los tres todavía no puede distinguir un mensaje de control de un mensaje de chat de una entrada de invitados sin la clave de la sala. La especificación se divide en siete documentos CORD: flujos privados (01), comunidades y membresía (02), canales (03), roles (04), invitaciones (05), re-cifrado y refundación para cortar acceso a miembros eliminados (06), y audio/video via un intermediario de tokens ciegos (07). La membresía en sí no tiene lista del lado del servidor: quien pueda descifrar el plano es un miembro, y eliminar a alguien de verdad significa rotar la comunidad a una nueva época de clave y entregarla solo a quienes quedan, en lugar de borrar una fila de una tabla.

## Diferencias con Marmot

Concord y [Marmot](/es/topics/marmot/) resuelven la mensajería grupal cifrada sobre Nostr con diferente criptografía para diferentes formas de grupo, y la propia comparación del proyecto Concord es explícita sobre la división: Marmot superpone [MLS](/es/topics/mls/) sobre Nostr para secreto hacia adelante y seguridad post-compromiso, usando paquetes de claves por dispositivo y commits ordenados que avanzan todo el grupo al unísono. Eso compra garantías fuertes, a un costo que escala con los cambios de membresía, bien adaptado a grupos pequeños y de alto riesgo donde las entradas y salidas son raras. Concord en cambio da a cada miembro la misma clave de sala y re-cifra toda la sala al eliminar en lugar de avanzar por commit, intercambiando algunas de las garantías criptográficas de MLS por un modelo que se mantiene económico a medida que una comunidad crece a cientos o miles de miembros casuales y de alta rotación, la forma que las comunidades estilo Discord realmente toman.

## Por qué Vector cambió

Las propias [notas de lanzamiento de Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) describen Concord solo como "nuestro protocolo de mensajería personalizado" para Chats Grupales, sin exponer el razonamiento directamente. El ajuste con la justificación publicada de Concord es claro de todos modos: los Chats Grupales en un cliente como Vector son exactamente el caso de membresía grande, abierta y cambiante donde el estado MLS por dispositivo de Marmot se convierte en la ruta más costosa, y el diseño asíncrono y plegable de Concord está construido para ese caso. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) retiró Marmot para Chats Grupales a favor de Concord, y el historial existente de grupos Marmot no se transfirió en el cambio. [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) lanzó "Concord v2" cuatro días después con mejoras de privacidad y estabilidad. Dentro de la misma semana, [Amethyst fusionó su propia implementación limpia y compatible a nivel de protocolo](https://github.com/vitorpamplona/amethyst/pull/3566), y el cliente estilo Discord de Soapbox, [Armada](https://gitlab.com/soapbox-pub/armada), ya construye su función de Comunidades sobre la misma especificación como implementación de referencia. Tres clientes independientes convergiendo en una especificación abierta en días es un camino rápido hacia interoperabilidad real entre clientes, vale la pena rastrear frente a cuántos del resto de los clientes de chat grupal de Nostr se mantienen en Marmot.

## Implementaciones

- [Vector](https://github.com/VectorPrivacy/Vector) - mensajero Nostr de binario único enfocado en privacidad; primer cliente Concord en producción, en v0.4.0
- [Armada](https://gitlab.com/soapbox-pub/armada) (Soapbox) - cliente de comunidad estilo Discord; implementación de referencia, backend en el repositorio separado `armada-relay`
- [Amethyst](https://github.com/vitorpamplona/amethyst) - cliente Nostr rico en funciones para Android y multiplataforma; reimplementación de sala limpia compatible a nivel de protocolo con Armada ([PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566))

---

**Fuentes primarias:**
- [Especificaciones del protocolo Concord (CORD-01 a CORD-07)](https://github.com/concord-protocol/concord)
- [Notas de lanzamiento de Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)
- [Notas de lanzamiento de Vector v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1)
- [Amethyst PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566)

**Mencionado en:**
- [Newsletter #31: Vector v0.4.0 mueve los Chats Grupales de Marmot a Concord, y Amethyst lanza su propio cliente Concord días después](/es/newsletters/2026-07-15-newsletter/#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later)
- [Newsletter #31: Amethyst lanza una implementación limpia de Concord para comunidades cifradas de extremo a extremo](/es/newsletters/2026-07-15-newsletter/#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities)

**Ver también:**
- [Marmot Protocol](/es/topics/marmot/)
- [MLS (Message Layer Security)](/es/topics/mls/)
- [NIP-46: Nostr Connect](/es/topics/nip-46/)
