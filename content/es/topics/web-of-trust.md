---
title: "Web of Trust"
date: 2025-12-31
translationOf: /en/topics/web-of-trust.md
translationDate: 2025-12-31
draft: false
categories:
  - Confianza
  - Grafo Social
---

Web of Trust (WoT) es un modelo de confianza descentralizado donde la reputación y la confiabilidad se derivan de las relaciones del grafo social en lugar de autoridades centrales.

## Cómo Funciona

En Nostr, Web of Trust aprovecha el grafo de seguimiento (listas de contactos NIP-02) y eventos de reporte para calcular puntuaciones de confianza:

1. **Construcción del Grafo**: Se construye un grafo dirigido a partir de pubkeys, eventos y sus relaciones (seguimientos, silenciados, reportes)
2. **Asignación de Pesos**: Se asignan pesos iniciales a pubkeys conocidas como confiables (por ejemplo, aquellas con identificadores NIP-05 verificados)
3. **Propagación Iterativa**: Las puntuaciones de confianza fluyen a través de la red usando algoritmos similares a PageRank
4. **Resistencia a Sybil**: Si un atacante crea muchas cuentas falsas, la confianza pasada a ellas se divide por el número de falsas

## Propiedades Clave

- **Descentralizado**: Ninguna autoridad central determina la reputación
- **Personalizado**: La confianza puede calcularse desde la perspectiva de cada usuario basándose en a quién sigue
- **Resistente a Sybil**: Las granjas de bots no pueden manipular fácilmente el sistema debido a la dilución de confianza
- **Componible**: Puede aplicarse al filtrado de spam, moderación de contenido, admisión a relays y directorios de pago

## Aplicaciones en Nostr

- **Filtrado de Spam**: Los relays pueden usar WoT para filtrar contenido de baja confianza
- **Descubrimiento de Contenido**: Mostrar contenido de cuentas en las que confía tu red
- **Directorios de Pago**: Búsqueda de direcciones Lightning con prevención de suplantación
- **Políticas de Relay**: Los relays WoT aceptan solo notas de pubkeys confiables
- **Moderación Descentralizada**: Las comunidades pueden curar basándose en puntuaciones de confianza

## Implementaciones

Varios proyectos implementan Web of Trust para Nostr:
- **Nostr.Band Trust Rank**: Puntuación estilo PageRank para la red
- **WoT Relays**: Relays que filtran por distancia social
- **DCoSL**: Protocolo para sistemas de reputación descentralizados
- **Noswot**: Puntuación de confianza basada en seguimientos y reportes

---

**Fuentes principales:**
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [Protocolo DCoSL](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**Mencionado en:**
- [Newsletter #3: Resumen de Diciembre](/es/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Ver también:**
- [NIP-02: Lista de Seguidos](/es/topics/nip-02/)
