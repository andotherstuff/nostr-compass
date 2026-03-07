---
title: "NIP-32: Etiquetado"
date: 2026-01-21
translationOf: /en/topics/nip-32.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-32 define un estándar para adjuntar etiquetas a eventos, usuarios y otras entidades de Nostr. Las etiquetas proporcionan metadatos estructurados que los clientes pueden usar para categorización, advertencias de contenido, sistemas de reputación y moderación.

## Cómo Funciona

Las etiquetas usan eventos kind 1985 con un tag `L` que define el namespace de la etiqueta y tags `l` que aplican etiquetas específicas dentro de ese namespace. La entidad etiquetada se referencia mediante tags estándar como `e` (eventos), `p` (pubkeys) o `r` (URLs de relay).

```json
{
  "kind": 1985,
  "tags": [
    ["L", "content-warning"],
    ["l", "nsfw", "content-warning"],
    ["e", "<event_id>"]
  ],
  "content": "Contiene imágenes explícitas"
}
```

El sistema de namespaces previene colisiones de etiquetas. Una etiqueta "spam" en el namespace "ugc-moderation" tiene semántica diferente que "spam" en el namespace "relay-report". Esto permite que múltiples sistemas de etiquetado coexistan sin interferencia.

## Por Qué Importa

La decisión de diseño clave es que las etiquetas son afirmaciones, no hechos integrados en el protocolo. Un evento kind 1985 dice que algún actor etiquetó algo en algún namespace. Los clientes aún necesitan una política de confianza para decidir qué etiquetas mostrar, ocultar o ignorar.

Eso hace que NIP-32 sea útil mucho más allá de la moderación. La misma estructura puede transportar advertencias de contenido, marcadores de verificación, sistemas de clasificación o datos de reputación de relays sin forzar a todos los clientes a un vocabulario global único.

## Casos de Uso

Los sistemas de moderación de contenido usan etiquetas para marcar spam, contenido ilegal o violaciones de políticas. Los sistemas de reputación adjuntan puntuaciones de confianza o estado de verificación a pubkeys. Las plataformas de medios aplican advertencias de contenido como NSFW, violencia o spoilers. Los operadores de relays usan etiquetas para apelaciones y resolución de disputas.

La propuesta Trusted Relay Assertions usa etiquetas NIP-32 para apelaciones de relays. Cuando los operadores disputan puntuaciones de confianza, publican eventos kind 1985 con `L = relay-appeal` y etiquetas como `spam`, `censorship` o `score`.

## Notas de Interoperabilidad

Los clientes difieren en cómo consumen etiquetas. Algunos tratan etiquetas de usuarios seguidos como recomendaciones, mientras otros consultan servicios de etiquetado especializados. El diseño descentralizado permite a los usuarios elegir en qué etiquetadores confiar, pero también significa que una etiqueta sin contexto de confianza visible puede ser engañosa.

---

**Fuentes primarias:**
- [Especificación NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) - Estándar de etiquetado

**Mencionado en:**
- [Newsletter #6: Actualizaciones de NIPs](/en/newsletters/2026-01-21-newsletter/#nip-updates)

**Ver también:**
- [Trusted Relay Assertions](/es/topics/trusted-relay-assertions/)
- [NIP-51: Listas](/es/topics/nip-51/)
