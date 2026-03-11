---
title: 'NIP-33: Eventos Substituíveis Parametrizados (Eventos Endereçáveis)'
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Protocol
---

O NIP-33 definia originalmente eventos substituíveis parametrizados, uma classe de eventos em que apenas um evento por tupla `(pubkey, kind, d-tag)` é retido pelos relays. Desde então, o conceito foi renomeado para "eventos endereçáveis" e incorporado ao [NIP-01](/pt/topics/nip-01/). O documento do NIP-33 agora redireciona para o NIP-01, mas continua sendo uma referência comum em codebases e documentação.

## Como funciona

Um evento endereçável usa um kind na faixa `30000-39999`. Cada evento carrega uma tag `d` cujo valor, junto com a pubkey do autor e o número do kind, forma um endereço único. Quando um relay recebe um novo evento correspondente a uma tupla `(pubkey, kind, d-tag)` existente, ele substitui o evento anterior pelo mais novo (por `created_at`). Isso torna eventos endereçáveis úteis para estado mutável: perfis, configurações, configurações de aplicativo, anúncios classificados e estruturas semelhantes em que apenas a versão mais recente importa.

Clientes referenciam eventos endereçáveis com tags `a` no formato `<kind>:<pubkey>:<d-tag>`, opcionalmente seguidas por uma dica de relay.

## Usos comuns

- Kind `30023` para artigos long-form
- Kind `30078` para dados específicos de aplicativo (usado pelo NIP-78)
- Kind `31923` para eventos de calendário (NIP-52)
- Kind `31990` para recomendações de handlers (NIP-89)
- Kind `30009` para definições de badges (NIP-58)
- Kind `31991` para configurações de execução de agentes (Notedeck Agentium)

## Relação com o NIP-01

O NIP-33 foi incorporado ao NIP-01 como parte de um esforço de consolidação. A especificação do NIP-01 agora define três categorias de retenção de eventos: eventos regulares (mantidos como estão), eventos substituíveis (um por `(pubkey, kind)`) e eventos endereçáveis (um por `(pubkey, kind, d-tag)`). NIP-33 continua sendo uma abreviação válida para o conceito de evento endereçável.

---

**Fontes primárias:**
- [NIP-33 (redirecionamento)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [Especificação do NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) - Seção de eventos endereçáveis

**Mencionado em:**
- [Newsletter #13: Notedeck](/pt/newsletters/2026-03-11-newsletter/)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
