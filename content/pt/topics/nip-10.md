---
title: "NIP-10: Encadeamento de Notas de Texto"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
translationOf: /en/topics/nip-10.md
translationDate: 2025-12-26
---

NIP-10 especifica como notas kind 1 referenciam umas às outras para formar threads de respostas. Entender isso é essencial para construir visualizações de conversas.

## O Problema

Quando alguém responde a uma nota, os clientes precisam saber: A que isso é uma resposta? Qual é a raiz da conversa? Quem deve ser notificado? NIP-10 responde essas perguntas através de tags `e` (referências de eventos) e tags `p` (menções de pubkey).

## Tags Marcadas (Preferido)

Clientes modernos usam marcadores explícitos nas tags `e`:

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
  "content": "Otimo ponto! Eu concordo.",
  "sig": "b7d3f..."
}
```

O marcador `root` aponta para a nota original que iniciou o thread. O marcador `reply` aponta para a nota específica sendo respondida. Se respondendo diretamente à raiz, use apenas `root` (nenhuma tag `reply` é necessária). A distinção importa para renderização: o `reply` determina a indentação em uma visualização de thread, enquanto `root` agrupa todas as respostas.

## Regras de Encadeamento

- **Resposta direta a raiz:** Uma tag `e` com marcador `root`
- **Resposta a uma resposta:** Duas tags `e`, uma `root` e uma `reply`
- O `root` permanece constante durante todo o thread; `reply` muda baseado no que você está respondendo

## Tags de Pubkey para Notificações

Inclua tags `p` para todos que devem ser notificados. No mínimo, marque o autor da nota que você está respondendo. A convenção é também incluir todas as tags `p` do evento pai (para que todos na conversa permaneçam informados), além de quaisquer usuários que você @mencione em seu conteúdo.

## Dicas de Relay

A terceira posição nas tags `e` e `p` pode conter uma URL de relay onde aquele evento ou conteúdo do usuário pode ser encontrado. Isso ajuda os clientes a buscar o conteúdo referenciado mesmo se não estiverem conectados ao relay original.

## Tags Posicionais Obsoletas

Implementações antigas do Nostr inferiam significado da posição da tag em vez de marcadores: a primeira tag `e` era raiz, a última era resposta, as do meio eram menções. Esta abordagem está obsoleta porque cria ambiguidade. Se você vir tags `e` sem marcadores, elas provavelmente são de clientes antigos. Implementações modernas devem sempre usar marcadores explícitos.

## Construindo Visualizações de Thread

Para exibir um thread, busque o evento raiz, depois consulte todos os eventos com uma tag `e` referenciando aquela raiz:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Ordene os resultados por `created_at` e use marcadores `reply` para construir a estrutura em árvore. Eventos cujo `reply` aponta para a raiz são respostas de nível superior; eventos cujo `reply` aponta para outra resposta são respostas aninhadas.

---

**Fontes primárias:**
- [Especificação NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md)

**Mencionado em:**
- [Newsletter #2: Análise Profunda de NIP](/pt/newsletters/2025-12-24-newsletter/#nip-10-text-note-threading)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
