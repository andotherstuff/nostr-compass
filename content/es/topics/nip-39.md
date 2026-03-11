---
title: "NIP-39: Identidades externas en perfiles"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 define cómo los usuarios adjuntan claims de identidad externa a sus perfiles de Nostr usando etiquetas `i`. Estas etiquetas vinculan una pubkey de Nostr con cuentas en plataformas externas como GitHub, Twitter, Mastodon o Telegram.

## Cómo funciona

Los usuarios publican claims de identidad en eventos kind 10011 como etiquetas `i`. Cada etiqueta contiene un valor `platform:identity` más un puntero de prueba que permite a un cliente verificar el claim:

```json
{
  "id": "5f1c7b7e2c6f3d4a9b0e6a2d8c1f7e3b4a6d9c0e1f2a3b4c5d6e7f8091a2b3c4",
  "pubkey": "3bf0c63fcb8d0d8b6a8fcb3c7f5cb2a972f8a0b5a3d6d8790bb2d4e4f0d6b1c2",
  "created_at": 1741699200,
  "kind": 10011,
  "tags": [
    ["i", "github:alice", "9f5df4e2a8b14c1f9e6d2b7c4a1e8f90"],
    ["i", "twitter:alice_dev", "1898123456789012345"]
  ],
  "content": "",
  "sig": "8f4c62d8a7e9b1c3d5f7091a2b4c6d8e0f1234567890abcdeffedcba09876543211223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

Los clientes reconstruyen la URL de prueba a partir de la plataforma y el valor de prueba, y luego comprueban que la publicación externa contiene el `npub` del usuario. Eso mantiene el claim portable entre clientes sin requerir un verificador central.

## Modelo de prueba

El detalle importante es que NIP-39 demuestra el control de dos identidades al mismo tiempo: la clave de Nostr y la cuenta externa. Si cualquiera de los dos lados de esa prueba desaparece, la verificación se debilita. Un gist o un tuit eliminado no invalida el evento histórico, pero sí elimina la prueba activa de la que dependen la mayoría de los clientes.

Otro punto útil de implementación es la estrategia de fetch. Como los claims ahora viven fuera del kind 0, los clientes pueden decidir si solicitarlos solo en vistas de detalle de perfil, solo para usuarios seguidos o no solicitarlos en absoluto. Eso evita añadir más peso a la ya cargada ruta del kind 0.

## Implementaciones

- [Amethyst PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747) - Publica identidades externas como eventos kind 10011 dedicados
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - Añade una referencia explícita al registro de kind 10011 al conjunto de NIPs

## Estado actual

Según la especificación actual, los claims de identidad viven en eventos kind 10011 dedicados en lugar de metadatos kind 0. Esa separación surgió del esfuerzo más amplio por aligerar las consultas de perfil de kind 0.

---

**Fuentes primarias:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - Movió los claims de identidad fuera del kind 0
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - Añadió la referencia explícita a kind 10011

**Mencionado en:**
- [Newsletter #9: Actualizaciones de NIPs](/es/newsletters/2026-02-11-newsletter/#actualizaciones-de-nips)
- [Newsletter #12: Amethyst](/es/newsletters/2026-03-04-newsletter/#amethyst)
- [Newsletter #13: Actualizaciones de NIPs](/es/newsletters/2026-03-11-newsletter/#actualizaciones-de-nips)

**Ver también:**
- [NIP-05: Verificación basada en DNS](/es/topics/nip-05/)
