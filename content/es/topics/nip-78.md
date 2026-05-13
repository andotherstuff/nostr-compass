---
title: "NIP-78: Datos específicos de la aplicación"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-78.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Data Storage
---

NIP-78 define un kind de evento estándar para que las aplicaciones almacenen datos arbitrarios en nombre de un usuario usando eventos Nostr, permitiendo la sincronización de estado entre dispositivos sin un servidor centralizado.

## Cómo funciona

El kind de evento central es 30078, un evento reemplazable parametrizado. La etiqueta `d` es una cadena de identificador definida por la aplicación que delimita el espacio de almacenamiento a una aplicación y propósito específicos.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 30078,
  "tags": [
    ["d", "myapp-settings"]
  ],
  "content": "{\"theme\":\"dark\",\"fontSize\":14}",
  "sig": "<128-char hex>"
}
```

Una aplicación publica un evento 30078 con una etiqueta `d` única (por ejemplo `tamagostrich-pet-state` o `amethyst-settings`) y el contenido JSON o texto que necesita persistir. Como 30078 es reemplazable y está delimitado por la etiqueta `d`, actualizar el estado almacenado significa publicar un nuevo evento con la misma etiqueta `d`; el relay conserva solo la versión más reciente.

## Sincronización entre dispositivos

Cualquier cliente que conozca la clave pública de un usuario y la etiqueta `d` de la aplicación puede obtener el estado actual del conjunto de relays del usuario y reconstruirlo en cualquier dispositivo. El usuario es dueño de los datos porque viven en eventos firmados con su par de claves, almacenados en relays de su lista de relays [NIP-65](/es/topics/nip-65/).

## Datos privados vs. públicos

Para datos de aplicación privados, el campo de contenido puede cifrarse usando [NIP-44](/es/topics/nip-44/) antes de publicar, de modo que el relay almacena solo texto cifrado que únicamente el titular de la clave puede descifrar. Los datos de aplicación públicos pueden almacenarse sin cifrar para que otros clientes puedan leerlos y mostrarlos.

## Formato de contenido

NIP-78 deja deliberadamente el formato de contenido abierto; las aplicaciones eligen su propio esquema. La convención común es prefijar las etiquetas `d` con el nombre de la aplicación para evitar colisiones entre apps que usan el mismo relay.

## Implementaciones

- [Tamagostrich](https://github.com/Negr087/tamagostrich) — sincronización de estado de mascota entre dispositivos via eventos `tamagostrich-pet-state` kind:30078
- [Wisp](https://github.com/barrydeen/wisp-android) — copia de seguridad de cartera kind:30078 y sincronización de configuración de seguridad entre dispositivos; suscripciones outbox fusionadas en un único REQ usando filtro de autor NIP-78
- [NosPress](https://github.com/nostrapps/nospress) — estado de orquestación CMS almacenado en eventos NIP-78
- Varias implementaciones de sincronización de configuración de clientes Nostr (Amethyst, otros)

---

**Fuentes primarias:**
- [Especificación NIP-78](https://github.com/nostr-protocol/nips/blob/master/78.md)
- [Tamagostrich](https://github.com/Negr087/tamagostrich) — implementación en producción

**Mencionado en:**
- [Newsletter #22: NIP-78 Deep Dive](/es/newsletters/2026-05-14-newsletter/#nip-deep-dive-nip-78-app-specific-data)
- [Newsletter #22: Tamagostrich](/es/newsletters/2026-05-14-newsletter/#tamagostrich-launches-a-decentralized-nip-78-tamagotchi-with-sats-rewards)

**Ver también:**
- [NIP-51: Listas](/es/topics/nip-51/)
- [NIP-44: Cifrado con versión](/es/topics/nip-44/)
- [NIP-65: Metadatos de lista de relays](/es/topics/nip-65/)
