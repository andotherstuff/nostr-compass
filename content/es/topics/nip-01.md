---
title: "NIP-01: Protocolo Básico"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-01 define el protocolo fundamental de Nostr, estableciendo las estructuras de datos y los patrones de comunicación sobre los que se construyen todos los demás NIPs.

## Eventos

Los eventos son el único tipo de objeto en Nostr. Cada pieza de datos, desde una actualización de perfil hasta una publicación de texto o una reacción, se representa como un evento con esta estructura:

- **id**: Hash SHA256 del evento serializado (identificador único)
- **pubkey**: La clave pública del creador (32 bytes en hex, secp256k1)
- **created_at**: Marca de tiempo Unix
- **kind**: Entero que categoriza el tipo de evento
- **tags**: Array de arrays para metadatos
- **content**: El contenido (la interpretación depende del kind)
- **sig**: Firma Schnorr que demuestra autenticidad

## Kinds

Los kinds determinan cómo los relays almacenan y manejan los eventos:

- **Eventos regulares** (1, 2, 4-44, 1000-9999): Se almacenan normalmente, se guardan todas las versiones
- **Eventos reemplazables** (0, 3, 10000-19999): Solo se guarda el más reciente por pubkey
- **Eventos efímeros** (20000-29999): No se almacenan, solo se reenvían a los suscriptores
- **Eventos direccionables** (30000-39999): El más reciente por combinación de pubkey + kind + etiqueta `d`

Los kinds principales incluyen: 0 (metadatos de usuario), 1 (nota de texto), 3 (lista de seguidos).

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

## Filtros

Los filtros especifican qué eventos recuperar, con campos que incluyen: `ids`, `authors`, `kinds`, `#e`/`#p`/`#t` (valores de etiquetas), `since`/`until`, y `limit`. Las condiciones dentro de un filtro usan lógica AND; múltiples filtros en un `REQ` se combinan con lógica OR.

---

**Fuentes primarias:**
- [Especificación NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Mencionado en:**
- [Boletín #1: Análisis Profundo de NIP](/es/newsletters/2025-12-17-newsletter/#nip-deep-dive-nip-01-and-nip-19)

**Ver también:**
- [NIP-19: Entidades Codificadas en Bech32](/es/topics/nip-19/)
- [Registro de Kinds](/es/kind-registry/)
