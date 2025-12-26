---
title: "NIP-A4: Mensagens Públicas"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
translationOf: /en/topics/nip-a4.md
translationDate: 2025-12-26
---

NIP-A4 define mensagens públicas (kind 24) projetadas para telas de notificação, com amplo suporte de clientes como objetivo.

## Como Funciona

Diferente de conversas encadeadas, essas mensagens não têm conceito de histórico de chat ou cadeias de mensagens. São mensagens simples e únicas destinadas a aparecer no feed de notificações de um destinatário.

## Estrutura

- Usa tags `q` (citações) em vez de tags `e` para evitar complicações de encadeamento
- Sem estado de conversa ou histórico
- Projetado para notificações públicas simples

## Casos de Uso

- Reconhecimentos públicos ou menções
- Mensagens de transmissão para um usuário
- Notificações que não precisam de encadeamento de respostas

---

**Fontes primárias:**
- [PR NIP-A4](https://github.com/nostr-protocol/nips/pull/1988)

**Mencionado em:**
- [Newsletter #2: Atualizações de NIP](/pt/newsletters/2025-12-24-newsletter/#nip-updates)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
- [NIP-10: Encadeamento de Notas de Texto](/pt/topics/nip-10/)
