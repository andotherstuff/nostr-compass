---
title: "Negentropy: Protocolo de Reconciliación de Conjuntos"
date: 2026-01-28
translationOf: /en/topics/negentropy.md
translationDate: 2026-01-28
draft: false
categories:
  - Protocol
  - Sync
---

Negentropy es un protocolo de reconciliación de conjuntos que permite sincronización eficiente entre clientes y relays de Nostr identificando eventos faltantes sin transferir el conjunto de datos completo.

## Cómo Funciona

En lugar de solicitar todos los eventos que coinciden con un filtro, negentropy permite a los clientes comparar su conjunto local de eventos contra el conjunto de un relay e identificar solo las diferencias. Esto se logra a través de un protocolo de múltiples rondas:

1. **Huellas digitales**: Cliente y relay calculan cada uno una huella digital de sus conjuntos de eventos
2. **Comparación**: Las huellas digitales se intercambian y comparan
3. **Reconciliación**: Solo los IDs de eventos faltantes se identifican y transfieren

## Por Qué Importa

La sincronización tradicional de Nostr usa filtros `since` basados en marcas de tiempo, que pueden perder eventos debido a:
- Deriva de reloj entre cliente y relay
- Múltiples eventos con marcas de tiempo idénticas
- Eventos llegando fuera de orden

Negentropy resuelve estos problemas comparando conjuntos de eventos reales en lugar de depender de marcas de tiempo.

## Casos de Uso

- **Recuperación de DMs**: Los clientes pueden detectar y obtener mensajes directos faltantes incluso con marcas de tiempo antiguas
- **Sincronización de feeds**: Asegura sincronización completa de línea de tiempo a través de relays
- **Sincronización offline**: Alcanza eficientemente después de períodos de desconexión

## Implementación

Negentropy requiere soporte del relay. Los clientes típicamente lo implementan como un mecanismo de recuperación de respaldo en lugar de reemplazar suscripciones REQ estándar, degradando elegantemente cuando los relays no soportan el protocolo.

## Relacionado

- [NIP-01](/es/topics/nip-01/) - Protocolo Básico
