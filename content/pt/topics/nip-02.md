---
title: "NIP-02: Lista de Seguidos"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
translationOf: /en/topics/nip-02.md
translationDate: 2025-12-26
---

NIP-02 define eventos kind 3, que armazenam sua lista de seguidos. Este mecanismo simples alimenta o grafo social que torna os timelines possíveis.

## Estrutura

Um evento kind 3 contém tags `p` listando as pubkeys seguidas:

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Cada tag `p` tem quatro posições: o nome da tag, a pubkey seguida (hex), uma URL de relay opcional como dica, e um "petname" opcional (um apelido local). A dica de relay informa a outros clientes onde encontrar os eventos daquele usuário. O petname permite que você atribua nomes memoráveis aos contatos sem depender dos nomes de exibição declarados por eles.

## Comportamento Substituível

O kind 3 está na faixa substituível (0, 3, 10000-19999), então os relays mantêm apenas a versão mais recente por pubkey. Quando você segue alguém novo, seu cliente publica um novo kind 3 completo contendo todos os seus seguidos mais o novo. Isso significa que as listas de seguidos devem ser completas a cada vez; você não pode publicar atualizações incrementais.

## Construindo Timelines

Para construir um feed inicial, os clientes buscam o kind 3 do usuário, extraem todas as pubkeys das tags `p`, e então assinam eventos kind 1 daqueles autores:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

O relay retorna as notas correspondentes, e o cliente as renderiza. As dicas de relay no kind 3 ajudam os clientes a saber quais relays consultar para cada usuário seguido.

## Petnames e Identidade

O campo petname permite um esquema de nomenclatura descentralizado. Em vez de confiar em qualquer nome que um usuário declare em seu perfil, você pode atribuir seu próprio rótulo. Um cliente pode exibir "alice (Minha Irmã)" onde "alice" vem do perfil kind 0 dela e "Minha Irmã" é seu petname. Isso fornece contexto que nomes de usuário globais não podem fornecer.

## Considerações Práticas

Como os eventos kind 3 são substituíveis e devem ser completos, os clientes devem preservar tags desconhecidas ao atualizar. Se outro cliente adicionou tags que seu cliente não entende, sobrescrever cegamente perderia esses dados. Adicione novos seguidos em vez de reconstruir do zero.

---

**Fontes primárias:**
- [Especificação NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md)

**Mencionado em:**
- [Newsletter #2: Análise Profunda de NIP](/pt/newsletters/2025-12-24-newsletter/#nip-02-follow-list)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
