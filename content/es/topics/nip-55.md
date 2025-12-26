---
title: "NIP-55: Aplicación Firmante para Android"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55 define cómo las aplicaciones Android pueden solicitar operaciones de firma desde una aplicación firmante dedicada, permitiendo a los usuarios mantener sus claves privadas en un lugar seguro mientras usan múltiples clientes Nostr.

## Cómo Funciona

NIP-55 usa la interfaz de proveedor de contenido de Android para exponer operaciones de firma. Una aplicación firmante se registra como proveedor de contenido, y otras aplicaciones Nostr pueden solicitar firmas sin acceder nunca directamente a la clave privada.

El flujo:
1. La aplicación cliente llama al proveedor de contenido del firmante
2. El firmante muestra la UI de aprobación al usuario
3. El usuario aprueba o rechaza la solicitud
4. El firmante devuelve la firma (o rechazo) al cliente

## Operaciones Clave

- **get_public_key** - Obtener la clave pública del usuario (llamar una vez durante la conexión inicial)
- **sign_event** - Firmar un evento Nostr
- **nip04_encrypt/decrypt** - Encriptar o desencriptar mensajes NIP-04
- **nip44_encrypt/decrypt** - Encriptar o desencriptar mensajes NIP-44

## Iniciación de Conexión

Un error común de implementación es llamar a `get_public_key` repetidamente desde procesos en segundo plano. La especificación recomienda llamarlo solo una vez durante la configuración inicial de conexión, luego cachear el resultado.

---

**Fuentes primarias:**
- [Especificación NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Mencionado en:**
- [Boletín #1: Lanzamientos](/es/newsletters/2025-12-17-newsletter/#releases)
- [Boletín #2: Noticias](/es/newsletters/2025-12-24-newsletter/#news)
- [Boletín #2: Actualizaciones de NIP](/es/newsletters/2025-12-24-newsletter/#nip-updates)

**Ver también:**
- [NIP-46: Nostr Connect](/es/topics/nip-46/)
