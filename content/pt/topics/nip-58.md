---
title: 'NIP-58: Emblemas'
date: 2026-01-28
draft: false
categories:
- NIP
- Identity
- Reputation
translationOf: /en/topics/nip-58.md
translationDate: '2026-03-07'
---

NIP-58 define um sistema de crachás para Nostr. Um evento define o selo, outro o concede e um terceiro permite que o destinatário escolha se deseja exibi-lo em seu perfil.

## Como funciona

### Definição do selo (kind 30009)

Os emissores criam definições de crachás como eventos endereçáveis:

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Early Adopter"],
    ["description", "Joined before 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### Prêmio Distintivo (kind 8)

Os emissores concedem emblemas a um ou mais usuários:

```json
{
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ]
}
```

### Exibição de crachá (kind 30008)

Os usuários escolhem quais emblemas exibir em seus perfis:

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

Em um evento de crachás de perfil, os clientes deverão ler `a` e `e` tags como pares ordenados. Um `a` tag sem seu evento de premiação correspondente, ou um `e` tag sem sua definição de crachá correspondente, deve ser ignorado.

## Casos de uso

- **Associação à comunidade**: mostre a associação em grupos ou comunidades
- **Conquistas**: reconheça contribuições ou marcos
- **Atestados**: permita que um terceiro ateste uma função ou status
- **Controle de acesso**: recursos de portão ou espaços usando crachás apoiados pelo emissor

## Modelo de confiança

O valor do selo depende inteiramente da reputação do emissor. Qualquer pessoa pode criar crachás, portanto os clientes devem:

- Exibir informações do emissor com destaque
- Permitir que os usuários filtrem por emissores confiáveis
- Não tratar os emblemas como oficiais sem contexto

Os prêmios de distintivo são imutáveis ​​e intransferíveis. Isso torna os crachás adequados para atestados e reconhecimentos, mas não para credenciais portáteis no sentido tokenizado.

## Notas de implementação

As definições de crachás são eventos endereçáveis, de modo que os emissores podem atualizar a arte ou as descrições dos crachás ao longo do tempo, sem alterar o identificador do crachá. O evento de premiação é o registro durável que vincula o destinatário a essa definição em um determinado momento.

Os clientes também têm liberdade na apresentação. A especificação permite explicitamente que eles mostrem menos emblemas do que as listas de usuários e escolham o tamanho da miniatura que se ajusta ao espaço disponível.

---

**Fontes primárias:**
- [Especificação NIP-58](https://github.com/nostr-protocol/nips/blob/master/58.md)

**Mencionado em:**
- [Boletim informativo nº 7: Cinco anos de Nostr Januarys](/pt/newsletters/2026-01-28-newsletter/)
- [Boletim informativo nº 15: Cinco anos de fevereiro de Nostr](/pt/newsletters/2026-03-04-newsletter/)

**Veja também:**
- [NIP-51: Listas](/pt/topics/nip-51/)
- [Web of Trust](/pt/topics/web-of-trust/)
