---
title: "NIP-84: Highlights"
date: 2026-02-18
translationOf: /en/topics/nip-84.md
translationDate: 2026-02-18
draft: false
categories:
  - Content
  - Protocol
---

NIP-84 define eventos "highlight" kind 9802 que permiten a los usuarios marcar y compartir pasajes que encuentran valiosos en contenido de formato largo en Nostr.

## Cómo Funciona

El campo `.content` contiene el texto resaltado. Los eventos referencian su material fuente usando etiquetas `a` o `e` para contenido nativo de Nostr, o etiquetas `r` para URLs externas (los clientes deben eliminar los parámetros de seguimiento). Las etiquetas `p` opcionales atribuyen a los autores originales, y una etiqueta `context` opcional proporciona el texto circundante cuando el highlight es una porción de un pasaje más largo.

## Highlights con Cita

Los usuarios pueden añadir una etiqueta `comment` para crear highlights con cita, que se renderizan como reposts citados. Esto evita entradas duplicadas en clientes de microblogging. Dentro de los comentarios, las menciones con etiqueta `p` requieren un atributo "mention" para distinguirlas de las atribuciones de autor/editor, y las URLs con etiqueta `r` usan un atributo "source" para referencias de origen.

---

**Fuentes primarias:**
- [Especificación NIP-84](https://github.com/nostr-protocol/nips/blob/master/84.md)

**Mencionado en:**
- [Boletín #10: Lanzamientos](/es/newsletters/2026-02-18-newsletter/#prism-comparte-cualquier-cosa-en-nostr-desde-android)

**Ver también:**
- [NIP-94: File Metadata](/es/topics/nip-94/)
