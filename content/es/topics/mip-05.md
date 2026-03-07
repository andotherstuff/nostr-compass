---
title: "MIP-05: Notificaciones Push que Preservan la Privacidad"
date: 2025-12-17
translationOf: /en/topics/mip-05.md
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---

MIP-05 define un protocolo de notificaciones push para clientes Marmot que intenta preservar la privacidad en un contexto donde los sistemas push móviles ordinarios suelen exponer tokens de dispositivo y relaciones de cuentas.

## Cómo Funciona

- Los tokens de dispositivo se cifran con ECDH+HKDF y ChaCha20-Poly1305
- Las claves efímeras previenen la correlación entre notificaciones
- Un protocolo gossip de tres eventos (kinds 447-449) sincroniza tokens cifrados entre miembros del grupo
- Los tokens señuelo vía gift wrapping de NIP-59 ocultan los tamaños de grupo

## Modelo de Privacidad

- Los servidores de notificaciones push no pueden identificar usuarios
- La membresía del grupo no se revela por patrones de notificación
- Los tokens de dispositivo no pueden correlacionarse entre mensajes

La mejora concreta es que el proveedor push ve tokens de entrega opacos, no un mapa directo de miembro de grupo a dispositivo. Eso no hace las notificaciones anónimas en sentido absoluto, pero reduce cuánto aprende la capa push por defecto.

## Tipos de Evento

- **Kind 447**: Publicación de token de dispositivo cifrado
- **Kind 448**: Solicitud de sincronización de token
- **Kind 449**: Respuesta de sincronización de token

## Compensaciones

MIP-05 añade privacidad al añadir trabajo de coordinación. Los clientes deben sincronizar el estado de tokens cifrados entre los miembros del grupo, y los tokens señuelo aumentan la sobrecarga de mensajes a propósito.

Eso significa que los implementadores necesitan equilibrar la fiabilidad de entrega contra la protección de metadatos. El protocolo es útil precisamente porque trata el push como un problema de privacidad, no solo como una conveniencia de transporte.

---

**Fuentes primarias:**
- [Especificación MIP-05](https://github.com/marmot-protocol/marmot/blob/master/05.md)
- [PR de MIP-05](https://github.com/marmot-protocol/marmot/pull/18)
- [White Noise v0.2.1 release](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)
- [Boletín #3: Resumen de Diciembre](/es/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Ver también:**
- [Protocolo Marmot](/es/topics/marmot/)
- [NIP-59: Gift Wrap](/es/topics/nip-59/)
