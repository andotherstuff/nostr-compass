---
title: "NIP-39: Identidades Externas en Perfiles"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 define cómo los usuarios adjuntan claims de identidad externa a sus perfiles de Nostr usando tags `i`. Estos tags vinculan una pubkey de Nostr a cuentas en plataformas externas como GitHub, Twitter, Mastodon o Telegram.

## Cómo Funciona

Los usuarios publican claims de identidad en eventos kind 10011 como tags `i`. Cada tag contiene un valor `plataforma:identidad` más un puntero de prueba que permite al cliente verificar el claim:

```json
{
  "kind": 10011,
  "tags": [
    ["i", "github:username", "gist-id"],
    ["i", "twitter:handle", "tweet-id"]
  ]
}
```

Los clientes reconstruyen la URL de prueba a partir de la plataforma y el valor de prueba, luego verifican que la publicación externa contiene el `npub` del usuario. Eso mantiene el claim portable entre clientes sin requerir un verificador central.

## Modelo de Prueba

El detalle importante es que NIP-39 demuestra control de dos identidades a la vez: la clave Nostr y la cuenta externa. Si cualquier lado de esa prueba desaparece, la verificación se debilita. Un gist o tweet eliminado no invalida el evento histórico, pero sí elimina la prueba en vivo de la que dependen la mayoría de los clientes.

Otro punto útil de implementación es la estrategia de obtención. Como los claims ahora viven fuera del kind 0, los clientes pueden decidir si solicitarlos solo en vistas de detalle de perfil, solo para usuarios seguidos, o no hacerlo en absoluto. Eso evita añadir más peso al ya concurrido path del kind 0.

## Estado Actual

Según la especificación actual, los claims de identidad viven en eventos kind 10011 dedicados en lugar de metadatos kind 0. Esa separación surgió del esfuerzo más amplio por reducir las consultas de perfil del kind 0.

---

**Fuentes primarias:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - Movió claims de identidad fuera del kind 0

**Mencionado en:**
- [Newsletter #9: Actualizaciones de NIPs](/en/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12: Amethyst](/en/newsletters/2026-03-04-newsletter/#amethyst-nip-39-nip-c0-nip-66)

**Ver también:**
- [NIP-05: Verificación Basada en DNS](/es/topics/nip-05/)
