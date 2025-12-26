---
title: "NIP-69: Trading Peer-to-Peer"
date: 2025-12-17
draft: false
categories:
  - Trading
  - Protocol
---

NIP-69 define un protocolo para trading peer-to-peer sobre Nostr, creando un libro de órdenes unificado a través de múltiples plataformas en lugar de pools de liquidez fragmentados.

## Tipo de Evento

- **Kind 38383** - Eventos de orden P2P

## Estructura de Orden

Las órdenes usan etiquetas para especificar parámetros de intercambio:

- `d` - ID de orden
- `k` - Tipo de orden (compra/venta)
- `f` - Moneda fiat (código ISO 4217)
- `amt` - Cantidad de Bitcoin en satoshis
- `fa` - Cantidad fiat
- `pm` - Métodos de pago aceptados
- `premium` - Porcentaje de prima/descuento del precio
- `network` - Capa de liquidación (onchain, lightning, liquid)
- `expiration` - Cuándo expira la orden

## Ciclo de Vida de la Orden

Las órdenes progresan a través de estados:
- `pending` - Abierta y disponible para emparejar
- `in-progress` - Intercambio iniciado con contraparte
- `success` - Intercambio completado
- `canceled` - Retirada por el creador
- `expired` - Pasó el tiempo de expiración

## Seguridad

La etiqueta `bond` especifica un depósito de seguridad que ambas partes deben pagar, proporcionando protección contra abandono o fraude.

---

**Fuentes primarias:**
- [Especificación NIP-69](https://github.com/nostr-protocol/nips/blob/master/69.md)

**Mencionado en:**
- [Boletín #1: Actualizaciones de NIP](/es/newsletters/2025-12-17-newsletter/#nip-updates)
- [Boletín #1: Lanzamientos](/es/newsletters/2025-12-17-newsletter/#releases)
- [Boletín #2: Noticias](/es/newsletters/2025-12-24-newsletter/#news)
