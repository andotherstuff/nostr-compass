---
title: 'NIP-75: Metas de zap'
date: 2026-04-22
draft: false
categories:
  - NIPs
translationOf: /en/topics/nip-75.md
translationDate: 2026-04-22
---

NIP-75 define um evento de meta de arrecadação para o qual usuários podem enviar zaps. Uma meta declara um valor alvo em millisatoshis e uma lista de relays onde os recibos de zap dessa meta serão contabilizados. Qualquer zap [NIP-57](/pt/topics/nip-57/) que referencie o evento da meta conta para o progresso dela.

## Como funciona

Uma meta de zap é um evento `kind:9041`. O `.content` é uma descrição legível por humanos. As tags obrigatórias são `amount`, que define a meta em millisats, e `relays`, que define a lista de relays usada para contabilizar os recibos de zap. Tags opcionais incluem `closed_at`, para encerrar a contagem em um timestamp específico, `image` e `summary`. A meta também pode incluir uma tag `r` ou `a` apontando para uma URL externa ou para um evento endereçável, e pode carregar várias pubkeys beneficiárias por meio de tags de zap split emprestadas do apêndice G da NIP-57.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1776500000,
  "kind": 9041,
  "tags": [
    ["relays", "wss://alicerelay.example.com", "wss://bobrelay.example.com"],
    ["amount", "210000"],
    ["image", "<image url>"],
    ["summary", "Nostrasia travel expenses"]
  ],
  "content": "Nostrasia travel expenses",
  "sig": "<128-char hex>"
}
```

Clientes associam um zap a uma meta incluindo uma tag `e` apontando para o evento da meta dentro do request de zap. O progresso da meta é a soma dos valores dos recibos de zap correspondentes nos relays que a meta especificou. Quando `closed_at` está definido, recibos de zap publicados após esse timestamp não contam.

## Implementações

- [Amethyst](https://github.com/vitorpamplona/amethyst) agora renderiza barras de progresso de metas e botões de zap com um toque em cabeçalhos de live stream via [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469), que conecta NIP-75 à tela de Live Activities da NIP-53.

---

**Fontes primárias:**
- [Especificação NIP-75](https://github.com/nostr-protocol/nips/blob/master/75.md)
- [Amethyst PR #2469: top zappers e cabeçalho de meta em live stream](https://github.com/vitorpamplona/amethyst/pull/2469)

**Mencionado em:**
- [Newsletter #19: metas de zap em live streams no Amethyst](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NIP Deep Dive sobre NIP-57](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-57: Lightning Zaps](/pt/topics/nip-57/)
- [NIP-53: Atividades ao vivo](/pt/topics/nip-53/)
