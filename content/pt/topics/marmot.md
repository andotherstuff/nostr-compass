---
title: "Protocolo Marmot"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
translationOf: /en/topics/marmot.md
translationDate: 2025-12-26
---

Marmot é um protocolo para mensagens de grupo criptografadas de ponta a ponta construído sobre Nostr, usando o padrão Message Layer Security (MLS) para forward secrecy e segurança pós-comprometimento.

## Como Funciona

Marmot estende o Nostr com criptografia baseada em MLS para chats em grupo. Diferente das DMs NIP-17 que são um-para-um, Marmot lida com comunicação segura de grupo onde membros podem entrar e sair enquanto mantém garantias de criptografia.

## Recursos Principais

- Forward secrecy e segurança pós-comprometimento via MLS
- Gerenciamento de chave de grupo para membresia dinâmica
- Notificações push que preservam privacidade via MIP-05

---

**Fontes primárias:**
- [Repositório do Protocolo Marmot](https://github.com/marmot-protocol/marmot)

**Mencionado em:**
- [Newsletter #1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: Lançamentos](/pt/newsletters/2025-12-17-newsletter/#releases)

**Veja também:**
- [MIP-05: Notificações Push que Preservam Privacidade](/pt/topics/mip-05/)
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
- [NIP-59: Gift Wrap](/pt/topics/nip-59/)
