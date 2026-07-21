---
title: "Gamma Markets"
date: 2026-07-15
draft: false
translationOf: /en/topics/gamma-markets.md
translationDate: 2026-07-15
categories:
  - Commerce
  - Marketplace
  - Protocol
---

Gamma Markets es un conjunto de convenciones de comercio electrónico construidas directamente sobre las listas de clasificados [NIP-99](/es/topics/nip-99/), desarrolladas colaborativamente por un grupo de trabajo de desarrolladores de mercados Nostr: los equipos detrás de Shopstr, Cypher, Plebeian Market y Conduit Market. Completa las convenciones de envío, flujo de pedidos, colecciones y reseñas que NIP-99 deja sin definir.

## Cómo funciona

Gamma Markets añade cinco kinds de eventos alrededor del evento de lista kind `30402` existente de NIP-99, sin cambiar la forma de ese evento:

- **Kind 30405** - colecciones de productos, agrupando múltiples listas mediante etiquetas `a`
- **Kind 30406** - opciones de envío, con precios por país y reglas opcionales de costo basadas en peso o distancia
- **Kind 16** - mensajes de pedido: creación (type 1), solicitudes de pago (type 2), actualizaciones de estado (type 3) y actualizaciones de envío (type 4)
- **Kind 14** - comunicación general entre comprador y comerciante
- **Kind 17** - recibos de pago
- **Kind 31555** - reseñas de productos, dirigidas a un pubkey de vendedor y etiqueta `d` de lista específicos

Las preferencias de pago de un comerciante se declaran mediante una etiqueta `payment_preference` en sus metadatos de perfil kind `0`, y los clientes descubren aplicaciones compatibles a través de recomendaciones de aplicaciones [NIP-89](/es/topics/nip-89/). La comunicación de pedidos se construye sobre mensajes privados [NIP-17](/es/topics/nip-17/), sin un esquema de cifrado nuevo propio.

La decisión de diseño definitoria de la especificación es que nada se hereda en cascada: una lista que pertenece a una colección, o que usa una opción de envío, la referencia explícitamente con una etiqueta `a` en lugar de heredar automáticamente la configuración de su padre. Esa es una desviación deliberada del modelo de puesto más antiguo de [NIP-15](/es/topics/nip-15/), donde un producto heredaba silenciosamente la moneda y la tabla de envío de su puesto.

### Ejemplo: creación de pedido (kind 16, type 1)

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

## Por qué importa

NIP-99 por sí solo estandariza únicamente la lista en sí, un anuncio clasificado firmado y direccionable. Antes de Gamma Markets, cada cliente que construía comercio electrónico real sobre NIP-99 inventaba sus propias convenciones privadas para envío, pago y reseñas, lo que significaba que dos clientes compatibles con NIP-99 podían renderizar correctamente una lista pero carecían de una forma compartida de completar un pedido entre ellos. Gamma Markets cierra esa brecha sin tocar el formato de lista de NIP-99, de modo que las listas NIP-99 existentes siguen siendo válidas sin modificación.

## Implementaciones

- [Shopstr](https://github.com/shopstr-eng/shopstr) - mercado Nostr, uno de los cuatro proyectos que escribieron la especificación
- [Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) - protocolo de mercado que construye su propio flujo de estado de pedidos y pago en el mismo espacio de diseño

---

**Fuentes primarias:**
- [Repositorio de la especificación Gamma Markets](https://github.com/GammaMarkets/market-spec)
- [Extensión de caso de uso de comercio electrónico NIP-99, PR #1784](https://github.com/nostr-protocol/nips/pull/1784) - enlace fusionado desde el documento canónico de NIP-99 a la especificación de Gamma Markets

**Mencionado en:**
- [Newsletter #31: NIP Deep Dive: NIP-99 y la extensión de comercio Gamma Markets](/es/newsletters/2026-07-15-newsletter/#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension)

**Ver también:**
- [NIP-99: Classified Listings](/es/topics/nip-99/)
- [NIP-15: Nostr Marketplace](/es/topics/nip-15/)
- [NIP-17: Private Direct Messages](/es/topics/nip-17/)
