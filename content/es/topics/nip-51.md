---
title: "NIP-51: Listas"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Social
---

NIP-51 define varios tipos de listas para organizar referencias a eventos, usuarios y contenido en Nostr.

## Tipos de Listas

- **Kind 10000**: Lista de silenciados (usuarios, hilos o palabras a ocultar)
- **Kind 10001**: Lista de fijados (eventos para destacar en el perfil)
- **Kind 30000**: Conjuntos de seguidos (listas de seguidos categorizadas)
- **Kind 30003**: Conjuntos de marcadores
- **Kind 30004**: Conjuntos de curación (artículos)
- **Kind 30005**: Conjuntos de videos
- **Kind 30006**: Conjuntos de imágenes
- **Kind 30015**: Conjuntos de intereses (hashtags)
- **Kind 30030**: Conjuntos de emojis

## Estructura

Las listas usan etiquetas para referenciar contenido:
- Etiquetas `p` para pubkeys
- Etiquetas `e` para eventos
- Etiquetas `a` para eventos direccionables
- Etiquetas `t` para hashtags
- Etiquetas `word` para palabras silenciadas

## Público vs Privado

Las listas pueden tener etiquetas públicas (visibles para todos) y contenido encriptado (privado). Los elementos privados se encriptan usando NIP-44 y se almacenan en el campo `content` del evento. La encriptación usa las propias claves del autor (encriptando hacia ti mismo).

Esto permite características como marcadores públicos con notas privadas, o una lista de silenciados donde los elementos silenciados están ocultos de otros.

## Cambios Recientes

- Las etiquetas de hashtag y URL se eliminaron de los marcadores genéricos; los hashtags ahora usan kind 30015
- Se agregó kind 30006 para conjuntos de imágenes curadas

---

**Fuentes primarias:**
- [Especificación NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md)

**Mencionado en:**
- [Boletín #1: Actualizaciones de NIP](/es/newsletters/2025-12-17-newsletter/#nip-updates)
- [Boletín #2: Actualizaciones de NIP](/es/newsletters/2025-12-24-newsletter/#nip-updates)

**Ver también:**
- [NIP-02: Lista de Seguidos](/es/topics/nip-02/)
