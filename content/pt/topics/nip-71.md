---
title: 'NIP-71: Eventos de Vídeo'
date: 2026-01-13
draft: false
categories:
- Media
- Protocol
translationOf: /en/topics/nip-71.md
translationDate: '2026-03-07'
---

NIP-71 define o evento kinds para conteúdo de vídeo no Nostr, permitindo o compartilhamento de vídeo com suporte adequado de metadados. A especificação cobre eventos de vídeo regulares e eventos de vídeo endereçáveis, com o último adicionado em janeiro de 2026 para permitir que os criadores atualizem os metadados do vídeo sem republicá-los.

## Tipos de eventos

O NIP-71 define quatro eventos kinds divididos em duas categorias com base na proporção e endereçamento.

Eventos de vídeo regulares usam kind 21 para vídeos horizontais (paisagem) e kind 22 para vídeos verticais (retrato/shorts). Estes são eventos Nostr padrão com conteúdo imutável uma vez publicados.

Eventos de vídeo endereçáveis ​​usam kind 34235 para vídeos horizontais e kind 34236 para vídeos verticais. Esses são eventos substituíveis parametrizados identificados pela combinação de pubkey, kind e `d` tag. A publicação de um novo evento com os mesmos identificadores substitui a versão anterior, permitindo atualizações de metadados.

## Estrutura

Um evento de vídeo endereçável completo inclui campos de identificação, metadados tags e referência de conteúdo de vídeo.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 34235,
  "tags": [
    ["d", "my-video-2026-01"],
    ["title", "Introduction to Nostr Video"],
    ["summary", "A walkthrough of NIP-71 video events"],
    ["url", "https://example.com/video.mp4"],
    ["thumb", "https://example.com/thumbnail.jpg"],
    ["duration", "300"],
    ["dim", "1920x1080"],
    ["origin", "youtube:dQw4w9WgXcQ"]
  ],
  "content": "Extended description, transcript, or additional notes about the video.",
  "sig": "sig1234..."
}
```

O `d` tag fornece um identificador exclusivo em seus vídeos desse kind, para que você possa ter vários vídeos endereçáveis ​​usando diferentes valores `d`. O `title` e `summary` tags fornecem o título do vídeo e uma breve descrição para exibição nos clientes. O `url` tag aponta para o arquivo de vídeo real, enquanto `thumb` fornece uma imagem de visualização. O `duration` tag especifica a duração em segundos e `dim` especifica opcionalmente as dimensões do vídeo.

O `origin` tag rastreia a plataforma de origem ao importar conteúdo de outros serviços. Isso preserva a procedência ao migrar vídeos do YouTube, Vimeo ou outras plataformas para a hospedagem Nostr.

O campo `content` pode conter uma descrição estendida, uma transcrição completa ou qualquer texto adicional associado ao vídeo.

## Por que eventos endereçáveis ​​são importantes

Eventos de vídeo regulares (kinds 21 e 22) são imutáveis ​​depois de publicados. Se você publicar um vídeo e posteriormente notar um erro de digitação no título, desejar atualizar a miniatura ou precisar alterar o URL de hospedagem porque migrou para um serviço de vídeo diferente, não será possível modificar o evento original. Sua única opção é publicar um novo evento com um novo ID, o que quebra todas as referências existentes e perde métricas de engajamento.

Os eventos de vídeo endereçáveis ​​resolvem esse problema tornando o evento substituível. A combinação do seu pubkey, do evento kind e do `d` tag identifica exclusivamente o seu vídeo. Ao publicar um novo evento com os mesmos identificadores, relays substitui a versão antiga pela nova. Os clientes que buscam seu vídeo sempre recebem os metadados mais recentes.

Isso é particularmente valioso para corrigir erros de metadados após a publicação, atualizar miniaturas à medida que você melhora sua marca, migrar URLs de hospedagem de vídeo ao mudar de provedor e importar conteúdo de plataformas descontinuadas como Vine, preservando a proveniência por meio do `origin` tag.

Um benefício adicional é a vinculação estável. Outros eventos podem continuar se referindo ao mesmo vídeo endereçável enquanto o criador atualiza os detalhes da apresentação em torno dele, o que é mais limpo do que fragmentar comentários e referências em várias republicações imutáveis.

## Compensações

A substituibilidade ajuda na manutenção dos metadados, mas também significa que os clientes precisam decidir quanto estado histórico preservar. Se um criador alterar o título ou resumo após a publicação, o evento mais recente se tornará canônico, mesmo que clientes mais antigos possam ter indexado a versão anterior.

Os kinds 21 e 22 ainda são importantes para aplicativos que desejam um registro de publicação imutável. O NIP-71 não força todos os fluxos de trabalho de vídeo no modelo substituível.

## Implementações

Eventos de vídeo endereçáveis ​​(kinds 34235 e 34236) estão atualmente implementados em Amethyst e nostrvine. Ambos os clientes podem criar, exibir e atualizar eventos de vídeo endereçáveis.

---

**Fontes primárias:**
- [Especificação NIP-71](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - Atualização de eventos de vídeo endereçáveis

**Mencionado em:**
- [Boletim Informativo nº 5: Atualizações do NIP](/pt/newsletters/2026-01-13-newsletter/#nip-updates)
- [Boletim informativo nº 12: NoorNote](/pt/newsletters/2026-03-04-newsletter/)

**Veja também:**
- [NIP-94: Metadados do arquivo](/pt/topics/nip-94/)
