---
title: "NIP-13: Prueba de Trabajo"
date: 2026-01-28
translationOf: /en/topics/nip-13.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Spam Prevention
---

NIP-13 define un sistema de prueba de trabajo para eventos Nostr, requiriendo esfuerzo computacional para crear eventos como mecanismo de prevención de spam.

## Cómo Funciona

La prueba de trabajo se demuestra encontrando un ID de evento (hash SHA256) con un número específico de bits cero iniciales:

1. **Dificultad**: Medida en bits cero iniciales (ej., 20 bits = 2^20 intentos en promedio)
2. **Tag Nonce**: Los eventos incluyen un tag `nonce` con el valor del nonce y la dificultad objetivo
3. **Verificación**: Los relays y clientes pueden verificar rápidamente que el trabajo fue realizado

```json
{
  "tags": [["nonce", "12345", "20"]],
  ...
}
```

## Niveles de Dificultad

| Bits | Intentos Promedio | Uso Típico |
|------|-------------------|------------|
| 8 | 256 | Disuasivo mínimo de spam |
| 16 | 65,536 | Filtrado ligero |
| 20 | 1,048,576 | Protección moderada |
| 24 | 16,777,216 | Resistencia fuerte al spam |

## Casos de Uso

- **Admisión a relays**: Los relays pueden requerir PoW mínimo para aceptación de eventos
- **Limitación de tasa**: Mayor dificultad para acciones como registro de cuentas
- **Filtrado de spam**: Los clientes pueden priorizar eventos de alto PoW en feeds
- **Bootstrap de reputación**: Cuentas nuevas pueden demostrar compromiso vía PoW

## Limitaciones

- Favorece a usuarios con hardware potente
- Preocupaciones de consumo de energía
- No previene todo el spam, solo eleva el costo

## Relacionado

- [NIP-01](/es/topics/nip-01/) - Protocolo Básico
