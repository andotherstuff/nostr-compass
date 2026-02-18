---
title: "NIP-84: Highlights"
date: 2026-02-18
translationOf: /en/topics/nip-84.md
translationDate: 2026-02-18
draft: false
categories:
  - Content
  - Protocol
---

O NIP-84 define eventos kind 9802 de "highlight" que permitem que usuários marquem e compartilhem trechos que consideram valiosos de conteúdo de forma longa no Nostr.

## Como Funciona

O campo `.content` contém o texto em destaque. Eventos referenciam seu material-fonte usando tags `a` ou `e` para conteúdo nativo do Nostr, ou tags `r` para URLs externas (clientes devem remover parâmetros de rastreamento). Tags `p` opcionais atribuem autores originais, e uma tag `context` opcional fornece o texto ao redor quando o highlight é uma parte de um trecho maior.

## Quote Highlights

Usuários podem adicionar uma tag `comment` para criar quote highlights, que são renderizados como quote reposts. Isso evita entradas duplicadas em clientes de microblog. Dentro dos comentários, menções por tag `p` requerem um atributo "mention" para distingui-las de atribuições de autor/editor, e URLs por tag `r` usam um atributo "source" para referências de origem.

---

**Fontes primárias:**
- [Especificação NIP-84](https://github.com/nostr-protocol/nips/blob/master/84.md)

**Mencionado em:**
- [Compass #10: Lançamentos](/pt/newsletters/2026-02-18-newsletter/#prism-compartilhe-qualquer-coisa-no-nostr-a-partir-do-android)

**Veja também:**
- [NIP-94: Metadados de Arquivo](/pt/topics/nip-94/)
