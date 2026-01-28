---
title: "NIP-15: Mercado Nostr"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15 define un protocolo para mercados descentralizados en Nostr, permitiendo a comerciantes listar productos y a compradores realizar compras usando Bitcoin y Lightning.

## Cómo Funciona

### Puestos de Comerciantes (Kind 30017)

Los comerciantes crean puestos como eventos direccionables:

```json
{
  "kind": 30017,
  "tags": [
    ["d", "my-stall"],
    ["name", "Electrónica de Bob"],
    ["description", "Electrónica usada de calidad"],
    ["currency", "sat"],
    ["shipping", "{...opciones de envío...}"]
  ]
}
```

### Productos (Kind 30018)

Los productos se listan dentro de puestos:

```json
{
  "kind": 30018,
  "tags": [
    ["d", "product-123"],
    ["stall_id", "my-stall"],
    ["name", "Raspberry Pi 4"],
    ["price", "50000"],
    ["quantity", "5"],
    ["images", "https://..."]
  ]
}
```

## Flujo de Compra

1. El comprador navega productos a través de múltiples puestos
2. El comprador envía mensaje de pedido cifrado al comerciante
3. El comerciante responde con factura Lightning
4. El comprador paga la factura
5. El comerciante envía el producto

## Características Clave

- **Descentralizado**: Sin operador central de mercado
- **Interoperable**: Cualquier cliente NIP-15 puede navegar cualquier comerciante
- **Privado**: Los pedidos están cifrados entre comprador y vendedor
- **Nativo de Bitcoin**: Pagos Lightning integrados

## Implementaciones

- **Plebeian Market** - Mercado NIP-15 con todas las funciones
- **Shopstr** - Comercio Bitcoin sin permisos
- **Amethyst** - Listados de productos integrados en el feed social

## Relacionado

- [NIP-44](/es/topics/nip-44/) - Mensajes cifrados para pedidos
- [NIP-57](/es/topics/nip-57/) - Zaps Lightning
