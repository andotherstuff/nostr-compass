---
title: "NIP-77: Reconciliación Negentropy"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-77.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Sync
---

NIP-77 define cómo los relays y clientes de Nostr utilizan el protocolo de reconciliación de conjuntos [Negentropy](/es/topics/negentropy/) para sincronizar eficientemente conjuntos de eventos, encontrando qué eventos faltan en cada lado sin reenviar el conjunto de datos completo.

## Cómo funciona

La reconciliación Negentropy se ejecuta sobre una conexión WebSocket usando un tipo de mensaje dedicado. El cliente y el relay intercambian huellas digitales de rango compactas sobre sus conjuntos de eventos ordenados, convergiendo solo en los rangos que difieren. Una vez identificadas las diferencias, solo se transfieren los IDs de eventos faltantes (y luego los eventos faltantes en sí).

NIP-77 estandariza el encuadre de mensajes para que cualquier cliente y relay que implemente la especificación pueda negociar una sesión de sincronización eficiente. El protocolo utiliza los tipos de mensaje `NEG-OPEN`, `NEG-MSG` y `NEG-CLOSE` sobre la conexión WebSocket existente de Nostr.

## Por qué es importante

La sincronización tradicional de Nostr usa filtros `since` basados en marcas de tiempo, que pueden perder eventos debido a la deriva del reloj, eventos con marcas de tiempo idénticas, o eventos que llegan fuera de orden. Negentropy compara conjuntos de eventos reales en lugar de depender de marcas de tiempo, proporcionando una sincronización completa y demostrable en significativamente menos viajes de ida y vuelta que el sondeo simple.

Esto es especialmente útil para:
- Clientes móviles que se ponen al día después de estar sin conexión
- Replicación de relay a relay
- Sincronización de relay local (como en el agregador de relay de Citrine)

## Implementaciones

- [Citrine](https://github.com/greenart7c3/Citrine) — [PR #139](https://github.com/greenart7c3/Citrine/pull/139) añadió soporte NIP-77 para sincronización eficiente de reconciliación de conjuntos en el nodo relay de Android
- [strfry](https://github.com/hoytech/strfry) — soporte Negentropy del lado del relay
- [nostr-tools](https://github.com/nbd-wtf/nostr-tools) — implementación Negentropy del lado del cliente

---

**Fuentes primarias:**
- [Especificación NIP-77](https://github.com/nostr-protocol/nips/blob/master/77.md)
- [Protocolo Negentropy](https://github.com/hoytech/negentropy)

**Mencionado en:**
- [Newsletter #22: Citrine v3.0.0-pre1](/es/newsletters/2026-05-14-newsletter/#citrine-v300-pre1-lands-built-in-tor-and-relay-aggregation)

**Ver también:**
- [Negentropy](/es/topics/negentropy/)
