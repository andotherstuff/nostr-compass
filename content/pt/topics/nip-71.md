---
title: "NIP-71: Eventos de Vídeo"
date: 2026-01-13
draft: false
categories:
  - Media
  - Protocol
---

O NIP-71 define kinds de evento para conteúdo de vídeo no Nostr, habilitando compartilhamento de vídeo com suporte adequado a metadados. A especificação cobre tanto eventos de vídeo regulares quanto eventos de vídeo endereçáveis, com os últimos adicionados em janeiro de 2026 para permitir que criadores atualizem metadados de vídeo sem republicar.

## Kinds de Evento

O NIP-71 define quatro kinds de evento divididos em duas categorias baseadas em proporção de aspecto e endereçabilidade.

Eventos de vídeo regulares usam kind 21 para vídeos horizontais (paisagem) e kind 22 para vídeos verticais (retrato/shorts). Estes são eventos Nostr padrão com conteúdo imutável uma vez publicados.

Eventos de vídeo endereçáveis usam kind 34235 para vídeos horizontais e kind 34236 para vídeos verticais. Estes são eventos substituíveis parametrizados identificados pela combinação de pubkey, kind e tag `d`. Publicar um novo evento com os mesmos identificadores substitui a versão anterior, permitindo atualizações de metadados.

## Estrutura

Um evento de vídeo endereçável completo inclui campos de identificação, tags de metadados e a referência do conteúdo de vídeo.

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

A tag `d` fornece um identificador único dentro dos seus vídeos daquele kind, para que você possa ter múltiplos vídeos endereçáveis usando valores `d` diferentes. As tags `title` e `summary` fornecem o título do vídeo e uma descrição curta para exibição nos clientes. A tag `url` aponta para o arquivo de vídeo real, enquanto `thumb` fornece uma imagem de preview. A tag `duration` especifica a duração em segundos, e `dim` opcionalmente especifica as dimensões do vídeo.

A tag `origin` rastreia a plataforma de origem ao importar conteúdo de outros serviços. Isso preserva a proveniência ao migrar vídeos do YouTube, Vimeo ou outras plataformas para hospedagem Nostr.

O campo `content` pode conter uma descrição estendida, transcrição completa ou qualquer texto adicional associado ao vídeo.

## Por que Eventos Endereçáveis Importam

Eventos de vídeo regulares (kinds 21 e 22) são imutáveis uma vez publicados. Se você publicar um vídeo e depois notar um erro de digitação no título, quiser atualizar a miniatura, ou precisar mudar a URL de hospedagem porque migrou para um serviço de vídeo diferente, você não pode modificar o evento original. Sua única opção é publicar um novo evento com um novo ID, o que quebra quaisquer referências existentes e perde métricas de engajamento.

Eventos de vídeo endereçáveis resolvem esse problema tornando o evento substituível. A combinação de sua pubkey, o kind do evento e a tag `d` identifica unicamente seu vídeo. Quando você publica um novo evento com os mesmos identificadores, os relays substituem a versão antiga pela nova. Clientes buscando seu vídeo sempre obtêm os metadados mais recentes.

Isso é particularmente valioso para corrigir erros de metadados após publicar, atualizar miniaturas conforme você melhora sua marca, migrar URLs de hospedagem de vídeo ao trocar de provedores e importar conteúdo de plataformas descontinuadas como Vine enquanto preserva a proveniência através da tag `origin`.

## Implementações

Eventos de vídeo endereçáveis (kinds 34235 e 34236) estão atualmente implementados no Amethyst e nostrvine. Ambos os clientes podem criar, exibir e atualizar eventos de vídeo endereçáveis.

---

**Fontes primárias:**
- [Especificação NIP-71](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - Atualização de eventos de vídeo endereçáveis

**Mencionado em:**
- [Newsletter #5: Atualizações de NIPs](/pt/newsletters/2026-01-13-newsletter/#nip-updates)

**Veja também:**
- [NIP-94: Metadados de Arquivo](/pt/topics/nip-94/)
