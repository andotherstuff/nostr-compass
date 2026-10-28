---
title: "NIP-06: derivación de claves a partir de mnemónicos"
date: 2026-10-28
translationOf: /en/topics/nip-06.md
translationDate: 2026-10-28
draft: false
categories: ["Identity", "Keys"]
---

NIP-06 describe cómo derivar un par de claves de Nostr a partir de una frase semilla mnemónica. El [texto oficial actual de NIP-06](https://github.com/nostr-protocol/nips/blob/master/06.md) está marcado como borrador y opcional, e incluye esta advertencia:

> __Advertencia__ `unrecommended`: prefiere un único nsec

Esta página trata NIP-06 por compatibilidad histórica. No recomienda adoptar la derivación a partir de semillas.

## Cómo funciona

Según la [especificación actual](https://github.com/nostr-protocol/nips/blob/master/06.md), BIP39 se usa para generar las palabras mnemónicas y para derivar de ellas una semilla binaria. Después, BIP32 deriva las claves siguiendo la ruta `m/44'/1237'/<account>'/0/0`, donde 1237 es la entrada de Nostr en SLIP44. Un cliente básico puede usar la cuenta 0. Si se incrementa el valor de la cuenta, se obtienen otras claves a partir de la misma semilla. Dos implementaciones solo reproducen la misma identidad cuando coinciden en los pasos de derivación y usan las codificaciones correctas para el resultado.

## Vectores de prueba

Un [commit del 12 de octubre de 2023](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b) añadió dos vectores de prueba: uno construido a partir de un mnemónico de 12 palabras y otro a partir de uno de 24 palabras. Cada uno enumera la clave privada y la clave pública esperadas en hexadecimal, junto con las codificaciones nsec y npub correspondientes. Los desarrolladores pueden usar los vectores para contrastar implementaciones. Los vectores no dicen nada sobre la custodia de claves, no certifican la seguridad y no garantizan una interoperabilidad universal.

## Véase también

- [NIP-01](/es/topics/nip-01/)

**Fuentes primarias:**

- [NIP-06 (actual)](https://github.com/nostr-protocol/nips/blob/master/06.md)
- [Commit que añade los vectores de prueba de NIP-06 (12 de octubre de 2023)](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b)

**Mencionado en:**

- [Boletín n.º 46](/es/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)
