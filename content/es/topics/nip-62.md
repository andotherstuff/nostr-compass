---
title: "NIP-62: Solicitudes de Desvanecimiento"
date: 2026-01-13
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62 define las solicitudes de desvanecimiento, un mecanismo para que los usuarios soliciten que los relays eliminen su contenido. Aunque los relays no están obligados a honrar estas solicitudes, soportar NIP-62 da a los usuarios más control sobre sus datos publicados y proporciona una forma estandarizada de señalar la intención de eliminación a través de la red.

## Cómo Funciona

Una solicitud de desvanecimiento es un evento kind 62 firmado por el usuario que quiere que su contenido sea eliminado. La solicitud puede dirigirse a eventos específicos incluyendo sus IDs en etiquetas `e`, o puede solicitar la eliminación de todo el contenido de esa pubkey omitiendo las etiquetas `e` por completo.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 62,
  "tags": [
    ["e", "event1234...", "wss://relay.example.com"],
    ["e", "event5678...", "wss://relay.example.com"]
  ],
  "content": "Eliminando publicaciones antiguas",
  "sig": "sig1234..."
}
```

El campo `content` opcionalmente contiene una razón legible por humanos para la solicitud de eliminación. Las pistas de relay en las etiquetas `e` indican a los relays dónde se publicaron los eventos originales, aunque los relays pueden honrar las solicitudes independientemente de si tienen los eventos especificados.

## Comportamiento del Relay

Los relays que soportan NIP-62 deben eliminar los eventos especificados de su almacenamiento y dejar de servirlos a los suscriptores. La solicitud de desvanecimiento en sí puede ser retenida como un registro de que se solicitó la eliminación, lo que ayuda a prevenir que los eventos eliminados sean reimportados desde otros relays.

Cuando una solicitud de desvanecimiento omite todas las etiquetas `e`, los relays interpretan esto como una solicitud para eliminar todos los eventos de esa pubkey. Esta es una acción más drástica y los relays pueden manejarla de manera diferente, por ejemplo marcando la pubkey como "desvanecida" y rechazando aceptar o servir cualquiera de sus eventos en adelante.

Los relays no están obligados a soportar NIP-62. La red Nostr es descentralizada, y cada operador de relay decide sus propias políticas de retención de datos. Los usuarios no deben asumir que su contenido será eliminado en todas partes simplemente porque publicaron una solicitud de desvanecimiento.

## Consideraciones de Privacidad

Las solicitudes de desvanecimiento son un mecanismo de eliminación de mejor esfuerzo, no una garantía de privacidad. Incluso después de publicar una solicitud de desvanecimiento, copias del contenido pueden existir en otros lugares de la red incluyendo en otros relays que no soportan NIP-62, en cachés locales en dispositivos cliente, en archivos de terceros o motores de búsqueda, y en copias de seguridad.

La solicitud en sí también es un evento firmado de Nostr, lo que significa que se convierte en parte de tu registro público. Cualquiera que vea la solicitud de desvanecimiento sabe que eliminaste algo, incluso si no pueden ver qué fue eliminado.

Para contenido que debe permanecer privado, considera usar mensajería cifrada como [NIP-17](/es/topics/nip-17/) en lugar de depender de la eliminación después del hecho.

---

**Fuentes primarias:**
- [Especificación NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md)

**Mencionado en:**
- [Newsletter #5: Cambios Notables de Código](/es/newsletters/2026-01-13-newsletter/#rust-nostr-biblioteca)
