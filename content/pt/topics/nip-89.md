---
title: "NIP-89: Handlers de Aplicação Recomendados"
date: 2026-01-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

O NIP-89 define como aplicações podem anunciar suas capacidades e como usuários podem recomendar apps que lidam com tipos específicos de eventos.

## Tipos de Eventos

- **kind 31990** - Handler de aplicação (publicado por desenvolvedores de apps)
- **kind 31989** - Recomendação de app (publicada por usuários)

## Como Funciona

1. **Aplicações** publicam eventos de handler descrevendo quais tipos de eventos suportam e como abrir conteúdo
2. **Usuários** recomendam apps que usam para tipos específicos de eventos
3. **Clientes** consultam recomendações para oferecer funcionalidade "abrir em..." para tipos de eventos desconhecidos

## Handler de Aplicação

```json
{
  "id": "<event-id>",
  "pubkey": "<app-developer-pubkey>",
  "created_at": 1736200000,
  "kind": 31990,
  "tags": [
    ["d", "<app-identifier>"],
    ["k", "30023"],
    ["web", "https://app.example.com/a/<bech32>", "naddr"],
    ["ios", "appname://open/<bech32>"]
  ],
  "content": "{\"name\": \"My App\", \"picture\": \"...\"}",
  "sig": "<signature>"
}
```

As tags `k` especificam os tipos de eventos suportados. Templates de URL usam `<bech32>` como placeholder para entidades codificadas em NIP-19.

## Recomendação de Usuário

```json
{
  "id": "<event-id>",
  "pubkey": "<user-pubkey>",
  "created_at": 1736200000,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:app-pubkey:identifier", "wss://relay", "web"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

A tag `d` é o tipo de evento sendo recomendado. Múltiplas tags `a` podem recomendar diferentes apps para diferentes plataformas.

## Casos de Uso

- Descobrir apps que podem exibir artigos longos (kind 30023)
- Encontrar clientes que suportam tipos específicos de eventos
- Funcionalidade "abrir em..." entre clientes
- Detectar capacidades de clientes para suporte de criptografia

---

**Fontes primárias:**
- [Especificação NIP-89](https://github.com/nostr-protocol/nips/blob/master/89.md)

**Mencionado em:**
- [Newsletter #4: Aprofundamento em NIPs](/pt/newsletters/2026-01-07-newsletter/#nip-44-criptografia-versionada)

**Veja também:**
- [NIP-19: Entidades Codificadas em Bech32](/pt/topics/nip-19/)
