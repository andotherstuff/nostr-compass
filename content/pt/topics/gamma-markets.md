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

Gamma Markets é um conjunto de convenções de e-commerce construídas diretamente sobre as listas de classificados [NIP-99](/pt/topics/nip-99/), desenvolvidas colaborativamente por um grupo de trabalho de desenvolvedores de marketplaces Nostr: as equipes por trás de Shopstr, Cypher, Plebeian Market e Conduit Market. Preenche as convenções de frete, fluxo de pedidos, coleções e avaliações que NIP-99 deixa indefinidas.

## Como funciona

Gamma Markets adiciona cinco kinds de eventos em torno do evento de lista kind `30402` existente de NIP-99, sem alterar a forma desse evento:

- **Kind 30405** - coleções de produtos, agrupando múltiplas listas via tags `a`
- **Kind 30406** - opções de frete, com preços por país e regras opcionais de custo baseadas em peso ou distância
- **Kind 16** - mensagens de pedido: criação (type 1), requisições de pagamento (type 2), atualizações de status (type 3) e atualizações de frete (type 4)
- **Kind 14** - comunicação geral entre comprador e comerciante
- **Kind 17** - recibos de pagamento
- **Kind 31555** - avaliações de produtos, endereçadas a um pubkey de vendedor e tag `d` de lista específicos

As preferências de pagamento de um comerciante são declaradas via uma tag `payment_preference` em seus metadados de perfil kind `0`, e clientes descobrem aplicativos compatíveis através de recomendações de aplicativos [NIP-89](/pt/topics/nip-89/). A comunicação de pedidos se constrói sobre mensagens privadas [NIP-17](/pt/topics/nip-17/), sem um esquema de criptografia novo próprio.

A escolha de design definitória da especificação é que nada herda em cascata: uma lista que pertence a uma coleção, ou que usa uma opção de frete, a referencia explicitamente com uma tag `a` em vez de herdar automaticamente a configuração de seu pai. Essa é uma divergência deliberada do modelo de estande mais antigo de [NIP-15](/pt/topics/nip-15/), onde um produto herdava silenciosamente a moeda e a tabela de frete de seu estande.

### Exemplo: criação de pedido (kind 16, type 1)

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

## Por que importa

NIP-99 sozinho padroniza apenas a lista em si, um anúncio classificado assinado e endereçável. Antes de Gamma Markets, cada cliente que construía e-commerce real sobre NIP-99 inventava suas próprias convenções privadas para frete, checkout e avaliações, o que significava que dois clientes compatíveis com NIP-99 podiam renderizar corretamente uma lista mas não tinham uma forma compartilhada de completar um pedido entre eles. Gamma Markets fecha essa lacuna sem tocar o formato de lista de NIP-99, de modo que listas NIP-99 existentes permanecem válidas sem modificação.

## Implementações

- [Shopstr](https://github.com/shopstr-eng/shopstr) - marketplace Nostr, um dos quatro projetos que escreveram a especificação
- [Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) - protocolo de marketplace construindo seu próprio fluxo de estado de pedidos e checkout no mesmo espaço de design

---

**Fontes primárias:**
- [Repositório da especificação Gamma Markets](https://github.com/GammaMarkets/market-spec)
- [Extensão de caso de uso de e-commerce NIP-99, PR #1784](https://github.com/nostr-protocol/nips/pull/1784) - link mergeado no documento canônico de NIP-99 para a especificação Gamma Markets

**Mencionado em:**
- [Newsletter #31: NIP Deep Dive: NIP-99 e a extensão de comércio Gamma Markets](/pt/newsletters/2026-07-15-newsletter/#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension)

**Veja também:**
- [NIP-99: Classified Listings](/pt/topics/nip-99/)
- [NIP-15: Nostr Marketplace](/pt/topics/nip-15/)
- [NIP-17: Private Direct Messages](/pt/topics/nip-17/)
