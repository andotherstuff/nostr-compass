---
title: 'NIP-10: Encadeamento de notas de texto'
date: 2025-12-24
draft: false
categories:
- Protocol
- Social
translationOf: /en/topics/nip-10.md
translationDate: '2026-03-07'
---

NIP-10 especifica como as notas kind 1 fazem referência umas às outras para formar threads de resposta. Compreender isso é essencial para construir visualizações de conversa.

## Como funciona

Quando alguém responde a uma nota, os clientes precisam saber: Para que isso é uma resposta? Qual é a raiz da conversa? Quem deve ser notificado? O NIP-10 responde a essas perguntas por meio de `e` tags (referências de eventos) e `p` tags (menções de pubkey).

## Tags marcadas (preferencial)

Os clientes modernos usam marcadores explícitos em `e` tags:

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "Great point! I agree.",
  "sig": "b7d3f..."
}
```

O marcador `root` aponta para a nota original que iniciou o tópico. O marcador `reply` aponta para a nota específica que está sendo respondida. Se responder diretamente ao root, use apenas `root` (não é necessário `reply` tag). A distinção é importante para a renderização: o `reply` determina o recuo em uma visualização de thread, enquanto o `root` agrupa todas as respostas.

## Regras de Threading

- **Resposta direta ao root:** Um `e` tag com marcador `root`
- **Resposta a uma resposta:** Dois `e` tags, um `root` e um `reply`
- O `root` permanece constante durante toda a rosca; `reply` muda com base no que você está respondendo

## Notificações e menções

Inclua `p` tags para todos que devem ser notificados. No mínimo, tag é o autor da nota à qual você está respondendo. A convenção é incluir também todos os `p` tags do evento pai, para que todos na conversa permaneçam informados, além de quaisquer usuários que você @mencionar em seu conteúdo.

## Dicas de relay

A terceira posição em `e` e `p` tags pode conter uma URL relay onde esse evento ou conteúdo do usuário pode ser encontrado. Isso ajuda os clientes a buscar o conteúdo referenciado mesmo que não estejam conectados ao relay original.

## Notas de interoperabilidade

As primeiras implementações do Nostr inferiram o significado da posição tag em vez dos marcadores: o primeiro `e` tag era a raiz, o último era a resposta, os do meio eram as menções. Essa abordagem está obsoleta porque cria ambiguidade. Se você vir `e` tags sem marcadores, provavelmente são de clientes mais antigos. As implementações modernas devem sempre usar marcadores explícitos.

Os clientes ainda precisam analisar ambos os formatos se quiserem renderizar threads mais antigos corretamente. Na prática, a interoperabilidade do NIP-10 é, em parte, um problema de migração: os produtores deveriam emitir a marca tags, mas os leitores deveriam permanecer tolerantes com as formas posicionais mais antigas.

## Construindo visualizações de thread

Para exibir um thread, busque o evento raiz e consulte todos os eventos com um `e` tag referenciando essa raiz:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Classifique os resultados por `created_at` e use marcadores `reply` para construir a estrutura em árvore. Os eventos cujo `reply` aponta para a raiz são respostas de nível superior; eventos cujo `reply` aponta para outra resposta são respostas aninhadas.

---

**Fontes primárias:**
- [Especificação NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md)

**Mencionado em:**
- [Boletim informativo nº 2: Aprofundamento do NIP](/pt/newsletters/2025-12-24-newsletter/#nip-10-text-note-threading)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
- [NIP-18: Repostagens](/pt/topics/nip-18/)
