---
title: "NIP-22: Comentários"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Social
---

NIP-22 define um padrão para comentar em qualquer conteúdo Nostr endereçável, permitindo discussões em threads em artigos, vídeos, eventos de calendário e outros eventos endereçáveis.

## Como Funciona

Comentários usam eventos kind 1111 com tags referenciando o conteúdo sendo comentado:

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["E", "root-event-id", "wss://relay.example"],
    ["K", "30023"]
  ],
  "content": "Ótimo artigo!"
}
```

## Estrutura de Tags

- **Tag `A`**: Referencia o evento endereçável sendo comentado (formato kind:pubkey:d-tag)
- **Tag `E`**: Referencia o ID do evento raiz para threading
- **Tag `K`**: Indica o kind do evento raiz
- **Tag `e`**: Referencia comentário pai para respostas aninhadas

## Diferença do Kind 1

Enquanto notas kind 1 podem responder a outras notas, comentários NIP-22 são especificamente projetados para:

- Conteúdo endereçável (artigos, vídeos, eventos de calendário)
- Manter relacionamentos pai-filho claros
- Permitir moderação e threading em conteúdo de formato longo

## Casos de Uso

- Discussões de artigos
- Comentários de vídeos
- Discussões de eventos de calendário [NIP-52](/pt/topics/nip-52/)
- Páginas de discussão de wiki
- Qualquer tipo de evento endereçável

## Relacionados

- [NIP-01](/pt/topics/nip-01/) - Protocolo Básico (notas kind 1)
- [NIP-52](/pt/topics/nip-52/) - Eventos de Calendário
