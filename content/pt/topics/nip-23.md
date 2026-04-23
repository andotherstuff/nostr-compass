---
title: 'NIP-23: Conteúdo de formato longo'
date: 2026-04-08
draft: false
categories:
  - Protocol
translationOf: /en/topics/nip-23.md
translationDate: 2026-04-22
---

NIP-23 define o kind `30023` para conteúdo de formato longo no Nostr. Diferente das notas curtas kind `1`, eventos de formato longo são eventos parameterized replaceable, identificados por uma tag `d`, suportam formatação Markdown e incluem tags de metadados para títulos, resumos, imagens e datas de publicação.

## Como funciona

Um evento de formato longo usa o kind `30023` com uma tag `d` como identificador único, permitindo que o autor atualize o conteúdo publicando um novo evento com a mesma tag `d`. O campo `content` contém texto em Markdown. As tags padrão incluem `title`, `summary`, `image` (URL da imagem de cabeçalho), `published_at` (timestamp Unix da publicação original) e `t` (hashtags). Como o evento é parameterized replaceable, os relays armazenam apenas a versão mais recente por tag `d` para cada autor.

## Tags principais

- `d` - identificador único do artigo (slug)
- `title` - título do artigo
- `summary` - descrição curta
- `image` - URL da imagem de cabeçalho
- `published_at` - timestamp Unix da publicação original, distinto de `created_at`, que muda a cada edição
- `t` - hashtags e tags de tópico

## Implementações

- [Habla](https://habla.news) - leitor e publicador de conteúdo de formato longo
- [YakiHonne](https://yakihonne.com) - plataforma de conteúdo de formato longo
- [Highlighter](https://highlighter.com) - ferramenta de leitura e anotação

---

**Fontes primárias:**
- [Especificação NIP-23](https://github.com/nostr-protocol/nips/blob/master/23.md)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
