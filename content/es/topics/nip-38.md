---
title: "NIP-38: Estados de usuario"
date: 2026-08-26
translationOf: /en/topics/nip-38.md
translationDate: 2026-08-26
draft: false
description: "Define eventos de estado de usuario de corta duración, incluidas las categorías de estado general y musical."
---

NIP-38 define eventos direccionables kind 30315 para estados breves de usuario. Un tag `d` identifica la categoría del estado, como `general` o `music`, mientras tags `r` y `p` opcionales pueden enlazar a una URL o identificar a un artista. Los clientes pueden usar el tag `expiration` del evento para dejar de mostrar estados obsoletos.

## Cómo funciona

Un usuario publica un evento kind 30315 con el texto del estado en `content`. El evento es direccionable por pubkey, kind y tag `d`, así que un evento más reciente de la misma categoría sustituye al anterior. Un campo de contenido vacío borra ese estado.

---

**Fuentes primarias:**
- [Especificación de NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) - Estados de usuario

**Mencionado en:**
- [Newsletter #37: NoorNote v1.3.6: estados de perfil y anuncios clasificados](/es/newsletters/2026-08-26-newsletter/#noornote-v136-estados-de-perfil-y-anuncios-clasificados)
