---
title: "NIP-07: Firmante de Extensión de Navegador"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Signing
  - Security
---

NIP-07 define una interfaz estándar para que extensiones de navegador proporcionen capacidades de firma a clientes Nostr basados en web, manteniendo las claves privadas seguras en la extensión en lugar de exponerlas a sitios web.

## Cómo Funciona

Las extensiones de navegador inyectan un objeto `window.nostr` que las aplicaciones web pueden usar:

```javascript
// Obtener clave pública
const pubkey = await window.nostr.getPublicKey();

// Firmar un evento
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// Cifrar (NIP-04, legacy)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// Descifrar (NIP-04, legacy)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// Métodos NIP-44 (modernos, si están soportados)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## Modelo de Seguridad

- **Aislamiento de claves**: Las claves privadas nunca abandonan la extensión
- **Aprobación del usuario**: Las extensiones pueden solicitar confirmación para cada solicitud de firma
- **Control de dominio**: Las extensiones pueden restringir qué sitios pueden solicitar firmas

## Implementaciones

Extensiones NIP-07 populares incluyen:
- **Alby** - Billetera Lightning con firma Nostr
- **nos2x** - Firmante Nostr ligero
- **Flamingo** - Extensión Nostr con muchas funciones

## Limitaciones

- Solo navegador (sin soporte móvil)
- Requiere instalación de extensión
- Cada extensión tiene diferente UX para aprobaciones

## Alternativas

- [NIP-46](/es/topics/nip-46/) - Firma remota vía relays Nostr
- [NIP-55](/es/topics/nip-55/) - Firmante local Android

## Relacionado

- [NIP-44](/es/topics/nip-44/) - Cifrado moderno (reemplazando NIP-04)
- [NIP-46](/es/topics/nip-46/) - Firma Remota
