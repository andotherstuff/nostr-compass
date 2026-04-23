---
title: 'Cashu: Protocolo de ecash'
date: 2026-01-28
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
translationOf: /en/topics/cashu.md
translationDate: 2026-04-22
---

Cashu é um protocolo de ecash Chaumiano construído sobre Bitcoin e Lightning. Usuários mantêm bearer tokens emitidos por uma mint e depois transferem esses tokens sem expor o grafo completo de pagamentos à mint.

## Como funciona

Cashu usa blind signatures para emitir tokens de ecash:

1. **Minting**: usuários depositam Bitcoin ou Lightning em uma mint e recebem tokens cegados
2. **Spending**: tokens podem ser transferidos peer-to-peer sem envolvimento da mint
3. **Redemption**: destinatários resgatam tokens na mint por Bitcoin ou Lightning

A mint assina segredos cegados, então pode verificar os tokens depois sem ver os segredos originais no momento da emissão. Isso quebra o vínculo direto entre depósito e resgate dentro da mint.

## Modelo de segurança e confiança

Cashu melhora a privacidade de pagamentos, mas continua sendo custodial. Uma mint pode recusar resgates, sair do ar ou perder os fundos de lastro.

Proofs Cashu são instrumentos bearer. Quem controla a proof pode gastá-la. Isso torna o manuseio de proofs mais próximo de dinheiro em espécie do que de um saldo de conta: backup, comprometimento do dispositivo ou vazamento de tokens em plaintext importam imediatamente.

## Integração com Nostr

Cashu se integra ao Nostr de várias formas:

- **Nutzaps**: tokens de ecash enviados como zaps com mais privacidade
- **Escrow**: escrow de pagamento baseado em HTLC para serviços como ride-sharing
- **Carteiras**: carteiras nativas de Nostr armazenam tokens Cashu criptografados em relays
- **[NIP-87](/pt/topics/nip-87/)**: descoberta e reviews de mints via Nostr
- **[TollGate](/pt/topics/tollgate/)**: protocolo de acesso à rede pay-per-use que aceita tokens de ecash Cashu para conectividade, definido em [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) a partir do [release v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)

## Tradeoffs

Cashu é rápido porque as transferências acontecem off-chain e, com frequência, off-mint até o resgate. O tradeoff é interoperabilidade e confiança.

Na prática, usuários frequentemente precisam usar a mesma mint, ou então uma swap ou bridge entre mints. É por isso que aplicações Nostr costumam combinar Cashu com descoberta de mints, sincronização de carteiras e sistemas de review.

---

**Fontes primárias:**
- [Repositório Cashu NUTs](https://github.com/cashubtc/nuts)
- [NUT-00: criptografia e modelos](https://github.com/cashubtc/nuts/blob/main/00.md)
- [Especificação NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md)
- [Especificação NIP-87](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Mencionado em:**
- [Newsletter #7](/pt/newsletters/2026-01-28-newsletter/)
- [Newsletter #11](/pt/newsletters/2026-02-25-newsletter/)
- [Newsletter #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-60: Carteira Cashu](/pt/topics/nip-60/)
- [NIP-87: Recomendações de mints Cashu](/pt/topics/nip-87/)
- [TollGate](/pt/topics/tollgate/)
