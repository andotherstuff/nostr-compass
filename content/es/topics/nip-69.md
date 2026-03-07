---
title: "NIP-69: Trading Peer-to-Peer"
date: 2025-12-17
translationOf: /en/topics/nip-69.md
translationDate: 2026-03-07
draft: false
categories:
  - Trading
  - Protocol
---

NIP-69 define un protocolo para trading peer-to-peer sobre Nostr, creando un libro de órdenes unificado a través de múltiples plataformas en lugar de pools de liquidez fragmentados.

## Cómo Funciona

NIP-69 usa eventos direccionables kind 38383 para órdenes de compra y venta. El formato direccionable importa porque una orden puede pasar por varios estados a lo largo del tiempo manteniendo la misma identidad lógica a través de su etiqueta `d`.

## Estructura de Orden

Las órdenes usan etiquetas para especificar parámetros de intercambio:

- `d` - ID de orden
- `k` - Tipo de orden (compra/venta)
- `f` - Moneda fiat (código ISO 4217)
- `amt` - Cantidad de Bitcoin en satoshis
- `fa` - Cantidad fiat
- `pm` - Métodos de pago aceptados
- `premium` - Porcentaje de prima/descuento del precio
- `network` - Red de Bitcoin (mainnet, testnet, signet, regtest)
- `layer` - Capa de liquidación (onchain, lightning, liquid)
- `expiration` - Cuándo expira la orden

## Ciclo de Vida de la Orden

Las órdenes progresan a través de estados:
- `pending` - Abierta y disponible para emparejar
- `in-progress` - Intercambio iniciado con contraparte
- `success` - Intercambio completado
- `canceled` - Retirada por el creador
- `expired` - Pasó el tiempo de expiración

La especificación distingue dos límites de tiempo. `expires_at` marca cuándo una orden pendiente debe dejar de considerarse abierta, mientras que `expiration` da a los relays un timestamp que pueden usar con [NIP-40](/es/topics/nip-40/) para eliminar por completo los eventos de órdenes obsoletas.

## Por Qué Importa

NIP-69 es una apuesta por la interoperabilidad. Mostro, lnp2pBot, RoboSats, Peach y otros sistemas de trading P2P pueden exponer órdenes en un formato de evento compartido en lugar de mantener la liquidez atrapada dentro de aplicaciones separadas.

La etiqueta `g` opcional también hace posible el trading local cara a cara sin cambiar el resto del esquema de órdenes. Eso es útil porque los intercambios locales en efectivo necesitan filtrado geográfico, mientras que los intercambios Lightning en línea no.

## Seguridad y Confianza

La etiqueta `bond` especifica un depósito de seguridad que ambas partes deben pagar, proporcionando protección contra abandono o fraude.

Eso no elimina el riesgo de contraparte. Las disputas de pago, el fraude fiat, la reputación y las reglas de custodia siguen viviendo en la capa de aplicación. NIP-69 estandariza la publicación de órdenes, no la resolución de disputas.

---

**Fuentes primarias:**
- [Especificación NIP-69](https://github.com/nostr-protocol/nips/blob/master/69.md)
- [Especificación del Protocolo Mostro](https://mostro.network/protocol/)

**Mencionado en:**
- [Newsletter #1: Actualizaciones de NIP](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #1: Lanzamientos](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2: Noticias](/en/newsletters/2025-12-24-newsletter/#news)

**Ver también:**
- [NIP-40: Timestamp de Expiración](/es/topics/nip-40/)
