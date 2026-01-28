---
title: "Cashu: Protocolo Ecash"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-01-28
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu é um protocolo ecash Chaumiano construído sobre Bitcoin e Lightning Network, permitindo pagamentos privados, instantâneos e de baixa taxa através de tokens criptográficos.

## Como Funciona

Cashu usa assinaturas cegas para criar tokens ecash não rastreáveis:

1. **Cunhagem**: Usuários depositam Bitcoin/Lightning em um mint e recebem tokens cegos
2. **Gasto**: Tokens podem ser transferidos peer-to-peer sem envolvimento do mint
3. **Resgate**: Destinatários resgatam tokens no mint por Bitcoin/Lightning

O mint não pode vincular depósitos a resgates devido ao processo de cegamento, fornecendo fortes garantias de privacidade.

## Propriedades Principais

- **Privacidade**: O mint não pode rastrear transferências de tokens entre usuários
- **Instantâneo**: Transferências acontecem offline, sem necessidade de confirmação na blockchain
- **Baixa taxa**: Sem taxas on-chain para transferências de tokens
- **Custodial**: Usuários confiam no mint para honrar resgates

## Integração com Nostr

Cashu se integra com Nostr de várias formas:

- **Nutzaps**: Tokens ecash enviados como zaps com privacidade aprimorada
- **Escrow**: Escrow de pagamento baseado em HTLC para serviços como compartilhamento de caronas
- **Carteiras**: Carteiras nativas do Nostr armazenam tokens Cashu criptografados em relays
- **[NIP-87](/pt/topics/nip-87/)**: Descoberta e reviews de mints via Nostr

## Modelo de Confiança

Diferente do Bitcoin auto-custodial, Cashu requer confiar nos operadores de mint. Usuários devem:
- Usar mints reputáveis e bem avaliados
- Manter saldos pequenos apropriados ao nível de confiança
- Entender que mints podem dar exit-scam ou ficar offline, levando os fundos consigo

## Relacionados

- [NIP-87](/pt/topics/nip-87/) - Recomendações de Mint Cashu
- [NIP-60](/pt/topics/nip-60/) - Carteira Nostr
