---
title: "NIP-91: Operador AND para Filtros"
date: 2026-03-04
translationOf: /en/topics/nip-91.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - Protocol
---

NIP-91 añade semántica de filtro AND para arrays de etiquetas en suscripciones de relays Nostr. Se fusionó el 2026-03-03 después de que aparecieran implementaciones en múltiples relays.

## El problema

El sistema de filtros de Nostr ([NIP-01](/es/topics/nip-01/)) combina múltiples valores dentro de un mismo filtro de etiqueta usando lógica OR. Si un cliente especifica dos valores de etiqueta `p` en un filtro, el relay devuelve eventos que coincidan con cualquiera de las dos pubkeys. No había forma de solicitar eventos que referencien ambas pubkeys simultáneamente.

Esto forzaba a los clientes a obtener eventos en exceso desde los relays y filtrar localmente, aumentando el uso de ancho de banda y tiempo de procesamiento.

## Cómo funciona

NIP-91 introduce semántica AND para arrays de etiquetas. Cuando un cliente necesita eventos que coincidan con todos los valores de etiqueta especificados, puede optar por coincidencia de intersección en lugar del comportamiento de unión por defecto.

Eso importa para consultas como "eventos que etiqueten a ambos participantes en una conversación" o "eventos que lleven dos etiquetas requeridas a la vez." Antes de este cambio, los relays solo podían responder con el superconjunto más amplio y dejar la intersección precisa al cliente.

## Por qué importa

Los filtros AND hacen que los índices del lado del relay sean más útiles. Los clientes pueden pedir a un relay un conjunto de resultados más pequeño y ya relevante, lo que reduce el ancho de banda y el post-procesamiento local. La ganancia es más notable en clientes móviles y en consultas sobre conjuntos de datos grandes con muchas etiquetas.

## Notas de interoperabilidad

Al momento de la fusión, existían implementaciones funcionales en nostr-rs-relay, satellite-node, worker-relay y applesauce. La propuesta fue numerada anteriormente como NIP-119 antes de ser renumerada.

Los clientes deberían seguir esperando soporte mixto mientras la adopción en relays se pone al día. Un respaldo práctico es mantener la ruta antigua de intersección del lado del cliente para relays que aún no han implementado la nueva semántica.

---

**Fuentes primarias:**
- [PR #1365](https://github.com/nostr-protocol/nips/pull/1365)

**Mencionado en:**
- [Newsletter #12: NIP Updates](/es/newsletters/2026-03-04-newsletter/#nip-updates)

**Ver también:**
- [NIP-01: Basic Protocol](/es/topics/nip-01/)
