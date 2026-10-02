---
title: "NIP-28: Chat público"
date: 2026-09-30
translationOf: /en/topics/nip-28.md
translationDate: 2026-10-02
draft: false
categories:
  - NIPs
  - Social
---

O NIP-28 descreve canais de chat públicos, mensagens de canal e moderação no lado do cliente como events Nostr. A especificação atual está marcada como **draft** e **unrecommended** e orienta os implementadores a usar o NIP-29 para os grupos atuais baseados em relays.

## Modelo de events

O kind `40` cria um canal; o kind `41` atualiza seus metadados; o kind `42` transporta uma mensagem. Os kinds `43` e `44` permitem que um usuário oculte uma mensagem ou silencie outro usuário em seu cliente. As tags das mensagens se referem ao event de criação do canal e podem identificar a mensagem que está sendo respondida. Os relays não precisam aplicar essas escolhas de ocultar e silenciar feitas no lado do cliente.

A [mudança na especificação de setembro de 2022](https://github.com/nostr-protocol/nips/commit/3423a6dfb) tornou uma sala de chat pública um assunto compartilhado do protocolo. Esse papel histórico continua útil para entender o protocolo, mesmo que a [especificação atual](https://github.com/nostr-protocol/nips/blob/master/28.md) recomende um caminho diferente para novas implementações.

---

**Fontes primárias:**
- [Especificação e status atual do NIP-28](https://github.com/nostr-protocol/nips/blob/master/28.md)
- [Mudança de chat público de setembro de 2022](https://github.com/nostr-protocol/nips/commit/3423a6dfb)

**Mencionado em:**
- [Newsletter #42: setembro de 2022](/pt/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)

**Veja também:**
- [NIP-29: Grupos baseados em relays](/pt/topics/nip-29/)
