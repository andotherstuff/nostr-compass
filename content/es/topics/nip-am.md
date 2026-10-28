---
title: 'Borrador de NIP-AM de Buzz: métricas de turnos de agentes'
date: 2026-10-28
translationOf: /en/topics/nip-am.md
translationDate: 2026-10-28
draft: false
---

**Estado:** se trata de una propuesta en borrador específica del proyecto Buzz. NIP-AM no es un NIP oficial aceptado. La etiqueta procede de la documentación del proyecto Buzz, y el repositorio oficial de NIPs no la ha asignado ni aprobado.

## Propósito

NIP-AM registra el uso de cada turno completado de un agente de IA. Por cada turno, el agente publica un event `kind:44200`, que la convención de Buzz trata como un event regular de solo anexado. El contenido va cifrado con NIP-44 del agente al propietario. Contiene cifras de uso de tokens junto con IDs de correlación, y cualquier valor de coste es una estimación. No incluye ninguna transcripción de la conversación.

## Límites

Los tags públicos identifican al propietario y al agente, y los relays siguen pudiendo ver cuándo se publican los events. Por tanto, el formato no oculta que hubo actividad. Un valor de uso ausente significa desconocido y nunca debe contarse como cero.

## Propuesta de lectores delegados

Una pull request de documentación abierta, la #8582, propone una concesión de mínimo privilegio firmada por el propietario. Con ella, el agente publicaría una copia cifrada independiente para cada lector activo, cada una vinculada al ID exacto del event de concesión. La pull request no cambia ninguna autorización en tiempo de ejecución. Tanto el kind de concesión propuesto, `30180`, como el límite de lectores siguen siendo cuestiones abiertas, y la política de revocación tampoco está decidida. La revocación podría limitar el historial en los relays y las lecturas futuras. Lo que no puede es borrar las copias que un lector ya haya recibido.

## Fuentes primarias

- [Borrador de NIP-AM de Buzz: métricas de turnos de agentes (revisión fijada)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-AM.md)
- [Pull request #8582 de Buzz: lectores de métricas delegados (borrador abierto)](https://github.com/block/buzz/pull/8582)

## Véase también

- [NIP-44](/es/topics/nip-44/)

**Mencionado en:**

- [Boletín n.º 46: texto en borrador de NIP-AM para lectores de métricas delegados](/es/newsletters/2026-10-28-newsletter/#draft-nip-am-text-for-delegated-metric-readers)
- [Boletín n.º 46: Buzz](/es/newsletters/2026-10-28-newsletter/#buzz)
