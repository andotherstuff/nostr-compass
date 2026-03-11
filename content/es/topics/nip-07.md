---
title: "NIP-07: Firmante de Extensión de Navegador"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - Signing
  - Security
---

NIP-07 define una interfaz estándar para que las extensiones de navegador proporcionen capacidades de firma a clientes Nostr basados en web, manteniendo las claves privadas seguras en la extensión en lugar de exponerlas a sitios web.

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
- **Aprobación del usuario**: Las extensiones pueden solicitar confirmación para cada petición de firma
- **Control de dominio**: Las extensiones pueden restringir qué sitios pueden solicitar firmas

NIP-07 mejora la custodia de claves, pero no elimina la confianza en la extensión en sí. Una extensión maliciosa o comprometida puede firmar algo incorrecto, filtrar metadatos u otorgar permisos demasiado amplios.

## Notas de Interoperabilidad

La parte más difícil de NIP-07 no es la forma del API. Es la variación de capacidades. Algunas extensiones solo soportan `getPublicKey()` y `signEvent()`. Otras también exponen `nip04`, `nip44` u otros métodos opcionales más nuevos. Las aplicaciones web necesitan detección de funcionalidades y respaldos razonables en lugar de asumir que todos los firmantes inyectados se comportan igual.

La UX de aprobación del usuario también cambia el comportamiento. Un sitio que espera silenciosamente acceso en segundo plano puede funcionar con una extensión y sentirse roto con otra que solicita confirmación en cada petición. Las buenas aplicaciones NIP-07 tratan la firma como un límite de permisos interactivo.

## Estado de Implementación

Extensiones NIP-07 populares incluyen:
- **Alby** - Billetera Lightning con firma Nostr
- **nos2x** - Firmante Nostr ligero
- **Flamingo** - Extensión Nostr con muchas funciones

## Limitaciones

- Solo navegador (sin soporte móvil)
- Requiere instalación de extensión
- Cada extensión tiene diferente UX para aprobaciones

Para firma entre dispositivos o móvil, NIP-46 y NIP-55 generalmente encajan mejor.

---

**Fuentes primarias:**
- [Especificación NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md)
- [PR #2233](https://github.com/nostr-protocol/nips/pull/2233) - propuesta de `peekPublicKey()`

**Mencionado en:**
- [Boletín #7: Actualizaciones de NIP](/es/newsletters/2026-01-28-newsletter/#nip-updates)
- [Boletín #8: Noticias](/es/newsletters/2026-02-04-newsletter/#news)
- [Boletín #11: Noticias](/es/newsletters/2026-02-25-newsletter/#news)

**Ver también:**
- [NIP-04: Mensajes Directos Cifrados (Obsoleto)](/es/topics/nip-04/)
- [NIP-44: Payloads Cifrados](/es/topics/nip-44/)
- [NIP-46: Nostr Connect](/es/topics/nip-46/)
- [NIP-55: Aplicaciones Firmantes Android](/es/topics/nip-55/)
