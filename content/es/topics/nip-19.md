---
title: "NIP-19: Entidades Codificadas en Bech32"
date: 2025-12-17
translationOf: /en/topics/nip-19.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Identity
---

NIP-19 define formatos amigables para compartir identificadores de Nostr. Estas cadenas codificadas en bech32 se usan para visualización y para compartir, pero nunca se usan en el protocolo mismo (que usa hex).

## Cómo Funciona

Las claves hex sin procesar son propensas a errores al copiar y visualmente indistinguibles. La codificación bech32 agrega un prefijo legible y una suma de verificación, dejando claro qué tipo de datos se está viendo y atrapando muchos errores de copia.

Las formas básicas codifican un solo valor de 32 bytes:

- **npub** - Clave pública (tu identidad, segura para compartir)
- **nsec** - Clave privada (mantener en secreto, usada para firmar)
- **note** - ID de evento (referencia a un evento específico)

Ejemplo: La pubkey hex `3bf0c63f...` se convierte en `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

Las formas extendidas usan codificación TLV para poder llevar pistas de localización junto al identificador:

- **nprofile** - Perfil con pistas de relay
- **nevent** - Evento con pistas de relay, pubkey del autor y kind
- **naddr** - Referencia a evento direccionable con pubkey, kind, tag `d` y pistas de relay

## Por Qué Importa

Las pistas de relay no son autoritativas, pero a menudo determinan si un cliente puede obtener un evento compartido en el primer intento. Por eso `nevent`, `nprofile` y `naddr` suelen ser mejores formatos para compartir que los valores simples `note` o `npub` cuando el contenido está fuera del conjunto de relays actual del destinatario.

Otra distinción práctica es la estabilidad. `note` apunta a un ID de evento inmutable, mientras que `naddr` apunta a un evento direccionable que puede reemplazarse con el tiempo. Para contenido de formato largo, calendarios o anuncios de repositorios, `naddr` suele ser el tipo de enlace correcto.

## Notas de Implementación

- Usa bech32 solo para interfaces humanas: visualización, copiar/pegar, códigos QR, URLs
- Nunca uses formatos bech32 en mensajes de protocolo, eventos o respuestas NIP-05
- Toda la comunicación del protocolo debe usar codificación hex
- Al generar nevent/nprofile/naddr, incluye pistas de relay para mejor descubrimiento
- Trata `nsec` como material secreto en todo momento. Un cliente nunca debería mostrarlo por defecto, registrarlo en logs ni incluirlo en exportaciones de soporte

---

**Fuentes primarias:**
- [Especificación NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md)

**Mencionado en:**
- [Newsletter #1: NIP Deep Dive](/en/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#damus-ios)
- [Newsletter #4: Relay Hint Support](/en/newsletters/2026-01-07-newsletter/)
- [Newsletter #8: Damus iOS](/en/newsletters/2026-02-04-newsletter/#damus-ios)
- [Newsletter #11: notecrumbs](/en/newsletters/2026-02-25-newsletter/)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
- [NIP-10: Reply Threads](/es/topics/nip-10/)
