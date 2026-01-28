---
title: "NIP-22: Comentarios"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Social
---

NIP-22 define un estándar para comentar en cualquier contenido direccionable de Nostr, permitiendo discusiones en hilos sobre artículos, videos, eventos de calendario y otros eventos direccionables.

## Cómo Funciona

Los comentarios usan eventos kind 1111 con tags referenciando el contenido que se comenta:

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["E", "root-event-id", "wss://relay.example"],
    ["K", "30023"]
  ],
  "content": "¡Excelente artículo!"
}
```

## Estructura de Tags

- **Tag `A`**: Referencia el evento direccionable que se comenta (formato kind:pubkey:d-tag)
- **Tag `E`**: Referencia el ID del evento raíz para hilos
- **Tag `K`**: Indica el kind del evento raíz
- **Tag `e`**: Referencia comentario padre para respuestas anidadas

## Diferencia con Kind 1

Mientras las notas kind 1 pueden responder a otras notas, los comentarios NIP-22 están específicamente diseñados para:

- Contenido direccionable (artículos, videos, eventos de calendario)
- Mantener relaciones claras padre-hijo
- Habilitar moderación e hilos en contenido de formato largo

## Casos de Uso

- Discusiones de artículos
- Comentarios de videos
- Discusiones de eventos de calendario [NIP-52](/es/topics/nip-52/)
- Páginas de discusión de wiki
- Cualquier tipo de evento direccionable

## Relacionado

- [NIP-01](/es/topics/nip-01/) - Protocolo Básico (notas kind 1)
- [NIP-52](/es/topics/nip-52/) - Eventos de Calendario
