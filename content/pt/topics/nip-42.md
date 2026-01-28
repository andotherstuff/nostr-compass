---
title: "NIP-42: Autenticação de clientes para relays"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42 define como clientes se autenticam para relays. Relays podem exigir autenticação para fornecer controle de acesso, prevenir abuso ou implementar serviços de relay pagos.

## Como Funciona

O fluxo de autenticação começa quando um relay envia uma mensagem AUTH para o cliente. Esta mensagem contém uma string de desafio que o cliente deve assinar. O cliente cria um evento de autenticação kind 22242 contendo o desafio e o assina com sua chave privada. O relay verifica a assinatura e o desafio, então concede acesso.

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

O desafio previne ataques de replay: clientes devem assinar desafios frescos para cada tentativa de autenticação. A URL do relay nas tags garante que tokens de autenticação não possam ser reutilizados em diferentes relays.

## Casos de Uso

Relays pagos usam NIP-42 para verificar assinantes antes de conceder acesso. Após autenticar, relays podem verificar status de pagamento ou expiração de assinatura. Relays privados restringem acesso a pubkeys aprovadas, criando comunidades fechadas ou infraestrutura de relay pessoal.

Limitação de taxa se torna mais efetiva com autenticação. Relays podem rastrear taxas de requisição por pubkey autenticada em vez de por endereço IP, prevenindo abuso enquanto suportam usuários legítimos atrás de IPs compartilhados. Prevenção de spam melhora quando relays exigem autenticação para publicar eventos.

Alguns relays usam NIP-42 para analytics, rastreando quais usuários acessam qual conteúdo sem exigir contas centralizadas. Combinado com metadados [NIP-11](/pt/topics/nip-11/), clientes descobrem se relays exigem autenticação antes de tentar conexões.

---

**Fontes primárias:**
- [Especificação NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) - Autenticação de clientes para relays

**Veja também:**
- [NIP-11: Documento de Informação de Relay](/pt/topics/nip-11/)
- [NIP-50: Capacidade de Busca](/pt/topics/nip-50/)
