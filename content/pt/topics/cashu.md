---
title: 'Cashu: Protocolo Ecash'
date: 2026-01-28
draft: false
categories:
- Payments
- Privacy
- Bitcoin
translationOf: /en/topics/cashu.md
translationDate: '2026-03-07'
---

Cashu é um protocolo ecash Chaumian construído em Bitcoin e Lightning. Os usuários detêm tokens ao portador emitidos por um mint e, em seguida, transferem esses tokens sem expor o gráfico de pagamento completo ao mint.

## Como funciona

Cashu usa assinaturas cegas para emitir tokens ecash:

1. **Minting**: Os usuários depositam Bitcoin/Lightning em um mint e recebem tokens cegos
2. **Gastos**: Os tokens podem ser transferidos ponto a ponto sem o envolvimento do mint
3. **Resgate**: Os destinatários resgatam tokens no mint por Bitcoin/Lightning

O mint assina segredos cegos, para que possa verificar os tokens posteriormente sem ver os segredos originais no momento da emissão. Isso quebra a ligação direta entre depósito e resgate dentro do mint.

## Modelo de segurança e confiança

Cashu melhora a privacidade do pagamento, mas ainda tem custódia. Um mint pode recusar resgates, ficar offline ou perder fundos de garantia.

Cashu proofs são instrumentos de portador. Quem controla o proof pode gastá-lo. Isso torna o manuseio do proof mais próximo do dinheiro do que do saldo de uma conta: backup, comprometimento do dispositivo ou vazamento de token de texto simples são importantes imediatamente.

## Integração Nostr

Cashu se integra ao Nostr de várias maneiras:

- **Nutzaps**: tokens Ecash enviados como zaps com maior privacidade
- **Escrow**: garantia de pagamento baseada em HTLC para serviços como compartilhamento de viagens
- **Carteiras**: carteiras nativas Nostr armazenam tokens Cashu criptografados em relays
- **[NIP-87](/pt/topics/nip-87/)**: descoberta e análises do Mint via Nostr

## Compensações

Cashu é rápido porque as transferências acontecem fora da rede e muitas vezes fora do mint até o resgate. A compensação é interoperabilidade e confiança.

Na prática, os usuários geralmente precisam do mesmo mint ou de uma troca ou ponte entre mints. É por isso que os aplicativos Nostr frequentemente combinam Cashu com descoberta mint, sincronização de carteira e sistemas de revisão.

---

**Fontes primárias:**
- [Repositório Cashu NUTs](https://github.com/cashubtc/nuts)
- [NUT-00: Criptografia e modelos](https://github.com/cashubtc/nuts/blob/main/00.md)
- [NIP-60: Carteira Cashu](/pt/topics/nip-60/)
- [NIP-87: Recomendações Cashu Mint](/pt/topics/nip-87/)

**Mencionado em:**
- [Boletim informativo nº 7](/pt/newsletters/2026-01-28-newsletter/)
- [Boletim informativo nº 11](/pt/newsletters/2026-02-25-newsletter/)

**Veja também:**
- [NIP-60: Carteira Cashu](/pt/topics/nip-60/)
- [NIP-87: Recomendações Cashu Mint](/pt/topics/nip-87/)
