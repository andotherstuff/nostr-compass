---
title: "NIP-98: HTTP Auth"
date: 2026-03-25
translationOf: /en/topics/nip-98.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-98 define autenticação HTTP usando eventos Nostr. Permite que servidores verifiquem a identidade Nostr de um cliente em requisições HTTP padrão sem senhas, chaves de API ou fluxos OAuth.

## Como Funciona

Quando um cliente precisa autenticar uma requisição HTTP, ele cria um evento kind 27235. Este evento contém a URL alvo e o método HTTP em suas tags, vinculando a autenticação a uma requisição específica.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1742860800,
  "kind": 27235,
  "tags": [
    ["u", "https://files.example.com/upload"],
    ["method", "POST"],
    ["payload", "<sha256-hash-of-request-body>"]
  ],
  "content": "",
  "sig": "<128-char hex>"
}
```

O cliente assina este evento, codifica em base64 e envia no header HTTP `Authorization` com o esquema `Nostr`:

```
Authorization: Nostr <base64-encoded-signed-event>
```

O servidor decodifica o evento, verifica a assinatura, confere que a URL e o método correspondem à requisição real, e confirma que o timestamp é recente. Se todas as verificações passarem, o servidor sabe qual pubkey Nostr fez a requisição.

A tag opcional `payload` contém um hash SHA-256 do corpo da requisição, o que impede que o evento de auth seja reutilizado com conteúdo diferente. A verificação de timestamp (servidores tipicamente rejeitam eventos com mais de alguns minutos) previne ataques de replay.

## Casos de Uso

Servidores Blossom usam NIP-98 para autenticar uploads e exclusões de arquivos, vinculando mídia armazenada a uma identidade Nostr específica. Serviços de hospedagem de arquivos usam para impor cotas de upload por pubkey. Qualquer API HTTP que precise identificar um usuário Nostr sem manter seu próprio sistema de contas pode aceitar headers NIP-98 como prova de identidade.

---

**Fontes primárias:**
- [Especificação NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) - HTTP Auth

**Mencionado em:**
- [Newsletter #15](/pt/newsletters/2026-03-25-newsletter/)
