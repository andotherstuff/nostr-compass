---
title: 'Borrador de NIP-OA de Buzz: atestación del propietario'
date: 2026-10-28
translationOf: /en/topics/nip-oa.md
translationDate: 2026-10-28
draft: false
---

**Estado:** se trata de una propuesta en borrador específica del proyecto Buzz. NIP-OA no es un NIP oficial aceptado. La etiqueta procede de la documentación del proyecto Buzz, y el repositorio oficial de NIPs no la ha asignado ni aprobado.

## Propósito

NIP-OA define un tag opcional `auth` que permite a una clave de propietario autorizar a una clave de agente a publicar events. La autora del event sigue siendo la clave del agente. Un tag válido solo cuenta como prueba de autorización y no permite al agente suplantar al propietario.

## Mecanismo

Con una firma Schnorr, el propietario firma un hash con separación de dominio que vincula la pubkey del agente a una cadena de condiciones exacta. Las condiciones pueden exigir un kind de event y fijar límites sobre el `created_at` autodeclarado. El agente puede reutilizar el tag en sus events siempre que cada uno cumpla las condiciones. Los verificadores validan primero el event base y después comprueban la firma del propietario y cada una de las condiciones.

## Límites

Una cadena de condiciones vacía no añade restricciones. Las cláusulas de marca de tiempo restringen un campo que controla el agente, así que no proporcionan una caducidad basada en el tiempo real. Quien necesite frescura tiene que comprobarla por separado. Publicar el tag de forma pública vincula las claves del propietario y del agente.

## Fuentes primarias

- [Borrador de NIP-OA de Buzz: atestación del propietario (revisión fijada)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-OA.md)

## Véase también

- [NIP-01](/es/topics/nip-01/)

**Mencionado en:**

- [Boletín n.º 46: Buzz](/es/newsletters/2026-10-28-newsletter/#buzz)
