---
title: "NIP-50: Búsqueda"
date: 2025-12-31
translationOf: /en/topics/nip-50.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Relay
---

NIP-50 define una capacidad de búsqueda general para relays de Nostr. Añade consultas tipo texto completo sobre los filtros de coincidencia exacta de NIP-01.

## Cómo Funciona

El protocolo añade un campo `search` a los objetos de filtro en mensajes `REQ`:

1. Los clientes envían una cadena de consulta legible por humanos como `best nostr apps`.
2. Los relays interpretan esa consulta contra los datos de eventos, principalmente el campo `content`.
3. Los resultados se ordenan por calidad de coincidencia, no por `created_at`.
4. `limit` se aplica después de la ordenación por relevancia.

Los filtros de búsqueda pueden combinarse con `kinds`, `ids`, autores y otros campos de filtro normales para consultas más específicas.

## Extensiones de Búsqueda

Los relays pueden opcionalmente soportar estos parámetros de extensión:

- `include:spam` - Desactiva el filtrado de spam por defecto
- `domain:<domain>` - Filtra por dominio NIP-05 verificado
- `language:<code>` - Filtra por código de idioma ISO
- `sentiment:<value>` - Filtra por sentimiento negativo, neutral o positivo
- `nsfw:<true/false>` - Incluye o excluye contenido NSFW

Los relays deben ignorar extensiones que no soporten, por lo que los clientes necesitan tratarlas como sugerencias, no como garantías.

## Notas de Interoperabilidad

- Los clientes deben verificar las capacidades del relay mediante el campo `supported_nips`
- Se recomienda la verificación de resultados del lado del cliente
- No todos los relays implementan búsqueda; sigue siendo una función opcional

Dado que el ranking está definido por la implementación, la misma consulta puede retornar diferentes conjuntos de resultados en diferentes relays. Los clientes que se preocupan por la exhaustividad deben consultar más de un relay de búsqueda y fusionar resultados.

## Por Qué Importa

Los filtros estructurados funcionan bien cuando ya conoces el autor, kind o tag que quieres. La búsqueda es para el caso opuesto: descubrimiento. Eso hace que NIP-50 sea útil para directorios de aplicaciones, archivos extensos y búsqueda de notas públicas, pero también significa que la calidad de búsqueda depende en gran medida de las decisiones de indexación y filtrado de spam de cada relay.

---

**Fuentes primarias:**
- [Especificación NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md)

**Mencionado en:**
- [Newsletter #3: Resumen de Diciembre](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #7: Actualizaciones de NIPs](/en/newsletters/2026-01-07-newsletter/)

**Ver también:**
- [NIP-11: Información de Relay](/es/topics/nip-11/)
