---
title: 'NIP-39: Identidades Externas em Perfis'
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Identity
---

O NIP-39 define como usuários anexam declarações de identidade externa a seus perfis Nostr usando tags `i`. Essas tags vinculam uma pubkey Nostr a contas em plataformas externas como GitHub, Twitter, Mastodon ou Telegram.

## Como funciona

Usuários publicam declarações de identidade em eventos kind 10011 como tags `i`. Cada tag contém um valor `platform:identity` mais um ponteiro de prova que permite a um cliente verificar a declaração:

```json
{
  "id": "5f1c7b7e2c6f3d4a9b0e6a2d8c1f7e3b4a6d9c0e1f2a3b4c5d6e7f8091a2b3c4",
  "pubkey": "3bf0c63fcb8d0d8b6a8fcb3c7f5cb2a972f8a0b5a3d6d8790bb2d4e4f0d6b1c2",
  "created_at": 1741699200,
  "kind": 10011,
  "tags": [
    ["i", "github:alice", "9f5df4e2a8b14c1f9e6d2b7c4a1e8f90"],
    ["i", "twitter:alice_dev", "1898123456789012345"]
  ],
  "content": "",
  "sig": "8f4c62d8a7e9b1c3d5f7091a2b4c6d8e0f1234567890abcdeffedcba09876543211223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

Clientes reconstroem a URL da prova a partir da plataforma e do valor da prova, depois verificam se o post externo contém o `npub` do usuário. Isso mantém a declaração portável entre clientes sem exigir um verificador central.

## Modelo de prova

O detalhe importante é que o NIP-39 prova o controle de duas identidades ao mesmo tempo: a chave Nostr e a conta externa. Se qualquer lado dessa prova desaparecer, a verificação se torna mais fraca. Um gist ou tweet apagado não invalida o evento histórico, mas remove a prova ativa da qual a maioria dos clientes depende.

Outro ponto útil de implementação é a estratégia de busca. Como as declarações agora vivem fora do kind 0, clientes podem decidir se vão solicitá-las apenas em visualizações detalhadas de perfil, apenas para usuários seguidos, ou nem solicitá-las. Isso evita adicionar mais peso ao caminho de kind 0, que já é bastante exigido.

## Implementações

- [Amethyst PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747) - Publica identidades externas como eventos dedicados kind 10011
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - Adiciona referência explícita ao registro kind 10011 no conjunto de NIPs

## Status atual

Na especificação atual, as declarações de identidade vivem em eventos dedicados kind 10011 em vez de metadados kind 0. Essa separação veio do esforço mais amplo para reduzir o peso das buscas de perfil em kind 0.

---

**Fontes primárias:**
- [NIP-39: Identidades Externas em Perfis](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - Moveu declarações de identidade para fora do kind 0
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - Adicionou referência explícita ao kind 10011

**Mencionado em:**
- [Newsletter #9: Atualizações de NIP](/pt/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12: Amethyst](/pt/newsletters/2026-03-04-newsletter/#amethyst-nip-39-nip-c0-nip-66)
- [Newsletter #13: Atualizações de NIP](/pt/newsletters/2026-03-11-newsletter/#atualizacoes-de-nip)

**Veja também:**
- [NIP-05: Verificação de Domínio](/pt/topics/nip-05/)
