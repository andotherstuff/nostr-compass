---
title: "NIP-39: Identidades Externas em Perfis"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 define como usuários vinculam claims de identidade externa aos seus perfis Nostr usando tags `i`. Essas tags conectam uma pubkey Nostr a contas em plataformas externas como GitHub, Twitter ou domínios DNS.

## Como Funciona

Usuários publicam claims de identidade como tags `i`. Cada tag contém um identificador de plataforma e uma URL de prova onde a conta externa aponta de volta à pubkey Nostr, estabelecendo verificação bidirecional:

```json
{
  "tags": [
    ["i", "github:username", "https://gist.github.com/username/proof"],
    ["i", "twitter:handle", "https://twitter.com/handle/status/proof_tweet_id"]
  ]
}
```

Aplicações verificam claims buscando a URL de prova e confirmando que ela contém a pubkey Nostr do usuário. Isso cria uma rede de conexões de identidade sem exigir serviços centralizados de verificação.

## Mudanças Recentes

Em fevereiro de 2026, o [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) extraiu tags de identidade de eventos kind 0 (metadados de usuário) a um kind 10011 dedicado. A mudança fez parte da campanha de redução do kind 0 de vitorpamplona, motivada pela baixa adoção: quase nenhum cliente implementava verificação de tags `i`, mas cada busca de kind 0 carregava o overhead. O novo kind 10011 permite que aplicações interessadas busquem claims de identidade separadamente.

---

**Fontes primárias:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)

**Mencionado em:**
- [Newsletter #9: Atualizações de NIPs](/pt/newsletters/2026-02-11-newsletter/#atualizações-de-nips)

**Veja também:**
- [NIP-05: Verificação Baseada em DNS](/pt/topics/nip-05/)
