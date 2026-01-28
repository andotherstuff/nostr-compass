---
title: "NIP-58: Badges"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58 define um sistema de badges para Nostr, permitindo que emissores criem badges e as concedam a usuários que podem então exibi-las em seus perfis.

## Como Funciona

### Definição de Badge (Kind 30009)

Emissores criam definições de badge como eventos endereçáveis:

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Adotante Inicial"],
    ["description", "Entrou antes de 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### Concessão de Badge (Kind 8)

Emissores concedem badges a usuários:

```json
{
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ]
}
```

### Exibição de Badge (Kind 30008)

Usuários escolhem quais badges exibir em seu perfil:

```json
{
  "kind": 30008,
  "tags": [
    ["d", "profile_badges"],
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["e", "award-event-id"]
  ]
}
```

## Casos de Uso

- **Associação a Comunidade**: Provar associação a grupos ou comunidades
- **Conquistas**: Reconhecer contribuições ou marcos
- **Verificação**: Atestações de terceiros (funcionário, criador, etc.)
- **Controle de Acesso**: Restringir conteúdo ou recursos baseado em posse de badge

## Modelo de Confiança

O valor da badge depende inteiramente da reputação do emissor. Qualquer um pode criar badges, então clientes devem:
- Exibir informações do emissor de forma proeminente
- Permitir que usuários filtrem por emissores confiáveis
- Não tratar badges como autoritativas sem contexto

## Relacionados

- [NIP-51](/pt/topics/nip-51/) - Listas
- [Web of Trust](/pt/topics/web-of-trust/)
