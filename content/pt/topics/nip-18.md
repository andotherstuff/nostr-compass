---
title: "NIP-18: Reposts"
date: 2025-12-17
draft: false
categories:
  - Social
  - Protocol
translationOf: /en/topics/nip-18.md
translationDate: 2025-12-26
---

NIP-18 define como repostar eventos, similar a retweets em outras plataformas.

## Estrutura

Um repost é um evento kind 6 (para notas kind 1) ou kind 16 (repost genérico) contendo:
- Tag `e` referenciando o evento repostado
- Tag `p` referenciando o autor original
- Opcionalmente, o evento original completo no campo `content`

## Mudanças Recentes

Suporte melhorado para repostar eventos substituíveis com suporte a tag `a`. Isso permite que reposts de eventos endereçáveis (kinds 30000-39999) os referenciem por seu endereço em vez de um ID de evento específico.

---

**Fontes primárias:**
- [Especificação NIP-18](https://github.com/nostr-protocol/nips/blob/master/18.md)

**Mencionado em:**
- [Newsletter #1: Atualizações de NIP](/pt/newsletters/2025-12-17-newsletter/#nip-updates)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
