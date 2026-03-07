---
title: "NIP-29: Grupos Basados en Relay"
date: 2025-12-24
translationOf: /en/topics/nip-29.md
translationDate: 2026-03-07
draft: false
categories:
  - Social
  - Groups
---

NIP-29 define grupos basados en relay, donde un relay gestiona la membresía del grupo, los permisos y la visibilidad de mensajes.

## Cómo Funciona

Los grupos se identifican por un host de relay más un ID de grupo, y el relay es la autoridad para membresía y moderación. Los eventos creados por usuarios y enviados a un grupo llevan un tag `h` con el ID del grupo. Los metadatos generados por el relay usan eventos direccionables firmados por la propia clave del relay.

El evento principal de metadatos es kind 39000, mientras que los kinds 39001 a 39003 describen administradores, miembros y roles soportados. Las acciones de moderación ocurren a través de eventos de la serie 9000 como `put-user`, `remove-user`, `edit-metadata` y `create-invite`.

## Modelo de Acceso

- **private**: Solo los miembros pueden leer los mensajes del grupo
- **closed**: Las solicitudes de unión se ignoran a menos que el relay use manejo de códigos de invitación
- **hidden**: El relay oculta los metadatos del grupo de los no miembros, haciendo el grupo no descubrible
- **restricted**: Solo los miembros pueden escribir mensajes al grupo

Estos tags son independientes. Un grupo puede ser legible por todos pero escribible solo por miembros, o completamente oculto para no miembros. Esa separación importa porque los clientes no deberían tratar "private" como un atajo general para toda regla de acceso.

## Modelo de Confianza

NIP-29 no es un protocolo de grupo sin confianza. El relay anfitrión decide qué eventos de moderación son válidos, qué roles existen, si las listas de miembros son visibles y si los mensajes antiguos o fuera de contexto se aceptan. Un cliente puede verificar firmas y referencias de línea temporal, pero aún depende de la política del relay para el estado real del grupo.

Eso hace que la migración y bifurcación sean posibles, pero no automáticas. El mismo ID de grupo puede existir en diferentes relays con diferentes historiales o reglas, así que la URL del relay es parte de la identidad del grupo en la práctica.

## Notas Útiles de Implementación

- Los clientes deben tratar la URL del relay como la clave del host del grupo. Una clarificación de enero de 2026 hizo esto explícito en la especificación y eliminó la ambigüedad sobre usar una pubkey en su lugar
- El estado del grupo se reconstruye a partir del historial de moderación, mientras que los eventos relay de la serie 39000 son instantáneas informativas de ese estado
- Las referencias `previous` de línea temporal existen para prevenir la re-difusión fuera de contexto entre bifurcaciones de relay, no solo para mejorar el threading de la interfaz

---

**Fuentes primarias:**
- [Especificación NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - Clarificación de `private`, `closed` y `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - Clarificación de URL del relay como clave del relay
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - Adición de `unallowpubkey` y `unbanpubkey`

**Mencionado en:**
- [Newsletter #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #6: NIP Updates](/en/newsletters/2026-01-21-newsletter/#nip-updates)
- [Newsletter #11: NIP Updates](/en/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #12: NIP Updates](/en/newsletters/2026-03-04-newsletter/#nip-updates)

**Ver también:**
- [NIP-11: Relay Information Document](/es/topics/nip-11/)
