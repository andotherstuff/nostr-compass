---
title: "NIP-C7: Mensajes de chat"
date: 2026-04-15
translationOf: /en/topics/nip-c7.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Messaging
---

NIP-C7 define kind `9` como el kind de evento para mensajes de chat. El objetivo es separar el tráfico orientado a chat del tráfico general del feed social, para que los clientes puedan aplicar reglas distintas de UX y moderación a cada contexto.

## Cómo funciona

Un evento kind `9` lleva el contenido del mensaje más etiquetas que identifican el contexto del chat. En los grupos basados en relay de [NIP-29](/es/topics/nip-29/), el evento incluye una etiqueta `h` con el ID del grupo. El threading de respuestas usa etiquetas `q` que hacen referencia a eventos anteriores.

NIP-C7 se centra en dónde deberían renderizarse estos eventos. En lugar de aparecer en feeds globales de notas como las notas de texto kind `1`, los eventos kind `9` están pensados para vistas orientadas a chat donde el estado de la conversación y el threading son explícitos.

## Implementaciones

- [Flotilla](https://gitea.coracle.social/coracle/flotilla) y [Coracle](https://github.com/coracle-social/coracle) usan kind `9` en flujos de trabajo de chat grupal.
- [Amethyst](https://github.com/vitorpamplona/amethyst) incluye soporte para kind `9` en su stack de mensajería.
- [White Noise](https://github.com/marmot-protocol/whitenoise) usa threading de respuesta NIP-C7 con etiquetas `q`.

---

**Fuentes primarias:**
- [Especificación NIP-C7](https://github.com/nostr-protocol/nips/blob/master/C7.md)
- [PR #2310: Restringir kind 9 a vistas de chat](https://github.com/nostr-protocol/nips/pull/2310)

**Mencionado en:**
- [Boletín #18: Actualizaciones de NIP](/en/newsletters/2026-04-15-newsletter/)

**Ver también:**
- [NIP-29: Grupos basados en relay](/es/topics/nip-29/)
- [NIP-17: Mensajes directos privados](/es/topics/nip-17/)
