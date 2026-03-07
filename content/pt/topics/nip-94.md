---
title: 'NIP-94: Metadados de arquivo'
date: 2025-12-31
draft: false
categories:
- Media
- Protocol
translationOf: /en/topics/nip-94.md
translationDate: '2026-03-07'
---

O NIP-94 define um evento de metadados de arquivo (kind 1063) para organizar e classificar arquivos compartilhados no Nostr, permitindo que relays filtre e organize o conteúdo de forma eficaz.

## Como funciona

NIP-94 usa kind `1063` como um evento de metadados independente para um arquivo. O evento `content` contém uma descrição legível por humanos, enquanto tags carrega campos legíveis por máquina, como URL de download, tipo MIME, hashes, dimensões e dicas de visualização.

Essa separação é importante porque o evento de metadados pode ser indexado, filtrado e reutilizado independentemente de qualquer nota vinculada ao arquivo. Um cliente pode tratar um evento kind `1063` como a descrição canônica de um ativo em vez de extrair metadados do texto da postagem em formato livre.

## Tags obrigatórias e opcionais

**Núcleo tags:**
- `url` - Link para download do arquivo
- `m` - tipo MIME (é necessário formato minúsculo)
- `x` - hash SHA-256 do arquivo

**tags opcional:**
- `ox` - hash SHA-256 do arquivo original antes das transformações do servidor
- `size` - Tamanho do arquivo em bytes
- `dim` - Dimensões (largura x altura) para imagens/vídeo
- `magnet` - URI magnético para distribuição de torrent
- `i` - Infohash de torrent
- `blurhash` - Imagem de espaço reservado para visualizações
- `thumb` - URL da miniatura
- `image` - URL da imagem de visualização
- `summary` - Trecho do texto
- `alt` - Descrição de acessibilidade
- `fallback` - Fontes alternativas de download
- `service` - Protocolo de armazenamento ou tipo de serviço, como NIP-96

O `ox` e o `x` tags são fáceis de ignorar, mas úteis na prática. `ox` identifica o arquivo original carregado, enquanto `x` pode identificar a versão transformada que um servidor realmente atende. Quando um host de mídia compacta ou redimensiona uploads, os clientes ainda podem preservar a identidade do arquivo original sem fingir que o blob transformado é idêntico byte por byte.

## Quando usar

O NIP-94 foi projetado para aplicativos de compartilhamento de arquivos, em vez de clientes de conteúdo social ou de formato longo. As aplicações sugeridas incluem:

- Indexação de torrents relays
- Plataformas de compartilhamento de portfólio (semelhantes ao Pinterest)
- Configuração de software e distribuição de atualizações
- Bibliotecas e arquivos de mídia

Se os metadados do arquivo só precisam decorar uma URL embutida em outro evento, [NIP-92: Media Attachments](/pt/topics/nip-92/) é mais leve. NIP-94 é a melhor escolha quando o próprio arquivo deve ser consultado como um objeto de primeira classe.

## Notas de interoperabilidade

O NIP-94 funciona em back-ends de armazenamento. Um arquivo pode ser carregado através de [NIP-96: HTTP File Storage](/pt/topics/nip-96/), Blossom ou outro serviço, ainda descrito com o mesmo formato de evento kind `1063`. É por isso que o formato de metadados sobrevive a qualquer protocolo de upload único.

---

**Fontes primárias:**
- [Especificação NIP-94](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Mencionado em:**
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Veja também:**
- [NIP-92: Anexos de mídia](/pt/topics/nip-92/)
- [Blossom](/pt/topics/blossom/)
