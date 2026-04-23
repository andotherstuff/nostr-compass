---
title: "NIP-21: Esquema URI nostr:"
date: 2026-04-22
translationOf: /en/topics/nip-21.md
translationDate: 2026-04-23
draft: false
categories:
  - Protocolo
  - Interoperabilidade
---

NIP-21 define o esquema URI `nostr:`, um padrão para aplicações, websites e sistemas operacionais registrarem interesse em abrir identificadores Nostr como `npub`, `nprofile`, `nevent` e `naddr` em qualquer cliente Nostr que o usuário tenha registrado como manipulador.

## Como Funciona

Um URI `nostr:` é o prefixo do esquema seguido por qualquer um dos identificadores bech32 de [NIP-19](/pt/topics/nip-19/) exceto `nsec`. Clientes e sistemas operacionais tratam o esquema da mesma forma que tratam `mailto:` ou `tel:`: registrar-se como manipulador permite que o usuário clique em um link `nostr:` em qualquer lugar do sistema e o abra em seu cliente Nostr de escolha.

Exemplos da especificação:

- `nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9` aponta para um perfil de usuário
- `nostr:nprofile1...` aponta para um perfil de usuário com dicas de retransmissão incluídas
- `nostr:nevent1...` aponta para um evento específico com dicas de retransmissão
- `nostr:naddr1...` aponta para um evento substituível parametrizado (como um artigo de formato longo)

## Vinculando Páginas HTML a Entidades Nostr

NIP-21 também especifica duas convenções úteis de `<link>` para páginas da web que correspondem a entidades Nostr. Uma página que serve o mesmo conteúdo de um evento Nostr (por exemplo, um post de blog renderizado a partir de um artigo `kind:30023` de [NIP-23](/pt/topics/nip-23/)) pode incluir um `<link rel="alternate">` apontando para o URI Nostr. Uma página de perfil pode incluir um `<link rel="me">` ou `<link rel="author">` apontando para um `nprofile` para afirmar autoria baseada em Nostr.

## Por Que Importa

O esquema é a camada de interoperabilidade que permite que qualquer identificador Nostr se torne um link funcional fora da interface de um único cliente. Extensões de navegador, manipuladores de SO móvel e shells de desktop podem rotear URIs `nostr:` para qualquer cliente que o usuário tenha instalado, o que torna possível compartilhar um perfil ou evento colando um URI em qualquer lugar sem perder a capacidade de abri-lo de forma nativa ao Nostr.

## Implementações

O suporte para URIs `nostr:` é amplo no ecossistema de clientes, incluindo os principais clientes Nostr web, móvel e desktop. Extensões de navegador como [nos2x](https://github.com/fiatjaf/nos2x) e [Alby](https://github.com/getAlby/lightning-browser-extension) manipulam registro de URI em navegadores de desktop.

---

**Fontes primárias:**

- [Especificação NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md)

**Mencionado em:**

- [Boletim #19: Nostrability migra para NIP-34](/pt/newsletters/2026-04-22-newsletter/#nostrability-migrates-to-nip-34-and-opens-19-per-nip-interop-trackers)

**Veja também:**

- [NIP-19: Entidades codificadas em bech32](/pt/topics/nip-19/)
- [NIP-23: Conteúdo de formato longo](/pt/topics/nip-23/)
