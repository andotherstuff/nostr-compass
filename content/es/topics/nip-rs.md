---
title: 'Borrador de NIP-RS de Buzz: sincronización del estado de lectura entre dispositivos'
date: 2026-10-28
translationOf: /en/topics/nip-rs.md
translationDate: 2026-10-28
draft: false
---

**Estado:** se trata de una propuesta en borrador específica del proyecto Buzz. NIP-RS no es un NIP oficial aceptado. La etiqueta procede de la documentación del proyecto Buzz, y el repositorio oficial de NIPs no la ha asignado ni aprobado.

## Propósito

NIP-RS permite que los dispositivos de un mismo usuario compartan hasta dónde ha leído ese usuario. Cada instalación publica un event direccionable `kind:30078`. Su tag `d` es `read-state:` seguido de un ID de ranura aleatorio, y su contenido está cifrado con NIP-44 para la propia clave del usuario. En el texto plano, los IDs de contexto se asignan a fronteras de marca de tiempo, cada una de las cuales indica que se ha leído todo lo ocurrido en ese momento o antes. El borrador no publica confirmaciones de lectura ni revela lo que han leído otras personas.

## Límites

Las fronteras son indicaciones de mejor esfuerzo sobre la actividad reciente. No forman un historial completo de mensajes leídos. Las anulaciones de marcado manual como no leído, incluidos los suelos de lápida, siguen un contrato duradero independiente. La carga del estado completo de anulaciones depende del orden de los relays y de un comportamiento de capacidad que un cliente no puede verificar del todo, por lo que un relay arbitrario podría no devolver el estado completo de no leídos. En su mayoría, los IDs de contexto solo tienen significado dentro de una misma familia de clientes.

Una pull request abierta, la #8639, propone trasladar los clientes de Buzz a una capacidad NIP-11 `buzz_v1` respaldada por una API HTTP privada y autenticada, desactivada por defecto. Los relays sin esa capacidad seguirían usando NIP-RS.

## Fuentes primarias

- [Borrador de NIP-RS de Buzz: sincronización del estado de lectura entre dispositivos (revisión fijada)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-RS.md)
- [Pull request #8639 de Buzz: estado de lectura mediante una capacidad del relay (abierta)](https://github.com/block/buzz/pull/8639)

## Véase también

- [NIP-44](/es/topics/nip-44/)
- [NIP-78](/es/topics/nip-78/)

**Mencionado en:**

- [Boletín n.º 46: Buzz](/es/newsletters/2026-10-28-newsletter/#buzz)
