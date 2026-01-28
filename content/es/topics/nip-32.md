---
title: "NIP-32: Etiquetado"
date: 2026-01-21
translationOf: /en/topics/nip-32.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-32 define un estándar para adjuntar etiquetas a eventos, usuarios y otras entidades de Nostr. Las etiquetas proporcionan metadatos estructurados que los clientes pueden usar para categorización, advertencias de contenido, sistemas de reputación y moderación.

## Cómo Funciona

Las etiquetas usan eventos kind 1985 con un tag `L` definiendo el namespace de la etiqueta y tags `l` aplicando etiquetas específicas dentro de ese namespace. La entidad etiquetada se referencia a través de tags estándar como `e` (eventos), `p` (pubkeys), o `r` (URLs de relay).

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

El sistema de namespaces previene colisiones de etiquetas. Una etiqueta "spam" en el namespace "ugc-moderation" tiene semántica diferente que "spam" en el namespace "relay-report". Esto permite que múltiples sistemas de etiquetas coexistan sin interferencia.

## Casos de Uso

Los sistemas de moderación de contenido usan etiquetas para marcar spam, contenido ilegal o violaciones de políticas. Los sistemas de reputación adjuntan puntuaciones de confianza o estado de verificación a pubkeys. Las plataformas de medios aplican advertencias de contenido (NSFW, violencia, spoilers). Los operadores de relays usan etiquetas para apelaciones y resolución de disputas.

La propuesta Trusted Relay Assertions usa etiquetas NIP-32 para apelaciones de relays. Cuando los operadores disputan puntuaciones de confianza, publican eventos kind 1985 con `L` = `relay-appeal` y tipos de etiqueta como "spam", "censorship", o "score".

Las implementaciones de clientes varían en cómo consumen etiquetas. Algunos clientes tratan etiquetas de usuarios seguidos como recomendaciones, mientras otros consultan servicios de etiquetado especializados. El diseño descentralizado permite a los usuarios elegir en qué etiquetadores confiar.

---

**Fuentes primarias:**
- [Especificación NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) - Estándar de etiquetado

**Mencionado en:**
- [Newsletter #6: Actualizaciones de NIPs](/es/newsletters/2026-01-21-newsletter/#nip-updates)

**Ver también:**
- [Trusted Relay Assertions](/es/topics/trusted-relay-assertions/)
- [NIP-51: Listas](/es/topics/nip-51/)
