---
title: "NIP-68: Feeds que priorizam imagens"
date: 2026-07-29
draft: false
categories:
  - Media
  - Protocol
translationOf: /en/topics/nip-68.md
translationDate: 2026-07-29
---

NIP-68 define events endereçáveis de imagens. Ele oferece aos clientes uma forma portátil de publicar metadados de imagens, legendas, rótulos e referências a arquivos de imagem, mantendo o próprio event separado do armazenamento de blobs.

## Como funciona

Uma imagem usa o kind `20` e contém uma tag `title`, com uma descrição em `content`. A tag `imeta` descreve cada imagem com campos como `url`, `m` para o tipo MIME, `dim` para as dimensões, texto `alt` e um hash SHA-256 opcional. Várias tags `imeta` permitem que um event represente um conjunto de imagens.

O event pode incluir tags `p` para pessoas retratadas ou creditadas, tags `t` para tópicos e referências Nostr comuns. Também pode incluir tags de tipo de mídia, hash, localização e aviso de conteúdo para que os clientes filtrem e renderizem publicações com imagens de forma consistente.

NIP-68 não determina um backend de armazenamento. Os clientes podem referenciar URLs HTTPS comuns ou um sistema endereçado por conteúdo como o Blossom, desde que publiquem metadados `imeta` suficientes para que outro cliente exiba e verifique a imagem.

## Implementações

[NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0) adicionou tags de imagem NIP-68 junto com seus recursos de cliente voltados a imagens.

---

**Fontes primárias:**
- [Especificação NIP-68](https://github.com/nostr-protocol/nips/blob/master/68.md)
- [NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0)

**Mencionado em:**
- [Newsletter #33: Lançamentos com tag](/pt/newsletters/2026-07-29-newsletter/#tagged-releases)

**Veja também:**
- [Protocolo Blossom](/pt/topics/blossom/)
- [NIP-94: Metadados de arquivos](/pt/topics/nip-94/)
