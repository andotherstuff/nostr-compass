---
title: "NIP-13: Prova de Trabalho"
date: 2026-01-28
translationOf: /en/topics/nip-13.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Spam Prevention
---

NIP-13 define um sistema de prova de trabalho para eventos Nostr, exigindo esforço computacional para criar eventos como mecanismo de prevenção de spam.

## Como Funciona

Prova de trabalho é demonstrada encontrando um ID de evento (hash SHA256) com um número especificado de bits zero iniciais:

1. **Dificuldade**: Medida em bits zero iniciais (ex: 20 bits = 2^20 tentativas em média)
2. **Tag Nonce**: Eventos incluem uma tag `nonce` com o valor do nonce e dificuldade alvo
3. **Verificação**: Relays e clientes podem rapidamente verificar que o trabalho foi feito

```json
{
  "tags": [["nonce", "12345", "20"]],
  ...
}
```

## Níveis de Dificuldade

| Bits | Tentativas Médias | Uso Típico |
|------|-------------------|------------|
| 8 | 256 | Dissuasor mínimo de spam |
| 16 | 65.536 | Filtragem leve |
| 20 | 1.048.576 | Proteção moderada |
| 24 | 16.777.216 | Forte resistência a spam |

## Casos de Uso

- **Admissão em Relay**: Relays podem exigir PoW mínimo para aceitação de eventos
- **Limitação de Taxa**: Maior dificuldade para ações como registro de conta
- **Filtragem de Spam**: Clientes podem priorizar eventos de alto PoW em feeds
- **Bootstrap de Reputação**: Novas contas podem demonstrar comprometimento via PoW

## Limitações

- Favorece usuários com hardware poderoso
- Preocupações com consumo de energia
- Não previne todo spam, apenas aumenta o custo

## Relacionados

- [NIP-01](/pt/topics/nip-01/) - Protocolo Básico
