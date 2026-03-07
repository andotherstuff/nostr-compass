---
title: 'NIP-22: Comentários'
date: 2026-01-28
draft: false
categories:
- NIP
- Social
translationOf: /en/topics/nip-22.md
translationDate: '2026-03-07'
---

O NIP-22 define um padrão para comentar qualquer conteúdo endereçável do Nostr, permitindo discussões encadeadas em artigos, vídeos, eventos de calendário e outros eventos endereçáveis.

## Como funciona

Os comentários usam eventos kind 1111 com texto simples `content`. O escopo raiz tags está em letras maiúsculas e a resposta pai tags está em minúsculas:

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["K", "30023"],
    ["P", "<root-pubkey>", "wss://relay.example"],
    ["a", "30023:pubkey:article-id", "wss://relay.example"],
    ["e", "<parent-event-id>", "wss://relay.example", "<parent-pubkey>"],
    ["k", "30023"],
    ["p", "<parent-pubkey>", "wss://relay.example"]
  ],
  "content": "Great article!"
}
```

## Estrutura de tags

- **`A` / `E` / `I`** - Escopo raiz da discussão: evento endereçável, ID de evento ou identificador externo
- **`K`** - Tipo ou tipo de escopo raiz para esse item raiz
- **`P`** - Autor do evento raiz quando existir
- **`a` / `e` / `i`** - Pai imediato sendo respondido
- **`k`** – Tipo ou tipo de escopo do item pai
- **`p`** – Autor do item pai

Para comentários de nível superior, a raiz e o pai geralmente apontam para o mesmo destino. Para respostas a comentários, a raiz permanece fixa enquanto o pai minúsculo tags passa para o comentário específico que está sendo respondido.

## Notas de interoperabilidade

Os comentários do NIP-22 não são um substituto genérico para as respostas kind 1. A especificação diz explicitamente que os comentários não devem ser usados ​​para responder às notas kind 1. Para threads nota a nota, os clientes devem continuar usando [NIP-10](/pt/topics/nip-10/).

Outra distinção útil é o escopo. O NIP-22 pode ancorar a discussão em recursos não-notas por meio de `I` e `i` tags, incluindo URLs e outros identificadores externos de [NIP-73](/pt/topics/nip-73/). Isso oferece aos clientes uma maneira padrão de anexar tópicos de comentários a páginas da web, podcasts ou outros objetos fora do Nostr.

## Casos de uso

- Discussões de artigos
- Comentários de vídeo
- [NIP-52](/pt/topics/nip-52/) discussões de eventos da agenda
- Páginas de discussão da página Wiki
- Comentários sobre recursos externos identificados através de `I` tags

---

**Fontes primárias:**
- [Especificação NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md)

**Mencionado em:**
- [Boletim informativo nº 7: Notedeck](/pt/newsletters/2026-01-28-newsletter/#notedeck)
- [Boletim informativo nº 10: Chegada dos NIPs do agente de IA](/pt/newsletters/2026-02-18-newsletter/#ai-agent-nips-arrive)
- [Boletim informativo nº 12: divino](/pt/newsletters/2026-03-04-newsletter/#divine)

**Veja também:**
- [NIP-10: Tópicos de resposta](/pt/topics/nip-10/)
- [NIP-52: Eventos do calendário](/pt/topics/nip-52/)
- [NIP-73: IDs de conteúdo externo](/pt/topics/nip-73/)
