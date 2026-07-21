---
title: "NIP-4E: Desacoplamiento del cifrado de la identidad"
date: 2026-07-15
draft: false
translationOf: /en/topics/nip-4e.md
translationDate: 2026-07-15
categories:
  - NIP
  - Protocol
  - Encryption
---

NIP-4E es un borrador abierto, propuesto por fiatjaf, para compartir datos privados entre los propios dispositivos de un usuario sin que cada dispositivo tenga la clave de identidad principal de Nostr del usuario. No está fusionado y sigue siendo una propuesta `draft`/`optional`.

## El problema que aborda

Muchos NIPs existentes, incluyendo listas NIP-51 y billeteras Cashu NIP-60, cifran datos del usuario hacia sí mismo usando la clave de identidad para poder leerlos de vuelta en cualquier dispositivo. Eso falla cuando la clave de identidad no es directamente accesible, por ejemplo cuando un firmante remoto está protegido por fragmentos de umbral FROST, MuSig2 o un enclave seguro alojado, ya que cifrar y descifrar requiere entonces un viaje de ida y vuelta a ese firmante cada vez. También hace imposible el cifrado sin conexión cuando la clave de firma reside en un bunker remoto.

## Cómo funciona

NIP-4E separa una "clave de cliente" por dispositivo de una "clave de cifrado" compartida que no es la clave de identidad del usuario:

1. El primer cliente que un usuario configura genera un par de claves de cifrado aleatorio y anuncia su mitad pública en un evento `kind:10044` firmado por la clave de identidad del usuario.
2. Cualquier otro cliente que quiera cifrar o descifrar datos para ese usuario calcula su secreto compartido Diffie-Hellman contra la clave de cifrado anunciada en lugar de la clave de identidad.
3. Cuando un segundo dispositivo instala un nuevo cliente, ese cliente genera su propia "clave de cliente" local y publica un anuncio `kind:4454` (también firmado por la clave de identidad del usuario) pidiendo al primer cliente que comparta la clave de cifrado con él.
4. El cliente original detecta el nuevo anuncio `kind:4454`, cifra la clave de cifrado compartida hacia la clave del nuevo cliente usando [NIP-44](/es/topics/nip-44/), y la publica para que el nuevo cliente pueda descifrarla y usarla en adelante.

El resultado es que el cifrado y descifrado nunca requieren preguntar al firmante de clave de identidad una vez que un cliente tiene la clave de cifrado compartida localmente, y una configuración de firmante remoto (FROST, MuSig2, enclave alojado) puede usarse para identidad mientras el cifrado ordinario se mantiene rápido y funciona sin conexión.

## Por qué importa

NIP-4E se cita como la base para otras propuestas que necesitan una clave simétrica por unidad o por cuenta sin depender de un firmante remoto para cada llamada de cifrado/descifrado, incluyendo una propuesta de unidad cifrada privada ([PR #2412](https://github.com/nostr-protocol/nips/pull/2412)) y una versión más estrecha de la misma idea específica para NIP-17 ([PR #2361](https://github.com/nostr-protocol/nips/pull/2361)). Ambas permanecen abiertas junto con NIP-4E, haciendo de esto un área activa y sin resolver del protocolo en lugar de un bloque de construcción terminado.

---

**Fuentes primarias:**
- [Borrador NIP-4E, PR #1647](https://github.com/nostr-protocol/nips/pull/1647)

**Mencionado en:**
- [Newsletter #31: Abierta: unidad cifrada privada que extiende NIP-4E](/es/newsletters/2026-07-15-newsletter/#open-private-encrypted-drive-extends-nip-4e)

**Ver también:**
- [NIP-44: Encrypted Payloads](/es/topics/nip-44/)
- [NIP-17: Private Direct Messages](/es/topics/nip-17/)
- [NIP-46: Nostr Connect](/es/topics/nip-46/)
- [FROST](/es/topics/frost/)
