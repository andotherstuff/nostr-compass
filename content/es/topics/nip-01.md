---
title: "NIP-01: Protocolo Básico"
date: 2025-12-17
translationOf: /en/topics/nip-01.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
---

NIP-01 define el modelo base de eventos y el protocolo de relays sobre el que se construye el resto de Nostr. Si un cliente, relay o biblioteca habla Nostr, empieza aquí.

## Cómo Funciona

Los eventos son el único tipo de objeto en Nostr. Perfiles, notas, reacciones, listas de relays y muchos payloads específicos de aplicación usan la misma envoltura de siete campos:

- **id**: Hash SHA256 del evento serializado (identificador único)
- **pubkey**: La clave pública del creador (hex de 32 bytes, secp256k1)
- **created_at**: Marca de tiempo Unix
- **kind**: Entero que categoriza el tipo de evento
- **tags**: Array de arrays para metadatos
- **content**: El payload (la interpretación depende del kind)
- **sig**: Firma Schnorr que demuestra autenticidad

El `id` del evento es el hash SHA256 de los datos serializados del evento, no un identificador arbitrario. Esto importa en la práctica: cambiar cualquier campo, incluyendo el orden de etiquetas o la marca de tiempo, produce un evento diferente y requiere una nueva firma.

## Kinds

Los kinds determinan cómo los relays almacenan y manejan los eventos:

- **Eventos regulares** (1, 2, 4-44, 1000-9999): Se almacenan normalmente, se guardan todas las versiones
- **Eventos reemplazables** (0, 3, 10000-19999): Solo se guarda el más reciente por pubkey
- **Eventos efímeros** (20000-29999): No se almacenan, solo se reenvían a los suscriptores
- **Eventos direccionables** (30000-39999): El más reciente por combinación de pubkey + kind + etiqueta `d`

Los kinds principales incluyen: 0 (metadatos de usuario), 1 (nota de texto) y 3 (lista de seguidos).

## Comunicación Cliente-Relay

Los clientes se comunican con los relays a través de conexiones WebSocket usando arrays JSON:

**Cliente a relay:**
- `["EVENT", <event>]` - Publicar un evento
- `["REQ", <sub-id>, <filter>, ...]` - Suscribirse a eventos
- `["CLOSE", <sub-id>]` - Terminar una suscripción

**Relay a cliente:**
- `["EVENT", <sub-id>, <event>]` - Entregar evento coincidente
- `["EOSE", <sub-id>]` - Fin de eventos almacenados (ahora transmitiendo en vivo)
- `["OK", <event-id>, <true|false>, <message>]` - Confirmación de aceptación/rechazo
- `["NOTICE", <message>]` - Mensaje legible para humanos

En la práctica, la mayoría de NIPs de nivel superior no cambian la capa de transporte. Definen nuevos kinds de eventos, etiquetas o reglas de interpretación mientras siguen usando los mismos mensajes `EVENT`, `REQ` y `CLOSE` de NIP-01.

## Filtros

Los filtros especifican qué eventos recuperar, con campos que incluyen `ids`, `authors`, `kinds`, `#e`/`#p`/`#t`, `since`, `until` y `limit`. Las condiciones dentro de un filtro usan lógica AND. Múltiples filtros dentro de un `REQ` usan lógica OR.

## Notas de Interoperabilidad

Dos detalles causan muchos errores de implementación. Primero, los clientes deben tratar las respuestas del relay como eventualmente consistentes, no globalmente ordenadas, porque diferentes relays pueden devolver diferentes subconjuntos del historial. Segundo, los eventos reemplazables y direccionables significan que "el más reciente" es parte del modelo del protocolo, así que los clientes necesitan reglas determinísticas para elegir el evento válido más nuevo cuando varios relays no coinciden.

---

**Fuentes primarias:**
- [Especificación NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Mencionado en:**
- [Boletín #1: Análisis Profundo de NIP](/es/newsletters/2025-12-17-newsletter/#nip-deep-dive-nip-01-and-nip-19)

**Ver también:**
- [NIP-19: Entidades Codificadas en Bech32](/es/topics/nip-19/)
- [Registro de Kinds](/es/kind-registry/)
