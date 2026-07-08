---
title: "NIP-101e: Entrenamientos deportivos"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-101e.md
translationDate: 2026-07-01
categories:
  - Fitness
  - Discovery
---

NIP-101e define un formato de evento de entrenamiento para que las aplicaciones de seguimiento deportivo puedan publicar, compartir y descubrir sesiones de entrenamiento en Nostr. La especificación usa eventos de kind 1301 que transportan métricas de la sesión (distancia, duración, elevación, frecuencia cardíaca, calorías, cadencia de ciclismo, aplicación de origen) en tags estructurados para que un cliente pueda mostrar el entrenamiento como una tarjeta estructurada con métricas presentadas en sus unidades correctas.

## Cómo funciona

Un entrenamiento NIP-101e es un evento de kind 1301 con tags estructurados para cada métrica que la aplicación de origen capturó. Los tags comunes incluyen:

- `type` para la disciplina del entrenamiento (correr, ciclismo, natación, levantamiento, etc.)
- `distance` con valor y unidad
- `duration` en segundos
- `elevation_gain` con valor y unidad
- Timestamps `start` y `end`
- `heart_rate` (promedio y máximo)
- `calories` para el gasto energético
- `source` que nombra la aplicación publicadora
- Tags de tópico `t` para descubrimiento por hashtag

El campo `content` transporta una nota opcional escrita por el usuario (el equivalente al pie de foto que un usuario adjuntaría a una subida de Strava). Los clientes que reconocen kind 1301 muestran las métricas estructuradas como una tarjeta de entrenamiento; los clientes que no lo hacen recurren a mostrar el campo `content` como una nota normal.

## Descubrimiento y semántica del feed

Los eventos NIP-101e son eventos normales del feed, por lo que un entrenamiento publicado por un usuario aparece en las líneas de tiempo de sus seguidores como cualquier otra publicación. Los clientes con vistas dedicadas a entrenamientos pueden suscribirse a kind 1301 con filtros de autor o hashtag para construir superficies de registro de entrenamientos, tablas de clasificación o feeds de desafíos comunitarios. La pubkey del autor es la identidad canónica del entrenamiento, por lo que una aplicación de terceros que lee los entrenamientos de otro usuario hereda los mismos supuestos de confianza que cualquier otro feed de Nostr.

## Implementaciones

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) incorpora renderizado de entrenamientos kind 1301 con una métrica destacada, una cuadrícula de estadísticas, visualización de velocidad específica para ciclismo y distintivos de origen ([PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184), refactorizado en [PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226))

---

**Fuentes primarias:**
- [Especificación NIP-101e](https://github.com/nostr-protocol/nips/blob/master/101e.md)
- [Amethyst PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184) - Añadir soporte de entrenamientos deportivos NIP-101e (Kind 1301)
- [Amethyst PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226) - Rediseñar la visualización de entrenamientos con métrica destacada y cuadrícula de estadísticas

**Mencionado en:**
- [Boletín #27: Amethyst v1.12.0 incorpora wallets Cashu, nutzaps, un driver CLINK y auto-reparación de Tor](/es/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
