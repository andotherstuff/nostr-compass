---
title: "NIP-AR do Buzz: Artefatos de canal"
date: 2026-09-30
translationOf: /en/topics/nip-ar.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Collaboration
---

O NIP-AR é a especificação de artefatos de canal **específica do projeto** Buzz. O rótulo aqui não significa que ela tenha sido adotada pelo repositório `nostr-protocol/nips` ou por outros relays.

## Modelo de artefatos

Um artefato é um registro editável com uma identidade `d` estável, um único canal de origem em uma tag `h` e revisões com snapshots completos encadeadas por `prev`. Um relay só aceita uma edição se `prev` nomear a ponta atual. Duas revisões concorrentes, portanto, não podem se tornar ambas a próxima ponta. A implementação do Buzz usa o kind `45010` para artefatos e um marcador de kind `45011` assinado pelo relay quando um artefato sai de um canal. O canal de origem vê a remoção sem descobrir o destino a partir desse marcador.

O [merge da especificação do Buzz](https://github.com/block/buzz/pull/7791) descreve o modelo, e o [merge da implementação no relay](https://github.com/block/buzz/pull/7919) relata testes de tratamento de conflitos, consultas de histórico, movimentações e permissões de canal. Esses merges estabelecem comportamento no código-fonte do projeto, e não um padrão Nostr geral nem uma garantia de implantação pública.

---

**Fontes primárias:**
- [Merge da especificação de artefatos de canal do Buzz](https://github.com/block/buzz/pull/7791)
- [Merge da implementação de artefatos de canal do Buzz](https://github.com/block/buzz/pull/7919)

**Mencionado em:**
- [Newsletter #42: artefatos de canal do Buzz](/pt/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
