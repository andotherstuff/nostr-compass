---
title: "NIP-30: Emoji Personalizado"
date: 2026-03-04
draft: false
categories:
  - NIP
  - Social
translationOf: /en/topics/nip-30.md
translationDate: 2026-03-04
---

NIP-30 define como clientes exibem emoji personalizado em eventos Nostr. Emojis personalizados são referenciados no conteúdo do evento usando shortcodes (`:shortcode:`) e resolvidos através de tags `emoji` que mapeiam cada shortcode para uma URL de imagem.

## Como Funciona

Um evento usando emoji personalizado inclui tags `emoji` junto com as referências de shortcode no conteúdo:

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

Clientes substituem `:gleam:` e `:nostrich:` no conteúdo renderizado por imagens inline das URLs especificadas. Shortcodes devem ser alfanuméricos (com separadores de sublinhado permitidos), e as URLs de imagem devem apontar para imagens pequenas e quadradas adequadas para exibição inline.

## Conjuntos de Emoji

Emojis personalizados podem ser organizados em conjuntos nomeados publicados como eventos substituíveis parametrizados kind 30030. Cada conjunto agrupa emojis relacionados sob um identificador de tag `d`:

```json
{
  "kind": 30030,
  "tags": [
    ["d", "nostr-animals"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"],
    ["emoji", "nostrcat", "https://example.com/nostrcat.png"]
  ]
}
```

Uma atualização de março de 2026 ([PR #2247](https://github.com/nostr-protocol/nips/pull/2247)) adicionou referências opcionais de endereço de conjunto de emoji nas tags de emoji, permitindo que clientes abram o conjunto de origem para navegação ou favoritos quando um usuário clica em um emoji.

## Reações

Emojis personalizados NIP-30 também funcionam em eventos de reação kind 7. Uma reação com `content` definido como um shortcode e uma tag `emoji` correspondente renderiza como uma reação de emoji personalizado no evento referenciado:

```json
{
  "kind": 7,
  "content": ":fire:",
  "tags": [
    ["emoji", "fire", "https://example.com/fire.gif"],
    ["e", "<event-id>"]
  ]
}
```

---

**Fontes primárias:**
- [Especificação NIP-30](https://github.com/nostr-protocol/nips/blob/master/30.md)
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - Endereço de conjunto de emoji nas tags

**Mencionado em:**
- [Newsletter #12: NoorNote v0.5.x](/pt/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [Newsletter #12: Atualizações de NIPs](/pt/newsletters/2026-03-04-newsletter/#atualizações-de-nips)
