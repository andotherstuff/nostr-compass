---
title: "NIP-09"
date: 2026-02-25
translationOf: /en/topics/nip-09.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Protocol
---

NIP-09 define Deleção de Evento, um mecanismo para usuários solicitarem que relays removam seus eventos previamente publicados.

## Como Funciona

Usuários publicam eventos kind 5 contendo tags `e` referenciando os IDs de evento que querem deletados. Relays que suportam NIP-09 devem parar de servir os eventos referenciados e podem deletá-los do armazenamento.

Deleção é uma solicitação, não uma garantia. Relays podem ignorar requisições de deleção, e eventos podem já ter se propagado para relays que não suportam deleção. Usuários não devem confiar no NIP-09 para remoção de conteúdo sensível à privacidade.

## Recursos Principais

- Eventos de requisição de deleção kind 5
- Referenciar eventos deletados por ID via tags e
- Campo de razão opcional para contexto de deleção
- Conformidade de relay é voluntária

---

**Fontes primárias:**
- [Especificação NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md)

**Mencionado em:**
- [Newsletter #11: Deep Dive NIP-60](/pt/newsletters/2026-02-25-newsletter/#deep-dive-de-nip-nip-60-cashu-wallet)

**Veja também:**
- [NIP-60: Cashu Wallet](/pt/topics/nip-60/)
