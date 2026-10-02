---
title: "NIP-26: Assinatura delegada de events"
date: 2026-09-30
translationOf: /en/topics/nip-26.md
translationDate: 2026-10-02
draft: false
categories:
  - NIPs
  - Identity
---

O NIP-26 documenta uma forma de uma chave Nostr autorizar outra chave a assinar um conjunto limitado de events. Sua especificação atual está marcada como **draft** e **unrecommended**, então ela registra um design anterior, e não um conselho para novas integrações.

## Como funciona

A chave da conta assina um token de delegação que nomeia a chave delegada e as condições. As condições podem restringir kinds de event e horários de `created_at`. A chave delegada assina o event com sua própria chave e anexa o token em uma tag `delegation`. Quem lê precisa verificar tanto a assinatura do event quanto o token de delegação em relação a essas condições. Relays que oferecem suporte ao esquema também podem buscar por delegante.

O modelo permite que um aplicativo publique sem guardar a chave de assinatura principal da conta. Seus requisitos adicionais de validação e de busca nos relays explicam por que as implementações não podem tratar uma assinatura de event comum como prova suficiente de uma identidade delegada. A [especificação atual](https://github.com/nostr-protocol/nips/blob/master/26.md) marca explicitamente a abordagem como não recomendada.

---

**Fontes primárias:**
- [Especificação e status atual do NIP-26](https://github.com/nostr-protocol/nips/blob/master/26.md)
- [Texto de assinatura delegada de setembro de 2022](https://github.com/nostr-protocol/nips/commit/b62aa418d)

**Mencionado em:**
- [Newsletter #42: setembro de 2022](/pt/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)
