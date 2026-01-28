---
title: "NIP-32: Rotulagem"
date: 2026-01-21
translationOf: /en/topics/nip-32.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-32 define um padrão para anexar rótulos a eventos Nostr, usuários e outras entidades. Rótulos fornecem metadados estruturados que clientes podem usar para categorização, avisos de conteúdo, sistemas de reputação e moderação.

## Como Funciona

Rótulos usam eventos kind 1985 com uma tag `L` definindo o namespace do rótulo e tags `l` aplicando rótulos específicos dentro desse namespace. A entidade rotulada é referenciada através de tags padrão como `e` (eventos), `p` (pubkeys) ou `r` (URLs de relay).

```json
{
  "kind": 1985,
  "tags": [
    ["L", "content-warning"],
    ["l", "nsfw", "content-warning"],
    ["e", "<event_id>"]
  ],
  "content": "Contém imagens explícitas"
}
```

O sistema de namespace previne colisões de rótulos. Um rótulo "spam" no namespace "ugc-moderation" tem semântica diferente de "spam" no namespace "relay-report". Isso permite que múltiplos sistemas de rótulos coexistam sem interferência.

## Casos de Uso

Sistemas de moderação de conteúdo usam rótulos para marcar spam, conteúdo ilegal ou violações de política. Sistemas de reputação anexam pontuações de confiança ou status de verificação a pubkeys. Plataformas de mídia aplicam avisos de conteúdo (NSFW, violência, spoilers). Operadores de relay usam rótulos para recursos e resolução de disputas.

A proposta Trusted Relay Assertions usa rótulos NIP-32 para recursos de relay. Quando operadores disputam pontuações de confiança, eles publicam eventos kind 1985 com `L` = `relay-appeal` e tipos de rótulo como "spam", "censorship" ou "score".

Implementações de cliente variam em como consomem rótulos. Alguns clientes tratam rótulos de usuários seguidos como recomendações, enquanto outros consultam serviços de rotulagem especializados. O design descentralizado permite que usuários escolham em quais rotuladores confiar.

---

**Fontes primárias:**
- [Especificação NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) - Padrão de rotulagem

**Mencionado em:**
- [Newsletter #6: Atualizações de NIP](/pt/newsletters/2026-01-21-newsletter/#nip-updates)

**Veja também:**
- [Trusted Relay Assertions](/pt/topics/trusted-relay-assertions/)
- [NIP-51: Listas](/pt/topics/nip-51/)
