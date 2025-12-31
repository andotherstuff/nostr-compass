---
title: "NIP-04: Mensajes Directos Cifrados (Obsoleto)"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2025-12-31
draft: false
categories:
  - Privacidad
  - Mensajería
---

NIP-04 define mensajes directos cifrados usando cifrado AES-256-CBC. Fue el método original para mensajería privada en Nostr, pero ha sido obsoletado en favor de NIP-17 debido a limitaciones significativas de privacidad.

## Cómo funciona

Los mensajes usan eventos de kind 4 con el siguiente esquema de cifrado:
1. Se genera un secreto compartido usando ECDH con la clave pública del destinatario y la clave privada del remitente
2. El mensaje se cifra con AES-256-CBC
3. El texto cifrado se codifica en base64 con el vector de inicialización añadido
4. Una etiqueta `p` identifica la clave pública del destinatario

## Limitaciones de seguridad

NIP-04 tiene deficiencias significativas de privacidad:

- **Fuga de metadatos** - La pubkey del remitente es públicamente visible en cada mensaje
- **Sin privacidad del remitente** - Cualquiera puede ver quién está enviando mensajes a quién
- **Marcas de tiempo exactas** - El tiempo de los mensajes no está aleatorizado
- **Implementación no estándar** - Usa solo la coordenada X del punto ECDH en lugar del hash SHA256 estándar

La especificación advierte explícitamente que "no se acerca ni de lejos al estado del arte en comunicación cifrada".

## Estado de obsolescencia

NIP-04 está obsoleto en favor de NIP-17, que usa el envoltorio de regalo (gift wrapping) de NIP-59 para ocultar la identidad del remitente. Las nuevas implementaciones deberían usar NIP-17 para mensajería privada.

---

**Fuentes principales:**
- [Especificación NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Mencionado en:**
- [Newsletter #3: Resumen de Diciembre](/es/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Ver también:**
- [NIP-17: Mensajes Directos Privados](/es/topics/nip-17/)
- [NIP-59: Gift Wrap](/es/topics/nip-59/)
