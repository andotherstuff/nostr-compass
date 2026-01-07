---
title: "NIP-87: Descoberta de Mints Ecash"
date: 2026-01-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---

O NIP-87 define como mints de ecash (Cashu e Fedimint) podem se anunciar no Nostr, e como usuários podem recomendar mints para outros.

## Tipos de Eventos

- **kind 38172** - Anúncio de mint Cashu (publicado por operadores de mint)
- **kind 38173** - Anúncio de Fedimint (publicado por operadores de mint)
- **kind 38000** - Recomendação de mint (publicada por usuários)

## Como Funciona

1. **Operadores de mint** publicam a URL do mint, recursos suportados e rede (mainnet/testnet)
2. **Usuários** que confiam em um mint publicam recomendações com avaliações opcionais
3. **Outros usuários** consultam recomendações de pessoas que seguem para descobrir mints confiáveis

## Anúncio de Mint Cashu

```json
{
  "id": "<event-id>",
  "pubkey": "<mint-operator-pubkey>",
  "created_at": 1736200000,
  "kind": 38172,
  "tags": [
    ["d", "<mint-pubkey>"],
    ["u", "https://mint.example.com"],
    ["nuts", "1,2,3,4,5,6,7"],
    ["n", "mainnet"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

A tag `nuts` lista os NUTs (Notation, Usage, and Terminology specs for Cashu) suportados.

## Recomendações de Usuários

```json
{
  "id": "<event-id>",
  "pubkey": "<recommender-pubkey>",
  "created_at": 1736200000,
  "kind": 38000,
  "tags": [
    ["k", "38172"],
    ["d", "<mint-identifier>"],
    ["a", "38172:mint-pubkey:<d-tag>", "wss://relay"]
  ],
  "content": "Uso este mint há meses, muito confiável",
  "sig": "<signature>"
}
```

Usuários podem incluir avaliações no campo `content` e apontar para eventos de anúncio de mint específicos.

---

**Fontes primárias:**
- [Especificação NIP-87](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Mencionado em:**
- [Newsletter #4: Lançamentos](/pt/newsletters/2026-01-07-newsletter/#lançamentos)

**Veja também:**
- [NIP-60: Carteira Cashu](/pt/topics/nip-60/)
