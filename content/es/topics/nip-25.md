---
title: "NIP-25: Reacciones"
date: 2026-07-29
translationOf: /en/topics/nip-25.md
translationDate: 2026-08-26
draft: false
categories:
  - Protocol
  - Social
---

NIP-25 define las reacciones como eventos kind `7`. Da a los clientes una forma de evento compartida para adjuntar un emoji u otra reacción breve a una nota, un artículo, un anuncio clasificado u otro evento referenciado.

## Cómo funciona

Un evento de reacción lleva su texto de reacción en `content` y referencia el objetivo mediante el tag `e` del evento objetivo. Cuando el objetivo es direccionable, la reacción incluye además su tag `a`. También incluye tags `p` para el autor del evento referenciado, lo que permite a relays y clientes enrutar notificaciones sin inferir los destinatarios a partir del contenido del evento.

La reacción por defecto es `+`, así que los clientes pueden tratar un contenido de reacción vacío como una respuesta positiva. Otros emoji son valores de reacción válidos. La especificación también permite `-` para una reacción negativa, que el añadido de julio de 2022 incorporó tras la introducción original.

Los clientes deberían preservar la referencia al objetivo y los tags de autor al crear una reacción. Una reacción es un evento firmado ordinario, así que puede viajar por suscripciones normales de relay y ser renderizada por cualquier cliente que reconozca kind `7`.

## Implementaciones

NIP-25 está ampliamente implementado por clientes y bibliotecas de Nostr como parte de la interacción ordinaria con notas. Su modelo simple de kind y tags permite a los clientes mostrar recuentos, reacciones individuales y notificaciones sin un protocolo de transporte aparte.

---

**Fuentes primarias:**
- [NIP-25 Specification](https://github.com/nostr-protocol/nips/blob/master/25.md)
- [Commit de introducción](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88)
- [Añadido de voto negativo](https://github.com/nostr-protocol/nips/commit/89bb08ba8683)

**Mencionado en:**
- [Newsletter #33: Seis julios en la historia de Nostr](/es/newsletters/2026-07-29-newsletter/#seis-julios-en-la-historia-de-nostr)
- [Newsletter #37: Marmot](/es/newsletters/2026-08-26-newsletter/#marmot)

**Véase también:**
- [NIP-01: Basic Protocol](/es/topics/nip-01/)
- [NIP-10: Text Note Threading](/es/topics/nip-10/)
