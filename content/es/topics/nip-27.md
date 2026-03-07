---
title: "NIP-27 (Referencias en Notas de Texto)"
date: 2026-02-04
description: "NIP-27 define cómo referenciar perfiles, notas y otras entidades dentro del contenido de notas usando el esquema URI nostr:."
translationOf: /en/topics/nip-27.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---

NIP-27 especifica cómo incrustar referencias a entidades de Nostr dentro del contenido de notas de texto. Las referencias usan el esquema URI `nostr:` seguido de un identificador codificado en bech32 (npub, note, nevent, nprofile, naddr).

## Cómo Funciona

Al componer una nota que menciona a otro usuario o referencia otro evento, la referencia se incrusta directamente en el contenido:

```
Check out this post by nostr:npub1... about nostr:note1...
```

Los clientes parsean estas referencias y las renderizan de forma apropiada, típicamente como enlaces clicables o tarjetas de perfil en línea. Las entidades referenciadas también pueden reflejarse en tags del evento para indexación o notificaciones, pero la especificación deja eso como opcional.

El NIP también cubre el parseo de hashtags. Los tags prefijados con `#` se extraen y agregan a los tags `t` del evento para búsqueda.

## Tipos de Referencias

- `nostr:npub1...` - Referencia a un perfil de usuario
- `nostr:note1...` - Referencia a un evento de nota específico
- `nostr:nevent1...` - Referencia a un evento con pistas de relay
- `nostr:nprofile1...` - Referencia a un perfil con pistas de relay
- `nostr:naddr1...` - Referencia a un evento direccionable

## Por Qué Importa

NIP-27 separa lo que la gente lee de lo que los clientes almacenan. Un usuario puede escribir `@name` en un compositor enriquecido, pero el evento publicado puede contener una referencia estable `nostr:nprofile...` en `content`. Eso hace la referencia portable entre clientes sin depender de la sintaxis de mención de una aplicación.

Otro beneficio práctico es la resiliencia. Un `nostr:nevent...` o `nostr:naddr...` incrustado en texto lleva información suficiente para que otro cliente reconstruya el objetivo incluso si nunca ha visto el renderizado local original.

## Notas de Interoperabilidad

- Usa la forma [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) en el contenido: `nostr:<bech32-id>`
- Agrega tags `p` o `q` solo cuando tu cliente quiera notificaciones de mención o indexación de eventos más fuerte
- No asumas que cada referencia en línea debe convertirse en una relación de respuesta. La especificación deja esa elección al cliente

---

**Fuentes primarias:**

- [Especificación NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Entidades Codificadas en Bech32)](/es/topics/nip-19/) - Define los formatos de codificación usados en referencias

**Mencionado en:**

- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - Corrección en nostr-tools para parseo de hashtags después de saltos de línea

**Ver también:**
- [NIP-18: Reposts](/es/topics/nip-18/)
- [NIP-19: Entidades Codificadas en Bech32](/es/topics/nip-19/)
