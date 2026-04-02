---
title: "NIP-99: Listados Clasificados"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Commerce
  - Marketplaces
---

NIP-99 define eventos de listados clasificados direccionables para bienes, servicios, empleos, alquileres y otras ofertas. Le da a las aplicaciones de marketplace un modelo de evento más simple que la antigua especificación de marketplace [NIP-15](/es/topics/nip-15/), razón por la cual muchos clientes de comercio actuales construyen sobre NIP-99 en su lugar.

## Cómo Funciona

Los listados activos usan kind `30402`, mientras que los borradores o listados inactivos usan kind `30403`. La pubkey del autor es el vendedor o creador de la oferta. El campo `content` lleva la descripción legible por humanos en Markdown, y las etiquetas contienen campos estructurados como título, resumen, precio, ubicación y estado.

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

El evento es direccionable, por lo que un vendedor puede actualizar el listado manteniendo la misma tupla de identidad de pubkey, kind y etiqueta `d`. Esto hace que las revisiones de listados sean más limpias para los clientes que publicar una nota inmutable completamente nueva para cada cambio de precio o estado.

## Por Qué Importa

La fortaleza de NIP-99 es que deja espacio para diferentes diseños de marketplace mientras estandariza la forma central del listado. Un cliente puede enfocarse en clasificados locales, otro en suscripciones, y otro en catálogos de productos globales. Si todos coinciden en la estructura del evento, los vendedores pueden publicar una vez y aún obtener algo de visibilidad entre clientes.

Esa flexibilidad también explica por qué los proyectos de marketplace actuales lo favorecen. La especificación es lo suficientemente estructurada para soportar búsqueda y visualización, pero no fuerza a cada aplicación a un único flujo de trabajo de escrow, envío o pago.

## Notas de Implementación

- Las etiquetas `price` pueden describir pagos únicos o recurrentes añadiendo un campo opcional de frecuencia.
- Las etiquetas `t` actúan como categorías o palabras clave de búsqueda.
- Las etiquetas `image` permiten a los clientes renderizar vistas de galería sin parsear el cuerpo Markdown.
- Un listado puede enlazar a eventos o documentos relacionados con etiquetas `e` o `a` cuando un marketplace quiere contexto de producto más rico.

## Implementaciones

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Marketplace Nostr usando listados NIP-99 con endpoints MCP orientados a agentes
- [Milk Market](https://github.com/shopstr-eng/milk-market) - Marketplace de alimentos construido sobre la misma capa de listados con opciones de pago mixtas

---

**Fuentes primarias:**
- [Especificación NIP-99](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - Endpoints de comercio MCP sobre listados NIP-99
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - Suscripción y checkout multi-comerciante sobre listados de marketplace

**Mencionado en:**
- [Newsletter #13: Shopstr y Milk Market Abren Superficies de Comercio MCP](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)

**Ver también:**
- [NIP-15: Ofertas de Marketplace](/es/topics/nip-15/)
- [NIP-47: Nostr Wallet Connect](/es/topics/nip-47/)
- [NIP-60: Cashu Wallet](/es/topics/nip-60/)
