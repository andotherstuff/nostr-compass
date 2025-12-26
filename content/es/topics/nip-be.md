---
title: "NIP-BE: Bluetooth Low Energy"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Connectivity
---

NIP-BE especifica cómo las aplicaciones Nostr pueden comunicarse y sincronizarse a través de Bluetooth Low Energy, habilitando aplicaciones con capacidad offline para sincronizar datos entre dispositivos cercanos sin conectividad a internet.

## Estructura GATT

Usa un Nordic UART Service con dos características:
- **Característica de escritura** - El cliente envía datos al servidor
- **Característica de lectura** - El servidor envía datos al cliente (vía notificaciones)

## Enmarcado de Mensajes

BLE tiene límites de payload pequeños (20-256 bytes dependiendo de la versión), por lo que los mensajes son:
- Comprimidos con DEFLATE
- Divididos en fragmentos con un índice de 2 bytes y bandera de lote final
- Limitados a 64KB de tamaño máximo

## Negociación de Roles

Los dispositivos comparan UUIDs anunciados al descubrirse:
- El UUID mayor se convierte en servidor GATT (rol de relay)
- El UUID menor se convierte en cliente GATT
- Existen UUIDs predeterminados para dispositivos de un solo rol

## Sincronización

Usa comunicación half-duplex con tipos de mensajes Nostr estándar (`EVENT`, `EOSE`, `NEG-MSG`) para coordinar la sincronización de datos a través de conexiones intermitentes.

## Casos de Uso

- Sincronización offline de eventos entre dispositivos cercanos
- Propagación de mensajes estilo mesh sin internet
- Conectividad de respaldo cuando la red no está disponible

---

**Fuentes primarias:**
- [Especificación NIP-BE](https://github.com/nostr-protocol/nips/blob/master/BE.md)

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)
