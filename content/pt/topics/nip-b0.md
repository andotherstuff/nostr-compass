---
title: "NIP-B0: Favoritos Web"
date: 2026-05-28
draft: false
translationOf: /en/topics/nip-b0.md
translationDate: 2026-07-01
categories:
  - Protocol
  - Social
---

NIP-B0 define um evento replaceable parametrizado (kind 39701) que publica favoritos web como eventos Nostr de primeira classe. A proposta permite que os usuários construam coleções curadas de favoritos que possam ser descobertas, zapadas e republicadas entre clientes sem depender de um serviço central de favoritos.

## Como funciona

Um favorito é um evento kind 39701 cuja tag `d` é a URL canônica da página favoritada. A semântica de replaceable permite que o autor atualize seu próprio favorito para aquela URL (re-tagueando, atualizando o título, marcando como obsoleto) sem produzir eventos duplicados. O campo content carrega a nota do autor sobre o favorito; as tags carregam título, descrição, imagem e tags de tópico `t` para descoberta.

```json
{
  "kind": 39701,
  "tags": [
    ["d", "https://example.com/an-article-worth-saving"],
    ["title", "Article Title"],
    ["t", "nostr"],
    ["t", "protocol"],
    ["published_at", "1717000000"]
  ],
  "content": "Useful primer on the topic.",
  "pubkey": "...",
  "sig": "..."
}
```

A tag `d` identifica o favorito de forma única por autor, então dois usuários podem favoritar a mesma URL com suas próprias anotações e conjuntos de tags.

## Descoberta e curadoria

Como cada favorito é um evento de primeira classe, qualquer cliente Nostr pode renderizar um feed de favoritos assinando eventos kind 39701 filtrados por tags ou autores. Fluxos de trabalho conduzidos por curadores tornam-se naturais: um curador publica uma lista de favoritos, os leitores seguem a pubkey do curador e os favoritos fluem por qualquer relay que os transporte. Não há um diretório central.

## Implementações

- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) — Cliente web de referência com uma arquitetura de três caixas (curador, indexador, visualizador) e um sistema de tiers financiado por zaps NIP-57 direto ao curador. Implementa NIP-B0 junto com NIP-07, NIP-46, NIP-57, NIP-44, NIP-98, NIP-65 e Blossom BUD-01/BUD-04 para armazenamento de arquivos.

## Notas de confiança e segurança

- Favoritos são públicos por padrão; não publique listas privadas de leitura dessa forma
- A republicação depende dos relays continuarem transportando os eventos; relays efêmeros descartarão favoritos
- A tag `published_at` é declarada pelo publicador, não é verificável

---

**Fontes primárias:**
- [Especificação proposta do NIP-B0](https://github.com/nostr-protocol/nips/pull/2089) — Acompanha o evento proposto de favorito web kind 39701
- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) — Implementação de referência com sistema de tiers para curadores

**Mencionado em:**
- [Newsletter #24: favoritos deepmarks NIP-B0 com publicação monetizada por curador](/pt/newsletters/2026-05-28-newsletter/#deepmarks-nip-b0-bookmarks-with-curator-monetized-publishing)
- [Newsletter #27: Também lançado](/pt/newsletters/2026-06-17-newsletter/#also-shipped)

**Veja também:**
- [NIP-57: Zaps Lightning](/pt/topics/nip-57/)
- [NIP-65: Metadados de Lista de Relays](/pt/topics/nip-65/)
