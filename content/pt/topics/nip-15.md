---
title: 'NIP-15: Mercado Nostr'
date: 2026-01-28
draft: false
categories:
- NIP
- Commerce
- Marketplace
translationOf: /en/topics/nip-15.md
translationDate: '2026-03-07'
---

O NIP-15 define um protocolo para mercados descentralizados no Nostr, permitindo que os comerciantes listem produtos e os compradores façam compras usando Bitcoin e Lightning.

## Como funciona

### Barracas de Comerciantes (kind 30017)

Os comerciantes criam barracas como eventos endereçáveis:

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

### Produtos (kind 30018)

Os produtos estão listados nas barracas:

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

## Fluxo de compra

1. O comprador procura produtos em várias barracas
2. O comprador envia uma mensagem criptografada do pedido ao comerciante
3. O comerciante responde com uma fatura Lightning
4. O comprador paga a fatura
5. Produto de navios mercantes

## Por que é importante

- **Descentralizado**: Sem operador central de mercado
- **Interoperável**: Qualquer cliente NIP-15 pode navegar em qualquer comerciante
- **Privado**: os pedidos são criptografados entre comprador e vendedor
- **Bitcoin nativo**: pagamentos relâmpago integrados

O ganho prático é a portabilidade. Um comerciante pode publicar dados de catálogo uma vez e permitir que vários clientes os processem, em vez de ficar preso a um front-end de mercado.

## Compensações

O NIP-15 padroniza listagens, não confiança. Os compradores ainda precisam decidir se um comerciante é legítimo, se o inventário é real e como as disputas serão tratadas. O protocolo fornece estruturas de dados e fluxo de mensagens comuns, mas a reputação e o cumprimento continuam sendo problemas no nível da aplicação.

Pagamentos e remessas também são apenas parcialmente padronizados. Um cliente pode entender barracas e produtos e ainda precisar de lógica personalizada para faturas, estado do pedido ou rastreamento de entrega.

## Status de implementação

- **Mercado Plebeu** - Mercado NIP-15 completo
- **Shopstr** - Comércio Bitcoin sem permissão
- **Ametista** - Listagens de produtos integradas no feed social

---

**Fontes primárias:**
- [Especificação NIP-15](https://github.com/nostr-protocol/nips/blob/master/15.md)

**Mencionado em:**
- [Boletim informativo nº 7: Endurecimento do protocolo de janeiro de 2024](/pt/newsletters/2026-01-28-newsletter/#january-2024-protocol-hardening)

**Veja também:**
- [NIP-44: cargas criptografadas](/pt/topics/nip-44/)
- [NIP-57: Zaps relâmpagos](/pt/topics/nip-57/)
