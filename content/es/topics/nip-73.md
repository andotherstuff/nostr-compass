---
title: "NIP-73: Identificadores de contenido externo"
date: 2026-02-04
draft: false
categories:
  - Protocol
  - Discovery
  - Metadata
translationOf: /en/topics/nip-73.md
translationDate: 2026-11-05
---

NIP-73 define una forma estándar de hacer referencia a contenido externo dentro de eventos de Nostr. Usa etiquetas `i` para el propio identificador y etiquetas `k` para el tipo de identificador. Así, los clientes pueden agrupar la conversación en torno a un mismo libro, sitio web, episodio de pódcast, ubicación, hashtag u objeto de blockchain. La [especificación actual](https://github.com/nostr-protocol/nips/blob/master/73.md) está marcada como borrador y opcional.

## Cómo funciona {#how-it-works}

Un evento que usa NIP-73 incluye una etiqueta `i` con un identificador externo normalizado y una etiqueta `k` que indica la familia del identificador. Los clientes pueden consultar a los relays por un único tema exacto mediante `i` o por una familia entera mediante `k`. NIP-73 no añade ningún kind de evento propio. Las etiquetas van en comentarios, reseñas y otros eventos.

Fragmento de etiquetas, no un evento completo:

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

Una página web pone su URL normalizada en `i` y asigna `web` a `k`. La especificación cubre varias familias de identificadores, entre ellas:

- URLs web normalizadas sin fragmento
- ISBN para libros
- ISAN para películas
- DOI
- geohashes y códigos ISO 3166 de país o de subdivisión
- GUID de feeds, episodios y editores de pódcast
- hashtags
- identificadores de transacciones y direcciones de blockchain

## Reglas de normalización {#normalization-rules}

La coincidencia depende de que las cadenas sean idénticas, así que la especificación fija una única forma escrita para cada familia. Algunos ejemplos de la especificación:

- los geohashes usan `geo:<value>` y deben ir en minúsculas
- los códigos de país y de subdivisión usan `iso3166:<code>` y deben ir en mayúsculas
- los ISBN se escriben sin guiones
- los DOI van en minúsculas
- las URLs web se escriben sin fragmentos
- los hashes de transacciones de blockchain usan hexadecimal en minúsculas

La normalización fija cómo se escribe un único identificador. No fusiona alias. Los ISBN de cada edición y las URLs que se normalizan en cadenas distintas siguen siendo identificadores separados, de modo que la conversación sobre un mismo libro o artículo puede seguir repartida entre varios valores `i`.

## Pistas de URL {#url-hints}

Una etiqueta `i` puede incluir una pista de URL opcional como tercer elemento del array, es decir, el segundo valor después del nombre de la etiqueta. Un cliente sin un renderizador propio para ese tipo de identificador puede usar la pista como enlace de respaldo.

Fragmento de etiqueta: `["i", "isbn:9780765382030", "<url-hint>"]`

La pista la elige el autor. No forma parte de la identidad, no demuestra ninguna propiedad y no designa un sitio canónico.

## Confianza y contexto {#trust-and-context}

Dos eventos con el mismo identificador acaban en la misma conversación, y el identificador compartido no establece nada más. Un evento firmado identifica a su autor. No autentica el libro, el sitio ni el editor del pódcast al que hace referencia, ni muestra quién los controla.

El significado de una etiqueta `i` depende del evento. En los comentarios de [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md), `I`/`K` en mayúsculas marcan el ámbito raíz y `i`/`k` en minúsculas marcan el padre. Esa estructura de hilo procede de NIP-22, y NIP-73 no define ningún kind de comentario. [NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md) usa `i` para identidades externas en perfiles, así que no toda etiqueta `i` es un tema de NIP-73.

Las afirmaciones de confianza (Trusted Assertions) de [NIP-85](/es/topics/nip-85/) también pueden apuntar a identificadores de NIP-73 como libros, sitios web, hashtags y ubicaciones.

## Implementaciones {#implementations}

El [nip73.rs de rust-nostr en el commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) convierte los prefijos conocidos en un `ExternalContentId` tipado y transforma una pista opcional en una URL tipada. Solo escribe el tercer elemento de la etiqueta cuando hay una pista. Sus tests conservan ISBN con guiones: el parser quita el prefijo y guarda el resto sin aplicar la normalización de la especificación, así que el análisis tipado no garantiza cadenas canónicas. Deja los IDs de cadena fuera de la familia y asigna `ethereum:100:tx:<hash>` a `ethereum:tx`. Esa revisión no tiene variante de país `iso3166`.

El [DisplayExternalId.kt de Amethyst en el commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) envía los identificadores de geohash, hashtag y URL a vistas específicas y muestra los demás tipos compatibles como un chip de ámbito genérico. Una URL abre la ruta de hilo propia de la app para esa página. Con las vistas previas desactivadas, el renderizado normal muestra un chip de enlace simple y no solicita ninguna vista previa. Con las vistas previas activadas, obtener una vista previa que falta puede implicar contactar con el sitio de destino. Ninguno de los dos archivos muestra cómo se comporta una versión publicada.

---

**Fuentes primarias:**
- [Especificación de NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Añade códigos ISO 3166 de país y de subdivisión
- [nip73.rs de rust-nostr en el commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs)
- [DisplayExternalId.kt de Amethyst en el commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt)

**Mencionado en:**
- [Boletín #47: Análisis a fondo de NIP](/es/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)
- [Boletín #45](/en/newsletters/2026-10-21-newsletter/#feather)
- [Boletín #43](/en/newsletters/2026-10-07-newsletter/#protocol-and-spec-work)
- [Boletín #37: agosto de 2025](/en/newsletters/2026-08-26-newsletter/#august-2025)
- [Boletín #8: Actualizaciones de NIPs](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [Boletín #10: Análisis a fondo de NIP-85](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Boletín #36: Comentarios (NIP-22)](/en/newsletters/2026-08-19-newsletter/#comments-nip-22)
- [Boletín #38: Análisis a fondo de NIP](/en/newsletters/2026-09-02-newsletter/#reactions-nip-25)
- [Boletín #40: filtros de medio de pódcast de NIP-73](/en/newsletters/2026-09-16-newsletter/#nip-73-proposes-podcast-medium-filters)
- [Boletín #42: contenido externo de septiembre de 2024](/en/newsletters/2026-09-30-newsletter/#september-2024-posts-acquire-richer-context)

**Véase también:**
- [NIP-31: Gestión de kinds de evento desconocidos](/es/topics/nip-31/)
- [NIP-22: Comentario](/es/topics/nip-22/)
- [NIP-39: Identidades externas en perfiles](/es/topics/nip-39/)
- [NIP-85: Afirmaciones de confianza (Trusted Assertions)](/es/topics/nip-85/)
