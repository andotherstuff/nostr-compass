---
title: "MIP-05: Notificaciones Push que Preservan la Privacidad"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---

MIP-05 define un protocolo para notificaciones push que mantienen la privacidad del usuario, resolviendo el problema de que los sistemas push tradicionales requieren que los servidores conozcan los tokens de dispositivo y las identidades de los usuarios.

## Cómo Funciona

- Los tokens de dispositivo se encriptan con ECDH+HKDF y ChaCha20-Poly1305
- Las claves efímeras previenen la correlación entre notificaciones
- Un protocolo gossip de tres eventos (kinds 447-449) sincroniza tokens encriptados entre miembros del grupo
- Los tokens señuelo vía gift wrapping de NIP-59 ocultan los tamaños de grupo

## Garantías de Privacidad

- Los servidores de notificaciones push no pueden identificar usuarios
- La membresía del grupo no se revela por patrones de notificación
- Los tokens de dispositivo no pueden correlacionarse entre mensajes

## Tipos de Evento

- **Kind 447**: Publicación de token de dispositivo encriptado
- **Kind 448**: Solicitud de sincronización de token
- **Kind 449**: Respuesta de sincronización de token

---

**Fuentes primarias:**
- [PR de MIP-05](https://github.com/marmot-protocol/marmot/pull/18)

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)

**Ver también:**
- [Protocolo Marmot](/es/topics/marmot/)
- [NIP-59: Gift Wrap](/es/topics/nip-59/)
