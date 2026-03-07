---
title: 'NIP-84: Destaques'
date: 2026-02-18
draft: false
categories:
- Content
- Protocol
translationOf: /en/topics/nip-84.md
translationDate: '2026-03-07'
---

NIP-84 define eventos de "destaque" kind 9802 que permitem aos usuários marcar e compartilhar passagens que consideram valiosas de conteúdo longo no Nostr.

## Como funciona

O campo `.content` contém o texto destacado. Os eventos fazem referência ao material de origem usando `a` ou `e` tags para conteúdo nativo do Nostr ou `r` tags para URLs externos (os clientes devem remover os parâmetros de rastreamento). `p` tags opcional atribui autores originais, e um `context` tag opcional fornece texto circundante quando o destaque é uma parte de uma passagem maior.

Para mídia não textual, o conteúdo destacado pode estar vazio. Isso dá aos clientes uma maneira de apontar para um destaque de áudio ou vídeo enquanto mantém a referência da fonte em tags.

## Destaques das citações

Os usuários podem adicionar um `comment` tag para criar destaques de citações, que são renderizados como republicações citadas. Isso evita entradas duplicadas em clientes de microblog. Nos comentários, as menções `p`-tag exigem um atributo "menção" para distingui-las das atribuições do autor/editor, e os URLs `r`-tag usam um atributo "fonte" para referências de origem.

## Por que é importante

O NIP-84 separa a passagem destacada da discussão circundante. Um cliente pode renderizar o texto selecionado como objeto principal e, em seguida, tratar os comentários como metadados opcionais, em vez de misturar ambos em uma nota normal.

Isso é útil para ferramentas de leitura e pesquisa porque preserva o trecho exato. Dois leitores podem comentar o mesmo artigo e ainda produzir eventos de destaque portáteis que outros clientes entendam.

## Notas de interoperabilidade

Atribuição tags são mais importantes do que parecem. Um `p` tag com uma função `author` ou `editor` informa aos clientes quem criou o material de origem, enquanto uma função `mention` dentro de um comentário de citação significa algo diferente. Se os clientes agruparem esses casos, eles poderão rotular incorretamente a fonte destacada ou notificar as pessoas incorretamente.

---

**Fontes primárias:**
- [Especificação NIP-84](https://github.com/nostr-protocol/nips/blob/master/84.md)

**Mencionado em:**
- [Boletim Informativo nº 10: Lançamentos](/pt/newsletters/2026-02-18-newsletter/#prism-share-anything-to-nostr-from-android)

**Veja também:**
- [NIP-94: Metadados do arquivo](/pt/topics/nip-94/)
