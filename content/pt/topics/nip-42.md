---
title: 'NIP-42: Autenticação de clientes para relays'
date: 2026-01-21
draft: false
categories:
- NIPs
- Authentication
translationOf: /en/topics/nip-42.md
translationDate: '2026-03-07'
---

NIP-42 define como os clientes se autenticam nos relays. Os relays podem exigir autenticação para fornecer controle de acesso, evitar abusos ou implementar serviços relay pagos.

## Como funciona

O fluxo de autenticação começa quando um relay envia uma mensagem `AUTH` ao cliente. Esta mensagem contém uma sequência de desafio que o cliente deve assinar. O cliente cria um evento de autenticação kind 22242 contendo o desafio e assina-o com sua chave privada. O relay verifica a assinatura e o desafio e, em seguida, concede o acesso.

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

O desafio evita ataques de repetição. A URL relay em tags evita que o mesmo evento assinado seja reutilizado em diferentes relays.

## Notas de Protocolo

A autenticação tem escopo de conexão. Um desafio permanece válido enquanto durar a conexão ou até que o relay envie um novo. O evento assinado é efêmero e não deve ser transmitido como um evento normal.

A especificação também define prefixos de erro legíveis por máquina. `auth-required:` significa que o cliente ainda não foi autenticado. `restricted:` significa que foi autenticado, mas pubkey ainda não tem permissão para a ação solicitada.

## Casos de uso

relays pago usa NIP-42 para verificar os assinantes antes de conceder acesso. relays privado usa-o para limitar leituras ou gravações em pubkeys aprovados. Também melhora a limitação de taxa porque relays pode rastrear o comportamento por chave autenticada em vez de por endereço IP.

Combinado com metadados [NIP-11](/pt/topics/nip-11/), os clientes podem descobrir se um relay suporta NIP-42 antes de tentar consultas protegidas. Na prática, o suporte ainda é desigual, então os clientes precisam de um caminho alternativo quando um relay anuncia NIP-42, mas trata eventos protegidos incorretamente.

---

**Fontes primárias:**
- [Especificação NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) - Autenticação de clientes para relays

**Mencionado em:**
- [Boletim informativo nº 6: Documentos de informações de relay](/pt/newsletters/2026-01-21-newsletter/#relay-information-documents-get-formalized)
- [Boletim informativo nº 9: Teste de status do relay Marmot](/pt/newsletters/2026-02-11-newsletter/#nip-70-relay-support-critical-for-encrypted-messaging-security)
- [Boletim informativo nº 10: Servidor Nostr MCP](/pt/newsletters/2026-02-18-newsletter/#nostr-mcp-server)

**Veja também:**
- [NIP-11: Documento de Informações do Relay](/pt/topics/nip-11/)
- [NIP-50: capacidade de pesquisa](/pt/topics/nip-50/)
