---
title: "NIP-BE: Bluetooth Low Energy"
date: 2025-12-17
translationOf: /en/topics/nip-be.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Connectivity
---

NIP-BE especifica cómo las aplicaciones Nostr pueden comunicarse y sincronizarse a través de Bluetooth Low Energy, habilitando aplicaciones con capacidad offline para sincronizar datos entre dispositivos cercanos sin conectividad a internet.

## Cómo funciona

NIP-BE reutiliza tramas de mensaje Nostr normales sobre BLE en lugar de inventar un modelo de evento separado. Los dispositivos anuncian un servicio BLE más un UUID de dispositivo, comparan UUIDs cuando se encuentran, y determinan de forma determinista cuál lado se convierte en servidor GATT y cuál en cliente GATT.

El servicio GATT usa una forma estilo Nordic UART con una característica de escritura y una característica de lectura/notificación. Eso mantiene el transporte lo suficientemente simple para pilas móviles restringidas mientras sigue transportando mensajes Nostr ordinarios.

## Enmarcado de mensajes

BLE tiene límites de payload pequeños, así que NIP-BE comprime los mensajes con DEFLATE, los divide en fragmentos indexados, y envía solo un mensaje a la vez. La especificación limita los mensajes a 64 KB, lo cual es un recordatorio útil de que este transporte es para sincronización y propagación local, no para transferencia masiva.

## Modelo de sincronización

Después de que se establece una conexión, los pares usan un flujo de sincronización half-duplex basado en mensajes negentropy de [NIP-77](https://github.com/nostr-protocol/nips/blob/master/77.md) como `NEG-OPEN`, `NEG-MSG`, `EVENT` y `EOSE`. Esa decisión de diseño importa porque permite que las implementaciones reutilicen la lógica de sincronización de relay existente en lugar de construir un algoritmo de replicación exclusivo para BLE.

La regla half-duplex también refleja la realidad de los enlaces BLE inestables. Las conexiones intermitentes de corto alcance funcionan mejor cuando cada lado sabe exactamente de quién es el turno de hablar.

## Por qué importa

NIP-BE da a las aplicaciones Nostr un camino hacia redes local-first. Dos teléfonos pueden sincronizar notas o estado de relay directamente cuando están cerca uno del otro, incluso si ninguno tiene internet funcional. Eso hace que BLE sea útil para resistencia a la censura, escenarios de desastre y aplicaciones sociales de baja conectividad.

Las restricciones son igualmente relevantes: el ancho de banda BLE es bajo, las conexiones son de corta duración, y los historiales grandes no encajan bien. En la práctica, NIP-BE es mejor para sincronización incremental y propagación de mensajes cercanos, no para replicación archivística completa.

---

**Fuentes primarias:**
- [Especificación NIP-BE](https://github.com/nostr-protocol/nips/blob/master/BE.md)
- [PR #1979](https://github.com/nostr-protocol/nips/pull/1979)

**Mencionado en:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Ver también:**
- [NIP-01: Basic Protocol](/es/topics/nip-01/)
