---
title: "NIP-29: Grupos Basados en Relay"
date: 2025-12-24
translationOf: /en/topics/nip-29.md
translationDate: 2026-04-22
draft: false
categories:
  - Social
  - Groups
---

NIP-29 define grupos basados en relay, donde un relay gestiona la membresía del grupo, los permisos y la visibilidad de mensajes.

## Cómo funciona

Los grupos se identifican por un host de relay más un ID de grupo, y el relay es la autoridad para membresía y moderación. Los eventos creados por usuarios y enviados a un grupo llevan un tag `h` con el ID del grupo. Los metadatos generados por el relay usan eventos direccionables firmados por la propia clave del relay.

El evento principal de metadatos es kind 39000, mientras que los kinds 39001 a 39003 describen administradores, miembros y roles soportados. Las acciones de moderación ocurren a través de eventos de la serie 9000 como `put-user`, `remove-user`, `edit-metadata` y `create-invite`.

## Modelo de acceso

- **private**: Solo los miembros pueden leer los mensajes del grupo
- **closed**: Las solicitudes de unión se ignoran a menos que el relay use manejo de códigos de invitación
- **hidden**: El relay oculta los metadatos del grupo de los no miembros, haciendo el grupo no descubrible
- **restricted**: Solo los miembros pueden escribir mensajes al grupo

Estos tags son independientes. Un grupo puede ser legible por todos pero escribible solo por miembros, o completamente oculto para no miembros. Esa separación importa porque los clientes no deberían tratar "private" como un atajo general para toda regla de acceso.

## Modelo de confianza

NIP-29 no es un protocolo de grupo sin confianza. El relay anfitrión decide qué eventos de moderación son válidos, qué roles existen, si las listas de miembros son visibles y si los mensajes antiguos o fuera de contexto se aceptan. Un cliente puede verificar firmas y referencias de línea temporal, pero aún depende de la política del relay para el estado real del grupo.

Eso hace que la migración y bifurcación sean posibles, pero no automáticas. El mismo ID de grupo puede existir en diferentes relays con diferentes historiales o reglas, así que la URL del relay es parte de la identidad del grupo en la práctica.

## Notas útiles de implementación

- Los clientes deben tratar la URL del relay como la clave del host del grupo. Una clarificación de enero de 2026 hizo esto explícito en la especificación y eliminó la ambigüedad sobre usar una pubkey en su lugar
- El estado del grupo se reconstruye a partir del historial de moderación, mientras que los eventos relay de la serie 39000 son instantáneas informativas de ese estado
- Las referencias `previous` de línea temporal existen para prevenir la re-difusión fuera de contexto entre bifurcaciones de relay, no solo para mejorar el threading de la interfaz

## Trabajo reciente de la especificación

- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310) y las [release notes de Flotilla 1.7.3/1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4) proponen envolver tipos de contenido no orientados a chat en kind `9` (eventos de calendario, encuestas y otros payloads) para que el contexto de la sala se conserve cuando esos objetos se envían a un grupo.
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319) extiende la especificación con una jerarquía de subgrupos para que un solo grupo pueda alojar múltiples canales paralelos sin crear grupos independientes en el mismo relay; el identificador del subgrupo reutiliza la etiqueta `h` existente y preserva mensajes de una sola etiqueta `h` para clientes antiguos.
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316) define permisos explícitos en el evento de roles kind `39003` para que cada rol se convierta en un conjunto nombrado de operaciones permitidas (invite, add-user, remove-user, edit-metadata, delete-event, add-permission) con una expiración temporal opcional.

## Implementaciones

- [Flotilla](https://gitea.coracle.social/coracle/flotilla) es el cliente principal de NIP-29 de hodlbod; [1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3) y [1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4) lanzaron envoltura kind-9, encuestas, login [NIP-46](/es/topics/nip-46/) mediante el esquema de URL Aegis, soporte nativo de share para invites de spaces, menciones de salas, pegado de imágenes del portapapeles móvil, drafts y vídeo en llamadas.
- [Wisp](https://github.com/barrydeen/wisp) añadió configuración de grupos NIP-29 para flags, invites, roles y prompts de AUTH en [PR #471](https://github.com/barrydeen/wisp/pull/471) y endureció la secuenciación de AUTH antes de eventos de grupo `9021`, `9007` y `9009` en [PR #478](https://github.com/barrydeen/wisp/pull/478).

---

**Fuentes primarias:**
- [Especificación NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - Clarificación de `private`, `closed` y `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - Clarificación de URL del relay como clave del relay
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - Adición de `unallowpubkey` y `unbanpubkey`
- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310) - Envoltura kind-9 para contenido no orientado a chat
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319) - Especificación de subgrupos
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316) - Permisos explícitos de roles en kind 39003
- [Flotilla 1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4)
- [Wisp PR #471](https://github.com/barrydeen/wisp/pull/471) - Configuración de grupos NIP-29

**Mencionado en:**
- [Newsletter #2: NIP Updates](/es/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/es/newsletters/2025-12-31-newsletter/)
- [Newsletter #6: NIP Updates](/es/newsletters/2026-01-21-newsletter/)
- [Newsletter #11: NIP Updates](/es/newsletters/2026-02-25-newsletter/)
- [Newsletter #12: NIP Updates](/es/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: Flotilla 1.7.3/1.7.4](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: configuración NIP-29 en Wisp](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: Actualizaciones de NIP (subgrupos y permisos de roles)](/en/newsletters/2026-04-22-newsletter/)

**Ver también:**
- [NIP-11: Relay Information Document](/es/topics/nip-11/)
