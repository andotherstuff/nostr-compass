---
title: "NIP-19: Entidades Codificadas en Bech32"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
---

NIP-19 define formatos amigables para humanos para compartir identificadores de Nostr. Estas cadenas codificadas en bech32 se usan para mostrar y compartir, pero nunca se usan en el protocolo mismo (que usa hex).

## ¿Por Qué Bech32?

Las claves hex sin procesar son propensas a errores al copiar y visualmente indistinguibles. La codificación bech32 agrega un prefijo legible para humanos y una suma de verificación, haciendo inmediatamente claro qué tipo de datos estás viendo.

## Formatos Básicos

Estos codifican valores de 32 bytes sin procesar:

- **npub** - Clave pública (tu identidad, segura para compartir)
- **nsec** - Clave privada (mantener en secreto, usada para firmar)
- **note** - ID de evento (referencia a un evento específico)

Ejemplo: La pubkey hex `3bf0c63f...` se convierte en `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

## Identificadores Compartibles

Estos usan codificación TLV (Tipo-Longitud-Valor) para incluir metadatos:

- **nprofile** - Perfil con pistas de relay (ayuda a los clientes a encontrar al usuario)
- **nevent** - Evento con pistas de relay, pubkey del autor y kind
- **naddr** - Referencia a evento direccionable (pubkey + kind + etiqueta d + relays)

Estos resuelven el problema de descubrimiento: cuando alguien comparte un ID de nota, ¿cómo saben los clientes qué relay lo tiene? Al agrupar las pistas de relay en el identificador, los enlaces compartidos se vuelven más confiables.

## Notas de Implementación

- Usa bech32 solo para interfaces humanas: mostrar, copiar/pegar, códigos QR, URLs
- Nunca uses formatos bech32 en mensajes de protocolo, eventos o respuestas NIP-05
- Toda la comunicación del protocolo debe usar codificación hex
- Al generar nevent/nprofile/naddr, incluye pistas de relay para mejor descubrimiento

---

**Fuentes primarias:**
- [Especificación NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md)

**Mencionado en:**
- [Boletín #1: Análisis Profundo de NIP](/es/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
- [NIP-21: Esquema URI nostr:](https://github.com/nostr-protocol/nips/blob/master/21.md)
