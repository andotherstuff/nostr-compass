---
title: 'NIP-57: Zaps'
date: 2025-12-17
draft: false
categories:
- Wallet
- Lightning
- Social
translationOf: /en/topics/nip-57.md
translationDate: '2026-03-07'
---

O NIP-57 define zaps, uma forma de anexar pagamentos Lightning a identidades e conteúdo Nostr. Ele padroniza tanto a solicitação de fatura habilitada para zap quanto o evento de recebimento que as carteiras publicam após o pagamento.

## Como funciona

1. O cliente descobre o endpoint LNURL do destinatário a partir dos metadados do perfil ou de um `zap` tag no evento de destino.
2. O cliente envia uma solicitação zap kind `9734` assinada para o retorno de chamada LNURL do destinatário, não para relays.
3. O usuário paga a fatura.
4. O servidor de carteira do destinatário publica um recibo zap kind `9735` para os relays listados na solicitação zap.
5. Os clientes validam e exibem o zap.

## Solicitação de Zap (kind 9734)

A solicitação zap é um evento assinado que identifica o pagador e o alvo pretendido. Geralmente inclui:

- `p` tag com destinatário pubkey
- `e` tag com evento sendo zapeado (opcional)
- `amount` tag em milisatoshis
- `relays` tag listagem onde publicar o recibo

O conteúdo endereçável pode usar um `a` tag em vez de, ou junto com, um `e` tag. O `k` tag opcional registra o destino kind.

## Recibo Zap (kind 9735)

Publicado pelo servidor da carteira do destinatário após a confirmação do pagamento. Ele contém:

- A solicitação original do zap em um `description` tag
- `bolt11` tag com a fatura paga
- `preimage` tag comprovando pagamento

Os clientes devem validar o recibo com o LNURL `nostrPubkey` do destinatário, o valor da fatura e a solicitação zap original. Um recibo sem essa validação é apenas uma reclamação.

## Confiança e compensações

Os Zaps são úteis porque tornam os pagamentos visíveis dentro do gráfico social, mas o recibo ainda é criado pela infraestrutura da carteira do destinatário. A própria especificação observa que um recibo zap não é um proof universal de pagamento. É melhor entendido como uma declaração assinada na carteira de que uma fatura vinculada a uma solicitação zap foi paga.

---

**Fontes primárias:**
- [Especificação NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Mencionado em:**
- [Boletim informativo nº 1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)
- [Boletim informativo nº 2: Notícias](/pt/newsletters/2025-12-24-newsletter/#news)
- [Boletim informativo nº 3: Mudanças notáveis no código](/pt/newsletters/2025-12-31-newsletter/#amethyst-android)
- [Boletim informativo nº 9: Atualizações do NIP](/pt/newsletters/2026-02-11-newsletter/#nip-updates)

**Veja também:**
- [NIP-47: Nostr Wallet Connect](/pt/topics/nip-47/)
