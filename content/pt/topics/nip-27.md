---
title: "NIP-27 (Referências em Notas de Texto)"
date: 2026-02-04
description: "NIP-27 define como referenciar perfis, notas e outras entidades dentro do conteúdo de notas usando o esquema de URI nostr:."
---

NIP-27 especifica como incorporar referências a entidades Nostr dentro do conteúdo de notas de texto. Referências usam o esquema de URI `nostr:` seguido de um identificador codificado em bech32 (npub, note, nevent, nprofile, naddr).

## Como Funciona

Ao compor uma nota que menciona outro usuário ou referencia outro evento, a referência é incorporada diretamente no conteúdo:

```
Confira este post de nostr:npub1... sobre nostr:note1...
```

Clientes analisam essas referências e as renderizam apropriadamente, tipicamente como links clicáveis ou cards de perfil inline. As entidades referenciadas também são adicionadas às tags do evento para indexação e propósitos de notificação.

O NIP também cobre análise de hashtags. Tags prefixadas com `#` são extraídas e adicionadas às tags `t` do evento para pesquisabilidade.

## Tipos de Referência

- `nostr:npub1...` - Referência a um perfil de usuário
- `nostr:note1...` - Referência a um evento de nota específico
- `nostr:nevent1...` - Referência a um evento com dicas de relay
- `nostr:nprofile1...` - Referência a um perfil com dicas de relay
- `nostr:naddr1...` - Referência a um evento endereçável

## Implementações

Todos os principais clientes Nostr implementam NIP-27:
- Parsers de texto extraem referências durante a composição
- Renderizadores exibem referências como elementos interativos
- Sistemas de notificação usam as tags associadas

## Fontes Primárias

- [Especificação NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Entidades Codificadas em Bech32)](/pt/topics/nip-19/) - Define os formatos de codificação usados em referências

## Mencionado Em

- [Newsletter #8 (2026-02-04)](/pt/newsletters/2026-02-04-newsletter/) - Correção no nostr-tools para análise de hashtags após quebras de linha
