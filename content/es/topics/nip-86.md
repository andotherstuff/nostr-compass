---
title: "NIP-86: API de Gestión de Relays"
date: 2026-04-01
translationOf: /en/topics/nip-86.md
translationDate: 2026-04-01
draft: false
categories:
  - Relays
  - Protocol
---

NIP-86 define una interfaz JSON-RPC para gestión de relays, permitiendo a clientes autorizados enviar comandos administrativos a relays a través de una API estandarizada. Los operadores de relays pueden banear o permitir pubkeys, gestionar listas de acceso, y consultar el estado del relay sin herramientas específicas del relay.

## Cómo Funciona

La API de gestión usa solicitudes tipo JSON-RPC sobre HTTP en la misma URI que el endpoint websocket del relay. Las solicitudes usan el tipo de contenido `application/nostr+json+rpc` y se autentican con un evento firmado [NIP-98](/es/topics/nip-98/) (HTTP Auth) en el encabezado `Authorization`. El relay verifica la pubkey solicitante contra su lista de administradores antes de ejecutar comandos.

Los métodos disponibles incluyen banear y permitir pubkeys, listar usuarios baneados, y consultar la configuración del relay. La interfaz estandarizada significa que una sola implementación de cliente puede gestionar cualquier relay compatible con NIP-86.

## Implementaciones

- [Amethyst](https://github.com/vitorpamplona/amethyst) - Cliente Android con UI de gestión de relays NIP-86 (v1.07.0+)

---

**Fuentes primarias:**
- [Especificación NIP-86](https://github.com/nostr-protocol/nips/blob/master/86.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - Soporte de NIP-86 del lado del cliente
- [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) - Diálogo de búsqueda de usuarios para gestión de relays

**Mencionado en:**
- [Newsletter #16: Amethyst lanza gestión de relays](/es/newsletters/2026-04-01-newsletter/#amethyst-lanza-notas-fijadas-gestión-de-relays-y-request-to-vanish)

**Ver también:**
- [NIP-11: Documento de Información del Relay](/es/topics/nip-11/)
- [NIP-98: HTTP Auth](/es/topics/nip-98/)
- [NIP-42: Autenticación de Clientes ante Relays](/es/topics/nip-42/)
