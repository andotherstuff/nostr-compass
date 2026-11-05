---
title: "NIP-73: IDs de conteúdo externo"
date: 2026-02-04
draft: false
categories:
  - Protocol
  - Discovery
  - Metadata
translationOf: /en/topics/nip-73.md
translationDate: 2026-11-05
---

A NIP-73 define uma forma padrão de referenciar conteúdo externo dentro de eventos Nostr. Ela usa tags `i` para o próprio identificador e tags `k` para o tipo de identificador, para que clientes possam agrupar discussões em torno do mesmo livro, site, episódio de podcast, local, hashtag ou objeto de blockchain. A [especificação atual](https://github.com/nostr-protocol/nips/blob/master/73.md) está marcada como rascunho e opcional.

## Como Funciona {#how-it-works}

Um evento que usa a NIP-73 inclui uma tag `i` com um identificador externo normalizado e uma tag `k` que nomeia a família do identificador. Os clientes podem consultar relays por um assunto exato por meio de `i` ou por uma família inteira por meio de `k`. A NIP-73 não adiciona nenhum kind de evento próprio. Comentários, resenhas e outros eventos carregam as tags.

Fragmento de tag, não um evento completo:

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

Uma página web coloca sua URL normalizada em `i` e define `k` como `web`. A especificação cobre várias famílias de identificadores, incluindo:

- URLs web normalizadas sem fragmento
- ISBNs para livros
- ISANs para filmes
- DOIs
- geohashes e códigos ISO 3166 de países ou subdivisões
- GUIDs de feeds, episódios e publicadores de podcast
- hashtags
- identificadores de transações e endereços de blockchain

## Regras de Normalização {#normalization-rules}

A correspondência depende de strings idênticas, então a especificação define uma forma escrita para cada família. Exemplos da especificação:

- geohashes usam `geo:<value>` e devem estar em minúsculas
- códigos de países e subdivisões usam `iso3166:<code>` e devem estar em maiúsculas
- ISBNs omitem hífens
- DOIs ficam em minúsculas
- URLs web descartam fragmentos
- hashes de transações de blockchain usam hex em minúsculas

A normalização fixa como um único identificador é escrito. Ela não mescla aliases. ISBNs específicos de edição e URLs que se normalizam em strings diferentes continuam sendo identificadores separados, então a discussão sobre um mesmo livro ou artigo ainda pode se espalhar por vários valores `i`.

## Dicas de URL {#url-hints}

Uma tag `i` pode incluir uma dica de URL opcional como terceiro elemento do array, que é o segundo valor depois do nome da tag. Um cliente sem renderizador personalizado para aquele tipo de identificador pode usar a dica como link alternativo.

Fragmento de tag: `["i", "isbn:9780765382030", "<url-hint>"]`

O autor escolhe a dica. Ela não faz parte da identidade, não prova propriedade e não nomeia um site canônico.

## Confiança e Contexto {#trust-and-context}

Dois eventos com o mesmo identificador acabam na mesma conversa, e o identificador compartilhado não estabelece nada além disso. Um evento assinado identifica seu autor. Ele não autentica o livro, o site ou o publicador do podcast que referencia, e não mostra quem os controla.

O significado de uma tag `i` depende do evento. Nos comentários da [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md), `I`/`K` maiúsculas marcam o escopo raiz e `i`/`k` minúsculas marcam o pai. Essa estrutura de thread vem da NIP-22, e a NIP-73 não define nenhum kind de comentário. A [NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md) usa `i` para identidades externas em perfis, então nem toda tag `i` é um assunto NIP-73.

As Trusted Assertions da [NIP-85](/pt/topics/nip-85/) também podem ter como alvo identificadores NIP-73, como livros, sites, hashtags e locais.

## Implementações {#implementations}

O [nip73.rs do rust-nostr no commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) interpreta prefixos conhecidos como um `ExternalContentId` tipado e transforma uma dica opcional em uma URL tipada. Ele escreve o terceiro elemento da tag apenas quando existe uma dica. Seus testes mantêm ISBNs com hífens: o parser remove o prefixo e armazena o restante sem aplicar a normalização da especificação, então o parsing tipado não garante strings canônicas. Ele mantém os IDs de cadeia fora da família, mapeando `ethereum:100:tx:<hash>` para `ethereum:tx`. Essa revisão não tem variante de país `iso3166`.

O [DisplayExternalId.kt do Amethyst no commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) envia identificadores de geohash, hashtag e URL para exibições dedicadas e mostra outros tipos suportados como um chip de escopo genérico. Uma URL abre a rota de thread do próprio app para aquela página. Com as pré-visualizações desativadas, a renderização normal mostra um chip de link simples e não solicita pré-visualização. Com as pré-visualizações ativadas, buscar uma pré-visualização ausente pode contatar o site de destino. Nenhum dos arquivos mostra como uma versão lançada se comporta.

---

**Fontes primárias:**
- [Especificação NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Adiciona códigos ISO 3166 de países e subdivisões
- [nip73.rs do rust-nostr no commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs)
- [DisplayExternalId.kt do Amethyst no commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt)

**Mencionado em:**
- [Newsletter #47: Mergulho em NIP](/pt/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)
- [Newsletter #45](/en/newsletters/2026-10-21-newsletter/#feather)
- [Newsletter #43](/en/newsletters/2026-10-07-newsletter/#protocol-and-spec-work)
- [Newsletter #37: agosto de 2025](/en/newsletters/2026-08-26-newsletter/#august-2025)
- [Newsletter #8: Atualizações de NIPs](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [Newsletter #10: Mergulho na NIP-85](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #36: Comentários (NIP-22)](/en/newsletters/2026-08-19-newsletter/#comments-nip-22)
- [Newsletter #38: Mergulho em NIP](/en/newsletters/2026-09-02-newsletter/#reactions-nip-25)
- [Newsletter #40: filtros de podcast-medium da NIP-73](/en/newsletters/2026-09-16-newsletter/#nip-73-proposes-podcast-medium-filters)
- [Newsletter #42: conteúdo externo de setembro de 2024](/en/newsletters/2026-09-30-newsletter/#september-2024-posts-acquire-richer-context)

**Veja também:**
- [NIP-31: Lidando com tipos de evento desconhecidos](/pt/topics/nip-31/)
- [NIP-22: Comentário](/pt/topics/nip-22/)
- [NIP-39: Identidades externas em perfis](/pt/topics/nip-39/)
- [NIP-85: Trusted Assertions](/pt/topics/nip-85/)
