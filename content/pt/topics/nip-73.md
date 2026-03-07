---
title: 'NIP-73: IDs de conteúdo externo'
date: 2026-02-04
draft: false
categories:
- Protocol
- Discovery
- Metadata
translationOf: /en/topics/nip-73.md
translationDate: '2026-03-07'
---

O NIP-73 define uma forma padrão de fazer referência a conteúdo externo dentro de eventos Nostr. Ele usa `i` tags para o próprio identificador e `k` tags para o tipo de identificador, para que os clientes possam agrupar discussões em torno do mesmo livro, site, episódio de podcast, localização, hashtag ou objeto blockchain.

## Como funciona

Um evento usando NIP-73 inclui um `i` tag contendo um identificador externo normalizado e um `k` tag descrevendo qual é o identificador kind. Os clientes podem então consultar todos os eventos que fazem referência ao mesmo assunto.

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

A especificação cobre várias famílias de identificadores, incluindo:

- URLs da web normalizados sem fragmento
- ISBNs para livros
- ISANs para filmes
- geohashes e códigos de país ou subdivisão ISO 3166
- feed de podcast, episódio e GUIDs do editor
- hashtags
- transações blockchain e identificadores de endereço

## Regras de normalização

O principal detalhe voltado para o leitor no NIP-73 é a normalização. O mesmo assunto deve ser mapeado para uma string canônica, caso contrário, os clientes dividirão a discussão em vários identificadores que significam a mesma coisa.

Exemplos da especificação:

- geohashes usam `geo:<value>` e devem estar em letras minúsculas
- os códigos de país e subdivisão usam `iso3166:<code>` e devem estar em letras maiúsculas
- ISBNs omitem hífens
- URLs da web descartam fragmentos
- hashes de transação blockchain usam hexadecimal minúsculo

Parece pouco, mas é a diferença entre uma conversa compartilhada e vários índices incompatíveis.

## Padrões úteis

NIP-73 é uma camada de referência geral, não um formato de conteúdo. Uma nota longa pode apontar para um ISBN de livro, uma resenha pode apontar para um ISAN de filme e uma postagem local pode apontar para um geohash ou código de país sem inventar um tag personalizado a cada vez.

A especificação também permite uma dica de URL opcional como o segundo valor de `i` tag. Isso fornece aos clientes um link alternativo quando eles não possuem um renderizador personalizado para o tipo de identificador.

## Por que é importante

A Nostr já possui fortes referências internas para eventos e perfis. O NIP-73 estende essa ideia para coisas fora do Nostr. Depois que os identificadores são normalizados, comentários, classificações, destaques e afirmações confiáveis ​​podem ser anexados ao mesmo assunto externo em clientes diferentes.

É também por isso que o NIP-85 se baseia no NIP-73. As asserções confiáveis ​​podem avaliar não apenas usuários e eventos, mas também identificadores NIP-73, como livros, sites, hashtags e locais.

---

**Fontes primárias:**
- [Especificação NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Adiciona códigos de país e subdivisão ISO 3166

**Mencionado em:**
- [Boletim informativo nº 8: Atualizações do NIP](/pt/newsletters/2026-02-04-newsletter/#nip-updates)
- [Boletim informativo nº 10: Aprofundamento do NIP-85](/pt/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)

**Veja também:**
- [NIP-85: Asserções confiáveis](/pt/topics/nip-85/)
