---
title: "NIP-37: Draft Wraps"
date: 2026-07-01
draft: false
translationOf: /en/topics/nip-37.md
translationDate: 2026-07-01
categories:
  - NIP
  - Drafts
  - Privacy
---

NIP-37 define um evento de armazenamento criptografado para eventos rascunho não assinados de qualquer kind. Um usuário compondo um artigo longo, um evento de calendário futuro ou uma mensagem que talvez queira enviar depois pode armazenar o rascunho em relays sob um evento kind `31234`, criptografado para sua própria chave com [NIP-44](/pt/topics/nip-44/). O rascunho é recuperável a partir de qualquer cliente que possua a chave do usuário, e o mesmo NIP define um evento de lista `kind:10013` separado que nomeia os relays nos quais o usuário deseja que seus rascunhos privados sejam armazenados.

## Como funciona

Um draft wrap é um evento replaceable parametrizado de kind `31234`. O evento de rascunho não assinado é serializado em JSON, criptografado com NIP-44 para a chave pública do próprio signer e colocado em `.content`. Uma tag `k` declara o kind do rascunho para que um cliente possa agrupar rascunhos por tipo de evento. Uma tag `d` carrega o identificador do rascunho para que o wrap possa ser substituído conforme o rascunho evolui, e uma tag `expiration` NIP-40 é recomendada para que rascunhos antigos expirem automaticamente.

```json
{
  "kind": 31234,
  "tags": [
    ["d", "<identifier>"],
    ["k", "<kind of the draft event>"],
    ["expiration", "<unix-timestamp>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

Um campo `.content` em branco sinaliza que o rascunho foi excluído.

## Checkpoints

O kind `1234` define checkpoints pertencentes a um evento pai `kind:31234`. Checkpoints carregam uma tag `a` apontando de volta para o rascunho pai e permitem que um cliente armazene o histórico de revisão junto com o rascunho mais recente.

```json
{
  "kind": 1234,
  "tags": [
    ["a", "31234:<pubkey>:<identifier>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

## Lista de Relays para Conteúdo Privado (kind 10013)

O kind `10013` é um evento replaceable cujas tags listam os relays nos quais o usuário deseja armazenar conteúdo privado, incluindo draft wraps. Clientes que publicam kind `31234` DEVEM publicar nos relays listados no evento kind `10013` do usuário. Isso separa o conjunto de relays usado para publicação pública (NIP-65) do conjunto de relays usado para armazenamento de conteúdo privado, permitindo que um usuário fixe rascunhos privados em um pequeno conjunto de relays confiáveis sem expor esse conjunto em sua outbox pública.

## Implementações

- [Notedeck](https://github.com/damus-io/notedeck) - armazena relays de sincronização privada como uma lista kind-10013 (adicionado em 2026-06)

---

**Fontes primárias:**
- [Especificação NIP-37](https://github.com/nostr-protocol/nips/blob/master/37.md)
- [Commit do Notedeck que armazena relays de sincronização privada como kind-10013](https://github.com/damus-io/notedeck) - Equipe do Damus adota a especificação para gerenciamento de relays de sincronização no desktop

**Mencionado em:**
- [Newsletter #29: Notedeck](/pt/newsletters/2026-07-01-newsletter/#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments)

**Veja também:**
- [NIP-44: Criptografia Versionada](/pt/topics/nip-44/)
- [NIP-65: Metadados de Lista de Relays](/pt/topics/nip-65/)
