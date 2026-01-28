---
title: "NIP-15: Marketplace Nostr"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15 define um protocolo para marketplaces descentralizados no Nostr, permitindo que comerciantes listem produtos e compradores façam compras usando Bitcoin e Lightning.

## Como Funciona

### Lojas de Comerciantes (Kind 30017)

Comerciantes criam lojas como eventos endereçáveis:

```json
{
  "kind": 30017,
  "tags": [
    ["d", "my-stall"],
    ["name", "Eletrônicos do Bob"],
    ["description", "Eletrônicos usados de qualidade"],
    ["currency", "sat"],
    ["shipping", "{...opções de envio...}"]
  ]
}
```

### Produtos (Kind 30018)

Produtos são listados dentro de lojas:

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

## Fluxo de Compra

1. Comprador navega produtos em múltiplas lojas
2. Comprador envia mensagem de pedido criptografada para o comerciante
3. Comerciante responde com invoice Lightning
4. Comprador paga o invoice
5. Comerciante envia o produto

## Recursos Principais

- **Descentralizado**: Sem operador central de marketplace
- **Interoperável**: Qualquer cliente NIP-15 pode navegar qualquer comerciante
- **Privado**: Pedidos são criptografados entre comprador e vendedor
- **Nativo do Bitcoin**: Pagamentos Lightning integrados

## Implementações

- **Plebeian Market** - Marketplace NIP-15 completo
- **Shopstr** - Comércio Bitcoin sem permissão
- **Amethyst** - Listagens de produtos integradas no feed social

## Relacionados

- [NIP-44](/pt/topics/nip-44/) - Mensagens criptografadas para pedidos
- [NIP-57](/pt/topics/nip-57/) - Zaps Lightning
