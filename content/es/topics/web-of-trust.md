---
title: "Web of Trust"
date: 2025-12-31
translationOf: /en/topics/web-of-trust.md
translationDate: 2026-03-07
draft: false
categories:
  - Trust
  - Social Graph
---

Web of Trust (WoT) es un modelo de confianza descentralizado donde la reputación y la confiabilidad se derivan de las relaciones del grafo social en lugar de autoridades centrales.

## Cómo funciona

En Nostr, Web of Trust generalmente comienza desde el grafo de seguidos en [NIP-02: Follow List](/es/topics/nip-02/) y a veces añade silencios, reportes o señales de identidad verificada. Un cliente o servicio elige una o más pubkeys semilla en las que ya confía, y luego propaga la confianza hacia afuera a través del grafo.

1. **Construcción del grafo**: Se construye un grafo dirigido de seguidos y señales negativas opcionales
2. **Selección de semillas**: Se parte de pubkeys que el observador ya confía
3. **Propagación de puntuación**: Se empuja el rango a través del grafo con un algoritmo como PageRank o una variante
4. **Cortes y normalización**: Se limita la profundidad del grafo, se amortiguan cuentas de baja señal y se normaliza la puntuación final para visualización o filtrado

El algoritmo exacto no está estandarizado. Dos sistemas WoT pueden ser ambos válidos mientras producen rankings diferentes porque usan diferentes semillas, profundidad de grafo, reglas de decaimiento o tratamientos de silencios y reportes.

## Por qué importa

WoT da a Nostr una forma de clasificar y filtrar sin un servicio central de moderación. Un grafo de confianza personalizado es más difícil de manipular que un conteo bruto de seguidores porque las cuentas falsas aún necesitan que la confianza fluya hacia ellas desde la red existente del observador.

La otra cara es el arranque en frío. Si no sigues a nadie, un WoT personalizado no tiene casi ninguna base para clasificar nada. Muchos productos resuelven esto con seguidos iniciales, valores predeterminados de proveedores de confianza, o puntuaciones precalculadas de servicios externos.

## Aplicaciones en Nostr

- **Filtrado de spam**: Los relays pueden usar WoT para filtrar contenido de baja confianza
- **Descubrimiento de contenido**: Mostrar contenido de cuentas en las que confía tu red
- **Directorios de pago**: Búsqueda de direcciones Lightning con prevención de suplantación
- **Políticas de relay**: Los relays WoT aceptan solo notas de pubkeys confiables
- **Moderación descentralizada**: Las comunidades pueden curar basándose en puntuaciones de confianza

## Notas de implementación

Dado que los cálculos de WoT requieren rastrear grandes partes de la red, muchos clientes no los calculan localmente. [NIP-85: Trusted Assertions](/es/topics/nip-85/) existe en parte por esta razón: da a los clientes una forma de consumir cálculos WoT firmados de terceros cuando el cómputo local es demasiado costoso.

Las implementaciones existentes también responden diferentes preguntas. Un rango de confianza global es útil para descubrimiento y resistencia al spam en toda la red. Una puntuación local personalizada es mejor para "muéstrame cuentas en las que mi grafo confiaría." Leer un número WoT sin saber qué modelo lo produjo es una fuente común de confusión.

---

**Fuentes primarias:**
- [NIP-02: Follow List](https://github.com/nostr-protocol/nips/blob/master/02.md)
- [NIP-85: Trusted Assertions](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [DCoSL Protocol](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**Mencionado en:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Ver también:**
- [NIP-02: Follow List](/es/topics/nip-02/)
