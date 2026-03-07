---
title: 'NIP-30: Emoji personalizado'
date: 2026-03-04
draft: false
categories:
- NIP
- Social
translationOf: /en/topics/nip-30.md
translationDate: '2026-03-07'
---

O NIP-30 define como os clientes exibem emojis personalizados em eventos Nostr. Emoji personalizados são referenciados no conteúdo do evento usando códigos de acesso (`:shortcode:`) e resolvidos por meio de `emoji` tags mapeando cada código de acesso para um URL de imagem.

## Como funciona

Um evento que usa emoji personalizado inclui `emoji` tags junto com as referências de shortcode no conteúdo:

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

Os clientes substituem `:gleam:` e `:nostrich:` no conteúdo renderizado por imagens embutidas dos URLs especificados. Os códigos de acesso devem ser alfanuméricos (com separadores de sublinhado permitidos) e os URLs das imagens devem apontar para imagens pequenas e quadradas adequadas para exibição in-line.

## Conjuntos de emojis

Emoji personalizados podem ser organizados em conjuntos nomeados publicados como eventos substituíveis parametrizados kind 30030. Cada conjunto agrupa emojis relacionados sob um identificador `d` tag:

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

Uma atualização de março de 2026 ([PR #2247](https://github.com/nostr-protocol/nips/pull/2247)) adicionou referências de endereço de conjunto de emoji opcionais no emoji tags, permitindo que os clientes abram o conjunto de origem para navegação ou marcação quando um usuário clica em um emoji.

## Notas de interoperabilidade

Emoji personalizados são um recurso de apresentação, não uma garantia de transporte. Se um cliente não entender o NIP-30 ou não conseguir buscar o URL da imagem, ele ainda deverá mostrar o texto `:shortcode:` bruto. Essa alternativa é a razão pela qual os códigos de acesso legíveis são importantes.

O tag é evento local, a menos que faça referência a um conjunto. A reutilização de `:fire:` em dois eventos diferentes não implica um significado global compartilhado, a menos que ambos apontem para a mesma imagem ou conjunto. Os clientes devem primeiro resolver a definição de emoji do evento atual.

## Reações

Os emojis personalizados NIP-30 também funcionam em eventos de reação kind 7. Uma reação com `content` definida como um shortcode e um `emoji` tag correspondente é renderizada como uma reação emoji personalizada no evento referenciado:

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
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - Emoji define endereço em tags

**Mencionado em:**
- [Boletim informativo nº 12: NoorNote v0.5.x](/pt/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [Boletim Informativo nº 12: Atualizações do NIP](/pt/newsletters/2026-03-04-newsletter/#nip-updates)
