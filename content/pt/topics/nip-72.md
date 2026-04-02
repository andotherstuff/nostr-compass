---
title: "NIP-72: Comunidades Moderadas"
date: 2026-03-25
translationOf: /en/topics/nip-72.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Communities
---

NIP-72 define comunidades moderadas no Nostr. Comunidades fornecem uma forma de organizar posts em torno de um tópico ou grupo compartilhado, com moderadores que aprovam conteúdo antes que ele se torne visível para os membros.

## Como Funciona

Uma comunidade é definida por um evento kind 34550 publicado por seu criador. Este evento contém o nome da comunidade, descrição, regras e uma lista de pubkeys de moderadores. O evento usa um formato de evento substituível (faixa de kinds 30000-39999), então a definição da comunidade pode ser atualizada ao longo do tempo.

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

Usuários enviam posts para uma comunidade marcando seus eventos com uma tag `a` apontando para a definição da comunidade. Esses posts ainda não são visíveis para os leitores da comunidade. Um moderador revisa a submissão e, se aprovada, publica um evento de aprovação kind 4549 que encapsula o post original. Clientes que exibem a comunidade mostram apenas posts que têm um evento de aprovação correspondente de um moderador reconhecido.

Esse modelo de aprovação significa que comunidades são filtradas na leitura, não restritas na escrita. Qualquer pessoa pode submeter um post, mas apenas posts aprovados aparecem no feed da comunidade. Moderadores atuam como curadores em vez de guardiões dos dados subjacentes.

## Considerações

Como eventos de aprovação são eventos Nostr separados, decisões de moderação são transparentes e auditáveis. Um post rejeitado por uma comunidade ainda pode ser aprovado por outra. O mesmo conteúdo pode existir em múltiplas comunidades com moderação independente.

Suporte de relay importa para a funcionalidade de comunidades. Clientes precisam consultar tanto a definição da comunidade quanto os eventos de aprovação, o que requer relays que indexem esses kinds de evento de forma eficiente.

---

**Fontes primárias:**
- [Especificação NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md) - Comunidades Moderadas

**Mencionado em:**
- [Newsletter #15](/pt/newsletters/2026-03-25-newsletter/)
