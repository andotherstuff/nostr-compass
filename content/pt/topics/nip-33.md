---
title: "NIP-33: Eventos Substituíveis Parametrizados (Eventos Endereçáveis)"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-33 originalmente definiu eventos substituíveis parametrizados, uma classe de eventos onde apenas um evento por tupla `(pubkey, kind, d-tag)` é retido pelos relays. O conceito foi desde então renomeado para "eventos endereçáveis" e incorporado ao [NIP-01](/pt/topics/nip-01/). O documento NIP-33 agora redireciona para o NIP-01 mas continua sendo uma referência comum em codebases e documentação.

## Como Funciona

Um evento endereçável usa um kind na faixa `30000-39999`. Cada evento carrega uma tag `d` cujo valor, junto com a pubkey do autor e o número do kind, forma um endereço único. Quando um relay recebe um novo evento correspondendo a uma tupla `(pubkey, kind, d-tag)` existente, ele substitui o evento mais antigo pelo mais novo (por `created_at`). Isso torna os eventos endereçáveis úteis para estado mutável: perfis, configurações, configurações de app, listagens classificadas e estruturas similares onde apenas a versão mais recente importa.

Clientes referenciam eventos endereçáveis com tags `a` no formato `<kind>:<pubkey>:<d-tag>`, opcionalmente seguido por uma dica de relay.

## Usos Comuns

- Kind `30023` artigos de formato longo
- Kind `30078` dados específicos de aplicação (usado pelo NIP-78)
- Kind `31923` eventos de calendário (NIP-52)
- Kind `31990` recomendações de handlers (NIP-89)
- Kind `30009` definições de badges (NIP-58)
- Kind `31991` configurações de execução de agentes (Notedeck Agentium)

## Relação com NIP-01

NIP-33 foi mergeado no NIP-01 como parte de um esforço de consolidação. A spec do NIP-01 agora define três categorias de retenção de eventos: eventos regulares (mantidos como estão), eventos substituíveis (um por `(pubkey, kind)`), e eventos endereçáveis (um por `(pubkey, kind, d-tag)`). NIP-33 continua sendo uma forma abreviada válida para o conceito de evento endereçável.

---

**Fontes primárias:**
- [NIP-33 (redirecionamento)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [Especificação NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) - Seção de eventos endereçáveis

**Mencionado em:**
- [Newsletter #13: Notedeck](/en/newsletters/2026-03-11-newsletter/#notedeck-adds-nip-11-relay-limits-and-agentium-features)

**Veja também:**
- [NIP-01: Basic Protocol](/pt/topics/nip-01/)
