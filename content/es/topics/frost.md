---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2026-03-07
draft: false
categories:
  - Cryptography
  - Protocol
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) es un esquema de firmas de umbral que permite a un grupo producir una firma Schnorr válida sin que ningún participante posea la clave privada completa.

## Cómo Funciona

FROST habilita la firma T-de-N. Cualquier conjunto umbral de participantes puede cooperar para producir una firma para la clave pública del grupo.

El protocolo de firma usa dos rondas:

1. **Ronda de compromiso**: Cada participante genera y comparte compromisos criptográficos
2. **Ronda de firma**: Los participantes combinan sus firmas parciales en una firma agregada final

La salida final se verifica como una firma Schnorr ordinaria. Los verificadores ven una firma bajo una clave pública, no una lista de co-firmantes.

## Notas de Seguridad

El manejo de nonces es crítico. El RFC es explícito en que los nonces de firma son de un solo uso. Reutilizarlos puede filtrar material de claves.

El RFC tampoco estandariza la generación distribuida de claves. Especifica el protocolo de firma en sí e incluye la generación de claves con dealer de confianza solo como apéndice. En la práctica, la seguridad de un despliegue FROST depende tanto del flujo de firma como de cómo se crearon y almacenaron los shares.

## Casos de Uso en Nostr

En el contexto de Nostr, FROST puede soportar:

- **Gobernanza por quórum**: Los grupos pueden compartir un nsec mediante esquemas T-de-N, donde los miembros pueden representarse a sí mismos o delegar en consejos
- **Administración multi-firma**: Moderación comunitaria que requiere múltiples firmas de administradores
- **Gestión descentralizada de claves**: Distribución de la confianza entre múltiples partes para operaciones críticas

## Estado

FROST está especificado en [RFC 9591](https://datatracker.ietf.org/doc/rfc9591/), publicado en el stream IRTF en junio de 2024. Eso le da al protocolo una especificación pública estable, pero no es un RFC de estándares IETF.

---

**Fuentes primarias:**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [Implementación Rust de Zcash Foundation](https://github.com/ZcashFoundation/frost)

**Mencionado en:**
- [Boletín #3: Repositorio de NIPs](/es/newsletters/2025-12-31-newsletter/#nips-repository)
- [Boletín #8](/es/newsletters/2026-02-04-newsletter/)
- [Boletín #10](/es/newsletters/2026-02-18-newsletter/)

**Ver también:**
- [NIP-46: Nostr Connect](/es/topics/nip-46/)
- [NIP-55: Android Signer Application](/es/topics/nip-55/)
