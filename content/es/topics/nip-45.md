---
title: "NIP-45: Conteo de Eventos"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45 define cómo los clientes piden a relays contar eventos que coincidan con un filtro sin transferir los eventos en sí. Reutiliza la sintaxis de filtros de NIP-01, de modo que un cliente a menudo puede convertir un `REQ` existente en una solicitud `COUNT` con los mismos filtros.

## Cómo funciona

Un cliente envía una solicitud `COUNT` con un ID de suscripción y filtro:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

El relay responde con un conteo:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

Esto evita descargar cientos o miles de eventos solo para mostrar un número. Si un cliente envía múltiples filtros en una solicitud `COUNT`, el relay los agrega en un único resultado, igual que múltiples filtros `REQ` se combinan con OR.

## Conteo aproximado HyperLogLog

A febrero de 2026, NIP-45 soporta conteo aproximado HyperLogLog (HLL) ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). Los relays pueden marcar un resultado como aproximado, y para deduplicación entre relays pueden retornar 256 registros HLL junto con el conteo:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<cadena hex de 512 caracteres>"}]
```

HLL resuelve un problema fundamental: contar eventos distintos a través de múltiples relays. Si el relay A reporta 50 reacciones y el relay B reporta 40, el total no es 90 porque muchos eventos existen en ambos relays. Los clientes fusionan los valores HLL tomando el valor máximo en cada posición de registro, lo que da una estimación a nivel de red sin descargar los eventos crudos.

La especificación fija la cantidad de registros en 256 para interoperabilidad. Eso mantiene el payload pequeño y hace práctico el caché del lado del relay porque cada relay calcula el mismo diseño de registros para el mismo filtro elegible.

## Notas de interoperabilidad

HLL solo está definido para filtros con un atributo de tag, porque el offset usado para construir los registros se deriva del primer valor etiquetado en el filtro. La especificación también menciona un pequeño conjunto de consultas canónicas, incluyendo reacciones, reposts, citas, respuestas, comentarios y conteos de seguidores. Esas son las cuentas más fáciles de precalcular o cachear para los relays.

## Por qué importa

Conteos de seguidores, reacciones y respuestas son los casos de uso principales. Sin NIP-45, los clientes deben confiar en la vista local de un único relay o descargar todos los eventos coincidentes y deduplicarlos localmente. NIP-45 mantiene el conteo dentro del relay, y HLL hace prácticos los conteos entre múltiples relays sin convertir a un relay en la autoridad.

---

## Implementaciones

- [nostream](https://github.com/Cameri/nostream) añadió soporte `COUNT` en [PR #522](https://github.com/Cameri/nostream/pull/522), permitiendo a los clientes preguntar cuántos eventos coinciden con un filtro sin obtener los eventos.

---

**Fuentes primarias:**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)
- [nostream PR #522](https://github.com/Cameri/nostream/pull/522) - soporte COUNT de NIP-45

**Mencionado en:**
- [Newsletter #9: Análisis Profundo de NIP](/es/newsletters/2026-02-11-newsletter/)
- [Newsletter #9: Actualizaciones de NIPs](/es/newsletters/2026-02-11-newsletter/)
- [Newsletter #12: Cinco Años de Febreros de Nostr](/es/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: soporte NIP-45 en nostream](/en/newsletters/2026-04-22-newsletter/)

**Ver también:**
- [NIP-11: Documento de Información de Relay](/es/topics/nip-11/)
