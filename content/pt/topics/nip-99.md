---
title: "NIP-99: Listagens Classificadas"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Commerce
  - Marketplaces
---

NIP-99 define eventos endereçáveis de listagem classificada para bens, serviços, empregos, aluguéis e outras ofertas. Ele dá aos apps de marketplace um modelo de evento mais simples que a spec de marketplace mais antiga [NIP-15](/pt/topics/nip-15/), que é por que muitos clientes de comércio atuais constroem sobre NIP-99 em vez dela.

## Como Funciona

Listagens ativas usam kind `30402`, enquanto rascunhos ou listagens inativas usam kind `30403`. A pubkey do autor é o vendedor ou criador da oferta. O campo `content` carrega a descrição legível por humanos em Markdown, e as tags contêm campos estruturados como título, resumo, preço, localização e status.

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

O evento é endereçável, então um vendedor pode atualizar a listagem mantendo a mesma tupla de identidade de pubkey, kind e tag `d`. Isso torna revisões de listagem mais limpas para clientes do que publicar uma nova nota imutável para cada mudança de preço ou status.

## Por Que Importa

A força do NIP-99 é que ele deixa espaço para diferentes designs de marketplace enquanto ainda padroniza o formato central da listagem. Um cliente pode focar em classificados locais, outro em assinaturas, e outro em catálogos de produtos globais. Se todos concordarem na estrutura do evento, vendedores podem publicar uma vez e ainda ter alguma visibilidade entre clientes.

Essa flexibilidade também explica por que projetos de marketplace atuais o favorecem. A spec é estruturada o suficiente para suportar busca e exibição, mas não força cada app em um único fluxo de escrow, envio ou pagamento.

## Notas de Implementação

- Tags `price` podem descrever pagamentos únicos ou recorrentes adicionando um campo opcional de frequência.
- Tags `t` funcionam como categorias ou palavras-chave de busca.
- Tags `image` permitem que clientes renderizem visualizações de galeria sem fazer parsing do corpo Markdown.
- Uma listagem pode vincular a eventos ou documentos relacionados com tags `e` ou `a` quando um marketplace quer contexto de produto mais rico.

## Implementações

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Marketplace Nostr usando listagens NIP-99 com endpoints MCP voltados para agentes
- [Milk Market](https://github.com/shopstr-eng/milk-market) - Marketplace de alimentos construído sobre a mesma camada de listagem com opções de pagamento mistas

---

**Fontes primárias:**
- [Especificação NIP-99](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - Endpoints de comércio MCP sobre listagens NIP-99
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - Assinatura e checkout multi-merchant sobre listagens de marketplace

**Mencionado em:**
- [Newsletter #13: Shopstr e Milk Market abrem superfícies de comércio MCP](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)

**Veja também:**
- [NIP-15: Marketplace Offers](/pt/topics/nip-15/)
- [NIP-47: Nostr Wallet Connect](/pt/topics/nip-47/)
- [NIP-60: Cashu Wallet](/pt/topics/nip-60/)
