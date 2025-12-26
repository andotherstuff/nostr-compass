---
title: "NIP-59: Gift Wrap"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-59 define el gift wrapping (envoltorio de regalo), una técnica para ocultar al remitente de un evento envolviéndolo en capas de encriptación con una identidad desechable.

## Estructura

Un evento envuelto en regalo tiene tres capas:

1. **Rumor** - El contenido del evento original sin firmar
2. **Seal** (kind 13) - El rumor encriptado para el destinatario, firmado por el remitente real
3. **Gift Wrap** (kind 1059) - El sello encriptado para el destinatario, firmado por una clave desechable aleatoria

La capa exterior usa un par de claves aleatorio generado solo para este mensaje, por lo que los observadores no pueden vincularlo al remitente.

## ¿Por Qué Tres Capas?

- El **rumor** contiene el contenido real
- El **seal** demuestra el remitente real (solo visible para el destinatario)
- El **gift wrap** oculta al remitente de los relays y observadores

## Soporte de Eliminación

Los eventos gift wrap ahora pueden eliminarse a través de solicitudes de eliminación NIP-09/NIP-62. Esto se agregó para permitir a los usuarios eliminar mensajes envueltos de los relays.

## Casos de Uso

- Mensajes directos privados (NIP-17)
- Consejos anónimos o denuncia de irregularidades
- Cualquier escenario donde la privacidad del remitente sea importante

---

**Fuentes primarias:**
- [Especificación NIP-59](https://github.com/nostr-protocol/nips/blob/master/59.md)

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)
- [Boletín #1: Actualizaciones de NIP](/es/newsletters/2025-12-17-newsletter/#nip-updates)

**Ver también:**
- [NIP-17: Mensajes Directos Privados](/es/topics/nip-17/)
