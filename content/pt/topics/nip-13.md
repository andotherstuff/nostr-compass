---
title: 'NIP-13: Prova de Trabalho'
date: 2026-01-28
draft: false
categories:
- NIP
- Spam Prevention
translationOf: /en/topics/nip-13.md
translationDate: '2026-03-07'
---

O NIP-13 define um sistema proof-of-work para eventos Nostr, exigindo esforço computacional para criar eventos como mecanismo de prevenção de spam.

## Como funciona

A prova de trabalho é demonstrada encontrando um ID de evento (hash SHA256) com um número especificado de zero bits à esquerda:

1. **Dificuldade**: medida em zero bits iniciais (por exemplo, 20 bits = 2^20 tentativas em média)
2. **Tag Nonce**: Os eventos incluem um `nonce` tag com o valor nonce e dificuldade alvo
3. **Verificação**: Retransmissores e clientes podem verificar rapidamente se o trabalho foi realizado

```json
{
  "tags": [["nonce", "12345", "20"]],
  ...
}
```

## Níveis de dificuldade

| Pedaços | Média de tentativas | Uso típico |
|------|------------------|------------|
| 8 | 256 | Dissuasão mínima de spam |
| 16 | 65.536 | Filtragem de luz |
| 20 | 1.048.576 | Proteção moderada |
| 24 | 16.777.216 | Forte resistência a spam |

## Por que é importante

- **Admissão de revezamento**: os revezamentos podem exigir PoW mínimo para aceitação do evento
- **Rate Limiting**: Maior dificuldade para ações como registro de conta
- **Filtragem de spam**: os clientes podem priorizar eventos de alto PoW em feeds
- **Bootstrap de reputação**: novas contas podem demonstrar comprometimento via PoW

A propriedade útil é o custo assimétrico. A criação de muitos eventos aceitáveis ​​torna-se cara para o remetente, enquanto a verificação do proof permanece barata para relays e clientes.

## Compensações

- Favorece usuários com hardware poderoso
- Preocupações com o consumo de energia
- Não evita todo spam, apenas aumenta o custo

O PoW também muda a resistência ao spam da identidade da conta para a disponibilidade da computação. Isso pode ajudar em ambientes sem permissão, mas não distingue entre um novo usuário legítimo e um spammer bem financiado.

---

**Fontes primárias:**
- [Especificação NIP-13](https://github.com/nostr-protocol/nips/blob/master/13.md)

**Mencionado em:**
- [Boletim informativo nº 7: Notícias](/pt/newsletters/2026-01-28-newsletter/#news)
- [Boletim informativo nº 12: Notícias](/pt/newsletters/2026-03-04-newsletter/#news)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
