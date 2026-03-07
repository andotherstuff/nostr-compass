---
title: NIP-27 (referências de notas de texto)
date: 2026-02-04
draft: false
description: 'O NIP-27 define como fazer referência a perfis, notas e outras entidades
  no conteúdo da nota usando o esquema nostr: URI.'
categories:
- NIP
- Social
translationOf: /en/topics/nip-27.md
translationDate: '2026-03-07'
---

O NIP-27 especifica como incorporar referências a entidades Nostr no conteúdo das notas de texto. As referências usam o esquema URI `nostr:` seguido por um identificador codificado em bech32 (npub, note, nevent, nprofile, naddr).

## Como funciona

Ao redigir uma nota que mencione outro usuário ou faça referência a outro evento, a referência é incorporada diretamente no conteúdo:

```
Check out this post by nostr:npub1... about nostr:note1...
```

Os clientes analisam essas referências e as renderizam adequadamente, normalmente como links clicáveis ​​ou cartões de perfil embutidos. As entidades referenciadas também podem ser espelhadas no evento tags para indexação ou notificações, mas a especificação deixa isso opcional.

O NIP também cobre a análise de hashtag. Tags prefixadas com `#` são extraídas e adicionadas ao `t` tags do evento para pesquisa.

## Tipos de referência

- `nostr:npub1...` - Referência a um perfil de usuário
- `nostr:note1...` - Referência a um evento de nota específico
- `nostr:nevent1...` - Referência a um evento com dicas de relay
- `nostr:nprofile1...` - Referência a um perfil com dicas de relay
- `nostr:naddr1...` - Referência a um evento endereçável

## Por que é importante

O NIP-27 separa o que as pessoas leem do que os clientes armazenam. Um usuário pode digitar `@name` em um compositor rico, mas o evento publicado ainda pode conter uma referência `nostr:nprofile...` estável em `content`. Isso torna a referência portátil entre clientes sem depender da sintaxe de menção de um aplicativo.

Outro benefício prático é a resiliência. Um `nostr:nevent...` ou `nostr:naddr...` bruto incorporado no texto ainda carrega informações suficientes para outro cliente reconstruir o alvo, mesmo que nunca tenha visto a renderização local original.

## Notas de interoperabilidade

- Utilizar o formulário [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) no próprio conteúdo: `nostr:<bech32-id>`
- Adicione `p` ou `q` tags somente quando seu cliente desejar notificações de menção ou indexação de eventos mais forte
- Não presuma que toda referência in-line deva se tornar um relacionamento de resposta. A especificação deixa essa escolha para o cliente

---

**Fontes primárias:**

- [Especificação NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Entidades Codificadas Bech32)](/pt/topics/nip-19/) - Define os formatos de codificação usados nas referências

**Mencionado em:**

- [Newsletter #8 (2026-02-04)](/pt/newsletters/2026-02-04-newsletter/) - correção de nostr-tools para análise de hashtag após novas linhas

**Veja também:**
- [NIP-18: Repostagens](/pt/topics/nip-18/)
- [NIP-19: Entidades codificadas em Bech32](/pt/topics/nip-19/)
