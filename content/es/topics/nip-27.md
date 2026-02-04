---
title: "NIP-27 (Referencias de Notas de Texto)"
date: 2026-02-04
description: "NIP-27 define cómo referenciar perfiles, notas y otras entidades dentro del contenido de notas usando el esquema URI nostr:."
---

NIP-27 especifica cómo incrustar referencias a entidades de Nostr dentro del contenido de notas de texto. Las referencias usan el esquema URI `nostr:` seguido de un identificador codificado en bech32 (npub, note, nevent, nprofile, naddr).

## Cómo Funciona

Al componer una nota que menciona a otro usuario o referencia otro evento, la referencia se incrusta directamente en el contenido:

```
Mira esta publicación de nostr:npub1... sobre nostr:note1...
```

Los clientes parsean estas referencias y las renderizan apropiadamente, típicamente como enlaces clicables o tarjetas de perfil en línea. Las entidades referenciadas también se agregan a las etiquetas del evento para indexación y propósitos de notificación.

El NIP también cubre el parseo de hashtags. Las etiquetas prefijadas con `#` se extraen y agregan a las etiquetas `t` del evento para búsqueda.

## Tipos de Referencias

- `nostr:npub1...` - Referencia a un perfil de usuario
- `nostr:note1...` - Referencia a un evento de nota específico
- `nostr:nevent1...` - Referencia a un evento con pistas de relay
- `nostr:nprofile1...` - Referencia a un perfil con pistas de relay
- `nostr:naddr1...` - Referencia a un evento direccionable

## Implementaciones

Todos los clientes principales de Nostr implementan NIP-27:
- Los parseadores de texto extraen referencias durante la composición
- Los renderizadores muestran referencias como elementos interactivos
- Los sistemas de notificación usan las etiquetas asociadas

## Fuentes Primarias

- [Especificación NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Entidades Codificadas en Bech32)](/es/topics/nip-19/) - Define los formatos de codificación usados en referencias

## Mencionado En

- [Boletín #8 (2026-02-04)](/es/newsletters/2026-02-04-newsletter/) - Corrección en nostr-tools para parseo de hashtags después de saltos de línea
