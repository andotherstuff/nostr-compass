---
title: "NIP-22: Comentarios"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---

NIP-22 define un estándar para comentar en cualquier contenido direccionable de Nostr, habilitando discusiones con hilos sobre artículos, videos, eventos de calendario y otros eventos direccionables.

## Cómo Funciona

Los comentarios usan eventos kind 1111 con `content` en texto plano. Los tags de alcance raíz van en mayúscula, y los tags de respuesta al padre van en minúscula:

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

## Estructura de Tags

- **`A` / `E` / `I`** - Alcance raíz de la discusión: evento direccionable, ID de evento o identificador externo
- **`K`** - Kind o tipo de alcance raíz para ese elemento raíz
- **`P`** - Autor del evento raíz cuando existe
- **`a` / `e` / `i`** - Padre inmediato al que se responde
- **`k`** - Kind o tipo de alcance del elemento padre
- **`p`** - Autor del elemento padre

Para comentarios de nivel superior, la raíz y el padre suelen apuntar al mismo objetivo. Para respuestas a comentarios, la raíz permanece fija mientras los tags en minúscula del padre se mueven al comentario específico que se responde.

## Notas de Interoperabilidad

Los comentarios NIP-22 no son un reemplazo genérico de las respuestas kind 1. La especificación dice explícitamente que los comentarios no deben usarse para responder a notas kind 1. Para hilos nota-a-nota, los clientes deben seguir usando [NIP-10](/es/topics/nip-10/).

Otra distinción útil es el alcance. NIP-22 puede anclar discusiones a recursos que no son notas mediante los tags `I` e `i`, incluyendo URLs y otros identificadores externos de [NIP-73](/es/topics/nip-73/). Eso da a los clientes una forma estándar de adjuntar hilos de comentarios a páginas web, podcasts u otros objetos fuera de Nostr.

## Casos de Uso

- Discusiones de artículos
- Comentarios de videos
- Discusiones de eventos de calendario [NIP-52](/es/topics/nip-52/)
- Páginas de discusión de wiki
- Comentarios sobre recursos externos identificados mediante tags `I`

---

**Fuentes primarias:**
- [Especificación NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md)

**Mencionado en:**
- [Newsletter #7: Notedeck](/en/newsletters/2026-01-28-newsletter/#notedeck)
- [Newsletter #10: AI Agent NIPs Arrive](/en/newsletters/2026-02-18-newsletter/#ai-agent-nips-arrive)
- [Newsletter #12: diVine](/en/newsletters/2026-03-04-newsletter/#divine)

**Ver también:**
- [NIP-10: Reply Threads](/es/topics/nip-10/)
- [NIP-52: Calendar Events](/es/topics/nip-52/)
- [NIP-73: External Content IDs](/es/topics/nip-73/)
