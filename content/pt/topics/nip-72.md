---
title: 'NIP-72: Comunidades moderadas'
date: 2026-03-25
draft: false
categories:
  - NIPs
  - Communities
translationOf: /en/topics/nip-72.md
translationDate: 2026-04-22
---

NIP-72 define comunidades moderadas no Nostr. Comunidades oferecem uma forma de organizar posts em torno de um tópico ou grupo compartilhado, com moderadores que aprovam conteúdo antes que ele fique visível para os membros.

## Como funciona

Uma comunidade é definida por um evento kind `34550` publicado por seu criador. Esse evento contém o nome da comunidade, descrição, regras e uma lista de pubkeys de moderadores. O evento usa um formato de evento replaceable, na faixa kind `30000-39999`, então a definição da comunidade pode ser atualizada ao longo do tempo.

```json
{
  "kind": 34550,
  "tags": [
    ["d", "example-community"],
    ["name", "Example Community"],
    ["description", "A community for discussing examples"],
    ["p", "<moderator_pubkey>", "", "moderator"],
    ["relay", "wss://relay.example.com", "moderator"]
  ],
  "content": "",
  "pubkey": "<creator_pubkey>",
  "created_at": 1742860800,
  "sig": "<signature>"
}
```

Usuários enviam posts para uma comunidade marcando seus eventos com uma tag `a` que aponta para a definição da comunidade. Esses posts ainda não ficam visíveis para leitores da comunidade. Um moderador revisa a submissão e, se aprovada, publica um evento de aprovação kind `4549` que envolve o post original. Clientes que exibem a comunidade mostram apenas posts que têm um evento de aprovação correspondente vindo de um moderador reconhecido.

Esse modelo de aprovação significa que comunidades são filtradas na leitura, não restritas na escrita. Qualquer pessoa pode enviar um post, mas apenas posts aprovados aparecem no feed da comunidade. Moderadores agem como curadores, não como gatekeepers dos dados subjacentes.

## Considerações

Como eventos de aprovação são eventos Nostr separados, decisões de moderação são transparentes e auditáveis. Um post rejeitado por uma comunidade ainda pode ser aprovado por outra. O mesmo conteúdo pode existir em múltiplas comunidades com moderação independente.

O suporte de relay importa para o funcionamento das comunidades. Clientes precisam consultar tanto a definição da comunidade quanto os eventos de aprovação, o que exige relays que indexem esses kinds de evento com eficiência.

Comparada aos grupos baseados em relay da [NIP-29](/pt/topics/nip-29/), em que o relay é a autoridade tanto para membership quanto para moderação, a NIP-72 vive em eventos Nostr comuns. Qualquer relay que carregue os kinds `34550`, `4549` e os kinds de submissão pode servir uma comunidade, e a moderação é visível e passível de fork. O tradeoff é que submissões não aprovadas só ficam ocultas na camada de renderização do cliente, então a NIP-29 continua sendo a melhor escolha quando spam precisa ficar totalmente fora do wire.

## Implementações

- [noStrudel](https://github.com/hzrd149/nostrudel) tem suporte antigo a comunidades NIP-72, incluindo uma fila de submissões pendentes para moderadores.
- [Amethyst](https://github.com/vitorpamplona/amethyst) adicionou criação e gerenciamento de comunidades como recursos de primeira classe no [PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468): criação da definição de comunidade kind `34550`, adição de moderadores e relay hints, submissão de posts com uma tag `a` e gerenciamento de aprovações pendentes via eventos kind `4549`.

---

**Fontes primárias:**
- [Especificação NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md) - comunidades moderadas
- [Amethyst PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) - criação e moderação de comunidades NIP-72

**Mencionado em:**
- [Newsletter #15](/pt/newsletters/2026-03-25-newsletter/)
- [Newsletter #19: suporte a comunidades no Amethyst](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NIP Deep Dive](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-29: Grupos baseados em relay](/pt/topics/nip-29/)
