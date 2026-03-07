---
title: 'NIP-69: Negociação ponto a ponto'
date: 2025-12-17
draft: false
categories:
- Trading
- Protocol
translationOf: /en/topics/nip-69.md
translationDate: '2026-03-07'
---

O NIP-69 define um protocolo para negociação peer-to-peer através do Nostr, criando uma carteira de pedidos unificada em múltiplas plataformas, em vez de pools de liquidez fragmentados.

## Como funciona

O NIP-69 usa eventos endereçáveis ​​kind 38383 para ordens de compra e venda. O formato endereçável é importante porque uma ordem pode passar por vários estados ao longo do tempo, mantendo a mesma identidade lógica através do seu `d` tag.

## Estrutura do pedido

Os pedidos usam tags para especificar parâmetros de negociação:

- `d` - ID do pedido
- `k` - Tipo de pedido (compra/venda)
- `f` - Moeda Fiat (código ISO 4217)
- `amt` - Quantidade de Bitcoin em satoshis
- `fa` - Valor Fiat
- `pm` - Métodos de pagamento aceitos
- `premium` - Percentual de prêmio/desconto de preço
- `network` - Rede Bitcoin (mainnet, testnet, signet, regtest)
- `layer` - Camada de liquidação (onchain, relâmpago, líquido)
- `expiration` - Quando o pedido expira

## Ciclo de vida do pedido

Os pedidos progridem através dos status:
- `pending` - Aberto e disponível para correspondência
- `in-progress` - Negociação iniciada com contraparte
- `success` - Negociação concluída
- `canceled` - Retirado pelo fabricante
- `expired` - Tempo de expiração passado

A especificação distingue dois limites de tempo. `expires_at` marca quando uma ordem pendente deve parar de ser considerada aberta, enquanto `expiration` fornece aos relays um carimbo de data e hora que eles podem usar com [NIP-40](/pt/topics/nip-40/) para remover totalmente eventos de ordem obsoleta.

## Por que é importante

NIP-69 é um jogo de interoperabilidade. Mostro, lnp2pBot, RoboSats, Peach e outros sistemas de negociação P2P podem expor ordens em um formato de evento compartilhado em vez de manter a liquidez presa em aplicativos separados.

O `g` tag opcional também torna possível a negociação local e presencial sem alterar o restante do esquema do pedido. Isso é útil porque as negociações locais em dinheiro precisam de filtragem geográfica, enquanto as negociações relâmpago online não.

## Segurança e Confiança

O `bond` tag especifica uma caução que ambas as partes devem pagar, proporcionando proteção contra abandono ou fraude.

Isso não elimina o risco de contraparte. Disputas de pagamento, fraude fiduciária, reputação e regras de custódia ainda residem na camada de aplicação. O NIP-69 padroniza a publicação de pedidos, não a resolução de disputas.

---

**Fontes primárias:**
- [Especificação NIP-69](https://github.com/nostr-protocol/nips/blob/master/69.md)
- [Especificação do protocolo Mostro](https://mostro.network/protocol/)

**Mencionado em:**
- [Boletim informativo nº 1: atualizações do NIP](/pt/newsletters/2025-12-17-newsletter/#nip-updates)
- [Boletim Informativo nº 1: Lançamentos](/pt/newsletters/2025-12-17-newsletter/#releases)
- [Boletim informativo nº 2: Notícias](/pt/newsletters/2025-12-24-newsletter/#news)

**Veja também:**
- [NIP-40: Carimbo de data e hora de expiração](/pt/topics/nip-40/)
