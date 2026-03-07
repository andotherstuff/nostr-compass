---
title: "Negentropy: Protocolo de Reconciliación de Conjuntos"
date: 2026-01-28
translationOf: /en/topics/negentropy.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Sync
---

Negentropy es un protocolo de reconciliación de conjuntos para determinar qué eventos tiene un lado y le faltan al otro, sin reenviar el conjunto de datos completo.

## Cómo Funciona

En lugar de solicitar todos los eventos que coinciden con un filtro, negentropy compara dos conjuntos ordenados y se enfoca solo en los rangos que difieren. El protocolo intercambia resúmenes compactos de rangos y recurre a listas explícitas de IDs solo donde es necesario.

1. **Ordenamiento**: Ambos lados ordenan los registros por marca de tiempo y luego por ID
2. **Comparación de rangos**: Intercambian huellas digitales para rangos de registros
3. **Refinamiento**: Los rangos que no coinciden se subdividen hasta que los IDs faltantes quedan claros

## Por Qué Importa

La sincronización tradicional de Nostr usa filtros `since` basados en marcas de tiempo, que pueden perder eventos debido a:
- Deriva de reloj entre cliente y relay
- Múltiples eventos con marcas de tiempo idénticas
- Eventos que llegan fuera de orden

Negentropy resuelve estos problemas comparando conjuntos de eventos reales en lugar de depender de marcas de tiempo.

## Uso Práctico

- **Recuperación de DMs**: Los clientes pueden detectar y obtener mensajes directos faltantes incluso con marcas de tiempo antiguas
- **Sincronización de feeds**: Asegura sincronización completa de línea de tiempo a través de relays
- **Sincronización offline**: Permite ponerse al día de forma eficiente después de períodos de desconexión

El detalle útil de implementación es que muchos clientes no reemplazan las suscripciones normales con negentropy. Lo usan como ruta de reparación. Damus, por ejemplo, mantuvo la carga ordinaria de DMs y añadió negentropy en la actualización manual para recuperar mensajes que el flujo normal omitiría.

## Compensaciones

Negentropy requiere soporte en ambos lados y añade complejidad al protocolo más allá del uso estándar de `REQ`. Es más útil cuando la corrección importa más que el esfuerzo mínimo de implementación.

En entornos mixtos, los clientes aún necesitan comportamiento de respaldo elegante porque no todos los relays soportan el protocolo.

---

**Fuentes primarias:**
- [Repositorio del Protocolo Negentropy](https://github.com/hoytech/negentropy)
- [Damus PR #3536](https://github.com/damus-io/damus/pull/3536)
- [Damus PR #3547](https://github.com/damus-io/damus/pull/3547)

**Mencionado en:**
- [Boletín #6: Damus implementa negentropy para sincronización confiable de DMs](/es/newsletters/2026-01-28-newsletter/#damus-ships-negentropy-for-reliable-dm-syncing)
- [Boletín #12](/es/newsletters/2026-03-04-newsletter/)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
