---
title: "NIP-A3: Objetivos de Pago"
date: 2026-09-09
translationOf: /en/topics/nip-a3.md
translationDate: 2026-09-11
draft: false
categories:
  - Protocol
  - Payments
---

NIP-A3 define una forma portátil para que una cuenta de Nostr publique direcciones de pago para múltiples redes y servicios. Un evento reemplazable de tipo `10133` transporta una o más etiquetas `payto`.

## Cómo Funciona

Cada etiqueta tiene la forma `["payto", "<type>", "<address>"]`. El tipo va en minúsculas, como `bitcoin`, `lightning` o `monero`. Los clientes pueden validar los formatos conocidos y generar un URI de pago nativo cuando existe uno; los tipos desconocidos recurren al esquema URI `payto:` del RFC 8905.

El evento declara destinos, no un pago completado ni un zap de Nostr. Los clientes siguen decidiendo qué tipos de pago admiten, cómo validar una dirección y con qué claridad mostrar el destino antes de entregarlo a una billetera.

## Implementaciones

- [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041) ofrece una entrega de pago opcional cuando reconoce un objetivo compatible.
- [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851) asigna los tipos de objetivo permitidos a URIs de pago.
- [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) valida los objetivos de Monero y consulta los relays del autor.

---

**Fuentes primarias:**
- [Especificación de NIP-A3](https://github.com/nostr-protocol/nips/blob/master/A3.md)
- [RFC 8905: El esquema URI payto](https://www.rfc-editor.org/rfc/rfc8905.html)

**Mencionado en:**
- [Boletín #39: Los objetivos de pago de NIP-A3 llegan a tres clientes](/es/newsletters/2026-09-09-newsletter/#nip-a3-payment-targets-reach-three-clients)

**Véase también:**
- [NIP-47: Nostr Wallet Connect](/es/topics/nip-47/)
