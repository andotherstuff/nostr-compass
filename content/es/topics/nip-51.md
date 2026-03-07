---
title: "NIP-51: Listas"
date: 2025-12-17
translationOf: /en/topics/nip-51.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---

NIP-51 define eventos de lista para organizar usuarios, eventos, relays, hashtags y otras referencias. Es el protocolo principal para marcadores, listas de silenciados, conjuntos de seguidos, conjuntos de relays y varias otras colecciones curadas por el usuario.

## Listas estándar y conjuntos

- **Listas estándar** usan kinds de eventos reemplazables como kind `10000` para listas de silenciados, kind `10003` para marcadores y kind `10007` para relays de búsqueda.
- **Conjuntos** usan kinds direccionables con etiquetas `d`, como kind `30000` para conjuntos de seguidos, kind `30003` para conjuntos de marcadores y kind `30030` para conjuntos de emojis.

La distinción importa en el comportamiento de los clientes. Las listas estándar implican una lista canónica por usuario y kind. Los conjuntos implican muchas colecciones con nombre, así que los clientes deben preservar la etiqueta `d` de cada lista.

## Estructura

Las listas usan etiquetas para referenciar contenido:

- Etiquetas `p` para pubkeys
- Etiquetas `e` para eventos
- Etiquetas `a` para eventos direccionables
- Etiquetas `t` para hashtags
- Etiquetas `word` para palabras silenciadas
- Etiquetas `relay` para URLs de relay en kinds de lista orientados a relays

Algunos kinds de lista tienen formas de etiquetas permitidas más restringidas que otros. Por ejemplo, las listas orientadas a relays usan etiquetas `relay`, mientras que los marcadores apuntan a notas o eventos direccionables. Los clientes que traten cada lista NIP-51 como etiquetas arbitrarias de forma libre perderán interoperabilidad.

## Público vs privado

Las listas pueden tener etiquetas públicas y elementos privados. Los elementos privados se serializan como un array JSON que replica la estructura de `tags`, se cifran y se almacenan en el `content` del evento. La especificación actual usa NIP-44 para este modelo de autocifrado, con NIP-04 solo como compatibilidad legacy.

Esa separación permite a los usuarios publicar un esqueleto de lista visible mientras ocultan algunas entradas. Una lista de marcadores puede permanecer pública mientras las notas privadas o los marcadores privados quedan en contenido cifrado.

## Kinds útiles

- **Kind 10000**: lista de silenciados para pubkeys, hilos, hashtags y palabras silenciadas
- **Kind 10003**: marcadores para notas y contenido direccionable
- **Kind 10007**: relays de búsqueda preferidos
- **Kind 30002**: conjuntos de relays para grupos de relays con nombre
- **Kind 30006**: conjuntos de curación de imágenes
- **Kind 39089**: starter packs para paquetes de seguidos compartibles

Cambios recientes en la especificación movieron los hashtags fuera de los marcadores genéricos hacia conjuntos de intereses, y agregaron kind `30006` para curación de imágenes. Ambos cambios reducen la ambigüedad en cómo los clientes interpretan el contenido de las listas.

---

**Fuentes primarias:**
- [Especificación NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md)

**Mencionado en:**
- [Boletín #1: Actualizaciones de NIP](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Boletín #2: Actualizaciones de NIP](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Boletín #4: NIP Deep Dive](/en/newsletters/2026-01-13-newsletter/#nip-deep-dive-nip-51-and-nip-65)
- [Boletín #8: njump agrega soporte NIP-51](/en/newsletters/2026-02-04-newsletter/#njump)

**Ver también:**
- [NIP-02: Lista de seguidos](/es/topics/nip-02/)
