---
title: "NIP-69: Negociação Peer-to-Peer"
date: 2025-12-17
draft: false
categories:
  - Trading
  - Protocol
translationOf: /en/topics/nip-69.md
translationDate: 2025-12-26
---

NIP-69 define um protocolo para negociação peer-to-peer sobre Nostr, criando um livro de ordens unificado através de múltiplas plataformas em vez de pools de liquidez fragmentados.

## Tipo de Evento

- **Kind 38383** - Eventos de ordem P2P

## Estrutura da Ordem

Ordens usam tags para especificar parâmetros de negociação:

- `d` - ID da ordem
- `k` - Tipo de ordem (compra/venda)
- `f` - Moeda fiduciária (código ISO 4217)
- `amt` - Quantidade de Bitcoin em satoshis
- `fa` - Quantidade em moeda fiduciária
- `pm` - Métodos de pagamento aceitos
- `premium` - Porcentagem de prêmio/desconto no preço
- `network` - Camada de liquidação (onchain, lightning, liquid)
- `expiration` - Quando a ordem expira

## Ciclo de Vida da Ordem

Ordens progridem através de status:
- `pending` - Aberta e disponível para correspondência
- `in-progress` - Negociação iniciada com contraparte
- `success` - Negociação concluída
- `canceled` - Retirada pelo criador
- `expired` - Passou do tempo de expiração

## Segurança

A tag `bond` especifica um depósito de segurança que ambas as partes devem pagar, fornecendo proteção contra abandono ou fraude.

---

**Fontes primárias:**
- [Especificação NIP-69](https://github.com/nostr-protocol/nips/blob/master/69.md)

**Mencionado em:**
- [Newsletter #1: Atualizações de NIP](/pt/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #1: Lançamentos](/pt/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2: Notícias](/pt/newsletters/2025-12-24-newsletter/#news)
