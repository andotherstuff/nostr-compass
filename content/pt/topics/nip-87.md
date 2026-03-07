---
title: 'NIP-87: Capacidade de descoberta do Ecash Mint'
date: 2026-01-07
draft: false
categories:
- Ecash
- Discovery
- Protocol
translationOf: /en/topics/nip-87.md
translationDate: '2026-03-07'
---

O NIP-87 define como o ecash mints (Cashu e Fedimint) pode se anunciar no Nostr e como os usuários podem recomendar o mints a outras pessoas.

## Tipos de eventos

- **kind 38172** - Anúncio Cashu mint (publicado pelos operadores mint)
- **kind 38173** - Anúncio Fedimint (publicado pelos operadores mint)
- **kind 38000** - Recomendação Mint (publicada pelos usuários)

## Como funciona

1. **Operadores Mint** publicam o URL, os recursos suportados e a rede do mint (mainnet/testnet)
2. **Usuários** que confiam no mint publicam recomendações com avaliações opcionais
3. **Outros usuários** consultam recomendações de pessoas que seguem para descobrir mints confiável

## Anúncio da Casa da Moeda Cashu

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

O `nuts` tag lista NUTs suportados (especificações de notação, uso e terminologia para Cashu).

O `d` tag deve ser o Cashu pubkey do mint, que fornece aos clientes um identificador estável para descoberta, mesmo que o mint posteriormente altere os metadados ou republice seu anúncio.

## Recomendações de usuários

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
  "content": "I've used this mint for months, very reliable",
  "sig": "<signature>"
}
```

Os usuários podem incluir comentários no campo `content` e apontar para eventos específicos de anúncio do mint.

Os eventos de recomendação são eventos substituíveis parametrizados. Isso é útil porque um usuário pode revisar uma recomendação, atualizar seu texto de revisão ou parar de endossar um mint sem deixar para trás vários eventos de recomendação obsoletos.

## Modelo de confiança

O NIP-87 não informa aos clientes qual mint é seguro. Isso lhes dá uma maneira de combinar metadados publicados pela operadora com recomendações sociais de contas nas quais o usuário já confia.

Essa distinção é importante porque as consultas diretas para eventos de anúncio do mint podem ser ruidosas ou maliciosas. A especificação alerta explicitamente os clientes para usarem medidas de prevenção de spam ou relays de alta qualidade ao ignorar recomendações sociais e consultar anúncios diretamente.

## Notas de interoperabilidade

Cashu e Fedimint usam anúncios diferentes kinds porque expõem detalhes de conexão diferentes. Os anúncios Cashu publicam URLs mint e NUTs suportados, enquanto os anúncios Fedimint publicam códigos de convite e módulos de federação suportados. Uma carteira que suporte ambos precisa analisar ambos os formatos.

---

**Fontes primárias:**
- [Especificação NIP-87](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Mencionado em:**
- [Boletim Informativo nº 4: Lançamentos](/pt/newsletters/2026-01-07-newsletter/#releases)
- [Boletim informativo nº 7: Zeus](/pt/newsletters/2026-01-28-newsletter/)

**Veja também:**
- [Cashu](/pt/topics/cashu/)
- [NIP-60: Carteira Cashu](/pt/topics/nip-60/)
