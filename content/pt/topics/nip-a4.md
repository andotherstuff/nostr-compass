---
title: 'NIP-A4: Mensagens Públicas'
date: 2025-12-24
draft: false
categories:
- Protocol
- Social
translationOf: /en/topics/nip-a4.md
translationDate: '2026-03-07'
---

O NIP-A4 define mensagens públicas (kind 24) destinadas a telas de notificação, tendo como objetivo amplo suporte ao cliente.

## Como funciona

O kind `24` é uma mensagem de texto simples assinada para um ou mais destinatários. O corpo da mensagem reside em `content` e `p` tags identifica os destinatários pretendidos. A especificação diz que os clientes devem enviar esses eventos para aos relays de caixa de entrada do destinatário [NIP-65](/pt/topics/nip-65/) e para a relay de caixa de saída do remetente.

Ao contrário das conversas encadeadas, essas mensagens não têm conceito de histórico de bate-papo, estado da sala ou raízes do tópico. Eles devem aparecer em uma superfície de notificação e serem compreensíveis por si próprios.

## Regras do Protocolo

- Usa `p` tags para identificar destinatários
- Não deve usar `e` tags para rosqueamento
- Pode usar `q` tags para citar outro evento
- Funciona melhor com [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md) expiração tags para que mensagens obsoletas de estilo de notificação desapareçam com o tempo

## Por que existe

O NIP-A4 oferece aos clientes uma primitiva de mensagem pública mais simples do que uma nota encadeada completa. Isso é útil para mensagens de estilo de menção, mensagens leves ou notificações únicas, onde a construção de uma árvore de conversa permanente acrescentaria mais complexidade do que valor.

A desvantagem é que essas mensagens são públicas. Eles são fáceis de mostrar em uma interface de notificação precisamente porque não criam um estado de sessão privada. Qualquer pessoa pode lê-los e respondê-los se os vir.

## Notas de interoperabilidade

O NIP-A4 é fácil de confundir com protocolos de mensagem direta porque tem como alvo destinatários nomeados, mas ainda é um evento público kind. Os clientes não devem apresentar kind `24` como mensagem privada ou assumir qualquer confidencialidade além da colocação de relay.

---

**Fontes primárias:**
- [Especificação NIP-A4](https://github.com/nostr-protocol/nips/blob/master/A4.md)
- [NIP-A4 PR](https://github.com/nostr-protocol/nips/pull/1988)

**Mencionado em:**
- [Boletim Informativo nº 2: Atualizações do NIP](/pt/newsletters/2025-12-24-newsletter/#nip-updates)
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
- [NIP-10: Threading de notas de texto](/pt/topics/nip-10/)
