---
title: "NIP-89: Manejadores de Aplicaciones Recomendados"
date: 2026-01-07
translationOf: /en/topics/nip-89.md
translationDate: 2026-03-07
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

El mismo evento de manejador puede anunciar varios kinds soportados si comparten el mismo patrón de enrutamiento. Eso mantiene el descubrimiento de aplicaciones compacto y evita publicar un evento de manejador por kind cuando la lógica de destino es idéntica.

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

## Etiqueta Client

NIP-89 también define una etiqueta `client` opcional que las aplicaciones que publican pueden adjuntar a eventos ordinarios. Registra el nombre del cliente más un puntero al evento de manejador, lo que permite a otros clientes mostrar de dónde vino una nota o buscar metadatos más ricos de la aplicación.

Esto tiene implicaciones de privacidad. La especificación dice explícitamente que los clientes deben permitir a los usuarios desactivarlo, porque publicar la identidad del software en cada evento puede revelar patrones de uso que las personas pueden no querer exponer.

## Casos de Uso

- Descubrir aplicaciones que pueden mostrar artículos de formato largo (kind 30023)
- Encontrar clientes que soportan tipos de eventos específicos
- Funcionalidad "abrir en..." entre clientes
- Detectar capacidades de cliente para soporte de cifrado

## Notas de Confianza y Seguridad

NIP-89 mejora la interoperabilidad, pero también crea una superficie de redirección. Si un cliente consulta anuncios de manejadores arbitrarios desde relays no confiables, puede terminar enviando usuarios a aplicaciones maliciosas o engañosas.

Por eso el flujo de recomendación comienza con personas que sigues. Las recomendaciones filtradas socialmente no son perfectas, pero son más seguras que tratar cada manejador publicado como igualmente confiable.

---

**Fuentes primarias:**
- [Especificación NIP-89](https://github.com/nostr-protocol/nips/blob/master/89.md)

**Mencionado en:**
- [Newsletter #4: Análisis Profundo de NIPs](/en/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [Newsletter #12: Damus](/en/newsletters/2026-03-04-newsletter/#damus-nip-89-recommended-application-handlers)

**Ver también:**
- [NIP-19: Entidades Codificadas en Bech32](/es/topics/nip-19/)
