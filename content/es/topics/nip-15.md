---
title: "NIP-15: Mercado Nostr"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15 define un protocolo para mercados descentralizados en Nostr, que permite a comerciantes listar productos y a compradores realizar compras usando Bitcoin y Lightning.

## Cómo Funciona

### Puestos de Comerciantes (Kind 30017)

Los comerciantes crean puestos como eventos direccionables:

```json
{
  "kind": 30017,
  "tags": [
    ["d", "my-stall"],
    ["name", "Bob's Electronics"],
    ["description", "Quality used electronics"],
    ["currency", "sat"],
    ["shipping", "{...shipping options...}"]
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
2. El comprador envía un mensaje de pedido cifrado al comerciante
3. El comerciante responde con una factura Lightning
4. El comprador paga la factura
5. El comerciante envía el producto

## Por Qué Importa

- **Descentralizado**: Sin operador central de mercado
- **Interoperable**: Cualquier cliente NIP-15 puede navegar cualquier comerciante
- **Privado**: Los pedidos están cifrados entre comprador y vendedor
- **Nativo de Bitcoin**: Pagos Lightning integrados

La ventaja práctica es la portabilidad. Un comerciante puede publicar datos de catálogo una vez y dejar que múltiples clientes los muestren, en lugar de quedar atado a un solo frontend de mercado.

## Compromisos

NIP-15 estandariza los listados, no la confianza. Los compradores aún necesitan decidir si un comerciante es legítimo, si el inventario es real y cómo se manejan las disputas. El protocolo proporciona estructuras de datos y flujo de mensajes comunes, pero la reputación y el cumplimiento siguen siendo problemas a nivel de aplicación.

Los pagos y envíos también están solo parcialmente estandarizados. Un cliente puede entender puestos y productos y aún necesitar lógica personalizada para facturas, estado de pedidos o seguimiento de entregas.

## Estado de Implementación

- **Plebeian Market** - Mercado NIP-15 completo
- **Shopstr** - Comercio Bitcoin sin permisos
- **Amethyst** - Listados de productos integrados en el feed social

---

**Fuentes primarias:**
- [Especificación NIP-15](https://github.com/nostr-protocol/nips/blob/master/15.md)

**Mencionado en:**
- [Newsletter #7: January 2024 Protocol Hardening](/en/newsletters/2026-01-28-newsletter/#january-2024-protocol-hardening)

**Ver también:**
- [NIP-44: Encrypted Payloads](/es/topics/nip-44/)
- [NIP-57: Lightning Zaps](/es/topics/nip-57/)
