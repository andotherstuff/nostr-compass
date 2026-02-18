---
title: "NIP-56: Denúncias"
date: 2026-02-18
translationOf: /en/topics/nip-56.md
translationDate: 2026-02-18
draft: false
categories:
  - Moderation
  - Protocol
---

O NIP-56 define um mecanismo de denúncia usando eventos kind 1984, permitindo que usuários e aplicações sinalem conteúdo indesejável em toda a rede Nostr.

## Como Funciona

Um usuário publica um evento kind 1984 com uma tag `p` referenciando o pubkey sendo denunciado. Ao denunciar uma nota específica, uma tag `e` referencia o ID da nota. Ambas as tags aceitam um terceiro parâmetro especificando a categoria de violação.

## Categorias de Denúncia

- **nudity**: conteúdo adulto
- **malware**: vírus, trojans, ransomware
- **profanity**: linguagem ofensiva e discurso de ódio
- **illegal**: conteúdo potencialmente violando leis
- **spam**: mensagens repetitivas indesejadas
- **impersonation**: reivindicações fraudulentas de identidade
- **other**: violações que não se enquadram nas categorias acima

## Comportamento de Clientes e Relays

Clientes podem usar denúncias de usuários seguidos para decisões de moderação, como desfocar conteúdo quando múltiplos contatos confiáveis o sinalizam. Relays devem evitar moderação automática via denúncias devido a riscos de manipulação; denúncias de moderadores confiáveis podem informar a aplicação manual em vez disso. Classificação adicional é suportada por meio das tags `l` e `L` do NIP-32.

---

**Fontes primárias:**
- [Especificação NIP-56](https://github.com/nostr-protocol/nips/blob/master/56.md)

**Mencionado em:**
- [Compass #10: Atualizações de Projetos](/pt/newsletters/2026-02-18-newsletter/#notedeck-preparação-para-android-app-store)

**Veja também:**
- [NIP-22: Comentário](/pt/topics/nip-22/)
