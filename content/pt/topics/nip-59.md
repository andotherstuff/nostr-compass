---
title: "NIP-59: Gift Wrap"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Protocol
translationOf: /en/topics/nip-59.md
translationDate: 2025-12-26
---

NIP-59 define gift wrapping, uma técnica para esconder o remetente de um evento envolvendo-o em camadas de criptografia com uma identidade descartável.

## Estrutura

Um evento gift-wrapped tem três camadas:

1. **Rumor** - O conteúdo original do evento não assinado
2. **Selo** (kind 13) - O rumor criptografado para o destinatário, assinado pelo remetente real
3. **Gift Wrap** (kind 1059) - O selo criptografado para o destinatário, assinado por uma chave descartável aleatória

A camada externa usa um par de chaves aleatório gerado apenas para esta mensagem, então observadores não podem vinculá-la ao remetente.

## Por que Três Camadas?

- O **rumor** contém o conteúdo real
- O **selo** prova o remetente real (visível apenas para o destinatário)
- O **gift wrap** esconde o remetente de relays e observadores

## Suporte a Deleção

Eventos gift wrap agora podem ser deletados via solicitações de deleção NIP-09/NIP-62. Isso foi adicionado para permitir que usuários removam mensagens envolvidas dos relays.

## Casos de Uso

- Mensagens diretas privadas (NIP-17)
- Denúncias anônimas ou whistleblowing
- Qualquer cenário onde privacidade do remetente é importante

---

**Fontes primárias:**
- [Especificação NIP-59](https://github.com/nostr-protocol/nips/blob/master/59.md)

**Mencionado em:**
- [Newsletter #1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: Atualizações de NIP](/pt/newsletters/2025-12-17-newsletter/#nip-updates)

**Veja também:**
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
