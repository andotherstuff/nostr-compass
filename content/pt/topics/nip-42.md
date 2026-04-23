---
title: 'NIP-42: Autenticação de clientes em relays'
date: 2026-01-21
draft: false
categories:
  - NIPs
  - Authentication
translationOf: /en/topics/nip-42.md
translationDate: 2026-04-22
---

NIP-42 define como clientes se autenticam em relays. Relays podem exigir autenticação para aplicar controle de acesso, prevenir abuso ou implementar serviços de relay pagos.

## Como funciona

O fluxo de autenticação começa quando um relay envia uma mensagem `AUTH` ao cliente. Essa mensagem contém uma challenge string que o cliente precisa assinar. O cliente cria um evento de autenticação kind 22242 contendo a challenge e o assina com sua chave privada. O relay verifica a assinatura e a challenge e então concede acesso.

```json
{
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com"],
    ["challenge", "random-challenge-string"]
  ],
  "content": "",
  "pubkey": "<client_pubkey>",
  "created_at": 1736784000,
  "sig": "<signature>"
}
```

A challenge previne ataques de replay. A URL do relay nas tags impede que o mesmo evento assinado seja reutilizado em relays diferentes.

## Notas de protocolo

A autenticação tem escopo de conexão. Uma challenge permanece válida pela duração da conexão, ou até que o relay envie uma nova. O evento assinado é efêmero e não deve ser transmitido como um evento normal.

A spec também define prefixos de erro legíveis por máquina. `auth-required:` significa que o cliente ainda não se autenticou. `restricted:` significa que ele se autenticou, mas aquela pubkey ainda não tem permissão para a ação solicitada.

## Casos de uso

Relays pagos usam NIP-42 para verificar assinantes antes de conceder acesso. Relays privados a usam para limitar leitura ou escrita a pubkeys aprovadas. Ela também melhora rate limiting porque relays conseguem acompanhar comportamento por chave autenticada, e não apenas por endereço IP.

Combinada com metadados da [NIP-11](/pt/topics/nip-11/), clientes podem descobrir se um relay suporta NIP-42 antes de tentar queries protegidas. Na prática, o suporte ainda é desigual, então clientes precisam de fallback quando um relay anuncia NIP-42 mas lida incorretamente com eventos protegidos.

---

**Fontes primárias:**
- [Especificação NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) - autenticação de clientes em relays

**Mencionado em:**
- [Newsletter #6: Relay Information Documents](/pt/newsletters/2026-01-21-newsletter/)
- [Newsletter #9: testes de status de relay no Marmot](/pt/newsletters/2026-02-11-newsletter/)
- [Newsletter #10: servidor Nostr MCP](/pt/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Relay AUTH começa a chegar a apps reais](/en/newsletters/2026-03-11-newsletter/)

**Veja também:**
- [NIP-11: Relay Information Document](/pt/topics/nip-11/)
- [NIP-50: capacidade de busca](/pt/topics/nip-50/)
