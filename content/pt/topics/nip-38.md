---
title: "NIP-38: Status de usuário"
date: 2026-08-26
translationOf: /en/topics/nip-38.md
translationDate: 2026-08-26
draft: false
description: "Define eventos de status de usuário de curta duração, incluindo as categorias de status geral e musical."
---

O NIP-38 define eventos endereçáveis kind 30315 para status breves de usuário. Uma tag `d` identifica a categoria do status, como `general` ou `music`, enquanto tags `r` e `p` opcionais podem apontar para uma URL ou identificar um artista. Clientes podem usar a tag `expiration` do evento para parar de exibir status desatualizados.

## Como funciona

Um usuário publica um evento kind 30315 com o texto do status em `content`. O evento é endereçável por pubkey, kind e tag `d`, então um evento mais recente da mesma categoria substitui o anterior. Um campo de conteúdo vazio limpa esse status.

---

**Fontes primárias:**
- [Especificação do NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) - Status de usuário

**Mencionado em:**
- [Newsletter #37: NoorNote v1.3.6: status de perfil e anúncios classificados](/pt/newsletters/2026-08-26-newsletter/#noornote-v136-status-de-perfil-e-anúncios-classificados)
