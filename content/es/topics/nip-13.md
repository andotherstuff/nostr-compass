---
title: "NIP-13: Prueba de Trabajo"
date: 2026-01-28
translationOf: /en/topics/nip-13.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Spam Prevention
---

NIP-13 define un sistema de prueba de trabajo para eventos Nostr, que exige esfuerzo computacional para crear eventos como mecanismo de prevención de spam.

## Cómo Funciona

La prueba de trabajo se demuestra encontrando un ID de evento (hash SHA256) con un número determinado de bits cero iniciales:

1. **Dificultad**: Se mide en bits cero iniciales (ej., 20 bits = 2^20 intentos en promedio)
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

## Por Qué Importa

- **Admisión a relays**: Los relays pueden requerir PoW mínimo para aceptar eventos
- **Limitación de tasa**: Mayor dificultad para acciones como registro de cuentas
- **Filtrado de spam**: Los clientes pueden priorizar eventos de alto PoW en feeds
- **Bootstrap de reputación**: Cuentas nuevas pueden demostrar compromiso vía PoW

La propiedad útil es el costo asimétrico. Crear muchos eventos aceptables se vuelve caro para el emisor, mientras que verificar la prueba sigue siendo barato para relays y clientes.

## Compromisos

- Favorece a usuarios con hardware potente
- Preocupaciones por consumo de energía
- No previene todo el spam, solo eleva el costo

PoW también traslada la resistencia al spam de la identidad de la cuenta a la disponibilidad de cómputo. Eso puede ayudar en entornos sin permisos, pero no distingue entre un usuario legítimo nuevo y un spammer con recursos.

---

**Fuentes primarias:**
- [Especificación NIP-13](https://github.com/nostr-protocol/nips/blob/master/13.md)

**Mencionado en:**
- [Newsletter #7: News](/en/newsletters/2026-01-28-newsletter/#news)
- [Newsletter #12: News](/en/newsletters/2026-03-04-newsletter/#news)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
