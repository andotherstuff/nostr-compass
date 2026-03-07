---
title: 'NIP-39: Identidades Externas em Perfis'
date: 2026-02-11
draft: false
categories:
- NIPs
- Identity
translationOf: /en/topics/nip-39.md
translationDate: '2026-03-07'
---

O NIP-39 define como os usuários anexam declarações de identidade externas aos seus perfis Nostr usando `i` tags. Esses tags vinculam um Nostr pubkey a contas em plataformas externas como GitHub, Twitter, Mastodon ou Telegram.

## Como funciona

Os usuários publicam declarações de identidade em eventos kind 10011 como `i` tags. Cada tag contém um valor `platform:identity` mais um ponteiro proof que permite ao cliente verificar a declaração:

```json
{
  "kind": 10011,
  "tags": [
    ["i", "github:username", "gist-id"],
    ["i", "twitter:handle", "tweet-id"]
  ]
}
```

Os clientes reconstroem o URL proof a partir da plataforma e do valor proof e, em seguida, verificam se a postagem externa contém o `npub` do usuário. Isso mantém a portabilidade da reivindicação entre clientes sem a necessidade de um verificador central.

## Modelo de prova

O detalhe importante é que o NIP-39 comprova o controle de duas identidades ao mesmo tempo: a chave Nostr e a conta externa. Se um dos lados desse proof desaparecer, a verificação se tornará mais fraca. Uma essência ou tweet excluído não invalida o evento histórico, mas remove o proof ativo do qual a maioria dos clientes depende.

Outro ponto de implementação útil é a estratégia de busca. Como as reivindicações agora estão fora kind 0, os clientes podem decidir se desejam solicitá-las apenas nas visualizações de detalhes do perfil, apenas para usuários seguidos ou não. Isso evita adicionar mais peso ao caminho kind 0 já quente.

## Status atual

A partir da especificação atual, as declarações de identidade residem em eventos kind 10011 dedicados em vez de metadados kind 0. Essa separação veio do esforço mais amplo para reduzir as buscas de perfil kind 0.

---

**Fontes primárias:**
- [NIP-39: Identidades Externas em Perfis](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - Reivindicações de identidade movidas de kind 0

**Mencionado em:**
- [Boletim informativo nº 9: Atualizações do NIP](/pt/newsletters/2026-02-11-newsletter/#nip-updates)
- [Boletim informativo nº 12: Ametista](/pt/newsletters/2026-03-04-newsletter/#amethyst-nip-39-nip-c0-nip-66)

**Veja também:**
- [NIP-05: Verificação baseada em DNS](/pt/topics/nip-05/)
