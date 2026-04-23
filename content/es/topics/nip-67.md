---
title: "NIP-67: Indicio de completitud de EOSE"
date: 2026-04-22
translationOf: /en/topics/nip-67.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-67 es una propuesta abierta que amplía el mensaje `EOSE` existente en [NIP-01](/es/topics/nip-01/) con un tercer elemento opcional que indica si el relay ha entregado todos los eventos almacenados que coinciden con el filtro. Su objetivo es reemplazar la heurística poco fiable que usan hoy los clientes para decidir si una suscripción se agotó o fue recortada por un límite del relay.

## El problema

`EOSE` marca la frontera entre eventos almacenados y eventos en tiempo real, pero no aporta ninguna información sobre completitud. En la práctica, los relays aplican un límite por suscripción, normalmente entre 300 y 1000 eventos, independiente del `limit` del cliente. Un cliente que pide las últimas 500 notas a un relay limitado a 300 recibe 300 eventos y un `EOSE`, sin forma de distinguir entre "eso era todo" y "nos detuvimos a mitad de camino". La solución actual es comparar la cantidad de eventos con el `limit` del cliente y paginar de forma defensiva, lo que tanto pierde eventos cuando el límite del relay es menor que el solicitado como desperdicia una vuelta extra cuando el límite coincide con un múltiplo del conteo real.

Los empates en el límite empeoran el problema. Paginar con `until = oldest_created_at` corre el riesgo de perder o volver a pedir eventos que comparten el timestamp más antiguo del lote, según cómo compare timestamps el relay.

## El cambio

NIP-67 añade un tercer elemento opcional a `EOSE`:

```
["EOSE", "<subscription_id>", "finish"]   // se entregaron todos los eventos almacenados coincidentes
["EOSE", "<subscription_id>"]             // no hay afirmación de completitud (legado)
```

Solo se especifica la señal positiva. Un relay que anuncia soporte para NIP-67 pero omite el indicio está diciendo que hay más. Un relay que no anuncia soporte cae en la heurística existente, así que el cambio es retrocompatible con todos los clientes y relays actuales.

Los clientes que saben que su relay soporta NIP-67 pueden dejar de paginar en cuanto ven `"finish"`, evitar la vuelta extra obligatoria cuando el límite coincide exactamente con el conjunto de resultados y mostrar al usuario una completitud correcta.

## Estado

La propuesta está [abierta como PR #2317](https://github.com/nostr-protocol/nips/pull/2317) contra el repositorio de NIPs.

---

**Fuentes primarias:**
- [PR #2317: NIP-67 EOSE Completeness Hint](https://github.com/nostr-protocol/nips/pull/2317)
- [Especificación NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Mencionado en:**
- [Boletín #19: Actualizaciones de NIP](/en/newsletters/2026-04-22-newsletter/)

**Ver también:**
- [NIP-01: Flujo básico del protocolo](/es/topics/nip-01/)
- [NIP-11: Documento de información del relay](/es/topics/nip-11/)
