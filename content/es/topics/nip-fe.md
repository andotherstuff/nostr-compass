---
title: "Propuesta NIP-FE: comandos de relay por HTTP"
date: 2026-09-30
draft: false
categories:
  - Project Proposals
  - Relays
translationOf: /en/topics/nip-fe.md
translationDate: 2026-10-01
---

Amethyst utiliza la etiqueta provisional NIP-FE para los comandos de relay por HTTP en su trabajo con el relay Geode y el cliente Quartz. La etiqueta no es un NIP asignado ni una prueba de adopción entre los relays de Nostr.

## Transporte

En lugar de abrir una conexión WebSocket, un cliente envía mediante POST una trama `REQ`, `COUNT` o `EVENT` a un endpoint HTTP del relay. La respuesta transmite tramas del relay como JSON delimitado por saltos de línea. Un cliente debe distinguir una respuesta completa de un flujo interrumpido, y una solicitud autenticada sigue utilizando la autorización HTTP firmada de Nostr. El transporte cambia la forma en que los comandos llegan a un relay; no cambia la firma subyacente del event ni su contenido.

La [implementación integrada](https://github.com/vitorpamplona/amethyst/pull/4231) de Amethyst añade la ruta de Geode, compatibilidad con el cliente Quartz, límites de tamaño del cuerpo y de concurrencia, y pruebas del formato de las tramas y de la autorización. Constituye evidencia de implementación a nivel de código fuente, no una prueba de que relays independientes hayan implementado la misma propuesta.

## Colisión de nombres

Un [pull request en borrador en el repositorio de NIPs](https://github.com/nostr-protocol/nips/pull/2488), sin relación con lo anterior, también utiliza **NIP-FE**, esta vez para feeds privados basados en un sobre propuesto para múltiples destinatarios. Ese trabajo sigue abierto y describe un problema distinto del transporte HTTP de Amethyst. Ninguno de los dos usos provisionales establece que la etiqueta se haya asignado a una especificación aceptada; los lectores deben identificar la propuesta por su fuente y su tema.

---

**Fuentes primarias:**
- [PR de implementación de Geode y Quartz en Amethyst](https://github.com/vitorpamplona/amethyst/pull/4231)
- [Repositorio de Amethyst](https://github.com/vitorpamplona/amethyst)
- [Borrador abierto sobre feeds privados que también utiliza NIP-FE](https://github.com/nostr-protocol/nips/pull/2488)

**Mencionado en:**
- [Boletín #42: comandos de relay de Amethyst](/es/newsletters/2026-09-30-newsletter/#amethyst-repairs-encrypted-group-interoperability)
