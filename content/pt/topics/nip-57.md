---
title: "NIP-57: Zaps"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
  - Social
translationOf: /en/topics/nip-57.md
translationDate: 2025-12-26
---

NIP-57 define zaps, uma forma de enviar pagamentos Lightning para usuários e conteúdo Nostr com prova criptográfica de que o pagamento ocorreu.

## Como Funciona

1. Cliente busca o endereço Lightning do destinatário do perfil kind 0
2. Cliente solicita uma invoice do servidor LNURL do destinatário, incluindo um evento de solicitação de zap
3. Usuário paga a invoice
4. Servidor LNURL publica um recibo de zap kind 9735 nos relays Nostr
5. Clientes exibem o zap no conteúdo do destinatário

## Solicitação de Zap (kind 9734)

A solicitação de zap é um evento assinado que prova quem enviou o zap e para qual conteúdo. Inclui:
- Tag `p` com pubkey do destinatário
- Tag `e` com evento sendo zapeado (opcional)
- Tag `amount` em millisatoshis
- Tag `relays` listando onde publicar o recibo

## Recibo de Zap (kind 9735)

Publicado pelo servidor LNURL após confirmação do pagamento. Contém:
- A solicitação de zap original em uma tag `description`
- Tag `bolt11` com a invoice paga
- Tag `preimage` provando pagamento

---

**Fontes primárias:**
- [Especificação NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Mencionado em:**
- [Newsletter #1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Notícias](/pt/newsletters/2025-12-24-newsletter/#news)

**Veja também:**
- [NIP-47: Nostr Wallet Connect](/pt/topics/nip-47/)
