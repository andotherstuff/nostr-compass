---
title: "NIP-21: Esquema URI nostr:"
date: 2026-04-22
translationOf: /en/topics/nip-21.md
translationDate: 2026-04-23
draft: false
categories:
  - Protocol
  - Interoperability
---

NIP-21 define el esquema URI `nostr:`, una forma estándar para que aplicaciones, sitios web y sistemas operativos registren interés en abrir identificadores Nostr tales como `npub`, `nprofile`, `nevent` y `naddr` a través del cliente Nostr que el usuario haya registrado como manejador.

## Cómo Funciona

Un URI `nostr:` es el prefijo del esquema seguido por cualquiera de los identificadores bech32 de [NIP-19](/es/topics/nip-19/) excepto `nsec`. Los clientes y sistemas operativos tratan el esquema de la misma manera que tratan `mailto:` o `tel:`: registrarse como manejador permite al usuario hacer clic en un enlace `nostr:` en cualquier lugar del sistema y abrirlo en su cliente Nostr elegido.

Ejemplos de la especificación:

- `nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9` apunta a un perfil de usuario
- `nostr:nprofile1...` apunta a un perfil de usuario con pistas de relay incluidas
- `nostr:nevent1...` apunta a un evento específico con pistas de relay
- `nostr:naddr1...` apunta a un evento reemplazable parametrizado (como un artículo de forma larga)

## Vinculación de Páginas HTML a Entidades Nostr

NIP-21 también especifica dos convenciones útiles de `<link>` para páginas web que corresponden a entidades Nostr. Una página que sirve el mismo contenido que un evento Nostr (por ejemplo, un artículo de blog renderizado desde un artículo [NIP-23](/es/topics/nip-23/) `kind:30023`) puede incluir un `<link rel="alternate">` apuntando al URI de Nostr. Una página de perfil puede incluir un `<link rel="me">` o `<link rel="author">` apuntando a un `nprofile` para afirmar autoría basada en Nostr.

## Por Qué Es Importante

El esquema es la capa de interoperabilidad que permite que cualquier identificador Nostr sea un enlace funcional fuera de la interfaz de usuario de un solo cliente. Las extensiones del navegador, los manejadores del sistema operativo móvil y los shells de escritorio pueden todos enrutar URIs `nostr:` al cliente que el usuario haya instalado, lo que hace posible compartir un perfil o evento pegando un URI en cualquier lugar sin perder la capacidad de abrirlo de manera nativa a Nostr.

## Implementaciones

El soporte para URIs `nostr:` es amplio en todo el ecosistema de clientes, incluyendo los principales clientes Nostr web, móviles y de escritorio. Las extensiones del navegador tales como [nos2x](https://github.com/fiatjaf/nos2x) y [Alby](https://github.com/getAlby/lightning-browser-extension) manejan el registro de URI en navegadores de escritorio.

---

**Fuentes primarias:**

- [Especificación NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md)

**Mencionado en:**

- [Newsletter #19: Nostrability migra a NIP-34](/es/newsletters/2026-04-22-newsletter/#nostrability-migrates-to-nip-34-and-opens-19-per-nip-interop-trackers)

**Ver también:**

- [NIP-19: Entidades codificadas en bech32](/es/topics/nip-19/)
- [NIP-23: Contenido de forma larga](/es/topics/nip-23/)
