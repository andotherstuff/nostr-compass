---
title: "NIP-94: File Metadata"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2025-12-31
draft: false
categories:
  - Mídia
  - Protocolo
---

NIP-94 define um evento de metadados de arquivo (kind 1063) para organizar e classificar arquivos compartilhados no Nostr, permitindo que relays filtrem e organizem conteúdo de forma eficaz.

## Como Funciona

1. O usuário faz upload de um arquivo para um serviço de hospedagem
2. Um evento kind 1063 é publicado com metadados sobre o arquivo
3. O conteúdo do evento contém uma descrição legível por humanos
4. Tags estruturadas fornecem metadados legíveis por máquinas
5. Clientes especializados podem organizar e exibir arquivos sistematicamente

## Tags Obrigatórias e Opcionais

**Tags principais:**
- `url` - Link de download do arquivo
- `m` - MIME type (formato em minúsculas obrigatório)
- `x` - Hash SHA-256 do arquivo

**Tags opcionais:**
- `ox` - Hash SHA-256 do arquivo original antes das transformações do servidor
- `size` - Tamanho do arquivo em bytes
- `dim` - Dimensões (largura x altura) para imagens/vídeo
- `magnet` - Magnet URI para distribuição torrent
- `i` - Infohash do torrent
- `blurhash` - Imagem de placeholder para pré-visualizações
- `thumb` - URL da miniatura
- `image` - URL da imagem de pré-visualização
- `summary` - Trecho de texto
- `alt` - Descrição de acessibilidade
- `fallback` - Fontes alternativas de download

## Casos de Uso

NIP-94 é projetado para aplicações de compartilhamento de arquivos, em vez de clientes de conteúdo social ou de formato longo. Aplicações sugeridas incluem:

- Relays de indexação de torrents
- Plataformas de compartilhamento de portfólios (similar ao Pinterest)
- Distribuição de configuração e atualizações de software
- Bibliotecas e arquivos de mídia

---

**Fontes principais:**
- [Especificação NIP-94](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Mencionado em:**
- [Newsletter #3: Resumo de Dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Veja também:**
- [NIP-92: Anexos de Mídia](/pt/topics/nip-92/)
- [Blossom](/pt/topics/blossom/)
