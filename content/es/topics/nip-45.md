---
title: "NIP-45: Conteo de Eventos"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45 define cómo pedir a relays que cuenten eventos que coincidan con un filtro sin transferir los eventos en sí. El cliente envía un mensaje COUNT con la misma sintaxis de filtro que REQ, y el relay responde con un conteo.

## Cómo Funciona

El cliente envía una solicitud COUNT con un ID de suscripción y filtro:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

El relay responde con el conteo:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

Esto evita descargar cientos o miles de eventos solo para mostrar un número.

## Conteo Aproximado HyperLogLog

A febrero de 2026, NIP-45 soporta conteo aproximado HyperLogLog (HLL) ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). Junto a las respuestas COUNT, el relay puede retornar valores de registro HLL de 256 bytes:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

HLL resuelve un problema fundamental en el conteo de eventos distintos a través de múltiples relays. Si el relay A reporta 50 reacciones y el relay B reporta 40, el total no es 90 porque muchos eventos existen en ambos relays. Al tomar el valor máximo en cada posición de registro, la fusión de registros HLL de múltiples relays deduplica automáticamente a través de la red.

Con 256 registros, el error estándar es aproximadamente 5.2%. Correcciones HyperLogLog++ mejoran la precisión para cardinalidades pequeñas menores a ~200 eventos. Incluso dos eventos de reacción consumen más ancho de banda que el payload HLL de 256 bytes, haciendo esto eficiente para cualquier conteo por encima de números triviales.

La spec fija la cantidad de registros en 256 para interoperabilidad entre todas las implementaciones de relay.

## Casos de Uso

Métricas sociales (conteos de seguidores, reacciones, reposts) son la aplicación principal. Sin HLL, el cliente debe consultar un único relay "de confianza" para obtener conteos (centralizando los datos) o descargar todos los eventos de todos los relays para deduplicar localmente (desperdiciando ancho de banda). HLL proporciona conteos aproximados entre relays con 256 bytes de overhead por relay.

---

**Fuentes principales:**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)

**Mencionado en:**
- [Newsletter #9: Análisis Profundo de NIP](/es/newsletters/2026-02-11-newsletter/#análisis-profundo-de-nip-nip-45-conteo-de-eventos-y-hyperloglog)
- [Newsletter #9: Actualizaciones de NIPs](/es/newsletters/2026-02-11-newsletter/#actualizaciones-de-nips)

**Ver también:**
- [NIP-11: Documento de Información de Relay](/es/topics/nip-11/)
