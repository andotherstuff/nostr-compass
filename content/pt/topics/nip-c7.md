---
title: 'NIP-C7: Mensagens de chat'
date: 2026-04-15
draft: false
categories:
  - Protocol
  - Messaging
translationOf: /en/topics/nip-c7.md
translationDate: 2026-04-22
---

NIP-C7 define o kind `9` como o kind de evento para mensagens de chat. O objetivo é separar tráfego orientado a chat do tráfego geral de feed social, para que clientes possam aplicar regras diferentes de UX e moderação a cada contexto.

## Como funciona

Um evento kind `9` carrega o conteúdo da mensagem mais tags que identificam o contexto do chat. Em grupos baseados em relay da [NIP-29](/pt/topics/nip-29/), o evento inclui uma tag `h` com o ID do grupo. O encadeamento de respostas usa tags `q` que referenciam eventos anteriores.

NIP-C7 se concentra em onde esses eventos devem ser renderizados. Em vez de aparecerem em feeds globais de notas como as notas de texto kind `1`, eventos kind `9` são destinados a views orientadas a chat, onde o estado da conversa e o threading são explícitos.

## Implementações

- [Flotilla](https://gitea.coracle.social/coracle/flotilla) e [Coracle](https://github.com/coracle-social/coracle) usam kind `9` em fluxos de trabalho de chat em grupo.
- [Amethyst](https://github.com/vitorpamplona/amethyst) inclui suporte a kind `9` em sua stack de mensagens.
- [White Noise](https://github.com/marmot-protocol/whitenoise) usa threading de respostas NIP-C7 com tags `q`.

---

**Fontes primárias:**
- [Especificação NIP-C7](https://github.com/nostr-protocol/nips/blob/master/C7.md)
- [PR #2310: restringir kind 9 a views de chat](https://github.com/nostr-protocol/nips/pull/2310)

**Mencionado em:**
- [Newsletter #18: Atualizações de NIP](/en/newsletters/2026-04-15-newsletter/)

**Veja também:**
- [NIP-29: Grupos baseados em relay](/pt/topics/nip-29/)
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
