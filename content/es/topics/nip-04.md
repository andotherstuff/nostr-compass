---
title: "NIP-04: Mensajes Directos Cifrados (Obsoleto)"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-04 define mensajes directos cifrados usando eventos kind 4 y un secreto compartido derivado de ECDH. Fue el primer esquema de DM de Nostr, pero ahora es tecnología legacy y el nuevo trabajo de mensajería privada se ha trasladado a NIP-17.

## Cómo Funciona

Los mensajes usan eventos kind 4 con este flujo básico:

1. El remitente deriva un secreto compartido con ECDH de secp256k1.
2. El texto plano se cifra con AES-256-CBC.
3. El evento incluye una etiqueta `p` que identifica al destinatario.
4. El texto cifrado se codifica como base64 y se almacena en `content` junto con el IV.

El evento en sí sigue siendo un evento Nostr firmado normal, por lo que los relays pueden ver los metadatos externos aunque no puedan leer el texto plano.

## Límites de Seguridad y Privacidad

NIP-04 tiene deficiencias significativas de privacidad:

- **Fuga de metadatos**: La pubkey del remitente es públicamente visible en cada mensaje
- **Sin privacidad del remitente**: Cualquiera puede ver quién envía mensajes a quién
- **Marcas de tiempo exactas**: El tiempo de los mensajes no está aleatorizado
- **Manejo de claves no estándar**: El esquema usa solo la coordenada X del punto ECDH, lo que dificultó la corrección entre bibliotecas y dejó poco margen para la evolución del protocolo

La especificación advierte explícitamente que "no se acerca ni de lejos al estado del arte en comunicación cifrada".

## Por Qué Fue Reemplazado

NIP-04 cifra el contenido del mensaje, pero no oculta el grafo social. Los operadores de relays aún pueden ver quién envió el evento, quién lo recibe y cuándo fue publicado. Esos metadatos son suficientes para mapear conversaciones incluso sin descifrar el payload.

NIP-17 aborda esto combinando el cifrado de payload de NIP-44 con el gift wrapping de NIP-59, que oculta al remitente de los relays y observadores casuales. Las nuevas implementaciones deben tratar NIP-04 como solo para compatibilidad.

## Estado de Implementación

Los clientes y firmantes legacy aún exponen métodos de cifrado/descifrado de NIP-04 porque las conversaciones antiguas y aplicaciones más viejas siguen en circulación. Esa capa de compatibilidad importa para la migración, pero construir nuevas funcionalidades sobre eventos kind 4 generalmente significa cargar las limitaciones de privacidad antiguas.

---

**Fuentes primarias:**
- [Especificación NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Mencionado en:**
- [Boletín #4: Análisis Profundo de NIP](/es/newsletters/2026-01-07-newsletter/#nip-04-encrypted-direct-messages-legacy)
- [Boletín #3: Resumen de Diciembre](/es/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Ver también:**
- [NIP-44: Payloads Cifrados](/es/topics/nip-44/)
- [NIP-17: Mensajes Directos Privados](/es/topics/nip-17/)
- [NIP-59: Gift Wrap](/es/topics/nip-59/)
