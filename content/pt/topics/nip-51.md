---
title: "NIP-51: Listas"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Social
translationOf: /en/topics/nip-51.md
translationDate: 2025-12-26
---

NIP-51 define vários tipos de listas para organizar referências a eventos, usuários e conteúdo no Nostr.

## Tipos de Lista

- **Kind 10000**: Lista de silenciados (usuários, threads ou palavras para esconder)
- **Kind 10001**: Lista de fixados (eventos para destacar no perfil)
- **Kind 30000**: Conjuntos de seguidos (listas de seguidos categorizadas)
- **Kind 30003**: Conjuntos de favoritos
- **Kind 30004**: Conjuntos de curadoria (artigos)
- **Kind 30005**: Conjuntos de videos
- **Kind 30006**: Conjuntos de imagens
- **Kind 30015**: Conjuntos de interesses (hashtags)
- **Kind 30030**: Conjuntos de emojis

## Estrutura

Listas usam tags para referenciar conteúdo:
- Tags `p` para pubkeys
- Tags `e` para eventos
- Tags `a` para eventos endereçáveis
- Tags `t` para hashtags
- Tags `word` para palavras silenciadas

## Público vs Privado

Listas podem ter tags públicas (visíveis para todos) e conteúdo criptografado (privado). Itens privados são criptografados usando NIP-44 e armazenados no campo `content` do evento. A criptografia usa as próprias chaves do autor (criptografando para si mesmo).

Isso permite recursos como favoritos públicos com notas privadas, ou uma lista de silenciados onde os itens silenciados são escondidos de outros.

## Mudanças Recentes

- Tags de hashtag e URL removidas de favoritos genéricos; hashtags agora usam kind 30015
- Kind 30006 adicionado para conjuntos de imagens curados

---

**Fontes primárias:**
- [Especificação NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md)

**Mencionado em:**
- [Newsletter #1: Atualizações de NIP](/pt/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2: Atualizações de NIP](/pt/newsletters/2025-12-24-newsletter/#nip-updates)

**Veja também:**
- [NIP-02: Lista de Seguidos](/pt/topics/nip-02/)
