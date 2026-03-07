---
title: "NIP-87: Descubrimiento de Mints Ecash"
date: 2026-01-07
translationOf: /en/topics/nip-87.md
translationDate: 2026-03-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---

NIP-87 define cómo los mints de ecash (Cashu y Fedimint) pueden anunciarse en Nostr, y cómo los usuarios pueden recomendar mints a otros.

## Tipos de Eventos

- **kind 38172** - Anuncio de mint Cashu (publicado por operadores de mint)
- **kind 38173** - Anuncio de Fedimint (publicado por operadores de mint)
- **kind 38000** - Recomendación de mint (publicado por usuarios)

## Cómo Funciona

1. **Los operadores de mint** publican la URL de su mint, características soportadas y red (mainnet/testnet)
2. **Los usuarios** que confían en un mint publican recomendaciones con reseñas opcionales
3. **Otros usuarios** consultan recomendaciones de personas que siguen para descubrir mints confiables

## Anuncio de Mint Cashu

```json
{
  "id": "<event-id>",
  "pubkey": "<mint-operator-pubkey>",
  "created_at": 1736200000,
  "kind": 38172,
  "tags": [
    ["d", "<mint-pubkey>"],
    ["u", "https://mint.example.com"],
    ["nuts", "1,2,3,4,5,6,7"],
    ["n", "mainnet"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

La etiqueta `nuts` lista los NUTs soportados (especificaciones de Notación, Uso y Terminología para Cashu).

La etiqueta `d` debe ser la pubkey Cashu del mint, lo que da a los clientes un identificador estable para el descubrimiento incluso si el mint luego cambia metadatos o republica su anuncio.

## Recomendaciones de Usuarios

```json
{
  "id": "<event-id>",
  "pubkey": "<recommender-pubkey>",
  "created_at": 1736200000,
  "kind": 38000,
  "tags": [
    ["k", "38172"],
    ["d", "<mint-identifier>"],
    ["a", "38172:mint-pubkey:<d-tag>", "wss://relay"]
  ],
  "content": "He usado este mint por meses, muy confiable",
  "sig": "<signature>"
}
```

Los usuarios pueden incluir reseñas en el campo `content` y apuntar a eventos de anuncio de mint específicos.

Los eventos de recomendación son eventos reemplazables parametrizados. Eso es útil porque un usuario puede revisar una recomendación, actualizar el texto de su reseña o dejar de respaldar un mint sin dejar varios eventos de recomendación obsoletos detrás.

## Modelo de Confianza

NIP-87 no le dice a los clientes qué mint es seguro. Les da una forma de combinar metadatos publicados por el operador con recomendaciones sociales de cuentas en las que el usuario ya confía.

Esa distinción importa porque las consultas directas de eventos de anuncio de mint pueden ser ruidosas o maliciosas. La especificación advierte explícitamente a los clientes que usen medidas de prevención de spam o relays de alta calidad al omitir las recomendaciones sociales y consultar anuncios directamente.

## Notas de Interoperabilidad

Cashu y Fedimint usan kinds de anuncio diferentes porque exponen detalles de conexión distintos. Los anuncios de Cashu publican URLs de mint y NUTs soportados, mientras que los anuncios de Fedimint publican códigos de invitación y módulos de federación soportados. Una billetera que soporte ambos necesita parsear ambos formatos.

---

**Fuentes primarias:**
- [Especificación NIP-87](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Mencionado en:**
- [Newsletter #4: Lanzamientos](/en/newsletters/2026-01-07-newsletter/#releases)
- [Newsletter #7: Zeus](/en/newsletters/2026-01-28-newsletter/)

**Ver también:**
- [Cashu](/es/topics/cashu/)
- [NIP-60: Billetera Cashu](/es/topics/nip-60/)
