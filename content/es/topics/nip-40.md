---
title: "NIP-40: Marca de Tiempo de Expiración"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-40 define una etiqueta de expiración que indica a los relays cuándo un evento debe ser eliminado.

## Estructura

Los eventos incluyen una etiqueta `expiration` con una marca de tiempo Unix:

```json
["expiration", "1734567890"]
```

Después de este tiempo, los relays deben eliminar el evento y negarse a servirlo.

## Casos de Uso

- Contenido efímero que debe desaparecer después de un tiempo establecido
- Ofertas o anuncios de tiempo limitado
- Expiración de listados en marketplaces (ej., Shopstr)
- Reducción de requisitos de almacenamiento de relays

## Consideraciones

- Los relays no están obligados a respetar la expiración (pero la mayoría lo hace)
- Los clientes no deben confiar en la expiración para eliminación de contenido crítico para la seguridad
- Una vez que el contenido es obtenido por otro cliente, puede ser cacheado o re-publicado

---

**Fuentes primarias:**
- [Especificación NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md)

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)
