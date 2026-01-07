---
title: "NIP-87: Descubrimiento de Mints Ecash"
date: 2026-01-07
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

---

**Fuentes primarias:**
- [Especificación NIP-87](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Mencionado en:**
- [Newsletter #4: Lanzamientos](/es/newsletters/2026-01-07-newsletter/#lanzamientos)

**Ver también:**
- [NIP-60: Billetera Cashu](/es/topics/nip-60/)
