---
title: "NIP-50: Search"
date: 2025-12-31
translationOf: /en/topics/nip-50.md
translationDate: 2025-12-31
draft: false
categories:
  - Protocolo
  - Relay
---

NIP-50 define una capacidad de búsqueda generalizada para relays de Nostr, permitiendo a los clientes realizar búsquedas de texto completo más allá de consultas estructuradas por tags o IDs.

## Cómo Funciona

El protocolo añade un campo `search` a los objetos de filtro en mensajes REQ:

1. Los clientes envían consultas de búsqueda legibles por humanos (ej., "mejores apps de nostr")
2. Los relays interpretan y hacen coincidir las consultas contra los datos de eventos, principalmente el campo `content`
3. Los resultados se ordenan por relevancia en lugar de orden cronológico
4. El filtro `limit` se aplica después de la ordenación por relevancia

Los filtros de búsqueda pueden combinarse con otras restricciones como `kinds` e `ids` para consultas más específicas.

## Extensiones de Búsqueda

Los relays pueden opcionalmente soportar estos parámetros de extensión:

- `include:spam` - Desactiva el filtrado de spam por defecto
- `domain:<domain>` - Filtra por dominio NIP-05 verificado
- `language:<code>` - Filtra por código de idioma ISO
- `sentiment:<value>` - Filtra por sentimiento negativo/neutral/positivo
- `nsfw:<true/false>` - Incluye o excluye contenido NSFW

## Consideraciones para Clientes

- Los clientes deben verificar las capacidades del relay mediante el campo `supported_nips`
- Se recomienda la verificación de resultados del lado del cliente
- No todos los relays implementan búsqueda; sigue siendo una característica opcional

---

**Fuentes primarias:**
- [Especificación NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md)

**Mencionado en:**
- [Newsletter #3: Resumen de Diciembre](/es/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Ver también:**
- [NIP-11: Información del Relay](/es/topics/nip-11/)
