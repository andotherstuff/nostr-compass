---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47 define un protocolo para conectar aplicaciones Nostr a billeteras Lightning, habilitando pagos sin exponer las credenciales de la billetera a cada aplicación.

## Cómo Funciona

Una billetera (como Zeus) ejecuta un servicio NWC que escucha solicitudes de pago en relays Nostr específicos. Las aplicaciones se conectan usando una cadena de conexión que incluye la pubkey de la billetera e información del relay. Las solicitudes de pago y respuestas se encriptan entre la aplicación y la billetera.

## Casos de Uso

- **Zapping** - Enviar sats a publicaciones, perfiles o creadores de contenido
- **Pagos** - Pagar facturas Lightning desde cualquier aplicación Nostr
- **Suscripciones** - Pagos recurrentes para contenido premium

## Características Clave

- **Controles de presupuesto** - Establecer límites de gasto por conexión
- **Relays personalizados** - Usar tu propio relay para comunicación de billetera
- **Pagos paralelos** - Procesar múltiples zaps simultáneamente para operaciones por lotes

---

**Fuentes primarias:**
- [Especificación NIP-47](https://github.com/nostr-protocol/nips/blob/master/47.md)

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)
- [Boletín #2: Lanzamientos](/es/newsletters/2025-12-24-newsletter/#releases)

**Ver también:**
- [NIP-57: Zaps](/es/topics/nip-57/)
