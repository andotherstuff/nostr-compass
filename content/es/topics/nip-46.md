---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
translationOf: /en/topics/nip-46.md
translationDate: 2026-03-07
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46 define la firma remota sobre relays de Nostr. Un cliente se comunica con un firmante separado, a menudo llamado bunker, para que las claves de firma puedan permanecer fuera de la aplicación que el usuario está usando activamente.

## Cómo Funciona

1. El cliente genera un par de claves local usado solo para la sesión con el bunker.
2. La conexión se establece con una URI `bunker://` o `nostrconnect://`.
3. Cliente y firmante intercambian eventos kind `24133` de solicitud y respuesta cifrados a través de relays.
4. Después de conectarse, el cliente llama a `get_public_key` para conocer la pubkey real del usuario para la cual está firmando.

## Métodos de Conexión

- **bunker://** - Conexión iniciada por el firmante
- **nostrconnect://** - Conexión iniciada por el cliente a través de código QR o deep link

Los flujos `nostrconnect://` incluyen un secreto compartido obligatorio para que el cliente pueda verificar que la primera respuesta realmente provino del firmante previsto. Eso previene suplantación simple de conexión.

## Operaciones Soportadas

- `sign_event` - Firmar un evento arbitrario
- `get_public_key` - Obtener la pubkey del usuario desde el firmante
- `nip04_encrypt/decrypt` - Operaciones de cifrado NIP-04
- `nip44_encrypt/decrypt` - Operaciones de cifrado NIP-44
- `switch_relays` - Pedir al firmante un conjunto de relays actualizado

Muchas implementaciones también usan cadenas de permisos como `sign_event:1` o `nip44_encrypt` durante la configuración para que el firmante pueda aprobar un alcance limitado en lugar de acceso completo.

## Modelo de Relay y Confianza

NIP-46 saca las claves privadas del cliente, pero no elimina la confianza del firmante. El firmante puede aprobar, denegar o retrasar solicitudes, y ve cada operación que el cliente le pide realizar. La elección de relay también importa porque el protocolo depende de la entrega de solicitudes y respuestas a través de relays a los que ambas partes puedan llegar.

El método `switch_relays` existe para que el firmante pueda mover la sesión a un conjunto diferente de relays con el tiempo. Los clientes que lo ignoran funcionarán de forma menos confiable cuando cambien las preferencias de relay del firmante.

---

**Fuentes primarias:**
- [Especificación NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Mencionado en:**
- [Newsletter #1: Cambios Notables de Código](/en/newsletters/2025-12-17-newsletter/#amethyst-android)
- [Newsletter #3: Resumen de Diciembre](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #7: Primal Android se Convierte en Hub de Firma Completo](/en/newsletters/2026-01-07-newsletter/#primal-android-becomes-a-full-signing-hub)
- [Newsletter #15: Eventos Colaborativos de NDK y Timeout de NIP-46](/en/newsletters/2026-03-04-newsletter/#ndk-collaborative-events-and-nip-46-timeout)

**Ver también:**
- [NIP-55: Android Signer](/es/topics/nip-55/)
