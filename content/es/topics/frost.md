---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2025-12-31
draft: false
categories:
  - Criptografía
  - Protocolo
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) es un esquema de firmas de umbral que permite a un grupo de participantes producir colaborativamente firmas Schnorr válidas sin que ninguna parte individual posea la clave privada completa.

## Cómo funciona

FROST permite la firma de umbral T-de-N, donde T participantes de un total de N poseedores de claves deben cooperar para producir una firma válida. El protocolo opera en dos rondas:

1. **Ronda de compromiso**: Cada participante genera y comparte compromisos criptográficos
2. **Ronda de firma**: Los participantes combinan sus firmas parciales en una firma agregada final

La firma resultante es indistinguible de una firma Schnorr estándar, manteniendo compatibilidad retroactiva con los sistemas de verificación existentes.

## Propiedades principales

- **Seguridad de umbral**: Ningún participante individual puede firmar solo; T partes deben cooperar
- **Eficiencia de rondas**: Solo se requieren dos rondas de comunicación para firmar
- **Protección contra falsificación**: Técnicas novedosas protegen contra ataques a esquemas de umbral anteriores
- **Agregación de firmas**: Múltiples firmas se combinan en una única firma compacta
- **Privacidad**: Las firmas finales no revelan qué T participantes firmaron

## Casos de uso en Nostr

En el contexto de Nostr, FROST permite:

- **Gobernanza por quórum**: Los grupos pueden compartir un nsec mediante esquemas T-de-N, donde los miembros pueden representarse a sí mismos o delegar en consejos
- **Administración multi-firma**: Moderación comunitaria que requiere múltiples firmas de administradores
- **Gestión descentralizada de claves**: Distribución de la confianza entre múltiples partes para operaciones críticas

## Estandarización

FROST fue estandarizado como RFC 9591 en junio de 2024, titulado "The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol for Two-Round Schnorr Signatures".

---

**Fuentes principales:**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [University of Waterloo CrySP](https://crysp.uwaterloo.ca/software/frost/)
- [Zcash Foundation Rust Implementation](https://github.com/ZcashFoundation/frost)

**Mencionado en:**
- [Newsletter #3: Repositorio de NIPs](/es/newsletters/2025-12-31-newsletter/#nips-repository)

**Ver también:**
- [Propuesta NIP-XX Quorum](https://github.com/nostr-protocol/nips/pull/2179)
