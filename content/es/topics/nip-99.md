---
title: "NIP-99: Anuncios clasificados"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Commerce
  - Marketplaces
---

NIP-99 define eventos direccionables de anuncios clasificados para bienes, servicios, empleos, alquileres y otras ofertas. Da a las apps de marketplace un modelo de evento más simple que la especificación de marketplace más antigua de [NIP-15](/es/topics/nip-15/), por lo que muchos clientes de comercio actuales se apoyan en NIP-99 en su lugar.

## Cómo funciona

Los anuncios activos usan kind `30402`, mientras que los borradores o anuncios inactivos usan kind `30403`. La pubkey del autor es la del vendedor o creador de la oferta. El campo `content` lleva la descripción legible para humanos en Markdown, y las etiquetas contienen campos estructurados como título, resumen, precio, ubicación y estado.

```json
{
  "id": "b3e392b11f5d4f28321cedd09303a748acfd0487aea5a7450b3481c60b6e4f87",
  "pubkey": "a695f6b60119d9521934a691347d9f78e8770b56da16bb255ee286ddf9fda919",
  "created_at": 1741699200,
  "kind": 30402,
  "tags": [
    ["d", "shopstr-handmade-wallet-001"],
    ["title", "Handmade leather wallet"],
    ["summary", "Brown bifold wallet with Bitcoin and Nostr branding"],
    ["published_at", "1741699200"],
    ["location", "Austin, TX"],
    ["price", "75000", "SAT"],
    ["status", "active"],
    ["t", "merch"],
    ["t", "bitcoin"]
  ],
  "content": "Full listing description in Markdown, shipping details, and contact terms.",
  "sig": "4a5c7e8f9012ab34cd56ef7890ab12cd34ef56ab78cd90ef12ab34cd56ef78900112233445566778899aabbccddeeff00112233445566778899aabbccddeeff"
}
```

El evento es direccionable, así que un vendedor puede actualizar el anuncio manteniendo la misma tupla de identidad de pubkey, kind y etiqueta `d`. Eso hace que las revisiones del anuncio sean más limpias para los clientes que publicar una nota inmutable completamente nueva por cada cambio de precio o de estado.

## Por qué importa

La fuerza de NIP-99 es que deja espacio para distintos diseños de marketplace mientras sigue estandarizando la forma central del anuncio. Un cliente puede centrarse en clasificados locales, otro en suscripciones y otro en catálogos globales de productos. Si todos coinciden en la estructura del evento, los vendedores pueden publicar una vez y aun así obtener cierta visibilidad entre clientes.

Esa flexibilidad también explica por qué los proyectos de marketplace actuales lo favorecen. La especificación está lo bastante estructurada para soportar búsqueda y visualización, pero no obliga a cada app a un único flujo de escrow, envío o pago.

## Notas de implementación

- Las etiquetas `price` pueden describir pagos únicos o recurrentes añadiendo un campo opcional de frecuencia.
- Las etiquetas `t` actúan como categorías o palabras clave de búsqueda.
- Las etiquetas `image` permiten a los clientes renderizar vistas de galería sin analizar el cuerpo Markdown.
- Un anuncio puede enlazar a eventos o documentos relacionados con etiquetas `e` o `a` cuando un marketplace quiere un contexto de producto más rico.

## Implementaciones

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Marketplace Nostr que usa anuncios NIP-99 con endpoints MCP orientados a agentes
- [Milk Market](https://github.com/shopstr-eng/milk-market) - Marketplace de alimentos construido sobre la misma capa de anuncios con opciones de pago mixtas

---

**Fuentes primarias:**
- [Especificación de NIP-99](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - Endpoints de comercio MCP sobre anuncios NIP-99
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - Checkout por suscripción y multi-merchant sobre anuncios de marketplace

**Mencionado en:**
- [Newsletter #13: Shopstr y Milk Market abren superficies MCP para comercio](/es/newsletters/2026-03-11-newsletter/#shopstr-y-milk-market-abren-superficies-mcp-para-comercio)

**Ver también:**
- [NIP-15: Ofertas de marketplace](/es/topics/nip-15/)
- [NIP-47: Nostr Wallet Connect](/es/topics/nip-47/)
- [NIP-60: Cashu Wallet](/es/topics/nip-60/)
