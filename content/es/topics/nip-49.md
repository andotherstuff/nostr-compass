---
title: "NIP-49: Cifrado de Clave Privada"
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Key Management
  - Security
---

NIP-49 define cómo un cliente puede cifrar la clave privada de un usuario con una contraseña y codificar el resultado como una cadena `ncryptsec`. El objetivo es portabilidad con mejores valores predeterminados que almacenar un `nsec` en bruto, mientras se mantiene la clave cifrada fácil de mover entre clientes.

## Cómo Funciona

El cliente comienza con la clave privada secp256k1 de 32 bytes en bruto, no una cadena hex o bech32. Deriva una clave simétrica temporal de la contraseña del usuario con scrypt, usando un salt aleatorio por clave y un factor de trabajo ajustable almacenado como `LOG_N`. Luego cifra la clave privada con XChaCha20-Poly1305, antepone metadatos de versionado y manejo de clave, y codifica el resultado en bech32 bajo el prefijo `ncryptsec`.

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

El evento anterior es un contenedor de ejemplo, no un requisito de NIP-49. NIP-49 estandariza el formato de clave cifrada en sí, no un kind de evento dedicado para publicarlo. Los clientes pueden almacenar un `ncryptsec` localmente, sincronizarlo a través de almacenamiento específico de la aplicación, o presentarlo como una exportación de respaldo.

## Modelo de Seguridad

NIP-49 hace dos cosas a la vez. Convierte una contraseña de usuario en una clave de cifrado adecuada, y ralentiza los intentos de recuperación por fuerza bruta con un KDF con uso intensivo de memoria. El factor de trabajo importa. Valores más altos de `LOG_N` hacen el descifrado más lento para usuarios legítimos, pero también elevan el costo de adivinación offline para atacantes.

El formato también lleva un flag de un byte que describe si la clave ha sido manejada de forma insegura antes del cifrado. Esto no cambia el texto cifrado en sí, pero da a los clientes una forma de distinguir un respaldo protegido recién generado de una clave que ya fue pegada en texto plano antes de ser envuelta.

## Notas de Implementación

- Las contraseñas se normalizan a Unicode NFKC antes de la derivación de clave para que la misma contraseña pueda ingresarse consistentemente entre clientes.
- XChaCha20-Poly1305 usa un nonce de 24 bytes y cifrado autenticado, así que la manipulación del texto cifrado falla limpiamente durante el descifrado.
- La clave simétrica debería ser borrada con ceros y descartada después del uso.
- La especificación no recomienda publicar claves cifradas en relays públicos, porque recopilar muchas claves cifradas mejora la posición de crackeo offline de un atacante.

## Implementaciones

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Añade compatibilidad de registro usando claves privadas cifradas con NIP-49

---

**Fuentes primarias:**
- [Especificación NIP-49](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Flujo de registro del lado del cliente usando NIP-49

**Mencionado en:**
- [Newsletter #13: Formstr](/en/newsletters/2026-03-11-newsletter/#formstr)
- [Newsletter #13: NIP Deep Dive](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-49-private-key-encryption)

**Ver también:**
- [NIP-46: Nostr Connect](/es/topics/nip-46/)
- [NIP-55: Aplicación Firmante de Android](/es/topics/nip-55/)
