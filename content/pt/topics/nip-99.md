---
title: 'NIP-99: Anúncios Classificados'
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Commerce
  - Marketplaces
---

O NIP-99 define eventos endereçáveis de anúncios classificados para bens, serviços, vagas, aluguéis e outras ofertas. Ele dá aos aplicativos de marketplace um modelo de evento mais simples do que a especificação de marketplace mais antiga do [NIP-15](/pt/topics/nip-15/), razão pela qual muitos clientes de comércio atuais usam o NIP-99.

## Como funciona

Listagens ativas usam o kind `30402`, enquanto rascunhos ou listagens inativas usam o kind `30403`. A pubkey do autor é o vendedor ou criador da oferta. O campo `content` carrega a descrição legível por humanos em Markdown, e as tags guardam campos estruturados como título, resumo, preço, localização e status.

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

O evento é endereçável, então um vendedor pode atualizar a listagem mantendo a mesma tupla de identidade de pubkey, kind e tag `d`. Isso torna revisões de listagem mais limpas para clientes do que publicar uma nota imutável totalmente nova a cada mudança de preço ou status.

## Por que isso importa

A força do NIP-99 é deixar espaço para diferentes designs de marketplace, ao mesmo tempo em que padroniza a forma básica da listagem. Um cliente pode focar em classificados locais, outro em assinaturas e outro em catálogos globais de produtos. Se todos concordarem com a estrutura do evento, vendedores podem publicar uma vez e ainda assim obter alguma visibilidade entre clientes.

Essa flexibilidade também explica por que projetos atuais de marketplace o favorecem. A especificação é estruturada o suficiente para suportar busca e exibição, mas não força cada app a um único fluxo de escrow, envio ou pagamento.

## Notas de implementação

- Tags `price` podem descrever pagamentos únicos ou recorrentes ao adicionar um campo opcional de frequência.
- Tags `t` funcionam como categorias ou palavras-chave de busca.
- Tags `image` permitem que clientes renderizem visualizações de galeria sem fazer parsing do corpo Markdown.
- Uma listagem pode vincular eventos ou documentos relacionados com tags `e` ou `a` quando um marketplace quer um contexto de produto mais rico.

## Implementações

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Marketplace Nostr usando listagens NIP-99 com endpoints MCP voltados a agentes
- [Milk Market](https://github.com/shopstr-eng/milk-market) - Marketplace de alimentos construído sobre a mesma camada de listagens com opções mistas de pagamento

---

**Fontes primárias:**
- [Especificação do NIP-99](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - Endpoints de comércio MCP sobre listagens NIP-99
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - Assinaturas e checkout multi-merchant sobre listagens de marketplace

**Mencionado em:**
- [Newsletter #13: Shopstr e Milk Market](/pt/newsletters/2026-03-11-newsletter/)

**Veja também:**
- [NIP-15: Ofertas de Marketplace](/pt/topics/nip-15/)
- [NIP-47: Nostr Wallet Connect](/pt/topics/nip-47/)
- [NIP-60: Carteira Cashu](/pt/topics/nip-60/)
