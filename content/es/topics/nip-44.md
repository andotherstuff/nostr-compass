---
title: "NIP-44: Payloads Cifrados"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - Criptografía
  - Privacidad
---

NIP-44 define un estándar de cifrado versionado para payloads de Nostr, reemplazando el esquema de cifrado defectuoso de NIP-04 con primitivas criptográficas modernas.

## Cómo funciona

NIP-44 versión 2 utiliza un proceso de cifrado de múltiples pasos:

1. **Acuerdo de Claves**: ECDH (secp256k1) entre las claves públicas del remitente y destinatario produce un secreto compartido
2. **Derivación de Claves**: HKDF-extract con SHA256 y salt `nip44-v2` crea una clave de conversación
3. **Claves Por Mensaje**: HKDF-expand deriva la clave ChaCha, nonce y clave HMAC de un nonce aleatorio
4. **Relleno**: El contenido se rellena para ocultar la longitud del mensaje
5. **Cifrado**: ChaCha20 cifra el contenido rellenado
6. **Autenticación**: HMAC-SHA256 proporciona integridad del mensaje

La salida es un payload base64 versionado que va dentro de un evento Nostr firmado normal. La especificación requiere que los clientes validen la firma del evento NIP-01 externo antes de descifrar el payload NIP-44 interno.

## Elecciones criptográficas

- **ChaCha20** sobre AES: Más rápido, mejor resistencia a ataques multi-clave
- **HMAC-SHA256** sobre Poly1305: Los MACs polinomiales son más fáciles de falsificar
- **SHA256**: Consistente con las primitivas existentes de Nostr
- **Formato Versionado**: Permite futuras actualizaciones de algoritmos

## Propiedades de seguridad

- **Cifrado Autenticado**: Los mensajes no pueden ser manipulados
- **Ocultación de Longitud**: El relleno oscurece el tamaño del mensaje
- **Claves de Conversación**: La misma clave para conversaciones continuas reduce la computación
- **Auditado**: La auditoría de seguridad de Cure53 no encontró vulnerabilidades explotables

## Notas de Implementación

NIP-44 no es un reemplazo directo para payloads NIP-04. Define un formato de cifrado, no un tipo de evento de mensaje directo. Protocolos como [NIP-17](/es/topics/nip-17/) y [NIP-59](/es/topics/nip-59/) definen cómo se usan los payloads cifrados en flujos de mensajes reales.

La entrada de texto plano es texto UTF-8 con una longitud de 1 a 65535 bytes. Esa es una restricción real para implementadores: si tu aplicación necesita cifrar blobs binarios arbitrarios, necesitas una codificación adicional o un formato de contenedor diferente.

## Limitaciones

NIP-44 no proporciona:
- **Forward Secrecy**: Las claves comprometidas exponen mensajes pasados
- **Post-Compromise Security**: Recuperación después del compromiso de claves
- **Negabilidad**: Los mensajes están demostrablemente firmados por claves específicas
- **Ocultación de Metadatos**: La arquitectura de relays limita la privacidad

Para necesidades de alta seguridad, NIP-104 (double ratchet) o protocolos basados en MLS como Marmot ofrecen garantías más fuertes.

## Historia

NIP-44 revisión 3 se fusionó en diciembre de 2023 tras una auditoría de seguridad independiente de Cure53. Forma la base criptográfica para los DMs privados de NIP-17 y el gift wrapping de NIP-59.

---

**Fuentes primarias:**
- [Especificación NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [Implementaciones de Referencia NIP-44](https://github.com/paulmillr/nip44)
- [Informe de Auditoría Cure53](https://cure53.de/audit-report_nip44-implementations.pdf)

**Mencionado en:**
- [Newsletter #4: Análisis Profundo de NIP](/es/newsletters/2026-01-07-newsletter/)
- [Newsletter #3: Diciembre 2023](/es/newsletters/2025-12-31-newsletter/)
- [Newsletter #3: Diciembre 2024](/es/newsletters/2025-12-31-newsletter/)
- [Newsletter #12: Marmot](/es/newsletters/2026-03-04-newsletter/)
- [Newsletter #13: Vector](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: migración a NIP-44 en nostter](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: nowhere cifra tráfico Nostr](/en/newsletters/2026-04-22-newsletter/)

**Ver también:**
- [NIP-04: Mensajes Directos Cifrados (obsoleto)](/es/topics/nip-04/)
- [NIP-17: Mensajes Directos Privados](/es/topics/nip-17/)
- [NIP-59: Gift Wrap](/es/topics/nip-59/)
- [NIP-104: Cifrado Double Ratchet](/es/topics/nip-104/)
- [MLS: Message Layer Security](/es/topics/mls/)
