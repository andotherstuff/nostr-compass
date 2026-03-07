---
title: 'NIP-32: Rotulagem'
date: 2026-01-21
draft: false
categories:
- NIPs
- Protocol
translationOf: /en/topics/nip-32.md
translationDate: '2026-03-07'
---

O NIP-32 define um padrão para anexar rótulos a eventos, usuários e outras entidades Nostr. Os rótulos fornecem metadados estruturados que os clientes podem usar para categorização, avisos de conteúdo, sistemas de reputação e moderação.

## Como funciona

Os rótulos usam eventos kind 1985 com um `L` tag definindo o namespace do rótulo e `l` tags aplicando rótulos específicos dentro desse namespace. A entidade rotulada é referenciada por meio de tags padrão como `e` (eventos), `p` (pubkeys) ou `r` (URLs relay).

```json
{
  "kind": 1985,
  "tags": [
    ["L", "content-warning"],
    ["l", "nsfw", "content-warning"],
    ["e", "<event_id>"]
  ],
  "content": "Contains explicit imagery"
}
```

O sistema de namespace evita colisões de rótulos. Um rótulo "spam" no namespace "ugc-moderation" tem semântica diferente de "spam" no namespace "relay-report". Isto permite que vários sistemas de etiquetas coexistam sem interferência.

## Por que é importante

A principal escolha de design é que os rótulos sejam afirmações, e não fatos incorporados ao protocolo. Um evento kind 1985 diz que algum ator rotulou algo em algum namespace. Os clientes ainda precisam de uma política de confiança para decidir quais rótulos mostrar, ocultar ou ignorar.

Isso torna o NIP-32 útil muito além da moderação. A mesma estrutura pode conter avisos de conteúdo, marcadores de verificação, sistemas de classificação ou dados de reputação relay sem forçar todos os clientes a um vocabulário global.

## Casos de uso

Os sistemas de moderação de conteúdo usam rótulos para marcar spam, conteúdo ilegal ou violações de políticas. Os sistemas de reputação atribuem pontuações de confiança ou status de verificação ao pubkeys. As plataformas de mídia aplicam avisos de conteúdo como NSFW, violência ou spoilers. Os operadores de relay usam rótulos para apelações e resolução de disputas.

A proposta Trusted Relay Assertions utiliza rótulos NIP-32 para apelos relay. Quando as operadoras contestam pontuações de confiança, elas publicam eventos kind 1985 com `L = relay-appeal` e rótulos como `spam`, `censorship` ou `score`.

## Notas de interoperabilidade

Os clientes diferem na forma como consomem os rótulos. Alguns tratam rótulos de usuários seguidos como recomendações, enquanto outros consultam serviços especializados de etiquetagem. O design descentralizado permite que os usuários escolham em quais rotuladores confiar, mas também significa que um rótulo sem contexto de confiança visível pode ser enganoso.

---

**Fontes primárias:**
- [Especificação NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) - Padrão de rotulagem

**Mencionado em:**
- [Boletim informativo nº 6: Atualizações do NIP](/pt/newsletters/2026-01-21-newsletter/#nip-updates)

**Veja também:**
- [Trusted Relay Assertions](/pt/topics/trusted-relay-assertions/)
- [NIP-51: Listas](/pt/topics/nip-51/)
