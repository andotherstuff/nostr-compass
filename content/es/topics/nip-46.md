---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46 define la firma remota, permitiendo que una aplicación firmante mantenga las claves mientras los clientes solicitan firmas a través de relays Nostr.

## Cómo Funciona

1. El firmante genera una URI de conexión (`bunker://` o `nostrconnect://`)
2. El usuario pega la URI en un cliente
3. El cliente envía solicitudes de firma como eventos encriptados al relay del firmante
4. El firmante solicita aprobación al usuario, devuelve eventos firmados

## Métodos de Conexión

- **bunker://** - Conexión iniciada por el firmante
- **nostrconnect://** - Conexión iniciada por el cliente a través de código QR o deep link

## Operaciones Soportadas

- `sign_event` - Firmar un evento arbitrario
- `get_public_key` - Obtener la clave pública del firmante
- `nip04_encrypt/decrypt` - Operaciones de encriptación NIP-04
- `nip44_encrypt/decrypt` - Operaciones de encriptación NIP-44

---

**Fuentes primarias:**
- [Especificación NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Mencionado en:**
- [Boletín #1: Cambios Notables de Código](/es/newsletters/2025-12-17-newsletter/#amethyst-android)

**Ver también:**
- [NIP-55: Android Signer](/es/topics/nip-55/)
