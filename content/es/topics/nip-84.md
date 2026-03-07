---
title: "NIP-84: Highlights"
date: 2026-02-18
translationOf: /en/topics/nip-84.md
translationDate: 2026-03-07
draft: false
categories:
  - Content
  - Protocol
---

NIP-84 define eventos "highlight" kind 9802 que permiten a los usuarios marcar y compartir pasajes que encuentran valiosos en contenido de formato largo en Nostr.

## Cómo Funciona

El campo `.content` contiene el texto resaltado. Los eventos referencian su material fuente usando etiquetas `a` o `e` para contenido nativo de Nostr, o etiquetas `r` para URLs externas (los clientes deben eliminar los parámetros de seguimiento). Las etiquetas `p` opcionales atribuyen a los autores originales, y una etiqueta `context` opcional proporciona el texto circundante cuando el highlight es una porción de un pasaje más largo.

Para medios no textuales, el contenido del highlight puede estar vacío. Eso da a los clientes una forma de apuntar a un highlight de audio o video manteniendo la referencia de la fuente en las etiquetas.

## Highlights con Cita

Los usuarios pueden añadir una etiqueta `comment` para crear highlights con cita, que se renderizan como reposts citados. Esto evita entradas duplicadas en clientes de microblogging. Dentro de los comentarios, las menciones con etiqueta `p` requieren un atributo "mention" para distinguirlas de las atribuciones de autor/editor, y las URLs con etiqueta `r` usan un atributo "source" para referencias de origen.

## Por Qué Importa

NIP-84 separa el pasaje resaltado de la discusión que lo rodea. Un cliente puede renderizar el texto seleccionado como el objeto principal, y luego tratar el comentario como metadatos opcionales en lugar de mezclar ambos en una nota regular.

Eso es útil para herramientas de lectura e investigación porque preserva el extracto exacto. Dos lectores pueden comentar sobre el mismo artículo y aún producir eventos de highlight portables que otros clientes entienden.

## Notas de Interoperabilidad

Las etiquetas de atribución son más importantes de lo que parecen. Una etiqueta `p` con un rol `author` o `editor` le dice a los clientes quién creó el material fuente, mientras que un rol `mention` dentro de un comentario de cita significa algo diferente. Si los clientes colapsan esos casos juntos, pueden etiquetar mal la fuente resaltada o notificar incorrectamente a personas.

---

**Fuentes primarias:**
- [Especificación NIP-84](https://github.com/nostr-protocol/nips/blob/master/84.md)

**Mencionado en:**
- [Newsletter #10: Lanzamientos](/en/newsletters/2026-02-18-newsletter/#prism-share-anything-to-nostr-from-android)

**Ver también:**
- [NIP-94: Metadatos de Archivos](/es/topics/nip-94/)
