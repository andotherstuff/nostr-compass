---
title: "NIP-89: Manejadores de Aplicaciones Recomendados"
date: 2026-01-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

NIP-89 define cómo las aplicaciones pueden anunciar sus capacidades y cómo los usuarios pueden recomendar aplicaciones que manejan tipos de eventos específicos.

## Tipos de Eventos

- **kind 31990** - Manejador de aplicación (publicado por desarrolladores de aplicaciones)
- **kind 31989** - Recomendación de aplicación (publicado por usuarios)

## Cómo Funciona

1. **Las aplicaciones** publican eventos de manejador describiendo qué tipos de eventos soportan y cómo abrir contenido
2. **Los usuarios** recomiendan aplicaciones que usan para tipos de eventos específicos
3. **Los clientes** consultan recomendaciones para ofrecer funcionalidad "abrir en..." para tipos de eventos desconocidos

## Manejador de Aplicación

```json
{
  "id": "<event-id>",
  "pubkey": "<app-developer-pubkey>",
  "created_at": 1736200000,
  "kind": 31990,
  "tags": [
    ["d", "<app-identifier>"],
    ["k", "30023"],
    ["web", "https://app.example.com/a/<bech32>", "naddr"],
    ["ios", "appname://open/<bech32>"]
  ],
  "content": "{\"name\": \"My App\", \"picture\": \"...\"}",
  "sig": "<signature>"
}
```

Las etiquetas `k` especifican los tipos de eventos soportados. Las plantillas de URL usan `<bech32>` como marcador de posición para entidades codificadas en NIP-19.

## Recomendación de Usuario

```json
{
  "id": "<event-id>",
  "pubkey": "<user-pubkey>",
  "created_at": 1736200000,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:app-pubkey:identifier", "wss://relay", "web"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

La etiqueta `d` es el tipo de evento que se recomienda. Múltiples etiquetas `a` pueden recomendar diferentes aplicaciones para diferentes plataformas.

## Casos de Uso

- Descubrir aplicaciones que pueden mostrar artículos de formato largo (kind 30023)
- Encontrar clientes que soportan tipos de eventos específicos
- Funcionalidad "abrir en..." entre clientes
- Detectar capacidades de cliente para soporte de cifrado

---

**Fuentes primarias:**
- [Especificación NIP-89](https://github.com/nostr-protocol/nips/blob/master/89.md)

**Mencionado en:**
- [Newsletter #4: Profundización en NIPs](/es/newsletters/2026-01-07-newsletter/#nip-44-cifrado-versionado)

**Ver también:**
- [NIP-19: Entidades Codificadas en Bech32](/es/topics/nip-19/)
