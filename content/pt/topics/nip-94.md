---
title: 'NIP-94: Metadados de arquivo'
date: 2025-12-31
draft: false
categories:
  - Media
  - Protocol
translationOf: /en/topics/nip-94.md
translationDate: 2026-04-22
---

NIP-94 define um evento de metadados de arquivo, kind 1063, para organizar e classificar arquivos compartilhados no Nostr, permitindo que relays filtrem e organizem conteúdo com eficiência.

## Como funciona

A NIP-94 usa o kind `1063` como um evento autônomo de metadados para um arquivo. O `content` do evento contém uma descrição legível por humanos, enquanto tags carregam campos legíveis por máquina, como URL de download, tipo MIME, hashes, dimensões e hints de preview.

Essa separação importa porque o evento de metadados pode ser indexado, filtrado e reutilizado independentemente de qualquer nota que faça link para o arquivo. Um cliente pode tratar um evento kind `1063` como a descrição canônica de um asset em vez de raspar metadados de texto livre em um post.

## Tags obrigatórias e opcionais

**Tags centrais:**
- `url` - link de download do arquivo
- `m` - tipo MIME, com formato em lowercase obrigatório
- `x` - hash SHA-256 do arquivo

**Tags opcionais:**
- `ox` - hash SHA-256 do arquivo original antes de transformações do servidor
- `size` - tamanho do arquivo em bytes
- `dim` - dimensões, largura x altura, para imagem ou vídeo
- `magnet` - URI magnet para distribuição por torrent
- `i` - infohash do torrent
- `blurhash` - imagem placeholder para previews
- `thumb` - URL de thumbnail
- `image` - URL de imagem de preview
- `summary` - trecho de texto
- `alt` - descrição de acessibilidade
- `fallback` - fontes alternativas de download
- `service` - protocolo de armazenamento ou tipo de serviço, como NIP-96

As tags `ox` e `x` são fáceis de ignorar, mas úteis na prática. `ox` identifica o arquivo original enviado, enquanto `x` pode identificar a versão transformada que um servidor realmente serve. Quando um host de mídia comprime ou redimensiona uploads, clientes ainda conseguem preservar a identidade do arquivo original sem fingir que o blob transformado é byte a byte idêntico.

## Quando usar

A NIP-94 foi desenhada para aplicações de compartilhamento de arquivos, e não para clientes sociais ou de conteúdo longform. Aplicações sugeridas incluem:

- relays de indexação de torrents
- plataformas de compartilhamento de portfólio, no estilo Pinterest
- distribuição de configuração e updates de software
- bibliotecas e arquivos de mídia

Se os metadados do arquivo só precisarem decorar uma URL embutida dentro de outro evento, a [NIP-92: Media Attachments](/pt/topics/nip-92/) é mais leve. A NIP-94 é a melhor escolha quando o próprio arquivo deve ser consultável como objeto de primeira classe.

## Notas de interoperabilidade

A NIP-94 funciona em diferentes backends de armazenamento. Um arquivo pode ser enviado via [NIP-96: HTTP File Storage](/pt/topics/nip-96/), Blossom ou outro serviço, e ainda assim ser descrito com o mesmo formato de evento kind `1063`. É por isso que o formato de metadados sobrevive a qualquer protocolo individual de upload.

---

**Fontes primárias:**
- [Especificação NIP-94](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Mencionado em:**
- [Newsletter #3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/)
- [Newsletter #14: NIP Deep Dive](/pt/newsletters/2026-03-18-newsletter/)

**Veja também:**
- [NIP-92: Media Attachments](/pt/topics/nip-92/)
- [Blossom](/pt/topics/blossom/)
